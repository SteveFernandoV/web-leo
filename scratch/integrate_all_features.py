import re
import os
import sys

def build_integrated_html(content):
    print("Building integrated tactical web experience...")

    # =========================================================================
    # 1. CSS STYLES TO INJECT BEFORE </style>
    # =========================================================================
    all_new_css = """
    /* ========================================================================
       HERO STATS HUD & SOCIAL PROOF TRUST STRIP
       ======================================================================== */
    .hero-stats-hud {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 36px;
      padding: 20px 24px;
      background: rgba(10, 14, 20, 0.75);
      border: 1px solid rgba(0, 229, 255, 0.2);
      border-radius: 12px;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(0, 229, 255, 0.04);
      position: relative;
    }
    .hero-stats-hud::before {
      content: '';
      position: absolute;
      top: 0;
      left: 15%;
      right: 15%;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
    }
    .hero-stat-card {
      text-align: center;
      position: relative;
    }
    .hero-stat-card:not(:last-child)::after {
      content: '';
      position: absolute;
      right: -8px;
      top: 15%;
      height: 70%;
      width: 1px;
      background: rgba(255, 255, 255, 0.08);
    }
    .hero-stat-number {
      font-family: var(--font-display);
      font-size: 28px;
      font-weight: 800;
      color: #fff;
      line-height: 1.1;
      letter-spacing: -0.5px;
      text-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
    }
    .hero-stat-number span {
      color: var(--neon-cyan);
      font-size: 18px;
    }
    .hero-stat-label {
      font-family: var(--font-sans);
      font-size: 11.5px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-top: 4px;
      font-weight: 600;
    }

    /* SOCIAL PROOF / ACCREDITATIONS & STANDARDS STRIP */
    .tactical-trust-strip {
      background: linear-gradient(180deg, rgba(8, 12, 18, 0.95) 0%, rgba(5, 7, 10, 0.98) 100%);
      border-top: 1px solid rgba(0, 229, 255, 0.15);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding: 16px 0;
      position: relative;
      z-index: 15;
    }
    .trust-strip-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }
    .trust-label-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: var(--neon-cyan);
      text-transform: uppercase;
      padding: 5px 12px;
      background: rgba(0, 229, 255, 0.08);
      border: 1px solid rgba(0, 229, 255, 0.3);
      border-radius: 4px;
    }
    .trust-badges-row {
      display: flex;
      align-items: center;
      gap: 28px;
      flex-wrap: wrap;
    }
    .trust-badge-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-main);
      letter-spacing: 0.6px;
      text-transform: uppercase;
      opacity: 0.85;
      transition: opacity 0.25s ease, color 0.25s ease;
    }
    .trust-badge-item:hover {
      opacity: 1;
      color: #fff;
    }
    .trust-icon {
      font-size: 14px;
      filter: drop-shadow(0 0 6px var(--neon-cyan));
    }

    /* ========================================================================
       TACTICAL CONTINUOUS GALLERY & LIGHTBOX (PHOTO STREAM)
       ======================================================================== */
    .gallery-section-wrap {
      position: relative;
      overflow: hidden;
      background: radial-gradient(circle at 50% 0%, rgba(0, 229, 255, 0.04) 0%, transparent 70%);
    }
    .gallery-stream-container {
      position: relative;
      margin-top: 35px;
      border: 1px solid rgba(0, 229, 255, 0.2);
      border-radius: 16px;
      background: rgba(6, 9, 14, 0.8);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      padding: 24px 0 20px 0;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.7);
    }
    .gallery-stream-viewport {
      display: flex;
      flex-direction: column;
      gap: 16px;
      overflow: hidden;
      position: relative;
      mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent);
      -webkit-mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent);
    }
    .gallery-stream-track {
      display: flex;
      gap: 16px;
      width: max-content;
      animation: marqueeLeft 42s linear infinite;
      will-change: transform;
    }
    .gallery-stream-track.reverse {
      animation: marqueeRight 45s linear infinite;
    }
    .gallery-stream-track.paused {
      animation-play-state: paused !important;
    }
    .gallery-stream-container:hover .gallery-stream-track {
      animation-play-state: paused;
    }
    @keyframes marqueeLeft {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
    @keyframes marqueeRight {
      0% { transform: translateX(-50%); }
      100% { transform: translateX(0); }
    }
    .gallery-stream-item {
      flex: 0 0 320px;
      height: 210px;
      border-radius: 10px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: #0d121a;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.35s ease, box-shadow 0.35s ease;
    }
    .gallery-stream-item:hover {
      transform: translateY(-4px) scale(1.02);
      border-color: var(--neon-cyan);
      box-shadow: 0 12px 28px rgba(0, 229, 255, 0.25), 0 0 15px rgba(0, 229, 255, 0.15);
      z-index: 10;
    }
    .gallery-stream-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
      display: block;
    }
    .gallery-stream-item:hover .gallery-stream-img {
      transform: scale(1.08);
    }
    .gallery-stream-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 12px;
      opacity: 0.9;
      transition: opacity 0.3s ease;
    }
    .gallery-stream-item:hover .gallery-stream-overlay {
      opacity: 1;
    }
    .gallery-badge {
      align-self: flex-start;
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      color: #fff;
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid var(--neon-cyan);
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .gallery-caption {
      font-family: var(--font-display);
      font-size: 12px;
      font-weight: 700;
      color: #fff;
      letter-spacing: 0.5px;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9);
      margin: 0;
    }
    .gallery-subcaption {
      font-family: var(--font-sans);
      font-size: 11px;
      color: var(--neon-cyan);
      margin-top: 2px;
    }
    .gallery-telemetry-tag {
      position: absolute;
      top: 10px;
      right: 10px;
      font-family: var(--font-mono, monospace);
      font-size: 9.5px;
      color: var(--neon-cyan);
      background: rgba(0, 0, 0, 0.65);
      border: 1px solid rgba(0, 229, 255, 0.3);
      border-radius: 3px;
      padding: 1px 6px;
      letter-spacing: 0.5px;
      opacity: 0;
      transform: translateY(-4px);
      transition: opacity 0.25s ease, transform 0.25s ease;
    }
    .gallery-stream-item:hover .gallery-telemetry-tag {
      opacity: 1;
      transform: translateY(0);
    }
    .gallery-hud-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 24px 0 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      margin-top: 16px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .gallery-hud-status {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 600;
      color: var(--text-dim);
      letter-spacing: 1px;
    }
    .gallery-hud-pulse {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--neon-cyan);
      box-shadow: 0 0 8px var(--neon-cyan);
      animation: pulseAnim 2s infinite;
    }
    .gallery-hud-buttons {
      display: flex;
      gap: 10px;
    }
    .gallery-hud-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: 6px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .gallery-hud-btn:hover {
      background: rgba(0, 229, 255, 0.15);
      border-color: var(--neon-cyan);
      color: #fff;
    }

    /* LIGHTBOX MODAL FOR TACTICAL PHOTOS */
    .tactical-lightbox-modal {
      border: 1px solid rgba(0, 229, 255, 0.4);
      border-radius: 16px;
      background: rgba(8, 12, 18, 0.96);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      color: #fff;
      max-width: 900px;
      width: 92vw;
      padding: 0;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 229, 255, 0.15);
      overflow: hidden;
      margin: auto;
    }
    .tactical-lightbox-modal::backdrop {
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .lightbox-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(0, 0, 0, 0.4);
    }
    .lightbox-badge {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--neon-cyan);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }
    .lightbox-img-wrap {
      width: 100%;
      max-height: 60vh;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }
    .lightbox-img-wrap img {
      max-width: 100%;
      max-height: 60vh;
      object-fit: contain;
      display: block;
    }
    .lightbox-footer {
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
    }
    .lightbox-caption {
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      color: #fff;
    }
    .lightbox-desc {
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: var(--text-dim);
      margin-top: 3px;
    }

    /* ========================================================================
       TACTICAL VIDEOTECA OPERATIVA & CINEMA SPOTLIGHT (VIDEO ZONE)
       ======================================================================== */
    .video-section-wrap {
      position: relative;
      background: radial-gradient(circle at 50% 10%, rgba(255, 179, 0, 0.03) 0%, transparent 60%);
    }
    .video-spotlight-wrap {
      margin-top: 35px;
    }
    .tactical-video-spotlight {
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: 28px;
      background: linear-gradient(135deg, rgba(14, 20, 30, 0.95) 0%, rgba(8, 12, 18, 0.98) 100%);
      border: 1px solid rgba(0, 229, 255, 0.3);
      border-radius: 16px;
      overflow: hidden;
      padding: 24px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(0, 229, 255, 0.08);
      position: relative;
    }
    .spotlight-media-wrap {
      position: relative;
      border-radius: 12px;
      overflow: hidden;
      aspect-ratio: 16 / 9;
      background: #000;
      cursor: pointer;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .spotlight-thumb {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }
    .spotlight-media-wrap:hover .spotlight-thumb {
      transform: scale(1.05);
    }
    .spotlight-scanline-overlay {
      position: absolute;
      inset: 0;
      background: repeating-linear-gradient(0deg, rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15) 1px, transparent 1px, transparent 2px);
      pointer-events: none;
      z-index: 2;
    }
    .spotlight-rec-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-display);
      font-size: 10.5px;
      font-weight: 700;
      color: #fff;
      background: rgba(0, 0, 0, 0.75);
      border: 1px solid rgba(255, 59, 48, 0.6);
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 1px;
      z-index: 3;
    }
    .spotlight-rec-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #ff3b30;
      box-shadow: 0 0 8px #ff3b30;
      animation: pulseAnim 1.5s infinite;
    }
    .spotlight-duration-tag {
      position: absolute;
      bottom: 14px;
      right: 14px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      background: rgba(0, 0, 0, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 3px 8px;
      border-radius: 4px;
      z-index: 3;
    }
    .spotlight-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.35);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      z-index: 3;
      transition: background 0.3s ease;
    }
    .spotlight-media-wrap:hover .spotlight-overlay {
      background: rgba(0, 0, 0, 0.15);
    }
    .spotlight-play-pulse-btn {
      width: 68px;
      height: 68px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.2);
      border: 2px solid var(--neon-cyan);
      box-shadow: 0 0 25px rgba(0, 229, 255, 0.5), inset 0 0 15px rgba(0, 229, 255, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 24px;
      padding-left: 4px;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
    }
    .spotlight-media-wrap:hover .spotlight-play-pulse-btn {
      transform: scale(1.15);
      box-shadow: 0 0 35px rgba(0, 229, 255, 0.8), inset 0 0 20px rgba(0, 229, 255, 0.5);
    }
    .spotlight-tap-hint {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      letter-spacing: 1.5px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.9);
      background: rgba(0, 0, 0, 0.6);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .spotlight-meta {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .spotlight-header-tags {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }
    .spotlight-category-label {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--neon-amber);
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .spotlight-title {
      font-family: var(--font-display);
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      line-height: 1.25;
      margin-bottom: 12px;
    }
    .spotlight-desc {
      font-family: var(--font-sans);
      font-size: 14px;
      color: var(--text-dim);
      line-height: 1.6;
      margin-bottom: 20px;
    }
    .spotlight-action-row {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    /* TACTICAL VIDEOS GRID */
    .tactical-video-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
      gap: 22px;
      margin-top: 25px;
    }
    .tactical-video-card {
      background: rgba(12, 17, 24, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.35s ease, box-shadow 0.35s ease;
      cursor: pointer;
      position: relative;
    }
    .tactical-video-card:hover {
      transform: translateY(-5px);
      border-color: var(--neon-cyan);
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 229, 255, 0.18);
    }
    .video-thumb-container {
      position: relative;
      width: 100%;
      height: 180px;
      background: #000;
      overflow: hidden;
    }
    .video-thumb-container img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
      display: block;
    }
    .tactical-video-card:hover .video-thumb-container img {
      transform: scale(1.06);
    }
    .video-card-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.3s ease;
    }
    .tactical-video-card:hover .video-card-overlay {
      background: rgba(0, 0, 0, 0.15);
    }
    .video-play-pulse-btn {
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: rgba(0, 229, 255, 0.25);
      border: 1.5px solid var(--neon-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 16px;
      padding-left: 2px;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.5);
      transition: transform 0.3s ease, background 0.3s ease;
    }
    .tactical-video-card:hover .video-play-pulse-btn {
      transform: scale(1.15);
      background: rgba(0, 229, 255, 0.4);
    }
    .video-duration-pill {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.8);
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      color: #fff;
      padding: 2px 6px;
      border-radius: 3px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .video-badge-pill {
      position: absolute;
      top: 8px;
      left: 8px;
      background: rgba(0, 0, 0, 0.75);
      border: 1px solid var(--neon-cyan);
      color: var(--neon-cyan);
      font-family: var(--font-display);
      font-size: 9.5px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }
    .video-card-content {
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
    }
    .video-card-title {
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      color: #fff;
      line-height: 1.35;
      margin-bottom: 6px;
      transition: color 0.25s ease;
    }
    .tactical-video-card:hover .video-card-title {
      color: var(--neon-cyan);
    }
    .video-card-desc {
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: var(--text-dim);
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
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 10px;
      margin-top: auto;
    }
    .video-watch-link {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--neon-cyan);
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }

    /* TACTICAL VIDEO CINEMA MODAL */
    .tactical-video-modal {
      border: 1px solid rgba(0, 229, 255, 0.4);
      border-radius: 16px;
      background: rgba(6, 10, 16, 0.98);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      color: #fff;
      max-width: 960px;
      width: 94vw;
      padding: 0;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.95), 0 0 50px rgba(0, 229, 255, 0.2);
      overflow: hidden;
      margin: auto;
    }
    .tactical-video-modal::backdrop {
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }
    .video-modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 22px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(0, 0, 0, 0.5);
    }
    .video-modal-badge {
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--neon-cyan);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }
    .video-player-container {
      width: 100%;
      background: #000;
      position: relative;
    }
    .video-iframe-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
    }
    .video-iframe-wrap iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }
    .video-modal-footer {
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
    }
    .video-modal-title {
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      color: #fff;
    }
    .video-modal-desc {
      font-family: var(--font-sans);
      font-size: 13px;
      color: var(--text-dim);
      margin-top: 4px;
    }

    /* RESPONSIVE MEDIA QUERIES */
    @media (max-width: 992px) {
      .hero-stats-hud {
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
      }
      .hero-stat-card:nth-child(2)::after {
        display: none;
      }
      .tactical-video-spotlight {
        grid-template-columns: 1fr;
      }
      .spotlight-title {
        font-size: 20px;
      }
    }
    @media (max-width: 768px) {
      .hero-stats-hud {
        grid-template-columns: 1fr 1fr;
        padding: 16px;
      }
      .hero-stat-number {
        font-size: 22px;
      }
      .trust-strip-inner {
        flex-direction: column;
        align-items: flex-start;
      }
      .trust-badges-row {
        gap: 14px;
      }
      .gallery-stream-item {
        flex: 0 0 240px;
        height: 160px;
      }
      .tactical-video-grid {
        grid-template-columns: 1fr;
      }
      .video-thumb-container {
        height: 190px;
      }
    }
    """

    # 1. Inyectar CSS antes de </style>
    if '</style>' in content:
        content = content.replace('</style>', all_new_css + '\n  </style>', 1)
        print("✓ CSS injected successfully")
    else:
        print("⚠ Could not find </style>")

    # =========================================================================
    # 2. UPDATE NAV LINKS (DESKTOP)
    # =========================================================================
    old_nav_cursos = '<li><a href="#cursos" class="nav-link">CURSOS</a></li>'
    new_nav_cursos = """<li><a href="#cursos" class="nav-link">CURSOS</a></li>
          <li><a href="#galeria" class="nav-link">GALERÍA</a></li>
          <li><a href="#videos" class="nav-link">VIDEOS</a></li>"""
    if old_nav_cursos in content:
        content = content.replace(old_nav_cursos, new_nav_cursos, 1)
        print("✓ Desktop Nav links updated with GALERÍA and VIDEOS")

    # =========================================================================
    # 3. UPDATE MOBILE DRAWER LINKS
    # =========================================================================
    old_drawer_cursos = '<a href="#cursos" class="nav-link mobile-link">CURSOS &amp; PROGRAMAS</a>'
    new_drawer_cursos = """<a href="#cursos" class="nav-link mobile-link">CURSOS &amp; PROGRAMAS</a>
    <a href="#galeria" class="nav-link mobile-link">GALERÍA OPERATIVA</a>
    <a href="#videos" class="nav-link mobile-link">VIDEOTECA TÁCTICA</a>"""
    if old_drawer_cursos in content:
        content = content.replace(old_drawer_cursos, new_drawer_cursos, 1)
        print("✓ Mobile drawer links updated")

    # =========================================================================
    # 4. HERO STATS HUD & SOCIAL PROOF TRUST STRIP
    # =========================================================================
    hero_stats_html = """
          <!-- STATS HUD COUNTER (AUTHORITY METRICS) -->
          <div class="hero-stats-hud">
            <div class="hero-stat-card">
              <div class="hero-stat-number">+15 <span>AÑOS</span></div>
              <div class="hero-stat-label">Trayectoria Operativa</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">+1,200</div>
              <div class="hero-stat-label">Efectivos Graduados</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">100%</div>
              <div class="hero-stat-label">Instructores Certificados</div>
            </div>
            <div class="hero-stat-card">
              <div class="hero-stat-number">24/7</div>
              <div class="hero-stat-label">Asistencia &amp; Sede Lima</div>
            </div>
          </div>"""

    old_hero_features = '<div class="hero-features-list">'
    # Let's insert hero stats right after closing tag of hero-features-list
    features_end_idx = content.find('</div>\n        </div>\n      </div>\n    </section>\n\n    <!-- 2. NOSOTROS')
    if features_end_idx == -1:
        features_end_idx = content.find('</div>\r\n        </div>\r\n      </div>\r\n    </section>\r\n\r\n    <!-- 2. NOSOTROS')
    
    trust_strip_html = """
    <!-- SOCIAL PROOF / ACCREDITATIONS & STANDARDS STRIP -->
    <div class="tactical-trust-strip" aria-label="Acreditaciones y Respaldos">
      <div class="container trust-strip-inner">
        <span class="trust-label-badge">
          <span>★</span> ESTÁNDAR OPERATIVO DE ALTO NIVEL
        </span>
        <div class="trust-badges-row">
          <div class="trust-badge-item">
            <span class="trust-icon">🛡️</span>
            <span>ESTÁNDAR MILITAR &amp; POLICIAL INTERNACIONAL</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">🩺</span>
            <span>PROTOCOLOS CERTIFICADOS TCCC CO-TECC</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">⚖️</span>
            <span>CONFORMIDAD SUCAMEC &amp; MININTER</span>
          </div>
          <div class="trust-badge-item">
            <span class="trust-icon">🏢</span>
            <span>BRIGADAS CORPORATIVAS LEY 29783</span>
          </div>
        </div>
      </div>
    </div>
"""

    old_hero_end = '</section>\n\n    <!-- 2. NOSOTROS / IDENTIDAD WITH 3D CARD -->'
    if old_hero_end not in content:
        old_hero_end = '</section>\r\n\r\n    <!-- 2. NOSOTROS / IDENTIDAD WITH 3D CARD -->'

    # Add stats HUD before closing of hero-content
    old_hero_features_block = """          <div class="hero-features-list">
            <div class="hero-feat-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              <span>Certificación Oficial</span>
            </div>
            <div class="hero-feat-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
              <span>100% Práctica Operativa</span>
            </div>
            <div class="hero-feat-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              <span>Instructores Calificados</span>
            </div>
          </div>"""

    if old_hero_features_block in content:
        content = content.replace(old_hero_features_block, old_hero_features_block + hero_stats_html, 1)
        print("✓ Hero Stats HUD inserted")
    
    if old_hero_end in content:
        content = content.replace(old_hero_end, '</section>\n' + trust_strip_html + '\n    <!-- 2. NOSOTROS / IDENTIDAD WITH 3D CARD -->', 1)
        print("✓ Tactical Trust Strip inserted")

    # =========================================================================
    # 5. INSERT SECTIONS 3.5 (GALERÍA) AND 3.6 (VIDEOTECA)
    # =========================================================================
    gallery_and_video_html = """
    <!-- 3.5. GALERÍA TÁCTICA INTERACTIVA CONTINUA -->
    <section class="section-spacing gallery-section-wrap" id="galeria" aria-labelledby="gallery-title">
      <div class="container" style="max-width: 1400px; padding: 0 20px;">
        <div class="section-head">
          <span class="section-kicker">EVIDENCIA OPERATIVA // FLUJO VISUAL CONTINUO</span>
          <h2 id="gallery-title" class="section-title">GALERÍA <span>EN ACCIÓN</span></h2>
          <p class="section-desc">
            Registro visual dinámico de entrenamientos tácticos, medicina en combate TCCC, tiro defensivo y operaciones especiales. Haz clic en cualquier imagen para verla en pantalla completa o consultar sobre el entrenamiento.
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

    old_cursos_calendario_trans = '</section>\n\n    <!-- 4. CALENDARIO -->'
    if old_cursos_calendario_trans not in content:
        old_cursos_calendario_trans = '</section>\r\n\r\n    <!-- 4. CALENDARIO -->'
    
    if old_cursos_calendario_trans in content:
        content = content.replace(old_cursos_calendario_trans, '</section>\n' + gallery_and_video_html + '\n    <!-- 4. CALENDARIO -->', 1)
        print("✓ Galería and Videoteca sections inserted between Cursos and Calendario")
    else:
        print("⚠ Could not find transition anchor between Cursos and Calendario")

    # =========================================================================
    # 6. INSERT MODALS (LIGHTBOX & CINEMA VIDEO)
    # =========================================================================
    modals_html = """
  <!-- TACTICAL IMAGE LIGHTBOX MODAL -->
  <dialog class="tactical-lightbox-modal" id="tacticalLightboxModal" aria-labelledby="lightboxTitle">
    <div class="lightbox-header">
      <span class="lightbox-badge" id="lightboxBadge">[ EVIDENCIA FOTOGRÁFICA TÁCTICA ]</span>
      <button type="button" class="modal-close-btn" onclick="closeTacticalLightbox()" aria-label="Cerrar modal de imagen">
        &times;
      </button>
    </div>
    <div class="lightbox-img-wrap">
      <img id="lightboxImg" src="" alt="Fotografía Táctica Operativa">
    </div>
    <div class="lightbox-footer">
      <div>
        <div class="lightbox-caption" id="lightboxTitle">Entrenamiento Táctico Operativo</div>
        <div class="lightbox-desc" id="lightboxDesc">Registro en campo de maniobras e instrucción especializada.</div>
      </div>
      <a href="https://wa.me/51977331267" id="lightboxWhatsAppBtn" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="white-space: nowrap;">
        CONSULTAR POR ESTE CURSO 📲
      </a>
    </div>
  </dialog>

  <!-- TACTICAL VIDEO CINEMA MODAL -->
  <dialog class="tactical-video-modal" id="tacticalVideoModal" aria-labelledby="videoModalTitle">
    <div class="video-modal-header">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span class="video-modal-badge" id="videoModalBadge">[ TCCC EN COMBATE ]</span>
      </div>
      <button type="button" class="modal-close-btn" onclick="closeTacticalVideoModal()" aria-label="Cerrar reproductor de video">
        &times;
      </button>
    </div>
    <div class="video-player-container">
      <div class="video-iframe-wrap" id="videoPlayerContainer">
        <!-- Iframe injected dynamically by JS -->
      </div>
    </div>
    <div class="video-modal-footer">
      <div>
        <div class="video-modal-title" id="videoModalTitle">Demostración Práctica Táctica</div>
        <div class="video-modal-desc" id="videoModalDesc">Procedimientos operativos avanzados impartidos por instructores certificados.</div>
      </div>
      <a href="https://wa.me/51977331267" id="videoWhatsAppBtn" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="white-space: nowrap;">
        CONSULTAR POR WHATSAPP 📲
      </a>
    </div>
  </dialog>
