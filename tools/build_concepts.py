#!/usr/bin/env python3
"""
Seven concept pages, one per reference Adrian sent.
All land in public/lab/ as NEW variants for the compare view.
"""
import os, random, math, html, base64, glob
BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "lab")
os.makedirs(OUT, exist_ok=True)
esc = html.escape
random.seed(7)

W, H = 941, 1346
FONTS = '<link rel="stylesheet" href="fonts.css">'

SHELL = """
*{box-sizing:border-box}
html,body{margin:0}
@page{size:13.07in 18.69in;margin:0}
body{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}
.page{position:relative;width:941px;height:1346px;overflow:hidden;background:#F6F1E4;color:#17100d;
 box-shadow:0 30px 58px rgba(17,16,13,.26)}
.sheet{position:absolute;inset:44px 50px 40px;display:flex;flex-direction:column;z-index:3}
.folio{display:flex;justify-content:space-between;gap:16px;padding-bottom:9px;
 border-bottom:1px solid currentColor;font-size:10px;font-weight:800;letter-spacing:.18em;
 text-transform:uppercase}
.folio span:last-child{text-align:right}
.foot{margin-top:auto;padding-top:10px;border-top:2px solid currentColor;display:flex;
 justify-content:space-between;gap:16px;font-size:10px;font-weight:800;letter-spacing:.16em;
 text-transform:uppercase}
.hed{font-weight:800;letter-spacing:-.03em;line-height:.9;margin:0;text-transform:uppercase}
.kick{margin:0 0 8px;font-size:11px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}
.hand{font-family:"Shantell Sans",cursive;font-weight:700}
.serif{font-family:"Newsreader",Georgia,serif}
"""

def page(n, title, css, body, cls=""):
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
           '<meta name="viewport" content="width=device-width,initial-scale=1"/>'
           f'<title>Between Sundays — Page {n} · {esc(title)}</title>{FONTS}'
           f'<style>{SHELL}{css}</style></head><body>'
           f'<main class="page {cls}">{body}</main></body></html>')
    open(os.path.join(OUT, f"between-sundays-page-{n}.html"), "w").write(doc)
    print(f"  p{n}  {title}")

# ═══════════════════════════════════════════════ 42 · HELP WANTED (tear-off tabs)
ROLES = [("ENCOURAGER","one honest sentence"),("DOOR HOLDER","ten seconds"),
         ("MEAL RUNNER","one casserole"),("RIDE GIVER","one round trip"),
         ("LISTENER","no advice given"),("NOTICER","say what you saw"),
         ("SITTER","stay in the room"),("PRAY-ER","nobody has to know")]
tabs = []
for i,(r,note) in enumerate(ROLES):
    torn = i in (2, 6)                      # two already taken
    tabs.append(
      f'<div class="tab{" torn" if torn else ""}" style="transform:rotate({random.uniform(-2.2,2.2):.1f}deg)">'
      + ('' if torn else f'<b>{r}</b><span>{note}</span><i>take one</i>')
      + ('<em>taken</em>' if torn else '') + '</div>')
