# Solução 05 - Tomada de Decisão e Qualidade de Dados 📈

!!! tip "Navegação"
    [← Exercício 05](exercicio-05.md) | [Próxima Solução →](solucao-06.md)

## 🟢 Respostas Básicas

### 1. As 4 Fases da Decisão

!!! success "Resposta 1"
    As fases são: **Inteligência, Design, Escolha e Implementação**.
    Na fase de **Inteligência**, o gestor identifica o problema ou a oportunidade (ex: "As vendas caíram na região Norte?"). É a fase de coleta de sintomas.

### 2. Conceito GIGO (Garbage In, Garbage Out)

!!! success "Resposta 2"
    Significa que, se os dados inseridos (entrada) forem lixos (errados, incompletos ou falsos), as informações geradas pelo sistema (relatórios/gráficos) também serão inúteis e levarão a decisões erradas. A qualidade da decisão depende da qualidade do dado.

## 🟡 Respostas Intermediárias

### 3. Níveis de Decisão: Estratégico vs Operacional

!!! success "Resposta 3"
    - **Estratégico**: Foco no longo prazo (anos), decisões que afetam toda a empresa (ex: abrir filial). O SIG fornece dados macro e tendências.
    - **Operacional**: Foco no curto prazo (dias/horas), decisões diárias (ex: repor item na prateleira). O SIG fornece dados detalhados e rotineiros.

### 4. Regras de Ouro: Precisão e Pontualidade

!!! success "Resposta 4"
    - **Precisão**: Garante que o valor financeiro ou quantidade seja exato. Erro ex: Digitar R$ 100 em vez de R$ 1.000 causa prejuízo de caixa.
    - **Pontualidade**: O dado deve entrar "na hora". Se a venda de ontem só for cadastrada hoje, o relatório de estoque de hoje de manhã estava mentindo (erro de decisão de compra).

## 🔴 Resposta Desafio

### 5. Simulação de Gestão de Crise (Supermercado)

!!! danger "Resposta 5"
    - **Fase de Design**: O gerente pensaria nas alternativas: "Abrir novos caixas?", "Dar desconto para self-checkout?", "Colocar empacotadores extras?". O SIG ajuda simulando o custo de cada opção.
    - **Impacto do Erro de Cadastro na Escolha**: Se o sistema diz que há 5 caixas disponíveis, mas 2 faltaram e não foram baixados no RH, a escolha "Abrir Caixas" será impossível de implementar, fazendo o gerente perder tempo precioso.
    - **Regra de Validação**: Criar um campo obrigatório (*not null*) onde o sistema não permite salvar o cadastro se o valor for zero ou vazio, exibindo o alerta: "Erro: Insira o preço de custo para calcular a margem".

---

!!! tip "Navegação"
    [← Exercício 05](exercicio-05.md) | [Próxima Solução →](solucao-06.md)
