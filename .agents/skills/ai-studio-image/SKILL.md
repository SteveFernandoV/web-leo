---
name: ai-studio-image
description: >-
  Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e imperfeicoes sutis.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
  - image-generation
  - ai-studio
  - google
  - photography
---

# AI Studio Image — Especialista em Imagens Humanizadas

## Overview

Geração de imagens humanizadas via Google AI Studio (Gemini / Imagen). Fotos realistas estilo influencer ou educacional com iluminação natural e imperfeições sutis.

---

## 1. Documentação de Referencia e Recursos

- 🔧 **[Guia de Instalação e Configuração](./references/setup-guide.md)**: Configuração de `GEMINI_API_KEY` e dependências.
- 📸 **[Engenharia de Prompts Humanizados](./references/prompt-engineering.md)**: As 5 camadas de realismo fotográfico (dispositivo, iluminação, imperfeições, autenticidade e ambiente).
- 📡 **[Referência de Modelos e API](./references/api-reference.md)**: Modelos disponíveis (`gemini-2-flash-exp`, `imagen-3.0-generate-002`, `imagen-4`) e formatos.
- 🎨 **[Catálogo de Templates Prontos](./resources/templates_catalogo.md)**: Cenários pré-configurados (`cafe-lifestyle`, `tutorial-step`, `workspace-minimal`, etc.).

---

## 2. When to Use This Skill

- When the user mentions "gera imagem" or related topics.
- When the user mentions "gerar foto", "criar imagem" or related topics.
- When the user mentions "foto realista", "imagem humanizada" or "foto influencer".

## 3. Do Not Use This Skill When

- The task is unrelated to image generation with Google AI Studio.
- A simpler, more specific tool can handle the request.
- The user needs general-purpose assistance without domain expertise.

---

## 4. Como Funciona

A diferença entre uma imagem de IA genérica e uma foto real está nos detalhes imperceptíveis:
a leve granulação de um sensor de celular, a iluminação que não é perfeita, o enquadramento ligeiramente descentralizado e a profundidade de campo característica de uma lente pequena. Esta skill injeta sistematicamente essas qualidades em cada geração.

---

## 5. Workflow Principal em 5 Passos

### Passo 1: Identificar o Modo
- **`influencer`**: Redes sociais, lifestyle, branding pessoal.
- **`educacional`**: Material didático, tutoriais, apresentações, infográficos.

### Passo 2: Identificar o Formato (Aspect Ratio)
- `square` (`1:1`): Feed Instagram, perfis.
- `portrait` (`3:4` / `4:5`): Posts verticais no Instagram, Pinterest.
- `landscape` (`16:9`): YouTube thumbnails, banners, desktop.
- `stories` (`9:16`): Stories do Instagram, TikTok, Reels, Shorts.

### Passo 3: Transformar o Prompt (Motor de Humanização)
Passe o prompt pelo motor de humanização para injetar as 5 camadas de realismo:
```bash
python scripts/prompt_engine.py --prompt "mulher jovem tomando cafe em cafeteria" --mode influencer --time golden-hour --level natural
```

### Passo 4: Gerar a Imagem
```bash
python scripts/generate.py \
  --prompt "Prompt humanizado gerado no passo anterior" \
  --mode influencer \
  --format square \
  --model imagen-3.0-generate-002 \
  --output outputs/
```

### Passo 5: Apresentar e Iterar
Apresente o resultado ao usuário e ajuste conforme necessário:
- **Iluminação:** `morning`, `golden-hour`, `midday`, `overcast`, `night`, `indoor`.
- **Nível de Humanização:** `ultra` (máximo realismo celular), `natural` (padrão balanceado), `polished`, `editorial`.

---

## 6. Modelos Recomendados

| Modelo | Velocidade | Qualidade | Custo | Uso Ideal |
| :--- | :--- | :--- | :--- | :--- |
| `gemini-2-flash-exp` | Rápido | Alta | **Gratuito** | **Padrão — Rápido e econômico** |
| `imagen-3.0-generate-002` | Rápido | Muito Alta | Quota padrão | **Alta fidelidade fotorrealista** |
| `imagen-4` / `imagen-4-ultra` | Médio | Máxima | Quota avançada | Impressão e resoluções elevadas |

---

## 7. Troubleshooting

| Problema | Solução |
| :--- | :--- |
| `GEMINI_API_KEY not found` | Configure a variável de ambiente (`export GEMINI_API_KEY="..."`) ou crie `.env` |
| `quota exceeded` | Aguarde reset do rate limit ou ajuste de quota no Google AI Studio |
| `image blocked` | Ajuste o prompt — termos sensíveis acionaram o filtro de segurança |
| `low quality output` | Aumente o nível de humanização para `ultra` ou use `imagen-3.0-generate-002` |
