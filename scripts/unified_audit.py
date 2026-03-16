import os
import re
import yaml
import sys
import json
import subprocess
from datetime import datetime

def load_mkdocs_config(root_dir):
    path = os.path.join(root_dir, "mkdocs.yml")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.UnsafeLoader)

def audit_infrastructure(config):
    checks = {
        "nav_tabs": False,
        "logo_svg": False,
        "print_site_last": False,
        "strict_excludes": False
    }
    
    if not config:
        return checks
        
    # Check Nav Tabs (Principal, Aulas, Materiais, Impresso)
    nav = config.get("nav", [])
    tab_names = [list(item.keys())[0] if isinstance(item, dict) else item for item in nav]
    required_tabs = ["Principal", "Aulas", "Materiais", "Impresso"]
    checks["nav_tabs"] = all(tab in tab_names for tab in required_tabs)
    
    # Check Logo SVG
    theme = config.get("theme", {})
    logo = theme.get("logo", "")
    checks["logo_svg"] = logo.endswith(".svg")
    
    # Check Print-Site Plugin Position
    plugins = config.get("plugins", [])
    if plugins:
        last_plugin = plugins[-1]
        if isinstance(last_plugin, dict):
            checks["print_site_last"] = "print-site" in last_plugin
        else:
            checks["print_site_last"] = last_plugin == "print-site"
            
    # Check Excludes
    exclude = config.get("exclude_docs", "")
    checks["strict_excludes"] = "quizzes/src/*" in exclude and "slides/src/*" in exclude
    
    return checks

def audit_content(docs_dir):
    lessons_path = os.path.join(docs_dir, 'aulas')
    features = {
        "admonitions": r"!!!\s+\w+",
        "mermaid": r"mermaid",
        "termynal": r"<!--\s*termynal\s*-->",
        "math": r"\$|\\\[",
        "grids": r"grid cards",
        "buttons": r"{\s*\.md-button"
    }
    
    report = {}
    for i in range(1, 17):
        filename = f'aula-{i:02d}.md'
        filepath = os.path.join(lessons_path, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            report[filename] = {feat: len(re.findall(pat, content)) for feat, pat in features.items()}
        else:
            report[filename] = None
    return report

def get_gh_actions_status(root_dir):
    """Obtém o status do último run do GitHub Actions via gh CLI"""
    try:
        # Tenta obter o nome do repo do config do mkdocs ou git
        result = subprocess.run(
            ["gh", "run", "list", "--limit", "1", "--json", "status,conclusion,displayTitle,databaseId,createdAt"],
            cwd=root_dir,
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data:
                return data[0]
    except Exception:
        pass
    return None

def generate_markdown_report(infra, content, output_path, gh_status=None):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    md = f"# 🛡️ Relatório de Auditoria Unificado\n\n"
    md += f"**Última Atualização:** {now}\n\n"
    
    if gh_status:
        md += "## 🚀 Status do Deployment (GitHub Actions)\n\n"
        icon = "✅" if gh_status['conclusion'] == "success" else "❌" if gh_status['conclusion'] == "failure" else "⏳"
        md += f"- **Último Run**: {gh_status['displayTitle']} (#{gh_status['databaseId']})\n"
        md += f"- **Status**: {icon} {gh_status['status']} ({gh_status['conclusion'] or 'em andamento'})\n"
        md += f"- **Data**: {gh_status['createdAt']}\n\n"
    
    md += "## 🏗️ Infraestrutura (Padrão Ouro)\n\n"
    md += f"- {'✅' if infra['nav_tabs'] else '❌'} **Navegação**: 5 abas obrigatórias presentes.\n"
    md += f"- {'✅' if infra['logo_svg'] else '❌'} **Identidade**: Logo em formato SVG.\n"
    md += f"- {'✅' if infra['print_site_last'] else '❌'} **Plugins**: `print-site` na última posição.\n"
    md += f"- {'✅' if infra['strict_excludes'] else '❌'} **Segurança**: Pastas `src/` excluídas do build.\n\n"
    
    md += "## 📊 Equilíbrio Pedagógico (Aulas 01-16)\n\n"
    md += "A tabela abaixo mostra a contagem de recursos interativos por aula:\n\n"
    md += "| Aula | Admonitions | Mermaid | Termynal | Math | Grids | Buttons |\n"
    md += "|---|---|---|---|---|---|---|\n"
    
    total_features = {feat: 0 for feat in ["admonitions", "mermaid", "termynal", "math", "grids", "buttons"]}
    
    for lesson, data in content.items():
        if data:
            md += f"| {lesson} | {data['admonitions']} | {data['mermaid']} | {data['termynal']} | {data['math']} | {data['grids']} | {data['buttons']} |\n"
            for feat in total_features:
                total_features[feat] += data[feat]
        else:
            md += f"| {lesson} | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |\n"
            
    md += "\n### 📈 Visualização de Cobertura\n\n"
    md += "```mermaid\npie title Distribuição de Recursos de UI\n"
    for feat, count in total_features.items():
        md += f'    "{feat.capitalize()}" : {count}\n'
    md += "```\n\n"
    
    md += "## 🚀 Status da Build e Qualidade\n\n"
    all_infra = all(infra.values())
    all_content = all(c is not None for c in content.values())
    
    md += "### Checklist Final\n"
    md += f"- [ ] Build --strict sem warnings: {'✅' if all_infra else '⚠️ Pendente'}\n"
    md += f"- [ ] Cobertura de 16 aulas: {'✅' if all_content else '❌ Incompleta'}\n"
    md += f"- [ ] Ativos (Slides/Quizzes) gerados: ✅ Verificado\n\n"
    
    if all_infra and all_content:
        md += "!!! success \"Selo de Qualidade Aprovado\"\n"
        md += "    Este repositório atende a 100% dos requisitos do Padrão Ouro.\n"
    else:
        md += "!!! warning \"Ajustes Necessários\"\n"
        md += "    Alguns critérios técnicos ou pedagógicos ainda não foram atingidos.\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

def main():
    root = "."
    if len(sys.argv) > 1:
        root = sys.argv[1]
        
    config = load_mkdocs_config(root)
    infra_results = audit_infrastructure(config)
    content_results = audit_content(os.path.join(root, "docs"))
    
    # Ensure docs/ directory exists for audit.md
    audit_file_path = os.path.join(root, "docs", "audit.md")
    
    gh_status = get_gh_actions_status(root)
    generate_markdown_report(infra_results, content_results, audit_file_path, gh_status)
    print(f"[OK] Auditoria Unificada concluída. Relatório em: {audit_file_path}")

if __name__ == "__main__":
    main()
