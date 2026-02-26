# Solução 13 - Gestão de BD: Entrada e Processo 🗄️

!!! tip "Navegação"
    [← Exercício 13](exercicio-13.md) | [Próxima Solução →](solucao-14.md)

## 🟢 Respostas Básicas

### 1. Máscaras de Entrada e GIGO

!!! success "Resposta 1"
    **Máscaras de entrada** são padrões fixos que obrigam o dado a ser digitado corretamente (ex: 000.000.000-00 para CPF). Elas evitam que o "lixo" (dados errados) entre no sistema, pois bloqueiam o salvamento caso o padrão não seja seguido, garantindo a qualidade da base de dados desde o nascimento da informação.

### 2. Exemplos de Processamento

!!! success "Resposta 2"
    1. **Cálculos Automáticos**: O sistema multiplica quantidade por preço unitário para gerar o total da venda.
    2. **Validação de Estoque**: O sistema verifica se há saldo suficiente antes de autorizar a venda.

## 🟡 Respostas Intermediárias

### 3. Integridade Referencial na Venda

!!! success "Resposta 3"
    Isso é vital para evitar **dados órfãos**. Se o sistema permitisse vender para um cliente inexistente, seria impossível emitir nota fiscal, cobrar o boleto ou fazer entrega, pois a "venda" não teria um "dono" real no banco de dados. A integridade garante que as relações entre tabelas sejam verdadeiras.

### 4. Processamento de Regras de Negócio (Lucratividade)

!!! success "Resposta 4"
    O SIG deve emitir um **alerta de erro** ou exigir uma **supervisão gerencial** para autorizar a transação. Se o sistema processar a venda no prejuízo sem avisar, o administrador só descobrirá o erro no fechamento do mês, quando o dinheiro já foi perdido.

## 🔴 Resposta Desafio

### 5. Design de Formulário Seguro: RH

!!! danger "Resposta 5"
    - **Checklist de Campos**: 
        1. **CPF**: Máscara de números e Validador de dígito.
        2. **Data Adm**: Máscara dd/mm/aaaa (Bloquear datas futuras).
        3. **Salário**: Máscara numérica com decimais (Não aceitar negativo).
        4. **E-mail**: Regra de "@" e ".com/br".
        5. **Cargo**: Seleção via lista (*Dropdown*) para evitar erros de digitação.
    - **Fluxo do Dado**: Entrada (Teclado) -> Validação de Campos (Sistema) -> Motor de Processamento (Calcula encargos/FGTS) -> Armazenamento (Banco de Dados Central).
    - **Risco do Campo "Cargo" Aberto**: Se o RH digita "Gerente", "Geren.te" e "Gerens", o sistema entenderá como 3 cargos diferentes. Na hora de gerar um relatório de "Salário por Cargo", os dados estarão fragmentados e errados.

---

!!! tip "Navegação"
    [← Exercício 13](exercicio-13.md) | [Próxima Solução →](solucao-14.md)
