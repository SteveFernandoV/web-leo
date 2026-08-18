import re
import os

def fix_cursor():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    new_cursor_css = """/* Tactical High-Precision Zero-Lag Reticle Cursor System */
    #tacticalCursor {
      position: fixed;
      top: 0;
      left: 0;
      width: 36px;
      height: 36px;
      border: 1.5px solid var(--neon-cyan);
      border-radius: 50%;
      pointer-events: none;
      z-index: 100005;
      opacity: 0;
      will-change: transform, opacity;
      transform: translate3d(-100px, -100px, 0) translate(-50%, -50%);
      transition: opacity 0.15s ease, border-color 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease, width 0.2s ease, height 0.2s ease;
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
      box-shadow: 32px 0 0 var(--neon-cyan);
      pointer-events: none;
      transition: background-color 0.2s ease, box-shadow 0.2s ease;
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
      box-shadow: 0 32px 0 var(--neon-cyan);
      pointer-events: none;
      transition: background-color 0.2s ease, box-shadow 0.2s ease;
    }
    #tacticalCursorDot {
      position: fixed;
      top: 0;
      left: 0;
      width: 5px;
      height: 5px;
      background-color: var(--neon-pink);
      border-radius: 50%;
      pointer-events: none;
      z-index: 100006;
      opacity: 0;
      will-change: transform, opacity;
      transform: translate3d(-100px, -100px, 0) translate(-50%, -50%);
      box-shadow: 0 0 8px var(--neon-pink);
      transition: opacity 0.15s ease, background-color 0.2s ease, box-shadow 0.2s ease;
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
      width: 46px;
      height: 46px;
    }
    body.cursor-hover #tacticalCursor::before {
      background: var(--neon-pink);
      box-shadow: 42px 0 0 var(--neon-pink);
    }
    body.cursor-hover #tacticalCursor::after {
      background: var(--neon-pink);
      box-shadow: 0 42px 0 var(--neon-pink);
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

    new_cursor_js = """    // --- 12. Tactical Cursor Engine (Ultra-Responsive Zero-Lag Direct Hardware Lock) ---
    (() => {
      const cursor = document.getElementById('tacticalCursor');
      const cursorDot = document.getElementById('tacticalCursorDot');
      const badge = document.getElementById('tacticalCursorBadge');
      if (!cursor || !cursorDot) return;

      let mouseX = -100;
      let mouseY = -100;
      let isVisible = false;
      let isHovered = false;
      let isMouseDown = false;

      function renderTransform() {
        const scale = isMouseDown ? 0.85 : (isHovered ? 1.25 : 1.0);
        cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%) scale(${scale})`;
        cursorDot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
      }

      function handleMove(e) {
        if (e.pointerType === 'touch') {
          cursor.style.opacity = '0';
          cursorDot.style.opacity = '0';
          return;
        }

        mouseX = e.clientX;
        mouseY = e.clientY;

        if (!isVisible) {
          isVisible = true;
          cursor.style.opacity = '1';
          cursorDot.style.opacity = '1';
        }

        // Instantaneous 0-lag position sync directly to hardware coordinates
        renderTransform();
      }

      window.addEventListener('pointermove', handleMove, { passive: true });
      window.addEventListener('mousemove', handleMove, { passive: true });

      document.addEventListener('pointerleave', () => {
        isVisible = false;
        cursor.style.opacity = '0';
        cursorDot.style.opacity = '0';
      });

      document.addEventListener('pointerenter', (e) => {
        if (e.pointerType !== 'touch') {
          isVisible = true;
          cursor.style.opacity = '1';
          cursorDot.style.opacity = '1';
        }
      });

      document.addEventListener('pointerdown', (e) => {
        if (e.pointerType === 'touch') return;
        isMouseDown = true;
        cursor.classList.add('cursor-active');
        renderTransform();
      }, { passive: true });

      document.addEventListener('pointerup', () => {
        isMouseDown = false;
        cursor.classList.remove('cursor-active');
        renderTransform();
      }, { passive: true });

      // Interactive Elements Delegation
      const interactiveSelector = 'a, button, input, select, textarea, [data-ht-editable], .course-card, .pillar-card, .metric-box, .schedule-item, .contact-channel-card, .filter-btn, .owner-cat-btn, .modal-close-btn, .interactive-card, .gallery-stream-item, .tactical-video-card, .spotlight-media-wrap';

      document.addEventListener('pointerover', (e) => {
        if (e.pointerType === 'touch') return;
        const target = e.target.closest(interactiveSelector);
        if (target) {
          document.body.classList.add('cursor-hover');
          isHovered = true;

          if (badge) {
            if (target.classList.contains('modal-close-btn') || target.getAttribute('aria-label')?.toLowerCase().includes('cerrar')) {
              badge.textContent = '[CERRAR]';
            } else if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
              badge.textContent = '[ESCRIBIR]';
            } else if (target.tagName === 'SELECT') {
              badge.textContent = '[OPCIONES]';
            } else if (target.classList.contains('gallery-stream-item')) {
              badge.textContent = '[FOTO HD]';
            } else if (target.classList.contains('tactical-video-card') || target.classList.contains('spotlight-media-wrap')) {
              badge.textContent = '[VER VIDEO]';
            } else if (target.classList.contains('course-card') || target.hasAttribute('data-tilt')) {
              badge.textContent = '[EXPLORAR]';
            } else if (target.href && target.href.includes('wa.me')) {
              badge.textContent = '[WHATSAPP]';
            } else if (target.classList.contains('owner-access-link') || target.classList.contains('owner-cat-btn')) {
              badge.textContent = '[PANEL DUEÑO]';
            } else if (target.classList.contains('filter-btn')) {
              badge.textContent = '[FILTRAR]';
            } else if (target.tagName === 'A') {
              badge.textContent = '[ACCEDER]';
            } else if (target.tagName === 'BUTTON') {
              badge.textContent = '[EJECUTAR]';
            } else {
              badge.textContent = '[SELECCIONAR]';
            }
          }
          if (isVisible) renderTransform();
        }
      }, { passive: true });

      document.addEventListener('pointerout', (e) => {
        if (e.pointerType === 'touch') return;
        const target = e.target.closest(interactiveSelector);
        if (target) {
          document.body.classList.remove('cursor-hover');
          isHovered = false;
          if (badge) badge.textContent = '[TARGET]';
          if (isVisible) renderTransform();
        }
      }, { passive: true });
    })();

    """

    for p in files:
        if not os.path.exists(p):
            print(f"File not found: {p}")
            continue

        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Replace Cursor CSS
        css_pattern = re.compile(r'/\*\s*Tactical High-Precision Reticle Cursor System[\s\S]*?(?=/\*\s*Tactical Accessible Focus Indicators)')
        if css_pattern.search(content):
            content = css_pattern.sub(new_cursor_css + '\n\n    ', content)
            print(f"✓ Updated cursor CSS in {os.path.basename(p)}")
        else:
            print(f"⚠ Could not match cursor CSS in {os.path.basename(p)}")

        # 2. Replace Cursor JS
        js_pattern = re.compile(r'// --- 12\. Tactical Cursor Engine[\s\S]*?(?=// --- 13\.)')
        if js_pattern.search(content):
            content = js_pattern.sub(new_cursor_js, content)
            print(f"✓ Updated cursor JS in {os.path.basename(p)}")
        else:
            print(f"⚠ Could not match cursor JS in {os.path.basename(p)}")

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Saved {os.path.basename(p)}")

if __name__ == '__main__':
    fix_cursor()
