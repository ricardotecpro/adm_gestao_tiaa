# 📋 Plano de Implementação - Aperfeiçoamento do Curso ADM Gestão TI

## 🎯 Visão Geral

Este plano visa aperfeiçoar e padronizar todo o conteúdo do curso, elevando a qualidade técnica, visual e pedagógica seguindo as diretrizes do Master Prompt.

---

## 📅 ETAPAS DE IMPLEMENTAÇÃO

### 🚀 **FASE 1: CONFIGURAÇÃO E INFRAESTRUTURA** (Prioridade: ALTA)

#### Task 1.1: Atualizar mkdocs.yml - Configurações Visuais

**Responsável:** Desenvolvedor Principal  
**Prazo:** 1 dia  
**Status:** ⏳ Pendente

**Ações:**

- [ ] Atualizar paleta de cores com media queries
- [ ] Configurar extra.social com links atualizados
- [ ] Ativar navigation.sections e navigation.path
- [ ] Configurar plugin social para SEO
- [ ] Atualizar Mermaid para versão 11.12.3

**Código de Exemplo:**

```yaml
theme:
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: amber
      toggle:
        icon: material/weather-sunny
        name: Mudar para modo escuro
```

---

#### Task 1.2: Corrigir pyproject.toml

**Responsável:** Desenvolvedor Principal  
**Prazo:** 0.5 dia  
**Status:** ⏳ Pendente

**Ações:**

- [ ] Atualizar name para "adm_gestao_tiaa"
- [ ] Corrigir authors para padrão Ricardo Tec Pro
- [ ] Verificar dependências atualizadas

---

#### Task 1.3: Criar subpasta /logs e organizar arquivos

**Responsável:** Desenvolvedor Principal  
**Prazo:** 0.5 dia  
**Status:** ⏳ Pendente

**Ações:**

- [ ] Criar diretório /logs
- [ ] Mover logs existentes (exceto requirements.txt)
- [ ] Configurar .gitignore para logs

---

#### Task 1.4: Corrigir Bug dos Fragmentos nos Slides

**Responsável:** Desenvolvedor Principal  
**Prazo:** 1 dia  
**Status:** 🔥 CRÍTICO

**Problema:** `{ .fragment }` aparece literalmente nos slides
**Solução:**

- [ ] Atualizar script de geração para converter `{ .fragment }` para `<!-- .element: class="fragment" -->`
- [ ] Corrigir diretório de origem (usar `/src` correto)
- [ ] Testar todos os slides após correção

---

### 📚 **FASE 2: REVISÃO E EXPANSÃO DO CONTEÚDO DAS AULAS** (Prioridade: ALTA)

#### Task 2.1: Auditoria das 16 Aulas

**Responsável:** Especialista em Conteúdo  
**Prazo:** 3 dias  
**Status:** ⏳ Pendente

**Checklist por Aula:**

- [ ] ✅ Conteúdo alinhado com ementa TI
- [ ] 📊 Pelo menos 1 diagrama Mermaid relevante
- [ ] 💻 Pelo menos 1 exemplo TermynalJS
- [ ] 😊 Emojis moderados e coerentes
- [ ] 🧠 Blocos de destaque (info, warning, tip)
- [ ] 📈 Progressão para nível intermediário

**Template de Verificação:**

```markdown
## Aula XX - [Título]

- [ ] Diagrama Mermaid: ✅/❌
- [ ] Exemplo TermynalJS: ✅/❌
- [ ] Blocos de destaque: ✅/❌
- [ ] Nivel intermediário: ✅/❌
- [ ] Exemplos práticos: ✅/❌
```

---

#### Task 2.2: Expansão de Conteúdo

**Responsável:** Especialista em Conteúdo  
**Prazo:** 5 dias  
**Status:** ⏳ Pendente

**Por Aula, adicionar:**

- [ ] **Mais exemplos práticos** (min. 3 por aula)
- [ ] **Listas estruturadas** com casos de uso
- [ ] **Conceitos intermediários** sem perder progressão
- [ ] **Cenários reais** de TI corporativa
- [ ] **Comparações** entre tecnologias/abordagens

---

### 🎯 **FASE 3: EXERCÍCIOS E SOLUÇÕES** (Prioridade: ALTA)

#### Task 3.1: Verificar Alinhamento Exercícios-Aulas

**Responsável:** Especialista em Conteúdo  
**Prazo:** 2 dias  
**Status:** ⏳ Pendente

**Para cada exercicio-XX.md:**

