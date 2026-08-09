#!/usr/bin/env python3
"""
Between Sundays — Page 22 rebuilt.
"Obituaries for Things Not Dead" — one subject, two states, split by a hard horizon.
Above: the same blooms, standing, alive against sky.
Below: the identical blooms, laid out and shadowed, each one named.
"""
import os, random, math

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "v4")
random.seed(2822)

W, H = 941, 1346
HORIZON = 556                      # hard split

# ---- palette lifted from the reference -------------------------------------
PETALS = [
    ("#FFFFFF", "#F4CE3C"),        # white daisy
    ("#D63A2B", "#2A1A12"),        # red poppy
    ("#F5C518", "#E0851A"),        # yellow
    ("#3F6FD4", "#26418C"),        # cornflower blue
    ("#F0691E", "#F5C518"),        # orange cosmos
    ("#F07EA8", "#F5D24A"),        # pink cosmos
    ("#8B6FD4", "#F4CE3C"),        # lavender aster
    ("#FFFFFF", "#E0851A"),        # white / orange eye
    ("#5B9BE0", "#26418C"),        # pale blue
    ("#E8452F", "#2A1A12"),        # scarlet
]
GREENS = ["#4A8C3F", "#5FA34E", "#3E7A36"]

def bloom(cx, cy, r, petal, eye, n=8, rot=0, kind="round"):
    """One flower head as SVG."""
    out = []
    for i in range(n):
        a = rot + i * (360 / n)
        if kind == "round":
            out.append(f'<ellipse cx="{cx}" cy="{cy - r*0.60:.1f}" rx="{r*0.30:.1f}" ry="{r*0.62:.1f}" '
                       f'fill="{petal}" transform="rotate({a:.1f} {cx} {cy})"/>')
        else:  # narrow, daisy-like
            out.append(f'<ellipse cx="{cx}" cy="{cy - r*0.66:.1f}" rx="{r*0.19:.1f}" ry="{r*0.70:.1f}" '
                       f'fill="{petal}" transform="rotate({a:.1f} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.30:.1f}" fill="{eye}"/>')
    return "".join(out)

# ============================================================ ABOVE THE LINE
standing = []
stem_x = []
x = -14
while x < W + 20:
    r      = random.uniform(14, 24)
    height = random.uniform(96, 186)
    top    = HORIZON - height
    petal, eye = random.choice(PETALS)
    g      = random.choice(GREENS)
    sway   = random.uniform(-16, 16)
    # stem
    standing.append(
        f'<path d="M {x:.1f} {HORIZON} C {x+sway*0.4:.1f} {HORIZON-height*0.45:.1f} '
        f'{x+sway:.1f} {HORIZON-height*0.75:.1f} {x+sway:.1f} {top:.1f}" '
        f'stroke="{g}" stroke-width="{random.uniform(2.0,3.4):.1f}" fill="none" stroke-linecap="round"/>')
    # a leaf or two
    for _ in range(random.randint(0, 2)):
        ly = random.uniform(HORIZON - height*0.7, HORIZON - 12)
        lw = random.uniform(14, 30)
        d  = random.choice([-1, 1])
        standing.append(
            f'<path d="M {x+sway*0.3:.1f} {ly:.1f} q {lw*d:.1f} -{lw*0.5:.1f} {lw*1.25*d:.1f} 4 '
            f'q -{lw*0.7*d:.1f} {lw*0.42:.1f} -{lw*1.25*d:.1f} -4 Z" fill="{g}" opacity=".95"/>')
    stem_x.append(x+sway)
    standing.append(bloom(x+sway, top, r, petal, eye,
                          n=random.choice([6, 8, 8, 10, 12]),
                          rot=random.uniform(0, 40),
                          kind=random.choice(["round", "narrow", "narrow"])))
    x += random.uniform(20, 34)
STANDING = "".join(standing)

# soft shadows the standing row throws onto the ledge
ledge = "".join(
    f'<ellipse cx="{sx + random.uniform(6, 20):.1f}" cy="{HORIZON + random.uniform(14, 46):.1f}" '
    f'rx="{random.uniform(13, 22):.1f}" ry="{random.uniform(6, 10):.1f}" fill="#B9AE9C" '
    f'opacity="{random.uniform(.14,.26):.2f}" filter="url(#soft)"/>'
    for sx in stem_x)

