# 🤖 Master Prompt e Plano de Refatoração Universal de Cursos (MkDocs)

Este documento atua como o **Guia Mestre de Refatoração** para ser aplicado por IAs na padronização de todos os repositórios de cursos da grade. O objetivo é garantir consistência absoluta de UI/UX, arquitetura MkDocs, scripts em Python e progressão didática.

---

## 🧭 1. DIRETRIZES GERAIS (OBRIGATÓRIAS)

### 🇧🇷 Idioma
Todo o conteúdo sem exceção deve estar **100% em Português (Brasil)**:
- 16 Aulas fixas
- Comentários de código
- 16 Slides
- 16 Quizzes
- 16 Exercícios (e Soluções)
- 16 Projetos
- Terminais (Termynal)
- Diagramas e Menus

### 🎨 Padrão Visual Obrigatório
Atualizar todos os arquivos `index.md` seguindo o padrão moderno de cards MkDocs.
Cada aula deve conter estritamente:
- 😊 **Emojis** coerentes e moderados.
- 📊 **Modelagem**: Pelo menos 1 diagrama Mermaid relevante.
- 💻 **CLI**: Pelo menos 1 exemplo interativo usando TermynalJS.
- 🧠 **Admonitions**: Blocos MkDocs de destaque (`!!! info "Conceito"`, `!!! warning "Atenção"`, `!!! tip "Dica"`).
- 📝 **Prática**: Exercícios progressivos (linkados).
- 🚀 **Prática**: Mini-projeto.

### 📈 Progressão Cognitiva
Expandir o aprofundamento do conhecimento das `aulas-xx` para um nível **intermediário**, garantindo uma progressão cognitiva suave e didática da aula 01 à 16.

---

## 📂 2. PLANO POR DIRETÓRIO (RESPEITANDO ESTRUTURA ATUAL)

### 📚 `/docs/aulas/` (16 aulas fixas)
- **Base Fundamental:** Manter os arquivos existentes, mas **expandir e padronizar** o conteúdo.
- **Alinhamento:** Sempre revisar se o conteúdo das aulas está estritamente alinhado ao **Plano de Curso e Ementa**. Esta etapa é o ponto base para todas as demais tarefas.
- Nenhuma aula deve fugir do nicho específico do curso.

### 📝 `/docs/exercicios/`
- **Atenção!** O conteúdo dos exercícios deve refletir estritamente o conteúdo ministrado na sua `aula-xx.md` correspondente. **Sempre realizar uma verificação de alinhamento.**
- Cada arquivo de `exercicio-01.md` a `exercicio-16.md` deve conter exatamente **5 exercícios**:
  - 2 Básicos
  - 2 Intermediários
  - 1 Desafio
- **Atenção (Soluções):** Para cada conjunto de exercícios criado, criar obrigatoriamente um novo arquivo correspondente (`solucao-XX.md`) com a explicação detalhada para consulta posterior pelo aluno.
- Adicionar ao final da página de cada exercício um **LINK** direto para o arquivo com a solução e a explicação detalhada.

### 🚀 `/docs/projetos/`
- **Atenção!** O conteúdo dos projetos deve refletir estritamente o conteúdo ministrado na sua `aula-xx.md` correspondente. **Sempre realizar uma verificação de alinhamento.**
- Estrutura esperada: `Projeto 01` até o `Projeto 16`.
- O escopo dos projetos deve consolidar o conhecimento prático da sua aula base.

### ❓ `/docs/quizzes/`
- **Atenção!** O conteúdo dos quizzes deve refletir estritamente o conteúdo ministrado na sua `aula-xx.md` correspondente. **Sempre realizar uma verificação de alinhamento.**
- Arquivos base devem ficar em `\docs\quizzes\src\*.md`.
- **Interatividade:** Abandonar formatação estática Markdown nos quizzes. Implementar usando blocos HTML nativos interativos via formulários e JavaScript.
- Estética e CSS Premium. Adicionar correção Mobile (`flex-shrink: 0` nos radio-buttons).
- Cada quiz deve ter no mínimo **10 perguntas**.
- Alternativas coerentes, **100% pt-BR**, e com explicação clara (feedback) interativa para a resposta em JS.

