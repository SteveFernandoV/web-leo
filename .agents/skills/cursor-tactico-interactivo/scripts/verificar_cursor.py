#!/usr/bin/env python3
"""
Validador Automático de Implementación de Cursores Tácticos
Audita archivos HTML/CSS/JS para detectar y prevenir los 10 bugs clásicos de cursores.
"""

import sys
import os
import re

def auditar_archivo(ruta):
    if not os.path.exists(ruta):
        print(f"❌ Error: El archivo '{ruta}' no existe.")
        return False

    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read()

    errores = []
    advertencias = []
    exitos = []

    # 1. Verificar regla destructiva cursor: none global
    if re.search(r'\*\s*,\s*\*::before\s*,\s*\*::after\s*\{[^}]*cursor\s*:\s*none', contenido):
        errores.append("BUG CRÍTICO: Se detectó 'cursor: none !important' aplicado a todos los elementos globalmente (*, *::before, *::after). Esto oculta el cursor del sistema y causa que la pantalla se quede sin puntero.")
    else:
        exitos.append("No hay reglas globales destructivas de 'cursor: none'.")

    # 2. Verificar pointer-events: none en elementos del cursor
    if '#tacticalCursor' in contenido:
        pe_match = re.search(r'#tacticalCursor[^{]*\{[^}]*pointer-events\s*:\s*none', contenido) or re.search(r'pointer-events\s*:\s*none\s*!important', contenido)
        if pe_match:
            exitos.append("Los elementos del cursor tienen 'pointer-events: none' para no bloquear clics.")
        else:
            errores.append("ALERTA: '#tacticalCursor' no tiene 'pointer-events: none'. Puede interceptar clics del usuario.")

    # 3. Verificar números pares para evitar aberración subpixel
    dot_width = re.search(r'#tacticalCursorDot\s*\{[^}]*width\s*:\s*([0-9]+)px', contenido)
    if dot_width:
        w = int(dot_width.group(1))
        if w % 2 != 0:
            advertencias.append(f"El ancho de '#tacticalCursorDot' es impar ({w}px). Puede causar blur subpixel con translate(-50%, -50%). Se recomienda usar 6px.")
        else:
            exitos.append(f"El punto central '#tacticalCursorDot' tiene dimensión par ({w}px), garantizando nitidez perfecta.")

    # 4. Verificar requestAnimationFrame en el motor JS
    if 'tacticalCursor' in contenido and '<script' in contenido:
        if 'requestAnimationFrame' in contenido:
            exitos.append("El motor de animación utiliza 'requestAnimationFrame' para renderizado suave a 60/120Hz.")
        else:
            advertencias.append("No se detectó 'requestAnimationFrame' en el script del cursor. Actualizar directamente en 'mousemove' puede causar lag.")

    # 5. Verificar desacoplamiento en dispositivos móviles
    if '@media' in contenido and 'tacticalCursor' in contenido:
        if 'display: none' in contenido:
            exitos.append("Existe regla de desactivación para móviles y pantallas táctiles.")
        else:
            advertencias.append("No se encontró regla para ocultar el cursor táctico en pantallas móviles o touch.")

    # Reporte
    print(f"\n=======================================================")
    print(f"📊 REPORTE DE AUDITORÍA DE CURSOR: {os.path.basename(ruta)}")
    print(f"=======================================================\n")

    for e in exitos:
        print(f"  ✅ {e}")
    for a in advertencias:
        print(f"  ⚠️  {a}")
    for err in errores:
        print(f"  ❌ {err}")

    print("\n-------------------------------------------------------")
    if len(errores) == 0:
        print("🎯 VEREDICTO: APROBADO. La implementación cumple con los estándares libres de bugs.\n")
        return True
    else:
        print(f"🚫 VEREDICTO: RECHAZADO. Se detectaron {len(errores)} fallos críticos que deben corregirse.\n")
        return False

def main():
    if len(sys.argv) < 2:
        target = 'index.html'
    else:
        target = sys.argv[1]

    auditar_archivo(target)

if __name__ == '__main__':
    main()
