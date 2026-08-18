# Arquitectura Offline-First y Sincronización de Datos en Móvil

Estrategias para construir aplicaciones móviles resilientes ante pérdidas de conectividad o redes inestables.

---

## 1. Patrón de Almacenamiento Local y Caché

### React Native:
- **SQLite / Expo SQLite:** Base de datos relacional embebida para consultas complejas y filtrados locales.
- **MMKV / WatermelonDB:** Almacenamiento clave-valor de ultra alta velocidad para configuraciones, tokens y colecciones reactivas.
- **TanStack Query (React Query) + Persister:** Caché asíncrono con persistencia automática en AsyncStorage/MMKV.

### Flutter:
- **Isar / Hive:** Bases de datos NoSQL ultrarrápidas en memoria/disco con soporte para tipos Dart nativos.
- **Drift (Moor):** Capa de persistencia relacional SQL tipada con streams reactivos.

---

## 2. Cola de Mutaciones y Sincronización (*Mutation Queue*)

```text
┌─────────────────────────────────────────────────────────────┐
│                    Acción del Usuario                       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
            ┌────────────────────────────────────┐
            │   Actualización Optimista en UI    │
            └──────────────────┬─────────────────┘
                               │
                               ▼
            ┌────────────────────────────────────┐
            │   Guardado en Base de Datos Local  │
            │     (Estado: pending_sync = true)  │
            └──────────────────┬─────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
       [ Conexión Online ]            [ Sin Conexión ]
                │                             │
                ▼                             ▼
     ┌──────────────────────┐      ┌──────────────────────┐
     │ Envío a API / Backend│      │ Encolar en Cola Local│
     │                      │      │ (Reintento automático│
     │ pending_sync = false │      │  al recuperar red)   │
     └──────────────────────┘      └──────────────────────┘
```

---

## 3. Resolución de Conflictos

- **Last-Write-Wins (LWW):** Se utiliza la marca de tiempo (*timestamp*) UTC del servidor para resolver colisiones simples.
- **Server-Wins / Client-Wins:** Estrategia determinista según la criticidad del dato.
- **Diff / Merge Manual:** Para documentos colaborativos o datos complejos, registrar historial de revisiones y solicitar resolución si hay discrepancia.
