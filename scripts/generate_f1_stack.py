#!/usr/bin/env python3
"""
Generate stack.svg:
V6 Turbo Hybrid Power Unit Tech Orbit + Grouped Pit Stop Chip Grid.
Features 3 tilted 3D elliptical orbits with tech icons and orbiting moons,
plus a 4-group telemetry chip grid with sequential glowing borders.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stack.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="490" viewBox="0 0 860 490" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Mono', monospace">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="stackBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a101d"/>
      <stop offset="50%" stop-color="#050810"/>
      <stop offset="100%" stop-color="#070c17"/>
    </linearGradient>

    <!-- Core Glow -->
    <radialGradient id="powerUnitGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fcd700" stop-opacity="0.9"/>
      <stop offset="25%" stop-color="#ff6b00" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#ff1801" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#050810" stop-opacity="0"/>
    </radialGradient>

    <!-- Orbit Gradients -->
    <linearGradient id="orbGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff1801" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#fcd700" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ff1801" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="orbGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="orbGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff6b00" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#a855f7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#fcd700" stop-opacity="0.8"/>
    </linearGradient>

    <!-- Chip Background -->
    <linearGradient id="chipBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e172a"/><stop offset="100%" stop-color="#080e1a"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="stackGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#142137" stroke-width="0.75" opacity="0.6"/>
    </pattern>
  </defs>

  <style>
    /* Orbital Animations */
    .core-pulse { animation: cPulse 2.4s ease-in-out infinite alternate; }
    .rot-orbit1 { transform-origin: 430px 145px; animation: spin1 20s linear infinite; }
    .rot-orbit2 { transform-origin: 430px 145px; animation: spin2 28s linear infinite reverse; }
    .rot-orbit3 { transform-origin: 430px 145px; animation: spin3 36s linear infinite; }
    .moon-orbit  { transform-origin: 0px 0px; animation: moonSpin 6s linear infinite; }

    @keyframes cPulse {
      0% { r: 24; opacity: 0.8; }
      100% { r: 32; opacity: 1; filter: drop-shadow(0 0 16px #ff6b00); }
    }
    @keyframes spin1 { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes spin2 { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes spin3 { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes moonSpin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Sequential Chip Glowing Borders */
    .glow-chip1 { animation: chipGlow 6s ease-in-out infinite 0s; }
    .glow-chip2 { animation: chipGlow 6s ease-in-out infinite 1.5s; }
    .glow-chip3 { animation: chipGlow 6s ease-in-out infinite 3.0s; }
    .glow-chip4 { animation: chipGlow 6s ease-in-out infinite 4.5s; }

    @keyframes chipGlow {
      0%, 100% { stroke: #1f3354; }
      25% { stroke: #ff6b00; stroke-width: 1.5; }
      50% { stroke: #fcd700; stroke-width: 1.8; }
    }

    @media (prefers-reduced-motion: reduce) {
      .core-pulse, .rot-orbit1, .rot-orbit2, .rot-orbit3, .moon-orbit,
      .glow-chip1, .glow-chip2, .glow-chip3, .glow-chip4 {
        animation: none !important;
      }
    }
  </style>

  <!-- Frame Background -->
  <rect width="860" height="490" rx="16" fill="url(#stackBg)"/>
  <rect width="860" height="490" rx="16" fill="url(#stackGrid)"/>
  <rect x="0.5" y="0.5" width="859" height="489" rx="16" fill="none" stroke="#233858" stroke-width="1.2"/>

  <!-- Top Title Bar -->
  <path d="M0 0 L860 0 L860 38 L0 38 Z" fill="#070c17"/>
  <line x1="0" y1="38" x2="860" y2="38" stroke="#1d2d49" stroke-width="1"/>
  <circle cx="20" cy="19" r="4.5" fill="#ff1801"/>
  <circle cx="36" cy="19" r="4.5" fill="#fcd700"/>
  <circle cx="52" cy="19" r="4.5" fill="#39d353"/>

  <text x="74" y="23" fill="#ff6b00" font-size="11.5" font-weight="800" letter-spacing="0.14em">
    ENGINEERING STACK <tspan fill="#6880a4">// V6 TURBO HYBRID TECH ORBIT</tspan>
  </text>
  <text x="836" y="23" fill="#fcd700" font-size="11" font-weight="700" text-anchor="end">
    RPM: 15,000 MAX // ERS DEPLOYED
  </text>

  <!-- =================================================================== -->
  <!-- TOP HALF: V6 TURBO HYBRID ORBITAL SYSTEM (Center: 430, 145)        -->
  <!-- =================================================================== -->
  <g transform="translate(0, 0)">
    <!-- Core Ambient Glow -->
    <circle cx="430" cy="145" r="95" fill="url(#powerUnitGlow)"/>

    <!-- Orbit 1 Track (Inner: rx=150, ry=52, rot=-18deg) -->
    <g transform="translate(430, 145) rotate(-18)">
      <ellipse cx="0" cy="0" rx="150" ry="52" fill="none" stroke="url(#orbGrad1)" stroke-width="1.2" stroke-dasharray="8 6"/>
    </g>

    <!-- Orbit 2 Track (Middle: rx=230, ry=72, rot=14deg) -->
    <g transform="translate(430, 145) rotate(14)">
      <ellipse cx="0" cy="0" rx="230" ry="72" fill="none" stroke="url(#orbGrad2)" stroke-width="1.2" stroke-dasharray="10 8"/>
    </g>

    <!-- Orbit 3 Track (Outer: rx=320, ry=92, rot=-6deg) -->
    <g transform="translate(430, 145) rotate(-6)">
      <ellipse cx="0" cy="0" rx="320" ry="92" fill="none" stroke="url(#orbGrad3)" stroke-width="1.4" stroke-dasharray="12 10"/>
    </g>

    <!-- Pulsing Central Engine Core -->
    <circle cx="430" cy="145" r="28" fill="#ff1801" class="core-pulse"/>
    <circle cx="430" cy="145" r="18" fill="#fcd700"/>
    <text x="430" y="149" fill="#070c17" font-size="11" font-weight="900" text-anchor="middle">V6</text>

    <!-- Orbit 1 Rotating Nodes (Python & TypeScript) -->
    <g class="rot-orbit1">
      <!-- Node: Python (Top-Left) -->
      <g transform="translate(315, 115)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#fcd700" stroke-width="1.5"/>
        <text x="0" y="5" fill="#fcd700" font-size="16" font-weight="900" text-anchor="middle">🐍</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">Python</text>
      </g>
      <!-- Node: TypeScript (Bottom-Right) -->
      <g transform="translate(545, 175)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#00f0ff" stroke-width="1.5"/>
        <text x="0" y="5" fill="#00f0ff" font-size="13" font-weight="900" text-anchor="middle">TS</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">TypeScript</text>
      </g>
    </g>

    <!-- Orbit 2 Rotating Nodes (React with 2 Orbiting Moons: Next.js & Tailwind) -->
    <g class="rot-orbit2">
      <!-- React Mother Node -->
      <g transform="translate(230, 170)">
        <rect x="-20" y="-20" width="40" height="40" rx="10" fill="#091426" stroke="#00f0ff" stroke-width="1.8"/>
        <text x="0" y="6" fill="#00f0ff" font-size="18" font-weight="900" text-anchor="middle">⚛️</text>
        <text x="0" y="30" fill="#00f0ff" font-size="9.5" font-weight="800" text-anchor="middle">React</text>

        <!-- Moon 1: Next.js orbiting React -->
        <g class="moon-orbit">
          <circle cx="28" cy="0" r="11" fill="#040812" stroke="#ffffff" stroke-width="1"/>
          <text x="28" y="3" fill="#ffffff" font-size="8" font-weight="900" text-anchor="middle">N</text>
        </g>
        <!-- Moon 2: Tailwind orbiting React (opposite) -->
        <g class="moon-orbit">
          <circle cx="-28" cy="0" r="11" fill="#040812" stroke="#38bdf8" stroke-width="1"/>
          <text x="-28" y="3" fill="#38bdf8" font-size="8" font-weight="900" text-anchor="middle">≈</text>
        </g>
      </g>

      <!-- FastAPI Node (Opposite side) -->
      <g transform="translate(630, 120)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#009688" stroke-width="1.5"/>
        <text x="0" y="5" fill="#009688" font-size="14" font-weight="900" text-anchor="middle">⚡</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">FastAPI</text>
      </g>
    </g>

    <!-- Orbit 3 Rotating Nodes (C++, PyTorch, Docker) -->
    <g class="rot-orbit3">
      <!-- C++ Node -->
      <g transform="translate(140, 130)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#ff1801" stroke-width="1.5"/>
        <text x="0" y="5" fill="#ff1801" font-size="12" font-weight="900" text-anchor="middle">C++</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">Speed Core</text>
      </g>
      <!-- PyTorch Node -->
      <g transform="translate(430, 242)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#ff6b00" stroke-width="1.5"/>
        <text x="0" y="5" fill="#ff6b00" font-size="14" font-weight="900" text-anchor="middle">🔥</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">PyTorch</text>
      </g>
      <!-- Docker Node -->
      <g transform="translate(720, 160)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#2496ed" stroke-width="1.5"/>
        <text x="0" y="5" fill="#2496ed" font-size="14" font-weight="900" text-anchor="middle">🐳</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">Docker</text>
      </g>
    </g>
  </g>

  <!-- =================================================================== -->
  <!-- BOTTOM HALF: PIT STOP TELEMETRY CHIP GRID (4 Departments)          -->
  <!-- =================================================================== -->
  <g transform="translate(20, 275)">
    <!-- Department 1: POWERTRAIN // CORE -->
    <g transform="translate(0, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip1"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#ff1801" font-size="10.5" font-weight="800" letter-spacing="0.1em">POWERTRAIN // CORE</text>

      <!-- Chips -->
      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="78" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="39" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Python</text>

        <rect x="88" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="129" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">C++ Core</text>

        <rect x="0" y="36" width="94" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="47" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">TypeScript</text>

        <rect x="104" y="36" width="66" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="137" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">SQL DB</text>

        <rect x="0" y="72" width="102" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="51" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">JavaScript</text>

        <rect x="112" y="72" width="58" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="141" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Go Lang</text>

        <text x="0" y="132" fill="#6880a4" font-size="9" font-weight="700">SPEC: HIGH-THROUGHPUT</text>
      </g>
    </g>

    <!-- Department 2: AERODYNAMICS // FRONTEND -->
    <g transform="translate(208, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip2"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#ff6b00" font-size="10.5" font-weight="800" letter-spacing="0.1em">AERO // FRONTEND</text>

      <!-- Chips -->
      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="78" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="39" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">React.js</text>

        <rect x="88" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="129" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Next.js 14</text>

        <rect x="0" y="36" width="94" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="47" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Tailwind CSS</text>

        <rect x="104" y="36" width="66" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="137" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">HTML/CSS</text>

        <rect x="0" y="72" width="86" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="43" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Three.js</text>

        <rect x="96" y="72" width="74" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="133" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">SVG Motion</text>

        <text x="0" y="132" fill="#6880a4" font-size="9" font-weight="700">DOWNFORCE: ULTRA SMOOTH</text>
      </g>
    </g>

    <!-- Department 3: TELEMETRY // AI & DATA -->
    <g transform="translate(416, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip3"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#fcd700" font-size="10.5" font-weight="800" letter-spacing="0.1em">TELEMETRY // AI &amp; ML</text>

      <!-- Chips -->
      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="41" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">PyTorch</text>

        <rect x="92" y="0" width="78" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="131" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">OpenCV</text>

        <rect x="0" y="36" width="94" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="47" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Vision AI</text>

        <rect x="104" y="36" width="66" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="137" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">NumPy</text>

        <rect x="0" y="72" width="94" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="47" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">CUDA Accel</text>

        <rect x="104" y="72" width="66" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="137" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">LangChain</text>

        <text x="0" y="132" fill="#6880a4" font-size="9" font-weight="700">INFERENCE: 100 TFLOPS</text>
      </g>
    </g>

    <!-- Department 4: GARAGE // DEVOPS & INFRA -->
    <g transform="translate(624, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip4"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#00f0ff" font-size="10.5" font-weight="800" letter-spacing="0.1em">GARAGE // DEVOPS</text>

      <!-- Chips -->
      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="76" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="38" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Docker</text>

        <rect x="86" y="0" width="84" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="128" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Git / GitHub</text>

        <rect x="0" y="36" width="86" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="43" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Linux OS</text>

        <rect x="96" y="36" width="74" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="133" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">FastAPI</text>

        <rect x="0" y="72" width="102" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="51" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">GH Actions</text>

        <rect x="112" y="72" width="58" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="141" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">CI / CD</text>

        <text x="0" y="132" fill="#6880a4" font-size="9" font-weight="700">PIT STOP: ZERO DOWNTIME</text>
      </g>
    </g>
  </g>
</svg>"""

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Wrote {OUT_PATH}: {len(svg)} bytes")
