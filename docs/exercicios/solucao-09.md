# Solução 09 - Segurança e Autenticação com JWT 🔐

!!! tip "Navegação"
[← Exercício 09](exercicio-09.md) | [Próxima Solução →](solucao-10.md)

## 🟢 Respostas Fáceis

### 1. Autenticação vs Autorização

!!! success "Resposta 1"
**Diferença entre Autenticação e Autorização:**

    | Aspecto | **Autenticação** | **Autorização** |
    |---------|------------------|------------------|
    | **Pergunta** | **"Quem é você?"** | **"O que você pode fazer?"** |
    | **Processo** | **Verifica identidade** | **Verifica permissões** |
    | **Quando** | **Login** (entrada no sistema) | **A cada ação** dentro do sistema |
    | **Como** | Login/senha, biometria, 2FA | Roles, permissions, policies |

    **🏠 Analogia da Casa:**
    - **Autenticação**: Mostrar **RG na portaria** para provar quem você é
    - **Autorização**: **Chave específica** que define quais quartos você pode entrar

    **🔄 Fluxo Completo:**
    ```mermaid
    sequenceDiagram
        participant U as Usuário
        participant A as Autenticação
        participant S as Sistema
        participant B as Autorização

        U->>+A: Login (email + senha)
        A->>A: Validar credenciais
        A-->>-U: ✅ Token JWT (prova de identidade)

        U->>+S: Acessar /admin/users (com token)
        S->>+B: Verificar permissões
        B->>B: User é ADMIN?
        B-->>-S: ✅ Autorizado / ❌ Negado
        S-->>-U: Conteúdo / Erro 403
    ```

### 2. Partes do JWT

!!! success "Resposta 2"
**3 Partes de um token JWT:**

    ```
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
    │                                    │                                                                                │
    │            HEADER                  │                           PAYLOAD                                              │                 SIGNATURE
    ```

    **📋 Detalhamento das Partes:**

    | Parte | Conteúdo | Codificação | Finalidade |
    |-------|----------|-------------|------------|
    | **Header** | Tipo do token e algoritmo | Base64 | **Metadados** do token |
    | **Payload** | Claims (dados do usuário) | Base64 | **Informações** transportadas |
    | **Signature** | Assinatura criptográfica | HMACSHA256 | **Integridade** do token |

    **🔍 Exemplo Decodificado:**
    ```json
    // HEADER
    {
        "alg": "HS256",
        "typ": "JWT"
    }

    // PAYLOAD
    {
        "sub": "1234567890",
        "name": "João Silva",
        "role": "admin",
        "iat": 1516239022,
        "exp": 1516325422
    }

    // SIGNATURE (não decodificável sem chave)
    HMACSHA256(
        base64UrlEncode(header) + "." +
        base64UrlEncode(payload),
        secret
    )
    ```

## 🟡 Respostas Médias

### 3. Informações Sensíveis no JWT

!!! warning "Resposta 3"
**Por que NÃO incluir informações sensíveis no Payload:**

    **🚨 Problemas de Segurança:**
    - **Base64 ≠ Criptografia**: Qualquer um pode decodificar o payload
    - **Token viaja**: Headers HTTP, logs de servidor, cache de browser
    - **Immutable**: Não dá para "apagar" token já enviado
    - **Debugging**: Tokens aparecem em ferramentas de desenvolvimento

    **❌ O que NUNCA colocar:**
    ```json
    {
        "userId": 123,
        "name": "João",
        "senha": "senha123",           ❌ NUNCA!
        "cpf": "123.456.789-00",       ❌ PII sensível
        "numeroCartao": "1234567890",  ❌ Dados financeiros
        "salario": 15000,              ❌ Info confidencial
        "endereco": "Rua X, 123"       ❌ Dados pessoais
    }
    ```

    **✅ O que é SEGURO colocar:**
    ```json
    {
        "sub": "user_123",          ✅ ID não sensível
        "name": "João Silva",       ✅ Nome público
        "role": "admin",            ✅ Permissões
        "email": "joao@email.com",  ✅ Se necessário
        "iat": 1516239022,          ✅ Timestamps
        "exp": 1516325422,          ✅ Expiração
        "permissions": ["read", "write"] ✅ Autorizações
    }
    ```

    **🔒 Demonstração de Vulnerabilidade:**
    ```javascript
    // QUALQUER PESSOA pode fazer isso:
    const token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...";
    const payload = JSON.parse(atob(token.split('.')[1]));
    console.log(payload); // Vê TODOS os dados do payload!
    ```

