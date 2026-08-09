#!/usr/bin/env python3
"""
Page 30 · VARIANT B — the same nine panels, cut apart and re-staged.
Panels are individual crops now, so they can break the grid: a full-bleed
opening beat, a hero pulled large, and the last panel isolated on colour.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","labb")
os.makedirs(os.path.join(OUT,"art","p30"),exist_ok=True)
import shutil
for i in range(1,10):
    shutil.copy(f"{BASE}/public/lab/art/p30/panel{i}.png", f"{OUT}/art/p30/panel{i}.png")
if not os.path.exists(f"{OUT}/fonts.css"):
    shutil.copy(f"{BASE}/public/lab/fonts.css", f"{OUT}/fonts.css")

W,H=941,1346
CLAY="#C1613A"; SAGE="#8B9B84"; CREAM="#F6F1E6"; INK="#221E1A"; DEEP="#2E2A26"

# (panel, left, top, width) — heights follow the crop aspect
SEQ=[(1,"She gets there."),(2,"She reads the note."),(3,"She waits."),
     (4,"She sits down."),(6,"She makes herself small."),(7,"She turns away."),
     (8,"She stands back up.")]
strip="".join(
  f'<figure class="p"><img src="art/p30/panel{n}.png" alt=""/><figcaption><b>{n:02d}</b>{t}</figcaption></figure>'
  for n,t in SEQ)

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 30 · The Waiting Page</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};color:{INK}}}

/* hero — panel 5 pulled out of the grid, bled off the right trim */
.hero{{position:absolute;right:0;top:0;width:414px;height:586px;overflow:hidden;background:{SAGE}}}
.hero img{{width:100%;height:100%;object-fit:cover;object-position:center 28%;display:block}}
.herotag{{position:absolute;right:0;top:586px;background:{DEEP};color:{CREAM};padding:9px 22px 9px 16px;
 font-size:9.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}

.head{{position:absolute;left:44px;top:52px;width:452px}}
.dept{{font-size:10px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;color:{CLAY}}}
h1{{margin:14px 0 0;font-size:76px;font-weight:800;line-height:.84;letter-spacing:-.045em;
 text-transform:uppercase}}
h1 em{{font-style:normal;color:{CLAY}}}
.head p{{margin:18px 0 0;font-size:15.5px;line-height:1.5;font-weight:500;max-width:40ch}}
.pull{{margin-top:44px;padding-left:20px;border-left:6px solid {CLAY};font-size:38px;font-weight:800;
 line-height:1.02;letter-spacing:-.03em;text-transform:uppercase}}
.pull em{{font-style:normal;color:{CLAY}}}

/* the seven beats, small, in a run — deliberately uneven baseline */
.run{{position:absolute;left:44px;right:44px;top:648px;display:flex;gap:11px;align-items:flex-end}}
.p{{margin:0;flex:1 1 0}}
.p img{{width:100%;height:150px;object-fit:cover;display:block;background:{SAGE}}}
.p:nth-child(odd) img{{height:172px}}
.p figcaption{{margin-top:7px;font-size:10px;line-height:1.28;font-weight:600}}
.p b{{display:block;color:{CLAY};font-size:9px;letter-spacing:.14em;margin-bottom:3px}}

/* the ninth beat gets the whole bottom band, on colour */
.last{{position:absolute;left:0;right:0;bottom:0;height:392px;background:{CLAY};color:{CREAM};
 display:flex;align-items:stretch}}
.last figure{{margin:0;width:300px;flex:0 0 300px;overflow:hidden}}
.last img{{width:100%;height:100%;object-fit:cover;object-position:center;display:block}}
.last .say{{flex:1;padding:38px 44px 30px 34px;display:flex;flex-direction:column}}
.last .no{{font-size:9.5px;font-weight:800;letter-spacing:.24em;text-transform:uppercase;opacity:.75}}
.last h2{{margin:10px 0 0;font-size:46px;font-weight:800;line-height:.92;letter-spacing:-.035em;
 text-transform:uppercase}}
.last p{{margin:16px 0 0;font-size:15px;line-height:1.5;font-weight:500;max-width:42ch}}
.last .v{{margin-top:auto;padding-top:14px;border-top:2px solid rgba(246,241,230,.45);
 font-size:12.5px;font-style:italic;opacity:.9}}
.fol{{position:absolute;left:44px;top:610px;font-size:9.5px;font-weight:800;letter-spacing:.22em;
 text-transform:uppercase;opacity:.45}}
</style></head><body><main class="page">

  <div class="hero"><img src="art/p30/panel5.png" alt=""/></div>
  <div class="herotag">Panel 05 &#183; the one everybody skips</div>

  <div class="head">
    <div class="dept">Comics &#183; no words needed</div>
    <h1>Nothing<br/>is <em>happening.</em></h1>
    <p>A girl turns up somewhere she did not pick, reads a note on a door, and waits.
    That is the whole story. Nobody says anything in any of it.</p>
    <div class="pull">You already know<br/>what her shoulders<br/><em>mean.</em></div>
  </div>
  <div class="fol">Between Sundays &#183; Issue 001 &#183; Page 30</div>

  <div class="run">{strip}</div>

  <div class="last">
    <figure><img src="art/p30/panel9.png" alt=""/></figure>
    <div class="say">
      <div class="no">Panel 09</div>
      <h2>The door<br/>opens.</h2>
      <p>Most of a life looks like the small ones. Almost nobody draws those.
      Go back and look at the first panel again &mdash; she is not alone in any of them.
      She just cannot see it yet.</p>
      <div class="v">&ldquo;I am with you, and will keep you wherever you go.&rdquo; &mdash; Genesis 28:15</div>
    </div>
  </div>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-30.html"),"w").write(DOC)
print("wrote labb/between-sundays-page-30.html — panels cut apart and re-staged")