page("42","Help Wanted — tear-off tabs","""
.page{background:#2B2A26}
.poster{position:absolute;left:64px;right:64px;top:56px;bottom:52px;background:#F2E7C9;
 box-shadow:0 24px 48px rgba(0,0,0,.5);transform:rotate(-.6deg);
 display:flex;flex-direction:column;padding:38px 40px 0}
.tape{position:absolute;width:132px;height:34px;background:rgba(214,196,150,.85);
 border:1px solid rgba(120,105,70,.35)}
.t1{top:30px;left:96px;transform:rotate(-7deg)}
.t2{top:30px;right:120px;transform:rotate(6deg)}
.eye{font-family:"Shantell Sans",cursive;font-weight:700;font-size:19px;color:#B33A20;margin-top:26px}
.big{font-family:"Shantell Sans",cursive;font-weight:700;font-size:82px;line-height:.92;margin:10px 0 0}
.sub{font-family:"Shantell Sans",cursive;font-size:22px;line-height:1.35;margin:16px 0 0;max-width:44ch}
.rule{height:3px;background:#2B2A26;margin:20px 0 0}
.list{margin-top:16px;font-family:"Shantell Sans",cursive;font-size:19px;line-height:1.55}
.slots{margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:14px 30px;
 font-family:"Shantell Sans",cursive;font-size:17px;line-height:1.35}
.slot{display:flex;gap:10px;align-items:baseline;border-bottom:1.5px dotted rgba(43,42,38,.4);
 padding-bottom:7px}
.slot b{font-size:15px;letter-spacing:.02em;white-space:nowrap}
.slot span{color:#6B5E38;font-size:14px}
.pointer{margin-top:auto;display:flex;align-items:flex-end;gap:14px;padding-bottom:10px}
.pointer p{margin:0;font-family:"Shantell Sans",cursive;font-size:20px;color:#B33A20;line-height:1.2}
.tabs{margin-top:auto;display:flex;gap:7px;align-items:flex-end;padding-bottom:0}
.tab{flex:1;height:196px;background:#F2E7C9;border-left:1px dashed #8C7C50;border-right:1px dashed #8C7C50;
 border-top:2px dashed #8C7C50;display:flex;flex-direction:column;align-items:center;
 justify-content:flex-start;padding:12px 4px;text-align:center;
 font-family:"Shantell Sans",cursive}
.tab b{writing-mode:vertical-rl;transform:rotate(180deg);font-size:15px;letter-spacing:.04em;
 margin-bottom:6px}
.tab span{writing-mode:vertical-rl;transform:rotate(180deg);font-size:10.5px;color:#6B5E38}
.tab i{margin-top:auto;font-style:normal;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;
 color:#B33A20}
.tab.torn{background:#2B2A26;border-color:transparent;align-items:center;justify-content:center}
.tab.torn em{font-style:normal;writing-mode:vertical-rl;transform:rotate(180deg);
 font-size:12px;color:#6B6455;letter-spacing:.2em;text-transform:uppercase}
.pg{position:absolute;bottom:18px;right:70px;color:#F2E7C9;font-size:10px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;z-index:5}
""", f"""
<div class="poster">
  <div class="tape t1"></div><div class="tape t2"></div>
  <div class="eye">the noticeboard outside the room where it happens</div>
  <div class="big">HELP<br/>WANTED</div>
  <div class="sub">Small jobs. No experience necessary. Nobody checks your qualifications
  and nobody keeps a record. Tear one off and do it this week.</div>
  <div class="rule"></div>
  <div class="list">
    · no interview · no start date · no notice period<br/>
    · pay: someone is less alone on a Tuesday<br/>
    · two positions already taken — the tabs are gone<br/>
    · full job description on file: &ldquo;Share each other&rsquo;s burdens&rdquo; — Galatians 6:2
  </div>
  <div class="slots">
    <div class="slot"><b>ENCOURAGER</b><span>one honest sentence, said out loud</span></div>
    <div class="slot"><b>DOOR HOLDER</b><span>ten seconds, no thanks expected</span></div>
    <div class="slot"><b>MEAL RUNNER</b><span>doorstep drop, no staying required</span></div>
    <div class="slot"><b>RIDE GIVER</b><span>one round trip, radio optional</span></div>
    <div class="slot"><b>LISTENER</b><span>no advice given, none at all</span></div>
    <div class="slot"><b>NOTICER</b><span>say the thing you noticed</span></div>
    <div class="slot"><b>SITTER</b><span>stay in the room after it gets quiet</span></div>
    <div class="slot"><b>PRAY-ER</b><span>nobody has to know you did</span></div>
  </div>
  <div class="pointer"><p>tear one off ↓<br/><span style="font-size:15px;color:#6B5E38">two are already gone</span></p></div>
  <div class="tabs">{''.join(tabs)}</div>
</div>
<div class="pg">Issue 001 / Page 42 · Help Wanted</div>""")

# ═══════════════════════════════════════════════ 45 · MARK THE PLACE (post-its)
NOTES = [
 ("#FCE96A","the parking lot at 6am","filled"),("#FCE96A","","blank"),
 ("#B6E3F4","room 14 hallway","filled"),("#FCE96A","","blank"),
 ("#F9C6D9","the 22 bus, upper deck","filled"),("#C9EFC0","","blank"),
 ("#FCE96A","kitchen, after they went to bed","filled"),("#B6E3F4","","blank"),
 ("#F9C6D9","","blank"),("#FCE96A","gate B22, hour five","filled"),
 ("#C9EFC0","","blank"),("#FCE96A","the laundromat","filled"),
 ("#B6E3F4","","blank"),("#F9C6D9","the stairwell at work","filled"),
 ("#FCE96A","","blank"),("#C9EFC0","","blank"),
]
cells = "".join(
  f'<div class="note {k}" style="background:{c};transform:rotate({random.uniform(-3.4,3.4):.1f}deg)">'
  f'{"<span>"+esc(t)+"</span>" if t else "<i></i>"}</div>' for c,t,k in NOTES)
