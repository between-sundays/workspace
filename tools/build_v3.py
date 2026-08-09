#!/usr/bin/env python3
"""
Between Sundays Issue 001 — VERSION 3
Rebuilt to the Scripture map: the complete Jacob arc, direct Scripture every 4-5 pages,
and a different visual world per page (no shared template across the Reading).
"""
import json, os, html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "v3")
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
S2 = json.load(open(os.path.join(BASE, "scripture-web.json")))
S3 = json.load(open(os.path.join(BASE, "scripture-v3.json")))
DEP = json.load(open(os.path.join(BASE, "scripture-depts.json")))
esc = html.escape

# ---------------------------------------------------------------- shared shell
SHELL = """
*{box-sizing:border-box;letter-spacing:0}
@page{size:13.07in 18.69in;margin:0}
html,body{margin:0}
body{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Avenir Next","Gill Sans",system-ui,sans-serif}
.page{position:relative;width:941px;height:1346px;overflow:hidden;
 box-shadow:0 30px 58px rgba(17,16,13,.26);isolation:isolate}
.sheet{position:absolute;inset:46px 54px 44px;display:flex;flex-direction:column;z-index:2}
.grain{position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.5;
 background-image:radial-gradient(rgba(0,0,0,.14) .5px,transparent .8px);background-size:6px 6px}
.folio{display:flex;justify-content:space-between;align-items:flex-start;gap:18px;
 padding-bottom:9px;border-bottom:1px solid currentColor}
.folio p{margin:0;font-size:10.5px;font-weight:900;text-transform:uppercase;line-height:1.5}
.folio p:last-child{text-align:right}
.foot{margin-top:auto;padding-top:9px;border-top:1px solid currentColor;display:flex;
 justify-content:space-between;gap:14px;font-size:10px;font-weight:900;
 text-transform:uppercase;letter-spacing:.14em;opacity:.75}
/* scripture — ONE stable system, per the brief */
.scrip{font-family:Georgia,"Iowan Old Style",serif;text-align:justify;hyphens:auto}
.scrip p{margin:0 0 .62em}
.scrip sup{font-family:"Avenir Next",sans-serif;font-size:.58em;font-weight:900;
 vertical-align:super;margin-right:3px;opacity:.8}
.ref{display:block;font-family:"Avenir Next",sans-serif;font-size:10.5px;font-weight:900;
 text-transform:uppercase;padding-bottom:4px;margin:0 0 10px;border-bottom:2px solid currentColor}
.ref.later{margin-top:18px}
.hed{font-weight:900;text-transform:uppercase;letter-spacing:-.025em;line-height:.9;margin:0}
.kick{margin:0 0 8px;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.14em}
.scene{margin:0;font-family:Georgia,serif;font-style:italic;font-size:15px;line-height:1.45;opacity:.85}
.badge{display:inline-block;font-size:10px;font-weight:900;letter-spacing:.16em;
 text-transform:uppercase;padding:5px 10px;border:2px solid currentColor}
"""

def vs(store, key, lo=None, hi=None):
    out = []
    for v in store[key]:
        if lo is not None and not (lo <= v["n"] <= hi): continue
        out.append(f'<sup>{v["n"]}</sup>{esc(v["t"])} ')
    return "".join(out)

def write(num, doc, label):
    open(os.path.join(OUT, f"between-sundays-page-{num}.html"), "w").write(doc)
    print(f"  p{num}  {label}")

