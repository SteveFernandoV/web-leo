#!/usr/bin/env python3
"""
check_browser_env.py — Detects available browser automation tools.
Run this FIRST before any other testing script.
"""
import subprocess
import sys
import shutil
import platform

results = {}

print("=" * 55)
print("LOCAL BROWSER TESTER — Environment Check")
print("=" * 55)

# 1. OS
os_name = platform.system()
print(f"\n[OS] {os_name} {platform.machine()}")
results['os'] = os_name

# 2. Python
print(f"[Python] {sys.version.split()[0]}")

# 3. Selenium
try:
    import selenium
    print(f"[Selenium] ✓ v{selenium.__version__}")
    results['selenium'] = True
except ImportError:
    print("[Selenium] ❌ Not installed")
    results['selenium'] = False

# 4. ChromeDriver / Chrome
chrome_paths = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium-browser',
    shutil.which('chromedriver') or '',
    shutil.which('google-chrome') or '',
]
chrome_found = any(shutil.which(p) or (p and __import__('os').path.exists(p)) for p in chrome_paths)
print(f"[Chrome/Chromium] {'✓ Found' if chrome_found else '❌ Not found'}")
results['chrome'] = chrome_found

# 5. WebDriver Manager
try:
    import webdriver_manager
    print(f"[webdriver-manager] ✓ v{webdriver_manager.__version__}")
    results['webdriver_manager'] = True
except ImportError:
    print("[webdriver-manager] ❌ Not installed")
    results['webdriver_manager'] = False

# 6. AppleScript (macOS only)
if os_name == 'Darwin':
    as_test = subprocess.run(['osascript', '-e', 'return 1'], capture_output=True)
    as_ok = as_test.returncode == 0
    print(f"[AppleScript] {'✓ Available' if as_ok else '❌ Not available'}")
    results['applescript'] = as_ok
    
    # 7. Safari
    safari_exists = __import__('os').path.exists('/Applications/Safari.app')
    print(f"[Safari] {'✓ Found' if safari_exists else '❌ Not found'}")
    results['safari'] = safari_exists
    
    # 8. screencapture
    sc = shutil.which('screencapture')
    print(f"[screencapture] {'✓ ' + sc if sc else '❌ Not found'}")
    results['screencapture'] = bool(sc)
else:
    results['applescript'] = False
    results['safari'] = False
    results['screencapture'] = False

# 9. Pillow (for image processing)
try:
    from PIL import Image
    import PIL
    print(f"[Pillow] ✓ v{PIL.__version__}")
    results['pillow'] = True
except ImportError:
    print("[Pillow] ❌ Not installed")
    results['pillow'] = False

# 10. curl (for basic HTTP checks)
curl = shutil.which('curl')
print(f"[curl] {'✓ ' + curl if curl else '❌ Not found'}")
results['curl'] = bool(curl)

# RECOMMENDATION
print("\n" + "=" * 55)
print("RECOMMENDED STRATEGY:")
if results.get('selenium') and results.get('chrome'):
    print("  → STRATEGY A: Selenium + Chrome (BEST)")
    print("    Run: python3 scripts/selenium_tester.py")
elif results.get('applescript') and results.get('screencapture'):
    print("  → STRATEGY B: AppleScript + screencapture (macOS fallback)")
    print("    Run: python3 scripts/applescript_tester.py")
else:
    print("  → STRATEGY C: Static HTML injection (always works)")
    print("    Run: python3 scripts/inject_tester.py")

# Quick install advice
if not results.get('selenium'):
    print("\n  💡 To enable Strategy A, run:")
    print("     pip3 install selenium webdriver-manager")

print("=" * 55)
print(f"\nJSON summary: {results}")