### 4. Arquitetura Stateless para Escala

!!! warning "Resposta 4"
**Vantagens Stateless para Milhões de Usuários:**

    **🏗️ Stateful vs Stateless:**
    ```mermaid
    graph TD
        A[Cliente] --> B[Load Balancer]

        subgraph "❌ STATEFUL"
            B --> C[Servidor A]
            B --> D[Servidor B]
            C --> E[Session Store]
            D --> E
            E --> F[Redis/Database]
        end

        subgraph "✅ STATELESS"
            B --> G[Servidor A]
            B --> H[Servidor B]
            G --> I[JWT Token]
            H --> J[JWT Token]
        end

        style E fill:#ff6b6b
        style F fill:#ff6b6b
        style I fill:#81c784
        style J fill:#81c784
    ```

    **📊 Benefícios Stateless:**

    | Aspecto | Stateful (Sessions) | Stateless (JWT) |
    |---------|---------------------|-----------------|
    | **Escalabilidade** | Limitada pelo session store | **Infinita** (horizontal) |
    | **Performance** | Consulta BD a cada request | **Zero consultas** extras |
    | **Complexidade** | Session clustering, sticky sessions | **Distribuição simples** |
    | **Falhas** | Server down = session perdida | **Fault tolerant** |
    | **CDN/Cache** | Difícil de cachear | **Cache friendly** |

    **⚡ Cenário Real de Escala:**
    ```javascript
    // Stateful - Problema
    // 10 milhões de usuários online = 10M sessions em memória
    // Cada servidor precisa de 100GB+ RAM apenas para sessions
    // Load balancer precisa de "sticky sessions" complicadas

    // Stateless - Solução
    app.get('/dashboard', verificarJWT, (req, res) => {
        // Token já contém tudo que precisamos
        const { userId, role, permissions } = req.user;

        // Sem consulta ao session store!
        if (permissions.includes('dashboard.read')) {
            return res.json({ dashboard: "data" });
        }

        return res.status(403).json({ erro: "Sem permissão" });
    });
    ```

    **🚀 Impacto na Performance:**
    ```
    Stateful:  Request → Load Balancer → Server → Session Store → Business Logic
               ⏱️ ~50ms    ⏱️ ~10ms     ⏱️ ~30ms       ⏱️ ~20ms

    Stateless: Request → Load Balancer → Server → Business Logic
               ⏱️ ~50ms    ⏱️ ~10ms     ⏱️ ~20ms

    Ganho: 40%+ mais rápido + infinitamente escalável
    ```

## 🔴 Resposta Desafio

### 5. Análise de Token JWT

