# Setup Linux 🐧

Configuração do ambiente de estudos para usuários Linux no curso de Tecnologia da Informação aplicada à Administração.

!!! tip "Pré-requisitos" - Ubuntu 20.04+ ou distribuição equivalente - Conexão com a internet - Usuário com privilégios sudo

---

## 🔧 Atualização do Sistema

Sempre comece atualizando o sistema:

<!-- termynal -->

```bash
# Atualizar lista de pacotes
sudo apt update

# Atualizar sistema
sudo apt upgrade -y

# Instalar curl e wget (se não tiver)
sudo apt install curl wget -y
```

---

## 🌐 Navegadores Web

### Firefox (Geralmente pré-instalado)

<!-- termynal -->

```bash
# Verificar se está instalado
firefox --version

# Instalar se necessário
sudo apt install firefox -y
```

### Google Chrome

<!-- termynal -->

```bash
# Baixar e instalar Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install google-chrome-stable -y
```

---

## 💻 Editores de Código

### Visual Studio Code

<!-- termynal -->

```bash
# Via Snap (mais fácil)
sudo snap install code --classic

# Ou via repositório oficial
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y
```

### Vim/Nano (Editor de terminal)

<!-- termynal -->

```bash
# Vim (editor avançado)
sudo apt install vim -y

# Nano (editor simples)
sudo apt install nano -y
```

---

## 📊 Suíte de Escritório

### LibreOffice

<!-- termynal -->

```bash
# Instalação completa do LibreOffice
sudo apt install libreoffice libreoffice-l10n-pt-br -y

# Verificar instalação
libreoffice --version
```

### OnlyOffice (Alternativa moderna)

<!-- termynal -->

```bash
# Via Flatpak
sudo apt install flatpak -y
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo flatpak install flathub org.onlyoffice.desktopeditors -y
```

---

## 🛠️ Ferramentas de Sistema

### Git (Controle de versão)

<!-- termynal -->

```bash
# Instalar Git
sudo apt install git -y

# Configurar Git
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"

# Verificar configuração
git config --list
```

### Gerenciadores de Arquivo e Compactação

<!-- termynal -->

```bash
# 7-zip
sudo apt install p7zip-full p7zip-rar -y

# Unrar
sudo apt install unrar -y

# Tree (visualizar estrutura de pastas)
sudo apt install tree -y
```

---

## 📱 Comunicação

### Discord/Teams

<!-- termynal -->

```bash
# Discord via Snap
sudo snap install discord

# Teams via Flatpak
sudo flatpak install flathub com.microsoft.Teams -y
```

### WhatsApp (via WhatsApp Web)

- Use o navegador para acessar [web.whatsapp.com](https://web.whatsapp.com)
- Ou instale via Snap: `sudo snap install whatsapp-for-linux`

---

## 🖥️ Terminal Avançado

### Zsh + Oh My Zsh (Opcional)

<!-- termynal -->

```bash
# Instalar Zsh
sudo apt install zsh -y

# Instalar Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Definir como shell padrão
chsh -s $(which zsh)
```

### Terminator (Terminal multipainéis)

<!-- termynal -->

```bash
# Instalar Terminator
sudo apt install terminator -y
```

---

## 🎨 Customização (Opcional)

### GNOME Tweaks (para Ubuntu com GNOME)

<!-- termynal -->

```bash
sudo apt install gnome-tweaks -y
```

---

## ✅ Validação da Instalação

<!-- termynal -->

```bash
echo "=== Validação do Ambiente Linux ==="
echo ""

echo "1. Sistema:"
lsb_release -a

echo "2. Git:"
git --version

echo "3. VS Code:"
code --version

echo "4. LibreOffice:"
libreoffice --version

echo "5. Firefox:"
firefox --version

echo ""
echo "✅ Ambiente configurado com sucesso!"
```

---

## 🔧 Solução de Problemas

### Permissões de Arquivo

```bash
# Se tiver problemas de permissão
sudo chown -R $USER:$USER /home/$USER/.config
```

### Snap não funciona

```bash
# Reinstalar snapd
sudo apt remove --purge snapd -y
sudo apt install snapd -y
sudo systemctl enable --now snapd
```

---

## 📚 Próximos Passos

1. **Configure o VS Code** - Instale extensões recomendadas
2. **Teste o LibreOffice** - Crie uma planilha de exemplo
3. **Organize o workspace** - Crie pastas para materiais do curso
4. **Inicie o curso** - Vá para a [Aula 01](../aulas/aula-01.md)

!!! success "Ambiente Pronto!"
Seu Linux está configurado para o curso. Em caso de problemas específicos da sua distribuição, consulte a documentação oficial.

---

[:material-arrow-left: Voltar aos Setups](index.md) | [:material-play: Iniciar Aula 01](../aulas/aula-01.md)
