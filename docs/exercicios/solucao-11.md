# Solução 11 - Refresh Token e Segurança Avançada 🏗️

!!! tip "Navegação"
[← Exercício 11](exercicio-11.md) | [Próxima Solução →](solucao-12.md)

## 🟢 Respostas Fáceis

### 1. Access Tokens de Vida Curta

!!! success "Resposta 1"
**Por que Access Tokens têm vida curta (15min-1h):**

    - **Limitação de danos**: Se comprometido, expira rapidamente
    - **Redução de superfície de ataque**: Menos tempo para ser explorado
    - **Facilita revogação**: Usuário fica "deslogado" naturalmente
    - **Melhor auditoria**: Força re-validação frequente

    ```javascript
    // ✅ Estratégia típica
    const accessToken = jwt.sign(payload, secret, { expiresIn: '15m' });  // Curto
    const refreshToken = jwt.sign(payload, secret, { expiresIn: '7d' });  // Longo
    ```

### 2. Biblioteca Helmet

!!! success "Resposta 2"
**Helmet.js - Segurança de Headers HTTP:**

    ```javascript
    const helmet = require('helmet');
    app.use(helmet());

    // Remove headers que expõem informações
    // X-Powered-By: Express → (removido)
    // Server: nginx/1.18.0 → (ocultado)
    // Adiciona headers de segurança automáticos
    ```

## 🟡 Respostas Médias

### 3. CORS - Segurança do Navegador

!!! warning "Resposta 3"
**CORS é proteção do BROWSER, não do servidor:**

    ```bash
    # ✅ cURL funciona SEM CORS
    curl -X GET https://api.exemplo.com/dados
    # → 200 OK (servidor responde normalmente)

    # ❌ Browser bloqueia SEM CORS
    fetch('https://api.exemplo.com/dados')
    # → CORS error (browser bloqueia a resposta)
    ```

    **Servidor sempre processa** - browser que decide mostrar ou não.

### 4. Fluxo 401 + Refresh Token

!!! warning "Resposta 4"
`mermaid
    sequenceDiagram
        Frontend->>API: GET /data (token expirado)
        API-->>Frontend: 401 Token expirado
        Frontend->>Auth: POST /refresh (refresh token)
        Auth-->>Frontend: Novo access token
        Frontend->>API: GET /data (novo token)
        API-->>Frontend: 200 OK + dados
    `

### 5. Headers Sensíveis (Helmet)

!!! warning "Resposta 5"
**3 Informações que Helmet oculta:**

    1. **X-Powered-By**: Express.js versão específica
    2. **Server**: Tecnologia e versão do servidor
    3. **X-Sourcemap**: Localização dos source maps

## 🔴 Resposta Desafio

### 6. Segurança do Refresh Token

!!! danger "Resposta 6"
**Por que Refresh Token é mais seguro:**

    - **Escopo limitado**: Só serve para renovar tokens
    - **Armazenamento seguro**: httpOnly cookies
    - **Rotation**: Muda a cada uso
    - **Revogação**: Pode ser invalidado no servidor

    **Armazenamento: Cookies httpOnly** vs LocalStorage
    - ✅ Cookies: XSS não consegue acessar
    - ❌ LocalStorage: JS pode ler (vulnerável a XSS)

    **Refresh Token Rotation:**
    ```javascript
    // A cada refresh, gerar novo refresh token
    app.post('/refresh', (req, res) => {
        const oldRefresh = req.cookies.refreshToken;

        // Invalidar token antigo
        await blacklistToken(oldRefresh);

        // Gerar novo par
        const newAccessToken = generateAccessToken(user);
        const newRefreshToken = generateRefreshToken(user);

        res.cookie('refreshToken', newRefreshToken, { httpOnly: true });
        res.json({ accessToken: newAccessToken });
    });
    ```

---

!!! tip "Dicas para Próximos Estudos" - Implemente **Token Blacklisting** para logout seguro - Configure **CSP Headers** para proteção XSS - Use **HSTS** para forçar HTTPS

!!! tip "Navegação"
[← Exercício 11](exercicio-11.md) | [Próxima Solução →](solucao-12.md)
