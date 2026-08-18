#!/usr/bin/env python3
"""I AM WITH YOU — the labelled crowd.

Usage: python3 tools/build_iamwithyou.py public/plates/<plate>.png
Computes label positions from the photograph's own negative space, sets the type
in Chrome, then runs the whole page through the press.
"""
import os, sys, json, subprocess, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import label_space, press

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLATE = sys.argv[1] if len(sys.argv) > 1 else None
OUT = f"{B}/public/press2"
os.makedirs(OUT, exist_ok=True)
W, H = 941, 1346

# what people in the photograph are carrying — set light, lower case
NOW = ["on the way to a scan","has not told anyone yet","forty minutes from home",
 "praying without saying so","first day back","carrying it for someone else",
 "still deciding","running late again","waiting on a call","in the middle of it"]
# and the fourteen times the promise was made — set in caps, same size
P = json.load(open(f"{B}/public/data/iamwithyou.json"))
THEN = [(p["ref"], p["who"], p["what"]) for p in P]

def build(plate_path):
    plate = Image.open(plate_path).convert("RGB")
    pw, ph = plate.size
    # cover-fit the plate to the page
    sc = max(W / pw, H / ph)
    plate = plate.resize((int(pw * sc), int(ph * sc)), Image.LANCZOS)
    x0 = (plate.width - W) // 2; y0 = (plate.height - H) // 2
    plate = plate.crop((x0, y0, x0 + W, y0 + H))
    plate.save(f"{OUT}/_plate.png")

    # a label is measured at ~5.6px/char at 12.5px Inter; the promise block is wider
    def wid(s, px=5.6): return int(px * len(s)) + 14
    boxes = [(min(wid(t), 300), 26) for t in NOW]
    boxes += [(min(wid(f"{r} · to {w}, {what}", 4.4), 360), 40) for r, w, what in THEN[:8]]
    KEEPOUT = [(0, 0, W, 74),            # folio strip and its rule
               (0, H - 250, W, 250),     # headline, deck and credit
               (W - 40, 0, 40, H)]       # right trim — nothing may run off the edge
    pos = label_space.place(plate, boxes, margin=30, seed=9, keepout=KEEPOUT,
                            prefer_dark=1.35)

    labs = []
    for i, t in enumerate(NOW):
        x, y = pos[i]
        labs.append(f'<div class="now" style="left:{x}px;top:{y}px">{t}</div>')
    for j, (r, w, what) in enumerate(THEN[:8]):
        x, y = pos[len(NOW) + j]
        labs.append(f'''<div class="then" style="left:{x}px;top:{y}px">
          <b>I AM WITH YOU</b><span>{r} &nbsp;·&nbsp; to {w}, {what}</span></div>''')

    html = f"""<!doctype html><html><head><meta charset="utf-8"/>
<meta name="bible-source" content="Genesis 28:15 (NLT)"/>
<meta name="style-system" content="darkroom"/>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Newsreader:opsz,wght@6..72,400&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#0e0d0c}}
.plate{{position:absolute;inset:0;width:{W}px;height:{H}px;object-fit:cover}}
.now{{position:absolute;font-family:'Inter',sans-serif;font-size:13.5px;font-weight:500;
 color:#fff;letter-spacing:.02em;white-space:nowrap}}
.then{{position:absolute;white-space:nowrap}}
.then b{{display:block;font-family:'Inter',sans-serif;font-size:13px;font-weight:800;
 letter-spacing:.16em;color:#fff}}
.then span{{display:block;font-family:'Inter',sans-serif;font-size:10.5px;font-weight:600;
 letter-spacing:.04em;color:#fff;margin-top:2px}}
.folio{{position:absolute;left:44px;right:44px;top:30px;display:flex;
 font-family:'Inter',sans-serif;font-size:10px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;color:rgba(255,255,255,.82);z-index:5}}
.rule{{position:absolute;left:44px;right:44px;top:52px;height:1px;background:rgba(255,255,255,.4);z-index:5}}
.hed{{position:absolute;left:44px;bottom:150px;font-family:'Inter',sans-serif;
 font-size:44px;font-weight:800;letter-spacing:-.01em;line-height:1;color:#fff;
 z-index:5}}
.dek{{position:absolute;left:44px;right:300px;bottom:96px;font-family:'Newsreader',serif;
 font-size:16px;line-height:1.45;color:#fff;z-index:5}}
.src{{position:absolute;right:44px;bottom:38px;font-family:'Inter',sans-serif;font-size:9px;
 font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.6);z-index:5}}
</style></head><body><div class="page">
 <img class="plate" src="_plate.png"/>
 <div class="folio"><span>15</span><span style="flex:1"></span>
  <span>The place you almost walked past</span><span style="flex:1"></span>
  <span>Between Sundays · Issue 001</span></div>
 <div class="rule"></div>
 {''.join(labs)}
 <div class="hed">Fourteen times, to somebody<br/>in the middle of something.</div>
 <div class="dek">Every one of them was said to a person on their way somewhere, mid-situation,
  not at the end of it. None of them were said to somebody who had earned it.</div>
 <div class="src">Scripture: Genesis 28:15 and thirteen others, NLT</div>
</div></body></html>"""
    open(f"{OUT}/iamwithyou.html", "w").write(html)

    CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    uid = uuid.uuid4().hex[:8]
    pdf = f"{OUT}/_i{uid}.pdf"
    subprocess.run([CH, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=9000", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf}", "--no-margins", f"file://{OUT}/iamwithyou.html"],
        capture_output=True, timeout=420)
    subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1", pdf, f"{OUT}/_i{uid}"],
        capture_output=True, timeout=420)
    shot = f"{OUT}/_i{uid}-1.png"
    if not os.path.exists(shot):
        print("render failed"); return
    im = Image.open(shot).convert("RGB")
    # darkroom system: one dark ink plus a warm second, coarse screen on newsprint
    # a photograph, so tone-separated, not colour-separated
    out = press.duotone(im, dark=(24, 21, 19), light=(176, 132, 74), angles=(45, 15),
                        cell=4.4, seed=21, paper_tone=(244, 239, 228), roughness=1.0,
                        contrast=1.05, knockout=0.88)
    out.save(f"{OUT}/BTS-IAmWithYou-PRESSED.jpg", "JPEG", quality=93, optimize=True, progressive=True)
    for f in (pdf, shot): os.path.exists(f) and os.remove(f)
    print("built:", f"{OUT}/BTS-IAmWithYou-PRESSED.jpg")

if PLATE and os.path.exists(PLATE):
    build(PLATE)
else:
    print("no plate yet — save the Midjourney images into public/plates/ then run:")
    print("  python3 tools/build_iamwithyou.py public/plates/<file>.png")
