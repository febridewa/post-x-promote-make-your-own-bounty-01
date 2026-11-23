#!/usr/bin/env python3
"""Make the photo for the post-x-promote-make-your-own-bounty-01 X post.

Draws a 1200x675 card with PIL: a dark plum background with a magenta glow,
a big bold headline, the subline, and make.fun's wordmark pasted in as it is
from the press pack (https://make.fun/press/manifest.json — the wordmark is
only scaled proportionally, never redrawn, recoloured, stretched or cropped).

Press assets are expected in --press-dir (default: the `press/` folder next
to this repository, downloaded from make.fun's press manifest):
  3-wordmark.png  make.fun's wordmark (white, transparent background)

Usage:
  python3 scripts/make_photo.py [--press-dir DIR] [--out FILE]
"""

import argparse
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 675

# Colours
INK_TOP = (26, 8, 30)        # deep plum, top of the gradient
INK_BOTTOM = (12, 4, 16)     # near-black plum, bottom
MAGENTA = (226, 0, 122)      # make.fun magenta glow
MAGENTA_SOFT = (160, 20, 110)
GOLD = (255, 214, 10)        # bounty gold accent
WHITE = (255, 255, 255)
MIST = (214, 196, 222)       # soft lavender-grey for the subline

FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-ExtraBold.ttf"
FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vertical_gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (w, h), top)
    overlay = Image.new("RGB", (w, h), bottom)
    mask = Image.new("L", (1, h))
    mask.putdata([round(255 * (y / (h - 1))) for y in range(h)])
    mask = mask.resize((w, h))
    return Image.composite(overlay, base, mask)


def glow(canvas, cx, cy, radius, colour, alpha):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
              fill=colour + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55))
    canvas.alpha_composite(layer)


def draw_coin(canvas, cx, cy, r):
    """A simple gold bounty coin with a $ — drawn, not a stock image."""
    d = ImageDraw.Draw(canvas, "RGBA")
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD + (255,),
              outline=(255, 255, 255, 220), width=5)
    d.ellipse([cx - r + 14, cy - r + 14, cx + r - 14, cy + r - 14],
              outline=(176, 124, 0, 255), width=3)
    f = font(FONT_BOLD, int(r * 1.15))
    d.text((cx, cy), "$", font=f, fill=(90, 60, 0, 255), anchor="mm")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    ap = argparse.ArgumentParser()
    ap.add_argument("--press-dir", default=os.path.join(repo, "..", "press"))
    ap.add_argument("--out", default=os.path.join(repo, "assets", "photo.png"))
    args = ap.parse_args()

    img = vertical_gradient((W, H), INK_TOP, INK_BOTTOM).convert("RGBA")

    # Magenta glow, top right, and a faint second glow bottom left.
    glow(img, 1010, 90, 330, MAGENTA, 110)
    glow(img, 80, 640, 260, MAGENTA_SOFT, 60)

    # Scattered faint dots, like a starfield of bounties.
    d = ImageDraw.Draw(img, "RGBA")
    for (x, y, r, a) in [(1050, 180, 5, 160), (1120, 300, 3, 120),
                         (980, 420, 4, 140), (1150, 520, 3, 100),
                         (60, 120, 3, 110), (220, 60, 4, 90)]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, a))

    # Gold coin cluster, top right.
    draw_coin(img, 1015, 185, 72)
    draw_coin(img, 1120, 300, 44)
    draw_coin(img, 930, 300, 34)

    # Headline, left aligned.
    x0 = 72
    f_head = font(FONT_BOLD, 108)
    f_sub = font(FONT_REG, 33)
    f_sub_bold = font(FONT_BOLD, 33)
    # "PUT A BOUNTY" on one line: measure and draw word by word.
    y = 78
    d.text((x0, y), "GOT A TASK?", font=f_head, fill=WHITE + (255,))
    y += 118
    d.text((x0, y), "PUT A ", font=f_head, fill=WHITE + (255,))
    w_put = d.textlength("PUT A ", font=f_head)
    d.text((x0 + w_put, y), "BOUNTY", font=f_head, fill=GOLD + (255,))
    y += 118
    d.text((x0, y), "ON IT.", font=f_head, fill=WHITE + (255,))

    # Subline.
    y += 128
    d.text((x0, y), "Describe it. Set the reward. Agents compete.",
           font=f_sub, fill=MIST + (255,))
    y += 44
    d.text((x0, y), "Best entry gets paid.", font=f_sub_bold,
           fill=WHITE + (255,))

    # Wordmark from the press pack, pasted as-is (proportional scale only).
    wm_path = os.path.join(args.press_dir, "3-wordmark.png")
    if not os.path.exists(wm_path):
        print(f"wordmark not found: {wm_path}", file=sys.stderr)
        return 1
    wm = Image.open(wm_path).convert("RGBA")
    target_w = 250
    target_h = round(wm.height * target_w / wm.width)
    wm = wm.resize((target_w, target_h), Image.LANCZOS)
    img.alpha_composite(wm, (x0, H - target_h - 34))

    # Sponsor page, bottom right.
    f_url = font(FONT_BOLD, 30)
    url = "make.fun/sponsor/new"
    d.text((W - 72 - d.textlength(url, font=f_url), H - 34 - 30),
           url, font=f_url, fill=WHITE + (255,))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    img.convert("RGB").save(args.out, "PNG")
    print(f"wrote {args.out} ({W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
