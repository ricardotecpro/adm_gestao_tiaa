# Solução 07 - SIGs Corporativos e Nichos 🧪

!!! tip "Navegação"
    [← Exercício 07](exercicio-07.md) | [Próxima Solução →](solucao-08.md)

## 🟢 Respostas Básicas

### 1. Software de Nicho vs Genérico

!!! success "Resposta 1"
    O **Software de Nicho (Vertical)** é customizado para atender regras de negócio muito específicas de um setor. Diferente do genérico (que faz só o básico), ele possui campos e fluxos que não existem em outras empresas (ex: Prescrição Médica ou Mapa de Plantio).

### 2. Funções Específicas: Hospitalar e Industrial

!!! success "Resposta 2"
    - **Hospitalar**: Gestão de Leitos (saber qual quarto está limpo/ocupado).
    - **Industrial**: OEE (*Overall Equipment Effectiveness*) - cálculo de eficiência de uma máquina específica.

## 🟡 Respostas Intermediárias

### 3. Logs Imutáveis em Atividades de Risco

!!! success "Resposta 3"
    A imutabilidade garante a **rastreabilidade**. Em casos de acidentes, é necessário ter a certeza de que ninguém alterou o registro do sistema para esconder uma falha humana ou técnica. Isso é vital para auditorias de segurança.

### 4. Integração Setorial + Financeira

!!! success "Resposta 4"
    Embora o sistema de leitos gerencie a parte operacional, é necessário enviar a informação para o **Financeiro** para que o hospital saiba quanto cobrar do convênio por cada diária. Sem essa ponte, a operação acontece, mas a empresa não recebe o dinheiro.

## 🔴 Resposta Desafio

### 5. Consultoria: Posto de Combustível

!!! danger "Resposta 5"
    - **Dados Críticos**: Volume de litros nos tanques (sensores), preço do litro na bomba e integração com o sistema tributário (emissão de cupom fiscal de combustível).
    - **Alerta de Anomalia**: Um tanque com temperatura alta pode indicar vazamento ou risco de explosão. O SIG detecta isso antes do problema físico ser visível, permitindo o isolamento da área.
    - **Problemas com ERP de Loja**: 1. O ERP de loja não entende "venda de frações" (ex: 20,45 litros). 2. Ele não possui integração com medidores de tanques, exigindo medição manual e permitindo erros e roubos de combustível.

---

!!! tip "Navegação"
    [← Exercício 07](exercicio-07.md) | [Próxima Solução →](solucao-08.md)
