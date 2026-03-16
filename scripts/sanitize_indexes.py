import os
import glob

# Files to sanitize
ROOT = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs"
index_files = glob.glob(os.path.join(ROOT, "**/index.md"), recursive=True)
index_files.extend([
    os.path.join(ROOT, "sobre.md"),
    os.path.join(ROOT, "plano.md"),
    os.path.join(ROOT, "project_roadmap.md"),
    os.path.join(ROOT, "materiais.md"),
])

replace_map = {
    "Mobile Nativo": "Modelos de Negócios",
    "mobile nativo": "modelos de negócios",
    "desenvolvimento mobile": "desenvolvimento de produtos e gestão",
    "O Desenvolvedor Mobile": "O Empreendedor Ágil",
    "iOS e Android": "Validação e Receitas",
    "plano-ensino": "plano",
}

for fpath in index_files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        for old, new in replace_map.items():
            if old in content:
                content = content.replace(old, new)
                modified = True
                
        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
                
print("Sanitization completed on root and index files.")
