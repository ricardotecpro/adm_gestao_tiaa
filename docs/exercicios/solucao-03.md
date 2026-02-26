# Solução 03 - Características e Funções do ERP ⚙️

!!! tip "Navegação"
    [← Exercício 03](exercicio-03.md) | [Próxima Solução →](solucao-04.md)

## 🟢 Respostas Básicas

### 1. Modularidade e Módulos Essenciais

!!! success "Resposta 1"
    **Modularidade** significa que o sistema é composto por partes independentes (módulos) que se conectam. Isso permite que a empresa contrate apenas o que precisa.
    **Módulos essenciais:** Financeiro, Suprimentos (Estoque) e Faturamento (Fiscal).

### 2. Importância da Auditabilidade

!!! success "Resposta 2"
    A **auditabilidade** garante a confiança nos dados. Em finanças, saber quem alterou um valor ou deletou um lançamento evita fraudes, erros operacionais e permite rastrear a origem de qualquer inconsistência no saldo do caixa.

## 🟡 Respostas Intermediárias

### 3. Não Duplicidade e Banco de Dados Único

!!! success "Resposta 3"
    A **não duplicidade** evita que a mesma informação seja digitada duas vezes em lugares diferentes. Como existe um **Banco de Dados Único**, se o setor de Compras cadastra um novo fornecedor, o Financeiro visualiza os mesmos dados instantaneamente. Isso elimina erros de digitação e garante que todos consultem a "versão única da verdade".

### 4. Segurança por Níveis e Permissões

!!! success "Resposta 4"
    Por questões de **segurança e privacidade (LGPD)**, dados de salários são sensíveis. O ERP gerencia isso através de **perfis de acesso** (RBAC), onde cada usuário é vinculado a uma função que limita quais menus e dados ele pode "Ver", "Editar" ou "Deletar".

## 🔴 Resposta Desafio

### 5. Fluxo Transacional Integrado

!!! danger "Resposta 5"
    **Caminho da Informação:**
    1. **Comercial**: Registra a venda das 10 unidades.
    2. **Estoque**: O sistema "reserva" ou "baixa" as 10 unidades do saldo disponível automaticamente.
    3. **Financeiro**: Gera uma conta a receber e, após o faturamento, emite a Nota Fiscal e o boleto.

    **Falha na Integração:**
    Se a baixa não fosse automática, o vendedor poderia vender o mesmo produto para outro cliente (venda sem estoque físico), gerando atrasos, multas e insatisfação do cliente.

    **Integridade de Dados e Realidade:**
    O conceito de **integridade** garante que cada venda gere uma entrada financeira correspondente. Se o sistema diz que vendeu R$ 1.000, e a integridade for mantida, esse valor deve aparecer como "pendente" ou "recebido" no módulo financeiro, sem perdas de informação no caminho.

---

!!! tip "Navegação"
    [← Exercício 03](exercicio-03.md) | [Próxima Solução →](solucao-04.md)
