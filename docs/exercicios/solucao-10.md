# Solução 10 - Controle de Acesso (RBAC) 🛡️

!!! tip "Navegação"
[← Exercício 10](exercicio-10.md) | [Próxima Solução →](solucao-11.md)

## 🟢 Respostas Fáceis

### 1. Conceito de Role no RBAC

!!! success "Resposta 1"
**Role (Papel) no sistema RBAC:**

    **Role** é um **conjunto de permissões** agrupadas que define **o que um usuário pode fazer** no sistema.

    **🎭 Analogia de Empresa:**
    ```mermaid
    graph TD
        A[👤 João Silva] --> B[🏷️ ROLE: Gerente]
        B --> C[📖 Permissões:]
        C --> D[✅ Ler relatórios]
        C --> E[✅ Aprovar despesas]
        C --> F[✅ Gerenciar equipe]
        C --> G[❌ Acessar financeiro]
    ```

    **📋 Exemplos Práticos de Roles:**

    | Role | Permissões Típicas | Descrição |
    |------|-------------------|-----------|
    | **USER** | `read_profile`, `edit_profile` | Usuário comum do sistema |
    | **EDITOR** | `create_content`, `edit_content`, `delete_own_content` | Criador de conteúdo |
    | **MODERATOR** | `approve_content`, `delete_any_content`, `ban_users` | Moderador da comunidade |
    | **ADMIN** | `manage_users`, `system_settings`, `view_logs` | Administrador do sistema |
    | **SUPER_ADMIN** | `*` (todas as permissões) | Acesso total ao sistema |

    **🔧 Implementação em Código:**
    ```javascript
    // Definição de Roles
    const ROLES = {
        USER: {
            name: 'user',
            permissions: ['profile.read', 'profile.edit']
        },
        EDITOR: {
            name: 'editor',
            permissions: ['profile.read', 'profile.edit', 'content.create', 'content.edit']
        },
        ADMIN: {
            name: 'admin',
            permissions: ['*'] // Todas as permissões
        }
    };

    // Usuário com Role
    const usuario = {
        id: 123,
        nome: "João Silva",
        role: ROLES.EDITOR,
        permissions: ROLES.EDITOR.permissions
    };
    ```

### 2. Status Code para Acesso Negado

!!! success "Resposta 2"
**Status Code apropriado: `403 Forbidden`**

    **Justificativa:**
    - **401 Unauthorized**: "Quem é você?" - Não está logado/autenticado
    - **403 Forbidden**: "Sei quem você é, mas você não pode fazer isso" - Logado mas sem permissão

    **🎯 Usuário comum tentando área admin:**
    ```http
    GET /admin/dashboard HTTP/1.1
    Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "erro": "Acesso negado",
        "message": "Você não tem permissão para acessar esta área",
        "required_role": "admin",
        "your_role": "user"
    }
    ```

## 🟡 Respostas Médias

### 3. Diferença entre 401 e 403

!!! warning "Resposta 3"
**Diferença fundamental 401 vs 403:**

    | Aspecto | **401 Unauthorized** | **403 Forbidden** |
    |---------|---------------------|-------------------|
    | **Significado** | **"Quem é você?"** | **"Sei quem você é, mas não pode"** |
    | **Causa** | **Não autenticado** | **Sem autorização** |
    | **Token JWT** | **Ausente/inválido/expirado** | **Válido, mas role insuficiente** |
    | **Ação do Client** | **Ir para login** | **Mostrar "Acesso negado"** |
    | **Redirecionamento** | **✅ Sim → /login** | **❌ Não** |

    **🔄 Fluxos Comparativos:**
    ```mermaid
    flowchart TD
        A[Request com Token] --> B{Token válido?}

        B -->|Não| C[❌ 401 Unauthorized]
        B -->|Sim| D{Tem permissão?}

        C --> E[🔄 Redirecionar para /login]
        D -->|Não| F[❌ 403 Forbidden]
        D -->|Sim| G[✅ 200 OK + Conteúdo]
        F --> H[🚫 Mostrar "Acesso Negado"]

        style C fill:#ff6b6b
        style F fill:#ffa726
        style G fill:#81c784
    ```

    **💻 Implementação no Frontend:**
    ```javascript
    // Interceptor de resposta
    axios.interceptors.response.use(
        response => response,
        error => {
            if (error.response?.status === 401) {
                // ✅ Redirecionar para login
                localStorage.removeItem('authToken');
                window.location.href = '/login';
                toast.error('Sessão expirada. Faça login novamente.');
            } else if (error.response?.status === 403) {
                // ❌ Não redirecionar, apenas informar
                toast.error('Você não tem permissão para esta ação.');
                // Usuário fica na mesma página
            }
            return Promise.reject(error);
        }
    );
    ```

### 4. Middlewares para Rota Admin

