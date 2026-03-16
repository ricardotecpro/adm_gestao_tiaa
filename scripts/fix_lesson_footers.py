import os
import re

LESSONS_DIR = r"d:\SourceCode\REPOS\github.io\ads_mod_02_logica_e_algoritmos\docs\aulas"

lesson_titles = {
    1: "Algoritmos",
    2: "Ambiente",
    3: "Estrutura Sequencial",
    4: "Estrutura Condicional",
    5: "Estruturas Repetitivas",
    6: "Vetores",
    7: "Matrizes",
    8: "Funções",
    9: "C / C++",
    10: "JS / TS",
    11: "Java",
    12: ".NET",
    13: "Python",
    14: "Rust / Go",
    15: "Mobile",
    16: "PHP"
}

def get_footer(num):
    next_num = num + 1
    num_str = f"{num:02d}"
    next_num_str = f"{next_num:02d}"
    
    footer = f'''
---

## 🔗 Materiais da Aula

<div class="grid cards" markdown>
- :material-presentation: **Slides**

    ---

    Material visual com diagramas e conceitos-chave.

    [:octicons-arrow-right-24: Slide {num_str}](../slides/slide-{num_str}.html)

- :material-help-circle: **Quiz**

    ---

    Teste seu conhecimento com 10 questões interativas.

    [:octicons-arrow-right-24: Quiz {num_str}](../quizzes/quiz-{num_str}.md)

- :fontawesome-solid-pencil: **Exercícios**

    ---

    5 exercícios progressivos (básico → desafio).

    [:octicons-arrow-right-24: Exercício {num_str}](../exercicios/exercicio-{num_str}.md)

- :material-briefcase-outline: **Projeto**

    ---

    Aplicação prática dos conceitos da aula.

    [:octicons-arrow-right-24: Projeto {num_str}](../projetos/projeto-{num_str}.md)

</div>

---
'''
    if num < 16:
        next_name = lesson_titles.get(next_num, "Próxima")
        footer += f'\n[➡️ Próxima Aula: {next_name}](./aula-{next_num_str}.md){{ .md-button .md-button--primary }}\n'
    else:
        footer += '\n!!! success "Parabéns!"\n    Você concluiu todas as aulas deste curso!\n\n[🏆 Voltar à Trilha de Aulas](./index.md){ .md-button .md-button--primary }\n'
    
    return footer

for i in range(1, 17):
    filename = f"aula-{i:02d}.md"
    filepath = os.path.join(LESSONS_DIR, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Fix links (directory style to .html)
        content = re.sub(r'\((\.\.\/)?slides\/slide-(\d+)\.md\)', r'(\1slides/slide-\2.html)', content)
        
        # 2. Add footer
        if "## 🔗 Materiais da Aula" in content:
            content = content.split("## 🔗 Materiais da Aula")[0].rstrip()
            if content.endswith("---"):
                content = content[:-3].rstrip()
        
        new_content = content.rstrip() + "\n" + get_footer(i)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipping {filename} (not found)")
