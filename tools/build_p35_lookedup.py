#!/usr/bin/env python3
"""
Page 35 — MOST LOOKED UP. The facing page of the Bethel Directory.
The thirty heaviest verses from page 34, printed WHOLE (NLT), each tagged with
where it is filed — so nobody has to trust our filing. Same yellow, same furniture.
"""
import json, os, math
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
rows=json.load(open(os.path.join(BASE,"directory_verified.json")))
W,H=941,1346
YELLOW="#F5DE21"; INK="#141308"; RED="#C6261C"
MARGIN=28; HEADTOP=64; FOOTH=74
COLS=3; GUT=16
CW=(W-2*MARGIN-(COLS-1)*GUT)/COLS
COLTOP=HEADTOP+30; COLH=H-COLTOP-FOOTH

PICK=["Psalm 23:4","Isaiah 41:10","Matthew 11:28","Philippians 4:6","1 Peter 5:7",
"Psalm 34:18","Romans 8:1","1 John 1:9","Genesis 28:15","Psalm 46:1","Psalm 46:10",
"Proverbs 3:5","Romans 8:28","Lamentations 3:22","2 Corinthians 12:9","Isaiah 40:31",
"Matthew 6:34","Romans 5:8","Habakkuk 2:3","Luke 15:20","John 11:35","Revelation 21:4",
"Psalm 27:14","Galatians 6:9","Ephesians 2:10","Psalm 139:12",
"Mark 9:24","Psalm 68:6","1 Corinthians 10:13","Matthew 6:26"]

# text + every category each ref is filed under
bytext={}; cats={}
for r in rows:
    bytext[r["ref"]]=r["text"]
    cats.setdefault(r["ref"],[]).append(r["cat"])
cards=[]
for ref in PICK:
    if ref not in bytext: print("  !! not in directory:",ref); continue
    t=bytext[ref]; tag=" · ".join(dict.fromkeys(cats[ref]))
    lines=math.ceil(len(t)/40)
    h=30+lines*15.5+16
    cards.append((ref,t,tag,h))
print(f"  {len(cards)} verses, all pulled from the verified directory data")

cols=[[] for _ in range(COLS)]
heights=[0.0]*COLS
for c in cards:                       # tallest-first would break reading order; keep order, fill shortest
    i=heights.index(min(heights))
    cols[i].append(c); heights[i]+=c[3]+10
print("  cols:",[f"{h:.0f}" for h in heights],"of",f"{COLH:.0f}")
assert max(heights)<=COLH-8, "COLUMN OVERFLOW — a verse would be clipped"

def card(ref,t,tag):
    return (f'<div class="vc"><div class="vr">{ref}<span>NLT</span></div>'
            f'<p>{t}</p><div class="ft">Filed under: {tag}</div></div>')
colhtml="".join('<div class="col">'+ "".join(card(r,t,g) for r,t,g,_ in c) +"</div>" for c in cols)

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 35 · Most Looked Up</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{YELLOW};color:{INK}}}
.rh{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:26px;display:flex;
 justify-content:space-between;align-items:baseline;border-bottom:3px solid {INK};padding-bottom:5px}}
.rh b{{font-size:19px;font-weight:800;letter-spacing:.04em}}
.rh .tag{{font-size:9px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.strap{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{HEADTOP}px;display:flex;
 justify-content:space-between;font-size:8.5px;font-weight:700;letter-spacing:.1em;
 text-transform:uppercase;border-bottom:1px solid {INK};padding-bottom:4px}}
.cols{{position:absolute;left:{MARGIN}px;top:{COLTOP}px;width:{W-2*MARGIN}px;height:{COLH}px;
 display:flex;gap:{GUT}px}}
.col{{width:{CW}px;position:relative}}
.col+.col:before{{content:"";position:absolute;left:-{GUT/2:.0f}px;top:0;bottom:0;
 border-left:1px solid rgba(20,19,8,.45)}}
.vc{{border-bottom:1px solid rgba(20,19,8,.4);padding:8px 2px 9px;break-inside:avoid}}
.vr{{display:flex;justify-content:space-between;align-items:baseline;
 font-family:"Fraunces",Georgia,serif;font-weight:900;font-size:17px;letter-spacing:-.01em}}
.vr span{{font-family:"Bricolage Grotesque",sans-serif;font-size:7px;font-weight:800;
 letter-spacing:.18em;opacity:.6}}
.vc p{{margin:5px 0 6px;font-family:"Newsreader",Georgia,serif;font-size:11.8px;line-height:1.34}}
.ft{{font-size:7.2px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
 color:{RED};line-height:1.4}}
.banner{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;bottom:34px;background:{INK};
 color:{YELLOW};padding:9px 14px;display:flex;justify-content:space-between;align-items:center;gap:18px}}
.banner b{{font-family:"Fraunces",serif;font-weight:900;font-size:18px;line-height:1.05}}
.banner p{{margin:0;font-size:9px;line-height:1.4;max-width:52ch}}
.banner .pg{{font-family:"Fraunces",serif;font-weight:900;font-size:26px;white-space:nowrap}}
.folio{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;bottom:14px;display:flex;
 justify-content:space-between;font-size:8px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
</style></head><body><main class="page">
 <div class="rh"><b>35 &nbsp; MOST LOOKED UP &mdash; PRINTED WHOLE</b>
  <span class="tag">The Bethel Directory &#183; Issue 001</span></div>
 <div class="strap"><span>The words themselves, so you do not have to take our filing on trust</span>
  <span>Full listings by need: page 34</span><span>Free &#183; take one</span></div>
 <div class="cols">{colhtml}</div>
 <div class="banner">
  <div><b>Check our work.</b>
   <p style="margin-top:3px">Every verse here is printed as the New Living Translation has it, whole.
   If you think one is filed under the wrong feeling on page 34, you are exactly the reader we want
   &mdash; write to us and we will move it. The letters page is on 28.</p></div>
  <div class="pg">PAGE 34 &#8592;</div>
 </div>
 <div class="folio"><span>Between Sundays &#183; Issue 001</span>
  <span>Scripture: Holy Bible, New Living Translation &#183; used by permission &#183; notice on page 02</span>
  <span>Page 35</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-35.html","w").write(DOC)
print("  wrote press/between-sundays-page-35.html")