page("45","Mark the Place — the wall","""
.page{background:#EDEAE2}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);
 grid-template-rows:repeat(4,1fr);gap:22px;margin-top:20px}
.note{position:relative;display:flex;align-items:center;justify-content:center;padding:16px;
 box-shadow:5px 8px 14px rgba(23,16,13,.18);font-family:"Shantell Sans",cursive}
.note:before{content:"";position:absolute;top:0;left:0;right:0;height:16px;
 background:rgba(255,255,255,.28)}
.note span{font-size:18px;line-height:1.25;text-align:center}
.note i{display:block;width:70%;border-bottom:1.5px solid rgba(23,16,13,.25);height:52%}
.hd{padding-bottom:4px}
.hd .hed{font-size:74px}
.hd p{margin:12px 0 0;font-family:"Newsreader",serif;font-size:18px;line-height:1.45;max-width:70ch}
""", f"""<section class="sheet">
 <header class="folio"><span>Participation<br/>Issue 001</span><span>Sixteen notes · nine are yours<br/>Genesis 28:16</span></header>
 <div class="hd"><p class="kick" style="color:#B33A20;margin-top:16px">Mark the place</p>
  <h1 class="hed">Where Were<br/>You Standing?</h1>
  <p>Seven of these are already filled in by people who read the first draft. The blank ones are
  yours. Write the most ordinary place you have been this week — then look at it again on Sunday.</p></div>
 <div class="grid">{cells}</div>
 <footer class="foot"><span>Issue 001 / Page 45</span><span>Then tell us: betweensundays.com/found</span></footer>
</section>""")

# ═══════════════════════════════════════════════ 35 · NO DEAD ZONES (repeated type)
lines = []
for i in range(15):
    lines.append('<div class="ln">I AM WITH YOU.</div>' if i % 2 == 0
                 else '<div class="ln alt">WHEREVER YOU GO.</div>')
OBJ = [("#D9433A","ticket",-9),("#2F6BB5","cap",14),("#E8B93C","key",-22),
       ("#3F7F4E","stub",7),("#C9553F","receipt",-14),("#8A6FC4","token",19),
       ("#D9A13A","coin",-5),("#2F6BB5","pass",25)]
objs = "".join(
  f'<div class="ob" style="left:{random.uniform(18,72):.0f}%;top:{random.uniform(30,66):.0f}%;'
  f'transform:rotate({r}deg);background:{c};width:{random.randint(66,132)}px;'
  f'height:{random.randint(34,74)}px"><b>{t}</b></div>' for c,t,r in OBJ)
page("35","No Dead Zones — repeated","""
.page{background:#FBFAF7}
.stack{position:absolute;inset:74px 46px 92px;display:flex;flex-direction:column;
 justify-content:space-between;z-index:2}
.ln{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:60px;line-height:.92;
 letter-spacing:-.035em;white-space:nowrap;color:#17100d}
.ln.alt{color:#17100d;opacity:.92}
.objs{position:absolute;inset:0;z-index:3;pointer-events:none}
.ob{position:absolute;border:2px solid rgba(23,16,13,.55);border-radius:3px;
 box-shadow:0 10px 22px rgba(23,16,13,.3);display:grid;place-items:center}
.ob b{font-size:10px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#fff;
 opacity:.9}
.tagline{position:absolute;left:46px;right:46px;bottom:34px;display:flex;justify-content:space-between;
 gap:18px;align-items:flex-end;z-index:4;border-top:2px solid #17100d;padding-top:10px}
.tagline p{margin:0;font-family:"Newsreader",serif;font-size:15px;line-height:1.4;max-width:64ch}
.tagline span{font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 white-space:nowrap}
.top{position:absolute;top:32px;left:46px;right:46px;display:flex;justify-content:space-between;
 font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;z-index:4;
 border-bottom:1px solid #17100d;padding-bottom:8px}
""", f"""
<div class="top"><span>House Campaign · No Dead Zones</span><span>Genesis 28:15</span></div>
<div class="stack">{''.join(lines)}</div>
<div class="objs">{objs}</div>
<div class="tagline">
 <p>Everything you are carrying fell through the middle of the sentence and the sentence
 did not break. No towers. No roaming charges. No perfect itinerary required.</p>
 <span>Issue 001 / Page 35</span>
</div>""")

