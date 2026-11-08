#!/usr/bin/env python3
"""
Generate about-f1.svg: Dual telemetry cards:
Left: Capability rows with browser bar & telemetry tiles (Web Craft, Python Logic, Hackathons & Prototyping).
Right: Driver telemetry & carousel with Instagram progress bars & 3 daily activity rings.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "about-f1.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="380" viewBox="0 0 860 380" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Mono', monospace">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1322"/>
      <stop offset="100%" stop-color="#060912"/>
    </linearGradient>

    <!-- Ring Gradients -->
    <linearGradient id="ringOrange" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff6b00"/><stop offset="100%" stop-color="#fcd700"/>
    </linearGradient>
    <linearGradient id="ringRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff1801"/><stop offset="100%" stop-color="#ff6b00"/>
    </linearGradient>
    <linearGradient id="ringCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff"/><stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>

    <!-- Subtle Dot Grid Pattern -->
    <pattern id="dotPattern" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="8" cy="8" r="0.75" fill="#20304c" opacity="0.45"/>
    </pattern>
  </defs>

  <style>
    .cursor-blink { animation: cBlink 0.9s steps(2, start) infinite; }
    @keyframes cBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

    /* Ring Fill Keyframes */
    .r-outer { stroke-dasharray: 238; stroke-dashoffset: 238; animation: fillR1 3s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }
    .r-mid   { stroke-dasharray: 188; stroke-dashoffset: 188; animation: fillR2 3.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }
    .r-inner { stroke-dasharray: 138; stroke-dashoffset: 138; animation: fillR3 3.4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }

    @keyframes fillR1 { to { stroke-dashoffset: 24; } }
    @keyframes fillR2 { to { stroke-dashoffset: 38; } }
    @keyframes fillR3 { to { stroke-dashoffset: 35; } }

    @media (prefers-reduced-motion: reduce) {
      .cursor-blink, .r-outer, .r-mid, .r-inner { animation: none !important; }
      .r-outer { stroke-dashoffset: 24 !important; }
      .r-mid   { stroke-dashoffset: 38 !important; }
      .r-inner { stroke-dashoffset: 35 !important; }
    }
  </style>

  <!-- Canvas Background -->
  <rect width="860" height="380" rx="14" fill="#04060c"/>
  <rect width="860" height="380" rx="14" fill="url(#dotPattern)"/>

  <!-- ================================================================= -->
  <!-- LEFT CARD: RACE CRAFT // WHAT I BUILD (x: 15, y: 15, w: 410, h: 350) -->
  <!-- ================================================================= -->
  <g transform="translate(15, 15)">
    <!-- Card Frame -->
    <rect width="410" height="350" rx="14" fill="url(#cardBg)"/>
    <rect x="0.5" y="0.5" width="409" height="349" rx="14" fill="none" stroke="#1d2d49" stroke-width="1.2"/>

    <!-- Top Window Chrome / URL Bar -->
    <path d="M0 0 L410 0 L410 36 L0 36 Z" fill="#090f1c"/>
    <line x1="0" y1="36" x2="410" y2="36" stroke="#1d2d49" stroke-width="1"/>

    <!-- Window Dots -->
    <circle cx="18" cy="18" r="4.5" fill="#ff1801"/>
    <circle cx="34" cy="18" r="4.5" fill="#fcd700"/>
    <circle cx="50" cy="18" r="4.5" fill="#39d353"/>

    <!-- Telemetry URL Bar -->
    <rect x="72" y="8" width="322" height="20" rx="6" fill="#04070f" stroke="#19263e" stroke-width="0.8"/>
    <text x="82" y="22" fill="#6880a4" font-size="10" font-weight="600">telemetry://pitwall.f1/capabilities</text>
    <rect x="264" y="11" width="6" height="14" fill="#00f0ff" class="cursor-blink"/>

    <!-- Section Header -->
    <text x="20" y="62" fill="#fcd700" font-size="12" font-weight="800" letter-spacing="0.14em">
      RACE CRAFT <tspan fill="#6880a4">// WHAT I BUILD &amp; EXPLORE</tspan>
    </text>

    <!-- Capability Row 1: Frontend & Web Craft -->
    <g transform="translate(18, 76)">
      <rect width="374" height="72" rx="10" fill="#090f1d" stroke="#1c2d4a" stroke-width="1"/>
      <rect x="12" y="14" width="44" height="44" rx="8" fill="#111d33" stroke="#ff6b00" stroke-width="1"/>
      <text x="34" y="42" fill="#ff6b00" font-size="18" font-weight="900" text-anchor="middle">&lt;/&gt;</text>

      <text x="68" y="30" fill="#ffffff" font-size="13" font-weight="700">Modern Web Interfaces &amp; UI Craft</text>
      <text x="68" y="46" fill="#8da2c0" font-size="10.5">Semantic HTML5, CSS3 responsive grid &amp; ES6+ JavaScript.</text>
      <text x="68" y="60" fill="#ff6b00" font-size="9.5" font-weight="800">TELEMETRY: CLEAN CODE // RESPONSIVE DESIGN</text>
    </g>

    <!-- Capability Row 2: Python Scripting & Automation -->
    <g transform="translate(18, 160)">
      <rect width="374" height="72" rx="10" fill="#090f1d" stroke="#1c2d4a" stroke-width="1"/>
      <rect x="12" y="14" width="44" height="44" rx="8" fill="#111d33" stroke="#39d353" stroke-width="1"/>
      <text x="34" y="42" fill="#39d353" font-size="18" font-weight="900" text-anchor="middle">🐍</text>

      <text x="68" y="30" fill="#ffffff" font-size="13" font-weight="700">Python Automation &amp; CS Foundations</text>
      <text x="68" y="46" fill="#8da2c0" font-size="10.5">Data parsing, automation pipelines &amp; algorithmic logic.</text>
      <text x="68" y="60" fill="#39d353" font-size="9.5" font-weight="800">TELEMETRY: SCRIPTING // FIRST-PRINCIPLES CS</text>
    </g>

    <!-- Capability Row 3: Rapid Prototyping & Hackathons -->
    <g transform="translate(18, 244)">
      <rect width="374" height="72" rx="10" fill="#090f1d" stroke="#1c2d4a" stroke-width="1"/>
      <rect x="12" y="14" width="44" height="44" rx="8" fill="#111d33" stroke="#fcd700" stroke-width="1"/>
      <text x="34" y="42" fill="#fcd700" font-size="18" font-weight="900" text-anchor="middle">🏆</text>

      <text x="68" y="30" fill="#ffffff" font-size="13" font-weight="700">Rapid Prototyping &amp; Hackathon Lead</text>
      <text x="68" y="46" fill="#8da2c0" font-size="10.5">SIH 2026 Team Lead (ThermoIntel) &amp; NIAT Sprint Winner.</text>
      <text x="68" y="60" fill="#fcd700" font-size="9.5" font-weight="800">TELEMETRY: SMART INDIA HACKATHON 2026 QUALIFIED</text>
    </g>
  </g>

  <!-- =================================================================== -->
  <!-- RIGHT CARD: DRIVER TELEMETRY & CAROUSEL (x: 435, y: 15, w: 410, h: 350) -->
  <!-- =================================================================== -->
  <g transform="translate(435, 15)">
    <!-- Card Frame -->
    <rect width="410" height="350" rx="14" fill="url(#cardBg)"/>
    <rect x="0.5" y="0.5" width="409" height="349" rx="14" fill="none" stroke="#1d2d49" stroke-width="1.2"/>

    <!-- Top Instagram-style Story Segment Progress Bars (3 segments) -->
    <g transform="translate(20, 16)">
      <!-- Segment 1: 0s-4s -->
      <rect x="0" y="0" width="118" height="3" rx="1.5" fill="#1b2a44"/>
      <rect x="0" y="0" width="118" height="3" rx="1.5" fill="#fcd700">
        <animate attributeName="width" values="0;118;118;0" keyTimes="0;0.31;0.98;1" dur="12s" repeatCount="indefinite"/>
      </rect>

      <!-- Segment 2: 4s-8s -->
      <rect x="126" y="0" width="118" height="3" rx="1.5" fill="#1b2a44"/>
      <rect x="126" y="0" width="118" height="3" rx="1.5" fill="#ff6b00">
        <animate attributeName="width" values="0;0;118;118;0" keyTimes="0;0.33;0.64;0.98;1" dur="12s" repeatCount="indefinite"/>
      </rect>

      <!-- Segment 3: 8s-12s -->
      <rect x="252" y="0" width="118" height="3" rx="1.5" fill="#1b2a44"/>
      <rect x="252" y="0" width="118" height="3" rx="1.5" fill="#00f0ff">
        <animate attributeName="width" values="0;0;118;118;0" keyTimes="0;0.66;0.98;0.99;1" dur="12s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Carousel Header -->
    <g transform="translate(20, 48)">
      <text x="0" y="0" fill="#fcd700" font-size="12" font-weight="800" letter-spacing="0.14em">
        PASSIONS <tspan fill="#6880a4">// DRIVER TELEMETRY</tspan>
      </text>
    </g>

    <!-- Carousel Content Box (Slides 1, 2, 3) -->
    <g transform="translate(20, 68)">
      <!-- Slide 1: Formula 1 & Sim Racing -->
      <g opacity="0">
        <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.31;0.33" dur="12s" repeatCount="indefinite"/>
        <rect width="370" height="92" rx="10" fill="#090f1d" stroke="#ff1801" stroke-width="1"/>
        <text x="16" y="26" fill="#fcd700" font-size="13" font-weight="800">🏎️ FORMULA 1 &amp; SIM RACING</text>
        <text x="16" y="46" fill="#ffffff" font-size="11.5" font-weight="600">Max Verstappen #1 Oracle Red Bull Racing fan.</text>
        <text x="16" y="64" fill="#8da2c0" font-size="10.5">Telemetry breakdowns, race pace simulation &amp; apex pursuit.</text>
        <text x="16" y="80" fill="#ff6b00" font-size="9.5" font-weight="700">STATUS: "SIMPLY LOVELY, MATE!"</text>
      </g>

      <!-- Slide 2: Physical Conditioning -->
      <g opacity="0">
        <animate attributeName="opacity" values="0;1;1;0" keyTimes="0.33;0.38;0.64;0.66" dur="12s" repeatCount="indefinite"/>
        <rect width="370" height="92" rx="10" fill="#090f1d" stroke="#ff6b00" stroke-width="1"/>
        <text x="16" y="26" fill="#ff6b00" font-size="13" font-weight="800">⚡ ATHLETIC READINESS &amp; GYM</text>
        <text x="16" y="46" fill="#ffffff" font-size="11.5" font-weight="600">Reaction timer drills &amp; physical conditioning.</text>
        <text x="16" y="64" fill="#8da2c0" font-size="10.5">High cardiovascular stamina to sustain deep problem-solving.</text>
        <text x="16" y="80" fill="#fcd700" font-size="9.5" font-weight="700">STATUS: 5G REACTION VELOCITY</text>
      </g>

      <!-- Slide 3: Hackathons & Open Source -->
      <g opacity="0">
        <animate attributeName="opacity" values="0;1;1;0" keyTimes="0.66;0.71;0.97;1" dur="12s" repeatCount="indefinite"/>
        <rect width="370" height="92" rx="10" fill="#090f1d" stroke="#00f0ff" stroke-width="1"/>
        <text x="16" y="26" fill="#00f0ff" font-size="13" font-weight="800">🏆 HIGH-SPEED CODE SPRINTS</text>
        <text x="16" y="46" fill="#ffffff" font-size="11.5" font-weight="600">Hackathon sprints &amp; rapid MVP development.</text>
        <text x="16" y="64" fill="#8da2c0" font-size="10.5">Building practical prototypes from first principles.</text>
        <text x="16" y="80" fill="#39d353" font-size="9.5" font-weight="700">STATUS: POLE POSITION COMMIT CADENCE</text>
      </g>
    </g>

    <!-- 3 Daily Rings (Telemetry Lap Rings) -->
    <g transform="translate(20, 180)">
      <rect width="370" height="150" rx="10" fill="#090f1d" stroke="#1c2d4a" stroke-width="1"/>

      <!-- SVG Rings Container -->
      <g transform="translate(90, 75)">
        <!-- Outer Ring Track (R: 38, C: 238) -->
        <circle cx="0" cy="0" r="38" fill="none" stroke="#131e33" stroke-width="8"/>
        <circle cx="0" cy="0" r="38" fill="none" stroke="url(#ringOrange)" stroke-width="8" stroke-linecap="round" class="r-outer" transform="rotate(-90)"/>

        <!-- Middle Ring Track (R: 30, C: 188) -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#131e33" stroke-width="7"/>
        <circle cx="0" cy="0" r="30" fill="none" stroke="url(#ringRed)" stroke-width="7" stroke-linecap="round" class="r-mid" transform="rotate(-90)"/>

        <!-- Inner Ring Track (R: 22, C: 138) -->
        <circle cx="0" cy="0" r="22" fill="none" stroke="#131e33" stroke-width="6"/>
        <circle cx="0" cy="0" r="22" fill="none" stroke="url(#ringCyan)" stroke-width="6" stroke-linecap="round" class="r-inner" transform="rotate(-90)"/>

        <!-- Center F1 Icon -->
        <text x="0" y="4" fill="#fcd700" font-size="13" font-weight="900" text-anchor="middle">#1</text>
      </g>

      <!-- Rings Legend / Telemetry Breakdown -->
      <g transform="translate(195, 30)">
        <text x="0" y="0" fill="#6880a4" font-size="10" font-weight="800" letter-spacing="0.1em">DAILY ENGINE METRICS</text>

        <!-- Ring 1 Legend -->
        <g transform="translate(0, 20)">
          <circle cx="5" cy="5" r="4" fill="#ff6b00"/>
          <text x="16" y="8" fill="#ffffff" font-size="11" font-weight="700">Code Cadence: <tspan fill="#ff6b00">100%</tspan></text>
          <text x="16" y="21" fill="#6880a4" font-size="9.5">Daily Git commits &amp; builds</text>
        </g>

        <!-- Ring 2 Legend -->
        <g transform="translate(0, 48)">
          <circle cx="5" cy="5" r="4" fill="#ff1801"/>
          <text x="16" y="8" fill="#ffffff" font-size="11" font-weight="700">Sprint Laps: <tspan fill="#ff1801">85%</tspan></text>
          <text x="16" y="21" fill="#6880a4" font-size="9.5">CS fundamentals &amp; logic</text>
        </g>

        <!-- Ring 3 Legend -->
        <g transform="translate(0, 76)">
          <circle cx="5" cy="5" r="4" fill="#00f0ff"/>
          <text x="16" y="8" fill="#ffffff" font-size="11" font-weight="700">R&amp;D Laps: <tspan fill="#00f0ff">75%</tspan></text>
          <text x="16" y="21" fill="#6880a4" font-size="9.5">SIH &amp; prototype architecture</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Wrote {OUT_PATH}: {len(svg)} bytes")
