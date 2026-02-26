# Solução 16 - Context API e Gerenciamento Global 🌐

!!! tip "Navegação"
[← Exercício 16](exercicio-16.md) | [Voltar ao Índice](index.md)

## 🟢 Respostas Fáceis

### 1. Context API

!!! success "Resposta 1"
**Context compartilha dados globalmente sem prop drilling:**

    ```jsx
    const AuthContext = createContext();

    const AuthProvider = ({ children }) => {
        const [usuario, setUsuario] = useState(null);

        return (
            <AuthContext.Provider value={{ usuario, setUsuario }}>
                {children}
            </AuthContext.Provider>
        );
    };
    ```

### 2. Prop Drilling

!!! success "Resposta 2"
**Passar props através de múltiplos níveis:**

    ```jsx
    // ❌ Prop drilling
    <App> → <Header> → <Menu> → <UserIcon usuario={usuario} />

    // ✅ Context API
    const { usuario } = useContext(AuthContext); // Direto em UserIcon
    ```

## 🟡 Respostas Médias

### 3. useContext Hook

!!! warning "Resposta 3"
```jsx
const { usuario, login, logout } = useContext(AuthContext);

    // Acesso direto aos dados do context
    if (!usuario) return <LoginButton onClick={login} />;
    return <WelcomeMessage nome={usuario.nome} onLogout={logout} />;
    ```

### 4. Multiple Contexts

!!! warning "Resposta 4"
`jsx
    const App = () => (
        <AuthProvider>
            <ThemeProvider>
                <NotificationProvider>
                    <Router />
                </NotificationProvider>
            </ThemeProvider>
        </AuthProvider>
    );
    `

## 🔴 Resposta Desafio

### 5. Context vs Estado Local

!!! danger "Resposta 5"
**Quando usar cada um:**

    **Context API** para:
    - ✅ Autenticação de usuário
    - ✅ Tema da aplicação
    - ✅ Idioma/internacionalização
    - ✅ Carrinho de compras

    **Estado Local** para:
    - ✅ Dados de formulário
    - ✅ Estado de loading específico
    - ✅ Modals abertos/fechados
    - ✅ Filtros de uma página específica

    **Regra**: Context para dados que **muitos componentes** precisam acessar.

!!! example "Implementação Completa"
```jsx
// AuthContext.jsx
export const AuthContext = createContext();

    export const AuthProvider = ({ children }) => {
        const [usuario, setUsuario] = useState(null);
        const [loading, setLoading] = useState(true);

        const login = async (email, senha) => {
            setLoading(true);
            try {
                const response = await api.post('/login', { email, senha });
                setUsuario(response.data.usuario);
                localStorage.setItem('token', response.data.token);
            } catch (error) {
                throw error;
            } finally {
                setLoading(false);
            }
        };

        const logout = () => {
            setUsuario(null);
            localStorage.removeItem('token');
        };

        const value = {
            usuario,
            login,
            logout,
            loading,
            isAuthenticated: !!usuario
        };

        return (
            <AuthContext.Provider value={value}>
                {children}
            </AuthContext.Provider>
        );
    };

    // Hook customizado
    export const useAuth = () => {
        const context = useContext(AuthContext);
        if (!context) {
            throw new Error('useAuth deve ser usado dentro de AuthProvider');
        }
        return context;
    };
    ```

---

!!! tip "Dicas para Próximos Estudos" - Explore **Redux Toolkit** para estados complexos - Use **React Query** para gerenciamento de servidor state - Pratique **Custom Hooks** para lógica reutilizável - Configure **TypeScript** para type safety

!!! success "Parabéns! 🎉"
Você completou todos os exercícios do curso. Continue praticando e explorando o ecossistema React!

!!! tip "Navegação"
[← Exercício 16](exercicio-16.md) | [Voltar ao Índice](index.md)
