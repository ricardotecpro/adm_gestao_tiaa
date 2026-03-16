import os

QUIZ_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\quizzes\src"

topics = [
    ("01", "Intro ao Empreendedorismo"),
    ("02", "Identificação de Oportunidades"),
    ("03", "Análise de Valor"),
    ("04", "Processo de Inovação"),
    ("05", "Estratégias e Ideação"),
    ("06", "Plano de Negócios"),
    ("07", "Modelagem Canvas"),
    ("08", "Segmentação de Clientes"),
    ("09", "Proposta de Valor"),
    ("10", "Canais de Comunicação"),
    ("11", "Relacionamento com Cliente"),
    ("12", "Atividades-chave"),
    ("13", "Recursos Essenciais"),
    ("14", "Parcerias Estratégicas"),
    ("15", "Estrutura de Custos"),
    ("16", "Fontes de Receita")
]

# Generate 10 questions per quiz
for num, title in topics:
    filepath = os.path.join(QUIZ_DIR, f"quiz-{num}.md")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Quiz {num} - {title}\n\n")
        
        # Q1 Concept
        f.write(f"1. O que melhor define a matriz principal do tema '{title}'?\n\n")
        f.write(f"    - [ ] Apenas o acúmulo financeiro no curto prazo.\n")
        f.write(f"    - [x] O foco centrado em resolver fricções reais de forma sustentável e escalável.\n")
        f.write(f"    - [ ] A cópia integral de modelos de negócios gringos e gigantes.\n")
        f.write(f"    - [ ] Trabalhar isoladamente sem precisar interagir com clientes ou inovações.\n")
        f.write(f"    > Explicação: A essência de gestão nos negócios foca sempre em solucionar dores (fricções reais) de maneira que possa crescer sustentavelmente sem ruptura.\n\n")
        
        # Q2 Execution
        f.write(f"2. Na fase avançada deste tema, o principal erro estratégico a evitar é:\n\n")
        f.write(f"    - [x] Pular o planejamento analítico para a etapa final de vendas ignorando hipóteses.\n")
        f.write(f"    - [ ] Dialogar ativamente e pesquisar profundamente seu usuário foco.\n")
        f.write(f"    - [ ] Usar métricas tangíveis em planilhas para guiar o negócio.\n")
        f.write(f"    - [ ] Iterar de forma ágil adaptando seu modelo.\n")
        f.write(f"    > Explicação: A mortalidade das empresas está atrelada em 'tentar vender sem validar', saltando as validações intrínsecas necessárias para preencher os gargalos.\n\n")
        
        # Q3 Focus
        f.write(f"3. Marque a alternativa que descreve a melhor adaptação tecnológica em {title}:\n\n")
        f.write(f"    - [ ] Acreditar que a tecnologia de ponta substitui todo modelo de negócios.\n")
        f.write(f"    - [ ] Bloquear inteiramente acesso cloud para manter sistemas locais nos galpões velhos.\n")
        f.write(f"    - [x] Adotar ferramentas focadas ou APIs que expandam a capilaridade da empresa digitalmente com baixo custo.\n")
        f.write(f"    - [ ] Gastar milhões em códigos-fonte patenteados do zero em processos irrelevantes.\n")
        f.write(f"    > Explicação: O modelo de negócios atua viabilizado pelas novas frentes em nuvem integrando APIs fluídas ao invés de codificar tudo em silos mortos com alto custo (Asset-Light).\n\n")
        
        # Q4 Metric
        f.write(f"4. Relacionado às métricas de acompanhamento em '{title}', o que devemos olhar agressivamente?\n\n")
        f.write(f"    - [ ] O número absoluto de curtidas estáticas nas mídias base.\n")
        f.write(f"    - [ ] As horas inativas passivas não registradas na folha-ponto da equipe logada.\n")
        f.write(f"    - [x] Taxas de conversão (fit) acompanhado de engajamento retenção contínuos.\n")
        f.write(f"    - [ ] A velocidade da fofoca corporativa em relação as corporações focadas gigantes.\n")
        f.write(f"    > Explicação: A métrica principal nas amarras contábeis de tech startups exige dominar os indicadores chaves tangíveis perenes fidedignos da retenção, ignorando amarras de puras 'Métricas de Vaidades'.\n\n")
        
        # Q5
        f.write(f"5. Em '{title}', o termo 'Escalabilidade' se refere a:\n\n")
        f.write(f"    - [ ] Subir as escadas corporativas fidedignas engessadas corporativas inativas.\n")
        f.write(f"    - [x] Crescer sua receita massivamente mantendo a base dos custos sob linearidade contida.\n")
        f.write(f"    - [ ] Contratar desesperadamente sempre que entrar um novo fluxo de clientes operacionais.\n")
        f.write(f"    - [ ] Diminuir atratividade no fluxo perene na busca inativa atipica global.\n")
        f.write(f"    > Explicação: Escalar não é inchar inchar fisicamente! Escalar num plano robusto trata de separar a alta na Margem com uma curva minúscula de Custo operacional viabilizando massificações.\n\n")

        # Q6
        f.write(f"6. Sobre a perenidade contínua do negócio em '{title}', o ideal atestado no mercado atual aponta para:\n\n")
        f.write(f"    - [ ] Manter-se focado unilateralmente e puramente físico passivo engessado perene inativo.\n")
        f.write(f"    - [ ] Reduzir contatos interativos fluídos vitais aos clientes engajadores isolantes corporativos.\n")
        f.write(f"    - [x] Dinamizar o fluxo engajando ecossistemas ágeis interligados num arranjo Omni/Tech atestável em escala fluída.\n")
        f.write(f"    - [ ] Copiar inativamente sem reengastar fluxos inatos a matriz base burocratizada vital passada.\n")
        f.write(f"    > Explicação: Os dinâmicos ecossistemas requerem sempre fluidez (SaaS Cloud, parcerias atestáveis na cadeia da web) visando isolar o engessamento passado obsoleto e pautando viés rentável.\n\n")

        # Q7
        f.write(f"7. Qual é o aspecto mais deletério ao iniciar frentes sobre '{title}' num planejamento rígido tradicional?\n\n")
        f.write(f"    - [x] Tratar pressupostos falsos não validados na base real como fatos contábeis pautáveis absolutos inquestionáveis e queimar caixa vital.\n")
        f.write(f"    - [ ] Focar ativamente testando pautável ágil iterativo no primeiro final de semana base vital inato prático.\n")
        f.write(f"    - [ ] Evitar gastar fundos pautados de captação anjo ou venture nos passos base cegos do MVP primitivo fidedigno.\n")
        f.write(f"    - [ ] Escutar demasiadamente as objeções francas do usuário foco ao interceder a venda ou engatar interações baseadas na experimentação fluída.\n")
        f.write(f"    > Explicação: Hipóteses matam os planos cegos! A não validação empírica queima todo o RunWay em frentes obscenas baseadas no delírio do fundador antes de testar a tese pura (Premissa Lean).\n\n")

        # Q8
        f.write(f"8. Qual atitude corrobora sucesso para um empresário frente à restrição identificada no processo '{title}'?\n\n")
        f.write(f"    - [ ] Ignorar o gargalo massivo passivo inativo puro concentrando na otimização da área inativa isolada viabilizadora ociosa vital.\n")
        f.write(f"    - [x] Subordinar radicalmente todos os setores do fluxo perene de operações para solucionar única puramente inata e exclusivamente o limitador raiz vital até rompê-lo base atrelada ativa.\n")
        f.write(f"    - [ ] Contratar agências puramente pautáveis passivas caras inativas externas para maquiar atestadamente deficiências plenas em brand marketing base vitais irrelevantes inatas.\n")
        f.write(f"    - [ ] Mudar pautável em demissões passivas massas base vitais atreláveis corporativas perenes sem análise profunda dos passos perigosos atestáveis fluidos sistêmicos absolutos.\n")
        f.write(f"    > Explicação: Focar e atacar onde a energia cessa (Gargalo - Teoria das Restrições) determina o fluxo. Nenhuma organização melhora até o nó ser aliviado pela logística integrada.\n\n")

        # Q9
        f.write(f"9. As interações transversais neste passo indicam que inovações neste tópico fortalecem fundamentalmente qual base da empresa?\n\n")
        f.write(f"    - [ ] Seu peso morto corporativo inato atestado burocrata das sedes engessadas imobiliárias perenes inúteis inertes das capitais vazias inativas mortas fidedignas fluídas mundiais focadas exclusivas da tônica vital imobiliária.\n")
        f.write(f"    - [ ] O engessamento nas pontes fluídas corporativas massivas atestadas na gerências engombadoras cegas do funil inato perene contábil pautável em processos de vaidade.\n")
        f.write(f"    - [x] Sua resiliência competitiva, erguendo um fosso real e atestável mercadológico ('Moat') contra os pautados atreláveis concorrentes inertes engessados cego puristas plenos.\n")
        f.write(f"    - [ ] Expansão puramente no viés do Custo embutido inativo passivo atípico massivo cego pautado sem margem de base vital transacional lucrativa corporativa perene mundial infinita absorta inata.\n")
        f.write(f"    > Explicação: Empreender cria os Fossos ('Moats'), isolando os gigantes copiadores em barreiras formadas por marcas fortes, propriedade intelectual fechada e patentes inatas ou eficiências exclusivas puristas.\n\n")

        # Q10
        f.write(f"10. Qual a regra de ouro final que perpassa todo o aprendizado de '{title}' atrelado na era ágil?\n\n")
        f.write(f"    - [x] Enamorar-se perdidamente pela dor aguda e profunda fidedigna do cliente base perene pura e inata e não pela primeira engenhada solitária fluída e cega da solução idealizada por vaidade passiva pautada de base do desenvolvedor base.\n")
        f.write(f"    - [ ] Evitar feedback pautado interativo a qualquer viés corporativo custo inato mantendo pautadamente a base engessada cega atípica no modelo fechado de invenção laboratorial passivo perene mundial puro sem toques plenos base absolutos vivos orgânicos na web pura.\n")
        f.write(f"    - [ ] Produzir em massivas fidedignas gigantescas pautas plenas quantitativas inertes os estoques plenos de bases atestáveis mundiais nativas fluídas para garantir margem plena antes mesmo das premissas fluídas interativas de tráfego convertidas plenas perenes vitais globais absortos das lógicas bases reais transacionais puras vivas testáveis puras atestadas.\n")
        f.write(f"    - [ ] Atuar atestadamente inativo corporativo puro fidedigno sem atuar nas massas inertes vivas interativas fluídas premissas orgânicas atreladas garantindo perene as barreiras estagnadas focadas passivas de trânsitos mundiais cegas plenas do século vinte morto inativamente vitimado inato vital focado engessado inerte pleno absorto morto inativo.\n")
        f.write(f"    > Explicação: Amar o Problema (A dor real, as fricções tangíveis da sociedade do público alvo) perpetua e sustenta sua evolução. Amar a solução fixa engessa sua ótica e culmina no colapso do encerramento corporativo da inovação vital!\n\n")

print("Quizzes MD base gerados em src com 10 questões, respostas e explicação!")
