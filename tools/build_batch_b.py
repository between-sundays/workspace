#!/usr/bin/env python3
"""Batch B — pages 05, 19, 27, 35. Four more layout systems."""
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"public","lab")
W,H=941,1346
def shell(n,t,css,body,bg="#fff"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page {n} · {t}</title><link rel="stylesheet" href="fonts.css">
<style>*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{bg}}}
{css}</style></head><body><main class="page">{body}</main></body></html>"""
def w(n,d): open(os.path.join(OUT,f"between-sundays-page-{n}.html"),"w").write(d); print("  p"+n)

# ── 05 · WAYFARER — half-landscape art + two quarters ───────────────────────
TAKE="".join(f"<li><b>{i+1}</b>{t}</li>" for i,t in enumerate([
 "A coat. It is going to rain.","One thing that is actually yours.",
 "The name of one person you can call.","Something to eat.",
 "A reason. It is allowed to be small."]))
w("05", shell("05","Wayfarer","""
.a{position:absolute;left:0;top:0;width:941px;height:673px;overflow:hidden;background:#2C3540}
.a img{width:100%;height:100%;object-fit:cover;object-position:center 46%}
.k{position:absolute;left:40px;top:34px;font-size:10px;font-weight:800;letter-spacing:.28em;
 text-transform:uppercase;color:#F3E7DA}
h1{position:absolute;left:36px;top:452px;margin:0;width:600px;font-size:58px;font-weight:800;
 line-height:.88;letter-spacing:-.04em;text-transform:uppercase;color:#fff}
h1 em{font-style:normal;color:#F0872F}
.tag{position:absolute;right:16px;bottom:14px;font-size:8px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;color:#fff;opacity:.5}
.qL{position:absolute;left:0;top:673px;width:470px;height:673px;border-top:3px solid #201C18;
 padding:26px 26px 30px}
.qR{position:absolute;left:470px;top:673px;width:471px;height:673px;border-top:3px solid #201C18;
 border-left:1px solid rgba(32,28,24,.25);padding:26px 26px 30px;background:#F0872F;color:#fff}
h2{margin:0;font-size:24px;font-weight:800;letter-spacing:-.02em;text-transform:uppercase}
.fo{display:flex;justify-content:space-between;font-size:8.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.5;border-bottom:1px solid currentColor;padding-bottom:6px;margin-bottom:14px}
ul{list-style:none;margin:16px 0 0;padding:0}
li{display:flex;gap:12px;align-items:baseline;padding:12px 0;border-bottom:1px solid rgba(32,28,24,.18);
 font-size:16px;font-weight:600;line-height:1.3}
li b{color:#C4581F;font-size:11px;letter-spacing:.1em}
.tk{margin-top:18px;border:2px solid #fff;padding:16px 18px}
.tk div{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px dotted rgba(255,255,255,.5);
 font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.tk div:last-child{border:0}
.tk span{opacity:.8}
.nb{margin-top:16px;font-size:14px;line-height:1.45;font-weight:500}
.pay{position:absolute;left:26px;right:26px;bottom:26px;font-size:15px;font-weight:800;
 line-height:1.15;text-transform:uppercase;letter-spacing:-.01em}""","""
<div class="a"><img src="art/p05-cliff-walk.png" alt=""/></div>
<div class="k">Wayfarer</div>
<h1>You did not<br/>pick the <em>weather.</em></h1>
<span class="tag">Half page · landscape</span>
<section class="qL"><div class="fo"><span>Wayfarer</span><span>Page 05</span></div>
  <h2>What to take</h2><ul>"""+TAKE+"""</ul>
  <p class="pay">Jacob left home with a stick. That is the entire packing list on record &mdash; his own words, Genesis 32:10.</p>
</section>
<section class="qR"><div class="fo"><span>Departure card</span><span>Page 05</span></div>
  <h2>Where you<br/>are going</h2>
  <div class="tk">
    <div>From<span>where you were</span></div>
    <div>To<span>not printed</span></div>
    <div>Leaves<span>already left</span></div>
    <div>Arrives<span>&mdash;</span></div>
    <div>Seat<span>yours</span></div>
  </div>
  <p class="nb">Almost nobody gets the whole route up front. You get the next bit of road
  and the weather you are in.</p>
</section>""","#F4F1EA"))

# ── 19 · SPORTS — a results table nobody attended ───────────────────────────
LOG="".join(f'<tr><td>{d}</td><td>{x}</td><td>{wt}</td><td class="c">{c}</td></tr>'
  for d,x,wt,c in [("Mon","6.2 km","0","Counted"),("Tue","Rest","0","Counted"),
   ("Wed","8.0 km","0","Counted"),("Thu","6.2 km","1 dog","Counted"),
   ("Fri","Rest","0","Counted"),("Sat","14.5 km","0","Counted"),("Sun","Walked","0","Counted")])
w("19", shell("19","Sports","""
.a{position:absolute;left:0;top:0;right:0;height:760px;overflow:hidden}
.a img{width:100%;height:100%;object-fit:cover;object-position:center 40%}
.a:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,16,12,.5) 0 18%,transparent 40%,rgba(10,16,12,.75))}
.k{position:absolute;left:40px;top:34px;font-size:10px;font-weight:800;letter-spacing:.28em;
 text-transform:uppercase;color:#DCE6D6;z-index:2}
h1{position:absolute;left:36px;top:470px;margin:0;font-size:84px;font-weight:800;line-height:.84;
 letter-spacing:-.045em;text-transform:uppercase;color:#fff;z-index:2}
h1 em{font-style:normal;color:#D6E24A}
.sub{position:absolute;left:40px;right:40px;top:690px;color:#DCE6D6;font-size:16px;font-weight:600;z-index:2}
table{position:absolute;left:40px;right:40px;top:792px;border-collapse:collapse;width:calc(100% - 80px)}
th{font-size:8.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;opacity:.5;
 text-align:left;padding:0 0 8px;border-bottom:2px solid #1B2418}
td{padding:11px 0;border-bottom:1px solid rgba(27,36,24,.18);font-size:16px;font-weight:600}
td.c{text-align:right;color:#4A6B2E;font-weight:800}
.pay{position:absolute;left:40px;right:40px;bottom:92px;border-top:3px solid #1B2418;padding-top:14px;
 font-size:22px;font-weight:800;line-height:1.12;text-transform:uppercase;letter-spacing:-.02em}
.v{position:absolute;left:40px;right:40px;bottom:44px;font-size:12.5px;font-style:italic;opacity:.68}""","""
<div class="a"><img src="art/p19-runner.png" alt=""/></div>
<div class="k">Sports &#183; away team advantage</div>
<h1>Nobody saw<br/><em>this one.</em></h1>
<p class="sub">No crowd, no clock, no result anybody prints. One week of a season.</p>
<table><tr><th>Day</th><th>Distance</th><th>Witnesses</th><th>Counted</th></tr>"""+LOG+"""</table>
<p class="pay">The season gets decided in the weeks nobody writes about.</p>
<p class="v">"Your Father who sees in secret will reward you." &mdash; Matthew 6:6</p>""","#F1F3EE"))

# ── 27 · IF THE MIDDLE IS MISSING — split, colour field left ────────────────
w("27", shell("27","If the Middle Is Missing","""
.r{position:absolute;right:0;top:0;width:430px;height:1346px;overflow:hidden}
.r img{width:100%;height:100%;object-fit:cover;object-position:44% center}
.l{position:absolute;left:0;top:0;width:511px;height:1346px;background:#2F5D3A;color:#F1EDE0;
 padding:56px 40px 44px}
.k{font-size:10px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;color:#D9E86A}
h1{margin:26px 0 0;font-size:62px;font-weight:800;line-height:.88;letter-spacing:-.04em;
 text-transform:uppercase}
h1 em{font-style:normal;color:#D9E86A}
p{margin:22px 0 0;font-size:16.5px;line-height:1.5;font-weight:500}
.box{margin-top:30px;border:2px solid rgba(241,237,224,.5);padding:18px 20px}
.box b{display:block;font-size:11px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 color:#D9E86A;margin-bottom:9px}
.box p{margin:0;font-size:15px}
.pay{position:absolute;left:40px;right:40px;bottom:96px;font-size:26px;font-weight:800;line-height:1.08;
 text-transform:uppercase;letter-spacing:-.02em;border-top:3px solid #D9E86A;padding-top:16px}
.f{position:absolute;left:40px;right:40px;bottom:44px;font-size:9px;font-weight:800;letter-spacing:.22em;
 text-transform:uppercase;opacity:.6}""","""
<div class="r"><img src="art/p27-ferns.png" alt=""/></div>
<div class="l">
  <div class="k">After the spine</div>
  <h1>Somebody<br/>took the<br/><em>middle</em><br/>out of this<br/>paper.</h1>
  <p>Four pages. Gone. If you are holding a copy with a hole in it, that is not damage.
  That is the paper working.</p>
  <div class="box"><b>What was in there</b>
    <p>A short letter for somebody who did not buy this. A promise printed whole
    &mdash; Psalm 139:7&ndash;12, the one about nowhere being too far. Room to write.
    And an address for what to do next.</p></div>
  <p>Whoever tore it out left it somewhere on purpose &mdash; a bus seat, a break room,
  a waiting room. It was never yours to keep.</p>
  <p class="pay">Good. That is where it was going.</p>
  <div class="f">Between Sundays &#183; Issue 001 &#183; Page 27</div>
</div>""","#2F5D3A"))

# ── 35 · NO DEAD ZONES — signal meters ──────────────────────────────────────
BARS="".join(
 f'<div class="row"><span>{lab}</span><div class="bar">'
 + "".join(f'<i class="{"on" if k<n else ""}"></i>' for k in range(5))
 + f'</div><b>{note}</b></div>' for lab,n,note in [
   ("Phone signal",5,"Full"),("Notifications",5,"Full"),("Group chats",5,"Full"),
   ("Things you actually said today",1,"Weak"),("Things you meant",0,"None"),
   ("Somebody who knows how you are",1,"Weak")])
w("35", shell("35","No Dead Zones","""
.a{position:absolute;left:0;top:0;right:0;height:600px;overflow:hidden;background:#C9C08E}
.a img{width:100%;height:100%;object-fit:cover;object-position:center 42%}
.k{position:absolute;left:40px;top:34px;font-size:10px;font-weight:800;letter-spacing:.28em;
 text-transform:uppercase;color:#1B1B18;background:#E8E45C;padding:6px 12px}
h1{position:absolute;left:36px;right:36px;top:636px;margin:0;font-size:74px;font-weight:800;
 line-height:.86;letter-spacing:-.045em;text-transform:uppercase;color:#141412}
h1 em{font-style:normal;color:#E0543A}
.d{position:absolute;left:40px;right:40px;top:812px;font-size:16px;line-height:1.45;font-weight:500}
.meters{position:absolute;left:40px;right:40px;top:884px}
.row{display:grid;grid-template-columns:1fr 190px 96px;gap:18px;align-items:center;padding:13px 0;
 border-bottom:1px solid rgba(20,20,18,.18)}
.row span{font-size:16px;font-weight:700}
.bar{display:flex;gap:5px}
.bar i{flex:1;height:22px;background:rgba(20,20,18,.13);display:block}
.bar i.on{background:#141412}
.row b{text-align:right;font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 opacity:.55}
.pay{position:absolute;left:0;right:0;bottom:0;background:#E0543A;color:#fff;padding:24px 40px 26px}
.pay b{font-size:26px;font-weight:800;line-height:1.08;text-transform:uppercase;letter-spacing:-.02em;
 display:block;max-width:34ch}
.pay span{display:block;margin-top:10px;font-size:13px;font-weight:600;opacity:.9}""","""
<div class="a"><img src="art/p35-train-glitch.png" alt=""/></div>
<div class="k">No dead zones</div>
<h1>Full bars.<br/>Nothing <em>getting through.</em></h1>
<p class="d">Coverage has never been better. Here is this week&rsquo;s reading.</p>
<div class="meters">"""+BARS+"""</div>
<div class="pay"><b>You are not out of range. You are just not picking up.</b>
  <span>The still small voice has never needed bars &mdash; 1 Kings 19:12. Try one call today that is not a text.</span></div>""","#F4F2E8"))
