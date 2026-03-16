import os

PROJ_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\projetos"

data = {
    "01": {"title": "O Despertar do Empreendedor", "desc": "Criando o seu Mapa Estratégico Pessoal de Empreendedorismo."},
    "02": {"title": "Caçador de Dores", "desc": "Mapeamento em campo de frustrações e transformação em Oportunidades Viáveis."},
    "03": {"title": "A Máquina de LTV", "desc": "Projetando um modelo analítico de valor com planilhas de aquisição."},
    "04": {"title": "O Mapa da Evolução", "desc": "Criação de esteiras e processos TRL para escalar invenções acadêmicas."},
    "05": {"title": "Design a Fundo", "desc": "Sprint prático de Duplo Diamante num final de semana."},
    "06": {"title": "Break-Even Realizado", "desc": "Desenvolvimento do fluxo de caixa e cálculo definitivo do Break-Even."},
    "07": {"title": "O Canvas do Seu Negócio", "desc": "Construção visual dos 9 Blocos e simulação de Business Patterns."},
    "08": {"title": "A Persona Perfeita", "desc": "Pesquisa JTBD baseada em perfis demográficos tangíveis para nichos."},
    "09": {"title": "O 'Match' de Mercado", "desc": "Implementação e alinhamento do Canvas da Proposta de Valor."},
    "10": {"title": "A Malha Omnichannel", "desc": "Desenho de jornada fluída desde a primeira impressão web ao pacote na mão."},
    "11": {"title": "Retenção Absoluta", "desc": "Modelagem de réguas ativas (Onboarding e CS) vitais para mitigar Cohort Churn."},
    "12": {"title": "Destruindo Gargalos", "desc": "Mapeamento do processo produtivo em fluxograma para achar o elo frágil (TOC)."},
    "13": {"title": "Leasing vs Posse", "desc": "Cálculo e montagem de uma estrutura 'Asset-Light' contra um gigante OPEX."},
    "14": {"title": "Ecossistema Infinito", "desc": "Projeção de simbiose com APIs de terceiros e prospecção de Joint Ventures."},
    "15": {"title": "Driblando o Fim", "desc": "Gestão e alerta em painel indicador focado no Burn Rate e projeção de Runway."},
    "16": {"title": "As Fontes de Ouro", "desc": "Reforma do produto para atrelar Múltiplas Recorrências transacionais ativas no faturamento."}
}

for proj_num, info in data.items():
    proj_file = os.path.join(PROJ_DIR, f"projeto-{proj_num}.md")
    with open(proj_file, "w", encoding="utf-8") as f:
        f.write(f"# Projeto 01 - {info['title']} 🚀\n".replace("01", proj_num))
        f.write(f"\n!!! info \"Mão na Massa\"\n")
        f.write(f"    **Desafio Prático**: {info['desc']}\n")
        f.write(f"\n---\n\n")
        f.write(f"## 🎯 O Objetivo do Projeto\n\n")
        f.write(f"Este projeto visa aplicar todo o rigor e as ferramentas discutidas na [Aula {proj_num}](../aulas/aula-{proj_num}.md) em um cenário de negócios do mundo real. Você deixará o plano das ideias para a simulação ou aplicação tangível e prática.\n\n")
        f.write(f"## 🛠️ Requisitos de Entrega\n\n")
        f.write(f"Para obter êxito neste nível intermediário, certifique-se de apresentar:\n\n")
        f.write(f"1.  **Fundamentação**: Aplicação clara e documentada do conceito.\n")
        f.write(f"2.  **Dados Evidenciados**: Planilhas, textos focados ou gráficos que representem clareza analítica das métricas e não suposições cegas.\n")
        f.write(f"3.  **Registro de Insights**: Um breve parágrafo documentando as dificuldades encontradas nesta simulação (mitiga o risco de errar com dinheiro verdadeiro no futuro).\n\n")
        f.write(f"---\n\n")
        f.write(f"## 🚀 Passo a Passo da Execução\n\n")
        f.write(f"```termynal\n")
        f.write(f"$ projeto-init --aula {proj_num}\n")
        f.write(f"> Lendo os requisitos de inovação baseados...\n")
        f.write(f"> Criando workspace em branco do business.\n")
        f.write(f"> Dica: Mantenha o foco absoluto e estude seu mercado alvo!\n")
        f.write(f"> Iniciando [EXECUÇÃO].\n")
        f.write(f"```\n\n")
        f.write(f"1. Escreva sua premissa inicial e ancore nos tópicos debatidos na teoria.\n")
        f.write(f"2. Monte sua pesquisa ou quadro base sem preciosismo (rascunho inicial).\n")
        f.write(f"3. Refine a solução como se estivesse preparando um 'pitch' oficial para uma banca avaliadora de investidores Anjo.\n\n")
        f.write(f"---\n\n")
        f.write(f"**Revisão**: Sempre utilize a [Solução dos Exercícios da Aula {proj_num}](../exercicios/solucao-{proj_num}.md) para fixar conceitos fundamentais antes da entrega final dos desafios propostos nas frentes deste projeto!\n")

print("Projetos refatorados com consistencia e links.")
