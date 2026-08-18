# Guía de Diseño y Buenas Prácticas para Habilidades

Esta guía explica los principios de diseño recomendados por Google Antigravity para construir habilidades eficientes, robustas y de alto rendimiento.

---

## 1. Principio de Divulgación Progresiva (*Progressive Disclosure*)

Para evitar saturar la ventana de contexto (*context window*) del modelo con información innecesaria:

1. **`SKILL.md` Conciso:** Mantén las instrucciones centrales, los pasos del flujo y las reglas de decisión en el archivo raíz `SKILL.md`.
2. **Subdirectorios Especializados:**
   - **`references/`**: Documentación extensa, hojas de referencia, especificaciones de APIs o esquemas de base de datos.
   - **`resources/`**: Plantillas estáticas de código, archivos de configuración base, prompts o assets.
   - **`examples/`**: Casos prácticos y ejemplos completos de entrada/salida.
   - **`scripts/`**: Scripts auxiliares ejecutables (Python, Bash, Node.js).
3. **Enlaces Relativos:** Enlaza desde `SKILL.md` a estos archivos mediante enlaces Markdown relativos (ej. `[Guía de API](./references/api.md)`). El agente solo leerá esos archivos cuando los necesite.

---

## 2. Enfoque Modular y Único Objetivo (*Single Responsibility*)

- **Una habilidad debe resolver un dominio o flujo de trabajo específico.**
  - *Buen ejemplo:* `revision-codigo`, `migracion-base-datos`, `despliegue-cloud-run`.
  - *Mal ejemplo:* `herramientas-desarrollo-general` (demasiado amplio e impreciso).
- Si un flujo complejo requiere varios pasos especializados, crea habilidades separadas y haz que una habilidad orquestadora haga referencia a las demás.

---

## 3. Patrón de Scripts como "Caja Negra" (*Black Box*)

Si una habilidad requiere interactuar con APIs externas, procesar grandes volúmenes de datos o ejecutar comandos complejos:

- **Empaqueta la lógica en scripts** dentro de la carpeta `scripts/`.
- **Escribe salidas a archivos** (ej. formato JSON) en lugar de imprimirlas por salida estándar (`stdout`) para evitar truncamientos y ahorrar tokens.
- **Instruye al agente a ejecutar con `--help`** para descubrir argumentos de forma autónoma.
- Utiliza gestores modernos como `uv` para scripts en Python: `uv run scripts/mi_script.py --arg valor`.

---

## 4. Árboles de Decisión y Manejo de Errores

Incluye siempre en tu habilidad:

- **Estrategia ante fallos:** Qué debe hacer el agente si un paso falla (ej. si una API responde error 404 vs 429, reintentos con backoff, o solicitar confirmación al usuario).
- **Criterios de verificación:** Cómo comprobar de manera concluyente que la tarea se realizó con éxito (ej. ejecutar tests, verificar logs, revisar estado de archivos generados).
