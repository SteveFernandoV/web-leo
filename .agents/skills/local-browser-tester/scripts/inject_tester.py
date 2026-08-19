#!/usr/bin/env python3
"""
inject_tester.py — Strategy C: No browser needed.
Injects a self-testing diagnostic panel into any HTML file and generates
a static test report that can be opened in any browser.
Works 100% without Playwright, Selenium, or AppleScript.
"""
import argparse
import os
import re
import json
from datetime import datetime

INJECTED_DIAGNOSTIC_JS = """
<style>
  #__diag_panel {
    position: fixed; bottom: 0; left: 0; right: 0;
    background: rgba(0,0,0,0.92); color: #00e5ff;
    font-family: monospace; font-size: 12px;
    padding: 12px 16px; z-index: 999999999;
    border-top: 2px solid #00e5ff;
    max-height: 220px; overflow-y: auto;
  }
  #__diag_panel .pass { color: #00ff88; }
  #__diag_panel .fail { color: #ff4444; }
  #__diag_panel .warn { color: #ffaa00; }
  #__diag_title { font-weight:bold; font-size:14px; margin-bottom:8px; color:#fff; }
</style>
<div id="__diag_panel">
  <div id="__diag_title">🔬 DIAGNOSTIC PANEL — Local Browser Tester (Strategy C)</div>
  <div id="__diag_log"></div>
</div>
<script>
(function() {
  var log = document.getElementById('__diag_log');
  var errors = [];
  
  // Capture ALL JS errors
  window.addEventListener('error', function(e) {
    errors.push(e.message + ' at ' + e.filename + ':' + e.lineno);
    addLog('❌ JS ERROR: ' + e.message, 'fail');
  });
  window.addEventListener('unhandledrejection', function(e) {
    errors.push('Promise: ' + (e.reason && e.reason.message || e.reason));
    addLog('❌ PROMISE ERROR: ' + (e.reason && e.reason.message || e.reason), 'fail');
  });
  
  function addLog(msg, cls) {
    var div = document.createElement('div');
    div.className = cls || '';
    div.textContent = (new Date().toLocaleTimeString()) + ' → ' + msg;
    if (log) log.appendChild(div);
    console.log('[DIAG]', msg);
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    addLog('✓ DOMContentLoaded fired', 'pass');
    
    var checks = [
      // Cursor checks
      { label: 'body cursor:none', fn: function() {
          var s = window.getComputedStyle(document.body).cursor;
          return { ok: s === 'none', detail: 'cursor = "' + s + '"' };
      }},
      { label: '#hudCursorDot exists', fn: function() {
          var el = document.getElementById('hudCursorDot');
          return { ok: !!el, detail: el ? 'found' : 'NULL — DOMContentLoaded timing issue?' };
      }},
      { label: '#hudCursorRing exists', fn: function() {
          var el = document.getElementById('hudCursorRing');
          return { ok: !!el, detail: el ? 'found' : 'NULL' };
      }},
      { label: '#hudCursorDot opacity', fn: function() {
          var el = document.getElementById('hudCursorDot');
          if (!el) return { ok: false, detail: 'element missing' };
          var op = window.getComputedStyle(el).opacity;
          return { ok: op === '0', detail: 'opacity=' + op + ' (should be 0 before mousemove)' };
      }},
      { label: 'matchMedia hover:hover', fn: function() {
          var ok = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
          return { ok: ok, detail: ok ? 'fine pointer device' : 'touch/coarse — cursor disabled by design' };
      }},
      // Tab system checks
      { label: '#tab-imagenes exists', fn: function() {
          var el = document.getElementById('tab-imagenes');
          return { ok: !!el, detail: el ? 'admin image tab found' : 'not present (admin.html only)' };
      }},
      // General DOM health
      { label: 'No duplicate IDs', fn: function() {
          var all = document.querySelectorAll('[id]');
          var ids = {};
          var dupes = [];
          all.forEach(function(el) {
            if (ids[el.id]) dupes.push(el.id);
            ids[el.id] = true;
          });
          return { ok: dupes.length === 0, detail: dupes.length ? 'Dupes: ' + dupes.join(', ') : 'all IDs unique' };
      }},
    ];
    
    var passed = 0;
    checks.forEach(function(c) {
      try {
        var r = c.fn();
        addLog((r.ok ? '✓ ' : '❌ ') + c.label + ': ' + r.detail, r.ok ? 'pass' : 'fail');
        if (r.ok) passed++;
      } catch(e) {
        addLog('⚠️ ' + c.label + ': ERROR — ' + e.message, 'warn');
      }
    });
    
    addLog('━━━ SUMMARY: ' + passed + '/' + checks.length + ' passed | JS Errors: ' + errors.length, 
           passed === checks.length && errors.length === 0 ? 'pass' : 'fail');
    
    // Store results globally for extraction
    window.__diagResults = { passed: passed, total: checks.length, jsErrors: errors };
  });
})();
</script>"""

