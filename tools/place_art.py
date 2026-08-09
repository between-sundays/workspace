#!/usr/bin/env python3
"""
PRESS ONLY. Adrian makes the art; this places it on the broadsheet at trim.
No drawing, no added furniture — the artwork is the page.
"""
import os
from PIL import Image
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
TRIM_MM=(332,475); DPI_TARGET=300

# value = filename, or (filename, object-position) when the aspect needs a
# deliberate crop instead of a centred one
# SOURCES: the verse painted IN each artwork — emitted as <meta> so the
# source-rule checker can read what the pixels already say. Never alters visuals.
SOURCES={"14":"Genesis 28:16","21":"Psalm 105:5","39":"Genesis 28:16","41":"Psalm 32:8",
         "43":"Philippians 4:4-9","45":"Psalm 77:11","47":"Psalm 78:19"}
ART={"14":"p14-bloom-wasnt-the-beginning.png",
     "39":("p39-here-diner.png","center bottom"),
     "21":"p21-films-for-the-road.png",
     "41":"p41-flowchart-in-between.png",
     "43":("p43-stay-with-what-is-true.png","center bottom"),
     "47":"p47-table-in-the-wilderness.png",
     "45":"p45-keep-the-evidence.png"}

print(f"trim {TRIM_MM[0]}x{TRIM_MM[1]}mm · press-ready needs "
      f"{round(TRIM_MM[0]/25.4*DPI_TARGET)}x{round(TRIM_MM[1]/25.4*DPI_TARGET)}px\n")
for n,ent in sorted(ART.items()):
    f,pos = ent if isinstance(ent,tuple) else (ent,"center")
    p=os.path.join(OUT,"art",f)
    im=Image.open(p); w,h=im.size
    dpi=w/(TRIM_MM[0]/25.4)
    if abs(w/h - W/H) < .004:
        fit="exact"
    elif w/h > W/H:
        lost=(1-(W/H)/(w/h))*100; fit=f"{w/h:.4f} — {lost:.1f}% off the sides ({pos})"
    else:
        lost=(1-(H/W)*(w/h))*100; fit=f"{w/h:.4f} — {lost:.1f}% off top/bottom ({pos})"
    src_meta=f'<meta name="bible-source" content="{SOURCES[n]} (in artwork)"/>' if n in SOURCES else ""
    doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>{src_meta}
<title>Between Sundays — Page {n}</title>
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#fff}}
.page img{{display:block;width:100%;height:100%;object-fit:cover;object-position:{pos}}}
</style></head><body><main class="page">
<img src="art/{f}" alt="Between Sundays page {n}"/>
</main></body></html>"""
    open(os.path.join(OUT,f"between-sundays-page-{n}.html"),"w").write(doc)
    flag="" if dpi>=290 else f"   ** {dpi:.0f} dpi at trim — REVIEW ONLY, not press-ready **"
    print(f"  p{n}  {f}\n       {w}x{h}  aspect {fit}{flag}")
