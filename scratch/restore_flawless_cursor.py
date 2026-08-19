import re
import os

def clean_and_fix_cursor():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    for p in files:
        if not os.path.exists(p):
            continue

        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove all cursor: none rules and replace tactical cursor CSS with clean native styles
        css_pattern = re.compile(r'/\*\s*Tactical High-Precision Reticle Cursor System[\s\S]*?(?=/\*\s*Tactical Accessible Focus Indicators)')
        clean_css = """/* Clean Native Tactical Cursor Styling */
    html, body {
      cursor: default;
    }
    a, button, [role="button"], .filter-btn, .course-card, .gallery-stream-item, .tactical-video-card, .spotlight-media-wrap, .schedule-item, .interactive-card, .owner-cat-btn, .modal-close-btn {
      cursor: pointer;
    }
    input, textarea, [contenteditable="true"] {
      cursor: text;
    }
    select {
      cursor: pointer;
    }
    #tacticalCursor, #tacticalCursorDot, #tacticalCursorBadge {
      display: none !important;
    }"""

        if css_pattern.search(content):
            content = css_pattern.sub(clean_css + '\n\n    ', content)
            print(f"✓ Replaced cursor CSS in {os.path.basename(p)}")
        else:
            # Fallback if comment differs
            content = content.replace('cursor: none !important;', '/* cursor restored */')
            print(f"✓ Removed cursor: none in {os.path.basename(p)}")

        # 2. Disable / Remove buggy cursor JS engine
        js_pattern = re.compile(r'// --- 12\. Tactical Cursor Engine[\s\S]*?(?=// --- 13\.)')
        clean_js = """// --- 12. Tactical Cursor Engine (Native System Cursor Restored) ---
    // Custom lagging cursor disabled to ensure 100% native responsiveness across all browsers
    """
        if js_pattern.search(content):
            content = js_pattern.sub(clean_js + '\n    ', content)
            print(f"✓ Disabled buggy cursor JS engine in {os.path.basename(p)}")

        # 3. Ensure HTML elements #tacticalCursor are removed or hidden
        content = content.replace('<div id="tacticalCursor" aria-hidden="true">\n    <span id="tacticalCursorBadge">[TARGET]</span>\n  </div>\n  <div id="tacticalCursorDot" aria-hidden="true"></div>', '<!-- Native Cursor Active -->')
        content = content.replace('<div id="tacticalCursor" aria-hidden="true">\r\n    <span id="tacticalCursorBadge">[TARGET]</span>\r\n  </div>\r\n  <div id="tacticalCursorDot" aria-hidden="true"></div>', '<!-- Native Cursor Active -->')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Saved {os.path.basename(p)}")

if __name__ == '__main__':
    clean_and_fix_cursor()