- [ ] Verificar se reflete conteúdo da aula-XX.md
- [ ] Garantir 2 básicos + 2 intermediários + 1 desafio
- [ ] Validar que soluções existem e estão completas

---

#### Task 3.2: Melhorar Soluções Existentes

**Responsável:** Desenvolvedor Principal  
**Prazo:** 3 dias  
**Status:** ⏳ Pendente

**Aperfeiçoar as 16 soluções com:**

- [ ] **Mais diagramas explicativos**
- [ ] **Códigos funcionais testados**
- [ ] **Variações de implementação**
- [ ] **Troubleshooting comum**
- [ ] **Links para documentação**

---

### 🚀 **FASE 4: PROJETOS PRÁTICOS** (Prioridade: MÉDIA)

#### Task 4.1: Criar Projetos 01-16

**Responsável:** Especialista em Conteúdo + Desenvolvedor  
**Prazo:** 8 dias  
**Status:** ⏳ Pendente

**Estrutura por Projeto:**

- [ ] **Objetivo claro** baseado na aula correspondente
- [ ] **Requisitos técnicos** detalhados
- [ ] **Passo a passo** com capturas de tela
- [ ] **Critérios de avaliação**
- [ ] **Variações/extensões** para alunos avançados

**Template:**

````markdown
# Projeto XX - [Nome do Projeto]

## 🎯 Objetivo

[Baseado no conteúdo da Aula XX]

## 📋 Requisitos

- [ ] Requisito 1
- [ ] Requisito 2

## 🛠️ Tecnologias

- Ferramenta A (da Aula XX)
- Ferramenta B (da Aula XX)

## 📖 Passo a Passo

### Etapa 1: [Nome]

```termynal
$ comando exemplo
```
````

## 🎓 Critérios de Avaliação

- [ ] Funcionalidade (40%)
- [ ] Código limpo (30%)
- [ ] Documentação (30%)

