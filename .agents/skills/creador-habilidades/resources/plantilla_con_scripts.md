# Plantilla: Habilidad Basada en Scripts / Herramientas (CLI Pattern)

Utiliza esta plantilla cuando la habilidad incluya scripts auxiliares en la carpeta `scripts/` (ej. scripts en Python, Bash o Node.js) para interactuar con APIs o procesar datos.

---

```markdown
---
name: nombre-de-la-habilidad-tecnica
description: >-
  Describe cuándo y cómo usar esta herramienta técnica.
  Ejemplo: "Ejecuta análisis de dependencias y auditoría de seguridad en proyectos Node.js utilizando scripts automatizados."
---

# Título de la Habilidad Técnica

## 1. Visión General
Descripción del propósito y capacidades automatizadas por los scripts.

## 2. Scripts Disponibles

### Script: `scripts/mi_script.py`
- **Propósito:** [Descripción del objetivo del script]
- **Comando de ejecución:**
  ```bash
  uv run scripts/mi_script.py [subcomando] --opcion valor --output ruta/al/resultado.json
  ```
- **Parámetros principales:**
  - `--parametro1`: [Descripción]
  - `--output`: Ruta al archivo de destino para volcar el resultado en JSON.

## 3. Flujo de Ejecución

1. **Inspección de Ayuda:** Si es necesario conocer opciones adicionales, ejecuta:
   `uv run scripts/mi_script.py --help`
2. **Ejecución del Comando:** Invoca el script enviando la salida a un archivo en la carpeta temporal o directorio del proyecto.
3. **Análisis de Salida:** Lee el archivo generado para procesar únicamente los datos relevantes sin saturar el contexto.

## 4. Manejo de Errores y Límites de Tasa (Rate Limiting)
- **Límites de API:** [Detalles sobre cuotas o tiempos de espera]
- **En caso de error HTTP 429 (Too Many Requests):** Esperar con retroceso exponencial (*exponential backoff*).
- **En caso de error 5xx:** Reintentar hasta 3 veces.

## 5. Verificación
Verificar que el archivo de salida contenga los campos requeridos y que no se hayan producido errores de ejecución.
```