# ═══════════════════════════════════════════════ 21 · FILMS FOR THE ROAD (painted)
def poster(sky, ground, ink, shape, title, meta, stars):  # ink unused for caption
    return f'''<figure class="film">
      <div class="art" style="background:linear-gradient(180deg,{sky} 0 58%,{ground} 58%)">
        {shape}
      </div>
      <figcaption><b>{title}</b><span>{meta}</span><i>{stars}</i></figcaption>
    </figure>'''
p1 = poster("#7FB2DE","#3F7F4E","#1E3A2B",
  '<div class="pal"></div><div class="road"></div><div class="car"></div>',
  "A CERTAIN PLACE","dir. unknown · 94 min · road picture","★★★★☆")
p2 = poster("#E9C77A","#B4552F","#5A2415",
  '<div class="sun"></div><div class="dune"></div>',
  "THE LONG WAY BACK","dir. unknown · 111 min · desert","★★★★★")
p3 = poster("#2C3E63","#151E33","#E8D9A8",
  '<div class="moon"></div><div class="win"></div><div class="win w2"></div>',
  "ROOM 14","dir. unknown · 88 min · night shift","★★★☆☆")
page("21","Films for the Road — painted posters","""
.page{background:#F3EFE3}
.row{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:20px}
.film{margin:0}
.art{position:relative;height:556px;border:3px solid #17100d;overflow:hidden;
 box-shadow:0 12px 26px rgba(23,16,13,.22)}
.art>div{position:absolute}
.pal{left:22px;top:52px;width:10px;height:118px;background:#5A3E22;
 box-shadow:-16px -30px 0 -4px #2F6B3F,16px -30px 0 -4px #2F6B3F,0 -44px 0 -3px #2F6B3F}
.road{left:-10%;right:-10%;top:58%;height:16px;background:#E8DFC6;transform:rotate(-2deg)}
.car{left:30%;top:50%;width:126px;height:52px;background:#1E5B36;border-radius:26px 30px 6px 6px;
 box-shadow:0 9px 0 -3px rgba(0,0,0,.4),34px -18px 0 -12px #1E5B36}
.sun{right:34px;top:44px;width:74px;height:74px;border-radius:50%;background:#F0E0A4}
.dune{left:-6%;right:-6%;top:52%;height:60%;background:#C4682F;border-radius:60% 50% 0 0}
.moon{left:44px;top:40px;width:52px;height:52px;border-radius:50%;background:#E8D9A8}
.win{right:40px;top:210px;width:64px;height:88px;background:#E8C15B}
.win.w2{right:120px;top:246px;height:56px;background:#B99A45}
figcaption{padding-top:11px}
figcaption b{display:block;font-family:"Bricolage Grotesque",sans-serif;font-weight:800;
 font-size:23px;line-height:1.05;letter-spacing:-.02em}
figcaption span{display:block;font-family:"Newsreader",serif;font-size:13px;color:#6B6455;margin-top:5px}
figcaption i{display:block;font-style:normal;font-size:14px;color:#B33A20;margin-top:5px;letter-spacing:.14em}
.hd .hed{font-size:70px}
.hd p{margin:12px 0 0;font-family:"Newsreader",serif;font-size:17px;line-height:1.45;max-width:76ch}
.note{margin-top:26px;font-family:"Newsreader",serif;font-size:15px;line-height:1.45;
 border-top:2px solid #17100d;padding-top:12px;max-width:78ch}
""", f"""<section class="sheet">
 <header class="folio"><span>Culture · The film desk<br/>Issue 001</span><span>Three pictures<br/>None of them exist yet</span></header>
 <div class="hd"><p class="kick" style="color:#B33A20;margin-top:16px">Now showing, nowhere</p>
  <h1 class="hed">Films for<br/>the Road</h1>
  <p>Three films this desk would like somebody to make. Posters painted by hand,
  because a road picture has never once been sold with a photograph.</p></div>
 <div class="row">{p1}{p2}{p3}</div>
 <p class="note">Every one of these is the same film, which is the same story on page 7:
 someone leaves, stops somewhere unremarkable, and finds out they were accompanied the whole way.
 Hollywood has been remaking Genesis 28 for a hundred years without crediting it.</p>
 <footer class="foot"><span>Issue 001 / Page 21</span><span>Obituaries / Page 22</span></footer>
</section>""")

