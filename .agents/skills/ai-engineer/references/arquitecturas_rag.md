# Arquitecturas RAG Avanzadas y Estrategias de Recuperación

Guía de referencia técnica para el diseño de sistemas RAG (*Retrieval-Augmented Generation*) de nivel empresarial.

---

## 1. Estrategias de Chunking (Fragmentación)

- **Semantic Chunking:** Divide documentos según la similitud de embeddings entre oraciones consecutivas, preservando la cohesión temática.
- **Recursive Character Splitting:** Algoritmo por defecto con jerarquía de separadores (`\n\n`, `\n`, `.`, ` `) para mantener fragmentos homogéneos respetando límites naturales de texto.
- **Document-Structure Aware:** Fragmentación basada en etiquetas HTML/Markdown (`#`, `##`, `<table>`, `<section>`) para preservar tablas y relaciones jerárquicas.
- **Sliding Window:** Fragmentos con superposición (*overlap*) del 10% al 20% para asegurar continuidad de contexto en los bordes.

---

## 2. Búsqueda Híbrida (*Hybrid Search*) & Reranking

```text
               ┌───────────────────────┐
               │    Consulta Usuario   │
               └───────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
  ┌─────────────────────┐     ┌─────────────────────┐
  │  Búsqueda Vectorial │     │  Búsqueda Léxica    │
  │  (Cosine / Dense)   │     │  (BM25 / Sparse)    │
  └──────────┬──────────┘     └──────────┬──────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
              ┌─────────────────────────┐
              │   Reciprocal Rank Fusion │
              │          (RRF)          │
              └────────────┬────────────┘
                           ▼
              ┌─────────────────────────┐
              │   Cross-Encoder Reranker│
              │  (Cohere / BGE-Rerank)  │
              └────────────┬────────────┘
                           ▼
              ┌─────────────────────────┐
              │ Top-K Fragmentos al LLM │
              └─────────────────────────┘
```

- **Fórmula de Fusión RRF:** Combina los rankings de búsqueda densa y léxica asignando puntuaciones normalizadas:
  $$RRF(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$ (donde normalmente $k = 60$).
- **Cross-Encoder Reranker:** Modela la atención cruzada entre la consulta completa y cada fragmento candidato para reordenar con máxima precisión semántica.

---

## 3. Patrones RAG Avanzados

- **HyDE (Hypothetical Document Embeddings):** El LLM genera una respuesta hipotética ideal y se utiliza el embedding de esa respuesta para buscar en la base vectorial, resolviendo la discrepancia léxica entre preguntas y respuestas.
- **RAG-Fusion:** Genera múltiples variaciones de la consulta original, ejecuta búsquedas paralelas y fusiona los resultados mediante RRF.
- **GraphRAG:** Extrae entidades y relaciones para construir un grafo de conocimiento estructurado que permite razonamiento holístico sobre colecciones masivas de documentos.
- **Self-RAG & Corrective RAG (CRAG):** El agente evalúa dinámicamente si los fragmentos recuperados son suficientes o relevantes; si no lo son, reescribe la consulta o busca en fuentes externas (Web Search).
