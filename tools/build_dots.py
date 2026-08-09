#!/usr/bin/env python3
"""
Connect-the-dots pair.
  lab/p46   John 21:6  — the sea page; dots under the waterline spell THE RIGHT SIDE
  labb/p45  Amos 9:13  — the dominoes page; dots spell BLESSINGS ARE ON THE WAY (+ TO __ freehand)
Dots are generated from real letterform strokes, numbered globally; a small star
marks every pencil-lift. A solved overlay is rendered separately for verification.
"""
import os, math, shutil
BASE=os.path.dirname(os.path.abspath(__file__))
LAB=os.path.join(BASE,"public","lab"); LABB=os.path.join(BASE,"public","labb")
W,H=941,1346

# single-ink letterforms: letter -> list of strokes -> list of (x,y) on a 4x6 grid
L={ "A":[[(0,6),(0,2),(2,0),(4,2),(4,6)],[(0,3.5),(4,3.5)]],
    "B":[[(0,6),(0,0),(3,0),(3,3),(0,3),(4,3),(4,6),(0.7,6)]],
    "D":[[(0,6),(0,0),(3,0),(4,1.5),(4,4.5),(3,6),(0.7,6)]],
    "E":[[(4,0),(0,0),(0,6),(4,6)],[(0,3),(3,3)]],
    "G":[[(4,1),(3,0),(1,0),(0,1),(0,5),(1,6),(3,6),(4,5),(4,3),(2,3)]],
    "H":[[(0,0),(0,6)],[(4,0),(4,6)],[(0,3),(4,3)]],
    "I":[[(1,0),(3,0)],[(2,0),(2,6)],[(1,6),(3,6)]],
    "L":[[(0,0),(0,6),(4,6)]],
    "N":[[(0,6),(0,0),(4,6),(4,0)]],
    "O":[[(1,0),(3,0),(4,1),(4,5),(3,6),(1,6),(0,5),(0,1)]],
    "R":[[(0,6),(0,0),(3,0),(4,1),(3,3),(0,3)],[(2,3),(4,6)]],
    "S":[[(4,1),(3,0),(1,0),(0,1),(1,3),(3,3),(4,4),(3,6),(1,6),(0,5)]],
    "T":[[(0,0),(4,0)],[(2,0),(2,6)]],
    "W":[[(0,0),(1,6),(2,2),(3,6),(4,0)]],
    "Y":[[(0,0),(2,3),(2,6)],[(4,0),(2.75,1.95)]] }

def star(x,y,r=6.5,col="#1B2A4A"):
    p=[]
    for k in range(10):
        a=math.radians(-90+k*36); rr=r if k%2==0 else r*.45
        p.append(f"{x+math.cos(a)*rr:.1f} {y+math.sin(a)*rr:.1f}")
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'

def layout(rows,u,x0,y0,rowgap,col):
    """rows: list of words-per-row strings. Returns (dots_svg, solved_svg, n)."""
    dots=[]; solved=[]; n=0
    y=y0
    for row in rows:
        # width: letters*4u + gaps 2u between letters, 3.5u between words
        wd=0
        for wi,word in enumerate(row.split(" ")):
            wd+=len(word)*4*u+(len(word)-1)*2.7*u
            if wi: wd+=4.4*u
        x=x0+(W-2*x0-wd)/2
        for word in row.split(" "):
            for ch in word:
                for si,stroke in enumerate(L[ch]):
                    pts=[(x+px*u,y+py*u) for px,py in stroke]
                    for pi,(sx,sy) in enumerate(pts):
                        n+=1
                        first = pi==0
                        if first: dots.append(star(sx,sy,6.5,col))
                        else: dots.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3.4" fill="{col}"/>')
                        lx,ly=sx+6,sy-7
                        dots.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10.5" fill="{col}" '
                                    f'font-family="Bricolage Grotesque" font-weight="700">{n}</text>')
                    d="M "+" L ".join(f"{px:.1f} {py:.1f}" for px,py in pts)
                    solved.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3" '
                                  f'stroke-linejoin="round" stroke-linecap="round" opacity=".85"/>')
                x+=4*u+2.7*u
            x+=1.7*u
        y+=6*u+rowgap
    return "".join(dots),"".join(solved),n

NAVY="#1B2A4A"; CREAM="#FAF7EE"

