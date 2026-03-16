import os
import subprocess
import json
import csv
from datetime import datetime

# Configurações
REPOS_ROOT = r"D:\SourceCode\REPOS\github.io"
EXCLUDE_REPOS = ["ricardotecpro", "ricardotecpro.github.io"]
OUTPUT_JSON = r"D:\SourceCode\REPOS\_prompts\logs\bulk_test_results.json"
OUTPUT_MD = r"D:\SourceCode\REPOS\_prompts\logs\bulk_test_report.md"

import sys

def save_results(results):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

def run_test(repo_path, test_target="."):
    repo_name = os.path.basename(repo_path)
    print(f"🧪 Testando: {repo_name}...", end=" ", flush=True)
    
    try:
        # Usa o mesmo interpretador do processo pai para garantir dependências
        cmd = [sys.executable, "-m", "pytest", test_target]
        result = subprocess.run(
            cmd,
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=60 # Reduzi timeout para 1 minuto se for estrutural
        )
        
        status = "PASSED" if result.returncode == 0 else "FAILED"
        print(status)
        return {
            "repo": repo_name,
            "status": status,
            "exit_code": result.returncode,
            "error_msg": (result.stdout + "\n" + result.stderr).strip() if status == "FAILED" else ""
        }
    except subprocess.TimeoutExpired:
        print("TIMEOUT")
        return {"repo": repo_name, "status": "TIMEOUT", "exit_code": -1, "error_msg": "Timeout atingido"}
    except Exception as e:
        print("ERROR")
        return {"repo": repo_name, "status": "ERROR", "exit_code": -1, "error_msg": str(e)}

def main():
    repos = sorted([d for d in os.listdir(REPOS_ROOT) if os.path.isdir(os.path.join(REPOS_ROOT, d)) and d not in EXCLUDE_REPOS])
    
    all_results = []
    
    # Podemos passar o alvo do teste via argumento ou fixar estrutural primeiro
    test_target = "tests/test_course_structure.py" 
    
    print(f"🚀 Iniciando Validação Técnica Global (Alvo: {test_target})")
    print(f"Total: {len(repos)} repositórios")
    
    for repo in repos:
        repo_path = os.path.join(REPOS_ROOT, repo)
        if not os.path.exists(os.path.join(repo_path, "tests")):
            print(f"⏩ {repo}: Pulado (Sem pasta 'tests')")
            continue
            
        res = run_test(repo_path, test_target)
        all_results.append(res)
        save_results(all_results)
            
    # Gerar Relatório Markdown
    md = f"# 🏁 Relatório de Testes Globais (Ecossistema MkDocs)\n\n"
    md += f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    md += f"**Total de Repos Testados:** {len(all_results)}\n\n"
    
    passed = len([r for r in all_results if r["status"] == "PASSED"])
    failed = len([r for r in all_results if r["status"] == "FAILED"])
    others = len(all_results) - passed - failed
    
    md += f"- ✅ **Passaram**: {passed}\n"
    md += f"- ❌ **Falharam**: {failed}\n"
    md += f"- ⚠️ **Erro/Timeout**: {others}\n\n"
    
    md += "| Repositório | Status | Detalhes |\n"
    md += "|---|---|---|\n"
    
    for r in all_results:
        icon = "✅" if r["status"] == "PASSED" else "❌" if r["status"] == "FAILED" else "⚠️"
        msg = str(r.get("error_msg", ""))
        safe_msg = msg[:100].replace("\n", " ")
        md += f"| {r['repo']} | {icon} {r['status']} | {safe_msg} |\n"
        
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    
    print(f"\n✅ Testes concluídos! Relatório em: {OUTPUT_MD}")

if __name__ == "__main__":
    main()