!!! warning "Resposta 4"
**Dois middlewares para `/admin/dashboard`:**

    **1º `verificarAutenticacao` → 2º `verificarAutorizacao`**

    ```javascript
    // ✅ Ordem correta
    app.get('/admin/dashboard',
        verificarAutenticacao,    // 1º: Verifica se está logado
        verificarAutorizacao(['ADMIN']), // 2º: Verifica se é admin
        dashboardController      // 3º: Controller final
    );
    ```

    **🔧 Implementação dos Middlewares:**
    ```javascript
    // 1º MIDDLEWARE - Autenticação
    function verificarAutenticacao(req, res, next) {
        const token = req.headers.authorization?.replace('Bearer ', '');

        if (!token) {
            return res.status(401).json({
                erro: "Token não fornecido",
                action: "redirect_login"
            });
        }

        try {
            const payload = jwt.verify(token, process.env.JWT_SECRET);
            req.user = payload; // Adiciona usuário na request
            next(); // ✅ Passa para próximo middleware
        } catch (error) {
            return res.status(401).json({
                erro: "Token inválido",
                action: "redirect_login"
            });
        }
    }

    // 2º MIDDLEWARE - Autorização
    function verificarAutorizacao(rolesPermitidas) {
        return (req, res, next) => {
            // req.user já foi definido pelo middleware anterior
            const userRole = req.user.role;

            if (!rolesPermitidas.includes(userRole)) {
                return res.status(403).json({
                    erro: "Acesso negado",
                    required_roles: rolesPermitidas,
                    your_role: userRole
                });
            }

            next(); // ✅ Passa para controller
        };
    }
    ```

    **⚡ Por que essa ordem é importante:**
    ```mermaid
    sequenceDiagram
        participant C as Cliente
        participant A as Auth Middleware
        participant R as Role Middleware
        participant D as Dashboard Controller

        C->>+A: GET /admin/dashboard

        alt ❌ Sem token
            A-->>-C: 401 - Vá fazer login
        else ✅ Token válido
            A->>+R: Usuário autenticado

            alt ❌ Não é admin
                R-->>-C: 403 - Sem permissão
            else ✅ É admin
                R->>+D: Usuário autorizado
                D-->>-C: 200 - Dashboard data
            end
        end
    ```

## 🔴 Resposta Desafio

### 5. Sistema Hierárquico de Roles

