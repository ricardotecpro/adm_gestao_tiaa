# Solução 10 - Sistemas de Transações Comerciais 🛒

!!! tip "Navegação"
    [← Exercício 10](exercicio-10.md) | [Próxima Solução →](solucao-11.md)

## 🟢 Respostas Básicas

### 1. Definição de PDV

!!! success "Resposta 1"
    O **PDV (Ponto de Venda)** é o local físico ou digital onde o cliente finaliza sua compra. Sua função é registrar os itens, processar o pagamento e emitir o comprovante fiscal, sendo a principal interface operacional do varejo.

### 2. NF-e e NFC-e (XML)

!!! success "Resposta 2"
    - **NF-e**: Nota Fiscal Eletrônica (Uso geral/comercial).
    - **NFC-e**: Nota Fiscal de Consumidor Eletrônica (Varejo).
    O **XML** é o formato digital padrão exigido pelo governo Brasil. Ele garante a transparência fiscal em tempo real, permitindo que o fisco saiba exatamente o que foi vendido e quanto imposto foi gerado instantaneamente.

## 🟡 Respostas Intermediárias

### 3. Integração PDV → Backoffice

!!! success "Resposta 3"
    As 3 áreas principais são:
    1. **Estoque**: Baixa automática das quantidades vendidas.
    2. **Financeiro**: Registro da entrada de valores (dinheiro, cartão, pix).
    3. **Fiscal**: Envio dos dados para a SEFAZ para autorização da nota.
    *(Extra: O CRM também pode ser atualizado se o cliente for identificado).*

### 4. Importância da Automação Comercial

!!! success "Resposta 4"
    A automação elimina a digitação manual de preços. Se o sistema lê o peso da balança e o código do produto e já calcula o valor, evita que o operador erre o preço para mais ou para menos, garantindo que o "dinheiro no caixa" bata com o que o sistema diz ter vendido no final do dia.

## 🔴 Resposta Desafio

### 5. Planejamento de checkout para Pet Shop

!!! danger "Resposta 5"
    - **Hardware Necessário**: Computador/Tablet, Leitor de código de barras, Impressora térmica (para o cupom), Máquina de cartão (PIN Pad) e o equipamento SAT ou MFE.
    - **Fluxo da Venda (Ração)**: 1. Operador "bipa" o saco. 2. PDV consulta preço no ERP. 3. Pagamento autorizado. 4. PDV envia XML para Sefaz. 5. Sefaz autoriza (Protocolo). 6. Cupom é impresso. 7. Estoque central reduz 1 saco.
    - **Queda de Internet (SAT/MFE)**: São equipamentos que armazenam as notas fiscais de forma offline e segura. Assim que a internet volta, eles transmitem tudo para a Sefaz automaticamente, permitindo que a loja nunca pare de vender por falta de sinal.

---

!!! tip "Navegação"
    [← Exercício 10](exercicio-10.md) | [Próxima Solução →](solucao-11.md)
