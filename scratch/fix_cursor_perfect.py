import re
import os

def fix_cursor():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    new_cursor_css = """/* Tactical High-Precision Reticle Cursor System */
    #tacticalCursor, #tacticalCursorDot, #tacticalCursorBadge {
      pointer-events: none !important;
      user-select: none !important;
    }
    #tacticalCursor {
      position: fixed;
      top: 0;
      left: 0;
      width: 38px;
      height: 38px;
      border: 1.5px solid var(--neon-cyan);
      border-radius: 50%;
      z-index: 999999;
      opacity: 0;
      will-change: transform, opacity;
      transform: translate3d(-100px, -100px, 0) translate(-50%, -50%);
      transition: opacity 0.15s ease, border-color 0.18s ease, background-color 0.18s ease, box-shadow 0.18s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 0 1px rgba(0, 229, 255, 0.25), 0 0 15px rgba(0, 229, 255, 0.2);
    }
    #tacticalCursor::before {
      content: "";
      position: absolute;
      width: 8px;
      height: 1.5px;
      left: -4px;
      top: 50%;
      transform: translateY(-50%);
      background: var(--neon-cyan);
      box-shadow: 34px 0 0 var(--neon-cyan);
      pointer-events: none;
      transition: background-color 0.18s ease, box-shadow 0.18s ease;
    }
    #tacticalCursor::after {
      content: "";
      position: absolute;
      width: 1.5px;
      height: 8px;
      top: -4px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--neon-cyan);
      box-shadow: 0 34px 0 var(--neon-cyan);
      pointer-events: none;
      transition: background-color 0.18s ease, box-shadow 0.18s ease;
    }
    #tacticalCursorDot {
      position: fixed;
      top: 0;
      left: 0;
      width: 5px;
      height: 5px;
      background-color: var(--neon-pink);
      border-radius: 50%;
      z-index: 1000000;
      opacity: 0;
      will-change: transform, opacity;
      transform: translate3d(-100px, -100px, 0) translate(-50%, -50%);
      box-shadow: 0 0 8px var(--neon-pink);
      transition: opacity 0.15s ease, background-color 0.18s ease, box-shadow 0.18s ease;
    }
    #tacticalCursorBadge {
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%) translateY(8px);
      font-family: var(--font-display);
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 0.14em;
      color: var(--neon-cyan);
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.15s ease, transform 0.15s ease, color 0.15s ease, border-color 0.15s ease;
      background: rgba(3, 6, 12, 0.94);
      padding: 2px 7px;
      border-radius: 3px;
      border: 1px solid rgba(0, 229, 255, 0.45);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.7);
    }
    body.cursor-hover #tacticalCursor {
      border-color: var(--neon-pink);
      background-color: rgba(255, 0, 127, 0.08);
      box-shadow: 0 0 0 1px rgba(255, 0, 127, 0.4), 0 0 20px rgba(255, 0, 127, 0.3);
    }
    body.cursor-hover #tacticalCursor::before {
      background: var(--neon-pink);
      box-shadow: 34px 0 0 var(--neon-pink);
    }
    body.cursor-hover #tacticalCursor::after {
      background: var(--neon-pink);
      box-shadow: 0 34px 0 var(--neon-pink);
    }
    body.cursor-hover #tacticalCursorDot {
      background-color: var(--neon-cyan);
      box-shadow: 0 0 10px var(--neon-cyan);
    }
    body.cursor-hover #tacticalCursorBadge {
      opacity: 1;
      color: var(--neon-pink);
      border-color: rgba(255, 0, 127, 0.6);
      transform: translateX(-50%) translateY(10px);
    }
    #tacticalCursor.cursor-active {
      border-color: #ffffff;
      background-color: rgba(0, 229, 255, 0.25);
      box-shadow: 0 0 0 1px #ffffff, 0 0 25px rgba(0, 229, 255, 0.6);
    }

    @media (max-width: 900px), (hover: none) {
      #tacticalCursor, #tacticalCursorDot, #tacticalCursorBadge {
        display: none !important;
      }
    }"""

    new_cursor_js = """    // --- 12. Tactical Cursor Engine (Rock-Solid Locked Hardware Tracking) ---
    (() => {
      const cursor = document.getElementById('tacticalCursor');
      const cursorDot = document.getElementById('tacticalCursorDot');
      const badge = document.getElementById('tacticalCursorBadge');
      if (!cursor || !cursorDot) return;

      let clientX = -100;
      let clientY = -100;
      let isVisible = false;
      let isHovered = false;
      let isMouseDown = false;

      function updateCursorFrame() {
        if (isVisible) {
          const targetScale = isMouseDown ? 0.85 : (isHovered ? 1.3 : 1.0);
          cursor.style.transform = `translate3d(${clientX}px, ${clientY}px, 0) translate(-50%, -50%) scale(${targetScale})`;
          cursorDot.style.transform = `translate3d(${clientX}px, ${clientY}px, 0) translate(-50%, -50%)`;
        }
        requestAnimationFrame(updateCursorFrame);
      }
      requestAnimationFrame(updateCursorFrame);

      function onMove(e) {
        if (e.pointerType === 'touch') {
          cursor.style.opacity = '0';
          cursorDot.style.opacity = '0';
          isVisible = false;
          return;
        }

        clientX = e.clientX;
        clientY = e.clientY;

        if (!isVisible) {
          isVisible = true;
          cursor.style.opacity = '1';
          cursorDot.style.opacity = '1';
        }
      }

      window.addEventListener('pointermove', onMove, { passive: true });
      window.addEventListener('mousemove', onMove, { passive: true });

      window.addEventListener('pointerdown', (e) => {
        if (e.pointerType === 'touch') return;
        isMouseDown = true;
        cursor.classList.add('cursor-active');
      }, { passive: true });

      window.addEventListener('pointerup', () => {
        isMouseDown = false;
        cursor.classList.remove('cursor-active');
      }, { passive: true });

      // Clean delegation with closest() matching
      const interactiveSelector = 'a, button, input, select, textarea, [data-ht-editable], .course-card, .pillar-card, .metric-box, .schedule-item, .contact-channel-card, .filter-btn, .owner-cat-btn, .modal-close-btn, .interactive-card, .gallery-stream-item, .tactical-video-card, .spotlight-media-wrap, [role="button"], [tabindex="0"]';

      document.addEventListener('mouseover', (e) => {
        const target = e.target.closest(interactiveSelector);
        if (target) {
          if (!isHovered) {
            isHovered = true;
            document.body.classList.add('cursor-hover');
          }

          if (badge) {
            let txt = '[INTERACTUAR]';
            if (target.classList.contains('modal-close-btn') || target.getAttribute('aria-label')?.toLowerCase().includes('cerrar')) {
              txt = '[CERRAR]';
            } else if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
              txt = '[ESCRIBIR]';
            } else if (target.tagName === 'SELECT') {
              txt = '[OPCIONES]';
            } else if (target.classList.contains('gallery-stream-item')) {
              txt = '[FOTO HD]';
            } else if (target.classList.contains('tactical-video-card') || target.classList.contains('spotlight-media-wrap')) {
              txt = '[VER VIDEO]';
            } else if (target.classList.contains('course-card') || target.hasAttribute('data-tilt')) {
              txt = '[EXPLORAR]';
            } else if (target.href && target.href.includes('wa.me')) {
              txt = '[WHATSAPP]';
            } else if (target.classList.contains('owner-access-link') || target.classList.contains('owner-cat-btn')) {
              txt = '[PANEL DUEÑO]';
            } else if (target.classList.contains('filter-btn')) {
              txt = '[FILTRAR]';
            } else if (target.tagName === 'A') {
              txt = '[ACCEDER]';
            } else if (target.tagName === 'BUTTON') {
              txt = '[SELECCIONAR]';
            }
            badge.textContent = txt;
          }
        }
      }, { passive: true });

      document.addEventListener('mouseout', (e) => {
        const currentInteractive = e.target.closest(interactiveSelector);
        const nextInteractive = e.relatedTarget ? e.relatedTarget.closest(interactiveSelector) : null;

        if (currentInteractive && !nextInteractive) {
          isHovered = false;
          document.body.classList.remove('cursor-hover');
          if (badge) badge.textContent = '[TARGET]';
        }
      }, { passive: true });

      window.addEventListener('blur', () => {
        cursor.style.opacity = '0';
        cursorDot.style.opacity = '0';
        isVisible = false;
      });
      window.addEventListener('focus', () => {
        cursor.style.opacity = '1';
        cursorDot.style.opacity = '1';
        isVisible = true;
      });
    })();

    """

    for p in files:
        if not os.path.exists(p):
            continue

        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        css_pattern = re.compile(r'/\*\s*Tactical High-Precision[\s\S]*?(?=/\*\s*Tactical Accessible Focus Indicators)')
        if css_pattern.search(content):
            content = css_pattern.sub(new_cursor_css + '\n\n    ', content)

        js_pattern = re.compile(r'// --- 12\. Tactical Cursor Engine[\s\S]*?(?=// --- 13\.)')
        if js_pattern.search(content):
            content = js_pattern.sub(new_cursor_js, content)

        # Update Footer links to include Galería and Videos
        old_footer_links = """<ul class="footer-links">
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#nosotros">Nosotros</a></li>
            <li><a href="#cursos">Cursos &amp; Talleres</a></li>
            <li><a href="#calendario">Calendario 2026</a></li>
            <li><a href="#cotizador">Cotizador</a></li>
          </ul>"""
        
        new_footer_links = """<ul class="footer-links">
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#nosotros">Nosotros</a></li>
            <li><a href="#cursos">Cursos &amp; Talleres</a></li>
            <li><a href="#galeria">Galería Operativa</a></li>
            <li><a href="#videos">Videoteca Táctica</a></li>
            <li><a href="#calendario">Calendario 2026</a></li>
            <li><a href="#cotizador">Cotizador Rápido</a></li>
          </ul>"""
        
        if old_footer_links in content:
            content = content.replace(old_footer_links, new_footer_links, 1)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Saved updated {os.path.basename(p)}")

if __name__ == '__main__':
    fix_cursor()
