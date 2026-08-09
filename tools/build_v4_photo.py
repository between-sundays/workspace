#!/usr/bin/env python3
"""v4 = v3's Scripture map + real photography on the pages that were asking for it."""
import json, os, html
BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "v4")
os.makedirs(OUT, exist_ok=True)
S2  = json.load(open(os.path.join(BASE,"scripture-web.json")))
S3  = json.load(open(os.path.join(BASE,"scripture-v3.json")))
DEP = json.load(open(os.path.join(BASE,"scripture-depts.json")))
esc = html.escape

SHELL = """
*{box-sizing:border-box;letter-spacing:0}
@page{size:13.07in 18.69in;margin:0}
html,body{margin:0}
body{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Avenir Next","Gill Sans",system-ui,sans-serif}
.page{position:relative;width:941px;height:1346px;overflow:hidden;
 box-shadow:0 30px 58px rgba(17,16,13,.26);isolation:isolate;background:#f8f3e6;color:#17100d}
.sheet{position:absolute;inset:46px 54px 44px;display:flex;flex-direction:column;z-index:3}
.folio{display:flex;justify-content:space-between;gap:18px;padding-bottom:9px;border-bottom:1px solid currentColor}
.folio p{margin:0;font-size:10.5px;font-weight:900;text-transform:uppercase;line-height:1.5}
.folio p:last-child{text-align:right}
.foot{margin-top:auto;padding-top:9px;border-top:1px solid currentColor;display:flex;
 justify-content:space-between;gap:14px;font-size:10px;font-weight:900;text-transform:uppercase;
 letter-spacing:.14em;opacity:.75}
.hed{font-weight:900;text-transform:uppercase;letter-spacing:-.025em;line-height:.9;margin:0}
.kick{margin:0 0 8px;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.14em}
.scrip{font-family:Georgia,"Iowan Old Style",serif;text-align:justify;hyphens:auto}
.scrip p{margin:0 0 .62em}
.scrip sup{font-family:"Avenir Next",sans-serif;font-size:.58em;font-weight:900;vertical-align:super;
 margin-right:3px;opacity:.85}
.ref{display:block;font-family:"Avenir Next",sans-serif;font-size:10.5px;font-weight:900;
 text-transform:uppercase;padding-bottom:4px;margin:0 0 10px;border-bottom:2px solid currentColor}
.bleed{position:absolute;inset:0;z-index:1}
.bleed img{width:100%;height:100%;object-fit:cover;display:block}
.scrim{position:absolute;inset:0;z-index:2}
.cap{font-size:9.5px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;opacity:.75;margin:6px 0 0}
figure{margin:0}
figure img{width:100%;display:block;object-fit:cover}
"""
def vs(store,key,lo=None,hi=None):
    return "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in store[key]
                   if lo is None or lo<=v["n"]<=hi)
def write(num,doc,label):
    open(os.path.join(OUT,f"between-sundays-page-{num}.html"),"w").write(doc)
    print(f"  p{num}  {label}")
