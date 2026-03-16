
import os
import re

BASE_DIR = r"D:\SourceCode\REPOS\github.io"
EXCLUDE = ["ricardotecpro", "ricardotecpro.github.io"]
KEYWORDS = ["ads", "adm", "gestao", "mod", "spec", "proj", "extra"]
SUBJECTS = [
    "computacao", "logica", "interfaces", "html", "css", "javascript", "js",
    "git", "github", "backend", "apis", "sql", "nosql", "dados", "design",
    "qualidade", "testes", "devops", "cloud", "engenharia", "mobile", "ia",
    "linux", "mcp", "c", "cpp", "rust", "typescript", "dmn", "tiaa", "uml",
    "ferramentas", "hardware", "redes", "internet", "bi", "dashboards"
]

def analyze_repos():
    repos = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d not in EXCLUDE]
    repos = repos[:50]
    
    report = []
    
    for repo in repos:
        repo_path = os.path.join(BASE_DIR, repo)
        status = "MATCH"
        reasons = []
        
        # 1. Name Analysis
        words = re.split(r'[_ -]', repo.lower())
        has_keyword = any(kw in words for kw in KEYWORDS)
        has_subject = any(sub in words for sub in SUBJECTS)
        
        if not (has_keyword or has_subject):
            status = "DIVERGENT"
            reasons.append("Name does not match theme keywords")
            
        # 2. Content Analysis
        readme_path = os.path.join(repo_path, "README.md")
        docs_index = os.path.join(repo_path, "docs", "index.md")
        plano_paths = [
            os.path.join(repo_path, "docs", "plano.md"),
            os.path.join(repo_path, "docs", "plano-de-ensino.md")
        ]
        
        files_found = []
        if os.path.exists(readme_path): files_found.append("README.md")
        if os.path.exists(docs_index): files_found.append("docs/index.md")
        for p in plano_paths:
            if os.path.exists(p):
                files_found.append(os.path.basename(p))
                
        if not files_found:
            status = "DIVERGENT"
            reasons.append("No core content files found (README, index, plano)")
            
        report.append({
            "repo": repo,
            "status": status,
            "reasons": reasons,
            "files": files_found
        })
        
    return report

if __name__ == "__main__":
    results = analyze_repos()
    print("# Repository Analysis Report\n")
    print("| Repository | Status | Reasons | Files Found |")
    print("|------------|--------|---------|-------------|")
    for r in results:
        res_str = ", ".join(r["reasons"]) if r["reasons"] else "N/A"
        files_str = ", ".join(r["files"])
        print(f"| {r['repo']} | {r['status']} | {res_str} | {files_str} |")
