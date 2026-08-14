#!/usr/bin/env python3
"""Concept 01 — the teaser-strip front page (Le Cafetier), pressed for real."""
import os,sys,json,subprocess,uuid
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W,H=941,1346
BR="#241a12"; RED="#a8321e"; CREAM="#f7f2e7"
V=json.load(open(f"{B}/public/data/verses-full.json"))
g2816=V["Genesis 28:16"]

TOP=[("Genesis 28","The night he slept on a stone","07"),
     ("Words &amp; meaning","Bethel, Luz, and a ramp","16"),
     ("Games","Find the certain place","32"),
     ("But God","210 verses, sorted by what is wrong","34")]
BOT=[("Weather","Forecast for the middle of the week","20"),
     ("Music","Songs for walking home","40"),
     ("Write it down","One page. One question.","43"),
     ("Coupons","Redeemable at no cost","22")]
def strip(items,top):
    w=(W-104)/4; out=[]
    for i,(k,t,p) in enumerate(items):
        x=52+i*w
        out.append(f'''<div style="position:absolute;left:{x:.0f}px;top:{top}px;width:{w-18:.0f}px">
          <div class="k">{k}</div><div class="tz">{t}</div><div class="pg">PAGE {p}</div></div>''')
        if i: out.append(f'<div style="position:absolute;left:{x-9:.0f}px;top:{top}px;width:1px;'
                         f'height:74px;background:{BR};opacity:.55"></div>')
    return "".join(out)

HTML=f"""<!doctype html><html><head><meta charset="utf-8"/>
<meta name="bible-source" content="Genesis 28:16 (NLT)"/>
<meta name="style-system" content="didone-newsprint"/>
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,800;0,900;1,700;1,900&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter:wght@600;700;800&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:{CREAM}}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};
 font-family:'Newsreader',Georgia,serif;color:{BR}}}
.k{{font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;color:{RED}}}
.tz{{font-size:15px;line-height:1.24;margin-top:6px;font-weight:500}}
.pg{{font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:.14em;
 margin-top:7px;opacity:.62}}
.rule{{position:absolute;left:52px;right:52px;background:{BR}}}
</style></head><body><div class="page">

 <div style="position:absolute;left:52px;right:52px;top:34px;display:flex;
  font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:.22em;
  text-transform:uppercase;color:{RED}">
  <span>Issue One</span><span style="flex:1"></span><span>Good news. Printed.</span>
  <span style="flex:1"></span><span>Free — take one</span></div>
 <div class="rule" style="top:56px;height:1px;opacity:.5"></div>

 <div style="position:absolute;left:0;right:0;top:74px;text-align:center">
  <div style="font-family:'Playfair Display',serif;font-size:74px;font-weight:900;
   letter-spacing:-.035em;line-height:.92">Between</div>
  <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:96px;
   font-weight:900;letter-spacing:-.04em;line-height:.82;margin-top:-4px">Sundays</div>
 </div>
 <div class="rule" style="top:262px;height:2px"></div>
 <div class="rule" style="top:267px;height:1px;opacity:.6"></div>
 {strip(TOP,282)}
 <div class="rule" style="top:372px;height:1px;opacity:.55"></div>

 <!-- the middle moment: a night field, the line reversed out of it -->
 <div style="position:absolute;left:52px;right:52px;top:398px;height:596px;background:{BR};
   overflow:hidden">
  <div style="position:absolute;left:0;right:0;top:0;height:300px;
   background:linear-gradient(180deg,#3c2b1e 0%,{BR} 100%)"></div>
  <div style="position:absolute;right:66px;top:52px;width:132px;height:132px;border-radius:50%;
   background:#6b543f;opacity:.85"></div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:132px;background:#120c08"></div>
  <div style="position:absolute;left:44px;right:44px;top:196px;font-family:'Playfair Display',serif;
   font-size:63px;font-weight:900;line-height:.99;letter-spacing:-.03em;color:{CREAM}">
   Surely the LORD<br/>is in this place,
   <span style="font-style:italic;font-weight:700">and I<br/>wasn&rsquo;t even aware of it.</span></div>
  <div style="position:absolute;left:44px;bottom:38px;font-family:'Inter',sans-serif;font-size:10px;
   font-weight:800;letter-spacing:.2em;color:#c9a892">GENESIS 28:16 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
 </div>

 <div style="position:absolute;left:52px;top:1014px;width:520px;font-size:17.5px;line-height:1.45">
  He was running for his life and stopped because it got dark. He picked a rock for a pillow.
  Nothing about the place was special, and God was already there.</div>
 <div style="position:absolute;right:52px;top:1014px;width:300px;border-left:1px solid {BR};
  padding-left:20px">
  <div class="k">Inside</div>
  <div style="font-size:15px;line-height:1.42;margin-top:8px">Forty-eight pages. A removable
   section you can keep. Games at the back. Nothing in here assumes you have read it before.</div></div>

 <div class="rule" style="top:1146px;height:1px;opacity:.55"></div>
 {strip(BOT,1164)}
 <div class="rule" style="bottom:56px;height:1px;opacity:.5"></div>
 <div style="position:absolute;left:52px;right:52px;bottom:30px;display:flex;
  font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:.18em;
  text-transform:uppercase;opacity:.72">
  <span>A newspaper for the days in between</span><span style="flex:1"></span>
  <span>I Am With You</span></div>
</div></body></html>"""

out=f"{B}/public/press2"
os.makedirs(out,exist_ok=True)
open(f"{out}/ref01.html","w").write(HTML)

# render
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
uid=uuid.uuid4().hex[:8]
pdf=f"{out}/_r{uid}.pdf"
subprocess.run([CHROME,"--headless","--disable-gpu","--no-pdf-header-footer",
  "--virtual-time-budget=9000","--run-all-compositor-stages-before-draw",
  f"--print-to-pdf={pdf}",f"--no-margins",f"file://{out}/ref01.html"],
  capture_output=True,timeout=420)
subprocess.run(["pdftoppm","-png","-r","150","-f","1","-l","1",pdf,f"{out}/_r{uid}"],
  capture_output=True,timeout=420)
print("rendered:",os.path.exists(f"{out}/_r{uid}-1.png"))