def page(num,title,css,body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays v4 — Page {num} · {esc(title)}</title>
<style>{SHELL}{css}</style></head><body><main class="page">{body}</main></body></html>"""

print("Building v4 — photography\n")

# ---------------------------------------------------------------- 01 COVER
write("01", page("01","Cover","""
.page{background:#0e1524;color:#f2eddf}
.scrim{background:linear-gradient(180deg,rgba(14,21,36,.88) 0 26%,rgba(14,21,36,.25) 48%,
 rgba(14,21,36,.55) 72%,rgba(14,21,36,.95) 100%)}
.mast{font-size:78px;font-weight:900;letter-spacing:-.03em;text-align:center;margin:0;line-height:.92}
.mast em{font-style:italic;font-family:Georgia,serif;font-weight:400;letter-spacing:-.01em}
.rule{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-top:12px;
 padding-top:10px;border-top:1px solid rgba(242,237,223,.45);font-size:10px;font-weight:900;
 letter-spacing:.22em;text-transform:uppercase}
.big{font-size:150px;font-weight:900;letter-spacing:-.035em;line-height:.86;margin:0}
.dek{font-family:Georgia,serif;font-size:22px;line-height:1.4;max-width:62ch;margin:20px 0 0}
.teasers{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid rgba(242,237,223,.45);
 margin-top:auto}
.tz{padding:12px 14px 0;border-left:1px solid rgba(242,237,223,.25)}
.tz:first-child{border-left:none;padding-left:0}
.tz b{display:block;font-size:9.5px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#eff36a}
.tz span{display:block;font-family:Georgia,serif;font-size:13.5px;line-height:1.35;margin-top:5px}
""", """<div class="bleed"><img src="photos/cover_garage.jpg" alt=""></div><div class="scrim"></div>
<section class="sheet">
 <h1 class="mast">Between <em>Sundays</em></h1>
 <div class="rule"><span>Issue 001</span><span>The Sunday paper for the places between Sundays</span><span>Genesis 28</span></div>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <p class="kick" style="color:#eff36a">He stopped because the sun went down</p>
  <h2 class="big">I AM<br/>WITH YOU</h2>
  <p class="dek">Jacob stopped in a place with no name and slept on the ground.
  By morning he knew he had not been alone. This issue prints the whole story —
  and the eleven other times God says the same sentence.</p>
 </div>
 <div class="teasers">
  <div class="tz"><b>The Reading · p.6</b><span>Four chapters, printed in full. No commentary.</span></div>
  <div class="tz"><b>The Spine · p.23</b><span>The middle four pages are not yours. Leave them somewhere.</span></div>
  <div class="tz"><b>Photo desk · p.44</b><span>Rooms that held the moment.</span></div>
 </div>
 <p class="cap" style="margin-top:12px">Cover: an empty car park, after midnight. Photograph, public domain.</p>
</section>"""), "COVER — real photograph, full bleed")

# ------------------------------------------------- 04 GEOGRAPHY OF NOWHERE
places = [("terminal_figure","The gate that keeps changing","Terminal, hour five"),
          ("laundromat_bw","The laundromat, fluorescent and empty","Sunday, 11:48 p.m."),
          ("hall_lockers","The corridor with the humming light","Between two bells"),
          ("underpass","The way under the road","Nobody's address")]
cells = "".join(f'<figure><img src="photos/{f}.jpg" alt=""><figcaption><b>{esc(t)}</b>'
                f'<span>{esc(c)}</span></figcaption></figure>' for f,t,c in places)
write("04", page("04","The Geography of Nowhere","""
.top{padding:14px 0 16px;border-bottom:3px solid #17100d}
.top .hed{font-size:78px}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;
 gap:18px;margin-top:18px}
figure{display:flex;flex-direction:column;min-height:0}
figure img{flex:1;min-height:0;object-fit:cover}
figcaption{padding-top:8px}
figcaption b{display:block;font-family:Georgia,serif;font-weight:700;font-size:16px;line-height:1.25}
figcaption span{display:block;font-size:9.5px;font-weight:900;letter-spacing:.14em;
 text-transform:uppercase;color:#71695c;margin-top:4px}
""", f"""<section class="sheet">
 <header class="folio"><p>Special Report<br/>Ordinary places</p><p>Four photographs<br/>Public domain</p></header>
 <div class="top"><p class="kick" style="color:#c0392b">Genesis 28:11 — “a certain place”</p>
  <h1 class="hed">The Geography<br/>of Nowhere</h1>
  <p style="margin:12px 0 0;font-family:Georgia,serif;font-size:17px;line-height:1.5;max-width:76ch">
  The passage begins at an unplanned stop, not a staged holy site. So does most of your week.
  Four places nobody photographs on purpose.</p></div>
 <div class="grid">{cells}</div>
 <footer class="foot"><span>Issue 001 / Page 04</span><span>Wayfarer / Page 05</span></footer>
</section>"""), "4 real photographs replace the wireframe")

# ------------------------------------- 15 THE PLACE YOU ALMOST WALKED PAST
write("15", page("15","The Place You Almost Walked Past","""
.top{padding:14px 0 14px;border-bottom:3px solid #17100d}
.top .hed{font-size:66px}
.hero{margin-top:16px;position:relative}
.hero img{height:520px;object-fit:cover}
.strip{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px;flex:1;min-height:0}
.strip figure{display:flex;flex-direction:column;min-height:0}
.strip img{flex:1;min-height:0}
.strip figcaption{font-size:9.5px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;
 color:#71695c;padding-top:7px;line-height:1.4}
.herocap{display:flex;justify-content:space-between;gap:16px;padding-top:8px}
.herocap b{font-family:Georgia,serif;font-weight:700;font-size:19px}
.herocap span{font-size:9.5px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:#71695c}
""", """<section class="sheet">
 <header class="folio"><p>Special Report<br/>Field photography</p><p>Five locations<br/>Public domain</p></header>
 <div class="top"><p class="kick" style="color:#c0392b">A field report</p>
  <h1 class="hed">The Place You<br/>Almost Walked Past</h1></div>
 <div class="hero"><img src="photos/terminal_dusk.jpg" alt="">
  <div class="herocap"><b>Nobody arrives here. Everybody waits here.</b><span>Terminal · departures hold</span></div></div>
 <div class="strip">
  <figure><img src="photos/laundromat_fluor.jpg" alt=""><figcaption>Laundry room · after the last load</figcaption></figure>
  <figure><img src="photos/stairs_concrete.jpg" alt=""><figcaption>Stairs · between two floors</figcaption></figure>
  <figure><img src="photos/motel_room.jpg" alt=""><figcaption>Motel · one night only</figcaption></figure>
  <figure><img src="photos/porch_light.jpg" alt=""><figcaption>Porch light · left on for someone</figcaption></figure>
 </div>
 <footer class="foot"><span>Issue 001 / Page 15</span><span>Luz Local / Page 16</span></footer>
</section>"""), "photographic field report (5 locations)")

# ---------------------------------------------- 19 SPORTS + HEBREWS 12
write("19", page("19","Away Team Advantage","""
.page{background:#0f3d2e;color:#f3efe2}
.hero{margin-top:14px}
.hero img{width:100%;height:430px;object-fit:cover;display:block}
.split{flex:1;min-height:0;display:grid;grid-template-columns:1fr 300px;gap:30px;margin-top:16px}
.scrip{font-size:19px;line-height:1.6}
.scrip sup{color:#efd25c}
.ref{color:#efd25c;border-color:rgba(239,210,92,.6)}
.hed{font-size:76px}
.box{border:2px solid rgba(243,239,226,.5);padding:14px 16px;margin-bottom:12px}
.box h4{margin:0 0 8px;font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#efd25c}
.box table{width:100%;border-collapse:collapse;font-size:12px}
.box td{padding:4px 0;border-bottom:1px solid rgba(243,239,226,.22)}
.box td:last-child{text-align:right;font-weight:900}
""", f"""<section class="sheet">
 <header class="folio"><p>Sports / Road Game Desk<br/>Hebrews 12:1-3</p><p>Scripture in full<br/>World English Bible</p></header>
 <div style="padding:12px 0 12px;border-bottom:3px solid #efd25c">
  <p class="kick" style="color:#efd25c">The race set before us</p>
  <h1 class="hed">Away Team<br/>Advantage</h1></div>
 <div class="hero"><img src="photos/seats_red.jpg" alt="">
  <p class="cap">The visitors' end, two hours before anyone arrives.</p></div>
 <div class="split">
  <div class="scrip"><span class="ref">Hebrews 12:1-3 / World English Bible</span><p>{vs(S3,"heb12")}</p></div>
  <div><div class="box"><h4>Road report</h4><table>
   <tr><td>Field condition</td><td>Unfamiliar</td></tr>
   <tr><td>Weight carried</td><td>Set down</td></tr>
   <tr><td>Home-field dependent</td><td>No</td></tr></table></div>
   <div class="box"><h4>Endurance</h4><table>
   <tr><td>Witnesses</td><td>Great cloud</td></tr>
   <tr><td>Eyes fixed on</td><td>The author</td></tr>
   <tr><td>If weary</td><td>Consider him</td></tr></table></div></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 19</span><span>Weather / Page 20</span></footer>
</section>"""), "photograph + Hebrews 12 in full")

# ---------------------------------------------- 22 PRE-SPINE (empty seats)
write("22", page("22","The Next Four Pages","""
.page{background:#101b2b;color:#f4efe2}
.scrim{background:linear-gradient(180deg,rgba(16,27,43,.55),rgba(16,27,43,.92))}
.hed{font-size:104px}
""", """<div class="bleed"><img src="photos/seats_green.jpg" alt=""></div><div class="scrim"></div>
<section class="sheet">
 <header class="folio"><p>Notice<br/>Before the centre folio</p><p>Pages 23-26<br/>Removable</p></header>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:center;text-align:center">
  <p class="kick" style="color:#eff36a">One seat is not for you</p>
  <h1 class="hed">The Next<br/>Four Pages<br/>Are Not Yours.</h1>
  <p style="font-family:Georgia,serif;font-size:21px;line-height:1.5;max-width:56ch;margin:24px auto 0">
  They tear out. They carry Psalm 139 and a short note, and they are addressed to whoever
  finds them — a bench, a break room, a waiting area. Take them out. Leave them somewhere.</p>
 </div>
 <footer class="foot"><span>Issue 001 / Page 22</span><span>Tear along the centre fold / Page 23</span></footer>
</section>"""), "empty-seats photograph, full bleed")

# ------------------------------------------------------- 38 STONE
write("38", page("38","A Stone for the Table","""
.top{padding:14px 0 14px;border-bottom:3px solid #17100d}
.top .hed{font-size:70px}
.main{flex:1;min-height:0;display:grid;grid-template-columns:1.25fr 1fr;gap:30px;margin-top:18px}
.main img{width:100%;height:600px;object-fit:cover;display:block}
.scrip{font-size:18px;line-height:1.6}
.ref{color:#8a5a24}
.list{margin-top:16px;border-top:2px solid #17100d;padding-top:12px}
.list div{display:flex;gap:12px;padding:7px 0;border-bottom:1px solid rgba(23,16,13,.2)}
.list b{font-size:10px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:#a8571c;min-width:22px}
.list span{font-family:Georgia,serif;font-size:14.5px;line-height:1.4}
""", f"""<section class="sheet">
 <header class="folio"><p>Home / House object<br/>1 Samuel 7:12</p><p>Photograph<br/>Public domain</p></header>
 <div class="top"><p class="kick" style="color:#a8571c">Catalogue no. 001</p>
  <h1 class="hed">A Stone<br/>for the Table</h1></div>
 <div class="main">
  <div>
   <img src="photos/stone_hand.jpg" alt="">
   <p class="cap">Not magic. Not decor. A weight you can actually hold.</p></div>
  <div><div class="scrip"><span class="ref">Genesis 28:18 / World English Bible</span>
   <p>{vs(S2,"gen28b",18,18)}</p></div>
   <div class="list">
    <div><b>01</b><span>Entry shelf — the thing you pass twice a day.</span></div>
    <div><b>02</b><span>Kitchen table — near crumbs, near conversation.</span></div>
    <div><b>03</b><span>Desk corner — small enough to move, heavy enough to notice.</span></div>
    <div><b>04</b><span>Nightstand — last thing visible before the lights go out.</span></div>
    <div><b>05</b><span>Pocket — a place marker that learned how to travel.</span></div>
   </div></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 38</span><span>Poster / Page 39</span></footer>
</section>"""), "real stone photograph")

# ------------------------------------------- 43 BREAK GLASS + PHILIPPIANS 4
write("43", page("43","Stay With What Is True","""
.top{padding:14px 0 14px;border-bottom:3px solid #c0392b}
.top .hed{font-size:70px}
.main{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1.1fr;gap:30px;margin-top:18px}
.main img{width:100%;height:470px;object-fit:cover;display:block}
.scrip{font-size:17.6px;line-height:1.6}
.scrip sup{color:#c0392b}
.ref{color:#143653}
.safety{border:2px solid #17100d;padding:11px 14px;margin-top:12px}
.safety p{margin:0;font-family:Georgia,serif;font-size:13.5px;line-height:1.5}
""", f"""<section class="sheet">
 <header class="folio"><p>House Campaign<br/>Philippians 4:4-9</p><p>Scripture in full<br/>World English Bible</p></header>
 <div class="top"><p class="kick" style="color:#c0392b">In case of sudden hurry</p>
  <h1 class="hed">Stay With<br/>What Is True</h1></div>
 <div class="main">
  <div>
   <img src="photos/alarm_breakglass.jpg" alt="">
   <p class="cap">Break glass. Inside: one true sentence.</p></div>
  <div>
   <div class="scrip"><span class="ref">Philippians 4:4-9 / World English Bible</span><p>{vs(S3,"php4")}</p></div>
   <div class="safety"><p><b>A small safety note.</b> If the room is not safe, leave.
   This page is about staying present, not staying trapped.</p></div></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 43</span><span>Photo desk / Page 44</span></footer>
</section>"""), "real alarm photograph + Philippians 4")

# ---------------------------------------- 44 ROOMS THAT HELD THE MOMENT
rooms=[("motel_room","Motel room","One night only"),
       ("hall_lockers","School corridor","Between two bells"),
       ("laundromat_bw","Laundromat","Sunday, late"),
       ("underpass","The way under the road","Nobody's address"),
       ("porch_light","Porch light","Left on for someone")]
cells="".join(f'<figure><img src="photos/{f}.jpg" alt=""><figcaption><b>{esc(t)}</b><span>{esc(c)}</span></figcaption></figure>'
              for f,t,c in rooms)
write("44", page("44","Rooms That Held the Moment","""
.page{background:#14120e;color:#f2eddf}
.top{padding:14px 0 14px;border-bottom:2px solid rgba(242,237,223,.5)}
.top .hed{font-size:72px}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;
 gap:16px;margin-top:18px}
figure{display:flex;flex-direction:column;min-height:0}
figure img{flex:1;min-height:0;object-fit:cover}
figcaption{padding-top:7px}
figcaption b{display:block;font-family:Georgia,serif;font-weight:700;font-size:15px}
figcaption span{display:block;font-size:9.5px;font-weight:900;letter-spacing:.14em;
 text-transform:uppercase;opacity:.6;margin-top:3px}
.note{grid-column:span 1;display:flex;align-items:flex-end}
.note p{margin:0;font-family:Georgia,serif;font-size:15px;line-height:1.5;opacity:.9}
""", f"""<section class="sheet">
 <header class="folio"><p>Photo Essay / Picture desk<br/>Romans 12:1</p><p>Five photographs<br/>Public domain</p></header>
 <div class="top"><p class="kick" style="color:#eff36a">The picture desk</p>
  <h1 class="hed">Rooms That<br/>Held the Moment</h1></div>
 <div class="grid">{cells}
  <div class="note"><p>No heroics. No claim that the room explains anything.
  Just the kind of places where attention can begin — and where, according to page 6,
  the sentence has been said before.</p></div></div>
 <footer class="foot"><span>Issue 001 / Page 44</span><span>Mark the place / Page 45</span></footer>
</section>"""), "5 real photographs — the photo essay finally has photos")

# ------------------------------------------- 47 TABLE IN THE WILDERNESS
write("47", page("47","Table in the Wilderness","""
.page{background:#1a1206;color:#f4ecd8}
.scrim{background:linear-gradient(180deg,rgba(26,18,6,.82) 0 22%,rgba(26,18,6,.2) 46%,rgba(26,18,6,.9) 100%)}
.hed{font-size:96px}
.card{border:2px solid rgba(244,236,216,.6);padding:16px 18px;max-width:400px;background:rgba(26,18,6,.7)}
.card dl{margin:0;font-size:13px;line-height:1.6}
.card dt{font-weight:900;text-transform:uppercase;font-size:9.5px;letter-spacing:.12em;opacity:.65;margin-top:8px}
.card dd{margin:0;font-family:Georgia,serif}
""", """<div class="bleed"><img src="photos/table_long_night.jpg" alt=""></div><div class="scrim"></div>
<section class="sheet">
 <header class="folio"><p>Next Issue / 002 preview<br/>Exodus 16</p><p>Arrives next month<br/>Keep this paper close</p></header>
 <div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end">
  <p class="kick" style="color:#e0a33c">Issue 002 · a meal where there should not be one</p>
  <h1 class="hed">Table in the<br/>Wilderness</h1>
  <div class="card" style="margin-top:22px"><dl>
   <dt>Reading</dt><dd>Exodus 16, in full</dd>
   <dt>Question</dt><dd>What is enough for today?</dd>
   <dt>Table</dt><dd>Set in the place nobody planned</dd></dl></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 47</span><span>Back cover / Page 48</span></footer>
</section>"""), "full-bleed table photograph")

# ------------------------------------------------------- 48 BACK COVER
write("48", page("48","Back Cover","""
.page{background:#0b1a2c;color:#f4efe2}
.scrim{background:linear-gradient(180deg,rgba(11,26,44,.5) 0 30%,rgba(11,26,44,.15) 52%,rgba(11,26,44,.94) 100%)}
.big{font-size:112px;font-weight:900;letter-spacing:-.03em;line-height:.88;margin:0}
""", """<div class="bleed"><img src="photos/dawn_sky.jpg" alt=""></div><div class="scrim"></div>
<section class="sheet">
 <div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end">
  <p class="kick" style="color:#eff36a">Genesis 28:16</p>
  <h1 class="big">Surely God<br/>Is in This<br/>Place.</h1>
  <p style="font-family:Georgia,serif;font-size:21px;line-height:1.45;max-width:56ch;margin:20px 0 0">
  And I didn't know it. — A newspaper for the places between Sundays.
  Issue 002 arrives next month. Leave this one somewhere.</p>
  <div style="display:flex;justify-content:space-between;gap:16px;margin-top:26px;padding-top:12px;
   border-top:1px solid rgba(244,239,226,.5);font-size:10px;font-weight:900;letter-spacing:.2em;
   text-transform:uppercase">
   <span>Between Sundays</span><span>Issue 001</span><span>Pick it up. Pass it on.</span></div>
 </div>
</section>"""), "BACK COVER — full-bleed dawn photograph")

print("\n  12 photography pages built -> public/v4/")
