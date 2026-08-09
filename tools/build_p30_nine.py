#!/usr/bin/env python3
"""
Page 30 — COMICS. A wordless nine-panel strip.
Adrian's watercolour sheet placed uncropped; the key sits BESIDE and BELOW it
as a 3x3 grid that mirrors the panel layout, so nothing is printed on the art.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H = 941,1346
IW,IH = 560,806               # 912x1312 scaled 1:1, no crop
PAPER="#F4F2ED"; INK="#1A1815"; RULE="rgba(26,24,21,.22)"; MARK="#B4542C"

KEY=["She gets there.","She reads the note on the door.","She waits.",
     "She sits down on the floor.","She wonders if anyone is coming.","She makes herself small.",
     "She turns away.","She stands back up.","The door opens."]
cells="".join(f'<div class="cell{" last" if i==8 else ""}"><b>{i+1}</b><span>{t}</span></div>'
              for i,t in enumerate(KEY))

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 30 · Nothing Is Happening</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
.rub{{position:absolute;left:40px;right:40px;top:38px;display:flex;justify-content:space-between;
 font-size:9.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 border-bottom:2px solid {INK};padding-bottom:9px}}
.art{{position:absolute;left:40px;top:92px;width:{IW}px;height:{IH}px}}
.art img{{display:block;width:100%;height:100%}}
.acap{{position:absolute;left:40px;top:{92+IH+8}px;width:{IW}px;font-size:8.5px;font-weight:800;
 letter-spacing:.16em;text-transform:uppercase;opacity:.4}}

.side{{position:absolute;left:{40+IW+38}px;right:40px;top:92px;bottom:40px;display:flex;
 flex-direction:column}}
.kick{{font-size:9.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:{MARK}}}
h1{{margin:9px 0 0;font-size:44px;font-weight:800;line-height:.9;letter-spacing:-.035em;
 text-transform:uppercase}}
.deck{{margin:14px 0 0;font-family:"Newsreader",Georgia,serif;font-size:13.5px;line-height:1.5}}
.rule{{margin:16px 0;border-top:1px solid {RULE}}}
.pay{{margin-top:auto}}
.pay b{{display:block;font-size:15px;font-weight:800;line-height:1.22;letter-spacing:-.01em;
 text-transform:uppercase}}
.pay p{{margin:9px 0 0;font-family:"Newsreader",serif;font-size:13px;line-height:1.5}}
.pay span{{display:block;margin-top:12px;border-top:1px solid {RULE};padding-top:9px;
 font-family:"Newsreader",serif;font-style:italic;font-size:11.5px;opacity:.7;line-height:1.4}}

.key{{position:absolute;left:40px;top:{92+IH+30}px;width:{IW}px}}
.klab{{font-size:8.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;opacity:.45;
 border-bottom:1px solid {RULE};padding-bottom:6px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:2px}}
.cell{{padding:9px 10px 9px 0;border-bottom:1px solid {RULE};min-height:66px}}
.cell b{{display:block;font-size:10px;font-weight:800;color:{MARK};letter-spacing:.08em}}
.cell span{{display:block;margin-top:3px;font-family:"Newsreader",Georgia,serif;font-size:12.5px;
 line-height:1.35}}
.cell.last b,.cell.last span{{color:{INK}}}
.cell.last span{{font-weight:600}}
</style></head><body><main class="page">
  <div class="rub"><span>Comics &#183; no words needed</span><span>Issue 001 &#183; Page 30</span></div>

  <div class="art"><img src="art/p30-nine-panels.png" alt="Nine watercolour panels of a girl waiting"/></div>
  <div class="acap">Read them across, then down &#183; nine panels, no dialogue</div>

  <div class="key">
    <div class="klab">What is happening in each one</div>
    <div class="grid">{cells}</div>
  </div>

  <div class="side">
    <div class="kick">The waiting page</div>
    <h1>Nothing<br/>is<br/>happening.</h1>
    <p class="deck">A girl shows up somewhere she did not pick. She reads a note on a door.
    Then she waits. That is the entire story.</p>
    <p class="deck">There are no words in any of the nine drawings. You do not need them.
    You already know what her shoulders mean.</p>
    <div class="rule"></div>
    <p class="deck">Most of life looks like panels three through eight. Almost nobody draws
    those. They skip to the door.</p>
    <div class="pay">
      <b>Now go back and look at the first one again.</b>
      <p>She is not alone in a single frame. She just cannot see it yet. Neither could you,
      in the part of your life that felt like panel six.</p>
      <span>&ldquo;I am with you, and will keep you wherever you go.&rdquo; &mdash; Genesis 28:15</span>
    </div>
  </div>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-30.html"),"w").write(DOC)
print("wrote lab/between-sundays-page-30.html — art 560x806 at 1:1, 3x3 key beneath")