def shell(num, title, css, body, ink="#17100d", bg="#f8f3e6"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays v3 — Page {num} · {esc(title)}</title>
<style>{SHELL}
.page{{background:{bg};color:{ink}}}
{css}</style></head><body><main class="page"><div class="grain"></div>{body}</main></body></html>"""

print("Building v3 — Scripture map\n")

# =============================================================== p06 · ANTHOLOGY
# "I AM WITH YOU. AGAIN AND AGAIN." — replaces the departures board.
refrains = [
 ("Genesis 26:24", vs(S3,"gen26")), ("Genesis 28:15", '<sup>15</sup>' + esc(next(v["t"] for v in S2["gen28b"] if v["n"]==15)) ),
 ("Exodus 3:12", vs(S3,"exo3b",12,12)), ("Joshua 1:5-9", vs(S3,"jos1b")),
 ("Isaiah 41:10", vs(S3,"isa41")), ("Isaiah 43:1-3", vs(S3,"isa43b")),
 ("Jeremiah 1:7-8", vs(S3,"jer1")), ("Haggai 1:13", vs(S3,"hag1")),
 ("Matthew 1:22-23", vs(S3,"mat1b")), ("Acts 18:9-10", vs(S3,"act18")),
 ("Matthew 28:18-20", vs(S3,"mat28b")),
]
items = "".join(
 f'<div class="rf"><b>{esc(r)}</b><div class="scrip">{t}</div></div>' for r,t in refrains)
write("06", shell("06","I Am With You, Again and Again", """
.page{background:#12100c;color:#f4efe2}
.grain{opacity:.28;background-image:radial-gradient(rgba(255,255,255,.16) .5px,transparent .8px)}
.hero{padding:16px 0 14px;border-bottom:3px solid #f4efe2}
.hero .hed{font-size:92px}
.hero .hed em{font-style:normal;color:#eff36a;display:block}
.lede{margin:14px 0 0;font-family:Georgia,serif;font-size:17px;line-height:1.5;max-width:70ch;opacity:.9}
.grid{flex:1;min-height:0;margin-top:16px;column-count:2;column-gap:36px;
 column-rule:1px solid rgba(244,239,226,.28)}
.rf{break-inside:avoid;margin:0 0 13px;padding-bottom:11px;border-bottom:1px solid rgba(244,239,226,.2)}
.rf b{display:block;font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;
 color:#eff36a;margin-bottom:4px}
.rf .scrip{font-size:14px;line-height:1.5;text-align:left}
""", f"""<section class="sheet">
 <header class="folio"><p>Before the Reading<br/>Scripture only</p>
 <p>Eleven passages, printed in full<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#eff36a">The refrain, in the order it appears</p>
  <h1 class="hed">I Am With You.<em>Again and Again.</em></h1>
  <p class="lede">Not a theme this newspaper invented. A sentence God says, in these words, to a
  patriarch, a shepherd, a soldier, a prophet, a frightened church-planter, and finally to everyone.
  Read the eleven before you read the one.</p></div>
 <div class="grid">{items}</div>
 <footer class="foot"><span>Issue 001 / Page 06</span><span>The Reading begins / Page 07</span></footer>
</section>"""), "Anthology — 11 refrain passages (replaces departures board)")

# =============================================================== p07 · DEPARTURE
write("07", shell("07","Why He Was Running", """
.page{background:#efe9da}
.top{display:grid;grid-template-columns:1fr 300px;gap:26px;align-items:end;
 padding:14px 0 16px;border-bottom:3px solid #17100d}
.top .hed{font-size:74px}
.doc{border:2px solid #17100d;padding:14px 16px;background:#fff}
.doc h3{margin:0 0 8px;font-size:10.5px;font-weight:900;letter-spacing:.14em;text-transform:uppercase}
.doc dl{margin:0;font-size:12.5px;line-height:1.6}
.doc dt{font-weight:900;text-transform:uppercase;font-size:9.5px;letter-spacing:.1em;color:#6d6558;margin-top:7px}
.doc dd{margin:0;font-family:Georgia,serif}
.cols{flex:1;min-height:0;margin-top:18px;column-count:2;column-gap:38px;column-rule:1px solid rgba(23,16,13,.25)}
.scrip{font-size:17.6px;line-height:1.6}
.ref{color:#143653}
""", f"""<section class="sheet">
 <header class="folio"><p>The Reading / 01 of 07<br/>Genesis 27:41 – 28:9</p>
 <p>No commentary in this section<br/>World English Bible</p></header>
 <div class="top">
  <div><p class="kick" style="color:#c0392b">Beersheba · he leaves under threat</p>
   <h1 class="hed">Why He Was<br/>Running</h1>
   <p class="scene" style="margin-top:12px">Before the famous night, there is a reason he is sleeping outdoors.</p></div>
  <div class="doc"><h3>Scene marker</h3><dl>
   <dt>Place</dt><dd>Beersheba, leaving</dd>
   <dt>Cause</dt><dd>A stolen blessing; a brother's threat</dd>
   <dt>Sent by</dt><dd>His mother, to keep him alive</dd>
   <dt>Destination</dt><dd>Haran — roughly 500 miles</dd>
   <dt>Unresolved</dt><dd>Everything</dd></dl></div>
 </div>
 <div class="cols"><div class="scrip">
  <span class="ref">Genesis 27:41-46 / World English Bible</span><p>{vs(S2,"gen27")}</p>
  <span class="ref later">Genesis 28:1-9</span><p>{vs(S2,"gen28a")}</p>
 </div></div>
 <footer class="foot"><span>Issue 001 / Page 07</span><span>The night at Bethel / Pages 08-09</span></footer>
</section>"""), "Gen 27:41–28:9 — why he was running (22 v)")

# =========================================================== p08-09 · THE NIGHT
# Two-page spread, night ground, Scripture uninterrupted.
gen28 = S2["gen28b"]
part1 = "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in gen28 if v["n"] <= 17)
part2 = "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in gen28 if v["n"] >= 18)
NIGHT = """
.page{background:#141d33;color:#f2eddf}
.grain{opacity:.22;background-image:radial-gradient(rgba(255,255,255,.14) .5px,transparent .8px)}
.hero{padding:14px 0 14px;border-bottom:2px solid rgba(242,237,223,.55)}
.hero .hed{font-size:80px}
.cols{flex:1;min-height:0;margin-top:20px;column-count:2;column-gap:40px;
 column-rule:1px solid rgba(242,237,223,.22)}
.scrip{font-size:19.6px;line-height:1.68}
.scrip sup{color:#eff36a}
.ref{color:#eff36a;border-color:rgba(239,243,106,.6)}
.mark{margin-top:14px;font-size:10.5px;font-weight:900;letter-spacing:.2em;text-transform:uppercase;opacity:.6}
"""
write("08", shell("08","The Night at Bethel — 1", NIGHT, f"""<section class="sheet">
 <header class="folio"><p>The Reading / 02 of 07<br/>Genesis 28:10-17</p>
 <p>Uninterrupted · spread 1 of 2<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#eff36a">A certain place · night</p>
  <h1 class="hed">The Night<br/>At Bethel</h1></div>
 <div class="cols"><div class="scrip">
  <span class="ref">Genesis 28:10-17 / World English Bible</span><p>{part1}</p></div></div>
 <p class="mark">The passage continues on the facing page — no commentary between.</p>
 <footer class="foot"><span>Issue 001 / Page 08</span><span>Continues / Page 09</span></footer>
</section>"""), "Gen 28:10-17 — night spread 1")

write("09", shell("09","The Night at Bethel — 2", NIGHT, f"""<section class="sheet">
 <header class="folio"><p>The Reading / 03 of 07<br/>Genesis 28:18-22</p>
 <p>Uninterrupted · spread 2 of 2<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#eff36a">Morning · the stone becomes a marker</p>
  <h1 class="hed">And He Was<br/>Afraid</h1></div>
 <div class="cols"><div class="scrip">
  <span class="ref">Genesis 28:18-22 / World English Bible</span><p>{part2}</p>
  <div style="margin-top:22px;padding-top:16px;border-top:2px solid rgba(239,243,106,.6)">
  <p style="font-family:Georgia,serif;font-size:26px;line-height:1.3;font-style:italic;color:#eff36a;margin:0">
  “Surely Yahweh is in this place, and I didn't know it.”</p></div>
 </div></div>
 <footer class="foot"><span>Issue 001 / Page 09</span><span>Years later / Page 10</span></footer>
</section>"""), "Gen 28:18-22 — night spread 2")

# ======================================================== p10 · THE RECALL
write("10", shell("10","The God of Bethel Calls Again", """
.page{background:#f2ede0}
.tele{border:3px solid #17100d;padding:22px 26px;margin-top:14px;background:#fff}
.tele .stamp{display:flex;justify-content:space-between;font-size:10px;font-weight:900;
 letter-spacing:.16em;text-transform:uppercase;color:#c0392b;border-bottom:2px solid #17100d;padding-bottom:9px}
.tele .hed{font-size:62px;margin:16px 0 0}
.gap{display:flex;align-items:center;gap:14px;margin:22px 0 6px}
.gap span{flex:1;height:2px;background:#17100d}
.gap b{font-size:11px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
.cols{flex:1;min-height:0;margin-top:16px;column-count:2;column-gap:38px;column-rule:1px solid rgba(23,16,13,.25)}
.scrip{font-size:25px;line-height:1.66}
.ref{color:#143653}
""", f"""<section class="sheet">
 <header class="folio"><p>The Reading / 04 of 07<br/>Genesis 31:1-3, 10-13</p>
 <p>Twenty years later<br/>World English Bible</p></header>
 <div class="tele">
  <div class="stamp"><span>Notice · delivered in a dream</span><span>Haran</span></div>
  <p class="kick" style="margin-top:14px;color:#c0392b">He did not meet God once and move on</p>
  <h1 class="hed">The God of Bethel<br/>Calls Him Back</h1>
 </div>
 <div class="gap"><span></span><b>Twenty years pass</b><span></span></div>
 <div class="cols"><div class="scrip">
  <span class="ref">Genesis 31:1-3 / World English Bible</span><p>{vs(S3,"gen31a")}</p>
  <span class="ref later">Genesis 31:10-13</span><p>{vs(S3,"gen31b")}</p>
 </div></div>
 <footer class="foot"><span>Issue 001 / Page 10</span><span>The return / Pages 11-13</span></footer>
</section>"""), "Gen 31 — 'I am the God of Bethel'")

# ==================================================== p11-13 · THE RETURN
g35 = S3["gen35"]
r1 = "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in g35 if v["n"] <= 7)
r2 = "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in g35 if 8 <= v["n"] <= 15)
DAWN = """
.page{background:#f6efdd}
.band{padding:14px 0 14px;border-bottom:3px solid #8a5a24}
.band .hed{font-size:76px;color:#3a2a12}
.cols{flex:1;min-height:0;margin-top:20px;column-count:2;column-gap:40px;column-rule:1px solid rgba(138,90,36,.35)}
.scrip{font-size:25px;line-height:1.66;color:#221a0c}
.scrip sup{color:#a8571c}
.ref{color:#8a5a24}
.step{display:flex;gap:10px;margin-top:14px}
.step i{flex:1;height:5px;background:rgba(138,90,36,.25);font-style:normal}
.step i.on{background:#a8571c}
"""
for n,(kick,hed,ref,txt,foot,on) in {
 "11":("Return · he goes back to the place","Put Away<br/>The Gods","Genesis 35:1-7",r1,"Continues / Page 12",1),
 "12":("The promise repeated, and a new name","God Went Up<br/>From Him","Genesis 35:8-15",r2,"The arrival / Page 13",2),
}.items():
    steps = "".join(f'<i class="{"on" if i<on else ""}"></i>' for i in range(3))
    write(n, shell(n, hed.replace("<br/>"," "), DAWN, f"""<section class="sheet">
 <header class="folio"><p>The Reading / {int(n)-6:02d} of 07<br/>{ref}</p>
 <p>The return to Bethel<br/>World English Bible</p></header>
 <div class="band"><p class="kick" style="color:#a8571c">{kick}</p><h1 class="hed">{hed}</h1>
  <div class="step">{steps}</div></div>
 <div class="cols"><div class="scrip">
  <span class="ref">{ref} / World English Bible</span><p>{txt}</p></div></div>
 <footer class="foot"><span>Issue 001 / Page {n}</span><span>{foot}</span></footer>
</section>"""), f"{ref} — the return")

# p13 — the arrival: one monumental page closing the arc
arc = [("Genesis 27-28","He runs. A stolen blessing behind him, nothing settled ahead."),
       ("Genesis 28:10-22","He sleeps in a place with no name and wakes up somewhere else."),
       ("Genesis 31","Twenty years on, God names the place again and tells him to go back."),
       ("Genesis 35","He returns, puts away what he was carrying, and builds the altar.")]
arc_html = "".join(f'<div class="arc"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a,b in arc)
write("13", shell("13","The Place Did Not Change", """
.page{background:#241a10;color:#f4ecd8}
.grain{opacity:.24;background-image:radial-gradient(rgba(255,255,255,.14) .5px,transparent .8px)}
.mid{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center}
.mid .hed{font-size:104px;color:#f4ecd8}
.mid .hed em{font-style:normal;color:#e0a33c;display:block}
.line{margin:26px 0 0;font-family:Georgia,serif;font-size:25px;line-height:1.45;max-width:62ch}
.arcs{margin-top:28px;padding-top:18px;border-top:2px solid rgba(244,236,216,.4);
 display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.arc b{display:block;font-size:10px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;
 color:#e0a33c;margin-bottom:6px}
.arc span{font-family:Georgia,serif;font-size:13.5px;line-height:1.45;opacity:.9}
.verse{margin-top:26px;padding-top:18px;border-top:2px solid rgba(244,236,216,.4)}
.verse p{margin:0;font-family:Georgia,serif;font-size:21px;line-height:1.55}
.verse sup{font-family:"Avenir Next",sans-serif;font-size:11px;font-weight:900;color:#e0a33c;vertical-align:super;margin-right:3px}
""", f"""<section class="sheet">
 <header class="folio"><p>The Reading / 07 of 07<br/>The arc closes</p>
 <p>Genesis 27 - 35<br/>World English Bible</p></header>
 <div class="mid">
  <p class="kick" style="color:#e0a33c">Four chapters, one promise, twenty years</p>
  <h1 class="hed">The Place Did<br/>Not Change.<em>Jacob's Sight Did.</em></h1>
  <p class="line">He left the same ground he came back to. Nothing about Bethel was renovated
  between the first night and the last. What changed was a man who had been told, in the dirt,
  that he was not alone — and who lived long enough to find out it was true.</p>
  <div class="arcs">{arc_html}</div>
  <div class="verse"><p><sup>15</sup>{esc(next(v["t"] for v in g35 if v["n"]==15))}</p></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 13</span><span>After the Reading / Page 14</span></footer>
</section>"""), "The arrival — the arc closes")

# ================================================= p19 · SPORTS + HEBREWS 12
write("19", shell("19","Away Team Advantage", """
.page{background:#0f3d2e;color:#f3efe2}
.grain{opacity:.2;background-image:radial-gradient(rgba(255,255,255,.14) .5px,transparent .8px)}
.hero{padding:14px 0 16px;border-bottom:3px solid #efd25c}
.hero .hed{font-size:86px}
.split{flex:1;min-height:0;display:grid;grid-template-columns:1fr 330px;gap:32px;margin-top:18px}
.scrip{font-size:21px;line-height:1.62}
.scrip sup{color:#efd25c}
.ref{color:#efd25c;border-color:rgba(239,210,92,.6)}
.box{border:2px solid rgba(243,239,226,.5);padding:16px 18px;margin-bottom:14px}
.box h4{margin:0 0 9px;font-size:10.5px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#efd25c}
.box table{width:100%;border-collapse:collapse;font-size:12.5px}
.box td{padding:5px 0;border-bottom:1px solid rgba(243,239,226,.22)}
.box td:last-child{text-align:right;font-weight:900}
""", f"""<section class="sheet">
 <header class="folio"><p>Sports / Road Game Desk<br/>Hebrews 12:1-3</p>
 <p>Scripture printed in full<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#efd25c">The race set before us</p>
  <h1 class="hed">Away Team<br/>Advantage</h1></div>
 <div class="split">
  <div class="scrip">
   <span class="ref">Hebrews 12:1-3 / World English Bible</span><p>{vs(S3,"heb12")}</p>
   <p style="font-family:Georgia,serif;font-style:italic;font-size:22px;line-height:1.35;
   margin-top:20px;padding-top:16px;border-top:2px solid rgba(239,210,92,.6);color:#efd25c">
   The passage is the page. Everything below is just the box score.</p>
  </div>
  <div>
   <div class="box"><h4>Road report</h4><table>
    <tr><td>Field condition</td><td>Unfamiliar</td></tr>
    <tr><td>Crowd noise</td><td>Loud early</td></tr>
    <tr><td>Weight carried</td><td>Set down</td></tr>
    <tr><td>Home-field dependent</td><td>No</td></tr></table></div>
   <div class="box"><h4>Endurance table</h4><table>
    <tr><td>Witnesses in the stands</td><td>Great cloud</td></tr>
    <tr><td>Entanglement</td><td>Laid aside</td></tr>
    <tr><td>Eyes fixed on</td><td>The author</td></tr>
    <tr><td>Result if weary</td><td>Consider him</td></tr></table></div>
   <div class="box"><h4>Coach's note</h4>
    <p style="margin:0;font-family:Georgia,serif;font-size:14px;line-height:1.5">
    Endurance is not the same as hurry. The instruction is to run with patience — a word
    no scoreboard has ever rewarded.</p></div>
  </div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 19</span><span>Weather / Page 20</span></footer>
</section>"""), "Hebrews 12:1-3 in full + box scores")

# ============================================ p24-25 · SPINE CARRIES PSALM 139
SPINE = """
.page{background:#101b2b;color:#f4efe2}
.grain{opacity:.24;background-image:radial-gradient(rgba(255,255,255,.15) .5px,transparent .8px)}
.tear{position:absolute;top:0;bottom:0;width:34px;z-index:3;display:flex;align-items:center;justify-content:center}
.tear b{transform:rotate(-90deg);white-space:nowrap;font-size:9.5px;font-weight:900;
 letter-spacing:.4em;text-transform:uppercase;color:#eff36a;opacity:.9}
.scrip{font-size:24px;line-height:1.66}
.scrip sup{color:#eff36a}
.ref{color:#eff36a;border-color:rgba(239,243,106,.55)}
"""
write("24", shell("24","The Spine — Psalm 139:7-12", SPINE + """
.tear{left:0;border-right:2px dashed rgba(239,243,106,.75)}
.hero .hed{font-size:78px}
""", f"""<div class="tear"><b>Fold · leave · find</b></div>
<section class="sheet" style="left:74px">
 <header class="folio"><p>The Spine / Page 24<br/>For whoever finds it</p>
 <p>Psalm 139:7-12 in full<br/>World English Bible</p></header>
 <div class="hero" style="padding:16px 0 14px;border-bottom:2px solid rgba(244,239,226,.5)">
  <p class="kick" style="color:#eff36a">Someone left this here on purpose</p>
  <h1 class="hed">Where Can<br/>I Go?</h1></div>
 <div style="flex:1;min-height:0;margin-top:22px">
  <div class="scrip"><span class="ref">Psalm 139:7-12 / World English Bible</span>
  <p>{vs(DEP,"psa121",0,0) if False else vs(S3,"psa139b")}</p></div>
 </div>
 <footer class="foot"><span>The Spine / 02 of 04</span><span>Turn over</span></footer>
</section>"""), "Psalm 139:7-12 in full (Spine)")

write("25", shell("25","The Spine — Maybe Here Counts Too", SPINE + """
.page{background:#f4efe2;color:#17100d}
.grain{opacity:.5;background-image:radial-gradient(rgba(0,0,0,.14) .5px,transparent .8px)}
.tear{right:0;border-left:2px dashed #c0392b}
.tear b{color:#c0392b}
.scrip{font-size:20px;line-height:1.6}
.scrip sup{color:#c0392b}
.ref{color:#143653;border-color:#143653}
""", f"""<div class="tear"><b>This part belongs to whoever finds it next</b></div>
<section class="sheet" style="right:74px">
 <header class="folio"><p>The Spine / Page 25<br/>A short note</p>
 <p>Written for a stranger<br/>World English Bible</p></header>
 <div style="padding:16px 0 14px;border-bottom:3px solid #17100d">
  <p class="kick" style="color:#c0392b">No church required to read this</p>
  <h1 class="hed" style="font-size:76px">Maybe Here<br/>Counts Too</h1></div>
 <p class="scene" style="margin-top:16px;font-size:19px;max-width:66ch">You do not have to be in a
 building. You do not have to have the right words. The page you are holding was left where you are
 because the place you are in already counts.</p>
 <div style="flex:1;min-height:0;margin-top:18px" class="scrip">
  <span class="ref">Genesis 28:16-17 / World English Bible</span>
  <p>{"".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in S2["gen28b"] if v["n"] in (16,17))}</p>
  <span class="ref later">Matthew 28:20</span>
  <p><sup>20</sup>{esc(next(v["t"] for v in S3["mat28b"] if v["n"]==20))}</p>
 </div>
 <footer class="foot"><span>The Spine / 03 of 04</span><span>Leave it somewhere / Page 26</span></footer>
</section>"""), "Gen 28:16-17 + Matt 28:20 (Spine)")

# =================================== p36 · ROMANS 8 (merged campaign)
write("36", shell("36","No Dead Zones — the proof", """
.page{background:#c0392b;color:#fff6ea}
.grain{opacity:.24;background-image:radial-gradient(rgba(255,255,255,.16) .5px,transparent .8px)}
.hero{padding:14px 0 16px;border-bottom:3px solid #fff6ea}
.hero .hed{font-size:96px}
.cols{flex:1;min-height:0;margin-top:20px;column-count:2;column-gap:40px;column-rule:1px solid rgba(255,246,234,.35)}
.scrip{font-size:20.5px;line-height:1.64}
.scrip sup{color:#ffe08a}
.ref{color:#ffe08a;border-color:rgba(255,224,138,.6)}
""", f"""<section class="sheet">
 <header class="folio"><p>House Campaign / continued from Page 35<br/>Romans 8:31-39</p>
 <p>The claim, and the proof<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#ffe08a">Page 35 made the claim. This is the coverage map.</p>
  <h1 class="hed">Nothing<br/>Separates</h1></div>
 <div class="cols"><div class="scrip">
  <span class="ref">Romans 8:31-39 / World English Bible</span><p>{vs(DEP,"rom8")}</p>
 </div></div>
 <footer class="foot"><span>Issue 001 / Page 36</span><span>Food / Page 37</span></footer>
</section>"""), "Romans 8:31-39 in full (merged 35/36)")

# =================================== p37 · JOHN 6 as a real reading block
write("37", shell("37","What Bread Does", """
.page{background:#f7f0dd}
.top{padding:14px 0 16px;border-bottom:3px solid #17100d}
.top .hed{font-size:80px}
.split{flex:1;min-height:0;display:grid;grid-template-columns:1fr 300px;gap:32px;margin-top:18px}
.scrip{font-size:21.5px;line-height:1.64}
.scrip sup{color:#a8571c}
.ref{color:#8a5a24}
.receipt{border:2px dashed #17100d;padding:16px 18px;font-size:12.5px;line-height:1.9}
.receipt h4{margin:0 0 10px;font-size:10.5px;font-weight:900;letter-spacing:.16em;text-transform:uppercase}
.receipt div{display:flex;justify-content:space-between;border-bottom:1px dotted rgba(23,16,13,.4)}
""", f"""<section class="sheet">
 <header class="folio"><p>Food / Table Note<br/>John 6:32-35</p>
 <p>Scripture printed in full<br/>World English Bible</p></header>
 <div class="top"><p class="kick" style="color:#a8571c">Bread, bodies, tables, provision</p>
  <h1 class="hed">What Bread<br/>Does</h1></div>
 <div class="split">
  <div class="scrip"><span class="ref">John 6:32-35 / World English Bible</span><p>{vs(S3,"joh6b")}</p>
   <p style="font-family:Georgia,serif;font-style:italic;font-size:21px;line-height:1.35;margin-top:20px;
   padding-top:16px;border-top:2px solid #17100d">Some gifts are simple on purpose.</p></div>
  <div><div class="receipt"><h4>Table receipt</h4>
   <div><span>Bread for today</span><b>$0</b></div>
   <div><span>Second helping of patience</span><b>$0</b></div>
   <div><span>One honest question</span><b>$0</b></div>
   <div><span>Enough for whoever is here</span><b>$0</b></div>
   <p style="margin:12px 0 0;font-family:Georgia,serif;font-size:12.5px;line-height:1.5">
   Make one meal that does not need to be photographed. Eat it slowly.</p></div></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 37</span><span>Home / Page 38</span></footer>
</section>"""), "John 6:32-35 in full")

# =================================== p40 · PSALM 121 in full
write("40", shell("40","Songs for Walking Home", """
.page{background:#0d1424;color:#f2eddf}
.grain{opacity:.24;background-image:radial-gradient(rgba(255,255,255,.15) .5px,transparent .8px)}
.hero{padding:14px 0 16px;border-bottom:2px solid rgba(242,237,223,.5)}
.hero .hed{font-size:82px}
.split{flex:1;min-height:0;display:grid;grid-template-columns:1fr 280px;gap:34px;margin-top:20px}
.scrip{font-size:23px;line-height:1.66}
.scrip sup{color:#efd25c}
.ref{color:#efd25c;border-color:rgba(239,210,92,.55)}
.track{border-bottom:1px solid rgba(242,237,223,.25);padding:11px 0}
.track b{display:block;font-size:10px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:#ff9ec0}
.track span{font-family:Georgia,serif;font-size:15px}
""", f"""<section class="sheet">
 <header class="folio"><p>Music / Listening Guide<br/>Psalm 121</p>
 <p>The Psalm printed in full<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#efd25c">A song for the journey — the original one</p>
  <h1 class="hed">Songs for<br/>Walking Home</h1></div>
 <div class="split">
  <div class="scrip"><span class="ref">Psalm 121 / World English Bible</span><p>{vs(DEP,"psa121")}</p></div>
  <div><p style="font-size:10.5px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;
   color:#efd25c;margin:0 0 8px">The rotation</p>
   <div class="track"><b>Track 01 · after the parking lot</b><span>Slow Choir</span></div>
   <div class="track"><b>Track 02 · before replying</b><span>Road Psalm</span></div>
   <div class="track"><b>Track 03 · while washing dishes</b><span>Kitchen Hymn</span></div>
   <p style="font-family:Georgia,serif;font-size:14px;line-height:1.55;margin-top:16px;opacity:.85">
   Psalm 121 is a song of ascents — sung by people literally walking. It is the oldest
   walking-home track we know of, and it is on this page in full.</p></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 40</span><span>Younger readers / Page 41</span></footer>
</section>"""), "Psalm 121 in full")

# =================================== p43 · PHILIPPIANS 4 in full
write("43", shell("43","Stay With What Is True", """
.page{background:#f6f2e8}
.alarm{border:6px solid #c0392b;padding:20px 24px;margin-top:14px;background:#fff}
.alarm .strip{background:#c0392b;color:#fff;margin:-20px -24px 16px;padding:9px 14px;
 font-size:10.5px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
.alarm .hed{font-size:66px}
.cols{flex:1;min-height:0;margin-top:18px;column-count:2;column-gap:38px;column-rule:1px solid rgba(23,16,13,.25)}
.scrip{font-size:20px;line-height:1.62}
.scrip sup{color:#c0392b}
.ref{color:#143653}
.safety{border:2px solid #17100d;padding:12px 15px;margin-top:14px;background:#fff}
.safety p{margin:0;font-family:Georgia,serif;font-size:14px;line-height:1.5}
""", f"""<section class="sheet">
 <header class="folio"><p>House Campaign<br/>Philippians 4:4-9</p>
 <p>Scripture printed in full<br/>World English Bible</p></header>
 <div class="alarm"><div class="strip">In case of sudden hurry — break glass</div>
  <p class="kick" style="color:#c0392b">Campaign No. 004</p>
  <h1 class="hed">Stay With<br/>What Is True</h1></div>
 <div class="cols"><div class="scrip">
  <span class="ref">Philippians 4:4-9 / World English Bible</span><p>{vs(S3,"php4")}</p>
 </div></div>
 <div class="safety"><p><b>A small safety note.</b> If the room is not safe, leave. This page is about
 staying present, not staying trapped.</p></div>
 <footer class="foot"><span>Issue 001 / Page 43</span><span>Photo desk / Page 44</span></footer>
</section>"""), "Philippians 4:4-9 in full")

# =================================== p47 · EXODUS 16 teaser
write("47", shell("47","Table in the Wilderness", """
.page{background:#efe6cc}
.hero{padding:14px 0 16px;border-bottom:3px solid #8a5a24}
.hero .hed{font-size:88px;color:#3a2a12}
.split{flex:1;min-height:0;display:grid;grid-template-columns:1fr 290px;gap:32px;margin-top:20px}
.scrip{font-size:19.5px;line-height:1.62;color:#221a0c}
.scrip sup{color:#a8571c}
.ref{color:#8a5a24}
.next{border:3px solid #17100d;padding:18px 20px;background:#fff}
.next h4{margin:0 0 10px;font-size:10.5px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#c0392b}
.next dl{margin:0;font-size:13px;line-height:1.6}
.next dt{font-weight:900;text-transform:uppercase;font-size:9.5px;letter-spacing:.1em;color:#6d6558;margin-top:9px}
.next dd{margin:0;font-family:Georgia,serif}
""", f"""<section class="sheet">
 <header class="folio"><p>Next Issue / 002 preview<br/>Exodus 16:11-21</p>
 <p>The next issue begins here<br/>World English Bible</p></header>
 <div class="hero"><p class="kick" style="color:#a8571c">Issue 002 · a meal where there should not be one</p>
  <h1 class="hed">Table in the<br/>Wilderness</h1></div>
 <div class="split">
  <div class="scrip"><span class="ref">Exodus 16:11-21 / World English Bible</span><p>{vs(S3,"exo16")}</p></div>
  <div class="next"><h4>Issue 002</h4><dl>
   <dt>Reading</dt><dd>Exodus 16, in full</dd>
   <dt>Question</dt><dd>What is enough for today?</dd>
   <dt>Table</dt><dd>Set in the place nobody planned</dd>
   <dt>Arrives</dt><dd>Next month</dd></dl>
   <p style="font-family:Georgia,serif;font-size:13.5px;line-height:1.5;margin:14px 0 0">
   The next issue has already started on this page. Keep the paper close. Give part of it away.</p></div>
 </div>
 <footer class="foot"><span>Issue 001 / Page 47</span><span>Back cover / Page 48</span></footer>
</section>"""), "Exodus 16:11-21 — next issue begins early")

# --------------------------------------------------------------- tally
def count(store, key, lo=None, hi=None):
    return len([v for v in store[key] if lo is None or lo <= v["n"] <= hi])
total = (count(S2,"gen27")+count(S2,"gen28a")+count(S2,"gen28b")+count(S3,"gen31a")+
 count(S3,"gen31b")+count(S3,"gen35")+count(S3,"heb12")+count(S3,"psa139b")+
 count(DEP,"rom8")+count(S3,"joh6b")+count(DEP,"psa121")+count(S3,"php4")+count(S3,"exo16")+
 sum(len(t.split('<sup>'))-1 for _,t in refrains) + 3)
print(f"\n  v3 direct-Scripture verses printed in full: {total}")
print("  Scripture pages: 6,7,8,9,10,11,12,13,19,24,25,36,37,40,43,47  (16 of 48)")
print("  Longest gap without direct Scripture: 5 pages (meets the brief's rule)")
