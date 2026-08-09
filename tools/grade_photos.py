#!/usr/bin/env python3
"""Grade the CC0 photo set into one Between Sundays photo desk."""
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
Image.MAX_IMAGE_PIXELS = None
import json, os, random

BASE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(BASE, "photos")
OUT = os.path.join(P, "graded")
os.makedirs(OUT, exist_ok=True)
picks = json.load(open(os.path.join(P, "picks.json")))
random.seed(28)

INK   = (0x17, 0x10, 0x0d)
CREAM = (0xf8, 0xf3, 0xe6)
NIGHT = (0x0d, 0x14, 0x24)
BLUE  = (0x14, 0x36, 0x53)
PALE  = (0xdf, 0xe8, 0xef)
WARM  = (0x3a, 0x2a, 0x12)
SAND  = (0xf6, 0xef, 0xdd)

def duotone(im, dark, light, strength=1.0):
    g = ImageOps.grayscale(im)
    lut = []
    for c in range(3):
        lut += [int(dark[c] + (light[c] - dark[c]) * (i / 255)) for i in range(256)]
    d = ImageOps.colorize(g, dark, light)
    return Image.blend(im.convert("RGB"), d, strength)

def grain(im, amount=10):
    w, h = im.size
    n = Image.effect_noise((w, h), amount).convert("L").convert("RGB")
    return Image.blend(im, n, 0.055)

def crop_to(im, ratio):
    w, h = im.size
    tw, th = (w, int(w / ratio)) if w / h > ratio else (int(h * ratio), h)
    return im.crop(((w - tw) // 2, (h - th) // 2, (w - tw) // 2 + tw, (h - th) // 2 + th))

def prep(name, ratio, mode, width=2000, contrast=1.0, bright=1.0):
    src = os.path.join(P, "raw", picks[name]["file"])
    im = Image.open(src).convert("RGB")
    im = crop_to(im, ratio)
    if im.width > width:
        im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
    if contrast != 1.0: im = ImageEnhance.Contrast(im).enhance(contrast)
    if bright   != 1.0: im = ImageEnhance.Brightness(im).enhance(bright)
    if   mode == "night":  im = duotone(im, NIGHT, PALE, .85)
    elif mode == "bw":     im = duotone(im, INK, CREAM, 1.0)
    elif mode == "blue":   im = duotone(im, BLUE, CREAM, .8)
    elif mode == "warm":   im = duotone(im, WARM, SAND, .7)
    elif mode == "rich":   im = ImageEnhance.Color(im).enhance(1.12)
    im = grain(im)
    dst = os.path.join(OUT, f"{name}.jpg")
    im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"  {name:20} {mode:6} {im.size[0]}x{im.size[1]}")

# cover + heroes ------------------------------------------------------------
prep("cover_garage",     0.72, "night", 1900, 1.25, .92)   # the cover
prep("dawn_sky",         0.72, "rich",  1700, 1.10, 1.0)   # back cover
prep("road_sunrise_lot", 1.60, "rich",  2000, 1.12, 1.0)   # sunrise over a parking lot
prep("road_bridge_dawn", 1.60, "night", 1800, 1.15, .95)

# the photo desk — one consistent B&W treatment ------------------------------
for n, r in [("laundromat_bw",1.5),("hall_lockers",1.5),("underpass",1.5),
             ("terminal_figure",0.78),("terminal_dusk",1.5),("motel_room",1.4),
             ("laundromat_fluor",1.6),("stairs_concrete",1.0),("porch_light",0.72)]:
    prep(n, r, "bw", 1500, 1.18, 1.0)

# sports --------------------------------------------------------------------
prep("seats_red",   1.5, "rich", 1800, 1.15)
prep("seats_green", 1.5, "rich", 1600, 1.10)
prep("track_1500",  1.6, "rich", 1800, 1.12)

# objects -------------------------------------------------------------------
prep("stone_hand",  1.35, "warm", 1700, 1.20)
prep("stone_river", 1.50, "warm", 1500, 1.15)

# tables / alarm ------------------------------------------------------------
prep("table_warm",       1.55, "rich", 1700, 1.10)
prep("table_long_night", 0.78, "rich", 1400, 1.12)
prep("alarm_firebox",    1.0,  "rich", 1400, 1.15)
prep("alarm_breakglass", 1.35, "rich", 1500, 1.12)

# credits file for the colophon
cred = [{"name":k,"title":v["title"],"license":v["license"],
         "creator":v["creator"],"source":v["source"]} for k,v in picks.items()]
json.dump(cred, open(os.path.join(P,"credits.json"),"w"), indent=1)
print(f"\n{len(picks)} graded -> photos/graded/   (all CC0 / public domain)")
