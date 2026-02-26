# Solução 12 - Introdução ao React ⚛️

!!! tip "Navegação"
[← Exercício 12](exercicio-12.md) | [Próxima Solução →](solucao-13.md)

## 🟢 Respostas Fáceis

### 1. Conceito SPA

!!! success "Resposta 1"
**SPA - Single Page Application:**

    **Principal vantagem**: **Navegação fluida** sem recarregar página.

    ```mermaid
    graph TD
        A[Tradicional] --> B[Cada clique = Nova página]
        A --> C[Reload completo]

        D[SPA] --> E[Uma página inicial]
        D --> F[Conteúdo muda via JavaScript]

        style A fill:#ff6b6b
        style D fill:#81c784
    ```

    **Benefícios**: Experiência mobile-like, cache eficiente, transições suaves.

### 2. className vs class

!!! success "Resposta 2"
**Usamos `className` no React:**

    ```jsx
    // ✅ React - className
    <div className="botao-azul">Clique</div>

    // ❌ HTML - class (palavra reservada JavaScript)
    <div class="botao-azul">Clique</div>
    ```

    **Razão**: `class` é **palavra reservada** em JavaScript (ES6 classes).

## 🟡 Respostas Médias

### 3. Arquitetura LEGO

!!! warning "Resposta 3"
**React = LEGO por componentes reutilizáveis:**

    ```jsx
    // 🧩 Peças LEGO (componentes)
    const Botao = ({ texto, cor }) => <button className={cor}>{texto}</button>;
    const Card = ({ titulo, conteudo }) => (
        <div className="card">
            <h3>{titulo}</h3>
            <p>{conteudo}</p>
        </div>
    );

    // 🏗️ Construção final
    const App = () => (
        <div>
            <Card titulo="Post 1" conteudo="Lorem ipsum..." />
            <Botao texto="Curtir" cor="azul" />
            <Botao texto="Compartilhar" cor="verde" />
        </div>
    );
    ```

    **Organização**: Componentes pequenos, testáveis e composáveis.

### 4. Função do Vite

!!! warning "Resposta 4"
**Vite - Build tool moderno:**

    - **Dev server ultrarrápido**: Hot Module Reload instantâneo
    - **Build otimizado**: Bundling eficiente para produção
    - **ES Modules nativo**: Sem transpilação desnecessária
    - **Substituiu Create React App**: Performance superior

### 5. Props para Reutilização

!!! warning "Resposta 5"
**Props permitem customização:**

    ```jsx
    // 🔧 Componente flexível
    const Botao = ({ texto, cor, onClick }) => (
        <button
            className={`btn btn-${cor}`}
            onClick={onClick}
        >
            {texto}
        </button>
    );

    // 🎨 Usos diferentes
    <Botao texto="Salvar" cor="verde" onClick={salvar} />
    <Botao texto="Cancelar" cor="cinza" onClick={cancelar} />
    <Botao texto="Deletar" cor="vermelho" onClick={deletar} />
    ```

## 🔴 Resposta Desafio

### 6. JSX vs HTML

!!! danger "Resposta 6"
**É JavaScript** (JSX - JavaScript XML), não HTML puro.

    **2 Diferenças sutis do JSX:**

    1. **Self-closing obrigatório**:
       ```jsx
       // ✅ JSX - deve fechar
       <br />
       <img src="foto.jpg" />

       // ❌ HTML - pode não fechar
       <br>
       <img src="foto.jpg">
       ```

    2. **Expressões JavaScript**:
       ```jsx
       // ✅ JSX - {} para JavaScript
       <h1>{nome}</h1>
       <div className={ativo ? 'azul' : 'cinza'}>

       // ❌ HTML - texto literal
       <h1>{nome}</h1> <!-- mostra "{nome}" literal -->
       ```

    **Respostas específicas:**

    **a) Tag `<br>` não fechada:**
    ```jsx
    <br>  // ❌ SyntaxError: JSX element 'br' has no corresponding closing tag
    ```

    **b) Variável no h1:**
    ```jsx
    const nome = "João";
    <h1>{nome}</h1>  // ✅ Mostra: João
    <h1>Olá, {nome}!</h1>  // ✅ Mostra: Olá, João!
    ```

!!! example "Comparação JSX vs HTML"
| Aspecto | HTML | JSX |
|---------|------|-----|
| **Atributo CSS** | `class="botao"` | `className="botao"` |
| **Self-closing** | `<br>` opcional | `<br />` obrigatório |
| **Variáveis** | Não suporta | `{variavel}` |
| **Eventos** | `onclick="func()"` | `onClick={func}` |
| **Comentários** | `<!-- comentário -->` | `{/* comentário */}` |

---

!!! tip "Dicas para Próximos Estudos" - Pratique **componentes funcionais** com hooks - Configure **ESLint** para JSX - Use **React DevTools** para debugging

!!! tip "Navegação"
[← Exercício 12](exercicio-12.md) | [Próxima Solução →](solucao-13.md)
