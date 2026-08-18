#!/usr/bin/env python3
"""
The press. Turns a flat digital render into something that behaves like ink on
newsprint — because the AI tell is not taste, it is the absence of physical
process. See brain/print-craft.md.

Pipeline: separate into spot inks -> halftone each at its own screen angle ->
misregister -> overprint (multiply, so crossings make a third colour) -> lay on
a paper substrate with fibre, mottle and show-through.
"""
import numpy as np
from PIL import Image, ImageFilter
import math

# ---------------------------------------------------------------- substrate
def paper(w, h, seed=7, tone=(247, 242, 231), roughness=1.0):
    """Newsprint: warm, uneven, fibrous. Never #ffffff."""
    rng = np.random.default_rng(seed)
    base = np.zeros((h, w, 3), np.float32)
    base[:, :] = tone
    # long fibres, mostly horizontal, from the paper machine
    fib = rng.normal(0, 1, (h, w)).astype(np.float32)
    fib = np.array(Image.fromarray(((fib - fib.min()) / (np.ptp(fib) + 1e-6) * 255)
                                   .astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6)), np.float32)
    fib = (fib - fib.mean()) / 255.0
    fib_h = np.array(Image.fromarray(((rng.normal(0, 1, (h, w)) * 40 + 128).clip(0, 255)).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(radius=0.4)), np.float32)
    fib_h = (fib_h - fib_h.mean()) / 255.0
    # slow mottle — where the pulp is thicker the sheet is darker
    small = rng.normal(0, 1, (max(2, h // 60), max(2, w // 60))).astype(np.float32)
    mot = np.array(Image.fromarray(((small - small.min()) / (np.ptp(small) + 1e-6) * 255).astype(np.uint8))
                   .resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(18)), np.float32)
    mot = (mot - mot.mean()) / 255.0
    grain = (fib * 3.0 + fib_h * 2.0 + mot * 7.0) * roughness
    for c in range(3):
        base[:, :, c] = np.clip(base[:, :, c] + grain * (1.0 + 0.15 * c), 0, 255)
    return base

# ---------------------------------------------------------------- separation
def separate(img, inks, paper_tone=(247, 242, 231)):
    """Split an RGB render into per-ink density maps (0..1) by nearest-ink match."""
    a = np.asarray(img.convert("RGB"), np.float32)
    h, w, _ = a.shape
    pt = np.array(paper_tone, np.float32)
    ink_arr = [np.array(i, np.float32) for i in inks]
    d_paper = np.linalg.norm(a - pt, axis=2)
    dists = np.stack([np.linalg.norm(a - k, axis=2) for k in ink_arr], axis=0)
    nearest = np.argmin(dists, axis=0)
    out = []
    for i in range(len(inks)):
        # Density is measured against THIS ink's own full strength, not against black.
        # Otherwise a light ink (a red) never reaches 100% and its type never prints solid.
        full = max(np.linalg.norm(pt - ink_arr[i]), 1.0)
        total = np.clip(d_paper / full, 0, 1)
        m = (nearest == i).astype(np.float32)
        # soften ownership so edges of one ink bleed slightly into the next
        m = np.array(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7)), np.float32) / 255.0
        out.append(np.clip(total * m, 0, 1))
    return out