!!! danger "Resposta 5"
**Implementação de Hierarquia RBAC:**

    **a) Função autorizar() com múltiplas roles:**
    ```javascript
    function autorizar(rolesPermitidas) {
        return (req, res, next) => {
            const userRole = req.user.role;

            // ✅ Verificar se user tem QUALQUER uma das roles
            if (rolesPermitidas.includes(userRole)) {
                return next(); // Autorizado
            }

            return res.status(403).json({
                erro: "Acesso negado",
                required_roles: rolesPermitidas,
                your_role: userRole
            });
        };
    }

    // Exemplos de uso:
    app.get('/editor/posts',
        verificarAutenticacao,
        autorizar(['EDITOR', 'ADMIN']),  // EDITOR OU ADMIN podem acessar
        postsController
    );
    ```

    **b) Sistema Hierárquico Inteligente:**
    ```javascript
    // ✅ Sistema de hierarquia de roles
    const ROLE_HIERARCHY = {
        'USER': 1,
        'EDITOR': 2,
        'MODERATOR': 3,
        'ADMIN': 4,
        'SUPER_ADMIN': 5
    };

    function temPermissaoHierarquica(userRole, roleMinima) {
        const nivelUsuario = ROLE_HIERARCHY[userRole] || 0;
        const nivelMinimo = ROLE_HIERARCHY[roleMinima] || 0;

        return nivelUsuario >= nivelMinimo;
    }

    function autorizarHierarquico(roleMinima) {
        return (req, res, next) => {
            const userRole = req.user.role;

            if (temPermissaoHierarquica(userRole, roleMinima)) {
                return next(); // ✅ Autorizado
            }

            return res.status(403).json({
                erro: "Nível de acesso insuficiente",
                required_minimum: roleMinima,
                your_role: userRole,
                hierarchy: ROLE_HIERARCHY
            });
        };
    }

    // Uso simplificado:
    app.get('/user/profile',
        verificarAutenticacao,
        autorizarHierarquico('USER'),     // USER+ pode acessar
        profileController
    );

    app.get('/editor/dashboard',
        verificarAutenticacao,
        autorizarHierarquico('EDITOR'),   // EDITOR+ pode acessar (inclui ADMIN)
        editorController
    );

    app.get('/admin/settings',
        verificarAutenticacao,
        autorizarHierarquico('ADMIN'),    // Apenas ADMIN+ pode acessar
        adminController
    );
    ```

    **c) Sistema Avançado com Permissões Granulares:**
    ```javascript
    // Sistema híbrido: Roles + Permissions
    const ROLE_DEFINITIONS = {
        'USER': {
            level: 1,
            permissions: ['profile.read', 'profile.edit']
        },
        'EDITOR': {
            level: 2,
            inherits: ['USER'], // Herda permissões de USER
            permissions: ['content.create', 'content.edit', 'content.delete_own']
        },
        'MODERATOR': {
            level: 3,
            inherits: ['EDITOR'],
            permissions: ['content.moderate', 'users.suspend']
        },
        'ADMIN': {
            level: 4,
            inherits: ['MODERATOR'],
            permissions: ['users.manage', 'system.settings', 'logs.view']
        },
        'SUPER_ADMIN': {
            level: 5,
            permissions: ['*'] // Todas as permissões
        }
    };

    class PermissionManager {
        static obterPermissoesCompletas(role) {
            const roleDef = ROLE_DEFINITIONS[role];
            if (!roleDef) return [];

            let permissions = [...roleDef.permissions];

            // Herdar permissões das roles pai
            if (roleDef.inherits) {
                for (const parentRole of roleDef.inherits) {
                    permissions = [
                        ...permissions,
                        ...this.obterPermissoesCompletas(parentRole)
                    ];
                }
            }

            return [...new Set(permissions)]; // Remove duplicatas
        }

        static temPermissao(userRole, permissaoRequerida) {
            const permissions = this.obterPermissoesCompletas(userRole);

            // Super admin tem tudo
            if (permissions.includes('*')) return true;

            // Verificar permissão específica
            return permissions.includes(permissaoRequerida);
        }
    }

    // Middleware baseado em permissões
    function requerPermissao(permissao) {
        return (req, res, next) => {
            const userRole = req.user.role;

            if (PermissionManager.temPermissao(userRole, permissao)) {
                return next();
            }

            return res.status(403).json({
                erro: "Permissão insuficiente",
                required_permission: permissao,
                your_role: userRole,
                your_permissions: PermissionManager.obterPermissoesCompletas(userRole)
            });
        };
    }

    // Uso granular:
    app.delete('/posts/:id',
        verificarAutenticacao,
        requerPermissao('content.delete_own'), // Permissão específica
        deletePostController
    );
    ```

    **🎯 Vantagens da Abordagem Centralizada:**

    ```mermaid
    graph TD
        A[Sistema Centralizado] --> B[Manutenibilidade]
        A --> C[Consistência]
        A --> D[Auditabilidade]
        A --> E[Escalabilidade]

        B --> F["Uma mudança de role afeta todo o sistema"]
        C --> G["Regras iguais em toda aplicação"]
        D --> H["Logs centralizados de acesso"]
        E --> I["Fácil adicionar novas roles/permissions"]

        style A fill:#e3f2fd
        style B fill:#c8e6c9
        style C fill:#c8e6c9
        style D fill:#c8e6c9
        style E fill:#c8e6c9
    ```

    **✅ Benefícios Específicos:**

    1. **DRY (Don't Repeat Yourself)**:
       ```javascript
       // ❌ Sem hierarquia - repetitivo
       app.get('/users', autorizar(['USER', 'EDITOR', 'ADMIN']));
       app.get('/posts', autorizar(['USER', 'EDITOR', 'ADMIN']));
       app.get('/comments', autorizar(['USER', 'EDITOR', 'ADMIN']));

       // ✅ Com hierarquia - simples
       app.get('/users', autorizarHierarquico('USER'));
       app.get('/posts', autorizarHierarquico('USER'));
       app.get('/comments', autorizarHierarquico('USER'));
       ```

    2. **Mudanças Dinâmicas**:
       ```javascript
       // Promover usuário afeta automaticamente todas as routes
       await User.update({ role: 'ADMIN' }, { where: { id: userId } });
       // ✅ Usuário agora tem acesso a TODAS as rotas de níveis inferiores
       ```

    3. **Auditoria e Compliance**:
       ```javascript
       function logAcesso(req, res, next) {
           const { user, originalUrl, method } = req;

           console.log(`[ACCESS] ${user.role} ${user.name} → ${method} ${originalUrl}`);

           // Para compliance (SOX, GDPR, etc.)
           auditLogger.info({
               userId: user.id,
               action: `${method} ${originalUrl}`,
               role: user.role,
               timestamp: new Date(),
               ip: req.ip
           });

           next();
       }
       ```

---

!!! tip "Dicas para Próximos Estudos" - Implemente **Permission-based Access Control (PBAC)** para controle granular - Configure **Dynamic Role Assignment** baseado em contexto - Use **Policy-based Authorization** para regras complexas - Mantenha **audit logs** detalhados para compliance

!!! tip "Navegação"
[← Exercício 10](exercicio-10.md) | [Próxima Solução →](solucao-11.md)
