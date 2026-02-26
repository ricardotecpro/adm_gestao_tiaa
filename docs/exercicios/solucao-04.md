# Solução 04 - Documentação e Mocks 📝

!!! tip "Navegação"
[← Exercício 04](exercicio-04.md) | [Próxima Solução →](solucao-05.md)

## 🟢 Respostas Fáceis

### 1. OpenAPI vs Swagger - Conceptuação

!!! success "Resposta 1"
**OpenAPI** vs **Swagger**:

    - **OpenAPI**: É a **especificação/padrão** para documentar APIs REST (formato YAML/JSON)
    - **Swagger**: É o **conjunto de ferramentas** que implementa OpenAPI

    **🔄 Analogia:**
    - **OpenAPI** = "Manual de instruções" (especificação)
    - **Swagger** = "Kit de ferramentas" para ler/criar manuais

    **🛠️ Ferramentas Swagger:**
    - **Swagger Editor**: Escrever especificações
    - **Swagger UI**: Visualizar documentação interativa
    - **Swagger Codegen**: Gerar código automaticamente

    **📚 Evolução Histórica:**
    ```mermaid
    timeline
        title Evolução OpenAPI/Swagger
        2011 : Swagger nasce
             : Especificação proprietária
        2015 : Swagger 2.0
             : Ganha popularidade
        2017 : OpenAPI 3.0
             : Swagger doa especificação para Linux Foundation
             : Vira padrão aberto
        2024 : OpenAPI 3.1
             : Padrão consolidado na indústria
    ```

### 2. Mock Server - Necessidade do Frontend

!!! success "Resposta 2"
**Por que Frontend usa Mock Server:**

    **🎯 Independência de Desenvolvimento:**
    - **Não espera** o Backend ficar pronto
    - **Simula respostas** das APIs futuras
    - **Testa diferentes cenários** (sucesso, erro, loading)

    **🧪 Cenários de Teste:**
    - **Resposta lenta** (simular loading)
    - **Erro 500** (simular falha do servidor)
    - **Dados vazios** (simular lista vazia)
    - **Token expirado** (simular logout forçado)

    **📈 Benefícios:**
    - **Produtividade**: Desenvolve sem esperar Backend
    - **Qualidade**: Testa edge cases
    - **Demos**: Apresenta para clientes/stakeholders

## 🟡 Respostas Médias

### 3. Análise YAML OpenAPI

!!! warning "Resposta 3"
**Análise do trecho OpenAPI:**
`yaml
    /usuarios/{id}:          # ←  ENDPOINT: /usuarios/{id}
      get:                   # ←  VERBO: GET
        summary: Busca usuário por ID
        responses:
          '200':             # ←  RETORNO: Status 200
            description: Usuário encontrado
    `

    **📋 Respostas:**
    - **Endpoint**: `/usuarios/{id}` (onde `{id}` é path parameter)
    - **Verbo HTTP**: `GET`
    - **Retorno no sucesso**: Status **200** com descrição "Usuário encontrado"

    **⚠️ Problema**: Falta definir **o que** retorna (schema, exemplo)

### 4. Developer Experience (DX) - Documentação Ruim

!!! warning "Resposta 4"
**Por que `"POST /login - Envie os dados do usuário"` é documentação ruim:**

    **🔍 Problemas de DX:**

    | ❌ O que falta | 🤔 Perguntas que surgem |
    |---------------|------------------------|
    | **Formato dos dados** | JSON? XML? FormData? |
    | **Campos obrigatórios** | Quais campos enviar? |
    | **Validações** | CPF? E-mail? Tamanho mín/máx? |
    | **Respostas possíveis** | Status codes? Formato retorno? |
    | **Autenticação** | Como usar o token recebido? |
    | **Erros** | Códigos de erro e mensagens? |

    **📝 Documentação Ideal:**
    ```yaml
    /login:
      post:
        summary: Autentica usuário no sistema
        requestBody:
          content:
            application/json:
              schema:
                properties:
                  email: { type: string, format: email }
                  senha: { type: string, minLength: 6 }
                required: [email, senha]
              example:
                email: "joao@example.com"
                senha: "minhasenha123"
        responses:
          '200':
            description: Login realizado com sucesso
            content:
              application/json:
                schema:
                  properties:
                    token: { type: string }
                    expires_in: { type: integer }
          '401':
            description: Credenciais inválidas
    ```

## 🔴 Resposta Desafio

### 5. Cenário de Desenvolvimento com Mocks

