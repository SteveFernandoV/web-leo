import re
import os

def link_admin():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    for p in files:
        if not os.path.exists(p):
            continue

        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Footer link
        old_footer_owner = """<li style="margin-top: 8px;">
              <button type="button" class="owner-access-link" onclick="openOwnerPinModal()">
                [ 🔐 ACCESO PROPIETARIO ]
              </button>
            </li>"""

        new_footer_owner = """<li style="margin-top: 8px;">
              <a href="admin.html" class="owner-access-link" style="display: inline-flex; align-items: center; gap: 6px; text-decoration: none;">
                [ 🔐 CENTRO DE MANDO DEL PROPIETARIO ] ↗
              </a>
            </li>"""

        if old_footer_owner in content:
            content = content.replace(old_footer_owner, new_footer_owner, 1)

        # 2. Update ownerPinModal to add direct link to admin.html
        old_modal_end = """        <button type="submit" class="btn btn-primary btn-sm" style="flex: 1;">INGRESAR 🔓</button>
      </div>
    </form>"""

        new_modal_end = """        <button type="submit" class="btn btn-primary btn-sm" style="flex: 1;">INGRESAR 🔓</button>
      </div>
      <div style="margin-top: 14px; text-align: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px;">
        <a href="admin.html" class="btn btn-secondary btn-sm" style="width: 100%; display: inline-flex; align-items: center; justify-content: center; gap: 6px;">
          <span>ABRIR EDITOR EN PANTALLA COMPLETA</span> ↗
        </a>
      </div>
    </form>"""

        if old_modal_end in content:
            content = content.replace(old_modal_end, new_modal_end, 1)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Linked admin.html in {os.path.basename(p)}")

if __name__ == '__main__':
    link_admin()
