# Solução 15 - React Router e Navegação 🧭

!!! tip "Navegação"
[← Exercício 15](exercicio-15.md) | [Próxima Solução →](solucao-16.md)

## 🟢 Respostas Fáceis

### 1. React Router

!!! success "Resposta 1"
**Biblioteca para navegação em SPAs:**

    ```jsx
    import { BrowserRouter, Routes, Route } from 'react-router-dom';

    const App = () => (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/sobre" element={<Sobre />} />
                <Route path="/contato" element={<Contato />} />
            </Routes>
        </BrowserRouter>
    );
    ```

### 2. Link vs <a>

!!! success "Resposta 2"
**Link não recarrega página (SPA), <a> recarrega:**

    ```jsx
    // ✅ SPA navigation
    <Link to="/produtos">Produtos</Link>

    // ❌ Recarrega página
    <a href="/produtos">Produtos</a>
    ```

## 🟡 Respostas Médias

### 3. useParams Hook

!!! warning "Resposta 3"
**Captura parâmetros da URL:**

    ```jsx
    // Rota: /usuario/:id
    const { id } = useParams();

    // URL: /usuario/123
    // id = "123"
    ```

### 4. Rotas Protegidas

!!! warning "Resposta 4"
```jsx
const RotaProtegida = ({ children }) => {
const { usuario } = useContext(AuthContext);

        return usuario ? children : <Navigate to="/login" />;
    };

    <Route path="/admin" element={
        <RotaProtegida>
            <AdminPanel />
        </RotaProtegida>
    } />
    ```

## 🔴 Resposta Desafio

### 5. Nested Routes

!!! danger "Resposta 5"
**Rotas aninhadas para layouts complexos:**

    ```jsx
    <Routes>
        <Route path="/admin" element={<AdminLayout />}>
            <Route index element={<Dashboard />} />
            <Route path="usuarios" element={<Usuarios />} />
            <Route path="configuracoes" element={<Config />} />
        </Route>
    </Routes>

    // AdminLayout.jsx
    const AdminLayout = () => (
        <div>
            <AdminNavbar />
            <Outlet /> {/* Renderiza rota filha */}
        </div>
    );
    ```

---

!!! tip "Navegação"
[← Exercício 15](exercicio-15.md) | [Próxima Solução →](solucao-16.md)
