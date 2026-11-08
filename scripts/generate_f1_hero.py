#!/usr/bin/env python3
"""
Generate the Formula 1 & Max Verstappen #1 Cockpit Telemetry Hero SVG (hero.svg).
Pure self-contained SVG + SMIL / CSS keyframe animations.
Accurately displays Aryan Mall's F1 cockpit avatar and verified skills.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO_PATH = os.path.join(HERE, "..", "f1-avatar.png")
if not os.path.exists(PHOTO_PATH):
    PHOTO_PATH = os.path.join(HERE, "..", "source-photo.png")
OUT_PATH = os.path.join(HERE, "..", "hero.svg")

with open(PHOTO_PATH, "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("ascii")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="360" viewBox="0 0 860 360" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Mono', monospace">
  <defs>
    <!-- Dark F1 Carbon Navy Gradients -->
    <linearGradient id="carbonBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a101d"/>
      <stop offset="45%" stop-color="#05080f"/>
      <stop offset="100%" stop-color="#070c16"/>
    </linearGradient>

    <!-- Red Bull & Max Verstappen Racing Gradient -->
    <linearGradient id="rbGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff1801"/>
      <stop offset="35%" stop-color="#ff6b00"/>
      <stop offset="70%" stop-color="#fcd700"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>

    <!-- Dutch Orange Laser Beam -->
    <linearGradient id="laserBeam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff1801" stop-opacity="0"/>
      <stop offset="20%" stop-color="#ff6b00"/>
      <stop offset="50%" stop-color="#fcd700"/>
      <stop offset="80%" stop-color="#00f0ff"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </linearGradient>

    <!-- Viewfinder Halo Glow -->
    <radialGradient id="cockpitGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff6b00" stop-opacity="0.3"/>
      <stop offset="70%" stop-color="#ff1801" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#05080f" stop-opacity="0"/>
    </radialGradient>

    <!-- Carbon Fiber Weave Pattern -->
    <pattern id="carbonWeave" width="12" height="12" patternUnits="userSpaceOnUse">
      <rect width="12" height="12" fill="#060911"/>
      <path d="M0 0 L6 6 M6 0 L0 6 M6 6 L12 12 M12 6 L6 12" stroke="#10192b" stroke-width="0.8" opacity="0.65"/>
      <rect x="0" y="0" width="6" height="6" fill="#0c1322" opacity="0.4"/>
      <rect x="6" y="6" width="6" height="6" fill="#0c1322" opacity="0.4"/>
    </pattern>

    <!-- Clip Path for Driver Visor / Photo (in local coordinates of container <g>) -->
    <clipPath id="avatarVisor">
      <rect x="20" y="50" width="170" height="170" rx="22"/>
    </clipPath>

    <!-- Glow Filter -->
    <filter id="f1Glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* Racing HUD Animations */
    .rec-blink {{ animation: recFlash 1s steps(2, start) infinite; }}
    .laser-sweep {{ animation: laserMove 3.6s ease-in-out infinite; }}
    .rpm-pulse {{ animation: tachometer 1.8s ease-in-out infinite alternate; }}
    .halo-orbit {{ transform-origin: 710px 190px; animation: orbitRotate 18s linear infinite; }}
    .live-pulse {{ animation: livePulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}

    @keyframes recFlash {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.15; }}
    }}
    @keyframes laserMove {{
      0% {{ stroke-dashoffset: 600; opacity: 0.2; }}
      50% {{ stroke-dashoffset: 0; opacity: 1; }}
      100% {{ stroke-dashoffset: -600; opacity: 0.2; }}
    }}
    @keyframes tachometer {{
      0% {{ width: 28px; }}
      100% {{ width: 140px; }}
    }}
    @keyframes orbitRotate {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    @keyframes livePulse {{
      0%, 100% {{ opacity: 0.4; transform: scale(0.95); }}
      50% {{ opacity: 1; transform: scale(1.05); }}
    }}

    /* Role Cycler */
    .role-text {{
      font-size: 13.5px;
      font-weight: 800;
      letter-spacing: 0.1em;
      fill: #00f0ff;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .rec-blink, .laser-sweep, .rpm-pulse, .halo-orbit, .live-pulse {{
        animation: none !important;
      }}
    }}
  </style>

  <!-- Base Chassis -->
  <rect width="860" height="360" rx="16" fill="url(#carbonBg)"/>
  <rect width="860" height="360" rx="16" fill="url(#carbonWeave)"/>
  <rect x="0.5" y="0.5" width="859" height="359" rx="16" fill="none" stroke="#ff1801" stroke-width="1.2" stroke-opacity="0.7"/>

  <!-- Top Telemetry Bar & Red Bull Racing Livery Band -->
  <path d="M0 0 L860 0 L860 38 L0 38 Z" fill="#080d17"/>
  <line x1="0" y1="38" x2="860" y2="38" stroke="#1d2d49" stroke-width="1"/>

  <!-- Dutch Tricolor + Racing Stripe Accent on Left -->
  <rect x="22" y="14" width="4" height="12" fill="#ff1801"/>
  <rect x="26" y="14" width="4" height="12" fill="#ffffff"/>
  <rect x="30" y="14" width="4" height="12" fill="#21468b"/>

  <text x="44" y="23" fill="#ff6b00" font-size="11.5" font-weight="800" letter-spacing="0.16em">
    ORACLE RED BULL RACING <tspan fill="#fcd700">#1</tspan> <tspan fill="#5a7094">//</tspan> FIA FORMULA 1 HUD
  </text>

  <!-- F1 5-LIGHTS GANTRY (CENTER HUD) -->
  <g transform="translate(390, 11)">
    <rect x="-8" y="-1" width="116" height="18" rx="4" fill="#04060a" stroke="#253a5c" stroke-width="0.8"/>
    <!-- Light 1 -->
    <circle cx="8" cy="8" r="4.5" fill="#1b0808"/>
    <circle cx="8" cy="8" r="4.5" fill="#ff1801">
      <animate attributeName="opacity" values="0.15;1;1;0.15" keyTimes="0;0.18;0.82;0.86" dur="5s" repeatCount="indefinite"/>
    </circle>
    <!-- Light 2 -->
    <circle cx="28" cy="8" r="4.5" fill="#1b0808"/>
    <circle cx="28" cy="8" r="4.5" fill="#ff1801">
      <animate attributeName="opacity" values="0.15;0.15;1;1;0.15" keyTimes="0;0.18;0.34;0.82;0.86" dur="5s" repeatCount="indefinite"/>
    </circle>
    <!-- Light 3 -->
    <circle cx="48" cy="8" r="4.5" fill="#1b0808"/>
    <circle cx="48" cy="8" r="4.5" fill="#ff1801">
      <animate attributeName="opacity" values="0.15;0.15;1;1;0.15" keyTimes="0;0.34;0.50;0.82;0.86" dur="5s" repeatCount="indefinite"/>
    </circle>
    <!-- Light 4 -->
    <circle cx="68" cy="8" r="4.5" fill="#1b0808"/>
    <circle cx="68" cy="8" r="4.5" fill="#ff1801">
      <animate attributeName="opacity" values="0.15;0.15;1;1;0.15" keyTimes="0;0.50;0.66;0.82;0.86" dur="5s" repeatCount="indefinite"/>
    </circle>
    <!-- Light 5 -->
    <circle cx="88" cy="8" r="4.5" fill="#1b0808"/>
    <circle cx="88" cy="8" r="4.5" fill="#ff1801">
      <animate attributeName="opacity" values="0.15;0.15;1;1;0.15" keyTimes="0;0.66;0.82;0.82;0.86" dur="5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Live Status Right Tag -->
  <g transform="translate(710, 19)">
    <circle cx="0" cy="0" r="4" fill="#39d353" class="rec-blink"/>
    <text x="12" y="4" fill="#39d353" font-size="11" font-weight="700" letter-spacing="0.1em">LIVE ON TRACK</text>
  </g>

  <!-- LEFT HERO SECTION: TITLE, ROLE, SPECS -->
  <!-- Status Pill -->
  <g transform="translate(36, 60)">
    <rect width="230" height="26" rx="13" fill="#0d182b" stroke="#ff6b00" stroke-width="1"/>
    <circle cx="14" cy="13" r="3.5" fill="#ff1801" class="live-pulse"/>
    <text x="26" y="17" fill="#fcd700" font-size="10.5" font-weight="800" letter-spacing="0.14em">POLE POSITION // VER-01</text>
  </g>

  <!-- Driver Name in bold F1 Champion Typography -->
  <text x="36" y="132" font-size="44" font-weight="900" font-style="italic" letter-spacing="0.04em" fill="url(#rbGradient)">
    ARYAN MALL
  </text>
  <!-- Max Verstappen Driver Number #1 Emblem -->
  <g transform="translate(345, 96)">
    <rect width="42" height="38" rx="6" fill="#ff1801"/>
    <text x="21" y="27" fill="#ffffff" font-size="24" font-weight="900" font-style="italic" text-anchor="middle">1</text>
    <path d="M4 34 L38 34" stroke="#fcd700" stroke-width="3"/>
  </g>

  <!-- Laser Underline Sweep -->
  <line x1="36" y1="148" x2="560" y2="148" stroke="url(#laserBeam)" stroke-width="2.5" stroke-dasharray="200" stroke-dashoffset="600" class="laser-sweep"/>
  <circle cx="36" cy="148" r="2.5" fill="#fcd700"/>

  <!-- Cycling Role Lines (SMIL Crossfade) -->
  <g transform="translate(38, 182)">
    <!-- Role 1 -->
    <text class="role-text" opacity="0">
      ⚡ WEB CRAFTER // HTML · CSS · JS · PYTHON
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.30;0.34" dur="10.5s" repeatCount="indefinite"/>
      <animate attributeName="y" values="6;0;0;-6" keyTimes="0;0.08;0.30;0.34" dur="10.5s" repeatCount="indefinite"/>
    </text>
    <!-- Role 2 -->
    <text class="role-text" opacity="0">
      🏆 SIH 2026 TEAM LEADER // THERMOINTEL
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0.34;0.42;0.63;0.67" dur="10.5s" repeatCount="indefinite"/>
      <animate attributeName="y" values="6;0;0;-6" keyTimes="0.34;0.42;0.63;0.67" dur="10.5s" repeatCount="indefinite"/>
    </text>
    <!-- Role 3 -->
    <text class="role-text" opacity="0">
      🏎️ RAPID PROTOTYPER &amp; MAX VERSTAPPEN #1 FAN
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0.67;0.75;0.96;1" dur="10.5s" repeatCount="indefinite"/>
      <animate attributeName="y" values="6;0;0;-6" keyTimes="0.67;0.75;0.96;1" dur="10.5s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- Max Verstappen Champion Quote -->
  <g transform="translate(38, 222)">
    <rect width="520" height="42" rx="8" fill="#080e1a" stroke="#1d2d49" stroke-width="1"/>
    <path d="M0 0 L4 0 L4 42 L0 42 Z" fill="#ff1801"/>
    <text x="16" y="18" fill="#ffffff" font-size="12" font-style="italic" font-weight="600">
      "Simply lovely! If you don't go for a gap that exists, you are no longer a racing driver."
    </text>
    <text x="16" y="33" fill="#fcd700" font-size="10.5" font-weight="700" letter-spacing="0.1em">
      MAX VERSTAPPEN <tspan fill="#6880a4">· 4X F1 WORLD CHAMPION</tspan>
    </text>
  </g>

  <!-- Live Telemetry Sector Strip -->
  <g transform="translate(38, 290)">
    <rect width="520" height="44" rx="10" fill="#060b14" stroke="#253a5c" stroke-width="1"/>
    <!-- Sector 1 -->
    <text x="20" y="18" fill="#6880a4" font-size="10" font-weight="700">CAMPUS</text>
    <text x="20" y="34" fill="#a855f7" font-size="12" font-weight="900">SUSHANT UNIV</text>
    <!-- Sector 2 -->
    <text x="155" y="18" fill="#6880a4" font-size="10" font-weight="700">CORE TECH</text>
    <text x="155" y="34" fill="#00f0ff" font-size="12" font-weight="900">HTML·CSS·JS·PY</text>
    <!-- Top Speed -->
    <text x="295" y="18" fill="#6880a4" font-size="10" font-weight="700">TOP SPEED</text>
    <text x="295" y="34" fill="#fcd700" font-size="12" font-weight="900">345 KM/H (P1)</text>
    <!-- Tyre Compound -->
    <text x="415" y="18" fill="#6880a4" font-size="10" font-weight="700">TYRE STRAT</text>
    <text x="415" y="34" fill="#ff1801" font-size="12" font-weight="900">🔴 SOFT (L1)</text>
  </g>

  <!-- RIGHT COCKPIT VIEWFINDER (DRIVER VISOR & TELEMETRY) -->
  <g transform="translate(605, 55)">
    <!-- Cockpit Frame Outer Glow -->
    <circle cx="105" cy="135" r="100" fill="url(#cockpitGlow)"/>

    <!-- Dual Aerodynamic Halo Orbit Rings -->
    <ellipse cx="105" cy="135" rx="112" ry="112" fill="none" stroke="#ff1801" stroke-width="1" stroke-opacity="0.35"/>
    <ellipse cx="105" cy="135" rx="122" ry="122" fill="none" stroke="#ff6b00" stroke-width="0.75" stroke-dasharray="6 12" class="halo-orbit" stroke-opacity="0.5"/>

    <!-- Viewfinder Background Window -->
    <rect x="15" y="45" width="180" height="180" rx="22" fill="#080e1a" stroke="#253a5c" stroke-width="1.5"/>

    <!-- Embedded Driver Avatar (Now clipped cleanly to exact inner frame) -->
    <image href="data:image/png;base64,{photo_b64}" x="20" y="50" width="170" height="170" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarVisor)"/>

    <!-- Driver Visor Aerodynamic Border -->
    <rect x="20" y="50" width="170" height="170" rx="22" fill="none" stroke="#ff6b00" stroke-width="2" stroke-opacity="0.8"/>

    <!-- Viewfinder Camera Corner Brackets -->
    <path d="M 10 55 L 10 40 L 25 40" fill="none" stroke="#00f0ff" stroke-width="2.5"/>
    <path d="M 200 55 L 200 40 L 185 40" fill="none" stroke="#00f0ff" stroke-width="2.5"/>
    <path d="M 10 215 L 10 230 L 25 230" fill="none" stroke="#00f0ff" stroke-width="2.5"/>
    <path d="M 200 215 L 200 230 L 185 230" fill="none" stroke="#00f0ff" stroke-width="2.5"/>

    <!-- Top Viewfinder Header: REC dot & Timecode -->
    <g transform="translate(18, 25)">
      <circle cx="0" cy="0" r="4" fill="#ff1801" class="rec-blink"/>
      <text x="10" y="4" fill="#ff1801" font-size="10.5" font-weight="900" letter-spacing="0.1em">REC</text>
      <text x="80" y="4" fill="#00f0ff" font-size="10" font-weight="700">00:01:21.432</text>
      <text x="152" y="4" fill="#fcd700" font-size="9" font-weight="800">4K//60</text>
    </g>

    <!-- F1 RPM Shift Lights Array (Above Avatar) -->
    <g transform="translate(25, 42)">
      <!-- 8 Shift LEDs: Green Green Yellow Yellow Red Red Blue Blue -->
      <circle cx="10" cy="0" r="2.5" fill="#39d353"/>
      <circle cx="28" cy="0" r="2.5" fill="#39d353"/>
      <circle cx="46" cy="0" r="2.5" fill="#fcd700"/>
      <circle cx="64" cy="0" r="2.5" fill="#fcd700"/>
      <circle cx="82" cy="0" r="2.5" fill="#ff6b00"/>
      <circle cx="100" cy="0" r="2.5" fill="#ff1801"/>
      <circle cx="118" cy="0" r="2.5" fill="#ff1801"/>
      <circle cx="136" cy="0" r="2.5" fill="#00f0ff"/>
      <circle cx="150" cy="0" r="2.5" fill="#a855f7"/>
    </g>

    <!-- Bottom Scrubber Bar -->
    <g transform="translate(20, 235)">
      <rect width="170" height="4" rx="2" fill="#142138"/>
      <rect width="170" height="4" rx="2" fill="url(#rbGradient)">
        <animate attributeName="width" values="0;170;170;0" keyTimes="0;0.7;0.9;1" dur="4s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Driver Badge Tag -->
    <g transform="translate(30, 256)">
      <rect width="150" height="22" rx="6" fill="#04070e" stroke="#ff1801" stroke-width="1"/>
      <text x="75" y="15" fill="#ffffff" font-size="10" font-weight="800" letter-spacing="0.1em" text-anchor="middle">
        DRIVER // <tspan fill="#fcd700">AM-01</tspan>
      </text>
    </g>
  </g>
</svg>'''

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Wrote {OUT_PATH}: {len(svg_content)} bytes")