# ---------------------------------------------------------------- halftone
def halftone(dens, angle_deg, cell=5.0, gain=0.16, jitter=0.35, seed=3):
    """Amplitude-modulated dot screen. Real rosettes, real dot gain."""
    h, w = dens.shape
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t = math.radians(angle_deg)
    u = (xx * math.cos(t) + yy * math.sin(t)) / cell
    v = (-xx * math.sin(t) + yy * math.cos(t)) / cell
    # distance from the centre of each screen cell
    du = (u - np.floor(u) - 0.5)
    dv = (v - np.floor(v) - 0.5)
    r = np.sqrt(du * du + dv * dv) * 2.0
    d = np.clip(dens + gain * dens * (1 - dens) * 2.0, 0, 1)   # dot gain
    radius = np.sqrt(d) * 1.06
    # ink is never perfectly even: per-pixel noise starves some dots
    n = rng.normal(0, jitter * 0.06, (h, w)).astype(np.float32)
    dot = np.clip((radius + n - r) * cell * 1.6, 0, 1)
    dot = np.array(Image.fromarray((dot * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(0.45)), np.float32) / 255.0
    return np.clip(dot * np.clip(d * 1.25, 0, 1) ** 0.65, 0, 1)

# ---------------------------------------------------------------- press run
def shift(layer, dx, dy):
    return np.roll(np.roll(layer, dy, axis=0), dx, axis=1)

def press(render, inks, angles=None, cell=5.0, misreg=None, seed=7,
          paper_tone=(247, 242, 231), roughness=1.0, solid_at=0.86):
    """solid_at: density above this prints as LINE WORK (solid ink), not screened.
    This is how real newspapers work — type and rules are line art at 100%; only
    photographs and tints get a halftone screen. Screening the type is the single
    most common way a simulation gives itself away."""
    """Run a rendered page through the press. Returns a PIL image."""
    img = render.convert("RGB")
    w, h = img.size
    sheet = paper(w, h, seed=seed, tone=paper_tone, roughness=roughness)
    dens = separate(img, inks, paper_tone)
    if angles is None:
        angles = [15, 75, 45, 0][:len(inks)]
    if misreg is None:
        rng = np.random.default_rng(seed + 1)
        misreg = [(int(rng.integers(-2, 3)), int(rng.integers(-2, 3))) for _ in inks]
        misreg[0] = (0, 0)
    for i, (d, ink) in enumerate(zip(dens, inks)):
        line = np.clip((d - solid_at) / (1.0 - solid_at), 0, 1)      # type, rules, solids
        tone = np.where(d >= solid_at, 0.0, d)                        # photos, tints, fields
        scr = halftone(tone, angles[i % len(angles)], cell=cell, seed=seed + i * 5)
        # ink on newsprint spreads a little at the edge of solid areas
        edge = np.array(Image.fromarray((line * 255).astype(np.uint8))
                        .filter(ImageFilter.MaxFilter(3)), np.float32) / 255.0
        line = np.clip(line * 0.94 + edge * 0.10, 0, 1)
        scr = np.clip(scr + line, 0, 1)
        dx, dy = misreg[i]
        scr = shift(scr, dx, dy)
        k = np.array(ink, np.float32).reshape(1, 1, 3)
        a = scr[:, :, None]
        # transparent ink: multiply toward the ink colour
        sheet = sheet * (1 - a) + (sheet * (k / 255.0)) * a
    return Image.fromarray(np.clip(sheet, 0, 255).astype(np.uint8))


# ---------------------------------------------------------------- photographs
def duotone(img, dark, light, angles=(45, 15), cell=5.0, seed=7,
            paper_tone=(247, 242, 231), roughness=1.0, contrast=1.0, knockout=0.93):
    """Press a PHOTOGRAPH.

    Flat art separates by colour; a photograph separates by TONE. Luminance maps
    to ink density directly — shadows carry the dark ink, midtones carry the
    second. Anything brighter than `knockout` is treated as reversed-out type and
    left as bare paper, which is how white text on a dark photo actually prints.
    """
    a = np.asarray(img.convert("RGB"), np.float32)
    h, w, _ = a.shape
    lum = (0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]) / 255.0
    ko = (lum >= knockout).astype(np.float32)           # reversed-out type
    ko = np.array(Image.fromarray((ko * 255).astype(np.uint8))
                  .filter(ImageFilter.GaussianBlur(0.4)), np.float32) / 255.0
    d = np.clip((1.0 - lum - 0.5) * contrast + 0.5, 0, 1)
    d = d * (1.0 - ko)
    sheet = paper(w, h, seed=seed, tone=paper_tone, roughness=roughness)
    # dark ink carries the shadows, second ink lifts the midtones
    d_dark = np.clip((d - 0.28) / 0.72, 0, 1) ** 0.9
    d_mid = np.clip(d * 1.15, 0, 1) ** 1.5 * 0.55
    for i, (dens, ink) in enumerate(((d_mid, light), (d_dark, dark))):
        scr = halftone(dens, angles[i % len(angles)], cell=cell, seed=seed + i * 7)
        if i: scr = shift(scr, 1, -1)                   # the register slips
        k = np.array(ink, np.float32).reshape(1, 1, 3)
        al = scr[:, :, None]
        sheet = sheet * (1 - al) + (sheet * (k / 255.0)) * al
    return Image.fromarray(np.clip(sheet, 0, 255).astype(np.uint8))
