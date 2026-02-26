# Solução 14 - useEffect e Ciclo de Vida ⏳

!!! tip "Navegação"
[← Exercício 14](exercicio-14.md) | [Próxima Solução →](solucao-15.md)

## 🟢 Respostas Fáceis

### 1. useEffect Hook

!!! success "Resposta 1"
**useEffect executa efeitos colaterais:**

    ```jsx
    useEffect(() => {
        // Código que executa após render
        fetchDados();
    }, [dependencias]);
    ```

### 2. Array de Dependências

!!! success "Resposta 2"
**Controla quando o efeito executa:**

    - `[]` = Apenas uma vez (componente montou)
    - `[count]` = Quando count mudar
    - Sem array = A cada render

## 🟡 Respostas Médias

### 3. Cleanup Function

!!! warning "Resposta 3"
```jsx
useEffect(() => {
const timer = setInterval(() => {
console.log("tick");
}, 1000);

        // ✅ Cleanup para evitar memory leak
        return () => clearInterval(timer);
    }, []);
    ```

### 4. API Call no useEffect

!!! warning "Resposta 4"
```jsx
useEffect(() => {
const fetchDados = async () => {
const response = await api.get('/usuarios');
setUsuarios(response.data);
};

        fetchDados();
    }, []); // Array vazio = executa uma vez
    ```

## 🔴 Resposta Desafio

### 5. Múltiplos useEffects

!!! danger "Resposta 5"
**Separar responsabilidades em diferentes efeitos:**

    ```jsx
    // ✅ Efeito para dados iniciais
    useEffect(() => {
        fetchUsuarios();
    }, []);

    // ✅ Efeito para filtros
    useEffect(() => {
        filtrarUsuarios(filtro);
    }, [filtro]);

    // ✅ Efeito para timer
    useEffect(() => {
        const timer = setInterval(atualizarDados, 30000);
        return () => clearInterval(timer);
    }, []);
    ```

---

!!! tip "Navegação"
[← Exercício 14](exercicio-14.md) | [Próxima Solução →](solucao-15.md)
