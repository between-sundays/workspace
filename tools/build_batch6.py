#!/usr/bin/env python3
"""Six pages, six different layout systems. Art placed 1:1 where possible."""
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"public","lab")
W,H=941,1346
def shell(n,title,css,body,bg="#fff"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page {n} · {title}</title><link rel="stylesheet" href="fonts.css">
<style>*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{bg}}}
{css}</style></head><body><main class="page">{body}</main></body></html>"""
def w(n,doc): open(os.path.join(OUT,f"between-sundays-page-{n}.html"),"w").write(doc); print("  p"+n)

# ── 06 · GATE TO THE READING — full bleed, almost no type ────────────────────
w("06", shell("06","Gate to the Reading","""
.b{position:absolute;inset:0}.b img{width:100%;height:100%;object-fit:cover;object-position:center 22%}
.v{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,14,20,.55) 0 16%,transparent 34% 58%,rgba(8,14,20,.82))}
.d{position:absolute;left:50%;transform:translateX(-50%);top:52px;font-size:10px;font-weight:800;
 letter-spacing:.42em;text-transform:uppercase;color:#DCEEF5;opacity:.85}
.big{position:absolute;left:60px;right:60px;bottom:150px;margin:0;text-align:center;color:#fff;
 font-size:62px;font-weight:800;line-height:.94;letter-spacing:-.035em;text-transform:uppercase}
.big em{font-style:normal;color:#E8913F}
.sub{position:absolute;left:60px;right:60px;bottom:96px;text-align:center;color:#DCEEF5;
 font-size:15px;font-weight:600;letter-spacing:.02em;opacity:.85}
.f{position:absolute;left:0;right:0;bottom:0;height:44px;display:flex;align-items:center;
 justify-content:space-between;padding:0 44px;font-size:9px;font-weight:800;letter-spacing:.24em;
 text-transform:uppercase;color:#DCEEF5;opacity:.55}""","""
<div class="b"><img src="art/p06-gate.png" alt=""/></div><div class="v"></div>
<div class="d">The Reading begins here</div>
<h1 class="big">The next eight pages<br/>are <em>scripture.</em><br/>Nothing else.</h1>
<p class="sub">No ads. No jokes. No commentary. Genesis 28, printed whole.</p>
<div class="f"><span>Between Sundays · Issue 001</span><span>Page 06</span></div>""","#0B1218"))

# ── 15 · THE PLACE YOU ALMOST WALKED PAST — two half-portraits ───────────────
w("15", shell("15","The Place You Almost Walked Past","""
.l{position:absolute;left:0;top:0;width:470px;height:1346px;overflow:hidden}
.l img{width:100%;height:100%;object-fit:cover;object-position:58% center}
.r{position:absolute;left:470px;top:0;width:471px;height:1346px;background:#1B24C4;color:#fff;
 padding:52px 40px 40px}
.tag{position:absolute;left:0;top:0;background:#FF5A5A;color:#14161A;padding:9px 16px;font-size:9px;
 font-weight:800;letter-spacing:.24em;text-transform:uppercase}
.r h1{margin:44px 0 0;font-size:56px;font-weight:800;line-height:.9;letter-spacing:-.04em;
 text-transform:uppercase}
.r h1 em{font-style:normal;color:#FF5A5A}
.r p{margin:22px 0 0;font-size:16px;line-height:1.5;font-weight:500}
.list{margin-top:30px;border-top:2px solid rgba(255,255,255,.4)}
.list div{padding:13px 0;border-bottom:1px solid rgba(255,255,255,.22);font-size:15px;font-weight:600}
.list b{color:#FF5A5A;margin-right:10px}
.pay{position:absolute;left:40px;right:40px;bottom:96px;font-size:22px;font-weight:800;line-height:1.1;
 letter-spacing:-.02em;text-transform:uppercase;border-top:3px solid #FF5A5A;padding-top:16px}
.v{position:absolute;left:40px;right:40px;bottom:44px;font-size:12px;font-style:italic;opacity:.8}""","""
<div class="l"><img src="art/p15-street-walker.png" alt=""/></div>
<div class="r"><span class="tag">The place you almost walked past</span>
  <h1>He has walked<br/>this street<br/><em>400 times.</em></h1>
  <p>Ask him what is on it and he will say nothing. Ask him to draw it and he cannot.</p>
  <div class="list">
    <div><b>01</b>A door somebody painted on purpose.</div>
    <div><b>02</b>A window with the same plant in it for nine years.</div>
    <div><b>03</b>The spot where the road changes sound under your feet.</div>
    <div><b>04</b>A person who is there every single day.</div>
  </div>
  <p class="pay">Jacob slept on this street. He called it the house of God in the morning.</p>
  <p class="v">"Surely the Lord is in this place, and I was not aware of it." — Genesis 28:16</p>
</div>"""))

# ── 32 · FIND THE CERTAIN PLACE — a game, with tick boxes ────────────────────
BOX="".join(f'<li><i></i><b>{t}</b><span>{s}</span></li>' for t,s in [
 ("A door held open","by someone who did not have to"),
 ("Somebody eating alone","and looking fine about it"),
 ("A place that smells like your childhood",""),
 ("A stranger who says your name",""),
 ("The exact spot the light hits at 4pm",""),
 ("Something you have walked past all week",""),
 ("A person waiting for someone",""),
 ("Weather you would have complained about",""),])
w("32", shell("32","Find the Certain Place","""
.t{position:absolute;left:0;right:0;top:0;height:404px;overflow:hidden;background:#7FA8C4}
.t img{width:100%;height:100%;object-fit:cover;object-position:center 34%}
.k{position:absolute;left:44px;top:36px;font-size:10px;font-weight:800;letter-spacing:.28em;
 text-transform:uppercase;color:#fff}
h1{position:absolute;left:40px;top:250px;margin:0;font-size:64px;font-weight:800;line-height:.86;
 letter-spacing:-.04em;text-transform:uppercase;color:#fff;text-shadow:0 2px 20px rgba(20,40,60,.4)}
h1 em{font-style:normal;color:#FFD34E}
.d{position:absolute;left:44px;right:44px;top:432px;font-size:16px;line-height:1.5;font-weight:500}
ul{position:absolute;left:44px;right:44px;top:512px;list-style:none;margin:0;padding:0;
 display:grid;grid-template-columns:1fr 1fr;gap:0 30px}
li{display:grid;grid-template-columns:30px 1fr;gap:11px;align-items:start;padding:15px 0;
 border-bottom:1px solid rgba(20,30,40,.18)}
li i{width:26px;height:26px;border:2.5px solid #14202A;display:block;margin-top:1px}
li b{font-size:15.5px;font-weight:800;line-height:1.2;grid-column:2}
li span{grid-column:2;font-size:13px;opacity:.65;display:block;margin-top:2px}
.f{position:absolute;left:0;right:0;bottom:0;height:96px;background:#E2542A;color:#fff;
 padding:20px 44px;display:flex;justify-content:space-between;align-items:center}
.f b{font-size:19px;font-weight:800;text-transform:uppercase;letter-spacing:-.01em;max-width:60ch}
.f span{font-size:10px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;opacity:.8}""","""
<div class="t"><img src="art/p32-binoculars.png" alt=""/></div>
<div class="k">Games · look for these</div>
<h1>Find the<br/><em>certain place.</em></h1>
<p class="d">Jacob called it &ldquo;a certain place&rdquo; (Genesis 28:11) because it had no name and nothing in it.
Then it turned out to have everything in it. Tick these off this week.</p>
<ul>"""+BOX+"""</ul>
<div class="f"><b>You will not find all eight. Three is a good week.</b><span>Page 32</span></div>""","#F2EFE6"))
