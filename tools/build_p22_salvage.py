#!/usr/bin/env python3
"""
Page 22 — Obituaries for Things Not Dead.
Adrian's salvage figure placed 1:1 (941x941, no crop) with the type set under it.
  A -> public/lab   clean, nothing over the artwork
  B -> public/labb  same page + hairline call-outs into the empty ground
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__))
W,H,SQ = 941,1346,941
GROUND="#DBD8CB"; INK="#171612"; RULE="rgba(23,22,18,.28)"; HOT="#B8412A"

BODY = """Every piece of him was written off, and every notice was correct at the time.
The camera in 1974, when film stopped being the point. The headphones in 1991, when the
cord went. The drive in 2003, when nothing could read it anymore. Somebody carried each
one to the kerb and did not feel bad about it."""
BODY2 = """He is standing up. Nobody consulted the notices. Not one part of him was built to
sit beside any other part &mdash; wrong decade, wrong maker, wrong colour &mdash; and the
assembly holds anyway. What he is made of is not a list of failures. It is an inventory of
things that were only ever finished with."""

# call-outs: (side, label, line, label-y, target-x, target-y)
CALLOUTS=[
 ("l","Box camera",   "Obsolete 1974. Still sees.",         210, 322, 250),
 ("l","Shutter plate","Jammed since 1980. Still reaches.",  460, 330, 500),
 ("l","Hip housing",  "Scrapped as parts. Stands anyway.",  650, 400, 690),
 ("r","Twin lens",    "Last serviced 1968. Still focuses.", 180, 517, 225),
 ("r","Headphones",   "Cord severed 1991. Still listens.",  262, 610, 291),
 ("r","Drive bay",    "Unreadable since 2003. Still holds.",490, 555, 530),
]
def marks():
    o=""
    for side,lab,line,ly,tx,ty in CALLOUTS:
        y = ly + 34                      # leader runs UNDER the label, never through it
        if side=="l":
            edge = 276                   # label box is left:44 width:232
            o+=(f'<div class="co l" style="left:44px;top:{ly}px"><b>{lab}</b><span>{line}</span></div>'
                f'<svg class="ld" viewBox="0 0 {SQ} {SQ}">'
                f'<path d="M 60 {y} L {edge} {y} L {tx} {ty}" fill="none" stroke="{INK}" '
                f'stroke-width="1.2" opacity=".5"/>'
                f'<circle cx="{tx}" cy="{ty}" r="3.2" fill="{INK}" opacity=".65"/></svg>')
        else:
            edge = 664                   # label box is left:664 width:238
            o+=(f'<div class="co r" style="left:664px;top:{ly}px"><b>{lab}</b><span>{line}</span></div>'
                f'<svg class="ld" viewBox="0 0 {SQ} {SQ}">'
                f'<path d="M 886 {y} L {edge} {y} L {tx} {ty}" fill="none" stroke="{INK}" '
                f'stroke-width="1.2" opacity=".5"/>'
                f'<circle cx="{tx}" cy="{ty}" r="3.2" fill="{INK}" opacity=".65"/></svg>')
    return o

def doc(annotated):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 22 · Obituaries for Things Not Dead</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{GROUND};color:{INK}}}
.plate{{position:absolute;left:0;top:0;width:{SQ}px;height:{SQ}px}}
.plate img{{display:block;width:100%;height:100%}}
.rub{{position:absolute;left:40px;top:36px;font-size:10px;font-weight:800;letter-spacing:.24em;
 text-transform:uppercase;opacity:.55}}
.rub b{{font-weight:800}}
.fol{{position:absolute;right:40px;top:36px;font-size:10px;font-weight:800;letter-spacing:.24em;
 text-transform:uppercase;opacity:.4}}
.co{{position:absolute;width:232px;font-size:10px;line-height:1.3}}
.co.l{{text-align:right}} .co.r{{text-align:left;width:238px}}
.co b{{display:block;font-size:9.5px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}}
.co span{{display:block;font-family:"Newsreader",Georgia,serif;font-size:11px;opacity:.72;margin-top:2px}}
.ld{{position:absolute;left:0;top:0;width:{SQ}px;height:{SQ}px;pointer-events:none}}
.deck{{position:absolute;left:40px;right:40px;top:{SQ+2}px;height:{H-SQ-2}px;
 border-top:2px solid {INK};padding-top:14px;display:flex;flex-direction:column}}
.kick{{font-size:9.5px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:{HOT}}}
h1{{margin:8px 0 0;font-size:40px;font-weight:800;line-height:.94;letter-spacing:-.03em;
 text-transform:uppercase;max-width:20ch}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:12px}}
.cols p{{margin:0;font-family:"Newsreader",Georgia,serif;font-size:12.5px;line-height:1.5}}
.surv{{margin-top:14px;border-top:1px solid {RULE};padding-top:10px;display:flex;gap:14px;
 align-items:baseline}}
.surv b{{flex:0 0 auto;font-size:9px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;
 opacity:.5}}
.surv span{{font-family:"Newsreader",Georgia,serif;font-size:12.5px;line-height:1.45}}
.close{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:20px;
 border-top:1px solid {RULE};padding:10px 0 30px}}
.close b{{font-size:15px;font-weight:800;line-height:1.15;letter-spacing:-.01em;text-transform:uppercase;
 max-width:34ch}}
.close span{{font-family:"Newsreader",serif;font-style:italic;font-size:11.5px;opacity:.68;
 text-align:right;max-width:30ch;line-height:1.4}}
</style></head><body><main class="page">
  <div class="plate"><img src="art/p22-salvage.png" alt="A figure assembled from discarded parts"/>
  {marks() if annotated else ""}</div>
  <div class="rub"><b>Obituaries</b> &#183; for things that are not dead</div>
  <div class="fol">Issue 001 &#183; Page 22</div>
  <div class="deck">
    <div class="kick">Death notice &#183; filed in error</div>
    <h1>Nothing here was built to go together.</h1>
    <div class="cols"><p>{BODY}</p><p>{BODY2}</p></div>
    <div class="surv"><b>Survived by</b>
      <span>a shutter that still fires &#183; a lens that still focuses &#183; a drive nobody can
      open &#183; a cord that goes nowhere &#183; and whoever stopped and picked all of it up.</span></div>
    <div class="close">
      <b>Being finished with something is not the same as it being finished.</b>
      <span>&ldquo;Surely the Lord is in this place, and I was not aware of it.&rdquo;<br/>Genesis 28:16</span>
    </div>
  </div>
</main></body></html>"""

open(os.path.join(BASE,"public","lab","between-sundays-page-22.html"),"w").write(doc(False))
open(os.path.join(BASE,"public","labb","between-sundays-page-22.html"),"w").write(doc(True))
print("A -> lab/page-22 (clean)   B -> labb/page-22 (annotated,", len(CALLOUTS), "call-outs)")
