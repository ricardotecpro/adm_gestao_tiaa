# Solução 03 - Modelagem REST 📡

!!! tip "Navegação"
[← Exercício 03](exercicio-03.md) | [Próxima Solução →](solucao-04.md)

## 🟢 Respostas Fáceis

### 1. URI Design - Correção das URIs

!!! success "Resposta 1"
**❌ URIs Incorretas** → **✅ URIs Corretas:**

    | ❌ Incorreta | ✅ Correta | 📝 Explicação |
    |-------------|-----------|--------------|
    | `GET /listar_todos_usuarios` | `GET /usuarios` | Nomes em **português**, **verbos desnecessários** |
    | `POST /criarNovoPedido` | `POST /pedidos` | **CamelCase** e verbo redundante (POST já indica criação) |
    | `DELETE /remover-produto-por-id/123` | `DELETE /produtos/123` | **Hífen** e descrição longa desnecessária |

    **📋 Regras REST Aplicadas:**
    - **Substantivos** no plural (usuarios, pedidos, produtos)
    - **Inglês** como padrão internacional
    - **Verbos HTTP** indicam a ação, não a URI
    - **Caminhos simples** e limpos

### 2. Verbos HTTP - Atualização de Senha

!!! success "Resposta 2"
**Resposta**: `PATCH /usuarios/123/senha`

    **Justificativa:**
    - **PATCH**: Atualização **parcial** de um recurso específico
    - **PUT**: Substituiria **todo** o objeto usuário (overkill para só senha)
    - **POST**: Usado para **criação**, não atualização

    **Exemplo de payload:**
    ```json
    {
        "senha_atual": "senha123",
        "senha_nova": "novaSenhaSegura456!"
    }
    ```

## 🟡 Respostas Médias

### 3. Status Codes - Escolha Ideal

!!! warning "Resposta 3"
**Situações e Status Codes:**

    | 📋 Situação | 🎯 Status Code | 📖 Justificativa |
    |-------------|----------------|------------------|
    | **Usuário sem permissão de admin** para deletar | **403 Forbidden** | Acesso **negado** por falta de privilégios |
    | **Cadastro realizado** e dados retornados | **201 Created** | **Recurso criado** com sucesso + localização |
    | **Servidor caiu** por falta de memória | **500 Internal Server Error** | **Erro interno** não previsto pelo cliente |

    **🔍 Detalhamento:**
    ```http
    # Exemplo 403 - Sem permissão
    HTTP/1.1 403 Forbidden
    Content-Type: application/json
    {
        "erro": "Apenas administradores podem deletar arquivos",
        "codigo": "INSUFFICIENT_PRIVILEGES"
    }

    # Exemplo 201 - Criação bem-sucedida
    HTTP/1.1 201 Created
    Location: /usuarios/456
    Content-Type: application/json
    {
        "id": 456,
        "nome": "João Silva",
        "email": "joao@email.com"
    }
    ```

### 4. Idempotência - POST vs GET

!!! warning "Resposta 4"
**Idempotência**: Operação que pode ser **repetida** sem alterar o resultado.

    **🔄 GET é Idempotente:**
    ```http
    GET /usuarios/123  # 1ª chamada
    GET /usuarios/123  # 2ª chamada
    GET /usuarios/123  # 3ª chamada
    ```
    **Resultado**: Sempre retorna os **mesmos dados**, sem alterações.

    **❌ POST NÃO é Idempotente:**
    ```http
    POST /usuarios     # 1ª chamada → Cria usuário ID 100
    POST /usuarios     # 2ª chamada → Cria usuário ID 101
    POST /usuarios     # 3ª chamada → Cria usuário ID 102
    ```
    **Resultado**: Cada chamada **cria um novo** recurso (efeito colateral).

    **🎯 Comparação Prática:**
    - **GET**: Como **consultar saldo** - não muda nada
    - **POST**: Como **fazer depósito** - cada um adiciona dinheiro

## 🔴 Resposta Desafio

### 5. Design de Contrato - E-commerce

