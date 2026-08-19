import re
import os
import base64
import hashlib

def execute_all_structural_fixes():
    base_dir = '/Users/stevefernandovelarde/Desktop/web leo'
    assets_dir = os.path.join(base_dir, 'assets/images')
    os.makedirs(assets_dir, exist_ok=True)

    index_path = os.path.join(base_dir, 'index.html')
    mirror_path = os.path.join(base_dir, 'Happy_Tactical_Home_Mobile_Ordenado_V3-2.html')
    admin_path = os.path.join(base_dir, 'admin.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"📦 Tamaño inicial de index.html: {len(html)/1024:.1f} KB")

    # =========================================================================
    # 1. EXTRACT & DEDUPLICATE BASE64 IMAGES
    # =========================================================================
    matches = list(re.finditer(r'data:image/(png|jpeg|jpg|webp);base64,([A-Za-z0-9+/=]{100,})', html))
    print(f"🔍 Extrayendo {len(matches)} imágenes Base64 a assets/images/...")
    
    extracted_map = {}
    for m in matches:
        b64_str = m.group(0)
        ext = 'png' if m.group(1) == 'png' else 'jpg'
        b64_raw = m.group(2)
        img_hash = hashlib.md5(b64_raw.encode('utf-8')).hexdigest()[:8]
        filename = f"img_{img_hash}.{ext}"
        filepath = os.path.join(assets_dir, filename)

        if not os.path.exists(filepath):
            try:
                with open(filepath, 'wb') as img_f:
                    img_f.write(base64.b64decode(b64_raw))
                print(f"  ✓ Guardada imagen: {filename} ({len(b64_raw)//1024} KB)")
            except Exception as e:
                print(f"  ❌ Error decodificando imagen: {e}")

        rel_path = f"assets/images/{filename}"
        extracted_map[b64_str] = rel_path

    # Replace in html
    for b64_str, rel_path in extracted_map.items():
        html = html.replace(b64_str, rel_path)

    # =========================================================================
    # 2. PURGE ALL LEGACY / DEAD CURSOR STYLES & SCRIPT
    # =========================================================================
    # Remove any existing legacy cursor divs
    html = re.sub(r'<div id=\"(?:aiTacticalCursor|hudCursorDot|hudCursorRing|tacticalProximityRing|tacticalLaserDot|aiCursorRipple)\"[\s\S]*?</div>\s*</div>', '', html)
    html = re.sub(r'<div id=\"(?:aiTacticalCursor|hudCursorDot|hudCursorRing|tacticalProximityRing|tacticalLaserDot|aiCursorRipple)\"[^>]*></div>', '', html)
    html = re.sub(r'<canvas id=\"aiCursorTrailCanvas\"[^>]*></canvas>', '', html)

    # Remove any legacy cursor scripts
    html = re.sub(r'// --- Tactical Proximity Ring Engine[\s\S]*?\}\)\(\);', '', html)
    html = re.sub(r'// --- Tactical Reticle Cursor[\s\S]*?\}\)\(\);', '', html)
    html = re.sub(r'// --- AI Tactical Combat HUD Cursor[\s\S]*?\}\)\(\);', '', html)
    html = re.sub(r'// --- Ultra Interactive Tactical Cursor[\s\S]*?\}\)\(\);', '', html)

    # Remove legacy cursor CSS
    html = re.sub(r'/\* =+ (?:AI GENERATED TACTICAL|PERFECT CUSTOM|ULTRA-INTERACTIVE|ARO TÁCTICO|TACTICAL RETICLE)[\s\S]*?/\* =+', '/* =+', html)
    html = re.sub(r'\.tactical-reticle[^{}]*\{[^}]*\}', '', html)
    html = re.sub(r'#aiTacticalCursor[^{}]*\{[^}]*\}', '', html)
    html = re.sub(r'#tacticalProximityRing[^{}]*\{[^}]*\}', '', html)
    html = re.sub(r'#tacticalLaserDot[^{}]*\{[^}]*\}', '', html)

    # =========================================================================
    # 3. FIX 3D TRANSFORMATIONS ON BUTTONS & CONTAINERS
    # =========================================================================
    # Clean .hero-actions transform: translateZ(22px)
    html = html.replace('transform: translateZ(22px);', '/* 2D flat container */')
    html = html.replace('transform: perspective(600px) translateZ(0);', '')
    html = html.replace('transform-style: preserve-3d;', '')

    # Fix ctx.scale in canvas
    html = html.replace('ctx.scale(dpr, dpr);', 'ctx.setTransform(dpr, 0, 0, dpr, 0, 0);')

    # =========================================================================
    # 4. INJECT SINGLE DEFINITIVE TACTICAL HUD CURSOR (DESKTOP ONLY)
    # =========================================================================
    cursor_css = """
    /* ========================================================================
       SISTEMA ÚNICO DE CURSOR TÁCTICO HUD DE ALTA PRECISIÓN (DESKTOP ONLY)
       ======================================================================== */
    @media (hover: hover) and (pointer: fine) {
      body {
        cursor: default;
      }
      a, button, [role="button"], select, .btn {
        cursor: pointer;
      }
      input, textarea {
        cursor: text !important;
      }

      /* Punto Central Milimétrico */
      .hud-cursor-dot {
        position: fixed;
        top: 0;
        left: 0;
        width: 6px;
        height: 6px;
        margin: -3px 0 0 -3px;
        background: #00e5ff;
        border-radius: 50%;
        pointer-events: none !important;
        z-index: 2147483647;
        box-shadow: 0 0 8px #00e5ff, 0 0 2px #fff;
        opacity: 0;
        transition: opacity 0.2s ease, transform 0.05s linear, background-color 0.2s ease;
        will-change: transform;
      }
      .hud-cursor-dot::after {
        content: '';
        position: absolute;
        top: 2px;
        left: 2px;
        width: 2px;
        height: 2px;
        background: #ff007f;
        border-radius: 50%;
      }
      .hud-cursor-dot.visible {
        opacity: 1;
      }
      .hud-cursor-dot.text-mode {
        opacity: 0.15;
      }

      /* Aro Táctico Exterior con Resorte Suave */
      .hud-cursor-ring {
        position: fixed;
        top: 0;
        left: 0;
        width: 36px;
        height: 36px;
        margin: -18px 0 0 -18px;
        border: 1.5px dashed rgba(0, 229, 255, 0.65);
        border-radius: 50%;
        pointer-events: none !important;
        z-index: 2147483646;
        opacity: 0;
        box-sizing: border-box;
        transition: width 0.25s cubic-bezier(0.16, 1, 0.3, 1),
                    height 0.25s cubic-bezier(0.16, 1, 0.3, 1),
                    margin 0.25s cubic-bezier(0.16, 1, 0.3, 1),
                    border-color 0.25s ease,
                    box-shadow 0.25s ease,
                    opacity 0.2s ease,
                    transform 0.08s ease-out;
        will-change: transform, width, height, margin;
      }
      .hud-cursor-ring.visible {
        opacity: 1;
      }

      /* 4 Corchetes Tácticos */
      .hud-cursor-ring .ring-bracket {
        position: absolute;
        width: 6px;
        height: 6px;
        border-color: #00e5ff;
        border-style: solid;
        pointer-events: none;
        opacity: 0.8;
        transition: all 0.25s ease;
      }
      .hud-cursor-ring .ring-bracket.top-left {
        top: -2px; left: -2px; border-width: 1.5px 0 0 1.5px;
      }
      .hud-cursor-ring .ring-bracket.top-right {
        top: -2px; right: -2px; border-width: 1.5px 1.5px 0 0;
      }
      .hud-cursor-ring .ring-bracket.bottom-left {
        bottom: -2px; left: -2px; border-width: 0 0 1.5px 1.5px;
      }
      .hud-cursor-ring .ring-bracket.bottom-right {
        bottom: -2px; right: -2px; border-width: 0 1.5px 1.5px 0;
      }

      /* Estado de Fijación Táctica (Lock-On al entrar en botones) */
      .hud-cursor-ring.active-lock {
        width: 52px;
        height: 52px;
        margin: -26px 0 0 -26px;
        border: 1.5px solid rgba(0, 229, 255, 0.95);
        box-shadow: 0 0 16px rgba(0, 229, 255, 0.5), inset 0 0 8px rgba(0, 229, 255, 0.25);
        animation: hudRingPulse 1.8s infinite ease-in-out;
      }
      .hud-cursor-ring.active-lock .ring-bracket {
        border-color: #ff007f;
        width: 8px;
        height: 8px;
        opacity: 1;
      }

      /* Micro-pulso al hacer Click */
      .hud-cursor-ring.clicking {
        transform: scale(0.82) !important;
        border-color: #ff007f !important;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.7) !important;
      }

      /* Modo Texto: Ocultar aro para no molestar */
      .hud-cursor-ring.text-mode {
        opacity: 0 !important;
      }
    }

    @keyframes hudRingPulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.06); }
    }

    /* En Móvil y Pantallas Táctiles: Cero Cursor Personalizado */
    @media (pointer: coarse), (hover: none) {
      .hud-cursor-dot, .hud-cursor-ring {
        display: none !important;
      }
    }
    """

    # Inject CSS before </style>
    style_end_pos = html.find('</style>')
    if style_end_pos != -1:
        html = html[:style_end_pos] + "\n" + cursor_css + "\n" + html[style_end_pos:]

    # Inject HTML DOM elements before </body>
    cursor_dom = """
  <!-- SISTEMA ÚNICO DE CURSOR TÁCTICO HUD -->
  <div id="hudCursorDot" class="hud-cursor-dot" aria-hidden="true"></div>
  <div id="hudCursorRing" class="hud-cursor-ring" aria-hidden="true">
    <div class="ring-bracket top-left"></div>
    <div class="ring-bracket top-right"></div>
    <div class="ring-bracket bottom-left"></div>
    <div class="ring-bracket bottom-right"></div>
  </div>
    """
    body_end_pos = html.find('</body>')
    if body_end_pos != -1:
        html = html[:body_end_pos] + "\n" + cursor_dom + "\n" + html[body_end_pos:]

    # Inject definitive single JS engine before </script>
    cursor_js = """
    // ========================================================================
    // MOTOR DEFINITIVO DE CURSOR TÁCTICO HUD (SOLO ESCRITORIO CON NATIVE HOVER)
    // ========================================================================
    (function initHudCursorEngine() {
      const isFinePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
      if (!isFinePointer) return; // En móvil o pantallas táctiles no ejecutar nada

      const dot = document.getElementById('hudCursorDot');
      const ring = document.getElementById('hudCursorRing');
      if (!dot || !ring) return;

      let mouseX = window.innerWidth / 2;
      let mouseY = window.innerHeight / 2;
      let ringX = mouseX;
      let ringY = mouseY;
      let isVisible = false;
      let isRafRunning = false;

      // Actualizar posición del cursor instantáneamente
      function onPointerMove(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;

        if (!isVisible) {
          isVisible = true;
          dot.classList.add('visible');
          ring.classList.add('visible');
          ringX = mouseX;
          ringY = mouseY;
        }

        // El punto sigue al mouse en coordenadas exactas
        dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;

        if (!isRafRunning) {
          isRafRunning = true;
          requestAnimationFrame(updateRingPosition);
        }
      }

      // Interpolación suave del aro con resorte (lerp = 0.22)
      function updateRingPosition() {
        ringX += (mouseX - ringX) * 0.22;
        ringY += (mouseY - ringY) * 0.22;

        ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;

        const dist = Math.hypot(mouseX - ringX, mouseY - ringY);
        if (dist > 0.1 || isVisible) {
          requestAnimationFrame(updateRingPosition);
        } else {
          isRafRunning = false;
        }
      }

      // Detección 100% NATIVA de entrada y salida sobre elementos interactivos
      document.addEventListener('pointerover', (e) => {
        const target = e.target;
        if (!target) return;

        // Verificar si es un campo de texto
        if (target.matches('input, textarea, [contenteditable="true"]')) {
          dot.classList.add('text-mode');
          ring.classList.add('text-mode');
          return;
        }

        // Verificar si es un botón o elemento interactivo
        const interactive = target.closest('a, button, .btn, [role="button"], select, .gallery-stream-item, .interactive-card, .accordion-header, .faq-header');
        if (interactive) {
          ring.classList.add('active-lock');
          dot.classList.remove('text-mode');
          ring.classList.remove('text-mode');
        }
      }, { passive: true });

      document.addEventListener('pointerout', (e) => {
        const related = e.relatedTarget;
        if (!related || !related.closest('a, button, .btn, [role="button"], select, .gallery-stream-item, .interactive-card, .accordion-header, .faq-header')) {
          ring.classList.remove('active-lock');
        }
        if (!related || !related.matches('input, textarea, [contenteditable="true"]')) {
          dot.classList.remove('text-mode');
          ring.classList.remove('text-mode');
        }
      }, { passive: true });

      // Feedback visual táctico al hacer clic
      document.addEventListener('pointerdown', () => {
        ring.classList.add('clicking');
      }, { passive: true });

      document.addEventListener('pointerup', () => {
        ring.classList.remove('clicking');
      }, { passive: true });

      // Gestión de salida de la ventana
      document.addEventListener('mouseleave', () => {
        isVisible = false;
        dot.classList.remove('visible');
        ring.classList.remove('visible');
      }, { passive: true });

      document.addEventListener('mouseenter', () => {
        isVisible = true;
        dot.classList.add('visible');
        ring.classList.add('visible');
      }, { passive: true });

      window.addEventListener('pointermove', onPointerMove, { passive: true });
    })();
    """

    script_end_pos = html.rfind('</script>')
    if script_end_pos != -1:
        html = html[:script_end_pos] + "\n" + cursor_js + "\n" + html[script_end_pos:]

    # Save to index.html
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Mirror to Happy_Tactical_Home_Mobile_Ordenado_V3-2.html
    with open(mirror_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Also update admin.html images if needed
    if os.path.exists(admin_path):
        with open(admin_path, 'r', encoding='utf-8') as f:
            adm = f.read()
        for b64_str, rel_path in extracted_map.items():
            adm = adm.replace(b64_str, rel_path)
        with open(admin_path, 'w', encoding='utf-8') as f:
            f.write(adm)

    print(f"🎉 ÉXITO: Tamaño final de index.html: {len(html)/1024:.1f} KB")
    print("✓ Se implementó el cursor único, 100% nativo y aislado para desktop.")
    print("✓ Se corrigió la matriz de transformación del canvas 3D.")
    print("✓ Se optimizaron las hitboxes de los botones sin interferencias 3D.")

if __name__ == '__main__':
    execute_all_structural_fixes()
