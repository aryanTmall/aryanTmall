#!/usr/bin/env python3
"""
Generate connect.svg:
Podium Finish Connect Banner with F1 Checkered Flag, Speed Streaks,
and 4 Pit Board Link Cards with nudging arrows.
"""
import os

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "connect.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="220" viewBox="0 0 860 220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Mono', monospace">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="connBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1322"/>
      <stop offset="60%" stop-color="#060912"/>
      <stop offset="100%" stop-color="#09101d"/>
    </linearGradient>

    <!-- Card Background -->
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10192e"/><stop offset="100%" stop-color="#09101e"/>
    </linearGradient>

    <!-- Arrow Nudge Animation Gradient -->
    <linearGradient id="flagCheck" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.02"/>
    </linearGradient>
  </defs>

  <style>
    .nudge-arrow { animation: arrowNudge 1.6s ease-in-out infinite; }
    @keyframes arrowNudge {
      0%, 100% { transform: translateX(0px); }
      50% { transform: translateX(6px); }
    }
    .check-wave { animation: flagWave 4s ease-in-out infinite alternate; }
    @keyframes flagWave {
      0% { opacity: 0.15; transform: skewX(-4deg); }
      100% { opacity: 0.35; transform: skewX(4deg); }
    }
    @media (prefers-reduced-motion: reduce) {
      .nudge-arrow, .check-wave { animation: none !important; }
    }
  </style>

  <!-- Frame Background -->
  <rect width="860" height="220" rx="14" fill="url(#connBg)"/>
  <rect x="0.5" y="0.5" width="859" height="219" rx="14" fill="none" stroke="#1d2d49" stroke-width="1.2"/>

  <!-- Top Red/Gold Racing Line -->
  <line x1="20" y1="1" x2="840" y2="1" stroke="#ff1801" stroke-width="2"/>
  <line x1="280" y1="1" x2="580" y2="1" stroke="#fcd700" stroke-width="2"/>

  <!-- =================================================================== -->
  <!-- LEFT: F1 PODIUM FINISH & CHECKERED FLAG CREST (x: 20, y: 20)        -->
  <!-- =================================================================== -->
  <g transform="translate(25, 20)">
    <!-- Checkered Flag Texture in background -->
    <g class="check-wave" fill="#ffffff">
      <!-- 4x4 Checkered Flag blocks -->
      <rect x="0" y="10" width="16" height="16"/>
      <rect x="32" y="10" width="16" height="16"/>
      <rect x="64" y="10" width="16" height="16"/>
      <rect x="16" y="26" width="16" height="16"/>
      <rect x="48" y="26" width="16" height="16"/>
      <rect x="0" y="42" width="16" height="16"/>
      <rect x="32" y="42" width="16" height="16"/>
      <rect x="64" y="42" width="16" height="16"/>
      <rect x="16" y="58" width="16" height="16"/>
      <rect x="48" y="58" width="16" height="16"/>
    </g>

    <!-- Podium Emblem Box -->
    <rect x="90" y="12" width="48" height="48" rx="12" fill="#ff1801"/>
    <text x="114" y="44" fill="#ffffff" font-size="28" font-weight="900" font-style="italic" text-anchor="middle">P1</text>

    <!-- Title & Subtitle -->
    <text x="0" y="96" fill="#fcd700" font-size="18" font-weight="900" font-style="italic" letter-spacing="0.06em">
      THE PODIUM
    </text>
    <text x="0" y="114" fill="#ffffff" font-size="12" font-weight="800" letter-spacing="0.1em">
      LET'S BUILD SOMETHING FAST.
    </text>
    <text x="0" y="134" fill="#8da2c0" font-size="11">
      Open for breakthrough engineering roles,
    </text>
    <text x="0" y="150" fill="#8da2c0" font-size="11">
      AI research &amp; high-scale architecture.
    </text>
    <text x="0" y="172" fill="#39d353" font-size="10.5" font-weight="800">
      ● STATUS: READY FOR RACE WEEKEND
    </text>
  </g>

  <!-- Vertical Divider -->
  <line x1="285" y1="25" x2="285" y2="195" stroke="#1d2d49" stroke-width="1" stroke-dasharray="4 6"/>

  <!-- =================================================================== -->
  <!-- RIGHT: 4 HIGH-SPEED LINK CARDS WITH NUDGING ARROWS (2x2 Grid)       -->
  <!-- =================================================================== -->
  <g transform="translate(305, 20)">
    <!-- Link Card 1: GITHUB (x: 0, y: 0) -->
    <a href="https://github.com/aryanTmall" target="_blank">
      <g transform="translate(0, 0)">
        <rect width="255" height="82" rx="10" fill="url(#cardGrad)" stroke="#253a5c" stroke-width="1.2"/>
        <circle cx="28" cy="41" r="18" fill="#060a14" stroke="#ffffff" stroke-width="1"/>
        <text x="28" y="47" fill="#ffffff" font-size="18" text-anchor="middle">🐙</text>

        <text x="56" y="34" fill="#ffffff" font-size="13" font-weight="800">GITHUB REPOSITORIES</text>
        <text x="56" y="52" fill="#8da2c0" font-size="10.5">Explore source code &amp; experiments</text>

        <g class="nudge-arrow" transform="translate(225, 41)">
          <circle cx="0" cy="0" r="10" fill="#0c1626" stroke="#ff6b00" stroke-width="1"/>
          <text x="0" y="4" fill="#ff6b00" font-size="12" font-weight="900" text-anchor="middle">→</text>
        </g>
      </g>
    </a>

    <!-- Link Card 2: LINKEDIN (x: 270, y: 0) -->
    <a href="https://linkedin.com" target="_blank">
      <g transform="translate(270, 0)">
        <rect width="255" height="82" rx="10" fill="url(#cardGrad)" stroke="#253a5c" stroke-width="1.2"/>
        <circle cx="28" cy="41" r="18" fill="#060a14" stroke="#0077b5" stroke-width="1"/>
        <text x="28" y="47" fill="#0077b5" font-size="16" font-weight="900" text-anchor="middle">in</text>

        <text x="56" y="34" fill="#ffffff" font-size="13" font-weight="800">LINKEDIN NETWORK</text>
        <text x="56" y="52" fill="#8da2c0" font-size="10.5">Professional paddock &amp; background</text>

        <g class="nudge-arrow" transform="translate(225, 41)">
          <circle cx="0" cy="0" r="10" fill="#0c1626" stroke="#00f0ff" stroke-width="1"/>
          <text x="0" y="4" fill="#00f0ff" font-size="12" font-weight="900" text-anchor="middle">→</text>
        </g>
      </g>
    </a>

    <!-- Link Card 3: PORTFOLIO (x: 0, y: 94) -->
    <a href="https://aryantmall.github.io" target="_blank">
      <g transform="translate(0, 94)">
        <rect width="255" height="82" rx="10" fill="url(#cardGrad)" stroke="#253a5c" stroke-width="1.2"/>
        <circle cx="28" cy="41" r="18" fill="#060a14" stroke="#fcd700" stroke-width="1"/>
        <text x="28" y="47" fill="#fcd700" font-size="16" text-anchor="middle">🌐</text>

        <text x="56" y="34" fill="#ffffff" font-size="13" font-weight="800">LIVE PORTFOLIO</text>
        <text x="56" y="52" fill="#8da2c0" font-size="10.5">Interactive apps, UI &amp; system labs</text>

        <g class="nudge-arrow" transform="translate(225, 41)">
          <circle cx="0" cy="0" r="10" fill="#0c1626" stroke="#fcd700" stroke-width="1"/>
          <text x="0" y="4" fill="#fcd700" font-size="12" font-weight="900" text-anchor="middle">→</text>
        </g>
      </g>
    </a>

    <!-- Link Card 4: DIRECT EMAIL (x: 270, y: 94) -->
    <a href="mailto:aryanfreefire15@gmail.com">
      <g transform="translate(270, 94)">
        <rect width="255" height="82" rx="10" fill="url(#cardGrad)" stroke="#253a5c" stroke-width="1.2"/>
        <circle cx="28" cy="41" r="18" fill="#060a14" stroke="#ff1801" stroke-width="1"/>
        <text x="28" y="47" fill="#ff1801" font-size="16" text-anchor="middle">✉️</text>

        <text x="56" y="34" fill="#ffffff" font-size="13" font-weight="800">TEAM RADIO // EMAIL</text>
        <text x="56" y="52" fill="#8da2c0" font-size="10.5">Direct line: aryanfreefire15@gmail.com</text>

        <g class="nudge-arrow" transform="translate(225, 41)">
          <circle cx="0" cy="0" r="10" fill="#0c1626" stroke="#ff1801" stroke-width="1"/>
          <text x="0" y="4" fill="#ff1801" font-size="12" font-weight="900" text-anchor="middle">→</text>
        </g>
      </g>
    </a>
  </g>
</svg>"""

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Wrote {OUT_PATH}: {len(svg)} bytes")