def inject_diagnostic(source_html: str, output_html: str, checks: list = None):
    """Inject the diagnostic panel into an HTML file."""
    with open(source_html, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Inject before </body>
    if '</body>' in html:
        html = html.replace('</body>', INJECTED_DIAGNOSTIC_JS + '\n</body>', 1)
        print(f"  ✓ Injected diagnostic panel before </body>")
    else:
        html += INJECTED_DIAGNOSTIC_JS
        print(f"  ⚠️ No </body> found — appended at end")
    
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✓ Output: {output_html}")
    return output_html

def analyze_html_statically(source_html: str) -> dict:
    """Static analysis without a browser — parses the HTML/JS."""
    with open(source_html, 'r', encoding='utf-8') as f:
        html = f.read()
    
    results = {}
    
    # 1. cursor:none on body
    results['body_cursor_none'] = bool(re.search(r'body\s*\{[^}]*cursor\s*:\s*none', html, re.DOTALL))
    
    # 2. HUD elements
    results['dot_in_html'] = 'id="hudCursorDot"' in html
    results['ring_in_html'] = 'id="hudCursorRing"' in html
    
    # 3. DOMContentLoaded wrapping the cursor engine
    results['domcontentloaded_used'] = 'DOMContentLoaded' in html and 'initHudCursorEngine' in html
    
    # 4. Element order: script before or after elements?
    script_pos = html.find('initHudCursorEngine')
    dot_pos = html.find('id="hudCursorDot"')
    if script_pos != -1 and dot_pos != -1:
        results['dom_order_ok'] = ('DOMContentLoaded' in html[max(0,script_pos-200):script_pos+50]) or (dot_pos < script_pos)
        results['script_pos'] = script_pos
        results['dot_pos'] = dot_pos
    else:
        results['dom_order_ok'] = None
    
    # 5. pointermove registered
    results['pointermove_registered'] = "addEventListener('pointermove'" in html
    
    # 6. Conflicting animations on ring transform
    ring_css = re.search(r'\.hud-cursor-ring\s*\{([^}]*)\}', html, re.DOTALL)
    if ring_css:
        ring_block = ring_css.group(1)
        results['ring_has_animation'] = 'animation:' in ring_block or 'animation :' in ring_block
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Static HTML Injection Tester (Strategy C)')
    parser.add_argument('--source', default='index.html', help='Source HTML file to analyze')
    parser.add_argument('--output', default='test_injected.html', help='Output file with diagnostic panel')
    parser.add_argument('--report', default='static_analysis_report.json', help='Output JSON report')
    parser.add_argument('--checks', default='all', help='Comma-separated checks to run')
    args = parser.parse_args()
    
    print("=" * 55)
    print("LOCAL BROWSER TESTER — Strategy C (Static Analysis)")
    print("=" * 55)
    print(f"Source: {args.source}")
    
    # Static analysis
    print("\n[Static Analysis]")
    results = analyze_html_statically(args.source)
    
    check_labels = {
        'body_cursor_none': 'body { cursor: none }',
        'dot_in_html': '#hudCursorDot in HTML',
        'ring_in_html': '#hudCursorRing in HTML',
        'domcontentloaded_used': 'DOMContentLoaded wraps engine',
        'dom_order_ok': 'DOM order correct (elements before script or DOMContentLoaded)',
        'pointermove_registered': 'pointermove event registered',
        'ring_has_animation': 'ring has CSS animation (BAD if true — conflicts with JS transform)',
    }
    
    passed = 0
    for key, label in check_labels.items():
        val = results.get(key)
        if val is None:
            print(f"  ⚠️  {label}: could not determine")
        elif key == 'ring_has_animation':
            # This one is bad if True
            icon = '❌' if val else '✓'
            print(f"  {icon} {label}: {val}")
            if not val:
                passed += 1
        elif val:
            print(f"  ✓  {label}")
            passed += 1
        else:
            print(f"  ❌ {label}")
    
    # Inject diagnostic panel
    print(f"\n[Injecting Diagnostic Panel]")
    injected = inject_diagnostic(args.source, args.output)
    
    # Save report
    report = {
        'timestamp': datetime.now().isoformat(),
        'source': args.source,
        'static_analysis': results,
        'injected_output': args.output,
        'passed': passed,
        'total': len([k for k, v in results.items() if isinstance(v, bool)]),
    }
    with open(args.report, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{'='*55}")
    print(f"STATIC ANALYSIS: {passed} checks passed")
    print(f"Injected HTML: {args.output}")
    print(f"Report: {args.report}")
    print(f"\n💡 Open {args.output} in your browser to see the live diagnostic panel")
    
    return 0

if __name__ == '__main__':
    exit(main())
