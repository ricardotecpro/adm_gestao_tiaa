# Solução 06 - Cadastro e Fluxo de Informação 💾

!!! tip "Navegação"
    [← Exercício 06](exercicio-06.md) | [Próxima Solução →](solucao-07.md)

## 🟢 Respostas Básicas

### 1. Etapas do Ciclo de Vida da Informação

!!! success "Resposta 1"
    1. **Coleta/Entrada**: Cadastro do dado.
    2. **Armazenamento**: Gravação no banco de dados.
    3. **Processamento**: Transformação/Cálculo.
    4. **Disseminação**: Entrega do relatório.
    5. **Utilização**: Tomada de decisão.

### 2. Fluxo Vertical vs Horizontal

!!! success "Resposta 2"
    - **Vertical**: Ocorre entre hierarquias (ex: Supervisor enviando metas para o operacional ou Diretor recebendo resultados do Tático).
    - **Horizontal**: Ocorre entre departamentos colegas (ex: Vendas avisando o Estoque sobre uma venda para que o item seja separado).

## 🟡 Respostas Intermediárias

### 3. Importância na Gestão Documental

!!! success "Resposta 3"
    - **Versionamento**: Evita que a empresa use uma versão antiga (e inválida) de um contrato, garantindo segurança jurídica.
    - **Indexação**: Permite encontrar um documento entre milhares em segundos usando termos de busca (ex: "Contrato Fornecedor X"), aumentando a produtividade.

### 4. Ponto de Gargalo e SIG

!!! success "Resposta 4"
    Um **gargalo** é onde o fluxo de informação "trava", geralmente esperando uma aprovação manual ou por demora no processamento. O SIG integrado elimina isso através de **Notificações Automáticas** e alertas, fazendo com que a informação "ande" sozinha assim que uma etapa é concluída.

## 🔴 Resposta Desafio

### 5. Desenho de Arquitetura de Fluxo (Fábrica)

!!! danger "Resposta 5"
    - **Caminho da Informação**: O Estoque detecta falta -> SIG gera solicitação -> Gerente aprova via App/SIG -> Compras cota -> Financeiro agenda o pagamento. Todos os dados são compartilhados em tempo real.
    - **Backup e Segurança**: O **Backup** em nuvem garante que, se o servidor físico queimar, o fluxo de pedidos não se perca. A **Segurança** (Criptografia) garante que um concorrente não intercepte os dados de custos da fábrica.
    - **Disseminação e Valor**: Um dado como "10 parafusos comprados" não vale nada para o Diretor. A disseminação de que "o custo fixo de parafusos subiu 15%" permite ao Diretor decidir sobre o aumento do preço do carro final, protegendo o lucro da empresa.

---

!!! tip "Navegação"
    [← Exercício 06](exercicio-06.md) | [Próxima Solução →](solucao-07.md)