### 🎞 `/docs/slides/`
- **Atenção!** O conteúdo dos slides deve refletir estritamente o conteúdo ministrado na sua `aula-xx.md` correspondente. **Sempre realizar uma verificação de alinhamento.**
- Arquivos base ficam em `\docs\slides\src\*.md`.
- **Tamanho:** Média de 20 a 40 slides, sem fugir do tema ou gerar conteúdo vazio.
- **Visual:** Emojis moderados, Diagramas Mermaid embutidos nativamente, trechos de código altamente visíveis.
- **Reveal.js:** Transições modernas. **Correção Crítica:** Converter `{ .fragment }` para HTML `<!-- .element: class="fragment" -->`.
- **Nicho Específico:** Nenhum slide deve fugir do nicho específico do curso ou da aula.

### 🛠️ `/docs/setups/`
- **Atenção!** O conteúdo dos setups deve refletir estritamente a configuração necessária para que o aluno possa desenvolver os conteúdos das aulas (`aula-xx.md`). **Sempre realizar uma verificação de alinhamento.**
- Padrão mínimo:
  - `setup-01.md`: Windows.
  - `setup-02.md`: Linux.
  - `setup-03.md`: macOS.
- Manter formatação visual premium (Termynal, Admonitions, Mermaid).

### 📖 Projeto de Referência MkDocs
- O referencial técnico matriz (Padrão Ouro de Navegação, CSS, e UI) que a IA deve seguir espelhado para novos projetos é **estritamente** o repositório: `D:\SourceCode\REPOS\github.io\ads_extra_hardware_e_compiladores`. Todas as práticas de arquitetura MkDocs, layouts de exercícios e menus devem derivar deste molde.

>*Sempre VERIFICAR se todos os derivados (Slides, Quizzes, Setups, Projetos) estão de fato alinhados à matéria das aulas principais.*

---

## ⚙️ 3. CONFIGURAÇÕES GLOBAIS (mkdocs.yml e pyproject.toml)

### A. Identidade Visual e Logotipo (`mkdocs.yml` e assets)
**Logo (SVG Transparente)**
- Logotipos PNGs frequentemente quebram nos modos escuro/claro, apresentando fundos estranhos. A IA **deve exigir ou criar** (se suportado) o logotipo oficial do curso em formato `.svg` na **cor branca ou adaptável**, **estritamente em fundo transparente**.
- Substituir globalmente o ícone `favicon` e `logo` no `mkdocs.yml`.

Substitua e atualize o block de palette para garantir que responda à preferência do SO do usuário:
```yaml
  palette:
    # Light Mode (Default)
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: amber
      toggle:
        icon: material/weather-sunny
        name: Mudar para modo escuro
    # Dark Mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: amber
      toggle:
        icon: material/weather-night
        name: Mudar para modo claro
```

### B. Redes Sociais (`mkdocs.yml`)
A matriz extra social footer deve apontar sempre para o portfólio moderno:
```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/ricardotecpro
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/ricardotecpro
    - icon: fontawesome/solid/globe
      link: https://ricardotecpro.github.io/
    - icon: fontawesome/brands/youtube
      link: https://www.youtube.com/@ricardotecpro
    - icon: fontawesome/brands/x-twitter
      link: https://twitter.com/ricardotecpro
  version:
    provider: mike
    default: estavel
```

### C. Assinatura Universal (`pyproject.toml`)
Para cada curso validado, o `name` deve espelhar rigidamente a pasta pai (ex: `ads_<nome_generico_do_curso>`), e o author ser sobrescrito:
```toml
[project]
name = "ads_nome_do_curso" # Exemplo, atualizar caso a caso
version = "1.0.0"
description = "ads_nome_do_curso"
authors = [
    {name = "Ricardo Tec Pro", email = "ricardotecpro@hotmail.com"}
]
```

---

## 🔎 4. REVISÃO DE BUGS E SINTAXE (Troubleshooting)

1. **Mermaid.js CDNs & Macros**
   - Atualizar no `mkdocs.yml` o JS do Mermaid para a version robusta: `https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js`.
   - **Prevenção de Erros ("Syntax Error"):** Em diagramas OO, relações (ex: `Pessoa <|-- Aluno`) devem ser plotadas preferencialmente após os blocos de definição das classes. Use tipagem unificada (ex: `+String nome`).
   - **Conflito de MkDocs-Macros:** Troque chaves duplas internas do mermaid `{{ ... }}` por colchetes em balão `([ ... ])` para evitar embate com o jinja renderer.

