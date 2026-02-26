# Setup macOS 🍎

Configuração do ambiente de estudos para usuários macOS, incluindo ferramentas essenciais para o curso de Tecnologia da Informação aplicada à Administração.

!!! tip "Pré-requisitos" - macOS 10.14 (Mojave) ou superior - Conexão com a internet - Usuário com privilégios de administrador

---

## 🏗️ Instalação do Homebrew

O Homebrew é o gerenciador de pacotes mais popular para macOS.

<!-- termynal -->

```bash
# Instalar Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verificar instalação
brew --version

# Atualizar Homebrew
brew update
```

---

## 💻 Ferramentas Essenciais

### 1. Git (Controle de Versão)

<!-- termynal -->

```bash
# Git via Homebrew
brew install git

# Verificar instalação
git --version

# Configuração inicial
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### 2. Visual Studio Code

<!-- termynal -->

```bash
# Instalar VS Code via Homebrew
brew install --cask visual-studio-code

# Verificar instalação
code --version
```

### 3. Node.js (para ferramentas web)

<!-- termynal -->

```bash
# Instalar Node.js
brew install node

# Verificar instalação
node --version
npm --version
```

---

## 🌐 Navegadores e Ferramentas Web

### Chrome (recomendado)

<!-- termynal -->

```bash
# Instalar Chrome
brew install --cask google-chrome
```

### Ferramentas de API

<!-- termynal -->

```bash
# Instalar Postman para testes de API
brew install --cask postman

# Alternativa: Insomnia
brew install --cask insomnia
```

---

## 📊 Ferramentas de Produtividade

### LibreOffice (alternativa gratuita ao Office)

<!-- termynal -->

```bash
# Instalar LibreOffice
brew install --cask libreoffice
```

### Diagrama e Modelagem

<!-- termynal -->

```bash
# Instalar Draw.io (diagrama)
brew install --cask drawio

# Instalar GraphViz para diagramas
brew install graphviz
```

---

## 🛠️ Configurações do Sistema

### 1. Mostrar Arquivos Ocultos

<!-- termynal -->

```bash
# Mostrar arquivos ocultos no Finder
defaults write com.apple.finder AppleShowAllFiles TRUE
killall Finder
```

### 2. Configurar Terminal

!!! tip "Terminal Customizado" - Abra o Terminal (Applications > Utilities > Terminal) - Vá em Terminal > Preferences > Profiles - Escolha uma aparência que facilite a leitura

---

## 🔧 Validação da Instalação

Execute estes comandos para verificar se tudo foi instalado corretamente:

<!-- termynal -->

```bash
# Verificar todas as ferramentas
echo "=== Validação do Ambiente macOS ==="
echo ""

echo "1. Homebrew:"
brew --version

echo "2. Git:"
git --version

echo "3. VS Code:"
code --version

echo "4. Node.js:"
node --version

echo "5. NPM:"
npm --version

echo ""
echo "✅ Ambiente configurado com sucesso!"
```

---

## 📚 Próximos Passos

Com seu ambiente configurado:

1. **Explore o VS Code** - Instale extensões úteis (Live Server, GitLens)
2. **Teste o Git** - Clone um repositório de exemplo
3. **Familiarize-se com o Terminal** - Pratique comandos básicos
4. **Inicie o curso** - Vá para a [Aula 01](../aulas/aula-01.md)

!!! success "Ambiente Pronto!"
Seu macOS está configurado para o curso. Em caso de problemas, consulte a documentação oficial dos programas ou entre em contato.

---

[:material-arrow-left: Voltar aos Setups](index.md) | [:material-play: Iniciar Aula 01](../aulas/aula-01.md)
