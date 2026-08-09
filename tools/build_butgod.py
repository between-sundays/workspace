#!/usr/bin/env python3
"""
BUT GOD — three modules.
  p34  FULL PAGE   the wall: 32 ordinary faces, two words, no captions
  p33  HALF+2 QTR  the pairs table, a fill-in, and the uncomfortable one
No statement is ever attached to a face. Nobody is assigned a hardship.
"""
import os, glob
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
INK="#141414"; CREAM="#F2EFE8"; RED="#C4361F"; PAPER="#EDEAE2"

FACES=sorted(os.path.basename(f) for f in glob.glob(f"{OUT}/art/faces/f*.png"))
# 6 x 9 grid. Rows 3-4 are the headline band, row 8 is the footer — no face is
# ever cut in half by them, so those rows carry no portraits at all.
COLS,ROWS=6,9
CW,CH=W/COLS,H/ROWS
BAND_ROWS={3,4}; FOOT_ROW=8
cells=""; i=0
for r in range(ROWS):
    if r in BAND_ROWS or r==FOOT_ROW: continue
    for c in range(COLS):
        x,y=c*CW,r*CH
        if i<len(FACES):
            cells+=(f'<div class="c" style="left:{x:.2f}px;top:{y:.2f}px;width:{CW:.2f}px;'
                    f'height:{CH:.2f}px"><img src="art/faces/{FACES[i]}" alt=""/></div>'); i+=1
        else:
            cells+=(f'<div class="c blank" style="left:{x:.2f}px;top:{y:.2f}px;width:{CW:.2f}px;'
                    f'height:{CH:.2f}px"></div>')
BAND_TOP=3*CH; BAND_H=2*CH; FOOT_TOP=FOOT_ROW*CH; FOOT_H=CH

# ── p34 · THE WALL ───────────────────────────────────────────────────────────
open(f"{OUT}/between-sundays-page-34.html","w").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>Between Sundays — Page 34 · But God</title>
<link rel="stylesheet" href="fonts.css"><style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{INK}}}
.c{{position:absolute;overflow:hidden}}
.c img{{width:100%;height:100%;object-fit:cover;object-position:center 34%;display:block;
 filter:grayscale(.28) contrast(1.04)}}
.c.blank{{background:{RED}}}
.band{{position:absolute;left:0;right:0;top:{BAND_TOP:.2f}px;height:{BAND_H:.2f}px;background:{INK};
 display:flex;align-items:center;justify-content:center;padding-top:34px}}
.band h1{{margin:0;font-size:150px;font-weight:800;letter-spacing:-.055em;line-height:.8;color:#fff;
 text-transform:uppercase}}
.band h1 em{{font-style:normal;color:{RED}}}
.rub{{position:absolute;left:0;right:0;top:{BAND_TOP:.2f}px;height:40px;background:{RED};color:#fff;
 display:flex;align-items:center;justify-content:space-between;padding:0 26px;
 font-size:11px;font-weight:800;letter-spacing:.34em;text-transform:uppercase}}
.foot{{position:absolute;left:0;right:0;top:{FOOT_TOP:.2f}px;height:{FOOT_H:.2f}px;background:{INK};
 color:{CREAM};padding:26px 26px 0}}
.foot p{{margin:0;font-size:23px;font-weight:800;line-height:1.16;letter-spacing:-.015em;
 text-transform:uppercase;max-width:44ch}}
.foot span{{position:absolute;right:26px;bottom:14px;font-size:9.5px;font-weight:800;
 letter-spacing:.24em;text-transform:uppercase;opacity:.5}}
