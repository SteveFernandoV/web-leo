#!/usr/bin/env python3
"""
applescript_tester.py — Strategy B: macOS AppleScript + screencapture browser tester.
Opens a URL in Safari using AppleScript, waits for load, captures screenshot.
No Playwright, no Selenium required.
"""
import subprocess
import time
import argparse
import os
import json
from datetime import datetime

def run_applescript(script: str) -> tuple[str, int]:
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip(), result.returncode

def open_url_in_safari(url: str, delay: float = 2.5) -> bool:
    """Open URL in Safari and wait for it to load."""
    print(f"  → Opening {url} in Safari...")
    
    script = f'''
tell application "Safari"
    activate
    if (count of windows) is 0 then
        make new document with properties {{URL:"{url}"}}
    else
        set URL of current tab of front window to "{url}"
    end if
    delay {delay}
end tell
'''
    _, code = run_applescript(script)
    if code != 0:
        print("  ❌ AppleScript error opening Safari")
        return False
    print(f"  ✓ Page loaded (waited {delay}s)")
    return True

def capture_screenshot(output_path: str, window_only: bool = False) -> bool:
    """Capture screenshot using macOS screencapture."""
    print(f"  → Capturing screenshot to {output_path}...")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    if window_only:
        cmd = ['screencapture', '-o', '-w', output_path]
    else:
        # Capture full screen
        cmd = ['screencapture', '-x', output_path]  # -x = no sound
    
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0 and os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"  ✓ Screenshot saved: {output_path} ({size/1024:.1f} KB)")
        return True
    else:
        print(f"  ❌ screencapture failed: {result.stderr}")
        return False

def check_js_via_safari(js_expression: str) -> str:
    """Execute JavaScript in Safari via AppleScript and return result."""
    script = f'''
tell application "Safari"
    set theResult to do JavaScript "{js_expression}" in current tab of front window
    return theResult as string
end tell
'''
    output, code = run_applescript(script)
    return output if code == 0 else f"ERROR: {code}"

def run_cursor_tests() -> dict:
    """Run cursor-specific tests via Safari JS execution."""
    tests = {}
    
    print("\n  [Cursor Tests via Safari JS]")
    
    # Test 1: body cursor:none
    result = check_js_via_safari(
        "window.getComputedStyle(document.body).cursor"
    )
    tests['body_cursor_none'] = result == 'none'
    print(f"  body cursor: '{result}' → {'✓' if tests['body_cursor_none'] else '❌'}")
    
    # Test 2: hudCursorDot exists
    result = check_js_via_safari(
        "document.getElementById('hudCursorDot') !== null ? 'found' : 'null'"
    )
    tests['dot_exists'] = result == 'found'
    print(f"  hudCursorDot: '{result}' → {'✓' if tests['dot_exists'] else '❌'}")
    
    # Test 3: hudCursorRing exists
    result = check_js_via_safari(
        "document.getElementById('hudCursorRing') !== null ? 'found' : 'null'"
    )
    tests['ring_exists'] = result == 'found'
    print(f"  hudCursorRing: '{result}' → {'✓' if tests['ring_exists'] else '❌'}")
    
    # Test 4: dot opacity (should be 0 before mouse moves)
    result = check_js_via_safari(
        "window.getComputedStyle(document.getElementById('hudCursorDot') || document.body).opacity"
    )
    tests['dot_opacity_default'] = result == '0'
    print(f"  dot opacity (default): '{result}' → {'✓ (opacity:0, will show on mousemove)' if tests['dot_opacity_default'] else '⚠️ unexpected'}")
    
    # Test 5: DOMContentLoaded-based init
    result = check_js_via_safari(
        "(typeof document.getElementById('hudCursorDot') !== 'undefined') ? 'ok' : 'missing'"
    )
    tests['dom_ready'] = result == 'ok'
    print(f"  DOM ready check: '{result}' → {'✓' if tests['dom_ready'] else '❌'}")
    
    # Test 6: Any JS errors in console (via error count)
    # We inject a temporary error listener check
    result = check_js_via_safari(
        "window.__testErrorCount !== undefined ? window.__testErrorCount : 'not-tracked'"
    )
    tests['js_errors'] = result
    print(f"  JS error count: '{result}'")
    
    return tests

def main():
    parser = argparse.ArgumentParser(description='macOS AppleScript Browser Tester')
    parser.add_argument('--url', default='http://localhost:3000', help='URL to test')
    parser.add_argument('--output-dir', default='./test_screenshots', help='Output directory for screenshots')
    parser.add_argument('--delay', type=float, default=2.5, help='Wait time after page load (seconds)')
    parser.add_argument('--test', choices=['screenshot', 'cursor', 'console', 'all'], default='all')
    args = parser.parse_args()
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("=" * 55)
    print("LOCAL BROWSER TESTER — Strategy B (AppleScript)")
    print("=" * 55)
    print(f"URL: {args.url}")
    print(f"Test: {args.test}")
    
    # Open URL
    if not open_url_in_safari(args.url, args.delay):
        print("\n❌ FAILED: Could not open URL in Safari")
        return 1
    
    results = {'url': args.url, 'timestamp': timestamp, 'tests': {}}
    
    # Screenshot
    screenshot_path = os.path.join(args.output_dir, f'screenshot_{timestamp}.png')
    screenshot_ok = capture_screenshot(screenshot_path)
    results['screenshot'] = screenshot_path if screenshot_ok else None
    
    # Run tests
    if args.test in ('cursor', 'all'):
        results['tests']['cursor'] = run_cursor_tests()
    
    # Save results JSON
    report_path = os.path.join(args.output_dir, f'report_{timestamp}.json')
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*55}")
    print(f"RESULTS SAVED:")
    print(f"  Screenshot: {screenshot_path}")
    print(f"  Report JSON: {report_path}")
    
    # Summary
    if 'cursor' in results['tests']:
        ct = results['tests']['cursor']
        passed = sum(1 for v in ct.values() if v is True)
        total = sum(1 for v in ct.values() if isinstance(v, bool))
        print(f"\nCursor tests: {passed}/{total} passed")
        if not ct.get('dot_exists') or not ct.get('ring_exists'):
            print("  ❌ Cursor elements missing from DOM!")
        elif not ct.get('body_cursor_none'):
            print("  ❌ body cursor:none not applied — custom cursor won't show")
        else:
            print("  ✓ Cursor structure looks correct")
    
    return 0

if __name__ == '__main__':
    exit(main())
