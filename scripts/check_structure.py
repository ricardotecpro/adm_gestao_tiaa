import os
import json
from datetime import datetime

REPOS_ROOT = r"D:\SourceCode\REPOS\github.io"
EXCLUDE_REPOS = ["ricardotecpro", "ricardotecpro.github.io"]
OUTPUT_JSON = r"D:\SourceCode\REPOS\_prompts\logs\structure_audit_results.json"
OUTPUT_MD = r"D:\SourceCode\REPOS\_prompts\logs\structure_audit_report.md"

def check_repo(repo_path):
    repo_name = os.path.basename(repo_path)
    docs_dir = os.path.join(repo_path, "docs")
    aulas_dir = os.path.join(docs_dir, "aulas")
    
    errors = []
    
    # 1. Base dirs
    for d in ["slides", "quizzes", "exercicios", "projetos", "aulas"]:
        if not os.path.isdir(os.path.join(docs_dir, d)):
            errors.append(f"Pasta faltante: docs/{d}")
            
    # 2. Lessons
    if os.path.isdir(aulas_dir):
        lessons = [f for f in os.listdir(aulas_dir) if f.startswith("aula-") and f.endswith(".md")]
        if not lessons:
            errors.append("Nenhuma aula encontrada em docs/aulas")
        for l in lessons:
            if os.path.getsize(os.path.join(aulas_dir, l)) < 50:
                errors.append(f"Aula vazia ou muito pequena: {l}")
    else:
        errors.append("Pasta docs/aulas não existe")
        
    # 3. Hubs (index.md)
    EXPECTED_INDEXES = [
        "index.md",
        "aulas/index.md",
        "exercicios/index.md",
        "projetos/index.md",
        "quizzes/index.md",
        "slides/index.md",
        "setups/index.md"
    ]
    for idx in EXPECTED_INDEXES:
        if not os.path.isfile(os.path.join(docs_dir, idx)):
            errors.append(f"Arquivo faltante: docs/{idx}")

    # 4. Critical Files
    for f in ["materiais.md", "sobre.md", "plano.md"]:
        if not os.path.isfile(os.path.join(docs_dir, f)):
            errors.append(f"Arquivo faltante: docs/{f}")

    status = "PASSED" if not errors else "FAILED"
    return {
        "repo": repo_name,
        "status": status,
        "errors": errors
    }

def main():
    repos = sorted([d for d in os.listdir(REPOS_ROOT) if os.path.isdir(os.path.join(REPOS_ROOT, d)) and d not in EXCLUDE_REPOS])
    results = []
    
    print(f"🚀 Iniciando Auditoria Estrutural Purista em {len(repos)} repositórios...")
    
    for repo in repos:
        repo_path = os.path.join(REPOS_ROOT, repo)
        res = check_repo(repo_path)
        results.append(res)
        print(f"{'✅' if res['status'] == 'PASSED' else '❌'} {res['repo']}")
        
    # Salvar JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
        
    # Relatório MD
    md = f"# 📋 Relatório de Auditoria Estrutural (Ecossistema MkDocs)\n\n"
    md += f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    passed = len([r for r in results if r["status"] == "PASSED"])
    md += f"**Resumo:** {passed}/{len(results)} repositórios em conformidade plena.\n\n"
    
    md += "| Repositório | Status | Falhas Detectadas |\n"
    md += "|---|---|---|\n"
    
    for r in results:
        icon = "✅" if r["status"] == "PASSED" else "❌"
        err_str = "; ".join(r["errors"]) if r["errors"] else "Nenhuma"
        md += f"| {r['repo']} | {icon} | {err_str} |\n"
        
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    
    print(f"\n✅ Auditoria concluída! Relatório em: {OUTPUT_MD}")

if __name__ == "__main__":
    main()