"""

    old_modal_anchor = '<dialog class="tactical-modal" id="courseDetailModal">'
    if old_modal_anchor in content:
        content = content.replace(old_modal_anchor, modals_html + '\n  ' + old_modal_anchor, 1)
        print("✓ Lightbox and Video Cinema modals inserted")

    # =========================================================================
    # 7. UPDATE DEFAULT_CONFIG (ADD GALLERY & VIDEOS DATA)
    # =========================================================================
    old_config_end = """          startTime: '09:00',
          endTime: '13:00'
        }
      ]
    };"""

    new_config_end = """          startTime: '09:00',
          endTime: '13:00'
        }
      ],
      gallerySpeed: '1x',
      galleryAutoScroll: true,
      galleryImages: [
        {
          id: 'gal-1',
          title: 'Procedimiento de Control de Hemorragias TCCC',
          badge: 'TCCC MEDICINE',
          location: 'Lima - Sede Operativa',
          url: 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80',
          desc: 'Aplicación correcta de torniquetes CAT Gen 7 y empaquetamiento de heridas bajo protocolo MARCH.'
        },
        {
          id: 'gal-2',
          title: 'Entrenamiento de Tiro Táctico Defensivo',
          badge: 'POLÍGONO SUR',
          location: 'Polígono de Tiro Especializado',
          url: 'https://images.unsplash.com/photo-1595590424283-b8f17842773f?auto=format&fit=crop&w=800&q=80',
          desc: 'Técnicas dinámicas de tiro, transiciones de arma primaria a secundaria y resolución de encasquillamientos.'
        },
        {
          id: 'gal-3',
          title: 'Extracción Rápida de Heridos en Zona Bajo Fuego',
          badge: 'EVACUACIÓN CARE',
          location: 'Base de Maniobras',
          url: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=800&q=80',
          desc: 'Arrastre táctico, uso de camillas plegables Sked y aseguramiento del perímetro durante la atención.'
        },
        {
          id: 'gal-4',
          title: 'Formación de Brigadas Industriales y Rescate',
          badge: 'BRIGADAS LEY 29783',
          location: 'Instalaciones Corporativas',
          url: 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=800&q=80',
          desc: 'Capacitación para brigadistas empresariales en control de amagos de incendio y evacuación de emergencia.'
        },
        {
          id: 'gal-5',
          title: 'Rescate en Estructuras y Espacios Confinados',
          badge: 'GESTIÓN DE RESCATE',
          location: 'Campo de Simulación',
          url: 'https://images.unsplash.com/photo-1582139329536-e7284fece509?auto=format&fit=crop&w=800&q=80',
          desc: 'Técnicas de estabilización estructural, empaquetamiento y transporte seguro en terrenos hostiles.'
        },
        {
          id: 'gal-6',
          title: 'Manejo Avanzado de Vía Aérea y Triage Táctico',
          badge: 'PROTOCOLO MARCH',
          location: 'Módulo de Trauma',
          url: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=800&q=80',
          desc: 'Colocación de cánulas, descompresión torácica con aguja y clasificación masiva START/SALT.'
        },
        {
          id: 'gal-7',
          title: 'Tácticas de Cobertura y Despliegue en Escuadra',
          badge: 'SEGURIDAD INTEGRAL',
          location: 'Polígono Táctico',
          url: 'https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=800&q=80',
          desc: 'Desplazamiento táctico coordinado, comunicación operativa y cobertura cruzada para personal de protección.'
        },
        {
          id: 'gal-8',
          title: 'Simulacro de Desastres y Múltiples Víctimas',
          badge: 'SIMULACRO 360°',
          location: 'Centro de Entrenamiento',
          url: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=800&q=80',
          desc: 'Evaluación de toma de decisiones bajo estrés, liderazgo de brigada y comando de incidentes.'
        }
      ],
      videos: [
        {
          id: 'vid-1',
          title: 'Procedimientos de Medicina Táctica TCCC en Zona Hostil',
          badge: 'TCCC EN COMBATE',
          duration: '04:20',
          category: 'primeros-auxilios',
          thumbnail: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=1200&q=80',
          videoUrl: 'https://www.youtube.com/watch?v=ScMzIvxBSi4',
          desc: 'Demostración práctica de colocación de torniquete CAT bajo fuego simulado, hemostáticos y evacuación rápida en zona de amenaza directa.'
        },
        {
          id: 'vid-2',
          title: 'Entrenamiento de Tiro Táctico y Transición Rápida',
          badge: 'TIRO DE PRECISIÓN',
          duration: '03:45',
          category: 'seguridad',
          thumbnail: 'https://images.unsplash.com/photo-1595590424283-b8f17842773f?auto=format&fit=crop&w=800&q=80',
          videoUrl: 'https://www.youtube.com/watch?v=kJQP7kiw5Fk',
          desc: 'Técnicas avanzadas de desenfunde, recargas tácticas y tiro defensivo dinámico para escoltas y fuerzas de seguridad.'
        },
        {
          id: 'vid-3',
          title: 'Simulación de Rescate y Evacuación en Estructuras Colapsadas',
          badge: 'RESCATE URBANO',
          duration: '05:10',
          category: 'emergencias',
          thumbnail: 'https://images.unsplash.com/photo-1582139329536-e7284fece509?auto=format&fit=crop&w=800&q=80',
          videoUrl: 'https://www.youtube.com/watch?v=3JZ_D3ELwOQ',
          desc: 'Ejercicios prácticos de búsqueda, extracción y estabilización de pacientes en situaciones críticas de catástrofe.'
        },
        {
          id: 'vid-4',
          title: 'Capacitación de Brigadas de Emergencia Corporativa (Ley 29783)',
          badge: 'BRIGADAS EMPRESAS',
          duration: '03:15',
          category: 'corporativo',
          thumbnail: 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=800&q=80',
          videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
          desc: 'Formación integral de brigadas de lucha contra incendios, primeros auxilios y evacuación en plantas industriales y centros corporativos.'
        },
        {
          id: 'vid-5',
          title: 'Manejo Avanzado de Vía Aérea y Traumatismos Torácicos',
          badge: 'TCCC AVANZADO',
          duration: '06:00',
          category: 'primeros-auxilios',
          thumbnail: 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80',
          videoUrl: 'https://www.youtube.com/watch?v=ScMzIvxBSi4',
          desc: 'Colocación de sellos torácicos valvulados, cánulas nasofaríngeas y técnicas de descompresión con aguja bajo estándar TCCC.'
        }
      ]
    };"""

    if old_config_end in content:
        content = content.replace(old_config_end, new_config_end, 1)
        print("✓ DEFAULT_CONFIG enriched with galleryImages and videos")
    else:
        print("⚠ Could not find DEFAULT_CONFIG end anchor")

    # =========================================================================
    # 8. JAVASCRIPT FUNCTIONS (GALLERY STREAM + LIGHTBOX + VIDEOS + CINEMA MODAL)
    # =========================================================================
    new_js_logic = """
    // ========================================================================
    // TACTICAL PHOTO STREAM GALLERY & LIGHTBOX
    // ========================================================================
    let isGalleryPaused = false;

    function renderGalleryStream() {
      const track1 = document.getElementById('galleryTrack1');
      const track2 = document.getElementById('galleryTrack2');
      if (!track1 || !track2) return;

      const imgList = (HT_CONFIG.galleryImages && Array.isArray(HT_CONFIG.galleryImages) && HT_CONFIG.galleryImages.length > 0)
        ? HT_CONFIG.galleryImages
        : DEFAULT_CONFIG.galleryImages;

      // Duplicate list to achieve continuous seamless loop
      const doubled = [...imgList, ...imgList];

      const makeCardHtml = (item, idx) => `
        <div class="gallery-stream-item" onclick="openTacticalLightbox('${item.id || 'gal-' + idx}')" role="button" tabindex="0" aria-label="Ver imagen ampliada: ${item.title}">
          <span class="gallery-telemetry-tag">CAM-0${(idx % 8) + 1} // HD</span>
          <img src="${item.url}" alt="${item.title}" class="gallery-stream-img" loading="lazy">
          <div class="gallery-stream-overlay">
            <span class="gallery-badge">${item.badge || 'TÁCTICO'}</span>
            <div>
              <p class="gallery-caption">${item.title}</p>
              <p class="gallery-subcaption">${item.location || 'Happy Tactical'}</p>
            </div>
          </div>
        </div>
      `;

      track1.innerHTML = doubled.map((item, i) => makeCardHtml(item, i)).join('');
      // Track 2 in reverse order for dynamic visual depth
      const reversedDoubled = [...doubled].reverse();
      track2.innerHTML = reversedDoubled.map((item, i) => makeCardHtml(item, i)).join('');
    }

    function toggleGalleryAutoScroll() {
      const track1 = document.getElementById('galleryTrack1');
      const track2 = document.getElementById('galleryTrack2');
      const playIcon = document.getElementById('playIcon');
      const playText = document.getElementById('playText');
      const pulse = document.getElementById('galleryPulse');
      const statusTxt = document.getElementById('galleryStatusText');

      isGalleryPaused = !isGalleryPaused;

      if (isGalleryPaused) {
        if (track1) track1.classList.add('paused');
        if (track2) track2.classList.add('paused');
        if (playIcon) playIcon.textContent = '▶';
        if (playText) playText.textContent = 'REANUDAR';
        if (statusTxt) statusTxt.textContent = 'ROTACIÓN PAUSADA // MODO MANUAL';
        if (pulse) pulse.style.background = '#ffb300';
      } else {
        if (track1) track1.classList.remove('paused');
        if (track2) track2.classList.remove('paused');
        if (playIcon) playIcon.textContent = '⏸';
        if (playText) playText.textContent = 'PAUSAR';
        if (statusTxt) statusTxt.textContent = 'ROTACIÓN ACTIVA // AVANCE CONTINUO';
        if (pulse) pulse.style.background = 'var(--neon-cyan)';
      }
    }

    function stepGalleryStream(delta) {
      const viewport = document.getElementById('galleryStreamViewport');
      if (viewport) {
        viewport.scrollBy({ left: delta, behavior: 'smooth' });
      }
    }

    function openTacticalLightbox(imgId) {
      const imgList = (HT_CONFIG.galleryImages && Array.isArray(HT_CONFIG.galleryImages) && HT_CONFIG.galleryImages.length > 0)
        ? HT_CONFIG.galleryImages
        : DEFAULT_CONFIG.galleryImages;

      const item = imgList.find(img => img.id === imgId) || imgList[0];
      if (!item) return;

      const modal = document.getElementById('tacticalLightboxModal');
      const modalImg = document.getElementById('lightboxImg');
      const badge = document.getElementById('lightboxBadge');
      const title = document.getElementById('lightboxTitle');
      const desc = document.getElementById('lightboxDesc');
      const waBtn = document.getElementById('lightboxWhatsAppBtn');

      if (modalImg) modalImg.src = item.url;
      if (badge) badge.textContent = `[ ${item.badge || 'EVIDENCIA TÁCTICA'} // ${item.location || 'LIMA'} ]`;
      if (title) title.textContent = item.title;
      if (desc) desc.textContent = item.desc || 'Registro oficial de actividades y entrenamiento de alta intensidad Happy Tactical.';

      if (waBtn) {
        const cleanWa = (HT_CONFIG.whatsApp || '51977331267').replace(/\\D/g, '');
        const msg = encodeURIComponent(`Hola Happy Tactical, vi la foto "${item.title}" de la galería y quisiera información sobre las capacitaciones.`);
        waBtn.href = `https://wa.me/${cleanWa}?text=${msg}`;
      }

      if (modal && typeof modal.showModal === 'function') {
        modal.showModal();
        document.body.style.overflow = 'hidden';
      }
    }

    function closeTacticalLightbox() {
      const modal = document.getElementById('tacticalLightboxModal');
      if (modal && typeof modal.close === 'function') {
        modal.close();
      }
      document.body.style.overflow = '';
    }

    // ========================================================================
    // TACTICAL VIDEO LIBRARY, SPOTLIGHT HERO & CINEMA MODAL
    // ========================================================================
    let currentVideoCategory = 'todos';

    function getEmbedUrl(url) {
      if (!url) return '';
      if (url.includes('embed')) return url;
      
      const ytMatch = url.match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))([\\w-]{11})/);
      if (ytMatch && ytMatch[1]) {
        return `https://www.youtube-nocookie.com/embed/${ytMatch[1]}?autoplay=1&rel=0`;
      }

      const vimeoMatch = url.match(/vimeo\\.com\\/(?:channels\\/(?:\\w+\\/)?|groups\\/[^\\/]*\\/videos\\/|album\\/(?:\\d+\\/)?video\\/|video\\/|)(\\d+)/);
      if (vimeoMatch && vimeoMatch[1]) {
        return `https://player.vimeo.com/video/${vimeoMatch[1]}?autoplay=1`;
      }

      return url;
    }

    function getCategoryLabel(cat) {
      const map = {
        'seguridad': 'TIRO & SEGURIDAD',
        'primeros-auxilios': 'MEDICINA TCCC',
        'emergencias': 'GESTIÓN DE EMERGENCIAS',
        'corporativo': 'BRIGADAS EMPRESARIALES'
      };
      return map[cat] || 'TÁCTICO OPERATIVO';
    }

    function renderTacticalVideos(category = 'todos') {
      currentVideoCategory = category;
      const grid = document.getElementById('tacticalVideoGrid');
      const spotlightWrap = document.getElementById('videoSpotlightContainer');

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
            <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px; background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px dashed rgba(255,255,255,0.15);">
              <span style="font-size: 32px; display: block; margin-bottom: 10px;">📹</span>
              <p style="font-family: var(--font-display); font-size: 15px; color: var(--text-dim);">No hay videos registrados en esta categoría actualmente.</p>
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
                <a href="https://wa.me/${cleanWa}?text=${waMsg}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" style="display: inline-flex; align-items: center; gap: 6px;">
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

      if (typeof init3DTilt === 'function') {
        setTimeout(init3DTilt, 50);
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

    // Modal backdrop click listener for Lightbox & Video Modal
    document.addEventListener('DOMContentLoaded', () => {
      ['tacticalLightboxModal', 'tacticalVideoModal'].forEach(mId => {
        const m = document.getElementById(mId);
        if (m) {
          m.addEventListener('click', (e) => {
            const rect = m.getBoundingClientRect();
            const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                                rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
            if (!isInDialog) {
              if (mId === 'tacticalLightboxModal') closeTacticalLightbox();
              if (mId === 'tacticalVideoModal') closeTacticalVideoModal();
            }
          });
        }
      });
    });
"""

    old_apply_end = """      applyImagesAndFraming();
      renderScheduleList();
      populateOwnerFormInputs();
    }"""

    new_apply_end = """      applyImagesAndFraming();
      renderScheduleList();
      renderGalleryStream();
      renderTacticalVideos();
      populateOwnerFormInputs();
    }"""

    if old_apply_end in content:
        content = content.replace(old_apply_end, new_apply_end, 1)
        print("✓ applyConfigToDOM updated to render gallery and videos")

    old_func_anchor = "    function openCourseModal(courseKey) {"
    if old_func_anchor in content:
        content = content.replace(old_func_anchor, new_js_logic + "\n    " + old_func_anchor, 1)
        print("✓ New JS logic for Gallery and Video Zone added")

    return content

def run():
    files = [
        '/Users/stevefernandovelarde/Desktop/web leo/index.html',
        '/Users/stevefernandovelarde/Desktop/web leo/Happy_Tactical_Home_Mobile_Ordenado_V3-2.html'
    ]

    for path in files:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue

        print(f"\nProcessing {os.path.basename(path)}...")
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = build_integrated_html(content)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)

        print(f"✓ Saved {os.path.basename(path)} (Size: {len(updated)} bytes)")

if __name__ == '__main__':
    run()