SHELL=f"""<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};color:{NAVY}}}
.hd{{position:absolute;left:44px;right:44px;top:36px;display:flex;justify-content:space-between;
 font-size:9.5px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;opacity:.6;
 border-bottom:2px solid {NAVY};padding-bottom:8px}}
h1{{position:absolute;left:44px;top:64px;margin:0;font-size:42px;font-weight:800;
 letter-spacing:-.03em;line-height:.94;text-transform:uppercase}}
.vs{{position:absolute;left:44px;right:44px;font-family:"Newsreader",Georgia,serif;
 font-size:15.5px;line-height:1.5}}
.vs b{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;opacity:.6;display:block;margin-top:5px}}
.how{{position:absolute;left:44px;right:44px;font-size:12px;font-weight:600;line-height:1.5}}
svg.art{{position:absolute;pointer-events:none}}
.ans{{position:absolute;left:44px;right:44px;bottom:22px;text-align:center;font-size:10px;
 font-weight:700;letter-spacing:.08em;transform:rotate(180deg);opacity:.55}}
.fol{{position:absolute;right:44px;bottom:22px;font-size:9px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.4}}
</style>"""

# ═══ PAGE 46 · JOHN 21:6 · THE SEA ═══════════════════════════════════════════
dots46,sol46,n46=layout(["THE","RIGHT","SIDE"],24,90,560,66,NAVY)
def sea_art():
    waves="".join(f'<path d="M {x} 470 q 14 -13 28 0" fill="none" stroke="{NAVY}" stroke-width="2.4"/>'
                  for x in range(0,941,28))
    return f'''<g fill="none" stroke="{NAVY}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="856" cy="90" r="26"/>
    {"".join(f'<line x1="{856+math.cos(math.radians(a))*36:.0f}" y1="{90+math.sin(math.radians(a))*36:.0f}" x2="{856+math.cos(math.radians(a))*48:.0f}" y2="{90+math.sin(math.radians(a))*48:.0f}"/>' for a in range(0,360,45))}
    <path d="M 60 200 q 14 -10 28 2 M 104 186 q 12 -9 24 2"/>
    <path d="M 30 470 L 30 380 Q 30 366 44 362 L 118 362 Q 132 366 132 380 L 132 470"/>
    <path d="M 56 362 L 62 300 L 100 300 L 106 362 M 66 300 L 70 262 L 92 262 L 96 300
             M 70 262 L 92 262 M 74 262 L 74 240 L 88 240 L 88 262"/>
    <path d="M 66 320 L 96 320 M 62 340 L 100 340"/>
    <path d="M 430 470 Q 470 512 560 512 Q 660 512 690 470 Z"/>
    <path d="M 560 512 L 560 470 M 470 496 L 676 496" stroke-dasharray="7 6" stroke-width="1.8"/>
    <path d="M 588 470 L 588 386 M 588 386 L 640 386 L 640 410 L 588 410 M 588 424 L 660 424 L 660 470"/>
    <path d="M 470 452 Q 466 436 476 428 Q 488 422 496 430 Q 502 438 496 448 L 492 470
             M 496 430 L 520 402 L 560 388"/>
    <circle cx="482" cy="416" r="11"/>
    <path d="M 560 388 L 560 560" stroke-width="1.8"/>
    <path d="M 552 560 q 8 12 16 0" stroke-width="1.8"/>
    {waves}
    <path d="M 40 1240 q 6 -60 -6 -110 M 40 1240 q -14 -50 -4 -96 M 40 1240 q 22 -44 14 -92"/>
    <path d="M 880 1246 q -8 -54 8 -100 M 880 1246 q 16 -44 4 -88 M 880 1246 q -20 -40 -12 -84"/>
    <path d="M 0 1258 Q 240 1236 470 1252 T 941 1250" stroke-width="2.2"/>
    <path d="M 200 1252 q 4 -34 -6 -60 M 200 1252 q 14 -30 8 -58 M 700 1252 q -6 -36 6 -64 M 700 1252 q -18 -30 -10 -60"/>
    </g>'''
