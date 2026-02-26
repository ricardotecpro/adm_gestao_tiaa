# Solução 13 - Estado e Props no React 🔄

!!! tip "Navegação"
[← Exercício 13](exercicio-13.md) | [Próxima Solução →](solucao-14.md)

## 🟢 Respostas Fáceis

### 1. useState Hook

!!! success "Resposta 1"
**useState gerencia estado local do componente:**

    ```jsx
    const [contador, setContador] = useState(0);

    // contador = valor atual
    // setContador = função para alterar
    ```

### 2. Props vs State

!!! success "Resposta 2"
**Props**: Dados **recebidos** do componente pai
**State**: Dados **internos** do próprio componente

## 🟡 Respostas Médias

### 3. Fluxo de Dados

!!! warning "Resposta 3"
```mermaid
graph TD
A[Pai] -->|props| B[Filho]
B -->|eventos| A

        C[State no Pai] --> D[Props para Filho]
        D --> E[Filho atualiza via callback]
        E --> C
    ```

### 4. Imutabilidade

!!! warning "Resposta 4"
```jsx
// ✅ Correto - novo array
setItens([...itens, novoItem]);

    // ❌ Erro - muta diretamente
    itens.push(novoItem);
    setItens(itens);
    ```

## 🔴 Resposta Desafio

### 5. Lifting State Up

!!! danger "Resposta 5"
**Compartilhar estado entre componentes irmãos:**

    ```jsx
    // ✅ Estado no componente pai comum
    const App = () => {
        const [usuario, setUsuario] = useState(null);

        return (
            <>
                <Header usuario={usuario} />
                <Login onLogin={setUsuario} />
                <Dashboard usuario={usuario} />
            </>
        );
    };
    ```

---

!!! tip "Navegação"
[← Exercício 13](exercicio-13.md) | [Próxima Solução →](solucao-14.md)
