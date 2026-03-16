"""
Apply footer grid + button to all 16 restored aulas.
"""
import re
from pathlib import Path

aulas_dir = Path(r"D:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\aulas")

AULAS = [
    (1,  "Identificação de Oportunidades",    "aula-02"),
    (2,  "Análise de Valor",                  "aula-03"),
    (3,  "Processo de Inovação",              "aula-04"),
    (4,  "Estratégias e Ideação",             "aula-05"),
    (5,  "Plano de Negócios",                 "aula-06"),
    (6,  "Modelagem Canvas",                  "aula-07"),
    (7,  "Segmentação de Clientes",           "aula-08"),
    (8,  "Proposta de Valor",                 "aula-09"),
    (9,  "Canais de Comunicação",             "aula-10"),
    (10, "Relacionamento com Cliente",        "aula-11"),
    (11, "Atividades-chave",                  "aula-12"),
    (12, "Recursos Essenciais",               "aula-13"),
    (13, "Parcerias Estratégicas",            "aula-14"),
    (14, "Estrutura de Custos",               "aula-15"),
    (15, "Fontes de Receita",                 "aula-16"),
    (16, None,                                None),
]

def make_footer(num: int, proxima_slug: str | None) -> str:
    nn = f"{num:02d}"
    parts = [
        "\n---\n",
        "\n## 🔗 Materiais da Aula\n",
        "\n<div class=\"grid cards\" markdown>\n",
        f"- :material-presentation: **Slides**\n\n"
        f"    ---\n\n"
        f"    Material visual com diagramas e conceitos-chave.\n\n"
        f"    [:octicons-arrow-right-24: Slide {nn}](../slides/slide-{nn}.html)\n",
        f"\n- :material-help-circle: **Quiz**\n\n"
        f"    ---\n\n"
        f"    Teste seu conhecimento com 10 questões interativas.\n\n"
        f"    [:octicons-arrow-right-24: Quiz {nn}](../quizzes/quiz-{nn}.md)\n",
        f"\n- :fontawesome-solid-pencil: **Exercícios**\n\n"
        f"    ---\n\n"
        f"    5 exercícios progressivos (básico → desafio).\n\n"
        f"    [:octicons-arrow-right-24: Exercício {nn}](../exercicios/exercicio-{nn}.md)\n",
        f"\n- :material-briefcase-outline: **Projeto**\n\n"
        f"    ---\n\n"
        f"    Aplicação prática dos conceitos da aula.\n\n"
        f"    [:octicons-arrow-right-24: Projeto {nn}](../projetos/projeto-{nn}.md)\n",
        "\n</div>\n",
    ]
    if proxima_slug:
        next_nn = proxima_slug.split("-")[1]
        parts.append(
            f"\n---\n\n"
            f"[:octicons-arrow-right-24: Avançar para Aula {next_nn}](./{proxima_slug}.md){{ .md-button .md-button--primary }}\n"
        )
    else:
        parts.append(
            "\n---\n\n"
            "!!! success \"Parabéns!\"\n"
            "    Você completou as **16 aulas** do curso! Agora você tem todas as ferramentas\n"
            "    para construir modelos de negócios sólidos, lucrativos e inovadores. 🚀\n\n"
            "[:octicons-arrow-left-24: Voltar à Trilha de Aulas](./index.md){ .md-button .md-button--primary }\n"
        )
    return "".join(parts)

# Old patterns to remove
OLD_PATTERNS = [
    re.compile(r'\n---\n+## 📚 Material Complementar.*', re.DOTALL),
    re.compile(r'\n## 📚 Material Complementar.*', re.DOTALL),
    re.compile(r'\n---\n+## 🔗 Materiais da Aula.*', re.DOTALL),
]

updated = 0
for num, proxima_titulo, proxima_slug in AULAS:
    nn = f"{num:02d}"
    path = aulas_dir / f"aula-{nn}.md"
    if not path.exists():
        print(f"[ERROR] {path} not found!")
        continue
    content = path.read_text(encoding="utf-8")
    new_content = content
    for pat in OLD_PATTERNS:
        new_content, count = pat.subn("", new_content)
        if count:
            break
    new_footer = make_footer(num, proxima_slug)
    new_content = new_content.rstrip() + "\n" + new_footer
    path.write_text(new_content, encoding="utf-8")
    print(f"[OK] aula-{nn}.md")
    updated += 1

print(f"\n[DONE] {updated}/16 aulas updated")
