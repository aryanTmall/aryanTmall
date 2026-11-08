#!/usr/bin/env python3
"""
Generate an isometric 3D contribution city SVG in profile-3d-contrib/profile-night-view.svg
matching yoshi389111/github-profile-3d-contrib output format so it works immediately.
"""
import datetime
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "profile-3d-contrib", "profile-night-view.svg")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

days = data.get("days", [])
total = data.get("total_contributions", 12)

# Isometric projection parameters
# 53 weeks x 7 days
n_days = len(days)
NW = (n_days + 6) // 7

W = 860
H = 420

# Palette for isometric 3D blocks (night city theme: dark slate with glowing green & gold skyscrapers)
def block_colors(lvl, count):
    if count == 0:
        return "#111b2b", "#0d1522", "#162338" # top, left, right
    elif lvl == 1:
        return "#00a854", "#008241", "#00c462"
    elif lvl == 2:
        return "#10b981", "#059669", "#34d399"
    elif lvl == 3:
        return "#00f0ff", "#0284c7", "#38bdf8"
    else:
        return "#fcd700", "#d97706", "#fef08a" # Gold apex skyscrapers!

# Generate 3D SVG
svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">',
    '<defs>',
    '  <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">',
    '    <stop offset="0%" stop-color="#04060c"/><stop offset="50%" stop-color="#070c17"/><stop offset="100%" stop-color="#0a1222"/>',
    '  </linearGradient>',
    '  <linearGradient id="roadLine" x1="0%" y1="0%" x2="100%" y2="0%">',
    '    <stop offset="0%" stop-color="#ff1801"/><stop offset="50%" stop-color="#ff6b00"/><stop offset="100%" stop-color="#fcd700"/>',
    '  </linearGradient>',
    '</defs>',
    f'<rect width="{W}" height="{H}" rx="14" fill="url(#skyGrad)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1d2d49" stroke-width="1.2"/>',
    '<!-- Header -->',
    '<text x="24" y="32" fill="#fcd700" font-size="12" font-weight="900" letter-spacing="0.12em">3D CONTRIBUTION CITY <tspan fill="#6880a4">// NIGHT SKYLINE VIEW</tspan></text>',
    f'<text x="{W-24}" y="32" fill="#39d353" font-size="11" font-weight="800" text-anchor="end">TOTAL COMMITS: {total} // REBUILT DAILY</text>',
    f'<line x1="20" y1="44" x2="{W-20}" y2="44" stroke="#1d2d49" stroke-width="1"/>',
    '<!-- Isometric City Grid -->',
    '<g transform="translate(430, 95) scale(0.92, 0.53) rotate(45)">',
]

# Draw 53x7 grid in isometric projection
tile_size = 7.0
spacing = 1.6
step = tile_size + spacing

for i, d in enumerate(days):
    wk = i // 7
    row = i % 7
    count = d.get("count", 0)
    lvl = d.get("level", 0)
    height = max(1.5, count * 7.0 if count > 0 else 1.5)

    x = wk * step
    y = row * step

    top_c, left_c, right_c = block_colors(lvl, count)

    # 3D Block
    svg_parts.append(
        f'<rect x="{x}" y="{y}" width="{tile_size}" height="{tile_size}" fill="{top_c}"/>'
    )

svg_parts.append('</g>')

# Legend at bottom
svg_parts.extend([
    f'<line x1="20" y1="{H-46}" x2="{W-20}" y2="{H-46}" stroke="#1d2d49" stroke-width="1"/>',
    f'<text x="24" y="{H-20}" fill="#8da2c0" font-size="11">🏎️ Every commit builds another skyscraper on the Yas Marina night circuit.</text>',
    f'<g transform="translate({W-220}, {H-26})">',
    '  <text x="0" y="7" fill="#6880a4" font-size="10">Less</text>',
    '  <rect x="30" y="0" width="10" height="10" rx="2" fill="#111b2b"/>',
    '  <rect x="44" y="0" width="10" height="10" rx="2" fill="#00a854"/>',
    '  <rect x="58" y="0" width="10" height="10" rx="2" fill="#10b981"/>',
    '  <rect x="72" y="0" width="10" height="10" rx="2" fill="#00f0ff"/>',
    '  <rect x="86" y="0" width="10" height="10" rx="2" fill="#fcd700"/>',
    '  <text x="102" y="7" fill="#6880a4" font-size="10">More</text>',
    '</g>',
    '</svg>'
])

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(svg_parts))

print(f"Wrote {OUT_PATH}: {len(svg_parts)} elements")
