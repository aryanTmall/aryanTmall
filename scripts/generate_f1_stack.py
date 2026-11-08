#!/usr/bin/env python3
"""
Generate stack.svg:
Formula 1 & Max Verstappen #1 Tech Orbit + Telemetry Chip Grid.
Accurately reflects Aryan Mall's verified skillset:
- Core Accomplished: HTML5, CSS3, JavaScript, Python, Git
- Active Learning Roadmap: React, Next.js, C++, TypeScript, AI/ML
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
    GRID STATUS: ACTIVE BUILDER // ACCELERATING
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

    <!-- Orbit 1 Rotating Nodes: CORE FOUNDATION (HTML5 & CSS3) -->
    <g class="rot-orbit1">
      <!-- HTML5 -->
      <g transform="translate(315, 115)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#ff6b00" stroke-width="1.5"/>
        <text x="0" y="5" fill="#ff6b00" font-size="14" font-weight="900" text-anchor="middle">&lt;/&gt;</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">HTML5</text>
      </g>
      <!-- CSS3 -->
      <g transform="translate(545, 175)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#00f0ff" stroke-width="1.5"/>
        <text x="0" y="5" fill="#00f0ff" font-size="13" font-weight="900" text-anchor="middle">#CSS</text>
        <text x="0" y="27" fill="#ffffff" font-size="9" font-weight="800" text-anchor="middle">CSS3</text>
      </g>
    </g>

    <!-- Orbit 2 Rotating Nodes: LOGIC & ENGINES (JavaScript & Python) -->
    <g class="rot-orbit2">
      <!-- JavaScript -->
      <g transform="translate(230, 170)">
        <rect x="-20" y="-20" width="40" height="40" rx="10" fill="#091426" stroke="#fcd700" stroke-width="1.8"/>
        <text x="0" y="6" fill="#fcd700" font-size="16" font-weight="900" text-anchor="middle">JS</text>
        <text x="0" y="30" fill="#fcd700" font-size="9.5" font-weight="800" text-anchor="middle">JavaScript</text>
      </g>

      <!-- Python -->
      <g transform="translate(630, 120)">
        <rect x="-20" y="-20" width="40" height="40" rx="10" fill="#091426" stroke="#39d353" stroke-width="1.8"/>
        <text x="0" y="6" fill="#39d353" font-size="16" font-weight="900" text-anchor="middle">🐍</text>
        <text x="0" y="30" fill="#39d353" font-size="9.5" font-weight="800" text-anchor="middle">Python</text>
      </g>
    </g>

    <!-- Orbit 3 Rotating Nodes: ROADMAP & EXPLORATION (React, C++, AI/ML) -->
    <g class="rot-orbit3">
      <!-- React.js (Next on Grid) -->
      <g transform="translate(140, 130)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#00f0ff" stroke-width="1.5"/>
        <text x="0" y="5" fill="#00f0ff" font-size="14" font-weight="900" text-anchor="middle">⚛️</text>
        <text x="0" y="27" fill="#8da2c0" font-size="8.5" font-weight="700" text-anchor="middle">React (Roadmap)</text>
      </g>
      <!-- C++ -->
      <g transform="translate(430, 242)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#ff1801" stroke-width="1.5"/>
        <text x="0" y="5" fill="#ff1801" font-size="12" font-weight="900" text-anchor="middle">C++</text>
        <text x="0" y="27" fill="#8da2c0" font-size="8.5" font-weight="700" text-anchor="middle">C++ (Roadmap)</text>
      </g>
      <!-- AI / ML -->
      <g transform="translate(720, 160)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#0e172a" stroke="#a855f7" stroke-width="1.5"/>
        <text x="0" y="5" fill="#a855f7" font-size="14" font-weight="900" text-anchor="middle">🤖</text>
        <text x="0" y="27" fill="#8da2c0" font-size="8.5" font-weight="700" text-anchor="middle">AI/ML (Roadmap)</text>
      </g>
    </g>
  </g>

  <!-- =================================================================== -->
  <!-- BOTTOM HALF: PIT STOP TELEMETRY CHIP GRID (4 Honest Departments)    -->
  <!-- =================================================================== -->
  <g transform="translate(20, 275)">
    <!-- Department 1: WEB FOUNDATIONS // MASTERED -->
    <g transform="translate(0, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip1"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#ff6b00" font-size="10" font-weight="800" letter-spacing="0.1em">WEB CORE // READY</text>

      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="78" height="26" rx="6" fill="#080e1c" stroke="#ff6b00" stroke-width="1"/>
        <text x="39" y="17" fill="#ff6b00" font-size="11" font-weight="700" text-anchor="middle">HTML5</text>

        <rect x="88" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#00f0ff" stroke-width="1"/>
        <text x="129" y="17" fill="#00f0ff" font-size="11" font-weight="700" text-anchor="middle">CSS3</text>

        <rect x="0" y="36" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Responsive Layouts</text>

        <rect x="0" y="72" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Flexbox &amp; CSS Grid</text>

        <text x="0" y="132" fill="#39d353" font-size="9" font-weight="800">STATUS: ON TRACK // MASTERED</text>
      </g>
    </g>

    <!-- Department 2: LOGIC & SCRIPTING // ACTIVE -->
    <g transform="translate(208, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip2"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#fcd700" font-size="10" font-weight="800" letter-spacing="0.1em">LOGIC // ACTIVE</text>

      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#fcd700" stroke-width="1"/>
        <text x="41" y="17" fill="#fcd700" font-size="11" font-weight="700" text-anchor="middle">JavaScript</text>

        <rect x="90" y="0" width="80" height="26" rx="6" fill="#080e1c" stroke="#39d353" stroke-width="1"/>
        <text x="130" y="17" fill="#39d353" font-size="11" font-weight="700" text-anchor="middle">Python</text>

        <rect x="0" y="36" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">ES6+ &amp; DOM Scripting</text>

        <rect x="0" y="72" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="89" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Automation &amp; Scripts</text>

        <text x="0" y="132" fill="#39d353" font-size="9" font-weight="800">STATUS: ON TRACK // ACTIVE</text>
      </g>
    </g>

    <!-- Department 3: PIT STOP ACCELERATION // LEARNING -->
    <g transform="translate(416, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip3"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#00f0ff" font-size="10" font-weight="800" letter-spacing="0.1em">ROADMAP // IN PROGRESS</text>

      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#1d2d49" stroke-width="1"/>
        <text x="41" y="17" fill="#8da2c0" font-size="11" font-weight="700" text-anchor="middle">React.js</text>

        <rect x="90" y="0" width="80" height="26" rx="6" fill="#080e1c" stroke="#1d2d49" stroke-width="1"/>
        <text x="130" y="17" fill="#8da2c0" font-size="11" font-weight="700" text-anchor="middle">Next.js</text>

        <rect x="0" y="36" width="82" height="26" rx="6" fill="#080e1c" stroke="#1d2d49" stroke-width="1"/>
        <text x="41" y="53" fill="#8da2c0" font-size="11" font-weight="700" text-anchor="middle">TypeScript</text>

        <rect x="90" y="36" width="80" height="26" rx="6" fill="#080e1c" stroke="#1d2d49" stroke-width="1"/>
        <text x="130" y="53" fill="#8da2c0" font-size="11" font-weight="700" text-anchor="middle">C++</text>

        <rect x="0" y="72" width="170" height="26" rx="6" fill="#080e1c" stroke="#1d2d49" stroke-width="1"/>
        <text x="85" y="89" fill="#8da2c0" font-size="10.5" font-weight="700" text-anchor="middle">Full-Stack Frameworks</text>

        <text x="0" y="132" fill="#fcd700" font-size="9" font-weight="800">STATUS: TRAINING LAPS</text>
      </g>
    </g>

    <!-- Department 4: LABS & TOOLS // COLLABORATION -->
    <g transform="translate(624, 0)">
      <rect width="195" height="195" rx="12" fill="url(#chipBg)" stroke="#1f3354" stroke-width="1.2" class="glow-chip4"/>
      <path d="M0 0 L195 0 L195 30 L0 30 Z" fill="#0a1222"/>
      <line x1="0" y1="30" x2="195" y2="30" stroke="#1f3354" stroke-width="0.8"/>
      <text x="12" y="19" fill="#a855f7" font-size="10" font-weight="800" letter-spacing="0.1em">LABS // DEV TOOLS</text>

      <g transform="translate(12, 44)">
        <rect x="0" y="0" width="82" height="26" rx="6" fill="#080e1c" stroke="#39d353" stroke-width="1"/>
        <text x="41" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Git / GitHub</text>

        <rect x="90" y="0" width="80" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="130" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">VS Code</text>

        <rect x="0" y="36" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="53" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">UI / UX Prototyping</text>

        <rect x="0" y="72" width="170" height="26" rx="6" fill="#080e1c" stroke="#253a5e" stroke-width="1"/>
        <text x="85" y="89" fill="#a855f7" font-size="10.5" font-weight="700" text-anchor="middle">AI &amp; Geospatial (SIH)</text>

        <text x="0" y="132" fill="#00f0ff" font-size="9" font-weight="800">STATUS: INNOVATION R&amp;D</text>
      </g>
    </g>
  </g>
</svg>"""

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Wrote {OUT_PATH}: {len(svg)} bytes")
