# Solução 05 - Implementação de APIs ⚙️

!!! tip "Navegação"
[← Exercício 05](exercicio-05.md) | [Próxima Solução →](solucao-06.md)

## 🟢 Respostas Fáceis

### 1. Responsabilidade do Controller

!!! success "Resposta 1"
**Principal função do Controller:**

    O Controller é o **orquestrador** da requisição HTTP. Suas responsabilidades:

    - ✅ **Receber** requisições HTTP
    - ✅ **Validar** parâmetros de entrada
    - ✅ **Chamar** serviços de negócio
    - ✅ **Formatar** e retornar respostas
    - ❌ **NÃO** contém regras de negócio
    - ❌ **NÃO** acessa banco diretamente

    **🏗️ Arquitetura em Camadas:**
    ```mermaid
    graph TD
        A[HTTP Request] --> B[Controller]
        B --> C[Service/Use Case]
        C --> D[Repository]
        D --> E[Database]

        B --> F[Response Formatter]
        F --> G[HTTP Response]

        style B fill:#e3f2fd
        style C fill:#fff3e0
        style D fill:#f3e5f5
    ```

### 2. Handler no Contexto de Rotas

!!! success "Resposta 2"
**Handler em Backend:**

    Um **Handler** é a **função específica** que processa uma rota:

    ```javascript
    // Handler = função que "manipula" a requisição
    app.get('/usuarios', usuarioHandler);  // ← Handler

    function usuarioHandler(req, res) {    // ← Esta é a função Handler
        // Lógica de processamento
        res.json({ usuarios: [...] });
    }
    ```

    **🔄 Fluxo:**
    1. **Rota** define o caminho (`/usuarios`)
    2. **Handler** define o que fazer quando alguém acessar
    3. **Middleware** pode ser executado antes do Handler

## 🟡 Respostas Médias

### 3. Path Params vs Query Params

!!! warning "Resposta 3"
**Diferenciação com Exemplos:**

    | Tipo | Exemplo URI | Uso | Localização no Código |
    |------|-------------|-----|---------------------|
    | **Path Params** | `/usuarios/123/pedidos/456` | **Identificar recursos** específicos | `req.params.id` |
    | **Query Params** | `/usuarios?page=2&limit=10` | **Filtrar/configurar** busca | `req.query.page` |

    **🎯 Exemplos Práticos:**
    ```http
    # Path Params - Identificação obrigatória
    GET /clientes/789                    # cliente específico
    DELETE /produtos/456                 # produto específico
    PUT /pedidos/123/status             # status de pedido específico

    # Query Params - Filtros opcionais
    GET /produtos?categoria=eletronicos&preco_max=1000
    GET /pedidos?status=entregue&data_inicio=2024-01-01
    GET /clientes?cidade=sao-paulo&ativo=true
    ```

    **📝 Implementação em Express.js:**
    ```javascript
    // Path Params
    app.get('/usuarios/:id/pedidos/:pedidoId', (req, res) => {
        const userId = req.params.id;           // 123
        const pedidoId = req.params.pedidoId;   // 456
    });

    // Query Params
    app.get('/produtos', (req, res) => {
        const categoria = req.query.categoria;   // "eletronicos"
        const precoMax = req.query.preco_max;    // "1000"
        const page = req.query.page || 1;        // padrão: 1
    });
    ```

### 4. Status Code Explícito no Controller

!!! warning "Resposta 4"
**Por que sempre definir Status Code:**

    **❌ Problemas sem Status Code explícito:**
    - **Cliente confuso** sobre resultado da operação
    - **Caching inadequado** pelos proxies/CDNs
    - **Logs imprecisos** para monitoramento
    - **Integração quebrada** com outros sistemas

    **✅ Benefícios do Status Code explícito:**
    ```javascript
    // ❌ Ruim - Status implícito (200)
    app.post('/usuarios', (req, res) => {
        const usuario = criarUsuario(req.body);
        res.json(usuario);  // Status 200 - ERRADO para criação!
    });

    // ✅ Bom - Status explícito
    app.post('/usuarios', (req, res) => {
        const usuario = criarUsuario(req.body);
        res.status(201).json(usuario);  // 201 Created - CORRETO!
    });
    ```

    **📊 Impact no Comportamento da API:**

    | Operação | Status Implícito | Status Correto | Impacto |
    |----------|------------------|----------------|---------|
    | **POST /usuarios** | 200 OK | 201 Created | Cache e semântica |
    | **DELETE /usuarios/123** | 200 OK | 204 No Content | Clareza sobre vazio |
    | **PUT /usuarios/999** | 200 OK | 404 Not Found | Error handling |

## 🔴 Resposta Desafio

### 5. Cenário Real - PUT /produtos/123

