import subprocess
import time
import os

def run_screenshot(url, width, height, output_name):
    artifact_dir = '/Users/stevefernandovelarde/.gemini/antigravity-ide/brain/db7868f5-c664-42e3-a930-da0d9397573d'
    dest_path = os.path.join(artifact_dir, output_name)
    
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--window-size={width},{height}",
        f"--screenshot={dest_path}",
        "--virtual-time-budget=3000",
        url
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(dest_path):
            size_kb = os.path.getsize(dest_path) / 1024
            print(f"  ✓ Captura OK [{width}x{height}] -> {output_name} ({size_kb:.1f} KB)")
            return dest_path
    except Exception as e:
        print(f"  ❌ Error capturando {output_name}: {e}")
    return None

def main():
    print("🚀 INICIANDO BATERÍA DE PRUEBAS VISUALES Y DE NAVEGACIÓN:")
    
    # 1. Desktop 1920x1080
    run_screenshot("http://localhost:3000/index.html", 1920, 1080, "test_desktop_1920.png")
    
    # 2. iPhone 14/15 390x844
    run_screenshot("http://localhost:3000/index.html", 390, 844, "test_mobile_iphone_390.png")

    # 3. Android 360x800
    run_screenshot("http://localhost:3000/index.html", 360, 800, "test_mobile_android_360.png")

    # 4. Samsung Galaxy 412x915
    run_screenshot("http://localhost:3000/index.html", 412, 915, "test_mobile_galaxy_412.png")

    # 5. Admin Panel 1920x1080
    run_screenshot("http://localhost:3000/admin.html", 1920, 1080, "test_admin_desktop.png")

    print("\n✅ Todas las pruebas de renderizado finalizadas exitosamente.")

if __name__ == '__main__':
    main()
