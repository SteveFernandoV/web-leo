# Plantillas de Implementación de Sistemas RAG y Agentes

Patrones de código listos para producción para construir pipelines RAG y grafos de agentes con LangGraph / Pydantic.

---

## 1. Pipeline RAG con Búsqueda Híbrida y Reranker (Python / FastAPI)

```python
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import os

class QueryRequest(BaseModel):
    query: str = Field(..., description="Pregunta del usuario")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Metadatos para filtrado")
    top_k: int = Field(default=5, ge=1, le=20)

class RAGResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]]
    confidence_score: float

class ProductionRAGService:
    def __init__(self, vector_store, reranker_client, llm_client):
        self.vector_store = vector_store
        self.reranker = reranker_client
        self.llm = llm_client

    async def execute_pipeline(self, request: QueryRequest) -> RAGResponse:
        # 1. Recuperación Híbrida (Vector + BM25)
        raw_candidates = await self.vector_store.hybrid_search(
            query=request.query,
            filters=request.filters,
            limit=request.top_k * 3
        )

        # 2. Reranking de Alta Precisión
        reranked_docs = await self.reranker.rerank(
            query=request.query,
            documents=[doc.text for doc in raw_candidates],
            top_n=request.top_k
        )

        # 3. Construcción de Contexto y Prompt Seguro
        context = "\n\n".join([f"Fuente [{i+1}]: {doc.text}" for i, doc in enumerate(reranked_docs)])
        
        system_prompt = (
            "Eres un asistente de conocimiento empresarial experto. "
            "Responde estrictamente basándote en el contexto provisto. "
            "Si el contexto no contiene la información, declara explícitamente que no está disponible."
        )

        # 4. Generación con LLM
        response = await self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=f"Contexto:\n{context}\n\nPregunta: {request.query}",
            temperature=0.1
        )

        return RAGResponse(
            answer=response.text,
            sources=[{"index": i+1, "metadata": doc.metadata} for i, doc in enumerate(reranked_docs)],
            confidence_score=response.confidence or 0.95
        )
```

---

## 2. Orquestación de Agente React con Herramientas (LangGraph / StateGraph)

```python
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], "Lista ordenada de mensajes"]
    intermediate_steps: list

def build_production_agent(llm_with_tools, tools_list):
    workflow = StateGraph(AgentState)

    # Definir Nodos
    def call_model(state: AgentState):
        messages = state["messages"]
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools_list)

    # Registrar Nodos
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)

    # Definir Condiciones de Enrutamiento
    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        if last_message.tool_calls:
            return "tools"
        return END

    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue)
    workflow.add_edge("tools", "agent")

    return workflow.compile()
```