!!! danger "Resposta 5"
**🏗️ Organização do Trabalho:**

    **Semana 1-3: Desenvolvimento Paralelo**
    ```mermaid
    gantt
        title Cronograma Desenvolvimento com Mocks
        dateFormat X
        axisFormat %s

        section Frontend
        Setup Mock Server    :0, 1
        Telas + Integração Mock :1, 7
        Refinamento UX      :7, 14
        Testes E2E         :14, 21

        section Backend
        Modelagem Banco    :0, 7
        APIs + Business Logic :7, 14
        Testes + Deploy    :14, 21

        section Integração
        Troca Mock→Real    :21, 22
        Testes Integração  :22, 23
    ```

    **📋 Estratégia Detalhada:**

    **1️⃣ Definição do Contrato (Dia 1):**
    - **OpenAPI Spec** completa definida em conjunto
    - **Exemplos** de requests/responses documentados
    - **Cenários de erro** mapeados

    **2️⃣ Setup do Mock (Dia 1):**
    - Mock Server reproduz **exatamente** a especificação
    - **URLs idênticas** ao ambiente real
    - **Latência simulada** para realismo

    **3️⃣ Desenvolvimento Frontend (Semanas 1-3):**
    ```javascript
    // Frontend aponta para Mock inicialmente
    const API_BASE = process.env.NODE_ENV === 'development'
        ? 'http://localhost:3001'  // Mock Server
        : 'https://api.producao.com'; // Backend Real

    // Código permanece idêntico independente do servidor
    const login = async (email, senha) => {
        const response = await fetch(`${API_BASE}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });
        return response.json();
    };
    ```

    **4️⃣ Transição Seamless (Semana 4):**

    **✅ Zero Mudanças no Código:**
    ```bash
    # Apenas mudança na variável de ambiente
    NODE_ENV=production npm start
    ```

    **🧪 Validação do Contrato:**
    ```javascript
    // Testes garantem compatibilidade
    describe('API Contract', () => {
        it('Login retorna token e expires_in', async () => {
            const response = await login('test@email.com', 'senha123');
            expect(response).toHaveProperty('token');
            expect(response).toHaveProperty('expires_in');
            expect(typeof response.token).toBe('string');
        });
    });
    ```

    **🛠️ Ferramentas Recomendadas:**

    **1. json-server** - **Mais Simples**:
    ```bash
    npm install -g json-server
    json-server --watch db.json --port 3001
    ```
    ```json
    {
        "usuarios": [
            {"id": 1, "nome": "João", "email": "joao@email.com"}
        ]
    }
    ```

    **2. MSW (Mock Service Worker)** - **Mais Profissional**:
    ```javascript
    import { rest } from 'msw';

    const handlers = [
        rest.post('/login', (req, res, ctx) => {
            const { email, senha } = req.body;

            if (email === 'admin@teste.com' && senha === 'admin123') {
                return res(
                    ctx.status(200),
                    ctx.json({
                        token: 'fake-jwt-token-12345',
                        expires_in: 3600
                    })
                );
            }

            return res(
                ctx.status(401),
                ctx.json({ erro: 'Credenciais inválidas' })
            );
        })
    ];
    ```

    **3. Prism** - **OpenAPI Nativo**:
    ```bash
    npm install -g @stoplight/prism-cli
    prism mock api-spec.yaml
    ```

    **📊 Benefícios da Abordagem:**
    ```mermaid
    graph TD
        A[Definição Contrato OpenAPI] --> B[Mock Server]
        A --> C[Backend Real]

        B --> D[Desenvolvimento Frontend]
        C --> D

        D --> E[Código Único]
        E --> F[Zero Refactor na Integração]

        B --> G[Testes de Cenários]
        G --> H[Maior Qualidade]

        style A fill:#e1f5fe
        style E fill:#c8e6c9
        style F fill:#c8e6c9
    ```

!!! example "Script de Automação Completa"
```bash
#!/bin/bash # setup-mock-environment.sh

    echo "🚀 Configurando ambiente Mock..."

    # 1. Instalar dependências
    npm install -g json-server @stoplight/prism-cli

    # 2. Criar estrutura de arquivos
    mkdir -p mock/{data,specs}

    # 3. Gerar dados fake a partir da OpenAPI
    prism mock api-spec.yaml --port 3001 &

    # 4. Configurar Frontend para ambiente dev
    echo "REACT_APP_API_URL=http://localhost:3001" > .env.development

    echo "✅ Mock Server rodando em http://localhost:3001"
    echo "✅ Frontend configurado para usar Mock"
    echo "🎯 Desenvolvimento pode começar!"
    ```

---

!!! tip "Dicas para Próximos Estudos" - Pratique criando **OpenAPI specs** com Swagger Editor - Configure **Contract Testing** com Pact ou similares - Implemente **versionamento semântico** em suas APIs - Use **Schema validation** no Backend para manter contratos

!!! tip "Navegação"
[← Exercício 04](exercicio-04.md) | [Próxima Solução →](solucao-05.md)
