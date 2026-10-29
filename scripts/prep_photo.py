"""
Prepare a photo or illustration for clean ASCII conversion:
  1. remove the background (rembg or alpha channel) so the subject is isolated
  2. bilateral-smooth away noise/textures while keeping lines sharp
  3. stretch tones so skin lands near white and hair/lines stay dark
  4. darken the line work (difference-of-gaussians ridges) -- eyes, pupils,
     contours and details that plain luminance averaging washes out
  5. composite onto white and crop square around the subject

Output: source-prepped.png (grayscale), consumed by make_ascii_svg.py.

Usage:
    python scripts/prep_photo.py [input.png] [output.png]
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

LINE_WEIGHT = 0.6  # how hard drawn lines are pushed toward black


def prep_image(inp_path=INP, out_path=OUT):
    if not os.path.exists(inp_path):
        print(f"Error: {inp_path} does not exist", file=sys.stderr)
        return False

    raw_img = Image.open(inp_path)

    # 1. cut out the subject
    alpha = None
    if raw_img.mode == "RGBA":
        a = np.array(raw_img.split()[-1])
        if np.count_nonzero(a < 250) > 0.05 * a.size:
            # Already has transparent background
            cut = raw_img
            alpha = a
            rgb = np.array(cut.convert("RGB"))

    if alpha is None:
        try:
            from rembg import remove
            print("Removing background with rembg...")
            cut = remove(raw_img.convert("RGBA"))
            rgb = np.array(cut.convert("RGB"))
            alpha = np.array(cut.split()[-1])
        except Exception as e:
            print(f"rembg notice: {e}, falling back to direct luminance mask", file=sys.stderr)
            rgb = np.array(raw_img.convert("RGB"))
            gray_tmp = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
            # Create a basic subject mask if bright background
            _, alpha = cv2.threshold(gray_tmp, 240, 255, cv2.THRESH_BINARY_INV)

    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    # 2. smooth texture, keep edges
    smooth = gray
    for _ in range(3):
        smooth = cv2.bilateralFilter(smooth, 9, 40, 9)

    # 3. tone stretch over the subject only
    subj_mask = alpha > 128
    if np.count_nonzero(subj_mask) > 100:
        lo, hi = np.percentile(smooth[subj_mask], [2, 92])
        if hi <= lo:
            hi = lo + 1
        tone = np.clip((smooth.astype(np.float32) - lo) / (hi - lo), 0, 1)
    else:
        tone = smooth.astype(np.float32) / 255.0

    # 4. dark-on-light ridges -> darken
    fine = cv2.GaussianBlur(smooth, (0, 0), 1.5).astype(np.float32)
    coarse = cv2.GaussianBlur(smooth, (0, 0), 6).astype(np.float32)
    lines = np.clip((coarse - fine) / 40.0, 0, 1)
    out = np.clip(tone - LINE_WEIGHT * lines, 0, 1) * 255

    # 5. paste onto white (feathered a hair to avoid a halo), square crop
    mask = cv2.GaussianBlur(alpha.astype(np.float32) / 255.0, (0, 0), 1.0)
    out = out * mask + 255.0 * (1.0 - mask)

    ys, xs = np.where(alpha > 20)
    if len(xs) > 0 and len(ys) > 0:
        side = max(xs.max() - xs.min(), ys.max() - ys.min()) + 60
        cx, cy = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2
        canvas = np.full((side, side), 255, np.uint8)
        x0, y0 = cx - side // 2, cy - side // 2
        sx0, sy0 = max(x0, 0), max(y0, 0)
        sx1, sy1 = min(x0 + side, out.shape[1]), min(y0 + side, out.shape[0])
        canvas[sy0 - y0:sy1 - y0, sx0 - x0:sx1 - x0] = out[sy0:sy1, sx0:sx1].astype(np.uint8)
    else:
        canvas = out.astype(np.uint8)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    Image.fromarray(canvas, mode="L").save(out_path)
    print(f"wrote {out_path} with shape {canvas.shape}")
    return True


if __name__ == "__main__":
    prep_image()