!!! danger "Resposta 5"
**🛒 Design Completo das Rotas:**

    **a) Listar todos os itens de um carrinho específico:**
    ```http
    GET /usuarios/123/carrinho/itens
    # ou alternativa:
    GET /carrinhos/456/itens
    ```

    **b) Adicionar item ao carrinho:**
    ```http
    POST /usuarios/123/carrinho/itens
    # Payload:
    {
        "produto_id": 789,
        "quantidade": 2
    }
    ```

    **c) JSON do "Item de Carrinho":**
    ```json
    {
        "id": 1001,
        "produto_id": 789,
        "nome": "Smartphone Samsung Galaxy S24",
        "quantidade": 2,
        "preco_unitario": 2499.90,
        "subtotal": 4999.80,
        "adicionado_em": "2024-01-15T10:30:00Z"
    }
    ```

    **🗂️ Coleção Completa de Endpoints E-commerce:**
    ```http
    # Carrinho
    GET    /usuarios/{id}/carrinho              # Ver carrinho
    DELETE /usuarios/{id}/carrinho              # Limpar carrinho

    # Itens do Carrinho
    GET    /usuarios/{id}/carrinho/itens        # Listar itens
    POST   /usuarios/{id}/carrinho/itens        # Adicionar item
    PUT    /usuarios/{id}/carrinho/itens/{id}   # Atualizar quantidade
    DELETE /usuarios/{id}/carrinho/itens/{id}   # Remover item

    # Checkout e Pedidos
    POST   /usuarios/{id}/carrinho/checkout     # Finalizar compra
    GET    /usuarios/{id}/pedidos               # Histórico pedidos
    GET    /usuarios/{id}/pedidos/{id}          # Detalhes pedido
    ```

!!! example "Mermaid - Fluxo Completo E-commerce"
```mermaid
sequenceDiagram
participant C as Cliente
participant API as API Gateway
participant UC as User Service  
 participant PC as Product Service
participant CC as Cart Service

        C->>+API: GET /usuarios/123/carrinho/itens
        API->>+CC: Buscar itens do carrinho
        CC->>+PC: Buscar detalhes dos produtos
        PC-->>-CC: Dados dos produtos
        CC-->>-API: Itens com detalhes
        API-->>-C: Lista de itens

        C->>+API: POST /usuarios/123/carrinho/itens
        Note over C,API: {"produto_id": 789, "quantidade": 2}
        API->>+PC: Verificar produto existe
        PC-->>-API: ✅ Produto válido
        API->>+CC: Adicionar ao carrinho
        CC-->>-API: ✅ Item adicionado
        API-->>-C: 201 Created
    ```

!!! example "Implementação em Python (FastAPI)"
```python
from fastapi import FastAPI, Path
from typing import List

    @app.get("/usuarios/{user_id}/carrinho/itens")
    async def listar_itens_carrinho(user_id: int = Path(..., gt=0)):
        return await carrinho_service.buscar_itens(user_id)

    @app.post("/usuarios/{user_id}/carrinho/itens", status_code=201)
    async def adicionar_item(user_id: int, item: ItemCarrinhoRequest):
        # Validar produto existe
        produto = await produto_service.buscar(item.produto_id)
        if not produto:
            raise HTTPException(404, "Produto não encontrado")

        # Adicionar ao carrinho
        item_criado = await carrinho_service.adicionar_item(
            user_id, item.produto_id, item.quantidade
        )

        return {
            "id": item_criado.id,
            "produto_id": produto.id,
            "nome": produto.nome,
            "quantidade": item.quantidade,
            "preco_unitario": produto.preco,
            "subtotal": produto.preco * item.quantidade
        }
    ```

---

!!! tip "Dicas para Próximos Estudos" - Pratique com **Postman** ou **Insomnia** testando APIs REST - Estude **Richardson Maturity Model** para APIs avançadas - Implemente **versionamento** de APIs (/v1/, /v2/) - Use **OpenAPI/Swagger** para documentação automática

!!! tip "Navegação"
[← Exercício 03](exercicio-03.md) | [Próxima Solução →](solucao-04.md)