2. **Termynal Formatting**
   - Na injeção das Divs invisíveis (seja via classe HTML ou bloco `<!-- termynal -->`), use `markdown="1"` ou garanta os espaçamentos internos para que o texto MkDocs cruze a fronteira da tag como bloco visual íntegro.

3. **Admonitions & Tab Group Spacing**
   - Content Tabs `===` encavalados falham em processar o markdown interno se não tiverem linhas vazias de oxigênio entre o Header e o seu miolo. Remova linhas em branco avulsas entre várias de declarações de Headers de Tabs concorrentes, para amarrá-los numa janela única. Mas garanta sempre espaçamento interno perante Admonitions superiores.

4. **MathJax Rendering**
   - Validar massivamente se as fórmulas (LaTex) estão escapadas com clareza (testado com sucesso no modelo matemático de COCOMO e lógicas em aulas densas). Carregar o CDN MathJax caso offline configure quebra.

5. **Fix de Bug "Git Authors" Assinaturas**
   - Se os artigos acusarem e-mail de dev (`ricardo@example.com`), suba um artefato `.mailmap` oculto à raiz mapeando o e-mail legando para `ricardotecpro@hotmail.com` (O plugin lerá nativamente sem destruir a history branch).

6. **Conflitos de Rendering (ex: Svelte / Angular vs MkDocs Macros)**
   - Caso o curso lecione frameworks que utilizem interpolação com chaves duplas `{{ variavel }}`, configure compulsoriamente a flag `render_macros: false` no metadata (`frontmatter`) dos arquivos afetados para evitar quebra silenciosa ou erros de build do MkDocs Python jinja.

7. **Testes Quirks (Quizzes & Terminais em Playwright/Selenium)**
   - O comportamento de botões de cópia (Termynal) e feedback boxes (Quizzes interativos) exige visibilidade real CSS. Testes que acessam o DOM correm risco de *Timeout*. Sempre instruir *asserts* para aguardar transições HTML antes de iterar testes automatizados nestes elementos.

---

## 🛡️ 5. PLANO DE VALIDAÇÃO FINAL (CHECKLIST)

Antes do commit da Release, a IA deve atestar:
- [ ] O Logo do curso foi auditado: Deve ser `.svg` de cor branca em fundo transparente, eliminando bordas visíveis em Dark/Light cases de UI MkDocs.
- [ ] Build do MkDocs passa com comando irrestrito sem lixo de log: `mkdocs build --strict` - é vital não tolerar NENHUM `unmapped file`.
- [ ] Os arquivos gerados de `solucao-XX.md` **estão obrigatoriamente incluídos no Navigation Block** (`mkdocs.yml`).
- [ ] Todos os caminhos (Links Internos) estão sólidos (referências relativas exatas entre aulas `->` soluções `->` exercícios `->` slides).
- [ ] Renderizadores UI operantes (Mermaid e Termynal não quebram formatações).
- [ ] O Menu (Nav) obedece: *Informações (Curso, Plano, Projetos)* e *Configurações (Setups)* lógicos.
- [ ] Há um número padronizado de aulas, refletindo o escopo ideal do curso.
- [ ] O texto é fluído, 100% pt-BR, e **livre de menções literais a escopos mortos de outros cursos do passado**.
- [ ] Organização estrutural em disco: **Mover** arquivos .txt resultantes de logs antigos (menos o `requirements.txt`) para um novo diretório limpo e organizado `logs/`.
- [ ] Diretório Sagrado `_legado`: **Nocivo intocável**. Nunca altere ou apague pastas com nome `_legado`.
- [ ] Revisão dos indíces velhos na raiz: `index.md`, `materiais.md`, `plano-ensino.md` (deve ser `plano.md`), `project_roadmap.md`, `sobre.md`, `README.md` expurgados sobre quaisquer rastros da tecnologia velha do repositório template.
- [ ] O deploy e CD está devidamente engatilhado no branch `gh-pages` with pipeline viável.

## 🎓 RESULTADO ESPERADO
- **Atratividade Material:** 🎨 Interface premium.
- **Didática:** 🧠 Focado em alunos iniciantes (jovens e adultos), neutro e robusto pedagogicamente.
- **Arquitetura:** 📂 Organizado e hiper-escalável.
