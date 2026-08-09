#!/usr/bin/env python3
"""
Page 38 — HOME · Give Them the Tour.
Built as THREE modules, to show the grid working:
  HALF landscape 941x673   — illustration (1:1, uncropped) + the idea
  QUARTER 470x673 (left)   — where to stop
  QUARTER 470x673 (right)  — a form you fill in
Plain language, short sentences. Each module carries its own folio.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H,HALF,Q = 941,1346,673,470
PAPER="#EDECEA"; INK="#171614"; RULE="rgba(23,22,20,.24)"; MARK="#C4622F"; BLUE="#2E5A7A"

STOPS=[("01","A door","Who came through it?"),
       ("02","A window","What did you watch from here?"),
       ("03","The table","What got decided here?"),
       ("04","A corner nobody uses","Why is it still there?"),
       ("05","Outside","Turn around. Look at the house.")]
stops="".join(f'<li><b>{n}</b><div><h4>{t}</h4><span>{q}</span></div></li>' for n,t,q in STOPS)
rows="".join('<div class="row"><label>The place</label><i></i>'
             '<label>What happened here</label><i class="w"></i></div>' for _ in range(5))

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 38 · Give Them the Tour</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
.mod{{position:absolute;overflow:hidden;background:{PAPER}}}
.mod.half{{left:0;top:0;width:{W}px;height:{HALF}px}}
.mod.qL{{left:0;top:{HALF}px;width:{Q}px;height:{HALF}px;border-top:2px solid {INK}}}
.mod.qR{{left:{Q}px;top:{HALF}px;width:{W-Q}px;height:{HALF}px;border-top:2px solid {INK};
 border-left:1px solid {RULE}}}
.tag{{position:absolute;bottom:12px;right:16px;font-size:7.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.3}}
.fol{{display:flex;justify-content:space-between;font-size:9px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.5;border-bottom:1px solid {RULE};padding-bottom:7px}}

/* ── HALF ── */
.art{{position:absolute;left:22px;top:{(HALF-Q)//2}px;width:{Q}px;height:{Q}px}}
.art img{{display:block;width:100%;height:100%}}
.copy{{position:absolute;left:{Q+34}px;right:34px;top:34px;bottom:26px;display:flex;flex-direction:column}}
.kick{{font-size:9.5px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:{MARK};
 margin-top:14px}}
h1{{margin:8px 0 0;font-size:52px;font-weight:800;line-height:.92;letter-spacing:-.035em;
 text-transform:uppercase}}
.deck{{margin:14px 0 0;font-family:"Newsreader",Georgia,serif;font-size:16px;line-height:1.5}}
.body{{margin:12px 0 0;font-family:"Newsreader",Georgia,serif;font-size:14px;line-height:1.55;opacity:.86}}
.says{{list-style:none;margin:12px 0 0;padding:0 0 0 15px;border-left:3px solid {MARK}}}
.says li{{display:block;font-family:"Newsreader",Georgia,serif;font-size:14px;line-height:1.5;
 padding:3px 0;border:0}}
.pay{{margin-top:auto;border-top:2px solid {INK};padding-top:11px}}
.pay b{{display:block;font-size:16px;font-weight:800;line-height:1.2;letter-spacing:-.01em;
 text-transform:uppercase}}
.pay span{{display:block;margin-top:6px;font-family:"Newsreader",serif;font-size:11.5px;
 font-style:italic;opacity:.7;line-height:1.4}}

/* ── QUARTERS ── */
.qin{{position:absolute;inset:22px 22px 30px}}
.qh{{margin:14px 0 0;font-size:23px;font-weight:800;line-height:1;letter-spacing:-.02em;
 text-transform:uppercase}}
.qs{{margin:7px 0 0;font-family:"Newsreader",serif;font-size:12.5px;line-height:1.45;opacity:.75}}
ul{{list-style:none;margin:14px 0 0;padding:0}}
li{{display:flex;gap:11px;align-items:baseline;padding:9px 0;border-bottom:1px solid {RULE}}}
li b{{font-size:11px;font-weight:800;color:{MARK};letter-spacing:.06em}}
li h4{{margin:0;font-size:14px;font-weight:800;letter-spacing:-.01em}}
li span{{display:block;margin-top:2px;font-family:"Newsreader",serif;font-size:12px;opacity:.7}}
.tip{{margin:12px 0 0;font-family:"Newsreader",serif;font-size:12px;line-height:1.45;opacity:.72}}
.nohouse{{margin-top:16px;border:2px solid {INK};padding:12px 13px}}
.nohouse b{{display:block;font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 color:{MARK};margin-bottom:5px}}
.nohouse span{{font-family:"Newsreader",serif;font-size:12.5px;line-height:1.45}}
.row{{margin-top:19px}}
.row label{{display:block;font-size:8.5px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;
 opacity:.45;margin-bottom:3px}}
.row i{{display:block;height:22px;border-bottom:1.5px solid {INK};opacity:.55}}
.row i.w{{height:22px;margin-bottom:2px}}
.fridge{{position:absolute;left:22px;right:22px;bottom:30px;border-top:2px solid {INK};padding-top:9px;
 font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:{BLUE}}}
</style></head><body><main class="page">

<!-- ═══ MODULE 1 · HALF PAGE · LANDSCAPE · 332 × 237.5 mm ═══ -->
<section class="mod half">
  <div class="art"><img src="art/p38-the-tour.png" alt="A dad showing his two kids a doorway"/></div>
  <div class="copy">
    <div class="fol"><span>Home</span><span>Issue 001 &#183; Page 38</span></div>
    <div class="kick">Ten minutes &#183; costs nothing</div>
    <h1>Give them<br/>the tour.</h1>
    <p class="deck">Your kids do not know which parts of your home matter.
    They will not know until you tell them.</p>
    <p class="body">So walk them around it. Stop in five spots. At each one, say one true thing
    that happened there.</p>
    <ul class="says">
      <li>&ldquo;This is the door we brought you home through.&rdquo;</li>
      <li>&ldquo;This is where Grandma always sat.&rdquo;</li>
      <li>&ldquo;This is the wall we painted the wrong color.&rdquo;</li>
      <li>&ldquo;This is where we ate when there was not much.&rdquo;</li>
    </ul>
    <p class="body">That is the whole thing. Ten minutes. They will keep it for years.</p>
    <div class="pay"><b>A place is just a place until someone tells you what happened there.</b>
      <span>&ldquo;When your children ask you what these stones mean, tell them.&rdquo;
      &mdash; Joshua 4:21&ndash;22</span></div>
  </div>
  <span class="tag">Half page &#183; landscape</span>
</section>

<!-- ═══ MODULE 2 · QUARTER · 166 × 237.5 mm ═══ -->
<section class="mod qL">
  <div class="qin">
    <div class="fol"><span>Home</span><span>Page 38</span></div>
    <h2 class="qh">Where to stop</h2>
    <p class="qs">Five spots. Any house has them.</p>
    <ul>{stops}</ul>
    <p class="tip">You do not need a story for all five. One is enough.</p>
    <div class="nohouse"><b>No house?</b>
      <span>Do it with a car. A street. A school. Any place you have been more than once.</span></div>
  </div>
  <span class="tag">Quarter page</span>
</section>

<!-- ═══ MODULE 3 · QUARTER · 166 × 237.5 mm ═══ -->
<section class="mod qR">
  <div class="qin">
    <div class="fol"><span>Fill this in</span><span>Page 38</span></div>
    <h2 class="qh">Your tour</h2>
    <p class="qs">Write it down so they still have it when you are not there to say it.</p>
    {rows}
  </div>
  <div class="fridge">Cut this out. Put it on the fridge.</div>
  <span class="tag">Quarter page</span>
</section>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-38.html"),"w").write(DOC)
print("wrote lab/between-sundays-page-38.html — 1 half + 2 quarters, art placed 470x470 at 1:1")