</style></head><body><main class="page">
{cells}
<div class="band"><h1>But <em>God</em></h1></div>
<div class="foot"><p>Not one of these people is having the day you think they are.</p>
<span>The Bethel Directory · thirty-two people · no captions · Issue 001 · Page 34</span></div>
</main></body></html>""")
print("  p34 · the wall ·", len(FACES), "faces")

# ── p33 · THE PAIRS + FILL-IN + THE HARD ONE ────────────────────────────────
PAIRS=[("Somebody did it to you on purpose.",
        "As for you, you meant evil against me, but God meant it for good.","Genesis 50:20"),
       ("You are the only one still awake in the house.",
        "My flesh and my heart fails, but God is the strength of my heart and my portion forever.","Psalm 73:26"),
       ("You are not who you hoped you would be by now.",
        "But God, being rich in mercy, for his great love with which he loved us&hellip;","Ephesians 2:4"),
       ("You do not think you have earned any of this.",
        "But God commends his own love toward us, in that while we were yet sinners, Christ died for us.","Romans 5:8"),
       ("You were not the one they picked.",
        "But God chose the foolish things of the world that he might put to shame those who are wise.","1 Corinthians 1:27"),
       ("It is over, and it is not coming back.",
        "But God raised him from the dead.","Acts 13:30")]
rows="".join(f'<div class="pr"><div class="lft">{a}</div><div class="mid">but God</div>'
             f'<div class="rgt">&ldquo;{b}&rdquo;<i>{c}</i></div></div>' for a,b,c in PAIRS)
lines="".join('<div class="ln"><span>but God</span></div>' for _ in range(4))

open(f"{OUT}/between-sundays-page-33.html","w").write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>Between Sundays — Page 33 · But God</title>
<link rel="stylesheet" href="fonts.css"><style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
.half{{position:absolute;left:0;top:0;width:{W}px;height:673px;padding:30px 34px 20px}}
.qL{{position:absolute;left:0;top:673px;width:470px;height:673px;border-top:3px solid {INK};
 padding:26px 28px}}
.qR{{position:absolute;left:470px;top:673px;width:471px;height:673px;border-top:3px solid {INK};
 border-left:1px solid rgba(20,20,20,.22);padding:26px 28px;background:{INK};color:{CREAM}}}
.fo{{display:flex;justify-content:space-between;font-size:8.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.5;border-bottom:1px solid currentColor;padding-bottom:6px}}
h1{{margin:14px 0 0;font-size:52px;font-weight:800;line-height:.9;letter-spacing:-.04em;
 text-transform:uppercase}}
h1 em{{font-style:normal;color:{RED}}}
.dek{{margin:10px 0 0;font-size:13.5px;line-height:1.45;max-width:82ch;opacity:.8}}
.pr{{display:grid;grid-template-columns:1fr 84px 1.25fr;gap:14px;align-items:center;
 padding:11px 0;border-bottom:1px solid rgba(20,20,20,.18)}}
.lft{{font-size:14.5px;font-weight:700;line-height:1.25}}
.mid{{text-align:center;font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;
 color:{RED}}}
.rgt{{font-family:"Newsreader",Georgia,serif;font-size:13.5px;line-height:1.36}}
.rgt i{{display:block;font-style:normal;font-family:"Bricolage Grotesque",sans-serif;font-size:8.5px;
 font-weight:800;letter-spacing:.16em;text-transform:uppercase;opacity:.5;margin-top:3px}}
h2{{margin:14px 0 0;font-size:26px;font-weight:800;letter-spacing:-.02em;text-transform:uppercase;
 line-height:.98}}
.q p{{margin:10px 0 0;font-size:13.5px;line-height:1.45}}
.ln{{margin-top:26px;border-bottom:2px solid rgba(20,20,20,.55);position:relative;height:34px}}
.ln span{{position:absolute;left:50%;transform:translateX(-50%);bottom:5px;background:{PAPER};
 padding:0 9px;font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{RED}}}
.note{{position:absolute;left:28px;right:28px;bottom:26px;font-size:12px;line-height:1.4;opacity:.7}}
.hard{{margin-top:16px;border:2px solid rgba(242,239,232,.5);padding:15px 16px}}
.hard p{{margin:0;font-family:"Newsreader",Georgia,serif;font-size:14.5px;line-height:1.4}}
.hard i{{display:block;font-style:normal;font-size:8.5px;font-weight:800;letter-spacing:.16em;
 text-transform:uppercase;opacity:.6;margin-top:7px;font-family:"Bricolage Grotesque",sans-serif}}
</style></head><body><main class="page">
<section class="half">
  <div class="fo"><span>But God</span><span>Issue 001 · Page 33</span></div>
  <h1>Two words that<br/>turn a <em>sentence</em> around.</h1>
  <p class="dek">On the left, an ordinary thing anybody could write. On the right, the Bible using
  the same two words. These are not anybody&rsquo;s real story. The left column is blank on purpose &mdash;
  it is for yours.</p>
  {rows}
</section>
<section class="qL">
  <div class="fo"><span>Write your own</span><span>Page 33</span></div>
  <h2>Yours</h2>
  <p style="margin:9px 0 0;font-size:13.5px;line-height:1.45">Put the true thing on the top line.
  Leave the bottom one alone for now.</p>
  {lines}
  <p class="note">You do not have to fill the second line in today. Plenty of people in this book
  waited years for theirs.</p>
</section>
<section class="qR">
  <div class="fo"><span>Not all of them are comfort</span><span>Page 33</span></div>
  <h2>The one<br/>nobody<br/>prints</h2>
  <p style="margin:10px 0 0;font-size:13.5px;line-height:1.45;opacity:.85">A man in Luke finally
  gets his plan sorted. Bigger barns, everything stored, years of it. Then:</p>
  <div class="hard"><p>&ldquo;But God said to him, &lsquo;You foolish one, tonight your soul is
  required of you. The things which you have prepared &mdash; whose will they be?&rsquo;&rdquo;</p>
  <i>Luke 12:20</i></div>
  <p style="margin:14px 0 0;font-size:13.5px;line-height:1.45;opacity:.85">Sometimes <b>but God</b>
  is the rescue. Sometimes it is the interruption. It is the same two words either way, and you do
  not get to pick which one is coming.</p>
</section>
</main></body></html>""")
print("  p33 · half + two quarters ·", len(PAIRS), "pairs")