# clouds
def cloud(cx, cy, s, o):
    return ("".join(
        f'<ellipse cx="{cx+dx*s:.0f}" cy="{cy+dy*s:.0f}" rx="{rx*s:.0f}" ry="{ry*s:.0f}" fill="#FFFFFF" opacity="{o}"/>'
        for dx,dy,rx,ry in [(-70,10,78,34),(-16,-16,86,46),(46,4,72,34),(104,14,54,26),(-118,16,50,24)]))
CLOUDS = cloud(300,150,1.0,.86)+cloud(700,96,.8,.72)+cloud(120,300,.62,.5)+cloud(820,300,.55,.45)

# ============================================================ BELOW THE LINE
DEAD = [
 ("Loneliness", "34 · died Tuesday"),
 ("Certainty", "b. 2019 · not returned"),
 ("Hurry", "200 mph · 11:00–11:04"),
 ("The Deal", "20 yrs · at the river"),
 ("Nowhere", "age unknown"),
 ("Knowing What To Say", "died mid-sentence"),
 ("The Need To Earn Rest", "lifelong · in its sleep"),
 ("Self-Sufficiency", "collapsed under weight"),
 ("Perfect Timing", "never arrived"),
 ("The Highlight Reel", "outlived by Tuesday"),
 ("Proving Myself", "retired quietly"),
 ("Fear Of Not Being Enough", "died at the table"),
]
cols, rows = 4, 3
x0, y0 = 136, HORIZON + 158
dx, dy = 224, 178
fallen, labels = [], []
for i, (name, note) in enumerate(DEAD):
    cx = x0 + (i % cols) * dx + random.uniform(-24, 24)
    cy = y0 + (i // cols) * dy + random.uniform(-16, 16)
    r  = random.uniform(28, 36)
    petal, eye = PETALS[i % len(PETALS)]
    rot = random.uniform(0, 40)
    n   = random.choice([6, 8, 8, 10, 12])
    kind= random.choice(["round", "narrow"])
    g   = random.choice(GREENS)
    ang = random.uniform(-38, 38)
    # laid-flat stem
    fallen.append(f'<g transform="rotate({ang:.1f} {cx:.1f} {cy:.1f})">'
                  f'<path d="M {cx:.1f} {cy+r*0.78:.1f} q 4 {r*0.55:.1f} -2 {r*0.95:.1f}" '
                  f'stroke="{g}" stroke-width="2.6" fill="none" stroke-linecap="round"/></g>')
    # blurred shadow copy, offset down-right
    fallen.append(f'<g filter="url(#soft)" opacity=".34" transform="translate(15,20)">'
                  f'{bloom(cx, cy, r, "#9C917F", "#9C917F", n, rot, kind)}</g>')
    fallen.append(bloom(cx, cy, r, petal, eye, n, rot, kind))
    labels.append(
        f'<div class="tag" style="left:{cx-104:.0f}px;top:{cy+r+40:.0f}px"><b>{name}</b><span>{note}</span></div>')
FALLEN  = "".join(fallen)
LABELS  = "".join(labels)

SVG = f'''<svg class="art" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#3E93D0"/><stop offset=".55" stop-color="#6EB6E4"/>
   <stop offset="1" stop-color="#B4DAF0"/></linearGradient>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
   <feGaussianBlur stdDeviation="9"/></filter>
 </defs>
 <rect width="{W}" height="{HORIZON}" fill="url(#sky)"/>
 {CLOUDS}
 {STANDING}
 <rect y="{HORIZON}" width="{W}" height="{H-HORIZON}" fill="#F1EBE0"/>
 {ledge}
 {FALLEN}
</svg>'''

DOC = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays — Page 22 · Obituaries for Things Not Dead</title>
<style>
*{{box-sizing:border-box;letter-spacing:0}}
@page{{size:13.07in 18.69in;margin:0}}
html,body{{margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Avenir Next","Gill Sans",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#F1EBE0;color:#17100d;
 box-shadow:0 30px 58px rgba(17,16,13,.26)}}
.art{{position:absolute;inset:0;width:100%;height:100%}}
.layer{{position:absolute;inset:0;z-index:2}}
.folio{{position:absolute;top:26px;left:44px;right:44px;display:flex;justify-content:space-between;
 color:#fff;font-size:10.5px;font-weight:900;text-transform:uppercase;letter-spacing:.14em;
 padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,.5)}}
