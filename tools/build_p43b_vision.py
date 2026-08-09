#!/usr/bin/env python3
"""
Page 43 · VARIANT B — WRITE IT DOWN, landscape.
The trim stays portrait; the whole design is rotated 90° so the reader turns
the paper. Left half: Habakkuk 2:2-3 + the prompt. Right half: nothing but
ruled lines to write on.
"""
import os, random, shutil
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","labb")
os.makedirs(OUT,exist_ok=True)
if not os.path.exists(f"{OUT}/fonts.css"): shutil.copy(f"{BASE}/public/lab/fonts.css",f"{OUT}/fonts.css")
PW,PH=941,1346            # portrait trim
W,H=1346,941              # landscape design canvas
RULE=42; TOP=100
BLUE="#8FB4D9"; RED="#D96A6A"; INKB="#23418F"; PAPER="#FBFAF6"
random.seed(43)

NRULES=(H-TOP)//RULE
rules="".join(f'<line x1="0" y1="{TOP+k*RULE}" x2="{W}" y2="{TOP+k*RULE}" stroke="{BLUE}" stroke-width="1.3"/>'
              for k in range(NRULES+1))
pts="0,50 "
x=0
while x<W:
    x+=random.randint(18,44); pts+=f"{min(x,W)},{50+random.randint(-12,12)} "
pts+=f"{W},50 {W},0 0,0"
holes="".join(f'<circle cx="{86+i*97}" cy="30" r="11" fill="#cfc3b3"/>' for i in range(13))

def line(i,txt,cls="vl"):   # text sitting ON rule i (baseline just above it)
    return f'<div class="{cls}" style="top:{TOP+i*RULE-33}px">{txt}</div>'

LEFT=(
 line(1,"Yahweh answered me,","vl sm")
+line(2,"&ldquo;Write the vision, and make it")
+line(3,"plain on tablets, that he who")
+line(4,"runs may read it.")
+line(5,"For the vision is yet for the")
+line(6,"appointed time, and it hurries toward")
+line(7,"the end, and won&rsquo;t prove false.")
+line(8,"Though it takes time, wait for it;")
+line(9,"because it will surely come.")
+line(10,"It won&rsquo;t delay.&rdquo;")
+f'<div class="ref" style="top:{TOP+10*RULE+4}px">Habakkuk 2 : 2&ndash;3 &#183; that is the whole assignment</div>'
+line(13,'Write <b>one specific thing</b> you believe',"pl")
+line(14,"God has put in front of you.","pl")
+line(15,"Not a feeling. A thing.","pl")
+line(16,"With a size and a date on it.","pl")
+line(17,"Then put this page where you will see it.","nt")
+line(18,"It may take longer than you want. That is not the same as late.","nt"))

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 43 · Write It Down</title><link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Shantell Sans","Bricolage Grotesque",cursive}}
.page{{position:relative;width:{PW}px;height:{PH}px;overflow:hidden;background:{PAPER}}}
.land{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;
 transform:rotate(-90deg) translate(-{W}px,0);transform-origin:0 0}}
svg.bg{{position:absolute;inset:0;width:100%;height:100%}}
.margin{{position:absolute;top:0;bottom:0;left:88px;width:5px;
 border-left:2px solid {RED};border-right:1.4px solid {RED};opacity:.75}}
.vl{{position:absolute;left:116px;width:540px;height:{RULE}px;line-height:{RULE}px;
 font-size:21.5px;color:{INKB};font-weight:600;white-space:nowrap}}
.vl.sm{{font-size:18px;opacity:.85}}
.ref{{position:absolute;left:116px;font-size:12.5px;color:{INKB};opacity:.7;
 letter-spacing:.07em;text-transform:uppercase;font-weight:700}}
.pl{{position:absolute;left:116px;width:540px;height:{RULE}px;line-height:{RULE}px;
 font-size:19px;color:#28251F;font-weight:600;white-space:nowrap}}
.pl b{{background:rgba(217,106,106,.22);padding:0 5px}}
.nt{{position:absolute;left:116px;width:540px;height:{RULE}px;line-height:{RULE}px;
 font-size:14px;color:#4A463D;font-weight:600;white-space:nowrap}}
.dv{{position:absolute;top:{TOP-16}px;bottom:30px;left:692px;width:0;
 border-left:2.4px dashed rgba(35,65,143,.35)}}
.yr{{position:absolute;left:724px;top:{TOP+RULE-33}px;height:{RULE}px;line-height:{RULE}px;
 font-size:15px;color:#4A463D;font-weight:600}}
.yr i{{font-style:normal;display:inline-block;width:170px;border-bottom:1.6px solid #4A463D;
 height:24px;vertical-align:bottom;margin-left:8px}}
.turn{{position:absolute;right:34px;top:56px;font-size:12px;color:#8A8578;letter-spacing:.14em;
 text-transform:uppercase;font-weight:700}}
.fol{{position:absolute;left:116px;bottom:12px;font-size:10.5px;color:#8A8578;letter-spacing:.14em;
 text-transform:uppercase;font-weight:700}}
</style></head><body><main class="page"><div class="land">
<svg class="bg" viewBox="0 0 {W} {H}">{rules}</svg>
<svg class="bg" style="height:66px" viewBox="0 0 {W} 66" preserveAspectRatio="none">
 <polygon points="{pts}" fill="#cfc3b3"/>{holes}</svg>
<div class="margin"></div>
{LEFT}
<div class="dv"></div>
<div class="yr">date<i></i></div>
<div class="fol">Between Sundays &#183; Issue 001 &#183; Page 43 &#183; turn the paper &#183; tear this out</div>
</div></main></body></html>"""
open(f"{OUT}/between-sundays-page-43.html","w").write(DOC)
print(f"labb/p43 landscape · left = verse+prompt · right = {NRULES} blank rules")
