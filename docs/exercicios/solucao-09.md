# Solução 09 - Rastreamento Logístico 📦

!!! tip "Navegação"
    [← Exercício 09](exercicio-09.md) | [Próxima Solução →](solucao-10.md)

## 🟢 Respostas Básicas

### 1. Definição de Rastreabilidade

!!! success "Resposta 1"
    **Rastreabilidade** é a capacidade de registrar e consultar todo o histórico de um produto, desde a origem até o destino final.
    **Motivos para investir:**
    - **Recall**: Localizar rapidamente produtos com defeito para retirada do mercado.
    - **Segurança**: Evitar furtos e garantir que a carga não foi desviada do trajeto original.

### 2. Diferenciação das Tecnologias

!!! success "Resposta 2"
    - **Código de Barras**: Leitura óptica direta, um por um. Barato, mas lento para grandes volumes.
    - **QR Code**: Armazena mais dados e pode ser lido por qualquer celular comum.
    - **RFID**: Usa ondas de rádio. Leitura em massa e a distância, sem precisar "ver" a etiqueta.

## 🟡 Respostas Intermediárias

### 3. Superioridade do RFID no Inventário

!!! success "Resposta 3"
    O **RFID** permite ler centenas de etiquetas simultaneamente através de rádio frequência. Enquanto no código de barras o funcionário precisaria pegar caixa por caixa e bipar manualmente (levando horas ou dias), com RFID basta passar um leitor pelo corredor para identificar todas as 10.000 caixas em segundos, mesmo que estejam dentro de pallets.

### 4. Telemetria e Atendimento B2C

!!! success "Resposta 4"
    A telemetria fornece a localização real do caminhão. Isso permite que a empresa envie notificações automáticas ao cliente como: "Seu produto está a 10km da sua casa e chegará em 20 minutos". Isso reduz a ansiedade do consumidor e evita que o entregador perca a viagem por não encontrar ninguém em casa.

## 🔴 Resposta Desafio

### 5. Design de Solução: Distribuidora de Medicamentos

!!! danger "Resposta 5"
    - **Tecnologia**: RFID ou QR Code com data de validade embutida. O RFID é melhor para o galpão gerenciar lotes, e o QR Code é útil para o hospital consultar a bula e validade no ato do uso.
    - **Fluxo com Rastreabilidade**: Na recepção, o sistema bipa o lote e já cadastra a validade. Ao separar para o hospital, o sistema bloqueia se o funcionário pegar um remédio de um lote diferente do solicitado ou próximo do vencimento, evitando a entrega de produtos inutilizáveis.
    - **FIFO/PEPS**: "First-In, First-Out" (Primeiro que Entra, Primeiro que Sai). O SIG prioriza a venda dos itens que chegaram primeiro (ou que vencem primeiro), evitando prejuízos com expiração de estoque.

---

!!! tip "Navegação"
    [← Exercício 09](exercicio-09.md) | [Próxima Solução →](solucao-10.md)
