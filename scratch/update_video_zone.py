import re
import sys
import os

def update_index():
    path = '/Users/stevefernandovelarde/Desktop/web leo/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Original index.html length: {len(content)}")

    # 1. CLEAN UP CSS AND ADD COMPLETE TACTICAL VIDEO & GALLERY STYLES
    # Search for start of TACTICAL VIDEO GALLERY & CINEMA MODAL
    css_start_idx = content.find('/* ========================================================================\n       TACTICAL VIDEO GALLERY & CINEMA MODAL')
    if css_start_idx == -1:
        css_start_idx = content.find('/* ========================================================================\r\n       TACTICAL VIDEO GALLERY & CINEMA MODAL')
    
    css_end_idx = content.find('</style>', css_start_idx)
    if css_start_idx == -1 or css_end_idx == -1:
        print("Could not find CSS markers, searching alternative...")
        css_start_idx = content.find('.tactical-videos-wrap')
        css_end_idx = content.find('</style>', css_start_idx)

    print(f"CSS block replacement from index {css_start_idx} to {css_end_idx}")

    new_video_css = """    /* ========================================================================
       TACTICAL CONTINUOUS GALLERY & LIGHTBOX (PHOTO STREAM)
       ======================================================================== */
    .gallery-section-wrap {
      position: relative;
      overflow: hidden;
    }

    /* ========================================================================
       TACTICAL VIDEOTECA OPERATIVA & CINEMA SPOTLIGHT (VIDEO ZONE)
       ======================================================================== */
    .video-section-wrap {
      position: relative;
      background: radial-gradient(circle at 50% 0%, rgba(255, 0, 127, 0.05) 0%, transparent 65%), #05070c;
      border-top: 1px solid rgba(0, 229, 255, 0.12);
      border-bottom: 1px solid rgba(0, 229, 255, 0.12);
      overflow: hidden;
    }

    .video-spotlight-wrap {
      margin-top: 25px;
      margin-bottom: 35px;
    }

    .tactical-video-spotlight {
      background: rgba(13, 17, 26, 0.85);
      border: 1.5px solid var(--border-cyan);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 229, 255, 0.15);
      position: relative;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .tactical-video-spotlight:hover {
      border-color: var(--neon-cyan);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9), 0 0 45px rgba(0, 229, 255, 0.3);
    }

    .spotlight-media-wrap {
      position: relative;
      height: 380px;
      background: #000;
      overflow: hidden;
      cursor: pointer;
    }

    .spotlight-thumb {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
      filter: brightness(0.85);
    }

    .tactical-video-spotlight:hover .spotlight-thumb {
      transform: scale(1.04);
      filter: brightness(0.98);
    }

    .spotlight-scanline-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
      background-size: 100% 3px, 3px 100%;
      pointer-events: none;
      z-index: 2;
    }

    .spotlight-rec-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(3, 4, 7, 0.88);
      border: 1px solid var(--neon-pink);
      color: #fff;
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 1.2px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      gap: 7px;
      z-index: 3;
      backdrop-filter: blur(6px);
    }

    .spotlight-rec-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--neon-pink);
      box-shadow: 0 0 8px var(--neon-pink);
      animation: pulseAlert 1.2s infinite ease-in-out;
    }

    .spotlight-duration-tag {
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(3, 4, 7, 0.88);
      border: 1px solid var(--border-cyan);
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.8px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      z-index: 3;
      backdrop-filter: blur(6px);
    }

    .spotlight-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(3,4,7,0.7) 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      z-index: 3;
    }

    .spotlight-play-pulse-btn {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.92);
      color: #030407;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      box-shadow: 0 0 25px rgba(0, 229, 255, 0.7);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.25s ease, box-shadow 0.3s ease;
      padding-left: 4px;
    }

    .tactical-video-spotlight:hover .spotlight-play-pulse-btn {
      transform: scale(1.18);
      background: #ffffff;
      box-shadow: 0 0 35px rgba(0, 229, 255, 1);
    }

    .spotlight-tap-hint {
      font-family: var(--font-display);
      font-size: 11px;
      color: var(--neon-cyan);
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      text-shadow: 0 2px 10px rgba(0,0,0,0.9);
      opacity: 0.9;
    }

    .spotlight-meta {
      padding: 32px 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: rgba(13, 17, 26, 0.95);
      position: relative;
    }

    .spotlight-meta::before {
      content: "";
      position: absolute;
      left: 0;
      top: 20px;
      bottom: 20px;
      width: 1px;
      background: linear-gradient(180deg, transparent, rgba(0, 229, 255, 0.3), transparent);
    }

    .spotlight-header-tags {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .spotlight-category-label {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .spotlight-title {
      font-family: var(--font-display);
      font-size: clamp(18px, 2.2vw, 24px);
      font-weight: 800;
      color: var(--text-white);
      line-height: 1.35;
      margin-bottom: 12px;
    }

    .spotlight-desc {
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .spotlight-action-row {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      align-items: center;
    }

    /* Grid de Videos Tácticos */
    .tactical-video-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 26px;
      margin-top: 15px;
    }

    .tactical-video-card {
      background: rgba(13, 17, 26, 0.78);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }

    .tactical-video-card:hover {
      transform: translateY(-7px);
      border-color: var(--neon-cyan);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85), 0 0 26px rgba(0, 229, 255, 0.3);
    }

    .video-thumb-container {
      position: relative;
      height: 205px;
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
      transform: scale(1.07);
      filter: brightness(1.02);
    }

    .video-card-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0, 0, 0, 0.1) 0%, rgba(3, 4, 7, 0.82) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .video-play-pulse-btn {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.9);
      color: #030407;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 900;
      box-shadow: 0 0 20px rgba(0, 229, 255, 0.65);
      transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
      padding-left: 3px;
    }

    .tactical-video-card:hover .video-play-pulse-btn {
      transform: scale(1.16);
      background: #ffffff;
      box-shadow: 0 0 30px rgba(0, 229, 255, 0.95);
    }

    .video-duration-pill {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(7, 9, 15, 0.88);
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
      padding: 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }

    .video-card-title {
      font-family: var(--font-display);
      font-size: 15.5px;
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
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .video-card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 14px;
      border-top: 1px solid rgba(255, 255, 255, 0.07);
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
      transition: gap 0.2s ease;
    }

    .tactical-video-card:hover .video-watch-link {
      gap: 9px;
      color: #fff;
    }

    /* Modal de Video Táctico Cinema */
    .tactical-video-modal {
      width: 94%;
      max-width: 950px;
      background: rgba(7, 9, 15, 0.98);
      border: 1.5px solid var(--border-cyan);
      border-radius: var(--radius-md);
      color: var(--text-main);
      padding: 0;
      box-shadow: 0 25px 90px rgba(0, 0, 0, 0.95), 0 0 45px rgba(0, 229, 255, 0.3);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      overflow: hidden;
      margin: auto;
    }

    .tactical-video-modal::backdrop {
      background: rgba(2, 3, 5, 0.88);
      backdrop-filter: blur(12px);
    }

    .video-modal-header {
      padding: 16px 22px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(13, 17, 26, 0.88);
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
      padding: 20px 22px;
      background: rgba(13, 17, 26, 0.92);
      border-top: 1px solid var(--border-subtle);
    }

    @media (max-width: 900px) {
      .tactical-video-spotlight {
        grid-template-columns: 1fr;
      }
      .spotlight-media-wrap {
        height: 250px;
      }
      .spotlight-meta::before {
        display: none;
      }
      .spotlight-meta {
        padding: 22px 18px;
      }
    }

    @media (max-width: 600px) {
      .tactical-video-grid {
        grid-template-columns: 1fr;
      }
      .video-thumb-container {
        height: 185px;
      }
    }
  """

    content = content[:css_start_idx] + new_video_css + '\n  ' + content[css_end_idx:]

    # 2. UPDATE NAVBAR LINKS: ADD "VIDEOS" AFTER "GALERÍA"
    content = content.replace(
        '<li><a href="#galeria" class="nav-link">GALERÍA</a></li>',
        '<li><a href="#galeria" class="nav-link">GALERÍA</a></li>\n          <li><a href="#videos" class="nav-link">VIDEOS</a></li>'
    )

    # 3. UPDATE MOBILE DRAWER LINKS: ADD "VIDEOTECA TÁCTICA" AFTER "GALERÍA OPERATIVA"
    content = content.replace(
        '<a href="#galeria" class="nav-link mobile-link">GALERÍA OPERATIVA</a>',
        '<a href="#galeria" class="nav-link mobile-link">GALERÍA OPERATIVA</a>\n    <a href="#videos" class="nav-link mobile-link">VIDEOTECA TÁCTICA</a>'
    )

    # 4. UPDATE FLOATING DOCK: ADD "VIDEOS" JUMP BUTTON
    content = content.replace(
        '<button type="button" class="dock-jump-btn" onclick="scrollToTacticalSection(\'cursos\')">📍 CURSOS</button>',
        '<button type="button" class="dock-jump-btn" onclick="scrollToTacticalSection(\'cursos\')">📍 CURSOS</button>\n      <button type="button" class="dock-jump-btn" onclick="scrollToTacticalSection(\'galeria\')">📍 GALERÍA</button>\n      <button type="button" class="dock-jump-btn" onclick="scrollToTacticalSection(\'videos\')">📍 VIDEOS</button>'
    )

    # 5. REORGANIZE GALLERY AND VIDEO SECTIONS IN HTML
    # We want:
    # 3.5. GALERÍA TÁCTICA INTERACTIVA CONTINUA (Photo Stream & HUD)
    # 3.6. VIDEOTECA OPERATIVA TÁCTICA & SPOTLIGHT CINEMA (Dedicated Video Section)
    
    old_galeria_start = content.find('<!-- 3.5. GALERÍA TÁCTICA INTERACTIVA CONTINUA -->')
    old_calendario_start = content.find('<!-- 4. CALENDARIO -->')

    if old_galeria_start != -1 and old_calendario_start != -1:
        print(f"Found Galeria and Calendario sections: {old_galeria_start} to {old_calendario_start}")
        
        new_sections_html = """<!-- 3.5. GALERÍA TÁCTICA INTERACTIVA CONTINUA -->
    <section class="section-spacing gallery-section-wrap" id="galeria" aria-labelledby="gallery-title" style="background: radial-gradient(circle at 50% 0%, rgba(0, 229, 255, 0.05) 0%, transparent 70%);">
      <div class="container" style="max-width: 1400px; padding: 0 20px;">
        <div class="section-head">
          <span class="section-kicker">EVIDENCIA OPERATIVA // FLUJO VISUAL CONTINUO</span>
          <h2 id="gallery-title" class="section-title">GALERÍA <span>EN ACCIÓN</span></h2>
          <p class="section-desc">
            Registro visual dinámico de entrenamientos tácticos, medicina en combate TCCC, tiro defensivo y operaciones especiales. Pasa el cursor para pausar o haz clic en cualquier imagen para verla en pantalla completa.
          </p>
          <div class="title-separator"></div>
        </div>

        <!-- Riel de Imágenes Continuo y Rotativo -->
        <div class="gallery-stream-container">
          <div class="gallery-stream-viewport" id="galleryStreamViewport">
            <!-- Pista 1: Movimiento Continuo Hacia la Izquierda -->
            <div class="gallery-stream-track" id="galleryTrack1">
              <!-- Rendered dynamically by JavaScript -->
            </div>

            <!-- Pista 2: Movimiento Continuo Hacia la Derecha -->
            <div class="gallery-stream-track reverse" id="galleryTrack2">
              <!-- Rendered dynamically by JavaScript -->
            </div>
          </div>

          <!-- Barra de Control HUD de Rotación -->
          <div class="gallery-hud-bar">
            <div class="gallery-hud-status">
              <span class="gallery-hud-pulse" id="galleryPulse"></span>
              <span id="galleryStatusText">ROTACIÓN ACTIVA // AVANCE CONTINUO</span>
            </div>

            <div class="gallery-hud-buttons">
              <button type="button" class="gallery-hud-btn" id="btnTogglePlay" onclick="toggleGalleryAutoScroll()" title="Pausar o Reanudar rotación">
                <span id="playIcon">⏸</span>
                <span id="playText">PAUSAR</span>
              </button>
              <button type="button" class="gallery-hud-btn" onclick="stepGalleryStream(-300)" title="Retroceder">
                <span>◀ ANTERIOR</span>
              </button>
              <button type="button" class="gallery-hud-btn" onclick="stepGalleryStream(300)" title="Avanzar">
                <span>SIGUIENTE ▶</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3.6. VIDEOTECA OPERATIVA TÁCTICA & SPOTLIGHT CINEMA -->
    <section class="section-spacing video-section-wrap" id="videos" aria-labelledby="videos-title">
      <div class="container" style="max-width: 1400px; padding: 0 20px;">
        <div class="section-head">
          <span class="section-kicker">EVIDENCIA AUDIOVISUAL // REGISTRO EN CAMPO</span>
          <h2 id="videos-title" class="section-title">VIDEOTECA <span>TÁCTICA</span></h2>
          <p class="section-desc">
            Visualiza en video nuestras operaciones de entrenamiento en campo: medicina de combate bajo fuego (TCCC), tiro defensivo de alta precisión, rescate y simulación para brigadas.
          </p>
          <div class="title-separator"></div>
        </div>

        <!-- Spotlight Featured Video Hero Card -->
        <div class="video-spotlight-wrap" id="videoSpotlightContainer">
          <!-- Dynamic Spotlight Rendered by JS -->
        </div>

        <!-- Filtros de Videos Tácticos -->
        <div class="calendar-filters" role="tablist" aria-label="Filtros de videos tácticos" style="margin: 30px auto 25px auto; justify-content: center;">
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
    </section>

    """
        content = content[:old_galeria_start] + new_sections_html + content[old_calendario_start:]

    # 6. ENRICH DEFAULT_CONFIG.videos
    old_videos_cfg_start = content.find('videos: [')
    old_videos_cfg_end = content.find('    };\n\n    let HT_CONFIG', old_videos_cfg_start)
    if old_videos_cfg_start != -1 and old_videos_cfg_end != -1:
        new_videos_cfg = """videos: [
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
        },
        {
          id: 'vid-5',
          title: 'Formaciones de Cobertura y Extracción Táctica en Pasillos',
          badge: 'EXTRACCIÓN TÁCTICA',
          duration: '04:15',
          category: 'seguridad',
          videoUrl: 'https://www.youtube.com/embed/ScMzIvxBSi4',
          thumbnail: 'https://images.unsplash.com/photo-1595590424283-b8f17842773f?auto=format&fit=crop&w=1200&q=80',
          desc: 'Desplazamientos coordinados bajo fuego simulado, protección de dignatarios y repliegue seguro en zonas confinadas.'
        },
        {
          id: 'vid-6',
          title: 'Manejo Avanzado de Vía Aérea y Sellado de Tórax en Campo',
          badge: 'TRAUMA CRÍTICO',
          duration: '03:30',
          category: 'primeros-auxilios',
          videoUrl: 'https://www.youtube.com/embed/dQw4w9WgXcQ',
          thumbnail: 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=1200&q=80',
          desc: 'Colocación de sellos torácicos valvulados, cánulas nasofaríngeas y técnicas de descompresión con aguja bajo estándar TCCC.'
        }
      ]
    };"""
        content = content[:old_videos_cfg_start] + new_videos_cfg + content[old_videos_cfg_end + len('    };'):]

    # 7. UPDATE JS IMPLEMENTATION FOR TACTICAL VIDEOS (SPOTLIGHT + GRID + MODAL + CATEGORY LABELS)
    old_js_video_start = content.find('// ========================================================================\n    // TACTICAL VIDEO LIBRARY & CINEMA MODAL')
    if old_js_video_start == -1:
        old_js_video_start = content.find('// ========================================================================\r\n    // TACTICAL VIDEO LIBRARY & CINEMA MODAL')

    old_js_video_end = content.find('function stepGalleryStream(delta)', old_js_video_start)
    if old_js_video_start != -1 and old_js_video_end != -1:
        new_js_video = """// ========================================================================
    // TACTICAL VIDEO LIBRARY, SPOTLIGHT HERO & CINEMA MODAL
    // ========================================================================
    let currentVideoCategory = 'todos';

    function getCategoryLabel(cat) {
      switch(cat) {
        case 'seguridad': return 'Tiro & Seguridad Táctica';
        case 'primeros-auxilios': return 'Medicina Táctico TCCC';
        case 'emergencias': return 'Gestión de Emergencias';
        case 'corporativo': return 'Brigadas Corporativas';
        default: return 'Operaciones Especiales';
      }
    }

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
      const spotlightWrap = document.getElementById('videoSpotlightContainer');
      const grid = document.getElementById('tacticalVideoGrid');

      const videoList = (HT_CONFIG.videos && Array.isArray(HT_CONFIG.videos) && HT_CONFIG.videos.length > 0)
        ? HT_CONFIG.videos
        : DEFAULT_CONFIG.videos;

      const filtered = category === 'todos'
        ? videoList
        : videoList.filter(v => v.category === category);

      if (filtered.length === 0) {
        if (spotlightWrap) spotlightWrap.innerHTML = '';
        if (grid) {
          grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 45px 20px; background: rgba(13,17,26,0.6); border: 1px dashed var(--border-subtle); border-radius: var(--radius-md);">
              <div style="font-size: 32px; margin-bottom: 10px;">🎬</div>
              <div style="font-family: var(--font-display); color: var(--text-white); font-size: 15px; font-weight: 700;">No hay videos registrados en esta categoría táctica.</div>
              <div style="color: var(--text-muted); font-size: 13px; margin-top: 6px;">Selecciona otra categoría en los filtros superiores o explora todos los videos.</div>
            </div>
          `;
        }
        return;
      }

      // 1. RENDER SPOTLIGHT (FEATURED VIDEO HERO)
      const featured = filtered[0];
      if (spotlightWrap && featured) {
        const cleanWa = (HT_CONFIG.whatsApp || '51977331267').replace(/\\D/g, '');
        const waMsg = encodeURIComponent(`Hola Happy Tactical, vi el video destacado "${featured.title}" y quisiera información sobre las capacitaciones en este tema.`);
        
        spotlightWrap.innerHTML = `
          <div class="tactical-video-spotlight tactical-3d-card" data-tilt="true">
            <div class="tactical-3d-glare"></div>
            <div class="spotlight-media-wrap" onclick="openTacticalVideoModal('${featured.id}')" role="button" tabindex="0" aria-label="Reproducir video destacado: ${featured.title}">
              <div class="spotlight-scanline-overlay"></div>
              <div class="spotlight-rec-badge">
                <span class="spotlight-rec-dot"></span> TRANSMISIÓN OPERATIVA 4K
              </div>
              <div class="spotlight-duration-tag">⏱️ ${featured.duration || '04:20'}</div>
              <img src="${featured.thumbnail || 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=1200&q=80'}" alt="${featured.title}" class="spotlight-thumb">
              <div class="spotlight-overlay">
                <div class="spotlight-play-pulse-btn" aria-hidden="true">
                  <span>▶</span>
                </div>
                <div class="spotlight-tap-hint">[ CLIC PARA REPRODUCIR VIDEO ]</div>
              </div>
            </div>
            
            <div class="spotlight-meta">
              <div>
                <div class="spotlight-header-tags">
                  <span class="video-badge-pill">${featured.badge || 'VIDEO DESTACADO'}</span>
                  <span class="spotlight-category-label">${getCategoryLabel(featured.category)}</span>
                </div>
                <h3 class="spotlight-title">${featured.title}</h3>
                <p class="spotlight-desc">${featured.desc || 'Demostración de procedimientos tácticos avanzados impartidos por instructores certificados en campo.'}</p>
              </div>

              <div class="spotlight-action-row">
                <button type="button" class="btn btn-primary btn-sm" onclick="openTacticalVideoModal('${featured.id}')">
                  VER VIDEO COMPLETO 🎬
                </button>
                <a href="https://wa.me/${cleanWa}?text=${waMsg}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="display: inline-flex; align-items: center; gap: 6px;">
                  <span>CONSULTAR POR WHATSAPP</span> 📲
                </a>
              </div>
            </div>
          </div>
        `;
      }

      // 2. RENDER GRID (ALL FILTERED VIDEOS)
      if (grid) {
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
                  <span style="font-family: var(--font-display); font-size: 10.5px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.8px;">${item.category || 'TÁCTICO'}</span>
                </div>
              </div>
            </article>
          `;
        }).join('');
      }

      // Refresh 3D tilt if available
      if (typeof setup3DCardTilt === 'function') {
        setTimeout(setup3DCardTilt, 50);
      }
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
      if (desc) desc.textContent = item.desc || 'Demostración práctica de procedimientos y maniobras operativas en campo.';

      const embedUrl = getEmbedUrl(item.videoUrl);
      if (playerWrap) {
        playerWrap.innerHTML = `
          <div class="video-iframe-wrap">
            <iframe 
              src="${embedUrl}" 
              title="${item.title}" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen>
            </iframe>
          </div>
        `;
      }

      if (waBtn) {
        const cleanWa = (HT_CONFIG.whatsApp || '51977331267').replace(/\\D/g, '');
        const msg = encodeURIComponent(`Hola Happy Tactical, vi el video "${item.title}" y quisiera información sobre las próximas fechas de capacitación.`);
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
        content = content[:old_js_video_start] + new_js_video + content[old_js_video_end:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated index.html successfully! New length: {len(content)}")

    # Also update Happy_Tactical_Home_Mobile_Ordenado_V3-2.html
    backup_path = '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Synchronized Happy_Tactical_Home_Mobile_Ordenado_V3-2.html successfully!")

if __name__ == '__main__':
    update_index()
