import re
import os

def upgrade_all():
    print("Iniciando actualización completa de Interfaz Admin y Cuadro de Carga...")

    # =========================================================================
    # 1. ACTUALIZAR index.html CON EL CUADRO DE CARGA TÁCTICO (PRELOADER)
    # =========================================================================
    index_path = '/Users/stevefernandovelarde/Desktop/web leo/index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    preloader_css = """
    /* ========================================================================
       TACTICAL HUD PRELOADER SCREEN (CUADRO DE CARGA)
       ======================================================================== */
    .tactical-preloader {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 50% 45%, #08101d 0%, #03060c 100%);
      z-index: 99999999;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.6s ease;
    }
    .tactical-preloader.loaded {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }
    .preloader-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 30px;
      max-width: 420px;
      width: 90%;
    }
    .preloader-radar {
      position: relative;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      border: 1.5px solid rgba(0, 229, 255, 0.3);
      box-shadow: 0 0 25px rgba(0, 229, 255, 0.2), inset 0 0 15px rgba(0, 229, 255, 0.1);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }
    .preloader-radar::before {
      content: "";
      position: absolute;
      width: 100%;
      height: 1px;
      background: rgba(0, 229, 255, 0.25);
    }
    .preloader-radar::after {
      content: "";
      position: absolute;
      height: 100%;
      width: 1px;
      background: rgba(0, 229, 255, 0.25);
    }
    .radar-sweep {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      background: conic-gradient(from 0deg, transparent 70%, rgba(0, 229, 255, 0.5) 100%);
      animation: radarSpin 1.6s linear infinite;
    }
    @keyframes radarSpin {
      100% { transform: rotate(360deg); }
    }
    .radar-reticle {
      position: relative;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: 1px dashed rgba(255, 0, 127, 0.5);
      z-index: 2;
    }
    .radar-dot {
      position: absolute;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--neon-pink);
      box-shadow: 0 0 10px var(--neon-pink);
      z-index: 3;
      animation: pulseAnim 1.2s infinite;
    }
    .preloader-title {
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 900;
      color: #fff;
      letter-spacing: 2px;
      margin-bottom: 8px;
    }
    .preloader-title span {
      color: var(--neon-cyan);
    }
    .preloader-telemetry {
      font-family: var(--font-display);
      font-size: 10.5px;
      font-weight: 700;
      color: var(--neon-cyan);
      letter-spacing: 1.2px;
      text-transform: uppercase;
      margin-bottom: 16px;
      min-height: 16px;
    }
    .preloader-bar-wrap {
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
      border: 1px solid rgba(0, 229, 255, 0.2);
    }
    .preloader-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--neon-cyan), var(--neon-pink));
      box-shadow: 0 0 12px var(--neon-cyan);
      transition: width 0.15s ease;
    }
    .preloader-percent {
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 800;
      color: #fff;
      margin-top: 10px;
      letter-spacing: 1px;
    }
    """

    preloader_html = """
  <!-- TACTICAL HUD PRELOADER SCREEN (CUADRO DE CARGA) -->
  <div id="tacticalPreloader" class="tactical-preloader" aria-label="Cargando Happy Tactical">
    <div class="preloader-content">
      <div class="preloader-radar">
        <div class="radar-sweep"></div>
        <div class="radar-reticle"></div>
        <div class="radar-dot"></div>
      </div>
      <div class="preloader-title">HAPPY <span>TACTICAL</span></div>
      <div class="preloader-telemetry" id="preloaderTelemetry">INICIALIZANDO PROTOCOLOS TÁCTICOS...</div>
      <div class="preloader-bar-wrap">
        <div class="preloader-bar" id="preloaderBar"></div>
      </div>
      <div class="preloader-percent" id="preloaderPercent">0%</div>
    </div>
  </div>
"""

    preloader_js = """
    // --- Tactical HUD Preloader Logic ---
    (() => {
      const preloader = document.getElementById('tacticalPreloader');
      const bar = document.getElementById('preloaderBar');
      const percent = document.getElementById('preloaderPercent');
      const telemetry = document.getElementById('preloaderTelemetry');
      if (!preloader) return;

      const messages = [
        'INICIALIZANDO PROTOCOLOS TÁCTICOS...',
        'CONECTANDO RED OPERATIVA SEDE LIMA...',
        'CARGANDO MÓDULOS DE ENTRENAMIENTO...',
        'DESPLEGANDO TELEMETRÍA 3D...',
        'SISTEMA LISTO // ACCESO CONCEDIDO'
      ];

      let currentPct = 0;
      let msgIdx = 0;

      const interval = setInterval(() => {
        currentPct += Math.floor(Math.random() * 14) + 8;
        if (currentPct >= 100) {
          currentPct = 100;
          clearInterval(interval);
          if (bar) bar.style.width = '100%';
          if (percent) percent.textContent = '100%';
          if (telemetry) telemetry.textContent = messages[messages.length - 1];

          setTimeout(() => {
            preloader.classList.add('loaded');
          }, 400);
        } else {
          if (bar) bar.style.width = currentPct + '%';
          if (percent) percent.textContent = currentPct + '%';
          if (msgIdx < messages.length - 1 && currentPct > (msgIdx + 1) * 20) {
            msgIdx++;
            if (telemetry) telemetry.textContent = messages[msgIdx];
          }
        }
      }, 70);

      // Safe fallback: remove preloader after 2.5s maximum
      setTimeout(() => {
        if (!preloader.classList.contains('loaded')) {
          preloader.classList.add('loaded');
        }
      }, 2500);
    })();
"""

    # Inject preloader into index.html
    if 'id="tacticalPreloader"' not in idx_content:
        # Inject CSS
        idx_content = idx_content.replace('</style>', preloader_css + '\n  </style>', 1)
        # Inject HTML right after <body>
        idx_content = re.sub(r'<body[^>]*>', lambda m: m.group(0) + '\n' + preloader_html, idx_content, 1)
        # Inject JS before </script>
        idx_content = idx_content.replace('</script>', preloader_js + '\n  </script>', 1)

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(idx_content)
        print("✓ Preloader injected into index.html")

    # Sincronizar con Happy_Tactical_Home_Mobile_Ordenado_V3-2.html
    backup_path = '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    if os.path.exists(backup_path):
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(idx_content)
        print("✓ Preloader synchronized into Happy_Tactical_Home_Mobile_Ordenado_V3-2.html")

if __name__ == '__main__':
    upgrade_all()
