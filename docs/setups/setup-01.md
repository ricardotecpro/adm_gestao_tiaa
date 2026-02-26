# Setup Windows 💻

Configuração completa do ambiente de estudo para o curso de Tecnologia da Informação aplicada à Administração no Windows.

!!! tip "Pré-requisitos" - Windows 10 ou superior - Conexão com a internet - Usuário com privilégios de administrador

---

## 🔧 Ferramentas Essenciais

### 1. Navegadores Web

**Microsoft Edge (Recomendado)**

- Já vem instalado no Windows
- Ferramenta de desenvolvedor integrada `F12`
- Suporte completo para aplicações web modernas

**Google Chrome (Alternativa)**

```powershell
# Via Chocolatey (opcional)
choco install googlechrome
```

### 2. Editores de Código

**Visual Studio Code**

- [:material-download: Download direto](https://code.visualstudio.com/)
- Editor leve e poderoso para desenvolvimento
- Extensões úteis:
  - Live Server
  - Prettier
  - Python
  - Excel Viewer

```powershell
# Via Chocolatey
choco install vscode
```

**Notepad++ (Editor simples)**

```powershell
# Via Chocolatey
choco install notepadplusplus
```

---

## 📊 Ferramentas de Produtividade

### 1. Microsoft Office / LibreOffice

**Microsoft Office 365 (Recomendado)**

- Excel para análise de dados e planilhas
- Word para documentação
- PowerPoint para apresentações
- Access para bancos de dados básicos

**LibreOffice (Alternativa Gratuita)**

- [:material-download: Download LibreOffice](https://pt-br.libreoffice.org/)

```powershell
# Via Chocolatey
choco install libreoffice-fresh
```

### 2. Gerenciadores de Arquivos

**7-Zip (Compactador)**

```powershell
choco install 7zip
```

---

## 🌐 Ferramentas de Internet e Comunicação

### 1. WhatsApp Desktop

```powershell
# Via Microsoft Store ou Chocolatey
choco install whatsapp
```

### 2. Teams / Zoom

```powershell
# Microsoft Teams
choco install microsoft-teams

# Zoom
choco install zoom
```

---

## 🖥️ Ferramentas de Sistema

### 1. Windows Terminal (Recomendado)

```powershell
# Via Microsoft Store (busque por "Windows Terminal")
# Ou via Chocolatey
choco install microsoft-windows-terminal
```

### 2. PowerToys (Utilitários do Windows)

```powershell
choco install powertoys
```

**Recursos úteis do PowerToys:**

- PowerRename: Renomeação em lote de arquivos
- FancyZones: Organização de janelas
- PowerLauncher: Launcher similar ao Spotlight do Mac

---

## 📱 Emuladores (Opcional)

Para estudar sistemas móveis empresariais:

**BlueStacks (Android)**

- [:material-download: Download BlueStacks](https://www.bluestacks.com/)
- Útil para testar aplicativos empresariais

---

## 🔧 Instalação via Package Manager

O **Chocolatey** facilita a instalação de ferramentas:

<!-- termynal -->

```powershell
# Instalar Chocolatey (executar como Administrador)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar ferramentas essenciais
choco install googlechrome vscode notepadplusplus 7zip libreoffice-fresh microsoft-teams powertoys -y

# Verificar instalações
choco list --local-only
```

---

## ✅ Validação da Instalação

Execute no PowerShell para verificar:

<!-- termynal -->

```powershell
echo "=== Validação do Ambiente Windows ==="
echo ""

echo "1. Chocolatey:"
choco --version

echo "2. VS Code:"
code --version

echo "3. Navegador (Edge):"
Get-AppxPackage -Name "Microsoft.MicrosoftEdge*" | Select Name, Version

echo ""
echo "✅ Ambiente configurado com sucesso!"
```

---

## 📚 Próximos Passos

1. **Configure o VS Code** - Instale extensões recomendadas
2. **Teste o Office** - Abra Excel e crie uma planilha de exemplo
3. **Organize pastas** - Crie estrutura para materiais do curso
4. **Inicie o curso** - Vá para a [Aula 01](../aulas/aula-01.md)

!!! success "Ambiente Pronto!"
Seu Windows está configurado para o curso de TI aplicada à Administração. Em caso de problemas, consulte a documentação oficial dos programas ou entre em contato.

---

[:material-arrow-left: Voltar aos Setups](index.md) | [:material-play: Iniciar Aula 01](../aulas/aula-01.md)
