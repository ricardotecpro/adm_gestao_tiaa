import os
import re

projects_dir = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\projetos"

old_objective = r"Este projeto visa aplicar todo o rigor e as ferramentas discutidas na \[Aula (\d+)\]\(\.\./aulas/aula-\d+\.md\) em um cenário de negócios do mundo real\. Você deixará o plano das ideias para a simulação ou aplicação tangível e prática\."
new_objective = r"Neste projeto, você aplicará os conceitos da [Aula \1](../aulas/aula-\1.md) em um cenário prático. O objetivo é transformar a teoria em uma entrega tangível que simula a realidade do mercado."

old_requirements = r"Para obter êxito neste nível intermediário, certifique-se de apresentar:\n\n1\.  \*\*Fundamentação\*\*: Aplicação clara e documentada do conceito\.\n2\.  \*\*Dados Evidenciados\*\*: Planilhas, textos focados ou gráficos que representem clareza analítica das métricas e não suposições cegas\.\n3\.  \*\*Registro de Insights\*\*: Um breve parágrafo documentando as dificuldades encontradas nesta simulação \(mitiga o risco de errar com dinheiro verdadeiro no futuro\)\."
new_requirements = r"Para concluir este desafio com sucesso, sua entrega deve conter:\n\n1. **Fundamentação Teórica**: Explicação de como os conceitos da aula foram aplicados.\n2. **Evidências Práticas**: Documentos, gráficos ou análises que comprovem a execução (evite generalismos).\n3. **Análise Crítica**: Um breve relato sobre os aprendizados e dificuldades da simulação."

for filename in os.listdir(projects_dir):
    if filename.endswith(".md") and filename.startswith("projeto-"):
        file_path = os.path.join(projects_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace objective
        new_content = re.sub(old_objective, new_objective, content)
        # Replace requirements
        new_content = re.sub(old_requirements, new_requirements, new_content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filename}")
        else:
            print(f"No match or already updated: {filename}")
