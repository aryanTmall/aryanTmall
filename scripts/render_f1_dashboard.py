#!/usr/bin/env python3
"""
Render the Formula 1 & Max Verstappen FIA Super License Lanyard ID Badge + Pit Wall Telemetry Dashboard.
Outputs: id-dashboard.svg (860 x 520)
Features:
- Damped pendulum swinging lanyard badge with woven strap, titanium clasp,
  driver portrait with traveling light border, gold microchip, barcode, and holographic foil sweep.
- Pit Wall Telemetry Dashboard with 4 count-up KPI tiles, monthly lap distribution bar chart,
  and live pit radio status.
"""
import base64
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "id-dashboard.svg")
PHOTO_PATH = os.path.join(HERE, "..", "f1-avatar.png")
if not os.path.exists(PHOTO_PATH):
    PHOTO_PATH = os.path.join(HERE, "..", "source-photo.png")

with open(PHOTO_PATH, "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("ascii")

# Load real contribution stats
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

cur_streak = data.get("current_streak", {}).get("length", 0)
long_streak = data.get("longest_streak", {}).get("length", 0)
total_contribs = data.get("total_contributions", 0)
active_days = data.get("active_days", 0)
avg_per_active = data.get("avg_per_active_day", 0.0)
best_day = data.get("best_day", {})
monthly = data.get("monthly", [])

# Colors: Red Bull Racing Carbon & High-Speed Highlights
BG = "#080d18"
BG_CARD = "#0d1628"
BORDER = "#1f3354"
RB_RED = "#ff1801"
RB_GOLD = "#fcd700"
DUTCH_ORANGE = "#ff6b00"
CYAN = "#00f0ff"
TEXT_WHITE = "#ffffff"
TEXT_MUTED = "#7c93b6"

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="520" viewBox="0 0 860 520" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Mono', monospace">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="dbBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a101d"/>
      <stop offset="60%" stop-color="#05080f"/>
      <stop offset="100%" stop-color="#070c17"/>
    </linearGradient>

    <!-- Badge Background -->
    <linearGradient id="badgeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141f36"/>
      <stop offset="40%" stop-color="#0c1424"/>
      <stop offset="100%" stop-color="#080e1a"/>
    </linearGradient>

    <!-- Gold Smart Chip Gradient -->
    <linearGradient id="goldChip" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff2a3"/>
      <stop offset="40%" stop-color="#fcd700"/>
      <stop offset="80%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#996515"/>
    </linearGradient>

    <!-- Holographic Foil Sweep Gradient -->
    <linearGradient id="holoFoil" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff1801" stop-opacity="0"/>
      <stop offset="25%" stop-color="#ff6b00" stop-opacity="0.18"/>
      <stop offset="50%" stop-color="#fcd700" stop-opacity="0.25"/>
      <stop offset="75%" stop-color="#00f0ff" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0"/>
    </linearGradient>

    <!-- Laser Traveling Light Gradient -->
    <linearGradient id="travelLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff1801"/>
      <stop offset="50%" stop-color="#fcd700"/>
      <stop offset="100%" stop-color="#00f0ff"/>
    </linearGradient>

    <!-- Clip Path for Badge Photo -->
    <clipPath id="badgePhotoClip">
      <rect x="0" y="0" width="105" height="115" rx="10"/>
    </clipPath>

    <!-- Clip Path for Lanyard Badge -->
    <clipPath id="badgeCardClip">
      <rect x="0" y="0" width="290" height="395" rx="16"/>
    </clipPath>

    <!-- Subtle Dot Pattern -->
    <pattern id="dbGrid" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="9" cy="9" r="0.75" fill="#182740" opacity="0.6"/>
    </pattern>
  </defs>

  <style>
    /* Damped Pendulum Physics for Lanyard Badge */
    .lanyard-swing {{
      transform-origin: 165px 0px;
      animation: pendulum 9s ease-in-out infinite;
    }}
    @keyframes pendulum {{
      0%   {{ transform: rotate(0deg); }}
      12%  {{ transform: rotate(4.2deg); }}
      28%  {{ transform: rotate(-3.4deg); }}
      44%  {{ transform: rotate(2.2deg); }}
      60%  {{ transform: rotate(-1.4deg); }}
      76%  {{ transform: rotate(0.8deg); }}
      90%  {{ transform: rotate(-0.3deg); }}
      100% {{ transform: rotate(0deg); }}
    }}

    /* Traveling Light Border around portrait */
    .border-runner {{
      stroke-dasharray: 80 200;
      animation: runBorder 4s linear infinite;
    }}
    @keyframes runBorder {{
      from {{ stroke-dashoffset: 440; }}
      to {{ stroke-dashoffset: 0; }}
    }}

    /* Holographic Foil Sweep Animation */
    .holo-sweep {{
      animation: hSweep 5.5s ease-in-out infinite;
    }}
    @keyframes hSweep {{
      0%   {{ transform: translateX(-320px) rotate(25deg); }}
      40%  {{ transform: translateX(380px) rotate(25deg); }}
      100% {{ transform: translateX(380px) rotate(25deg); }}
    }}

    /* Bar Chart Grow Animation */
    .bar-g {{
      transform-origin: bottom;
      animation: barGrow 0.8s ease-out both;
    }}
    @keyframes barGrow {{
      from {{ transform: scaleY(0); }}
      to {{ transform: scaleY(1); }}
    }}

    .rec-pulse {{ animation: rPulse 1.2s steps(2, start) infinite; }}
    @keyframes rPulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.2; }} }}

    @media (prefers-reduced-motion: reduce) {{
      .lanyard-swing, .border-runner, .holo-sweep, .bar-g, .rec-pulse {{
        animation: none !important;
      }}
    }}
  </style>

  <!-- Outer Dashboard Canvas -->
  <rect width="860" height="520" rx="16" fill="url(#dbBg)"/>
  <rect width="860" height="520" rx="16" fill="url(#dbGrid)"/>
  <rect x="0.5" y="0.5" width="859" height="519" rx="16" fill="none" stroke="{BORDER}" stroke-width="1.2"/>

  <!-- Top Title Bar -->
  <path d="M0 0 L860 0 L860 38 L0 38 Z" fill="#070c17"/>
  <line x1="0" y1="38" x2="860" y2="38" stroke="#1d2d49" stroke-width="1"/>
  <circle cx="20" cy="19" r="4.5" fill="#ff1801"/>
  <circle cx="36" cy="19" r="4.5" fill="#fcd700"/>
  <circle cx="52" cy="19" r="4.5" fill="#39d353"/>

  <text x="74" y="23" fill="#ff6b00" font-size="11.5" font-weight="800" letter-spacing="0.14em">
    FIA SUPER LICENSE <tspan fill="#6880a4">// ORACLE RED BULL RACING PADDOCK PASS</tspan>
  </text>
  <text x="836" y="23" fill="#39d353" font-size="11" font-weight="700" text-anchor="end">
    FIA ACCREDITED // 2026 SEASON
  </text>

  <!-- =================================================================== -->
  <!-- LEFT: SWINGING FIA LANYARD BADGE (Pendulum physics)                 -->
  <!-- =================================================================== -->
  <g class="lanyard-swing">
    <!-- Woven Lanyard Strap from top (x: 165) -->
    <path d="M 152 0 L 152 50 L 178 50 L 178 0 Z" fill="#0c1626" stroke="#253a5e" stroke-width="0.8"/>
    <!-- Red Bull Racing stripe on lanyard -->
    <line x1="165" y1="0" x2="165" y2="50" stroke="#ff1801" stroke-width="3"/>
    <line x1="162" y1="0" x2="162" y2="50" stroke="#fcd700" stroke-width="1"/>

    <!-- Metallic Clasp & Lanyard Clip -->
    <g transform="translate(165, 52)">
      <rect x="-14" y="0" width="28" height="12" rx="3" fill="#3a4b6b" stroke="#7186a8" stroke-width="1"/>
      <ellipse cx="0" cy="16" rx="8" ry="6" fill="none" stroke="#7186a8" stroke-width="2.5"/>
      <rect x="-4" y="19" width="8" height="10" rx="2" fill="#50668a"/>
    </g>

    <!-- Badge Card Container (x: 20, y: 78, w: 290, h: 395) -->
    <g transform="translate(20, 78)">
      <!-- Badge Drop Shadow & Base -->
      <rect width="290" height="395" rx="16" fill="url(#badgeBg)"/>
      <rect x="0.5" y="0.5" width="289" height="394" rx="16" fill="none" stroke="#ff1801" stroke-width="1.4" stroke-opacity="0.8"/>

      <!-- Inner Badge Graphic Clip Container -->
      <g clip-path="url(#badgeCardClip)">
        <!-- Top Badge Header: Holographic Band -->
        <rect width="290" height="42" fill="#ff1801"/>
        <text x="145" y="18" fill="#ffffff" font-size="11" font-weight="900" letter-spacing="0.14em" text-anchor="middle">
          FIA FORMULA ONE WORLD CHAMPIONSHIP
        </text>
        <text x="145" y="32" fill="#fcd700" font-size="9" font-weight="800" letter-spacing="0.12em" text-anchor="middle">
          ORACLE RED BULL RACING // SUPER LICENSE
        </text>

        <!-- Driver Photo Frame (w: 105, h: 115) -->
        <g transform="translate(18, 56)">
          <rect width="105" height="115" rx="10" fill="#04070f"/>
          <!-- Embedded Photo -->
          <image href="data:image/png;base64,{photo_b64}" width="105" height="115" preserveAspectRatio="xMidYMid slice" clip-path="url(#badgePhotoClip)"/>
          <!-- Traveling Laser Light Border -->
          <rect width="105" height="115" rx="10" fill="none" stroke="url(#travelLight)" stroke-width="2.5" class="border-runner"/>
        </g>

        <!-- Right of Photo: Gold Chip & Driver Info -->
        <g transform="translate(136, 56)">
          <!-- Gold Smart Chip (34x28) -->
          <rect width="36" height="28" rx="5" fill="url(#goldChip)" stroke="#b8860b" stroke-width="1"/>
          <!-- Chip Circuit Lines -->
          <line x1="0" y1="9" x2="36" y2="9" stroke="#7a5200" stroke-width="0.7"/>
          <line x1="0" y1="19" x2="36" y2="19" stroke="#7a5200" stroke-width="0.7"/>
          <line x1="18" y1="0" x2="18" y2="28" stroke="#7a5200" stroke-width="0.7"/>
          <circle cx="18" cy="14" r="3.5" fill="#7a5200"/>

          <!-- Driver Number #1 Badge -->
          <g transform="translate(48, 0)">
            <rect width="32" height="28" rx="5" fill="#ff1801"/>
            <text x="16" y="20" fill="#ffffff" font-size="18" font-weight="900" font-style="italic" text-anchor="middle">1</text>
          </g>

          <!-- License Tier & Category -->
          <text x="0" y="48" fill="#6880a4" font-size="9" font-weight="700">LICENSE CLASS</text>
          <text x="0" y="62" fill="#fcd700" font-size="12" font-weight="900">FIA GRADE 1-A</text>

          <text x="0" y="80" fill="#6880a4" font-size="9" font-weight="700">DRIVER ACCRED</text>
          <text x="0" y="94" fill="#00f0ff" font-size="11" font-weight="800">VER-01 // AM-01</text>
        </g>

        <!-- Driver Full Name & Role -->
        <g transform="translate(18, 192)">
          <text x="0" y="0" fill="#ffffff" font-size="19" font-weight="900" font-style="italic" letter-spacing="0.04em">
            ARYAN MALL
          </text>
          <text x="0" y="18" fill="#fcd700" font-size="11" font-weight="800" letter-spacing="0.08em">
            WEB CRAFTER &amp; CS EXPLORER
          </text>
          <text x="0" y="32" fill="#8da2c0" font-size="10" font-weight="600">
            Sushant University // SIH 2026 Team Lead
          </text>
        </g>

        <!-- Paddock Club Access VIP Ribbon -->
        <g transform="translate(18, 240)">
          <rect width="254" height="34" rx="8" fill="#091322" stroke="#253a5c" stroke-width="1"/>
          <!-- Access Indicator -->
          <circle cx="18" cy="17" r="4.5" fill="#39d353" class="rec-pulse"/>
          <text x="32" y="21" fill="#ffffff" font-size="10.5" font-weight="800" letter-spacing="0.1em">
            ALL ACCESS // PIT WALL &amp; GARAGE
          </text>
          <rect x="206" y="8" width="38" height="18" rx="4" fill="#ff1801"/>
          <text x="225" y="21" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">2026</text>
        </g>

        <!-- High-Precision Barcode -->
        <g transform="translate(18, 292)">
          <rect width="254" height="42" rx="6" fill="#04060e" stroke="#1d2d49" stroke-width="0.8"/>
          <!-- Barcode Bars -->
          <g transform="translate(14, 6)" fill="#ffffff">
            <rect x="0" width="3" height="22"/><rect x="5" width="1.5" height="22"/><rect x="8" width="4" height="22"/>
            <rect x="15" width="2" height="22"/><rect x="20" width="1" height="22"/><rect x="23" width="5" height="22"/>
            <rect x="31" width="2" height="22"/><rect x="36" width="3.5" height="22"/><rect x="42" width="1.5" height="22"/>
            <rect x="46" width="4" height="22"/><rect x="53" width="2" height="22"/><rect x="58" width="1" height="22"/>
            <rect x="62" width="6" height="22"/><rect x="71" width="2" height="22"/><rect x="76" width="3" height="22"/>
            <rect x="82" width="4" height="22"/><rect x="89" width="1.5" height="22"/><rect x="93" width="3" height="22"/>
            <rect x="99" width="2" height="22"/><rect x="104" width="5" height="22"/><rect x="112" width="2" height="22"/>
            <rect x="117" width="3.5" height="22"/><rect x="123" width="1.5" height="22"/><rect x="127" width="4" height="22"/>
            <rect x="134" width="2" height="22"/><rect x="139" width="1" height="22"/><rect x="143" width="6" height="22"/>
            <rect x="152" width="2" height="22"/><rect x="157" width="3" height="22"/><rect x="163" width="4" height="22"/>
            <rect x="170" width="1.5" height="22"/><rect x="174" width="3" height="22"/><rect x="180" width="2" height="22"/>
            <rect x="185" width="5" height="22"/><rect x="193" width="2" height="22"/><rect x="198" width="3.5" height="22"/>
            <rect x="204" width="1.5" height="22"/><rect x="208" width="4" height="22"/><rect x="215" width="2" height="22"/>
            <rect x="220" width="4" height="22"/>
          </g>
          <text x="127" y="37" fill="#6880a4" font-size="8.5" font-weight="700" letter-spacing="0.22em" text-anchor="middle">
            * FIA-F1-2026-ARYAN-VER1-01 *
          </text>
        </g>

        <!-- Bottom Security Strip -->
        <rect y="352" width="290" height="43" fill="#060a14"/>
        <text x="18" y="376" fill="#6880a4" font-size="9" font-weight="700">
          MAX ATTACK // NO LIFT NO GIFT
        </text>
        <text x="272" y="376" fill="#fcd700" font-size="9" font-weight="900" text-anchor="end">
          DUTCH GP #1
        </text>

        <!-- Holographic Foil Sweep Sheen -->
        <rect y="-50" width="120" height="500" fill="url(#holoFoil)" class="holo-sweep"/>
      </g>
    </g>
  </g>

  <!-- =================================================================== -->
  <!-- RIGHT: RED BULL RACING PIT WALL TELEMETRY DASHBOARD (x: 335, y: 55) -->
  <!-- =================================================================== -->
  <g transform="translate(335, 55)">
    <!-- Dashboard Outer Frame -->
    <rect width="505" height="440" rx="14" fill="{BG_CARD}" stroke="{BORDER}" stroke-width="1.2"/>

    <!-- Dashboard Title Banner -->
    <g transform="translate(18, 22)">
      <text x="0" y="0" fill="#fcd700" font-size="13" font-weight="900" letter-spacing="0.12em">
        PIT WALL TELEMETRY <tspan fill="#6880a4">// REAL-TIME DATA STREAM</tspan>
      </text>
    </g>

    <!-- 4 KPI Telemetry Tiles (2x2 Grid) -->
    <!-- Tile 1: PODIUM STREAK -->
    <g transform="translate(18, 38)">
      <rect width="226" height="82" rx="10" fill="#080e1c" stroke="#1c2d4a" stroke-width="1"/>
      <text x="14" y="22" fill="#6880a4" font-size="10" font-weight="800">PODIUM STREAK (DAYS)</text>
      <text x="14" y="58" fill="#39d353" font-size="34" font-weight="900">{cur_streak}</text>
      <text x="65" y="56" fill="#6880a4" font-size="13" font-weight="700">days active</text>
      <text x="14" y="74" fill="#39d353" font-size="9.5" font-weight="700">● 100% ON RACE PACE</text>
    </g>

    <!-- Tile 2: CAREER LAPS (COMMITS) -->
    <g transform="translate(260, 38)">
      <rect width="226" height="82" rx="10" fill="#080e1c" stroke="#1c2d4a" stroke-width="1"/>
      <text x="14" y="22" fill="#6880a4" font-size="10" font-weight="800">TOTAL CAREER COMMITS</text>
      <text x="14" y="58" fill="#fcd700" font-size="34" font-weight="900">{total_contribs}</text>
      <text x="75" y="56" fill="#6880a4" font-size="13" font-weight="700">commits</text>
      <text x="14" y="74" fill="#ff6b00" font-size="9.5" font-weight="700">AUTO-REFRESHED DAILY</text>
    </g>

    <!-- Tile 3: ACTIVE GRAND PRIX DAYS -->
    <g transform="translate(18, 130)">
      <rect width="226" height="82" rx="10" fill="#080e1c" stroke="#1c2d4a" stroke-width="1"/>
      <text x="14" y="22" fill="#6880a4" font-size="10" font-weight="800">ACTIVE RACE DAYS</text>
      <text x="14" y="58" fill="#00f0ff" font-size="34" font-weight="900">{active_days}</text>
      <text x="55" y="56" fill="#6880a4" font-size="13" font-weight="700">race sessions</text>
      <text x="14" y="74" fill="#00f0ff" font-size="9.5" font-weight="700">CONSISTENT TRAJECTORY</text>
    </g>

    <!-- Tile 4: BEST LAP (BEST DAY) -->
    <g transform="translate(260, 130)">
      <rect width="226" height="82" rx="10" fill="#080e1c" stroke="#1c2d4a" stroke-width="1"/>
      <text x="14" y="22" fill="#6880a4" font-size="10" font-weight="800">FASTEST LAP (BEST DAY)</text>
      <text x="14" y="58" fill="#ff1801" font-size="34" font-weight="900">{best_day.get("count", 0)}</text>
      <text x="55" y="56" fill="#6880a4" font-size="13" font-weight="700">commits in 1 day</text>
      <text x="14" y="74" fill="#fcd700" font-size="9.5" font-weight="700">RECORD: {best_day.get("date", "2026-10-29")}</text>
    </g>

    <!-- Monthly Commits / Lap Distribution Bar Chart -->
    <g transform="translate(18, 224)">
      <rect width="468" height="142" rx="10" fill="#080e1c" stroke="#1c2d4a" stroke-width="1"/>
      <text x="14" y="22" fill="#6880a4" font-size="10" font-weight="800">MONTHLY COMMIT LAP DISTRIBUTION (LAST 12 MONTHS)</text>

      <!-- Bar Chart Plot Area (l: 18, r: 450, bot: 116, top: 38) -->
      <g transform="translate(0, 0)">'''

# Generate Bar Chart Rectangles
chart_left, chart_right = 16, 452
chart_bot, chart_top = 114, 40
available_w = chart_right - chart_left
n_months = len(monthly) if monthly else 12
slot_w = available_w / n_months
bar_w = slot_w * 0.65
peak_val = max([m.get("total", 0) for m in monthly] or [1]) or 1

bars_xml = []
for i, m in enumerate(monthly):
    total = m.get("total", 0)
    month_str = m.get("month", "")
    mon_name = datetime.date.fromisoformat(month_str + "-01").strftime("%b")[0] if month_str else str(i)
    h = max(3.0, (chart_bot - chart_top) * total / peak_val)
    bx = chart_left + i * slot_w + (slot_w - bar_w) / 2
    by = chart_bot - h
    fill_color = RB_GOLD if total == peak_val and total > 0 else (RB_RED if total > 0 else "#16233b")

    bars_xml.append(
        f'<rect class="bar-g" x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{h:.1f}" rx="2" fill="{fill_color}" style="animation-delay:{0.1*i:.2f}s"/>'
    )
    bars_xml.append(
        f'<text x="{bx + bar_w/2:.1f}" y="{chart_bot + 16}" fill="{TEXT_MUTED}" font-size="10" font-weight="700" text-anchor="middle">{mon_name}</text>'
    )
    if total == peak_val and total > 0:
        bars_xml.append(
            f'<text x="{bx + bar_w/2:.1f}" y="{by - 6:.1f}" fill="{RB_GOLD}" font-size="11" font-weight="900" text-anchor="middle">{total}</text>'
        )

svg_content += "".join(bars_xml)

svg_content += f'''
      </g>
    </g>

    <!-- Bottom Pit Wall Radio / Live Telemetry Status Ticker -->
    <g transform="translate(18, 376)">
      <rect width="468" height="48" rx="8" fill="#060b16" stroke="#253a5c" stroke-width="1"/>
      <path d="M0 0 L4 0 L4 48 L0 48 Z" fill="#ff1801"/>

      <!-- Radio Icon -->
      <text x="14" y="20" fill="#fcd700" font-size="10" font-weight="800">PIT RADIO 📻</text>
      <text x="100" y="20" fill="#39d353" font-size="10" font-weight="800">STRAT 1 // ENGINE HEALTH: 100%</text>

      <text x="14" y="38" fill="#ffffff" font-size="11" font-style="italic" font-weight="600">
        "Max, box this lap, confirm." — <tspan fill="#fcd700">"Simply Lovely, mate! The car is on rails."</tspan>
      </text>
    </g>
  </g>
</svg>'''

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Wrote {OUT_PATH}: {len(svg_content)} bytes")