P46=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 46 · What's Under the Water</title>
<link rel="stylesheet" href="fonts.css">{SHELL}</head><body><main class="page">
<div class="hd"><span>Games · connect the dots</span><span>Issue 001 · Page 46</span></div>
<h1>What&rsquo;s under<br/>the water?</h1>
<p class="vs" style="top:196px;left:190px;max-width:52ch">He said to them, &ldquo;Cast the net on the right side
of the boat, and you will find some.&rdquo; They cast it therefore, and now they weren&rsquo;t able to
draw it in for the multitude of fish.<b>John 21 : 6 &#183; they had fished all night and caught nothing</b></p>
<p class="how" style="top:322px;left:190px;max-width:48ch">They moved the net one boat-width. Connect the dots
1 to {n46} to find out what was waiting under the water the whole time.
A <b>&#9733;</b> means lift your pencil and start a new line.</p>
<svg class="art" style="inset:0;width:100%;height:100%" viewBox="0 0 {W} {H}">{sea_art()}{dots46}</svg>
<div class="ans">answer: the thing he said &#183; three words &#183; John 21:6</div>
</main></body></html>"""
open(f"{LAB}/between-sundays-page-46.html","w").write(P46)

# solved proof
open(f"{LAB}/_p46_solved.html","w").write(P46.replace(dots46, dots46+sol46))
print(f"p46 sea · {n46} dots")

# ═══ PAGE 45B · AMOS 9:13 · DOMINOES ═════════════════════════════════════════
dots45,sol45,n45=layout(["BLESSINGS","ARE ON","THE WAY"],14.2,60,600,58,NAVY)
def dominoes():
    out=[]
    x=120
    for i,ang in enumerate([64,38,18,8,4,2,0]):
        w_,h_=64,150
        cx,cy=x,318
        out.append(f'''<g transform="translate({cx} {cy}) rotate({ang})">
         <rect x="{-w_/2}" y="{-h_}" width="{w_}" height="{h_}" rx="9" fill="none"
          stroke="{NAVY}" stroke-width="3"/>
         <line x1="{-w_/2+9}" y1="{-h_/2}" x2="{w_/2-9}" y2="{-h_/2}" stroke="{NAVY}" stroke-width="2.2"/>
         <circle cx="0" cy="{-h_*0.75}" r="5.5" fill="{NAVY}"/>
         <circle cx="-11" cy="{-h_*0.25}" r="5.5" fill="{NAVY}"/>
         <circle cx="11" cy="{-h_*0.32}" r="5.5" fill="{NAVY}"/>
         <circle cx="0" cy="{-h_*0.18}" r="5.5" fill="{NAVY}"/></g>''')
        x+=104
    out.append(f'<path d="M 96 330 q 26 10 52 2 M 92 344 q 30 12 60 2" fill="none" stroke="{NAVY}" stroke-width="2"/>')
    out.append(f'<line x1="60" y1="332" x2="880" y2="332" stroke="{NAVY}" stroke-width="2.6"/>')
    return "".join(out)
P45=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 45 · One Thing Starts Another</title>
<link rel="stylesheet" href="fonts.css">{SHELL}</head><body><main class="page">
<div class="hd"><span>Games · connect the dots</span><span>Issue 001 · Page 45</span></div>
<h1>One thing starts<br/>another.</h1>
<svg class="art" style="inset:0;width:100%;height:100%" viewBox="0 0 {W} {H}">{dominoes()}{dots45}</svg>
<p class="vs" style="top:376px;max-width:60ch">&ldquo;Behold, the days come,&rdquo; says Yahweh,
&ldquo;that the plowman shall overtake the reaper, and the one treading grapes him who sows seed;
and sweet wine will drip from the mountains, and flow from the hills.&rdquo;
<b>Amos 9 : 13 &#183; the harvest comes faster than you can plant</b></p>
<p class="how" style="top:496px;max-width:56ch">Connect the dots 1 to {n45}.
A <b>&#9733;</b> means lift your pencil and start a new line.</p>
<div class="how" style="position:absolute;left:44px;right:44px;top:1206px;font-size:13px">
The last word is yours to finish:&nbsp;&nbsp;<b style="letter-spacing:.2em">TO&nbsp;&nbsp;M&nbsp;___</b>
&nbsp;&mdash; write it in.</div>
<div class="ans">answer: four words, then yours &#183; Amos 9:13</div>
</main></body></html>"""
os.makedirs(LABB,exist_ok=True)
open(f"{LABB}/between-sundays-page-45.html","w").write(P45)
open(f"{LABB}/_p45_solved.html","w").write(P45.replace(dots45, dots45+sol45))
print(f"p45 dominoes · {n45} dots")
