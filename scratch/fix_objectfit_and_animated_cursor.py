import re
import os

def apply_both_fixes():
    base_dir = '/Users/stevefernandovelarde/Desktop/web leo'
    index_path = os.path.join(base_dir, 'index.html')
    mirror_path = os.path.join(base_dir, 'Happy_Tactical_Home_Mobile_Ordenado_V3-2.html')
    admin_path = os.path.join(base_dir, 'admin.html')

    # =========================================================================
    # FIX 1: IMAGE OBJECT-FIT — All images uploaded must fill their frame properly
    # =========================================================================
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix hero bg img
    html = re.sub(
        r'(<img[^>]*id="heroBgImg"[^>]*>)',
        lambda m: m.group(0) if 'object-fit' in m.group(0) else m.group(0).replace('>', ' style="width:100%; height:100%; object-fit:cover; object-position:center top;">'),
        html
    )

    # Fix about photo
    html = re.sub(
        r'(<img[^>]*id="aboutPhotoImg"[^>]*>)',
        lambda m: m.group(0) if 'object-fit' in m.group(0) else m.group(0).replace('>', ' style="width:100%; height:100%; object-fit:cover; object-position:center;">'),
        html
    )

    # Fix course images
    for cid in ['c1Img', 'c2Img', 'c3Img']:
        html = re.sub(
            r'(<img[^>]*id="' + cid + r'"[^>]*>)',
            lambda m: m.group(0) if 'object-fit' in m.group(0) else m.group(0).replace('>', ' style="width:100%; height:100%; object-fit:cover; object-position:center;">'),
            html
        )

    # Fix nav logo
    html = re.sub(
        r'(<img[^>]*id="mainNavLogo"[^>]*>)',
        lambda m: m.group(0) if 'object-fit' in m.group(0) else m.group(0).replace('>', ' style="object-fit:contain; object-position:center;">'),
        html
    )

    # =========================================================================
    # FIX 2: ANIMATED TACTICAL HUD CURSOR
    # Replace existing cursor CSS block with enhanced animated version
    # =========================================================================
    old_cursor_css_start = '/* ========================================================================\n       SISTEMA ÚNICO DE CURSOR TÁCTICO HUD DE ALTA PRECISIÓN (DESKTOP ONLY)'
    old_cursor_css_end = '    /* En Móvil y Pantallas Táctiles: Cero Cursor Personalizado */\n    @media (pointer: coarse), (hover: none) {\n      .hud-cursor-dot, .hud-cursor-ring {\n        display: none !important;\n      }\n    }'

    NEW_CURSOR_CSS = """/* ========================================================================
       CURSOR TÁCTICO HUD ANIMADO — UNA SOLA IMPLEMENTACIÓN (DESKTOP ONLY)
       ======================================================================== */
    @media (hover: hover) and (pointer: fine) {
      body { cursor: none !important; }
      a, button, [role="button"], select, .btn, .interactive-card, .gallery-stream-item { cursor: none !important; }
      input, textarea { cursor: text !important; }

      /* ── Punto Central (sigue al mouse 1:1) ── */
      .hud-cursor-dot {
        position: fixed;
        top: 0; left: 0;
        width: 8px; height: 8px;
        margin: -4px 0 0 -4px;
        border-radius: 50%;
        background: #00e5ff;
        pointer-events: none !important;
        z-index: 2147483647;
        box-shadow: 0 0 0 1.5px rgba(0,229,255,0.3), 0 0 10px #00e5ff, 0 0 4px #fff;
        opacity: 0;
        will-change: transform;
        transition: opacity 0.25s ease;
        animation: dotPulse 2s ease-in-out infinite;
      }
      /* Núcleo magenta interno */
      .hud-cursor-dot::after {
        content: '';
        position: absolute;
        top: 2.5px; left: 2.5px;
        width: 3px; height: 3px;
        background: #ff007f;
        border-radius: 50%;
        box-shadow: 0 0 4px #ff007f;
        animation: dotCorePulse 2s ease-in-out infinite;
      }
      .hud-cursor-dot.visible { opacity: 1; }
      .hud-cursor-dot.text-mode { opacity: 0.2; animation: none; }

      /* ── Aro Exterior (sigue con lerp suave) ── */
      .hud-cursor-ring {
        position: fixed;
        top: 0; left: 0;
        width: 38px; height: 38px;
        margin: -19px 0 0 -19px;
        border: 1.5px solid rgba(0, 229, 255, 0.55);
        border-radius: 50%;
        pointer-events: none !important;
        z-index: 2147483646;
        opacity: 0;
        box-sizing: border-box;
        will-change: transform, width, height;
        transition:
          width  0.28s cubic-bezier(0.16, 1, 0.3, 1),
          height 0.28s cubic-bezier(0.16, 1, 0.3, 1),
          margin 0.28s cubic-bezier(0.16, 1, 0.3, 1),
          border-color 0.25s ease,
          box-shadow 0.25s ease,
          opacity 0.25s ease;
        animation: ringRotate 4s linear infinite;
      }
      .hud-cursor-ring.visible { opacity: 1; }

      /* Segmentos del aro: gaps para efecto de dashes rotatorios */
      .hud-cursor-ring::before,
      .hud-cursor-ring::after {
        content: '';
        position: absolute;
        inset: -1.5px;
        border-radius: 50%;
        pointer-events: none;
      }
      .hud-cursor-ring::before {
        border: 1.5px dashed rgba(0, 229, 255, 0.3);
        animation: ringRotateReverse 3s linear infinite;
      }

      /* ── Corchetes de esquina ── */
      .hud-cursor-ring .ring-bracket {
        position: absolute;
        width: 7px; height: 7px;
        border-color: #00e5ff;
        border-style: solid;
        pointer-events: none;
        opacity: 0.85;
        transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .hud-cursor-ring .ring-bracket.top-left    { top: -2px;    left: -2px;    border-width: 2px 0 0 2px; }
      .hud-cursor-ring .ring-bracket.top-right   { top: -2px;    right: -2px;   border-width: 2px 2px 0 0; }
      .hud-cursor-ring .ring-bracket.bottom-left { bottom: -2px; left: -2px;    border-width: 0 0 2px 2px; }
      .hud-cursor-ring .ring-bracket.bottom-right{ bottom: -2px; right: -2px;   border-width: 0 2px 2px 0; }

      /* ── Estado Lock-On (hover sobre botones) ── */
      .hud-cursor-ring.active-lock {
        width: 54px; height: 54px;
        margin: -27px 0 0 -27px;
        border: 2px solid rgba(0, 229, 255, 1);
        box-shadow: 0 0 18px rgba(0,229,255,0.55), inset 0 0 10px rgba(0,229,255,0.18);
        animation: ringRotate 1.2s linear infinite;
      }
      .hud-cursor-ring.active-lock::before {
        border-color: rgba(255, 0, 127, 0.45);
        animation: ringRotateReverse 0.9s linear infinite;
      }
      .hud-cursor-ring.active-lock .ring-bracket {
        border-color: #ff007f;
        box-shadow: 0 0 6px #ff007f;
        width: 9px; height: 9px;
        opacity: 1;
      }

      /* ── Clic: micro-compresión ── */
      .hud-cursor-ring.clicking {
        transform: scale(0.78) !important;
        border-color: #ff007f !important;
        box-shadow: 0 0 24px rgba(255,0,127,0.75) !important;
        transition: transform 0.08s ease, border-color 0.08s ease, box-shadow 0.08s ease !important;
      }

      /* ── Modo texto: ocultar aro ── */
      .hud-cursor-ring.text-mode { opacity: 0 !important; animation: none !important; }
    }

    /* Móvil / Touch: invisible y desactivado */
    @media (pointer: coarse), (hover: none) {
      .hud-cursor-dot, .hud-cursor-ring { display: none !important; }
      body { cursor: auto !important; }
    }

    /* Keyframes de animación del cursor */
    @keyframes ringRotate {
      from { transform: translate3d(var(--tx,0),var(--ty,0),0) rotate(0deg); }
      to   { transform: translate3d(var(--tx,0),var(--ty,0),0) rotate(360deg); }
    }
    @keyframes ringRotateReverse {
      from { transform: rotate(0deg); }
      to   { transform: rotate(-360deg); }
    }
    @keyframes dotPulse {
      0%, 100% { box-shadow: 0 0 0 1.5px rgba(0,229,255,0.3), 0 0 10px #00e5ff, 0 0 4px #fff; }
      50%       { box-shadow: 0 0 0 3px rgba(0,229,255,0.15), 0 0 18px #00e5ff, 0 0 8px #fff; }
    }
    @keyframes dotCorePulse {
      0%, 100% { transform: scale(1);   opacity: 1; }
      50%       { transform: scale(1.5); opacity: 0.7; }
    }"""

    # Find and replace the existing cursor CSS block
    start_marker = '/* ========================================================================\n       SISTEMA ÚNICO DE CURSOR TÁCTICO HUD DE ALTA PRECISIÓN (DESKTOP ONLY)'
    end_marker = '    /* En Móvil y Pantallas Táctiles: Cero Cursor Personalizado */\n    @media (pointer: coarse), (hover: none) {\n      .hud-cursor-dot, .hud-cursor-ring {\n        display: none !important;\n      }\n    }'

    start_pos = html.find(start_marker)
    end_pos = html.find(end_marker)

    if start_pos != -1 and end_pos != -1:
        end_pos_full = end_pos + len(end_marker)
        html = html[:start_pos] + NEW_CURSOR_CSS + html[end_pos_full:]
        print("✓ Replaced cursor CSS with animated version.")
    else:
        print(f"  start found: {start_pos != -1}, end found: {end_pos != -1}")
        print("  Appending cursor CSS before </style> instead.")
        html = html.replace('</style>', '\n' + NEW_CURSOR_CSS + '\n</style>', 1)

    # FIX JS: remove CSS rotation conflict with transform in RAF loop
    # The ring rotation is via CSS animation, the JS only positions with translate3d
    # Update JS to use translateX/Y only (no rotation competition)
    OLD_RAF = "ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;"
    NEW_RAF = """// Position via CSS custom properties to not conflict with rotation animation
        ring.style.setProperty('--tx', ringX + 'px');
        ring.style.setProperty('--ty', ringY + 'px');
        ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0)`;"""

    html = html.replace(OLD_RAF, NEW_RAF)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(mirror_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Applied animated cursor + object-fit fixes to index.html and mirror.")

    # =========================================================================
    # FIX 3: Admin preview images should also use object-fit: cover
    # =========================================================================
    with open(admin_path, 'r', encoding='utf-8') as f:
        adm = f.read()

    # Fix all preview images in admin tab-imagenes to use object-fit:cover
    adm = re.sub(
        r'(id="preview_(?:logo|hero|about|c1|c2|c3)"[^>]*style=")([^"]*)',
        lambda m: m.group(1) + m.group(2).replace('object-fit:contain', 'object-fit:cover').replace('object-fit:cover', 'object-fit:cover') + ('' if 'object-fit' in m.group(2) else 'object-fit:cover; object-position:center; '),
        adm
    )

    with open(admin_path, 'w', encoding='utf-8') as f:
        f.write(adm)
    print("✓ Updated admin.html preview images with object-fit:cover.")

if __name__ == '__main__':
    apply_both_fixes()