!!! danger "Resposta 5"
**Cenário: Token JWT Interceptado**

    **a) Lendo dados sem chave secreta:**
    ```javascript
    // ✅ POSSÍVEL - Payload não é criptografado!
    const tokenInterceptado = "eyJhbGci...";

    function lerPayloadSemChave(token) {
        // Split nas 3 partes
        const partes = token.split('.');
        const payload = partes[1];

        // Decode Base64
        const dadosDecodificados = JSON.parse(atob(payload));

        console.log("Nome do usuário:", dadosDecodificados.name);
        console.log("Role:", dadosDecodificados.role);
        console.log("ID:", dadosDecodificados.sub);

        return dadosDecodificados;
    }

    // Exemplo real:
    lerPayloadSemChave("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c");
    // Output: { sub: "1234567890", name: "John Doe", iat: 1516239022 }
    ```

    **b) Por que servidor rejeita token alterado:**
    ```javascript
    // Atacante tenta burlar:
    const payloadOriginal = { "sub": "123", "name": "User", "role": "user" };
    const payloadMalicioso = { "sub": "1", "name": "Admin", "role": "admin" };

    // ❌ Token alterado será REJEITADO porque:
    function verificarToken(token, secret) {
        const [header, payload, signature] = token.split('.');

        // 1. Server recria a assinatura
        const assinaturaEsperada = crypto
            .createHmac('sha256', secret)
            .update(header + '.' + payload)
            .digest('base64url');

        // 2. Compara com assinatura do token
        if (signature !== assinaturaEsperada) {
            throw new Error("Token inválido - foi alterado!");
        }

        return JSON.parse(atob(payload));
    }
    ```

    **🔐 Fluxo da Verificação:**
    ```mermaid
    sequenceDiagram
        participant A as Atacante
        participant S as Servidor

        A->>A: Intercepta token válido
        A->>A: Altera payload (muda user_id)
        A->>+S: Envia token modificado

        S->>S: Extrai header + payload alterado
        S->>S: Recalcula signature com SECRET
        S->>S: Compara com signature do token

        Note over S: ❌ Signatures não batem!

        S-->>-A: 401 Unauthorized
        Note over A,S: Token foi rejeitado!
    ```

    **c) Armazenamento seguro no Frontend:**
    ```javascript
    // ❌ Opções INSEGURAS:
    // localStorage - XSS pode roubar
    // sessionStorage - XSS pode roubar
    // cookies sem flags - CSRF e XSS

    // ✅ Opção MAIS SEGURA:
    // httpOnly + secure + sameSite cookies

    // Backend seta cookie:
    app.post('/login', (req, res) => {
        const token = gerarJWT(usuario);

        res.cookie('authToken', token, {
            httpOnly: true,    // ✅ JavaScript não consegue acessar
            secure: true,      // ✅ Apenas HTTPS
            sameSite: 'strict', // ✅ Proteção CSRF
            maxAge: 24 * 60 * 60 * 1000 // 24h
        });

        res.json({ sucesso: true });
    });

    // ✅ Alternativa para SPA:
    // localStorage + XSS Protection
    class TokenManager {
        static salvar(token) {
            // Validar que não estamos sendo atacados
            if (this.detectarXSS()) {
                console.error("Possível ataque XSS detectado!");
                return;
            }

            localStorage.setItem('authToken', token);
        }

        static obter() {
            return localStorage.getItem('authToken');
        }

        static limpar() {
            localStorage.removeItem('authToken');
        }

        static detectarXSS() {
            // Verificações básicas de segurança
            return document.domain !== 'meusite.com' ||
                   window.location.protocol !== 'https:';
        }
    }
    ```

    **🛡️ Implementação de Middleware Seguro:**
    ```javascript
    function middlewareJWT(req, res, next) {
        try {
            // 1. Extrair token (cookie ou header)
            const token = req.cookies.authToken ||
                         req.headers.authorization?.replace('Bearer ', '');

            if (!token) {
                return res.status(401).json({ erro: "Token não fornecido" });
            }

            // 2. Verificar integridade e validade
            const payload = jwt.verify(token, process.env.JWT_SECRET);

            // 3. Verificar se não expirou
            if (payload.exp < Date.now() / 1000) {
                return res.status(401).json({ erro: "Token expirado" });
            }

            // 4. Adicionar dados do usuário na request
            req.user = payload;
            next();

        } catch (error) {
            if (error.name === 'JsonWebTokenError') {
                return res.status(401).json({
                    erro: "Token inválido",
                    detalhes: "Token foi alterado ou corrompido"
                });
            }

            return res.status(500).json({ erro: "Erro interno" });
        }
    }
    ```

    **📱 Proteção Adicional - Refresh Token:**
    ```javascript
    // Sistema mais seguro: Access Token (curto) + Refresh Token (longo)
    app.post('/login', async (req, res) => {
        const usuario = await validarCredenciais(req.body);

        const accessToken = jwt.sign(
            { userId: usuario.id, role: usuario.role },
            process.env.ACCESS_SECRET,
            { expiresIn: '15m' }  // Token curto
        );

        const refreshToken = jwt.sign(
            { userId: usuario.id },
            process.env.REFRESH_SECRET,
            { expiresIn: '7d' }  // Token longo
        );

        // Salvar refresh token no BD (pode ser revogado)
        await salvarRefreshToken(usuario.id, refreshToken);

        res.cookie('refreshToken', refreshToken, {
            httpOnly: true,
            secure: true,
            path: '/auth/refresh'  // Apenas endpoint específico
        });

        res.json({ accessToken, expiresIn: 15 * 60 });
    });
    ```

---

!!! tip "Dicas para Próximos Estudos" - Implemente **refresh tokens** para tokens de vida curta - Configure **JWT blacklist** para logout forçado - Use **asymmetric keys (RS256)** em microservices - Implement **rate limiting** no endpoint de login

!!! tip "Navegação"
[← Exercício 09](exercicio-09.md) | [Próxima Solução →](solucao-10.md)
