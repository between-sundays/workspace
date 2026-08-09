#!/usr/bin/env python3
"""
Page 34 — BUT GOD, yearbook edition (replaces the wall).
Dark ground, serif masthead, 16 photo cards each with a name and the thing
they are carrying, white hand-drawn doodles, BUT GOD + verse at the foot.
"""
import os, math, random
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
DARK="#191614"; CREAM="#F2EDE2"; RED="#C8381E"
random.seed(34)
def j(a=1.5): return random.uniform(-a,a)

CARDS=[("f00","Kenji","Job ended Friday."),
       ("f01","Dana","Has not slept right in weeks."),
       ("f03","Amara","New city. Knows nobody yet."),
       ("f04","Hiro","Behind on rent."),
       ("f07","Walt","Lost her in March."),
       ("f08","Marcus","The diagnosis came Tuesday."),
       ("f11","Ray","Retired. Now what?"),
       ("f13","Rosa","Prayed. Heard nothing back."),
       ("f16","Mei","Failed the exam. Again."),
       ("f17","Andre","Cannot forgive his brother."),
       ("f18","Viktor","Says he is fine. He is not."),
       ("f19","Helen","The house got quiet this year."),
       ("f20","Sato","Waiting on a call that has not come."),
       ("f21","Grace","Raising her grandkids."),
       ("f24","Luis","Two jobs. Still short."),
       ("f31","June","Everyone else seems fine.")]

cards="".join(
 f'''<figure class="cd" style="transform:rotate({j(1.2):.2f}deg)">
   <img src="art/faces/{f}.png" alt=""/>
   <figcaption><b>{n}</b><span>{p}</span></figcaption></figure>''' for f,n,p in CARDS)

# white hand doodles
def star(x,y,r,rot=0):
    p=[]
    for k in range(10):
        a=math.radians(rot+k*36); rr=r if k%2==0 else r*.42
        p.append(f"{x+math.cos(a)*rr:.0f} {y+math.sin(a)*rr:.0f}")
    return (f'<path d="M {p[0]} L '+" L ".join(p[1:])+' Z" fill="none" stroke="#F2EDE2" '
            f'stroke-width="2.2" stroke-linejoin="round" opacity=".85"/>')
def spark(x,y,r):
    o=""
    for k in range(4):
        a=math.radians(k*45+18)
        o+=(f'<path d="M {x-math.cos(a)*r:.0f} {y-math.sin(a)*r:.0f} L {x+math.cos(a)*r:.0f} '
            f'{y+math.sin(a)*r:.0f}" stroke="#F2EDE2" stroke-width="2.2" stroke-linecap="round" opacity=".8"/>')
    return o
def squig(x,y,w_):
    return (f'<path d="M {x} {y} q 9 -9 18 0 t 18 0 t 18 0" fill="none" stroke="#F2EDE2" '
            f'stroke-width="2.2" stroke-linecap="round" opacity=".7" transform="scale({w_/54},1) translate(0,0)"/>')
DOODLES=(star(60,150,13,12)+spark(886,132,12)+star(902,646,10,30)+spark(52,700,11)
 +star(70,1105,11,8)+spark(880,1078,12)
 +f'<text x="128" y="86" font-family="Shantell Sans" font-size="17" fill="#F2EDE2" opacity=".75" transform="rotate(-6 128 86)">xoxo</text>'
 +f'<path d="M 130 118 q 20 14 44 6" fill="none" stroke="#F2EDE2" stroke-width="2" opacity=".6"/>')

VERSE="My times are in your hand."   # Psalm 31:15, WEB — fetched
DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 34 · But God</title><link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{DARK};color:{CREAM};
 background-image:radial-gradient(rgba(242,237,226,.045) 1px,transparent 1px);background-size:7px 7px}}
.mast{{position:absolute;left:0;right:0;top:34px;text-align:center}}
.mast h1{{margin:0;font-family:"Fraunces",Georgia,serif;font-size:33px;font-weight:600;letter-spacing:.01em}}
.mast i{{display:block;font-family:"Fraunces",serif;font-style:italic;font-size:16px;opacity:.75;margin-top:3px}}
.grid{{position:absolute;left:44px;right:44px;top:126px;display:grid;
 grid-template-columns:repeat(4,1fr);gap:20px 22px}}
.cd{{margin:0;background:{CREAM};padding:7px 7px 9px;box-shadow:0 5px 16px rgba(0,0,0,.45)}}
.cd img{{display:block;width:100%;height:158px;object-fit:cover;object-position:center 30%}}
.cd b{{display:block;margin-top:8px;text-align:center;font-size:14px;font-weight:800;color:#1B1815}}
.cd span{{display:block;margin-top:3px;text-align:center;font-family:"Newsreader",Georgia,serif;
 font-size:11px;line-height:1.3;color:#3A352E;min-height:29px}}
svg.doo{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:190px;text-align:center;padding-top:14px}}
.foot h2{{margin:0;font-size:74px;font-weight:800;letter-spacing:-.04em;line-height:.9;text-transform:uppercase}}
.foot h2 em{{font-style:normal;color:{RED}}}
.foot p{{margin:10px auto 0;font-size:14.5px;line-height:1.4;font-weight:600;max-width:64ch}}
.foot .v{{margin-top:9px;font-family:"Newsreader",serif;font-style:italic;font-size:13.5px;opacity:.85}}
.foot .v b{{font-style:normal;font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;opacity:.6;margin-left:8px}}
.pg{{position:absolute;right:26px;bottom:12px;font-size:9px;font-weight:800;letter-spacing:.22em;
 text-transform:uppercase;opacity:.4}}
</style></head><body><main class="page">
<div class="mast"><h1>Bethel Community</h1><i>The Class of Right Now</i></div>
<div class="grid">{cards}</div>
<svg class="doo" viewBox="0 0 {W} {H}">{DOODLES}</svg>
<div class="foot">
  <h2>But <em>God</em></h2>
  <p>None of this gets fixed by magic. But God is on time, every time, and he is still in control.</p>
  <div class="v">&ldquo;{VERSE}&rdquo;<b>Psalm 31:15</b></div>
</div>
<span class="pg">Issue 001 · Page 34</span>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-34.html"),"w").write(DOC)
print("p34 yearbook ·",len(CARDS),"cards")
