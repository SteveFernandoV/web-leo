import os

def fix_tilt_and_sync():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    for p in files:
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'setup3DCardTilt' in content:
            content = content.replace(
                "if (typeof setup3DCardTilt === 'function') {\n        setTimeout(setup3DCardTilt, 50);\n      }",
                "if (typeof init3DTilt === 'function') {\n        setTimeout(init3DTilt, 50);\n      }"
            )
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated tilt in {os.path.basename(p)}")
        else:
            print(f"No setup3DCardTilt found in {os.path.basename(p)}")

if __name__ == '__main__':
    fix_tilt_and_sync()
