# Solução 08 - Boas Práticas e Validação de Dados ✅

!!! tip "Navegação"
[← Exercício 08](exercicio-08.md) | [Próxima Solução →](solucao-09.md)

## 🟢 Respostas Fáceis

### 1. Desconfiança nos Dados do Frontend

!!! success "Resposta 1"
**Por que NUNCA confiar 100% nos dados do frontend:**

    **🚨 Vulnerabilidades de Segurança:**
    - **Manipulação via DevTools**: Qualquer usuário pode alterar JavaScript
    - **Interceptação de Requests**: Ferramentas como Postman/Burp Suite
    - **Bots maliciosos**: Scripts automatizados enviando dados inválidos
    - **Bypass de validações**: Cliente pode desabilitar validações JavaScript

    **📱 Cenários Reais de Ataque:**
    ```javascript
    // Frontend validou, mas atacante interceptou:
    // Dados originais: { preço: 100.00, quantidade: 2 }
    // Dados alterados: { preço: 0.01, quantidade: 999999 }

    // ❌ Backend confiou cegamente
    function finalizarPedido(dadosDoFrontend) {
        const total = dadosDoFrontend.preco * dadosDoFrontend.quantidade;
        // total = 0.01 × 999999 = R$ 9.999,99 (deveria ser R$ 199.999.800,00!)
        return processarPagamento(total);
    }
    ```

    **✅ Princípio "Never Trust, Always Verify":**
    ```mermaid
    graph TD
        A[Dados do Cliente] --> B[Validação Frontend]
        B --> C[Request HTTP]
        C --> D[Validação Backend]
        D --> E[Sanitização]
        E --> F[Regras de Negócio]
        F --> G[Persistência]

        style D fill:#ff6b6b
        style E fill:#ffa726
        style B fill:#81c784

        H[⚠️ Validação Frontend] --> I[Apenas UX]
        J[🛡️ Validação Backend] --> K[Segurança Real]
    ```

### 2. Regra de Validação para Senha

!!! success "Resposta 2"
**Exemplo de validação robusta para senha:**

    ```javascript
    function validarSenha(senha) {
        const regras = [
            {
                teste: senha => senha.length >= 8,
                erro: "Senha deve ter pelo menos 8 caracteres"
            },
            {
                teste: senha => /[A-Z]/.test(senha),
                erro: "Senha deve conter pelo menos 1 letra maiúscula"
            },
            {
                teste: senha => /[a-z]/.test(senha),
                erro: "Senha deve conter pelo menos 1 letra minúscula"
            },
            {
                teste: senha => /[0-9]/.test(senha),
                erro: "Senha deve conter pelo menos 1 número"
            },
            {
                teste: senha => /[!@#$%^&*]/.test(senha),
                erro: "Senha deve conter pelo menos 1 caractere especial (!@#$%^&*)"
            },
            {
                teste: senha => !/\s/.test(senha),
                erro: "Senha não pode conter espaços"
            },
            {
                teste: senha => !isCommonPassword(senha),
                erro: "Senha muito comum, escolha uma mais segura"
            }
        ];

        const erros = [];
        for (const regra of regras) {
            if (!regra.teste(senha)) {
                erros.push(regra.erro);
            }
        }

        return {
            valida: erros.length === 0,
            erros,
            forca: calcularForcaSenha(senha)
        };
    }

    function isCommonPassword(senha) {
        const senhasComuns = [
            '12345678', 'password', 'admin123',
            'qwerty', '123456789', 'password123'
        ];
        return senhasComuns.includes(senha.toLowerCase());
    }
    ```

## 🟡 Respostas Médias

### 3. Validação vs Sanitização