# ═══════════════════════════════════════════════ 14 · MY PLANS / GOD'S PLAN
mass = []
for i in range(720):
    a = random.uniform(0, math.pi*2); rad = random.uniform(0, 1) ** .55
    cx = 620 + math.cos(a)*rad*430; cy = 700 + math.sin(a)*rad*470
    if cx < 250: continue
    r = random.uniform(11, 25)
    tone = random.choice(["#8E0F17","#A5121C","#B81622","#6E0A11","#C41F2B","#7C0D14"])
    mass.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{tone}"/>')
    mass.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r*0.52:.0f}" fill="none" '
                f'stroke="#5E070D" stroke-width="1.6" opacity=".55"/>')
page("14","After the Reading — my plans / God's plan","""
.page{background:#120C0C}
.art{position:absolute;inset:0;z-index:1}
.lamp{position:absolute;left:88px;top:300px;width:132px;height:9px;background:#F4E3B8;
 box-shadow:0 0 60px 26px rgba(244,227,184,.34);z-index:2}
.ledge{position:absolute;left:56px;top:520px;width:250px;height:13px;background:#2A1E1A;z-index:2;
 box-shadow:0 10px 26px rgba(0,0,0,.6)}
.small{position:absolute;left:96px;top:470px;z-index:3}
.small svg{display:block}
.lab{position:absolute;z-index:4;font-family:"Newsreader",serif;font-size:22px;color:#F4EDE2;
 letter-spacing:.01em}
.lab.a{left:78px;top:432px}
.lab.b{left:470px;top:706px;font-size:26px}
.copy{position:absolute;left:56px;right:56px;bottom:44px;z-index:5;border-top:1px solid rgba(244,237,226,.4);
 padding-top:14px;display:flex;justify-content:space-between;gap:24px;align-items:flex-end}
.copy p{margin:0;font-family:"Newsreader",serif;font-size:17px;line-height:1.45;color:#EDE4D6;max-width:62ch}
.copy span{font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#B9AC98;
 white-space:nowrap}
.top{position:absolute;top:34px;left:56px;right:56px;z-index:5;display:flex;justify-content:space-between;
 font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:#B9AC98;
 border-bottom:1px solid rgba(244,237,226,.3);padding-bottom:9px}
.verse{position:absolute;left:56px;top:600px;z-index:5;font-family:"Newsreader",serif;
 font-size:19px;line-height:1.45;color:#EDE4D6;max-width:22ch;font-style:italic;opacity:.92}
""", f"""
<svg class="art" viewBox="0 0 941 1346" xmlns="http://www.w3.org/2000/svg">
 <defs><radialGradient id="glow" cx="14%" cy="26%" r="42%">
   <stop offset="0" stop-color="#3A2A22"/><stop offset="1" stop-color="#120C0C"/></radialGradient></defs>
 <rect width="941" height="1346" fill="url(#glow)"/>
 {''.join(mass)}
</svg>
<div class="lamp"></div><div class="ledge"></div>
<div class="small"><svg width="150" height="60" viewBox="0 0 150 60">
  <path d="M10 46 L96 30" stroke="#3E6B39" stroke-width="3"/>
  <path d="M14 50 L92 36" stroke="#3E6B39" stroke-width="3"/>
  <circle cx="104" cy="27" r="12" fill="#A5121C"/><circle cx="104" cy="27" r="6" fill="none" stroke="#5E070D" stroke-width="1.6"/>
  <circle cx="120" cy="34" r="10" fill="#8E0F17"/><circle cx="120" cy="34" r="5" fill="none" stroke="#5E070D" stroke-width="1.4"/>
  <circle cx="92" cy="40" r="9" fill="#B81622"/>
</svg></div>
<div class="top"><span>After the Reading · Issue 001</span><span>Genesis 28:16</span></div>
<div class="lab a">my plans</div>
<div class="lab b">God's plan</div>
<p class="verse">"Surely the LORD is in this place, and I didn't know it."</p>
<div class="copy">
 <p>You have just read four chapters in which a man makes plans twice, and both times the thing
 that actually holds is the promise he did nothing to arrange. The small bunch on the ledge is
 not wrong. It is just not the whole room.</p>
 <span>Issue 001 / Page 14</span>
</div>""")

