# Guia de Instalacao e Configuracao (Setup Guide)

Instrucoes passo a passo para configurar a API do Google AI Studio e o ambiente de execucao para a skill `ai-studio-image`.

---

## 1. Obter a API Key do Google AI Studio

1. Acesse o portal [Google AI Studio](https://aistudio.google.com/apikey).
2. Faca login com sua conta Google.
3. Clique em **"Create API key"** ou copie uma chave existente.

---

## 2. Configurar a Variavel de Ambiente

### macOS / Linux:
```bash
export GEMINI_API_KEY="sua-api-key-aqui"
```
Para persistir a chave no terminal, adicione a linha acima ao seu `~/.zshrc` ou `~/.bashrc`:
```bash
echo 'export GEMINI_API_KEY="sua-api-key-aqui"' >> ~/.zshrc
source ~/.zshrc
```

### Windows (PowerShell / CMD):
```powershell
# PowerShell
$env:GEMINI_API_KEY="sua-api-key-aqui"

# CMD
set GEMINI_API_KEY=sua-api-key-aqui
```

### Arquivo `.env` (Opcional):
Crie um arquivo `.env` na raiz do seu projeto ou no diretorio da skill com:
```env
GEMINI_API_KEY=sua-api-key-aqui
```

---

## 3. Instalacao de Dependencias

Utilizando `pip` ou `uv`:

```bash
pip install -r scripts/requirements.txt
# ou
uv pip install -r scripts/requirements.txt
```
