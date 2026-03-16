import os
import yaml

MKDOCS_PATH = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\mkdocs.yml"

with open(MKDOCS_PATH, "r", encoding="utf-8") as file:
    lines = file.readlines()

new_lines = []
skip_mode = False

for line in lines:
    if line.strip() == "- Exercícios:":
        new_lines.append(line)
        new_lines.append("      - 'Índice': exercicios/index.md\n")
        # generate 16 entries
        for i in range(1, 17):
            n = f"{i:02d}"
            new_lines.append(f"      - 'Aula {n}':\n")
            new_lines.append(f"          - 'Exercícios': exercicios/exercicio-{n}.md\n")
            new_lines.append(f"          - 'Solução': exercicios/solucao-{n}.md\n")
        skip_mode = True
        continue
    
    if skip_mode:
        if line.strip().startswith("- Projetos:"):
            skip_mode = False
            new_lines.append(line)
        continue
        
    if not skip_mode:
        new_lines.append(line)

with open(MKDOCS_PATH, "w", encoding="utf-8") as file:
    file.writelines(new_lines)
    
print("mkdocs.yml atualizado com a arvore de navegacao de solucoes.")
