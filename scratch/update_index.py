import re
import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print('Initial length:', len(content))

    # 1. ADD VIDEO CSS STYLES
    video_css = """
    /* ========================================================================
       TACTICAL VIDEO GALLERY & CINEMA MODAL
       ======================================================================== */
    .tactical-videos-wrap {
      margin-top: 55px;
      padding-top: 45px;
      border-top: 1px dashed rgba(0, 229, 255, 0.2);
      position: relative;
    }

    .tactical-video-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 25px;
    }

    .tactical-video-card {
      background: rgba(13, 17, 26, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }

    .tactical-video-card:hover {
      transform: translateY(-6px);
      border-color: var(--neon-cyan);
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.8), 0 0 24px rgba(0, 229, 255, 0.3);
    }

    .video-thumb-container {
      position: relative;
      height: 200px;
      overflow: hidden;
      background: #040508;
    }

    .video-thumb-container img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
      filter: brightness(0.88);
    }

    .tactical-video-card:hover .video-thumb-container img {
      transform: scale(1.06);
      filter: brightness(1.02);
    }

    .video-card-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0, 0, 0, 0.1) 0%, rgba(3, 4, 7, 0.85) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .video-play-pulse-btn {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.9);
      color: #030407;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 900;
      box-shadow: 0 0 20px rgba(0, 229, 255, 0.6);
      transition: transform 0.3s ease, background-color 0.3s ease;
      padding-left: 3px;
    }

    .tactical-video-card:hover .video-play-pulse-btn {
      transform: scale(1.15);
      background: #ffffff;
      box-shadow: 0 0 28px rgba(0, 229, 255, 0.9);
    }

    .video-duration-pill {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(7, 9, 15, 0.85);
      border: 1px solid var(--border-cyan);
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.5px;
      backdrop-filter: blur(4px);
    }

    .video-badge-pill {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(0, 229, 255, 0.15);
      border: 1px solid var(--neon-cyan);
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 1px;
      backdrop-filter: blur(4px);
      text-transform: uppercase;
    }

    .video-card-content {
      padding: 18px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }

    .video-card-title {
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      color: var(--text-white);
      line-height: 1.4;
      margin-bottom: 8px;
      transition: color 0.25s ease;
    }

    .tactical-video-card:hover .video-card-title {
      color: var(--neon-cyan);
    }

    .video-card-desc {
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 14px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .video-card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }

    .video-watch-link {
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.8px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Modal de Video Táctico Cinema */
    .tactical-video-modal {
      width: 92%;
      max-width: 900px;
      background: rgba(7, 9, 15, 0.96);
      border: 1px solid var(--border-cyan);
      border-radius: var(--radius-md);
      color: var(--text-main);
      padding: 0;
      box-shadow: 0 25px 80px rgba(0, 0, 0, 0.9), 0 0 35px rgba(0, 229, 255, 0.25);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      overflow: hidden;
    }

    .tactical-video-modal::backdrop {
      background: rgba(2, 3, 5, 0.85);
      backdrop-filter: blur(10px);
    }

    .video-modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(13, 17, 26, 0.8);
    }

    .video-modal-badge {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      color: var(--neon-cyan);
      letter-spacing: 1.5px;
    }

    .video-player-container {
      position: relative;
      width: 100%;
      background: #000;
    }

    .video-iframe-wrap {
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 Aspect Ratio */
    }

    .video-iframe-wrap iframe {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border: none;
    }

    .video-modal-footer {
      padding: 18px 20px;
      background: rgba(13, 17, 26, 0.8);
      border-top: 1px solid var(--border-subtle);
    }

    @media (max-width: 768px) {
      .tactical-video-grid {
        grid-template-columns: 1fr;
      }
      .video-thumb-container {
        height: 180px;
      }
    }
  </style>
"""

    if '</style>' in content:
        content = content.replace('  </style>', video_css, 1)
        print('✓ Video CSS added')
    else:
        print('Error: </style> not found')
        sys.exit(1)

    # 2. REMOVE CLIENT-SIDE SPEED BUTTON AND ADD TACTICAL VIDEOS WRAP IN #galeria
    old_hud_btns = """              <button type="button" class="gallery-hud-btn" onclick="stepGalleryStream(300)" title="Avanzar">
                <span>SIGUIENTE ▶</span>
              </button>
              <button type="button" class="gallery-hud-btn" id="btnSpeed" onclick="toggleGallerySpeed()" title="Alternar velocidad de rotación">
                <span>⚡ VELOCIDAD: <b id="speedVal">1X</b></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>"""

    new_hud_btns_and_videos = """              <button type="button" class="gallery-hud-btn" onclick="stepGalleryStream(300)" title="Avanzar">
                <span>SIGUIENTE ▶</span>
              </button>
            </div>
          </div>
        </div>

        <!-- SECCIÓN DE VIDEOS TÁCTICOS (VIDEOTECA OPERATIVA) -->
        <div class="tactical-videos-wrap">
          <div class="section-head" style="margin-bottom: 24px;">
            <span class="section-kicker">EVIDENCIA AUDIOVISUAL // REGISTRO EN ACCIÓN</span>
            <h3 class="section-title" style="font-size: clamp(20px, 3.5vw, 32px);">VIDEOTECA <span>TÁCTICA</span></h3>
            <p class="section-desc">
              Visualiza en video nuestras operaciones de entrenamiento en campo: medicina de combate bajo fuego (TCCC), tiro defensivo de alta precisión, rescate y simulación para brigadas.
            </p>
          </div>

          <!-- Filtros de Videos -->
          <div class="calendar-filters" role="tablist" aria-label="Filtros de videos tácticos" style="margin-bottom: 30px; justify-content: center;">
            <button type="button" class="filter-btn active" onclick="filterTacticalVideos('todos', this)" role="tab" aria-selected="true">TODOS LOS VIDEOS</button>
            <button type="button" class="filter-btn" onclick="filterTacticalVideos('seguridad', this)" role="tab" aria-selected="false">TIRO &amp; SEGURIDAD</button>
            <button type="button" class="filter-btn" onclick="filterTacticalVideos('primeros-auxilios', this)" role="tab" aria-selected="false">MEDICINA TCCC</button>
            <button type="button" class="filter-btn" onclick="filterTacticalVideos('emergencias', this)" role="tab" aria-selected="false">GESTIÓN EMERGENCIAS</button>
            <button type="button" class="filter-btn" onclick="filterTacticalVideos('corporativo', this)" role="tab" aria-selected="false">BRIGADAS EMPRESAS</button>
          </div>

          <!-- Grid de Tarjetas de Video Tácticas -->
          <div class="tactical-video-grid" id="tacticalVideoGrid">
            <!-- Rendered dynamically by JavaScript -->
          </div>
        </div>
      </div>
    </section>"""

    if old_hud_btns in content:
        content = content.replace(old_hud_btns, new_hud_btns_and_videos, 1)
        print('✓ Gallery HUD button cleaned & Videoteca section added')
    else:
        print('Error: old_hud_btns match not found')
        sys.exit(1)

    # 3. ADD TACTICAL VIDEO MODAL DIALOG
    old_modal_anchor = """  <dialog class="calendar-sync-modal" id="calSyncModal">"""
    video_modal_html = """  <!-- TACTICAL VIDEO CINEMA MODAL -->
  <dialog class="tactical-video-modal" id="tacticalVideoModal">
    <div class="video-modal-header">
      <div class="video-modal-title-wrap">
        <span class="video-modal-badge" id="videoModalBadge">[ TCCC EN COMBATE ]</span>
        <h3 id="videoModalTitle" style="font-family: var(--font-display); font-size: clamp(16px, 2.5vw, 20px); color: var(--text-white); margin-top: 4px;">Título del Video</h3>
      </div>
      <button type="button" class="modal-close-btn" onclick="closeTacticalVideoModal()" aria-label="Cerrar video">&times;</button>
    </div>

    <div class="video-player-container">
      <div class="video-iframe-wrap" id="videoPlayerContainer">
        <!-- iframe rendered dynamically -->
      </div>
    </div>

    <div class="video-modal-footer">
      <div class="video-modal-desc-wrap">
        <p id="videoModalDesc" style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin: 0;"></p>
      </div>
      <div style="display: flex; gap: 10px; align-items: center; justify-content: flex-end; flex-wrap: wrap; margin-top: 14px;">
        <button type="button" class="btn btn-secondary btn-sm" onclick="closeTacticalVideoModal()">CERRAR</button>
        <a href="#" id="videoWhatsAppBtn" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
          CONSULTAR POR ESTE CURSO EN WHATSAPP 📲
        </a>
      </div>
    </div>
  </dialog>

  <dialog class="calendar-sync-modal" id="calSyncModal">"""

    if old_modal_anchor in content:
        content = content.replace(old_modal_anchor, video_modal_html, 1)
        print('✓ Tactical Video Modal dialog added')
    else:
        print('Error: old_modal_anchor not found')
        sys.exit(1)

    # 4. UPDATE DEFAULT_CONFIG WITH GALLERY SPEED & VIDEOS
    old_default_config_end = """        {
          id: 'gal-10',
          image: 'https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=1400&q=85'
        }
      ]
    };"""

    new_default_config_end = """        {
          id: 'gal-10',
          image: 'https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=1400&q=85'
        }
      ],
      gallerySpeed: '1x',
      galleryAutoScroll: true,
      videos: [
        {
          id: 'vid-1',
          title: 'Procedimientos de Medicina Táctica TCCC en Zona Hostil',
          badge: 'TCCC EN COMBATE',
          duration: '04:20',
          category: 'primeros-auxilios',
          videoUrl: 'https://www.youtube.com/embed/dQw4w9WgXcQ',
          thumbnail: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=1200&q=80',
          desc: 'Protocolos de atención bajo fuego, colocación de torniquetes de combate y empaquetamiento de heridas en zona de alto riesgo.'
        },
        {
          id: 'vid-2',
          title: 'Técnicas de Intervención Rápida & Tiro Táctico Defensivo',
          badge: 'TIRO DEFENSIVO',
          duration: '03:45',
          category: 'seguridad',
          videoUrl: 'https://www.youtube.com/embed/ScMzIvxBSi4',
          thumbnail: 'https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=1200&q=80',
          desc: 'Desplazamiento táctico en binomio, transición de armamento secundario y resolución de enfrentamientos en espacios reducidos.'
        },
        {
          id: 'vid-3',
          title: 'Simulacro de Comando y Control de Incidentes Mayores',
          badge: 'GESTIÓN EMERGENCIAS',
          duration: '05:10',
          category: 'emergencias',
          videoUrl: 'https://www.youtube.com/embed/kJQP7kiw5Fk',
          thumbnail: 'https://images.unsplash.com/photo-1582139329536-e7284fece509?auto=format&fit=crop&w=1200&q=80',
          desc: 'Metodología del Sistema de Comando de Incidentes (SCI) aplicada a evacuación masiva, sismos e incendios estructurales.'
        },
        {
          id: 'vid-4',
          title: 'Entrenamiento In-House para Brigadas Corporativas',
          badge: 'BRIGADA CORPORATIVA',
          duration: '02:50',
          category: 'corporativo',
          videoUrl: 'https://www.youtube.com/embed/3JZ_D3ELwOQ',
          thumbnail: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80',
          desc: 'Capacitación integral para brigadistas empresariales en primeros auxilios, control de pánico y rescate primario.'
        }
      ]
    };"""

    if old_default_config_end in content:
        content = content.replace(old_default_config_end, new_default_config_end, 1)
        print('✓ DEFAULT_CONFIG updated with gallerySpeed and videos')
    else:
        print('Error: old_default_config_end not found')
        sys.exit(1)

    # 5. UPDATE applyConfigToDOM TO APPLY GALLERY SPEED AND RENDER VIDEOS
    old_apply_end = """      applyImagesAndFraming();
      renderScheduleList();
      populateOwnerFormInputs();
    }"""

    new_apply_end = """      applyImagesAndFraming();
      renderScheduleList();
      populateOwnerFormInputs();

      // Apply Admin Speed & Dynamic Control to Gallery Stream
      const speed = HT_CONFIG.gallerySpeed || '1x';
      const duration = speed === '0.5x' ? '55s' : (speed === '2x' ? '18s' : '38s');
      const track1 = document.getElementById('galleryTrack1');
      const track2 = document.getElementById('galleryTrack2');
      if (track1) track1.style.animationDuration = duration;
      if (track2) track2.style.animationDuration = duration;

      if (HT_CONFIG.galleryAutoScroll === false) {
        isGalleryPaused = true;
        if (track1) track1.classList.add('paused');
        if (track2) track2.classList.add('paused');
        const pulse = document.getElementById('galleryPulse');
        if (pulse) pulse.classList.add('paused');
        const statusTxt = document.getElementById('galleryStatusText');
        if (statusTxt) statusTxt.textContent = 'ROTACIÓN PAUSADA // MODO INSPECCIÓN';
        const playIcon = document.getElementById('playIcon');
        if (playIcon) playIcon.textContent = '▶';
        const playText = document.getElementById('playText');
        if (playText) playText.textContent = 'REANUDAR';
      }

      // Render Tactical Video Library
      renderTacticalVideos();
    }"""

    if old_apply_end in content:
        content = content.replace(old_apply_end, new_apply_end, 1)
        print('✓ applyConfigToDOM updated')
    else:
        print('Error: old_apply_end not found')
        sys.exit(1)

    # 6. ADD VIDEO JS FUNCTIONS (renderTacticalVideos, filterTacticalVideos, openTacticalVideoModal, closeTacticalVideoModal, getEmbedUrl)
    video_js_code = """
    // ========================================================================
    // TACTICAL VIDEO LIBRARY & CINEMA MODAL
    // ========================================================================
    let currentVideoCategory = 'todos';

    function getEmbedUrl(url) {
      if (!url) return '';
      if (url.includes('youtube.com/embed/')) return url;
      const ytMatch = url.match(/(?:youtube\\.com\\/(?:[^\\/]+\\/.+\\/|(?:v|e(?:mbed)?)\\/|.*[?&]v=)|youtu\\.be\\/)([^"&?\\/\\s]{11})/i);
      if (ytMatch && ytMatch[1]) {
        return `https://www.youtube.com/embed/${ytMatch[1]}?autoplay=1&rel=0`;
      }
      const vimeoMatch = url.match(/vimeo\\.com\\/(\\d+)/i);
      if (vimeoMatch && vimeoMatch[1]) {
        return `https://player.vimeo.com/video/${vimeoMatch[1]}?autoplay=1`;
      }
      return url;
    }

    function renderTacticalVideos(category = 'todos') {
      currentVideoCategory = category;
      const grid = document.getElementById('tacticalVideoGrid');
      if (!grid) return;

      const videoList = (HT_CONFIG.videos && Array.isArray(HT_CONFIG.videos) && HT_CONFIG.videos.length > 0)
        ? HT_CONFIG.videos
        : DEFAULT_CONFIG.videos;

      const filtered = category === 'todos'
        ? videoList
        : videoList.filter(v => v.category === category);

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px; background: rgba(13,17,26,0.5); border: 1px dashed var(--border-subtle); border-radius: var(--radius-md);">
            <div style="font-size: 28px; margin-bottom: 8px;">🎬</div>
            <div style="font-family: var(--font-display); color: var(--text-white); font-size: 14px;">No hay videos registrados en esta categoría táctica.</div>
            <div style="color: var(--text-muted); font-size: 12px; margin-top: 4px;">Selecciona otra categoría o explora todos los videos.</div>
          </div>
        `;
        return;
      }

      grid.innerHTML = filtered.map(item => {
        return `
          <article class="tactical-video-card" onclick="openTacticalVideoModal('${item.id}')" role="button" tabindex="0" aria-label="Ver video: ${item.title}">
            <div class="video-thumb-container">
              ${item.thumbnail ? `<img src="${item.thumbnail}" alt="${item.title}" loading="lazy">` : `<div style="display:flex; align-items:center; justify-content:center; height:100%; color:var(--neon-cyan); font-size:32px;">▶</div>`}
              <div class="video-card-overlay">
                <div class="video-play-pulse-btn" aria-hidden="true">▶</div>
              </div>
              <span class="video-badge-pill">${item.badge || 'VIDEO TÁCTICO'}</span>
              <span class="video-duration-pill">⏱️ ${item.duration || '03:30'}</span>
            </div>

            <div class="video-card-content">
              <div>
                <h4 class="video-card-title">${item.title}</h4>
                <p class="video-card-desc">${item.desc || 'Entrenamiento táctico y operativo especializado.'}</p>
              </div>
              <div class="video-card-footer">
                <span class="video-watch-link">
                  <span>REPRODUCIR VIDEO</span>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                </span>
                <span style="font-family: var(--font-display); font-size: 10.5px; color: var(--text-dim); text-transform: uppercase;">${item.category || 'TÁCTICO'}</span>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    function filterTacticalVideos(category, btn) {
      if (btn) {
        const buttons = btn.parentElement.querySelectorAll('.filter-btn');
        buttons.forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        });
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
      }
      renderTacticalVideos(category);
    }

    function openTacticalVideoModal(videoId) {
      const videoList = (HT_CONFIG.videos && Array.isArray(HT_CONFIG.videos) && HT_CONFIG.videos.length > 0)
        ? HT_CONFIG.videos
        : DEFAULT_CONFIG.videos;

      const item = videoList.find(v => v.id === videoId);
      if (!item) return;

      const modal = document.getElementById('tacticalVideoModal');
      const badge = document.getElementById('videoModalBadge');
      const title = document.getElementById('videoModalTitle');
      const desc = document.getElementById('videoModalDesc');
      const playerWrap = document.getElementById('videoPlayerContainer');
      const waBtn = document.getElementById('videoWhatsAppBtn');

      if (badge) badge.textContent = `[ ${item.badge || 'VIDEO TÁCTICO'} ]`;
      if (title) title.textContent = item.title;
      if (desc) desc.textContent = item.desc || 'Demostración práctica de procedimientos y maniobras operativas.';

      const embedUrl = getEmbedUrl(item.videoUrl);
      if (playerWrap) {
        playerWrap.innerHTML = `
          <iframe 
            src="${embedUrl}" 
            title="${item.title}" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        `;
      }

      if (waBtn) {
        const cleanWa = (HT_CONFIG.whatsApp || '51977331267').replace(/\\D/g, '');
        const msg = encodeURIComponent(`Hola Happy Tactical, vi el video "${item.title}" y quisiera información sobre las capacitaciones en este tema.`);
        waBtn.href = `https://wa.me/${cleanWa}?text=${msg}`;
      }

      if (modal && typeof modal.showModal === 'function') {
        modal.showModal();
        document.body.style.overflow = 'hidden';
      }
    }

    function closeTacticalVideoModal() {
      const modal = document.getElementById('tacticalVideoModal');
      const playerWrap = document.getElementById('videoPlayerContainer');
      if (playerWrap) playerWrap.innerHTML = ''; // Stop video playback
      if (modal && typeof modal.close === 'function') {
        modal.close();
      }
      document.body.style.overflow = '';
    }

    // Modal backdrop click to close
    document.addEventListener('DOMContentLoaded', () => {
      const videoModal = document.getElementById('tacticalVideoModal');
      if (videoModal) {
        videoModal.addEventListener('click', (e) => {
          const rect = videoModal.getBoundingClientRect();
          const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                              rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
          if (!isInDialog) {
            closeTacticalVideoModal();
          }
        });
      }
    });
"""

    old_script_anchor = "    function stepGalleryStream(delta) {"
    if old_script_anchor in content:
        content = content.replace(old_script_anchor, video_js_code + "\n    function stepGalleryStream(delta) {", 1)
        print('✓ Video JS functions added')
    else:
        print('Error: old_script_anchor not found')
        sys.exit(1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Final length:', len(content))
    print('✓ index.html successfully updated!')

if __name__ == '__main__':
    main()