!!! warning "Resposta 3"
**Diferença Prática entre Validação e Sanitização:**

    | Aspecto | **Validação** | **Sanitização** |
    |---------|---------------|------------------|
    | **Objetivo** | **Verificar** se dados estão corretos | **Limpar/corrigir** dados problemáticos |
    | **Ação** | **Aceita** ou **rejeita** | **Transforma** e **corrige** |
    | **Resultado** | `true`/`false` ou lista de erros | Dados **modificados** |
    | **Momento** | **Antes** de processar | **Antes** de persistir |

    **🧪 Exemplos Práticos:**

    **Validação - Verifica sem alterar:**
    ```javascript
    function validarEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return {
            valido: regex.test(email),
            erro: !regex.test(email) ? "E-mail inválido" : null
        };
    }

    validarEmail("João@Email.Com"); // { valido: true, erro: null }
    validarEmail("email-inválido");  // { valido: false, erro: "E-mail inválido" }
    ```

    **Sanitização - Limpa e corrige:**
    ```javascript
    function sanitizarEmail(email) {
        return email
            .trim()                    // Remove espaços
            .toLowerCase()             // Padroniza caixa
            .replace(/\s+/g, '');      // Remove espaços internos
    }

    sanitizarEmail("  João@Email.Com  "); // "joão@email.com"
    sanitizarEmail("user @domain.com");   // "user@domain.com"
    ```

    **🔄 Workflow Completo:**
    ```javascript
    function processarEmail(emailBruto) {
        // 1. SANITIZAR primeiro
        const emailLimpo = sanitizarEmail(emailBruto);

        // 2. VALIDAR depois
        const validacao = validarEmail(emailLimpo);

        if (!validacao.valido) {
            throw new EmailInvalidoError(validacao.erro);
        }

        return emailLimpo;
    }

    // Exemplo de uso:
    processarEmail("  João@Email.Com  "); // "joão@email.com" ✅
    processarEmail("  email-ruim  ");     // EmailInvalidoError ❌
    ```

    **📋 Quando usar cada um:**

    **Use Validação quando:**
    - **CPF/CNPJ**: Não pode "corrigir" um CPF inválido
    - **Senhas**: Deve rejeitar senhas fracas
    - **Datas futuras**: Para agendamentos

    **Use Sanitização quando:**
    - **Nomes**: Remover espaços extras, padronizar case
    - **Telefones**: Remover máscaras e caracteres
    - **Textos**: Escapar HTML, remover scripts maliciosos

### 4. Clean Code - Refatoração de Função

!!! warning "Resposta 4"
**Refatoração da função `usr_ch(a, b)`:**

    **❌ Nome original:**
    ```javascript
    function usr_ch(a, b) { ... } // Recebe e-mail e id, checa se e-mail já existe
    ```

    **✅ Nome refatorado:**
    ```javascript
    async function verificarEmailJaExiste(email, usuarioId) {
        // Implementação clara e autodocumentada
    }
    ```

    **📝 Aplicando todas as boas práticas:**
    ```javascript
    // ✅ Versão completa seguindo Clean Code
    async function verificarEmailJaExiste(email, usuarioIdExcluir = null) {
        /**
         * Verifica se um e-mail já está em uso por outro usuário
         * @param {string} email - E-mail a ser verificado
         * @param {number|null} usuarioIdExcluir - ID do usuário a ignorar na busca (útil para updates)
         * @returns {Promise<boolean>} true se e-mail já existe, false caso contrário
         */

        if (!email || typeof email !== 'string') {
            throw new Error('E-mail é obrigatório e deve ser uma string');
        }

        const emailSanitizado = email.trim().toLowerCase();

        const query = `
            SELECT id FROM usuarios
            WHERE email = ?
            ${usuarioIdExcluir ? 'AND id != ?' : ''}
        `;

        const params = usuarioIdExcluir
            ? [emailSanitizado, usuarioIdExcluir]
            : [emailSanitizado];

        const resultado = await db.query(query, params);
        return resultado.rows.length > 0;
    }

    // Exemplos de uso autodocumentados:
    const emailExiste = await verificarEmailJaExiste('novo@email.com');
    const emailExisteParaOutroUsuario = await verificarEmailJaExiste('edit@email.com', 123);
    ```

    **🎯 Princípios de Clean Code aplicados:**
    - ✅ **Nome descritivo** e **intenção clara**
    - ✅ **Parâmetros nomeados** de forma significativa
    - ✅ **Uma responsabilidade** apenas
    - ✅ **Documentação** JSDoc
    - ✅ **Validação** de parâmetros
    - ✅ **Sanitização** automática

