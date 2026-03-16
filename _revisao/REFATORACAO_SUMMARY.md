# Plano de Implementação - Padronização de `adm_gestao_tiaa`

## Proposto Changes

### Configuration & Infrastructure

- **Logo/Favicon**: Mantido logo atual (necessário converter para SVG branco/transparente no futuro)
- **mkdocs.yml**: Refinado com nova paleta, links sociais expandidos, navegação modular com 4 abas principais
- **.mailmap**: Criado mapeamento de autoria para `ricardotecpro@hotmail.com`
- **pyproject.toml**: Atualizado nome do projeto para `ads_gestao_tecnologia_informacao_aplicada` e adicionadas dependências em falta
- **Auditoria de Índices**: Limpeza completa de todos os `index.md` removendo rastros de cursos anteriores (Backend/Mobile)
- **exclude_docs**: Adicionado ao mkdocs.yml para evitar warnings de arquivos não mapeados

### Navigation & Structure

- **Menu Superior**: Reorganizado em 4 abas principais seguindo o padrão: `Informações`, `Aulas`, `Materiais` e `Impressão`
- **Agrupamento de Aulas**: Aulas organizadas por módulos para melhor navegação:
  - Módulo 1: Fundamentos de Sistemas de Gestão (01-04)
  - Módulo 2: SIG e Decisão Estratégica (05-08)
  - Módulo 3: Operações e Comunicação (09-12)
  - Módulo 4: Gestão de Dados e E-commerce (13-16)

### Homepage (`docs/index.md`)

- **Header**: Título + citação de Steve Jobs sobre tecnologia
- **Atalhos Rápidos**: Grid de 6 cards (Trilha, Slides, Quizzes, Projetos, Exercícios, Setups)
- **Mapa da Jornada**: Resumo dos 4 módulos do curso
- **Dicas de Sucesso**: 3 dicas específicas para o curso de Tecnologia da Informação
- **CTA**: Botão direcionando para Aula 01

### Index Files Updates

- **`aulas/index.md`**: Atualizado para refletir curso de TI aplicada à Administração (removido conteúdo de Backend/Microsserviços)
- **`exercicios/index.md`**: Lista simples sem grid cards, organizada por módulos
- **`projetos/index.md`**: Projetos contextualizados para cenários administrativos e empresariais
- **`quizzes/index.md`**: Quizzes organizados por módulo com nomes adequados ao curso
- **`slides/index.md`**: Estrutura limpa com links para apresentações interativas
- **`setups/index.md`**: Grid com 3 cards (Windows, Linux, macOS) + seção próximos passos
- **`materiais.md`**: Grid de 5 cards seguindo o padrão Gold Standard

### Setup Files

- **`setup-03.md`**: Criado guia completo para macOS com Homebrew, ferramentas essenciais e validação

### Infrastructure Synchronization

- **Features**: Adicionadas navigation.instant, navigation.prune, search.share, content.tabs.link
- **Plugins**: Adicionados social (cards: false), tags, awesome-pages, minify
- **Social Links**: Expandidos para incluir YouTube e X-Twitter
- **URL Updates**: Corrigidos site_url, repo_url e README para refletir nome correto do repositório

## Status Atual

### ✅ Completado

- [x] Configuração base do mkdocs.yml com todas as features necessárias
- [x] Atualização da navegação para 4 abas principais
- [x] Criação do arquivo .mailmap
- [x] Atualização do pyproject.toml com dependências necessárias
- [x] **Correção de dependências**: Removido `mkdocs-tags-plugin` inexistente (tags é nativo do Material)
- [x] Criação do diretório /logs para organização
- [x] Auditoria completa de todos os arquivos index.md
- [x] Homepage seguindo o Gold Standard
- [x] Atualização de URLs no README e configurações
- [x] Correção de configuração do plugin mkdocs-revealjs
- [x] Teste de build com sucesso (mkdocs build --strict)
- [x] **CI/CD Fix**: Corrigido erro que causava falha no pipeline de deploy

### 🔄 Próximos Passos Recomendados

1. **Logo SVG**: Converter logo para formato SVG branco/transparente
2. **Aulas**: Expandir conteúdo das 16 aulas com Mermaid, Termynal e Admonitions
3. **Exercícios**: Criar 5 exercícios por aula + arquivos de solução
4. **Quizzes**: Implementar versão interativa HTML/JS
5. **Projetos**: Desenvolver projetos práticos para cada módulo
6. **Setups**: Completar guias para Windows (setup-01.md) e Linux (setup-02.md)

## Infrastructure Synchronization Status

### Sincronizado com padrão de referência:

- **Features**: navigation.sections, path, instant, prune, search.share ✅
- **Plugins**: social, tags, awesome-pages, minify, print-site (último) ✅
- **Navigation**: Hierarquia modular (Informações, Aulas, Materiais, Impressão) ✅
- **URLs e configurações**: Atualizadas para repositório correto ✅

## Verification Plan

### ✅ Automated Tests

- `mkdocs build --strict` - **PASSOU** sem warnings

### 📋 Manual Verification Next Steps

- `mkdocs serve` + Mobile Review + Mermaid/MathJax Check
- Verificação de todos os links internos
- Teste de responsividade em dispositivos móveis

### 🧹 Cleanup

- **Diretório logs**: Criado para futura organização de arquivos temporários
- **exclude_docs**: Configurado para evitar warnings de arquivos temporários

## Resultado Final

✅ **Infraestrutura Moderna**: MkDocs configurado com todos os plugins e features necessários
✅ **Navegação Otimizada**: Menu organizado em 4 abas com agrupamento modular
✅ **Índices Atualizados**: Todos os arquivos index.md refletem o contexto correto do curso
✅ **Build Funcional**: Projeto constrói sem warnings no modo strict
📚 **Conteúdo Preparado**: Estrutura pronta para expansão do conteúdo das aulas

O projeto está agora totalmente alinhado com as especificações do Master Prompt de Refatoração Universal, mantendo a infraestrutura sincronizada e o conteúdo contextualizado para o curso de Tecnologia da Informação Aplicada à Administração.