.folio span:last-child{{text-align:right}}
.head{{position:absolute;top:92px;left:44px;color:#fff;max-width:640px}}
.head .kick{{margin:0 0 10px;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.18em;
 color:#17100d;background:#FFF3B0;display:inline-block;padding:5px 11px}}
.head h1{{margin:0;font-size:76px;line-height:.88;font-weight:900;text-transform:uppercase;
 letter-spacing:-.03em;text-shadow:0 2px 14px rgba(20,50,80,.28)}}
.head p{{margin:16px 0 0;font-family:Georgia,serif;font-size:19px;line-height:1.42;max-width:46ch;
 text-shadow:0 1px 8px rgba(20,50,80,.3)}}
.tag{{position:absolute;width:208px;text-align:center}}
.tag b{{display:block;font-size:12px;font-weight:900;text-transform:uppercase;letter-spacing:.05em;
 line-height:1.2;color:#17100d}}
.tag span{{display:block;margin-top:3px;font-family:Georgia,serif;font-size:11.5px;line-height:1.3;
 color:#6E6455;font-style:italic}}
.foot{{position:absolute;left:44px;right:44px;bottom:34px;display:flex;justify-content:space-between;
 align-items:flex-end;gap:24px;border-top:2px solid #17100d;padding-top:10px}}
.foot .note{{font-family:Georgia,serif;font-size:13.5px;line-height:1.45;max-width:60ch;margin:0}}
.foot .pg{{font-size:10px;font-weight:900;text-transform:uppercase;letter-spacing:.18em;
 color:#6E6455;white-space:nowrap}}
.filed{{position:absolute;left:44px;right:44px;top:{HORIZON+62}px}}
.filed .lede{{margin:0;font-family:Georgia,serif;font-size:19px;line-height:1.4;max-width:62ch;color:#3A3227}}
.meta{{margin:0 0 8px;font-size:10px;font-weight:900;text-transform:uppercase;
 letter-spacing:.16em;color:#8A7F6D;line-height:1.7}}
.meta b{{color:#D63A2B}}
</style></head>
<body><main class="page">
{SVG}
<div class="layer">
 <div class="folio"><span>Obituaries<br/>Issue 001</span>
  <span>Filed quietly · buried gently<br/>Not all grief is a loss</span></div>
 <div class="head">
  <p class="kick">Deaths reported this month</p>
  <h1>Obituaries<br/>for Things<br/>Not Dead</h1>
 </div>
 <div class="filed">
  <p class="lede">Above the line: still growing, still loud, still insisting it is permanent.
  Below the line: the same twelve, laid out — and none of them were ever as alive as they claimed.</p>
 </div>
 {LABELS}
 <div class="foot">
  <p class="note"><b>Know something in your life that needs an obituary?</b> Fear, shame, a grudge with
  tenure, a story you have told so many times it calcified? Send it to obits@betweensundays.com.
  We write them with full honours. <i>Correction: Control has not actually died, but the family remains hopeful.</i></p>
  <div style="text-align:right;white-space:nowrap">
   <p class="meta">Twelve notices · <b>no flowers requested</b><br/>In lieu of flowers, sit with somebody</p>
   <span class="pg">Issue 001 / Page 22</span></div>
 </div>
</div>
</main></body></html>'''

open(os.path.join(OUT, "between-sundays-page-22.html"), "w").write(DOC)
print("wrote public/v4/between-sundays-page-22.html")
print(f"  {len(DEAD)} named blooms below the line")
print(f"  horizon at {HORIZON}px of {H}px")