!!! danger "Resposta 5"
**Implementação Completa:**

    **🔍 Captura dos Dados:**
    ```javascript
    app.put('/produtos/:id', (req, res) => {
        // 1. Capturar o ID da URL
        const idDaUrl = req.params.id;        // ← "123" como string

        // 2. Capturar nome do produto do Body
        const { nome, preco, categoria } = req.body;  // ← JSON payload

        // 3. Capturar query params (se houver)
        const forcUpdate = req.query.force;   // ← ?force=true

        console.log({
            idDaUrl,       // "123"
            nome,          // "Notebook Dell"
            preco,         // 2500.00
            categoria,     // "informatica"
            forcUpdate     // "true"
        });
    });
    ```

    **📋 Localização dos Dados:**

    | Dado | Objeto | Exemplo | Tipo |
    |------|--------|---------|------|
    | **ID do produto** | `req.params.id` | `"123"` | String |
    | **Nome novo** | `req.body.nome` | `"Notebook Dell"` | String |
    | **Preço** | `req.body.preco` | `2500.00` | Number |
    | **Flags opcionais** | `req.query.force` | `"true"` | String |

    **⚔️ Conflito ID URL vs Body:**
    ```javascript
    app.put('/produtos/:id', async (req, res) => {
        const idDaUrl = parseInt(req.params.id);
        const { id: idDoBody, ...dadosAtualizacao } = req.body;

        // ❌ CONFLITO DETECTADO
        if (idDoBody && idDoBody !== idDaUrl) {
            return res.status(400).json({
                erro: "ID inconsistente",
                detalhes: {
                    id_url: idDaUrl,
                    id_body: idDoBody,
                    solucao: "Remova o ID do body ou garanta que sejam iguais"
                }
            });
        }

        // ✅ VALIDAÇÃO PASSOU
        try {
            const produtoExistente = await buscarProduto(idDaUrl);
            if (!produtoExistente) {
                return res.status(404).json({
                    erro: "Produto não encontrado",
                    id: idDaUrl
                });
            }

            // Atualizar apenas com dados do body (sem ID)
            const produtoAtualizado = await atualizarProduto(
                idDaUrl,
                dadosAtualizacao
            );

            return res.status(200).json(produtoAtualizado);

        } catch (erro) {
            return res.status(500).json({
                erro: "Erro interno do servidor",
                message: erro.message
            });
        }
    });
    ```

    **🧪 Exemplo de Requisição:**
    ```http
    PUT /produtos/123 HTTP/1.1
    Content-Type: application/json

    {
        "nome": "Notebook Dell Inspiron 15",
        "preco": 2899.99,
        "categoria": "informatica",
        "especificacoes": {
            "ram": "16GB",
            "storage": "512GB SSD"
        }
    }
    ```

    **📱 Implementação com Validação Avançada:**
    ```javascript
    const { body, validationResult } = require('express-validator');

    const validarProduto = [
        body('nome').isString().isLength({ min: 3, max: 100 }),
        body('preco').isNumeric().custom(value => value > 0),
        body('categoria').isIn(['informatica', 'casa', 'roupas'])
    ];

    app.put('/produtos/:id', validarProduto, async (req, res) => {
        // Verificar erros de validação
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(422).json({
                erro: "Dados inválidos",
                detalhes: errors.array()
            });
        }

        // ... resto da implementação
    });
    ```

    **🔄 Fluxo Completo:**
    ```mermaid
    sequenceDiagram
        participant C as Cliente
        participant API as Controller
        participant V as Validador
        participant S as Service
        participant DB as Database

        C->>+API: PUT /produtos/123 + body
        API->>API: Extrair req.params.id
        API->>API: Extrair req.body.*
        API->>+V: Validar dados

        alt Dados inválidos
            V-->>-API: 422 Validation Error
            API-->>-C: 422 + erros detalhados
        else Dados válidos
            V-->>-API: ✅ Validação OK
            API->>+S: Atualizar produto
            S->>+DB: UPDATE produtos
            DB-->>-S: ✅ Atualizado
            S-->>-API: Produto atualizado
            API-->>-C: 200 + produto
        end
    ```

!!! example "Implementação em Python (FastAPI)"
```python
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

    class ProdutoUpdate(BaseModel):
        nome: str
        preco: float
        categoria: str

    @app.put("/produtos/{produto_id}")
    async def atualizar_produto(
        produto_id: int = Path(..., gt=0),
        produto: ProdutoUpdate
    ):
        # ID vem automaticamente do path
        produto_existente = await buscar_produto(produto_id)
        if not produto_existente:
            raise HTTPException(404, "Produto não encontrado")

        produto_atualizado = await atualizar_produto_db(
            produto_id,
            produto.dict()
        )

        return produto_atualizado  # FastAPI retorna 200 automaticamente
    ```

---

!!! tip "Dicas para Próximos Estudos" - Pratique **validação robusta** com express-validator ou Joi - Implemente **middleware de error handling** customizado - Use **OpenAPI decorators** para documentação automática - Configure **rate limiting** por endpoint

!!! tip "Navegação"
[← Exercício 05](exercicio-05.md) | [Próxima Solução →](solucao-06.md)
