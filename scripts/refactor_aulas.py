import os
import re
import json

AULAS_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\aulas"

def load_intermediate_content():
    json_path = os.path.join(os.path.dirname(__file__), "content_overlay.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

intermediate_content = load_intermediate_content()

for i in range(1, 17):
    num_str = f"{i:02d}"
    file_path = os.path.join(AULAS_DIR, f"aula-{num_str}.md")
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Re-number and inject
    content = content.replace("## 7. Exercício", "## 8. Exercício")
    content = content.replace("## 6. Mini-Projeto", "## 7. Mini-Projeto")
    
    intro = intermediate_content.get(num_str, "")
    intro = intro.replace("X", "6")
    
    # insert intro
    if "## 7. Mini-Projeto" in content:
        content = content.replace("## 7. Mini-Projeto", intro + "## 7. Mini-Projeto")
        
    links = f"\n---\n\n## 📚 Material Complementar\n\n*   **[📝 Exercícios da Aula {num_str}](../exercicios/exercicio-{num_str}.md)**: Pratique os conceitos com questões focadas.\n*   **[🚀 Projeto da Aula {num_str}](../projetos/projeto-{num_str}.md)**: Aplique o conhecimento em um desafio prático de nível intermediário.\n\n"
    
    # insert links
    if "**Próxima Aula**" in content:
        content = content.replace("**Próxima Aula**", links + "**Próxima Aula**")
    elif "!!! warning \"Atenção\"" in content and "**FIM DO CURSO**" not in content:
        content = content.replace("!!! warning \"Atenção\"", links + "!!! warning \"Atenção\"")
    elif "!!! success \"Conclusão do Módulo\"" in content:
        content = content.replace("!!! success \"Conclusão do Módulo\"", links + "!!! success \"Conclusão do Módulo\"")
    elif "**FIM DO CURSO**" in content:
        content = content.replace("**FIM DO CURSO**", links + "**FIM DO CURSO**")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Aulas refatoradas com sucesso!")
