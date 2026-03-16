import os
import re
import yaml
import json
import csv
from datetime import datetime

# Configurações
REPOS_ROOT = r"D:\SourceCode\REPOS\github.io"
EXCLUDE_REPOS = ["ricardotecpro", "ricardotecpro.github.io"]
OUTPUT_CSV = r"D:\SourceCode\REPOS\_prompts\logs\bulk_audit_results.csv"
OUTPUT_MD = r"D:\SourceCode\REPOS\_prompts\logs\bulk_audit_report.md"

def load_yaml(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.SafeLoader)
    except:
        # Fallback para tags customizadas do MkDocs
        try:
            class IgnoreUndefinedLoader(yaml.SafeLoader):
                def construct_undefined(self, node):
                    return None
            IgnoreUndefinedLoader.add_constructor(None, IgnoreUndefinedLoader.construct_undefined)
            with open(path, "r", encoding="utf-8") as f:
                return yaml.load(f, Loader=IgnoreUndefinedLoader)
        except:
            return "ERROR"

def check_grid_vulnerability(content):
    """Verifica se há headers ## ou ### dentro de uma div de grid cards."""
    grid_blocks = re.findall(r'<div class="grid cards".*?<\/div>', content, re.DOTALL)
    for block in grid_blocks:
        if re.search(r'^#{2,3}\s+', block, re.MULTILINE):
            return True
    return False

def check_lesson_icons(content):
    """Verifica se aulas 11-16 usos ícones numéricos (erro) ou temáticos (sucesso)."""
    # Procura por padrões como :material-numeric-11:
    bad_icons = re.findall(r':material-numeric-(1[1-6]):', content)
    return len(bad_icons) == 0

def audit_repo(repo_path):
    repo_name = os.path.basename(repo_path)
    mkdocs_path = os.path.join(repo_path, "mkdocs.yml")
    pyproject_path = os.path.join(repo_path, "pyproject.toml")
    index_path = os.path.join(repo_path, "docs", "index.md")
    aulas_index_path = os.path.join(repo_path, "docs", "aulas", "index.md")
    
    results = {
        "repo": repo_name,
        "mkdocs_yml": os.path.exists(mkdocs_path),
        "pyproject_toml": os.path.exists(pyproject_path),
        "gold_tabs": False,
        "print_site": False,
        "grid_index": False,
        "grid_error": False,
        "icons_ok": False,
        "mailmap": os.path.exists(os.path.join(repo_path, ".mailmap")),
        "score": 0
    }
    
    # 1. Analisar MkDocs.yml
    config = load_yaml(mkdocs_path)
    if isinstance(config, dict):
        # Tabs
        nav = config.get("nav", [])
        tab_names = [list(item.keys())[0] if isinstance(item, dict) else str(item) for item in nav]
        required_tabs = ["Principal", "Aulas", "Materiais", "Impresso"]
        results["gold_tabs"] = all(tab in tab_names for tab in required_tabs)
        
        # Plugins
        plugins = config.get("plugins", [])
        results["print_site"] = any("print-site" in str(p) for p in plugins)
        
    # 2. Analisar index.md (Grid)
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
            results["grid_index"] = "grid cards" in content
            results["grid_error"] = check_grid_vulnerability(content)
            
    # 3. Analisar aulas/index.md (Icons)
    if os.path.exists(aulas_index_path):
        with open(aulas_index_path, "r", encoding="utf-8") as f:
            content = f.read()
            results["icons_ok"] = check_lesson_icons(content)
    
    # Cálculo de Score Simples (0 a 100)
    metrics = ["mkdocs_yml", "pyproject_toml", "gold_tabs", "print_site", "grid_index", "icons_ok", "mailmap"]
    weights = {"mkdocs_yml": 10, "pyproject_toml": 10, "gold_tabs": 20, "print_site": 15, "grid_index": 15, "icons_ok": 20, "mailmap": 10}
    
    current_score = 0
    for m in metrics:
        if results[m]:
            current_score += weights[m]
    
    # Penalizar erro de grid
    if results["grid_error"]:
        current_score -= 10
        
    results["score"] = max(0, current_score)
    return results

def main():
    print(f"🚀 Iniciando Auditoria Massiva em {REPOS_ROOT}...")
    all_results = []
    
    repos = [d for d in os.listdir(REPOS_ROOT) if os.path.isdir(os.path.join(REPOS_ROOT, d)) and d not in EXCLUDE_REPOS]
    
    for repo in repos:
        path = os.path.join(REPOS_ROOT, repo)
        print(f"[AUDIT] {repo}...", end="\r")
        all_results.append(audit_repo(path))
    
    # Salvar CSV
    keys = all_results[0].keys()
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_results)
        
    # Salvar Markdown Report
    all_results.sort(key=lambda x: x["score"], reverse=True)
    
    md = "# 📋 Relatório de Auditoria Global — Ecossistema MkDocs\n\n"
    md += f"**Data:** {datetime.now().strftime('%Y-%m-%d')}\n"
    md += f"**Total de Repositórios:** {len(all_results)}\n\n"
    
    md += "| Repositório | Score | Tabs | Icons | Grid | Print | .mailmap |\n"
    md += "|---|---|---|---|---|---|---|\n"
    
    for r in all_results:
        status_tabs = "✅" if r["gold_tabs"] else "❌"
        status_icons = "✅" if r["icons_ok"] else "⚠️"
        status_grid = "❌" if r["grid_error"] else ("✅" if r["grid_index"] else "⚪")
        status_print = "✅" if r["print_site"] else "❌"
        status_mail = "✅" if r["mailmap"] else "❌"
        
        md += f"| {r['repo']} | **{r['score']}** | {status_tabs} | {status_icons} | {status_grid} | {status_print} | {status_mail} |\n"
        
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    
    print(f"\n✅ Auditoria concluída!")
    print(f"📊 Relatório CSV: {OUTPUT_CSV}")
    print(f"📄 Relatório Markdown: {OUTPUT_MD}")

if __name__ == "__main__":
    main()
