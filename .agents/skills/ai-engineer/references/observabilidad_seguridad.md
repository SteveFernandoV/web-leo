# Observabilidad, Seguridad y Control de Costes en Sistemas de IA

Directrices para garantizar la fiabilidad, seguridad y eficiencia económica en aplicaciones LLM de producción.

---

## 1. Guardrails de Seguridad y Mitigación de Riesgos

- **Detección de Prompt Injection & Jailbreaks:**
  - Separación estricta entre instrucciones del sistema (*System Prompts*) y datos de usuario (*User Content*).
  - Uso de delimitadores claros (`<user_input>...</user_input>`) e instrucciones de meta-evaluación.
  - Clasificadores de seguridad previos (ej. Llama Guard, NeMo Guardrails o API de Moderación).
- **Protección de PII (Información Personal Identificable):**
  - Redacción y anonimización de nombres, correos, números de tarjeta o IDs antes de enviar texto a modelos externos.
- **Control de Salidas Estructuradas:**
  - Validación con esquemas estrictos (Pydantic / Zod / JSON Schema) y `response_format` con `strict: true` para prevenir alucinaciones de formato o código malicioso.

---

## 2. Observabilidad y Trazabilidad (Tracing)

- **Instrumentación de Traces:** Trazar cada llamada a LLMs, embeddings, pasos de agentes y herramientas utilizando herramientas como LangSmith, Phoenix (Arize), Weights & Biases o OpenTelemetry.
- **Métricas de Evaluación de RAG (Framework RAGAS):**
  - *Faithfulness (Fidelidad):* ¿La respuesta se basa estrictamente en el contexto recuperado sin alucinar?
  - *Answer Relevance (Relevancia de Respuesta):* ¿La respuesta responde directamente a la pregunta?
  - *Context Precision & Recall:* ¿Los fragmentos recuperados contienen la información exacta requerida?

---

## 3. Optimización de Costes y Latencia

- **Semantic Caching:** Almacenar en caché pares de consulta-respuesta utilizando similitud de embeddings (ej. Redis / GPTCache) para evitar llamadas redundantes a LLMs.
- **Model Routing:** Dirigir consultas sencillas a modelos rápidos y económicos (ej. GPT-4o-mini, Claude 3.5 Haiku, Gemini 1.5 Flash) y reservar modelos insignia (GPT-4o, Claude 3.5 Sonnet) para razonamiento complejo.
- **Context Compression:** Filtrar y resumir fragmentos irrelevantes antes de agregarlos al prompt final, reduciendo el consumo de tokens de entrada hasta en un 50%.
