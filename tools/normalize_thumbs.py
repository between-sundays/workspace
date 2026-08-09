#!/usr/bin/env python3
"""
Every review image must be the full page, edge to edge.
Some renders came out with the body background around the page — crop it off.
Safe: only crops when a clear uniform border is found AND the result stays a sane page ratio.
"""
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import glob, os

TARGET = 941 / 1346          # 0.699 — the broadsheet ratio
TOL    = 26                  # per-channel tolerance for "same as the border colour"

def close(a, b, tol=TOL):
    return all(abs(int(x) - int(y)) <= tol for x, y in zip(a[:3], b[:3]))

def content_box(im):
    """Bounding box of everything that isn't the border colour."""
    w, h = im.size
    px = im.load()
    # border colour = median-ish of the four corners
    corners = [px[1,1], px[w-2,1], px[1,h-2], px[w-2,h-2]]
    bg = corners[0]
    if not all(close(c, bg, 18) for c in corners):
        return None                      # corners disagree -> probably a full-bleed page
    step = max(1, w // 500)
    left, right, top, bot = None, None, None, None
    for x in range(0, w, step):
        if any(not close(px[x, y], bg) for y in range(0, h, max(1, h // 220))):
            left = x; break
    for x in range(w - 1, -1, -step):
        if any(not close(px[x, y], bg) for y in range(0, h, max(1, h // 220))):
            right = x; break
    for y in range(0, h, step):
        if any(not close(px[x, y], bg) for x in range(0, w, max(1, w // 220))):
            top = y; break
    for y in range(h - 1, -1, -step):
        if any(not close(px[x, y], bg) for x in range(0, w, max(1, w // 220))):
            bot = y; break
    if None in (left, right, top, bot) or right <= left or bot <= top:
        return None
    return (left, top, right + 1, bot + 1)

fixed = skipped = clean = 0
for f in sorted(glob.glob("public/v*/BetweenSundays-Issue001-*.jpg") +
                glob.glob("public/v*/BetweenSundays-Issue001-*.png") +
                glob.glob("public/lab/BetweenSundays-Issue001-*.jpg") +
                glob.glob("public/lab/BetweenSundays-Issue001-*.png")):
    if "Contact-Sheet" in f or "PDF-Render" in f:
        continue
    im = Image.open(f).convert("RGB")
    W, H = im.size
    box = content_box(im)
    if not box:
        clean += 1; continue
    l, t, r, b = box
    cw, ch = r - l, b - t
    trimmed = (W - cw) + (H - ch)
    if trimmed < 12:
        clean += 1; continue                       # already essentially full bleed
    ratio = cw / ch
    if not (0.60 < ratio < 0.82):                  # refuse to butcher an odd page
        skipped += 1
        print(f"  SKIP  {os.path.basename(f):52} ratio {ratio:.3f}")
        continue
    out = im.crop(box)
    if f.lower().endswith(".jpg"):
        out.save(f, "JPEG", quality=87, optimize=True, progressive=True)
    else:
        out.save(f, "PNG", optimize=True)
    fixed += 1
    print(f"  CROP  {os.path.basename(f):52} {W}x{H} -> {cw}x{ch}")

print(f"\ncropped {fixed} · already full-bleed {clean} · skipped {skipped}")
