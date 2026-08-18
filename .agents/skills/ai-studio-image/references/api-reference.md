# Referencia de Modelos e API do Google AI Studio

Guia de modelos para geracao de imagens e integracao via SDK `google-genai`.

---

## 1. Modelos Disponiveis

| Modelo | Tipo / Engine | Velocidade | Qualidade | Custo | Casos de Uso Recomendados |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gemini-2-flash-exp` | Gemini Multimodal | Muito Rapido | Alta | **Gratuito** | **Padrao** — Rascunhos, posts e geracao rapida |
| `imagen-3.0-generate-002` | Imagen 3 | Rapido | Muito Alta | Pago por quota | Alta fidelidade, detalhes fotorrealistas |
| `imagen-4` / `imagen-4-ultra` | Imagen 4 | Medio / Lento | Maxima (2K/4K) | Pago por quota | Impressao, campanhas editoriais e posters |

---

## 2. Parametros de Aspect Ratio (Formatos)

| Formato | Aspect Ratio | Dimensoes Tipicas | Uso Ideal |
| :--- | :--- | :--- | :--- |
| `square` | `1:1` | 1024x1024 | Feed Instagram, avatares, fotos de perfil |
| `portrait` | `3:4` / `4:5` | 1024x1365 | Posts verticais no Instagram, Pinterest |
| `stories` | `9:16` | 1080x1920 | Instagram Stories, TikTok, Reels, Shorts |
| `landscape` | `16:9` | 1920x1080 | YouTube thumbnails, banners, apresentacoes |

---

## 3. Exemplo de Codigo com Google GenAI SDK (Python)

```python
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Geracao com Imagen 3
result = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='Casual candid photo of a person working in a coffee shop, natural window light',
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="1:1",
        person_generation="ALLOW_ADULT",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
    )
)

for generated_image in result.generated_images:
    with open("output.png", "wb") as f:
        f.write(generated_image.image.image_bytes)
```
