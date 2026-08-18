import re
import os

def enhance_web():
    path = '/Users/stevefernandovelarde/Desktop/web leo/index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Original index.html length:", len(content))

    # 1. REMOVE .gallery-hud-bar from #galeria HTML
    # Let's find .gallery-hud-bar in the HTML
    hud_bar_start = content.find('<!-- Barra de Control HUD de Rotación -->')
    if hud_bar_start != -1:
        hud_bar_end = content.find('</div>\n        </div>\n      </div>\n    </section>', hud_bar_start)
        if hud_bar_end == -1:
            hud_bar_end = content.find('</div>\r\n        </div>\r\n      </div>\r\n    </section>', hud_bar_start)
        
        if hud_bar_end != -1:
            print("Removing public gallery HUD bar...")
            # We keep the closing tags of gallery-stream-container and gallery-section-wrap
            content = content[:hud_bar_start] + content[hud_bar_end:]

    # 2. UPDATE CSS FOR GALLERY STREAM: FADE MASKS, SMOOTH OVERLAY & HOVER TELEMETRY
    # Let's find .gallery-stream-container CSS
    gallery_css_marker = '/* ========================================================================\n       TACTICAL CONTINUOUS GALLERY & LIGHTBOX (PHOTO STREAM)'
    if gallery_css_marker not in content:
        gallery_css_marker = '/* ========================================================================\r\n       TACTICAL CONTINUOUS GALLERY & LIGHTBOX (PHOTO STREAM)'
    
    if gallery_css_marker in content:
        gallery_css_end = content.find('/* ========================================================================\n       TACTICAL VIDEOTECA OPERATIVA')
        if gallery_css_end == -1:
            gallery_css_end = content.find('/* ========================================================================\r\n       TACTICAL VIDEOTECA OPERATIVA')
        
        enhanced_gallery_css = """/* ========================================================================
       TACTICAL CONTINUOUS GALLERY & LIGHTBOX (PHOTO STREAM)
       ======================================================================== */
    .gallery-section-wrap {
      position: relative;
      overflow: hidden;
      padding-top: 60px;
      padding-bottom: 70px;
    }

    .gallery-stream-container {
      position: relative;
      width: 100%;
      margin: 30px 0 10px 0;
    }

    .gallery-stream-viewport {
      position: relative;
      width: 100%;
      overflow: hidden;
      padding: 15px 0;
      /* Seamless lateral edge fade mask */
      mask-image: linear-gradient(to right, transparent 0%, black 7%, black 93%, transparent 100%);
      -webkit-mask-image: linear-gradient(to right, transparent 0%, black 7%, black 93%, transparent 100%);
    }

    .gallery-stream-track {
      display: flex;
      gap: 22px;
      width: max-content;
      animation: galleryStreamLeft 38s linear infinite;
      will-change: transform;
      padding: 10px 0;
    }

    .gallery-stream-track.reverse {
      animation: galleryStreamRight 42s linear infinite;
      margin-top: 18px;
    }

    .gallery-stream-track:hover,
    .gallery-stream-track.paused {
      animation-play-state: paused;
    }

    @keyframes galleryStreamLeft {
      0% { transform: translate3d(0, 0, 0); }
      100% { transform: translate3d(-50%, 0, 0); }
    }

    @keyframes galleryStreamRight {
      0% { transform: translate3d(-50%, 0, 0); }
      100% { transform: translate3d(0, 0, 0); }
    }

    .gallery-stream-item {
      position: relative;
      flex: 0 0 290px;
      height: 200px;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1.5px solid var(--border-subtle);
      background: rgba(13, 17, 26, 0.85);
      cursor: pointer;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .gallery-stream-item:hover {
      transform: translateY(-8px) scale(1.03);
      border-color: var(--neon-cyan);
      box-shadow: 0 18px 40px rgba(0, 0, 0, 0.9), 0 0 25px rgba(0, 229, 255, 0.35);
      z-index: 5;
    }

    .gallery-stream-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
      filter: brightness(0.88);
    }

    .gallery-stream-item:hover img {
      transform: scale(1.08);
      filter: brightness(1.02);
    }

    .gallery-item-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0, 0, 0, 0.05) 0%, rgba(3, 4, 7, 0.85) 100%);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 12px 14px;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .gallery-stream-item:hover .gallery-item-overlay {
      opacity: 1;
    }

    .gallery-item-badge {
      align-self: flex-start;
      font-family: var(--font-display);
      font-size: 9.5px;
      font-weight: 800;
      color: var(--neon-cyan);
      background: rgba(3, 4, 7, 0.85);
      border: 1px solid var(--border-cyan);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 1px;
      backdrop-filter: blur(4px);
    }

    .gallery-item-title {
      font-family: var(--font-display);
      font-size: 12.5px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
    }

    .gallery-item-zoom-icon {
      color: var(--neon-cyan);
      font-size: 14px;
    }

    @media (max-width: 768px) {
      .gallery-stream-item {
        flex: 0 0 230px;
        height: 160px;
      }
    }

    """
        content = content[:content.find(gallery_css_marker)] + enhanced_gallery_css + content[gallery_css_end:]

    # 3. ADD STATS HUD COUNTER TO HERO SECTION
    # Let's inspect where hero CTA buttons are in index.html
    hero_cta_marker = '<div class="hero-actions">'
    if hero_cta_marker in content:
        # Check if stats-hud already exists
        if 'hero-stats-hud' not in content:
            stats_hud_html = """
          <!-- STATS HUD COUNTER (AUTHORITY METRICS) -->
          <div class="hero-stats-hud">
            <div class="hero-stat-card">
              <div class="hero-stat-number">+15 <span>AÑOS</span></div>
              <div class="hero-stat-label">Experiencia Operativa en Campo</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">+5,000</div>
              <div class="hero-stat-label">Especialistas &amp; Brigadistas</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">100%</div>
              <div class="hero-stat-label">Certificación &amp; Estándar TCCC</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">24/7</div>
              <div class="hero-stat-label">Asistencia &amp; Sede Lima</div>
            </div>
          </div>
"""
            # Find the closing tag of hero-content
            hero_content_end = content.find('</div>\n        <div class="hero-visual-card')
            if hero_content_end == -1:
                hero_content_end = content.find('</div>\r\n        <div class="hero-visual-card')
            
            if hero_content_end != -1:
                content = content[:hero_content_end] + stats_hud_html + content[hero_content_end:]

    # 4. ADD SOCIAL PROOF ACCREDITATIONS STRIP (AFTER HERO)
    social_proof_marker = '<!-- SOCIAL PROOF ACCREDITATIONS -->'
    if social_proof_marker not in content:
        accreditations_html = """
    <!-- SOCIAL PROOF / ACCREDITATIONS & STANDARDS STRIP -->
    <div class="tactical-trust-strip" aria-label="Acreditaciones y Respaldos">
      <div class="container trust-strip-inner">
        <span class="trust-label">[ PROTOCOLOS &amp; RESPALDO OFICIAL ]</span>
        <div class="trust-badges-row">
          <div class="trust-badge-item">
            <span class="trust-icon">🛡️</span>
            <span>ESTÁNDAR TCCC / NAEMT</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">🎯</span>
            <span>TIRO DEFENSIVO &amp; SUCAMEC</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">⚡</span>
            <span>SISTEMA COMANDO SCI</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">🏥</span>
            <span>PRIMEROS AUXILIOS INDECI</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">🏢</span>
            <span>BRIGADAS CORPORATIVAS LEY 29783</span>
          </div>
        </div>
      </div>
    </div>
"""
        # Place right after </section> of hero
        hero_section_end = content.find('</section>\n\n    <!-- 2. NOSOTROS')
        if hero_section_end == -1:
            hero_section_end = content.find('</section>\r\n\r\n    <!-- 2. NOSOTROS')
        if hero_section_end == -1:
            hero_section_end = content.find('</section>\n    <!-- 2. NOSOTROS')

        if hero_section_end != -1:
            content = content[:hero_section_end + len('</section>')] + '\n' + accreditations_html + content[hero_section_end + len('</section>'):]

    # 5. ADD CSS FOR STATS HUD AND TRUST STRIP
    additional_css = """
    /* ========================================================================
       HERO STATS HUD & SOCIAL PROOF TRUST STRIP
       ======================================================================== */
    .hero-stats-hud {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 36px;
      padding-top: 24px;
      border-top: 1px solid rgba(0, 229, 255, 0.15);
    }

    .hero-stat-card {
      background: rgba(13, 17, 26, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      text-align: left;
      position: relative;
      transition: all 0.3s ease;
    }

    .hero-stat-card:hover {
      border-color: var(--neon-cyan);
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 229, 255, 0.15);
    }

    .hero-stat-number {
      font-family: var(--font-display);
      font-size: clamp(20px, 2.5vw, 26px);
      font-weight: 800;
      color: #fff;
      line-height: 1.1;
      background: linear-gradient(135deg, #00e5ff 0%, #ffffff 70%, #ff007f 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-stat-number span {
      font-size: 13px;
      color: var(--neon-cyan);
      -webkit-text-fill-color: var(--neon-cyan);
    }

    .hero-stat-label {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 4px;
      line-height: 1.3;
      font-weight: 500;
    }

    .tactical-trust-strip {
      background: rgba(7, 9, 15, 0.95);
      border-top: 1px solid rgba(0, 229, 255, 0.12);
      border-bottom: 1px solid rgba(0, 229, 255, 0.12);
      padding: 18px 0;
      position: relative;
      z-index: 5;
    }

    .trust-strip-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }

    .trust-label {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      color: var(--neon-cyan);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }

    .trust-badges-row {
      display: flex;
      align-items: center;
      gap: 22px;
      flex-wrap: wrap;
    }

    .trust-badge-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: 0.5px;
      transition: color 0.2s ease;
    }

    .trust-badge-item:hover {
      color: var(--neon-cyan);
    }

    .trust-icon {
      font-size: 14px;
    }

    @media (max-width: 900px) {
      .hero-stats-hud {
        grid-template-columns: repeat(2, 1fr);
      }
      .trust-strip-inner {
        flex-direction: column;
        align-items: flex-start;
      }
      .trust-badges-row {
        gap: 14px;
      }
    }
    """

    # Inject additional CSS before </style>
    style_end = content.find('</style>')
    if style_end != -1 and 'hero-stats-hud' not in content[:style_end]:
        content = content[:style_end] + additional_css + '\n  ' + content[style_end:]

    # 6. ENHANCE TITLES AND GRADIENT SHINE
    # Let's ensure .section-title span has a breathtaking vibrant gradient
    old_title_span_css = '.section-title span {'
    if old_title_span_css in content:
        content = content.replace(
            '.section-title span {\n      color: var(--neon-cyan);\n    }',
            '.section-title span {\n      background: linear-gradient(135deg, #00e5ff 0%, #ffffff 40%, #ff007f 100%);\n      -webkit-background-clip: text;\n      -webkit-text-fill-color: transparent;\n      text-shadow: 0 0 35px rgba(0, 229, 255, 0.4);\n    }'
        )

    # 7. WRITE BACK TO index.html and Happy_Tactical_Home_Mobile_Ordenado_V3-2.html
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated index.html successfully! New length: {len(content)}")

    backup_path = '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Synchronized Happy_Tactical_Home_Mobile_Ordenado_V3-2.html successfully!")

if __name__ == '__main__':
    enhance_web()
