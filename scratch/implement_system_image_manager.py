import re
import os

def upgrade_image_management():
    base_dir = '/Users/stevefernandovelarde/Desktop/web leo'
    admin_path = os.path.join(base_dir, 'admin.html')
    index_path = os.path.join(base_dir, 'index.html')
    mirror_path = os.path.join(base_dir, 'Happy_Tactical_Home_Mobile_Ordenado_V3-2.html')

    # 1. READ ADMIN.HTML
    with open(admin_path, 'r', encoding='utf-8') as f:
        admin_html = f.read()

    # Create the complete visual Image & Media Management Module for admin.html
    image_manager_module = """
        <!-- ========================================================================
             MÓDULO: GESTOR MULTIMEDIA & FOTOS DEL SISTEMA (TODAS LAS IMÁGENES)
             ======================================================================== -->
        <div class="module-card" id="module-imagenes">
          <div class="module-header">
            <div class="module-title-group">
              <span class="module-icon">🖼️</span>
              <div>
                <h3 class="module-title">Fotos del Sistema & Multimedia</h3>
                <p class="module-subtitle">Modifica cualquier imagen del sitio web subiendo fotos de tu galería o dispositivo</p>
              </div>
            </div>
            <button class="btn btn-primary btn-sm" onclick="saveAllImagesConfig()">
              <span>💾</span> Guardar Fotos
            </button>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-top: 16px;">
            
            <!-- 1. Logo Principal -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">🛡️ 01. Logo Principal (Navbar & Footer)</label>
                <span class="badge-tag">SISTEMA</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_logo" src="assets/images/img_930ab638.png" alt="Logo Preview" style="max-height: 65px; max-width: 100%; object-fit: contain;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_logo', 'input_img_logo')">
                </label>
                <input type="text" id="input_img_logo" class="form-control" placeholder="O pega la URL del logo" value="assets/images/img_930ab638.png" oninput="updateImagePreview('preview_logo', this.value)" style="font-size: 12px;">
              </div>
            </div>

            <!-- 2. Operador Táctico Portada (Hero) -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">🎖️ 02. Operador Táctico (Hero Portada)</label>
                <span class="badge-tag">HERO</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_hero" src="assets/images/img_7062ad4f.png" alt="Hero Preview" style="max-height: 80px; max-width: 100%; object-fit: cover; border-radius: 6px;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_hero', 'input_img_hero')">
                </label>
                <input type="text" id="input_img_hero" class="form-control" placeholder="O pega la URL del operador" value="assets/images/img_7062ad4f.png" oninput="updateImagePreview('preview_hero', this.value)" style="font-size: 12px;">
              </div>
            </div>

            <!-- 3. Foto Sección Nosotros / Misión -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">👥 03. Instructores (Sección Nosotros)</label>
                <span class="badge-tag">NOSOTROS</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_about" src="assets/images/img_3781d6ff.png" alt="About Preview" style="max-height: 80px; max-width: 100%; object-fit: cover; border-radius: 6px;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_about', 'input_img_about')">
                </label>
                <input type="text" id="input_img_about" class="form-control" placeholder="O pega la URL de la foto institucional" value="assets/images/img_3781d6ff.png" oninput="updateImagePreview('preview_about', this.value)" style="font-size: 12px;">
              </div>
            </div>

            <!-- 4. Foto Curso 1: Seguridad y Prevención -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">🎯 04. Portada Curso 1 (Seguridad)</label>
                <span class="badge-tag">CURSO 1</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_c1" src="assets/images/img_e7a7146c.jpg" alt="Curso 1 Preview" style="max-height: 80px; max-width: 100%; object-fit: cover; border-radius: 6px;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_c1', 'input_img_c1')">
                </label>
                <input type="text" id="input_img_c1" class="form-control" placeholder="O pega URL de portada Curso 1" value="assets/images/img_e7a7146c.jpg" oninput="updateImagePreview('preview_c1', this.value)" style="font-size: 12px;">
              </div>
            </div>

            <!-- 5. Foto Curso 2: Gestión de Emergencias -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">🚨 05. Portada Curso 2 (Emergencias)</label>
                <span class="badge-tag">CURSO 2</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_c2" src="assets/images/img_2d71eb4f.jpg" alt="Curso 2 Preview" style="max-height: 80px; max-width: 100%; object-fit: cover; border-radius: 6px;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_c2', 'input_img_c2')">
                </label>
                <input type="text" id="input_img_c2" class="form-control" placeholder="O pega URL de portada Curso 2" value="assets/images/img_2d71eb4f.jpg" oninput="updateImagePreview('preview_c2', this.value)" style="font-size: 12px;">
              </div>
            </div>

            <!-- 6. Foto Curso 3: Primeros Auxilios Tácticos -->
            <div class="field-card" style="background: rgba(14, 21, 38, 0.7); border: 1px solid rgba(0,229,255,0.2); border-radius: var(--radius-md); padding: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <label style="font-weight: 700; color: #fff; font-size: 13px;">🩹 06. Portada Curso 3 (TCCC Auxilios)</label>
                <span class="badge-tag">CURSO 3</span>
              </div>
              <div style="text-align: center; margin-bottom: 12px; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; min-height: 90px; display: flex; align-items: center; justify-content: center;">
                <img id="preview_c3" src="assets/images/img_5391baca.jpg" alt="Curso 3 Preview" style="max-height: 80px; max-width: 100%; object-fit: cover; border-radius: 6px;">
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                  <span>📁</span> Subir desde mi dispositivo / Galería
                  <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'preview_c3', 'input_img_c3')">
                </label>
                <input type="text" id="input_img_c3" class="form-control" placeholder="O pega URL de portada Curso 3" value="assets/images/img_5391baca.jpg" oninput="updateImagePreview('preview_c3', this.value)" style="font-size: 12px;">
              </div>
            </div>

          </div>
        </div>
    """

    # Replace or insert into admin.html
    if 'id="module-imagenes"' in admin_html:
        admin_html = re.sub(r'<div class="module-card" id="module-imagenes"[\s\S]*?</div>\s*</div>\s*</div>', image_manager_module, admin_html)
    else:
        # Insert after overview or first module card
        pos = admin_html.find('<div class="module-card"')
        if pos != -1:
            admin_html = admin_html[:pos] + image_manager_module + "\n" + admin_html[pos:]

    # Add Image Handler JavaScript in admin.html
    image_js_handlers = """
    // ========================================================================
    // GESTOR DE SUBIDA DE IMÁGENES DESDE GALERÍA / DISPOSITIVO (FILEREADER)
    // ========================================================================
    function handleImageFileUpload(event, previewImgId, targetInputId) {
      const file = event.target.files[0];
      if (!file) return;

      if (!file.type.startsWith('image/')) {
        alert('Por favor selecciona un archivo de imagen válido.');
        return;
      }

      const reader = new FileReader();
      reader.onload = function(e) {
        const base64Data = e.target.result;
        const previewEl = document.getElementById(previewImgId);
        const inputEl = document.getElementById(targetInputId);
        
        if (previewEl) previewEl.src = base64Data;
        if (inputEl) inputEl.value = base64Data;
        
        showToast('Foto cargada desde tu dispositivo.');
      };
      reader.readAsDataURL(file);
    }

    function updateImagePreview(previewImgId, url) {
      const previewEl = document.getElementById(previewImgId);
      if (previewEl && url) {
        previewEl.src = url;
      }
    }

    function saveAllImagesConfig() {
      const config = JSON.parse(localStorage.getItem('HT_CONFIG_PROD_V3') || '{}');
      config.images = config.images || {};
      
      config.images.logo = document.getElementById('input_img_logo') ? document.getElementById('input_img_logo').value : 'assets/images/img_930ab638.png';
      config.images.hero = document.getElementById('input_img_hero') ? document.getElementById('input_img_hero').value : 'assets/images/img_7062ad4f.png';
      config.images.about = document.getElementById('input_img_about') ? document.getElementById('input_img_about').value : 'assets/images/img_3781d6ff.png';
      config.images.c1 = document.getElementById('input_img_c1') ? document.getElementById('input_img_c1').value : 'assets/images/img_e7a7146c.jpg';
      config.images.c2 = document.getElementById('input_img_c2') ? document.getElementById('input_img_c2').value : 'assets/images/img_2d71eb4f.jpg';
      config.images.c3 = document.getElementById('input_img_c3') ? document.getElementById('input_img_c3').value : 'assets/images/img_5391baca.jpg';

      localStorage.setItem('HT_CONFIG_PROD_V3', JSON.stringify(config));
      localStorage.setItem('HT_CUSTOM_CONFIG_V2', JSON.stringify(config));
      localStorage.setItem('HT_OWNER_CONFIG_V2', JSON.stringify(config));
      window.dispatchEvent(new CustomEvent('ht_config_updated'));
      showToast('✓ Todas las fotos del sistema guardadas y sincronizadas.');
    }

    // Modal para agregar foto a la galería desde dispositivo o URL
    function promptAddGalleryPhoto() {
      const modalHtml = `
        <div id="addPhotoModal" style="position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(8px); z-index: 999999; display: flex; align-items: center; justify-content: center; padding: 20px;">
          <div style="background: #0d1424; border: 1px solid var(--neon-cyan); border-radius: 12px; padding: 24px; max-width: 480px; width: 100%; box-shadow: 0 0 30px rgba(0,229,255,0.25);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <h3 style="color: #fff; font-size: 16px; font-weight: 800; font-family: var(--font-display);">📸 AÑADIR FOTO A LA GALERÍA</h3>
              <button onclick="document.getElementById('addPhotoModal').remove()" style="background: none; border: none; color: #fff; font-size: 20px; cursor: pointer;">&times;</button>
            </div>
            
            <div style="margin-bottom: 12px; text-align: center; background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px;">
              <img id="newGalleryPreview" src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=800&q=80" style="max-height: 120px; max-width: 100%; border-radius: 6px; object-fit: cover;">
            </div>

            <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
              <label class="btn btn-secondary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer;">
                <span>📁</span> Seleccionar foto de mi galería / dispositivo
                <input type="file" accept="image/*" style="display: none;" onchange="handleImageFileUpload(event, 'newGalleryPreview', 'newGalleryUrl')">
              </label>

              <input type="text" id="newGalleryUrl" class="form-control" placeholder="O ingresa URL de la imagen" value="https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=800&q=80" oninput="updateImagePreview('newGalleryPreview', this.value)" style="font-size: 12px;">
              <input type="text" id="newGalleryTitle" class="form-control" placeholder="Título de la fotografía (ej: Polígono de Tiro)" value="Entrenamiento Operativo" style="font-size: 12px;">
              <input type="text" id="newGalleryBadge" class="form-control" placeholder="Insignia / Categoría (ej: TÁCTICO, NOCTURNO)" value="TÁCTICO" style="font-size: 12px;">
            </div>

            <div style="display: flex; gap: 10px; justify-content: flex-end;">
              <button class="btn btn-secondary btn-sm" onclick="document.getElementById('addPhotoModal').remove()">Cancelar</button>
              <button class="btn btn-primary btn-sm" onclick="confirmAddGalleryPhoto()">Confirmar y Guardar</button>
            </div>
          </div>
        </div>
      `;
      const div = document.createElement('div');
      div.innerHTML = modalHtml;
      document.body.appendChild(div.firstElementChild);
    }

    function confirmAddGalleryPhoto() {
      const url = document.getElementById('newGalleryUrl').value.trim();
      const title = document.getElementById('newGalleryTitle').value.trim() || 'Foto Operativa';
      const badge = document.getElementById('newGalleryBadge').value.trim() || 'TÁCTICO';

      if (!url) {
        alert('Por favor sube una imagen o ingresa una URL válida.');
        return;
      }

      if (!APP_CONFIG.gallery) APP_CONFIG.gallery = [];
      APP_CONFIG.gallery.push({
        id: 'gal-' + Date.now(),
        title: title,
        badge: badge,
        url: url,
        location: 'Happy Tactical - Sede Lima'
      });

      saveConfiguration();
      renderGalleryAdminCards();
      const modal = document.getElementById('addPhotoModal');
      if (modal) modal.remove();
      showToast('✓ Nueva foto agregada a la galería.');
    }
    """

    if 'function handleImageFileUpload' not in admin_html:
        script_pos = admin_html.rfind('</script>')
        admin_html = admin_html[:script_pos] + "\n" + image_js_handlers + "\n" + admin_html[script_pos:]

    # Replace old promptAddPhoto in admin.html
    admin_html = re.sub(r'function addPhoto\(\)[\s\S]*?\}', 'function addPhoto() { promptAddGalleryPhoto(); }', admin_html)

    with open(admin_path, 'w', encoding='utf-8') as f:
        f.write(admin_html)
    print("✓ Updated admin.html with device file pickers and complete system image manager.")

    # 2. UPDATE INDEX.HTML TO APPLY ALL SYSTEM IMAGES DYNAMICALLY FROM STORAGE
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_html = f.read()

    # In index.html applyConfigToDOM:
    apply_images_js = """
      // Aplicar imágenes personalizadas del sistema
      if (config.images) {
        if (config.images.logo) {
          const navLogo = document.getElementById('mainNavLogo');
          const footLogo = document.getElementById('mainFooterLogo');
          if (navLogo) navLogo.src = config.images.logo;
          if (footLogo) footLogo.src = config.images.logo;
        }
        if (config.images.hero) {
          const heroImg = document.getElementById('heroBgImg');
          if (heroImg) heroImg.src = config.images.hero;
        }
        if (config.images.about) {
          const aboutImg = document.getElementById('aboutPhotoImg');
          if (aboutImg) aboutImg.src = config.images.about;
        }
        if (config.images.c1) {
          const c1 = document.getElementById('c1Img');
          if (c1) c1.src = config.images.c1;
        }
        if (config.images.c2) {
          const c2 = document.getElementById('c2Img');
          if (c2) c2.src = config.images.c2;
        }
        if (config.images.c3) {
          const c3 = document.getElementById('c3Img');
          if (c3) c3.src = config.images.c3;
        }
      }
    """

    if 'applyCustomSystemImages' not in idx_html:
        # Inject into applyConfigToDOM or DOMContentLoaded
        idx_html = idx_html.replace('function applyConfigToDOM(config) {', 'function applyConfigToDOM(config) {\n' + apply_images_js)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_html)
    with open(mirror_path, 'w', encoding='utf-8') as f:
        f.write(idx_html)

    print("✓ Updated index.html and mirror to dynamically render all custom images from storage.")

if __name__ == '__main__':
    upgrade_image_management()