```

---

### ❓ **FASE 5: QUIZZES INTERATIVOS** (Prioridade: MÉDIA)

#### Task 5.1: Atualizar Quizzes em /docs/quizzes/src
**Responsável:** Especialista em Conteúdo
**Prazo:** 4 dias
**Status:** ⏳ Pendente

**Para cada quiz-XX.md:**
- [ ] Mínimo 10 perguntas por quiz
- [ ] Perguntas alinhadas com aula-XX.md
- [ ] Alternativas coerentes e desafiadoras
- [ ] Explicação detalhada da resposta correta
- [ ] Mistura de tipos: múltipla escolha, V/F, ordenação

---

#### Task 5.2: Corrigir Bug Visual nos Quizzes
**Responsável:** Desenvolvedor Principal
**Prazo:** 1 dia
**Status:** 🔥 CRÍTICO

- [ ] Aplicar CSS para círculos perfeitos (`flex-shrink: 0`)
- [ ] Corrigir script de conversão para feedback
- [ ] Testar renderização em mobile

---

### 🎞️ **FASE 6: SLIDES MODERNOS** (Prioridade: MÉDIA)

#### Task 6.1: Atualizar Slides em /docs/slides/src
**Responsável:** Designer + Desenvolvedor
**Prazo:** 6 dias
**Status:** ⏳ Pendente

**Padrão por Slide:**
- [ ] **20 slides**: aulas com conteúdo menor
- [ ] **40 slides**: aulas densas/complexas
- [ ] **Transições modernas** RevealJS
- [ ] **Diagramas Mermaid incorporados**
- [ ] **Animações { .fragment }** funcionando
- [ ] **Código visível** e bem formatado

---

#### Task 6.2: Gerar Slides por Aula
**Responsável:** Desenvolvedor Principal
**Prazo:** 2 dias
**Status:** ⏳ Pendente

**Script automático para:**
- [ ] Extrair conteúdo das aulas
- [ ] Converter para formato RevealJS
- [ ] Aplicar template visual consistente
- [ ] Gerar .html final para cada aula

---

### 🛠️ **FASE 7: SETUPS DE AMBIENTE** (Prioridade: BAIXA)

#### Task 7.1: Modernizar Setup Windows/Linux
**Responsável:** Desenvolvedor Principal
**Prazo:** 2 dias
**Status:** ⏳ Pendente

- [ ] **setup-01.md**: Windows com ferramentas atualizadas
- [ ] **setup-02.md**: Linux (Ubuntu/Debian)
- [ ] **setup-03.md**: macOS (manter existente)
- [ ] Adicionar diagramas de fluxo de instalação
- [ ] Troubleshooting comum

---

### 📊 **FASE 8: VALIDAÇÃO E OTIMIZAÇÃO** (Prioridade: ALTA)

#### Task 8.1: Validação Técnica Completa
**Responsável:** Desenvolvedor Principal
**Prazo:** 1 dia
**Status:** ⏳ Pendente

**Checklist Final:**
- [ ] `mkdocs build --strict` sem erros
- [ ] Todos os links internos funcionando
- [ ] Mermaid renderizando (versão 11.12.3)
- [ ] TermynalJS funcionando
- [ ] MathJax renderizando fórmulas
- [ ] Navigation.sections ativo
- [ ] Social cards funcionando

---

#### Task 8.2: Testes de UX
**Responsável:** Tester/QA
**Prazo:** 1 dia
**Status:** ⏳ Pendente

- [ ] **Mobile responsivo** em 3 dispositivos
- [ ] **Velocidade carregamento** < 2s
- [ ] **Navegação intuitiva** entre seções
- [ ] **Search funcionando** corretamente
- [ ] **Dark/Light mode** alternando

---

#### Task 8.3: Atualizações nos Índices
**Responsável:** Desenvolvedor Principal
**Prazo:** 1 dia
**Status:** ⏳ Pendente

- [ ] Todos os index.md com padrão de cards
- [ ] **materiais.md** atualizado
- [ ] **plano-ensino.md** → **plano.md**
- [ ] **project_roadmap.md** revisado
- [ ] **sobre.md** atualizado
- [ ] **README.md** com instruções claras

---

## 📈 **CRONOGRAMA RESUMIDO**

| Fase | Duração | Prioridade | Dependências |
|------|---------|------------|--------------|
| **1. Configuração** | 3 dias | 🔥 ALTA | - |
| **2. Conteúdo Aulas** | 8 dias | 🔥 ALTA | Fase 1 |
| **3. Exercícios** | 5 dias | 🔥 ALTA | Fase 2 |
| **4. Projetos** | 8 dias | 🟡 MÉDIA | Fase 2 |
| **5. Quizzes** | 5 dias | 🟡 MÉDIA | Fase 2 |
| **6. Slides** | 8 dias | 🟡 MÉDIA | Fase 2 |
| **7. Setups** | 2 dias | 🟢 BAIXA | Fase 1 |
| **8. Validação** | 3 dias | 🔥 ALTA | Todas |

**⏱️ Total Estimado:** 42 dias úteis

---

## 🎯 **CRITÉRIOS DE SUCESSO**

### ✅ **Técnicos**
- Build sem warnings/erros
- Performance Score > 90 (Lighthouse)
- Compatibilidade mobile/desktop 100%
- SEO Score > 85

### ✅ **Pedagógicos**
- 16 aulas com progressão cognitiva clara
- 16 exercícios + soluções completas
- 16 projetos práticos funcionais
- 16 quizzes com min. 10 perguntas

### ✅ **Visuais**
- Design consistente Material
- Soluções responsivas
- Transições/animações funcionando
- Dark/Light mode polido

---

## 🛠️ **FERRAMENTAS DE APOIO**

### **Scripts de Automação**
- `build_slides.py`: Gerar slides automaticamente
- `validate_content.py`: Verificar alinhamento aulas-exercícios
- `check_links.py`: Validar links internos
- `generate_index.py`: Criar índices com cards

### **Ambientes de Teste**
- **Local**: `mkdocs serve`
- **Staging**: GitHub Pages branch `staging`
- **Produção**: GitHub Pages branch `gh-pages`

---

## 📞 **RESPONSABILIDADES**

| Papel | Nome | Responsabilidades |
|-------|------|------------------|
| **Tech Lead** | [Nome] | Configurações, scripts, validação técnica |
| **Content Specialist** | [Nome] | Aulas, exercícios, projetos, quizzes |
| **UX Designer** | [Nome] | Visual, slides, navegação |
| **QA Tester** | [Nome] | Testes, validação final |

---

## 📋 **PRÓXIMOS PASSOS IMEDIATOS**

1. ✅ **Aprovar plano** com stakeholders
2. 🔥 **Iniciar Fase 1** (configurações críticas)
3. 📊 **Setup tracking** (GitHub Projects ou similar)
4. 🤝 **Definir responsáveis** por fase
5. 📅 **Agendar reuniões** de checkpoint semanais

---

*Última atualização: 26 de fevereiro de 2026*
```
