import os

TARGET_REPOS = [
    r"D:\SourceCode\REPOS\github.io\ads_extra_redes_e_internet",
    r"D:\SourceCode\REPOS\github.io\ads_mod_09_estruturas_de_dados",
    r"D:\SourceCode\REPOS\github.io\ads_spec_backend_com_java"
]

def generate_index(repo_path):
    aulas_dir = os.path.join(repo_path, "docs", "aulas")
    index_path = os.path.join(aulas_dir, "index.md")
    
    # Procura por arquivos aula-XX.md
    files = sorted([f for f in os.listdir(aulas_dir) if f.startswith("aula-") and f.endswith(".md")])
    if not files:
        print(f"  [SKIP] No lessons found in {aulas_dir}")
        return

    content = "# Conteúdo das Aulas\n\n"
    content += '<div class="grid cards" markdown>\n\n'
    
    for f in files:
        try:
            num = int(f.split("-")[1].split(".")[0])
        except:
            num = 1
            
        # Ícone
        if num <= 10:
            icon = f":material-numeric-{num}-box:"
        elif num == 11: icon = ":material-memory:"
        elif num == 12: icon = ":material-chip:"
        elif num == 13: icon = ":material-expansion-card-variant:"
        elif num == 14: icon = ":material-usb:"
        elif num == 15: icon = ":material-matrix:"
        else: icon = ":material-rocket-launch:"
            
        content += f"-   {icon}{{ .lg .middle }} __Aula {num:02d}__\n"
        content += f"    [:material-arrow-right: Ver conteúdo]({f})\n\n"
        
    content += "</div>\n"
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] Generated {index_path}")

for repo in TARGET_REPOS:
    generate_index(repo)