# ═══════════════════════════════════════════════ 39 · POSTER (photos inside letters)
ph = "/v4/photos"
page("39","Poster — type with photographs inside","""
.page{background:#F2EFE6}
.poster{position:absolute;inset:84px 52px 128px;display:flex;flex-direction:column;justify-content:center}
.big{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:158px;line-height:.84;
 letter-spacing:-.045em;text-transform:uppercase;margin:0}
.big .cut{-webkit-background-clip:text;background-clip:text;color:transparent;
 background-size:cover;background-position:center}
.c1{background-image:url("photos/road_sunrise_lot.jpg")}
.c2{background-image:url("photos/laundromat_bw.jpg")}
.c3{background-image:url("photos/underpass.jpg")}
.c4{background-image:url("photos/dawn_sky.jpg")}
.sub{font-family:"Newsreader",serif;font-size:25px;line-height:1.4;margin:34px 0 0;max-width:52ch}
.top{position:absolute;top:34px;left:56px;right:56px;display:flex;justify-content:space-between;
 font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 border-bottom:1px solid #17100d;padding-bottom:9px}
.found{position:absolute;left:56px;right:56px;bottom:40px;display:flex;justify-content:space-between;
 gap:20px;align-items:flex-end;border-top:2px solid #17100d;padding-top:12px}
.found .box{border:2px solid #17100d;padding:10px 14px;font-size:11px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;line-height:2.1}
.found .box u{text-decoration:none;border-bottom:1px solid rgba(23,16,13,.4);padding:0 34px}
.found p{margin:0;font-family:"Newsreader",serif;font-size:15px;line-height:1.4;max-width:44ch}
""", """
<div class="top"><span>Tear-out poster · Issue 001</span><span>Genesis 28:16</span></div>
<div class="poster">
  <h1 class="big">SURELY<br/><span class="cut c1">GOD</span> IS<br/>IN <span class="cut c2">THIS</span><br/><span class="cut c3">PLACE</span>.</h1>
  <p class="sub">And I didn't know it. Take this page out and put it where you keep forgetting.</p>
</div>
<div class="found">
  <p>The letters are filled with four ordinary places: a parking lot at sunrise, a laundromat,
  an underpass, and the sky over a plane. None of them look holy either.</p>
  <div class="box">Found here <u></u><br/>Date <u></u></div>
</div>""")

# ═══════════════════════════════════════════════ 31 · BLESSINGS IN PLAIN SIGHT
BL = "blessings.webp" if os.path.exists(os.path.join(OUT, "blessings.webp")) else None
page("31","Games — Blessings in Plain Sight","""
.page{background:#EFEAE0;padding:0}
.art{position:absolute;inset:0;z-index:1}
.art img{width:100%;height:100%;object-fit:cover;display:block}
.bar{position:absolute;left:0;right:0;top:0;z-index:3;display:flex;justify-content:space-between;
 padding:14px 26px;background:rgba(246,241,228,.94);border-bottom:2px solid #17100d;
 font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}
.under{position:absolute;left:0;right:0;bottom:0;z-index:3;padding:14px 26px;
 background:rgba(246,241,228,.94);border-top:2px solid #17100d;display:flex;
 justify-content:space-between;gap:20px;align-items:flex-end}
.under p{margin:0;font-family:"Newsreader",serif;font-size:15px;line-height:1.4;max-width:66ch}
.under span{font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;white-space:nowrap}
""", (f'<div class="art"><img src="{BL}" alt=""></div>' if BL else
      '<div class="art" style="background:#DDD"></div>') + """
<div class="bar"><span>Games · Seek and find</span><span>James 1:17 · eight hidden</span></div>
<div class="under">
 <p><b>Blessings in Plain Sight.</b> Eight of them are in this street. Nobody in the picture is
 looking for any of them, which is roughly the point. Answers are not printed —
 you either find them or you walk past them, same as the rest of the week.</p>
 <span>Issue 001 / Page 31</span>
</div>""")

print("\n7 concept pages -> public/lab/")