## 🔴 Resposta Desafio

### 5. Tratamento de Erros - Middleware Global

!!! danger "Resposta 5"
**Cenário: Banco de dados caiu**

    **🛠️ Middleware Global de Erros Profissional:**
    ```javascript
    function middlewareGlobalDeErros(error, req, res, next) {
        // 1. GERAR ID ÚNICO PARA O ERRO
        const erroId = gerarUUID();

        // 2. COLETAR CONTEXTO COMPLETO
        const contexto = {
            erroId,
            timestamp: new Date().toISOString(),
            url: req.url,
            method: req.method,
            userAgent: req.headers['user-agent'],
            ip: req.ip || req.connection.remoteAddress,
            userId: req.user?.id || 'anonimo',
            params: req.params,
            query: req.query,
            // ⚠️ NÃO logar req.body por segurança (pode ter senhas)
        };

        // 3. CLASSIFICAR TIPO DE ERRO
        let statusCode, mensagemPublica, categoria;

        if (error.name === 'ValidationError') {
            // Erro de validação - culpa do cliente
            statusCode = 400;
            mensagemPublica = 'Dados enviados são inválidos';
            categoria = 'validation';
        } else if (error.code === 'ECONNREFUSED' || error.code === 'ETIMEDOUT') {
            // Erro de banco - problema interno
            statusCode = 503;
            mensagemPublica = 'Serviço temporariamente indisponível. Tente novamente em alguns minutos.';
            categoria = 'database';
        } else if (error.name === 'JsonWebTokenError') {
            // Erro de autenticação
            statusCode = 401;
            mensagemPublica = 'Token de acesso inválido';
            categoria = 'auth';
        } else if (error.status && error.status < 500) {
            // Erros 4xx - problema do cliente
            statusCode = error.status;
            mensagemPublica = error.message || 'Requisição inválida';
            categoria = 'client';
        } else {
            // Erros 5xx - problema do servidor
            statusCode = 500;
            mensagemPublica = 'Erro interno do servidor. Nossa equipe foi notificada.';
            categoria = 'server';
        }

        // 4. LOGAR DETALHES TÉCNICOS (APENAS NO SERVIDOR)
        const logCompleto = {
            ...contexto,
            error: {
                name: error.name,
                message: error.message,
                stack: error.stack,
                code: error.code,
                categoria
            }
        };

        if (statusCode >= 500) {
            // Erros críticos - log de erro
            logger.error('Erro crítico do servidor', logCompleto);
            // ⚡ Enviar alerta para equipe de desenvolvimento
            alertaService.notificarErroSistema(logCompleto);
        } else {
            // Erros de cliente - log de warning
            logger.warn('Erro de requisição do cliente', logCompleto);
        }

        // 5. RESPOSTA SANITIZADA PARA O CLIENTE
        const respostaPublica = {
            sucesso: false,
            erro: mensagemPublica,
            codigo: categoria,
            timestamp: new Date().toISOString(),
            // ID para o cliente rastrear com suporte
            rastreamento: erroId
        };

        // 6. ADICIONAR DETALHES APENAS EM DESENVOLVIMENTO
        if (process.env.NODE_ENV === 'development') {
            respostaPublica.debug = {
                stack: error.stack,
                detalhes: error.message
            };
        }

        res.status(statusCode).json(respostaPublica);
    }
    ```

    **📱 Resposta para o Cliente (Produção):**
    ```json
    {
        "sucesso": false,
        "erro": "Serviço temporariamente indisponível. Tente novamente em alguns minutos.",
        "codigo": "database",
        "timestamp": "2024-01-15T10:30:00.000Z",
        "rastreamento": "uuid-12345-abcde"
    }
    ```

    **🖥️ Log Interno do Servidor:**
    ```json
    {
        "level": "error",
        "erroId": "uuid-12345-abcde",
        "timestamp": "2024-01-15T10:30:00.000Z",
        "url": "/api/usuarios/123",
        "method": "GET",
        "ip": "192.168.1.100",
        "userId": "user_456",
        "error": {
            "name": "MongoNetworkError",
            "message": "connection 0 to localhost:27017 closed",
            "stack": "MongoNetworkError: connection...",
            "code": "ECONNREFUSED",
            "categoria": "database"
        }
    }
    ```

    **🚫 Por que NÃO enviar erro técnico para o cliente:**

    **❌ Problemas de segurança:**
    - **Information Disclosure**: Revela estrutura interna do sistema
    - **Attack Vector**: Facilita ataques direcionados
    - **Database Schema**: Expõe nomes de tabelas e campos
    - **File Paths**: Mostra estrutura de arquivos do servidor

    **❌ Exemplo do que NÃO fazer:**
    ```json
    // ❌ NUNCA envie isso para o cliente!
    {
        "erro": "Error: ECONNREFUSED at MongoDB connection localhost:27017",
        "stack": "at /app/models/Usuario.js:45:12\n at /app/services/auth.js:123:5",
        "query": "SELECT * FROM usuarios WHERE password = '...'",
        "file": "/var/www/api/config/database.js"
    }
    ```

    **✅ Benefícios da abordagem segura:**
    ```mermaid
    graph TD
        A[Erro Interno] --> B[Middleware Global]
        B --> C[Log Detalhado Servidor]
        B --> D[Resposta Sanitizada Cliente]

        C --> E[Debug para Desenvolvedores]
        C --> F[Alertas para Equipe]
        C --> G[Métricas de Monitoramento]

        D --> H[UX Amigável]
        D --> I[Segurança Preservada]
        D --> J[ID para Suporte]

        style C fill:#ff6b6b
        style D fill:#81c784
    ```

    **🔧 Implementação com Express.js:**
    ```javascript
    const express = require('express');
    const app = express();

    // ... routes ...

    // Middleware de erro DEVE ser o último
    app.use(middlewareGlobalDeErros);

    // Exemplo de como um erro do banco seria tratado:
    app.get('/usuarios/:id', async (req, res, next) => {
        try {
            const usuario = await usuarioService.buscar(req.params.id);
            res.json(usuario);
        } catch (error) {
            // Passa para o middleware global
            next(error);  // ← Importante: usar next(error)
        }
    });
    ```

    **📊 Monitoramento e Alertas:**
    ```javascript
    // Sistema de alertas baseado na frequência de erros
    class AlertaService {
        static async notificarErroSistema(logCompleto) {
            // Contar erros dos últimos 5 minutos
            const errosRecentes = await contarErrosRecentes('5m');

            if (errosRecentes > 10) {
                // Alerta crítico - sistema instável
                await enviarSlack('#alertas-criticos', {
                    text: '🚨 ALERTA CRÍTICO: Sistema apresentando muitos erros',
                    detalhes: logCompleto
                });
            }

            // Log estruturado para ferramentas de monitoramento
            await metricas.incrementar('erros_servidor_total', {
                categoria: logCompleto.error.categoria,
                endpoint: logCompleto.url
            });
        }
    }
    ```

---

!!! tip "Dicas para Próximos Estudos" - Configure **Linting** (ESLint) com regras de segurança - Use **Helmet.js** para headers de segurança - Implemente **Rate Limiting** por endpoint - Configure **CORS** adequadamente para sua aplicação

!!! tip "Navegação"
[← Exercício 08](exercicio-08.md) | [Próxima Solução →](solucao-09.md)
