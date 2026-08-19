---
name: local-browser-tester
description: >
  Automated browser testing for local web apps WITHOUT Playwright/Puppeteer drivers.
  Use this skill whenever you need to test a local website running on localhost (any port),
  capture screenshots, inspect the DOM, check JavaScript console errors, verify CSS behavior,
  test cursor/animations, check hover states, or validate UI interactions — all via
  a lightweight Python HTTP + screenshot approach that works even when Playwright CDN fails.
  ACTIVATE THIS SKILL when: the browser_subagent fails with Playwright 404 errors, when you
  need to verify UI changes visually, when testing local dev servers, when checking animations
  or cursor behavior, when capturing before/after screenshots of code changes, or any time
  you need to inspect a running web app programmatically. Do NOT use for external URLs
  requiring auth — this skill targets local HTTP servers only.
---

# Local Browser Tester

A self-contained automated testing skill for local web applications. Works around Playwright
CDN failures by using system browsers (Safari/Chrome/Firefox) via AppleScript and Python
scripting to capture screenshots, read DOM state, and check console errors.

## When to Use This Skill

- Playwright `browser_subagent` fails with `404 Not Found` driver errors
- You need visual proof that a UI change worked
- Testing custom cursors, animations, hover effects, or CSS transitions
- Capturing multi-resolution screenshots (desktop + mobile)
- Checking JavaScript console errors without opening a browser manually
- Verifying local dev server pages render correctly

## Architecture

This skill uses **two strategies in priority order**:

1. **Strategy A — Python `selenium` with system Chrome/Safari** (if available)
2. **Strategy B — AppleScript + system Safari/Chrome** (fallback, macOS only)
3. **Strategy C — Static HTML injection tester** (always works, no browser needed)

Always attempt Strategy A first, fall back to B, then C.

---

## STEP 1: Check Available Browser Tools

Run this diagnostic first — never skip it:

```bash
python3 scripts/check_browser_env.py
```

Read the output and proceed with the recommended strategy. The script will tell you
exactly which strategy to use.

---

## STEP 2A — Strategy A: Selenium (Preferred)

If `check_browser_env.py` reports Selenium + ChromeDriver available:

```bash
python3 scripts/selenium_tester.py \
  --url "http://localhost:3000" \
  --test "cursor_visible" \
  --screenshot "test_result.png" \
  --width 1440 \
  --height 900
```

Available `--test` values: `cursor_visible`, `console_errors`, `element_exists`, `hover_state`, `screenshot_only`

---

## STEP 2B — Strategy B: AppleScript (macOS Fallback)

If Selenium isn't available but you're on macOS:

```bash
python3 scripts/applescript_tester.py \
  --url "http://localhost:3000" \
  --output-dir "./test_screenshots" \
  --delay 2
```

This opens the URL in Safari using AppleScript, waits for load, then captures a screenshot
via the `screencapture` command.

---

## STEP 2C — Strategy C: Static Injected Tester (Always Works)

When no browser automation is available, inject a self-testing HTML page:

```bash
python3 scripts/inject_tester.py \
  --source "index.html" \
  --output "test_injected.html" \
  --checks "cursor,dom_elements,script_errors"
```

This creates a version of the page with diagnostic JavaScript embedded that:
- Logs all JS errors to a visible on-screen panel
- Reports whether target elements exist in the DOM
- Shows CSS computed styles for key elements
- Can be opened manually or served locally

Then generate a static report:
```bash
python3 scripts/generate_report.py --input "test_injected.html" --output "test_report.html"
```

---

## STEP 3: Capture Multi-Resolution Screenshots

For responsive testing across devices:

```bash
python3 scripts/multi_resolution_capture.py \
  --url "http://localhost:3000" \
  --resolutions "1920x1080,390x844,360x800,412x915" \
  --output-dir "./test_results"
```

This uses whichever strategy is available (A → B → C).

---

## STEP 4: Read and Report Results

After running tests:

1. Read any generated screenshots and embed them in your response
2. Check `test_results/console_errors.json` for JS errors
3. Check `test_results/element_check.json` for DOM presence
4. Summarize findings clearly to the user

Always report:
- ✅ What passed
- ❌ What failed (with exact error message)
- 📸 Screenshots embedded inline
- 🔧 Recommended fix if something failed

---

## Common Test Scenarios

### Test: Custom Cursor Visibility
```bash
python3 scripts/selenium_tester.py --url "http://localhost:3000" --test "cursor_visible"
```
Checks:
- `body { cursor: none }` is applied
- `#hudCursorDot` and `#hudCursorRing` elements exist in DOM
- Elements have `pointer-events: none`
- JS engine is registered (checks for `pointermove` listener)

### Test: JavaScript Console Errors
```bash
python3 scripts/selenium_tester.py --url "http://localhost:3000" --test "console_errors"
```
Captures all `console.error()` and unhandled promise rejections.

### Test: Element Exists in DOM
```bash
python3 scripts/selenium_tester.py --url "http://localhost:3000" --test "element_exists" --selector "#tab-imagenes"
```

### Test: Page Screenshot Only
```bash
python3 scripts/applescript_tester.py --url "http://localhost:3000" --output-dir "./screenshots"
```

---

## Notes for the Agent

- **Always run `check_browser_env.py` first** — never assume which strategy is available
- **Screenshot paths**: save to the artifacts directory for embedding in responses
- **Port**: check if the server is running with `curl -s -o /dev/null -w "%{http_code}" http://localhost:PORT` before testing
- **After any code fix**: run tests again to confirm the fix works
- **Mobile simulation**: Strategy A (Selenium) supports viewport resize for mobile testing; Strategy B uses `screencapture` which is desktop only
- **Headless**: Prefer headless mode when available (faster, no window flashing)
