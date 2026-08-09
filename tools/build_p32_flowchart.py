#!/usr/bin/env python3
"""
Page 32 — "Find the Certain Place"
A hand-drawn decision tree that is rigged: every branch converges on the same box.
Replaces the maze.
"""
import os, math, random, html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "lab")
os.makedirs(OUT, exist_ok=True)
FONT = open(os.path.join(BASE, "fonts", "shantell.css")).read()
random.seed(32)
esc = html.escape

W, H = 941, 1346

# ---------------------------------------------------------------- arrow maker
def arrow(x1, y1, x2, y2, bend=0.0, head=13, w=3.0, dash=None):
    """Hand-drawn arrow from (x1,y1) to (x2,y2) with an optional sideways bend."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    # perpendicular offset for the bend
    px, py = -dy / L, dx / L
    cx, cy = mx + px * bend, my + py * bend
    # pull the tip back so the head sits on the target
    ux, uy = dx / L, dy / L
    tx, ty = x2 - ux * head * 0.75, y2 - uy * head * 0.75
    d = f"M {x1:.0f} {y1:.0f} Q {cx:.0f} {cy:.0f} {tx:.0f} {ty:.0f}"
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    # arrowhead: two strokes, drawn like a hand would
    ang = math.atan2(y2 - cy, x2 - cx)
    a1 = ang + math.radians(158)
    a2 = ang - math.radians(158)
    h1 = f"M {x2:.0f} {y2:.0f} L {x2+math.cos(a1)*head:.0f} {y2+math.sin(a1)*head:.0f}"
    h2 = f"M {x2:.0f} {y2:.0f} L {x2+math.cos(a2)*head:.0f} {y2+math.sin(a2)*head:.0f}"
    return (f'<path d="{d}" fill="none" stroke="#14110c" stroke-width="{w}" '
            f'stroke-linecap="round"{ds}/>'
            f'<path d="{h1}" fill="none" stroke="#14110c" stroke-width="{w}" stroke-linecap="round"/>'
            f'<path d="{h2}" fill="none" stroke="#14110c" stroke-width="{w}" stroke-linecap="round"/>')

def ring(cx, cy, rx, ry, w=3.0):
    """A hand-scrawled ellipse around something."""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" '
            f'stroke="#D62F1F" stroke-width="{w}" stroke-linecap="round"/>')

# ---------------------------------------------------------------- the chart
# node: (id, x, y, lines, size, kind)
N = {
 "q1":  (470, 214, ["DID YOU CHOOSE", "TO BE HERE?"],            40, "q"),
 "no1": (218, 330, ["NO"],                                        34, "a"),
 "ys1": (700, 330, ["YES"],                                       34, "a"),
 "s1":  (196, 424, ["neither did", "Jacob →"],                    27, "s"),
 "q2":  (706, 430, ["IS IT GOING", "TO PLAN?"],                   34, "q"),
 "no2": (630, 536, ["NO"],                                        28, "a"),
 "ys2": (798, 536, ["YES"],                                       28, "a"),
 "q3":  (250, 588, ["DOES IT", "FEEL HOLY?"],                     36, "q"),
 "no3": (168, 700, ["NOT", "REMOTELY"],                           26, "a"),
 "ys3": (334, 700, ["YES"],                                       26, "a"),
 "q4":  (700, 640, ["IS ANYONE", "WATCHING?"],                    32, "q"),
 "no4": (630, 742, ["NO"],                                        26, "a"),
 "ys4": (786, 742, ["YES"],                                       26, "a"),
 "s2":  (176, 806, ["correct.", "it didn't feel", "holy to him", "either."],  25, "s"),
 "s3":  (706, 826, ["still", "counts"],                           28, "s"),
 "esc": (470, 880, ["CAN I SKIP", "TO THE ANSWER?"],              30, "q"),
 "esa": (470, 952, ["yes, but it's the same answer"],             24, "s"),
 "ans": (470, 1104, [],                                            0, "x"),
}
def nx(k): return N[k][0]
def ny(k): return N[k][1]

nodes = []
for k,(x,y,lines,sz,kind) in N.items():
    if kind == "x": continue
    cls = {"q":"q","a":"a","s":"s"}[kind]
    txt = "<br/>".join(esc(l) for l in lines)
    nodes.append(f'<div class="n {cls}" style="left:{x}px;top:{y}px;font-size:{sz}px">{txt}</div>')

A = []
# top split
A.append(arrow(438, 262, 262, 316, bend=14))
A.append(arrow(516, 262, 676, 316, bend=-14))
# NO -> "neither did Jacob"
A.append(arrow(214, 356, 200, 404, bend=6))
# YES -> is it going to plan
A.append(arrow(704, 356, 706, 406, bend=-5))
# going to plan -> no / yes
A.append(arrow(676, 480, 634, 518, bend=8))
A.append(arrow(742, 480, 792, 518, bend=-8))
# "neither did Jacob" -> does it feel holy
A.append(arrow(216, 486, 240, 560, bend=-10))
# NO (not to plan) -> does it feel holy   (long cross-page arrow)
A.append(arrow(602, 552, 330, 588, bend=34))
# YES (to plan) -> is anyone watching
A.append(arrow(792, 566, 720, 616, bend=10))
# feel holy -> not remotely / yes
A.append(arrow(226, 646, 176, 682, bend=8))
A.append(arrow(288, 646, 330, 682, bend=-8))
# not remotely -> the correcting note
A.append(arrow(168, 730, 172, 782, bend=5))
# watching -> no/yes
A.append(arrow(676, 692, 634, 724, bend=6))
A.append(arrow(730, 692, 782, 724, bend=-6))
# both -> still counts
A.append(arrow(632, 768, 686, 802, bend=-8))
A.append(arrow(788, 768, 726, 802, bend=8))
# everything funnels to the answer
A.append(arrow(176, 884, 300, 986, bend=-40))          # from the "correct" note
A.append(arrow(336, 726, 420, 982, bend=-62))          # from YES it feels holy
A.append(arrow(706, 872, 600, 986, bend=40))           # from still counts
A.append(arrow(470, 976, 470, 990, bend=0))           # from the escape hatch
A.append(arrow(462, 918, 468, 932, bend=0))             # skip -> yes but
# the loop back to the top, up the left margin
A.append(arrow(104, 1120, 300, 200, bend=140, dash="14 11", w=2.6))
ARROWS = "".join(A)

# the answer slab
ANSWER = f'''
<div class="ans">
  <div class="ansin">
    <div class="ansq">SURELY THE LORD IS IN THIS PLACE.</div>
    <div class="anss">and I didn't know it.</div>
    <div class="ansr">Genesis 28:16</div>
  </div>
  <div class="ansyou">YOU ARE ALREADY IN IT.</div>
</div>'''

DOC = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays — Page 32 · Find the Certain Place</title>
<style>
{FONT}
*{{box-sizing:border-box}}
@page{{size:13.07in 18.69in;margin:0}}
html,body{{margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Shantell Sans",'Comic Sans MS',cursive}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#FBF8F0;color:#14110c;
 box-shadow:0 30px 58px rgba(17,16,13,.26)}}
.paper{{position:absolute;inset:0;
 background-image:radial-gradient(rgba(20,17,12,.10) .6px,transparent .9px);background-size:7px 7px;
 opacity:.55}}
svg.wires{{position:absolute;inset:0;width:100%;height:100%;z-index:1}}
.layer{{position:absolute;inset:0;z-index:2}}

.folio{{position:absolute;top:34px;left:46px;right:46px;display:flex;justify-content:space-between;
 font-family:"Avenir Next",sans-serif;font-size:10.5px;font-weight:900;letter-spacing:.2em;
 text-transform:uppercase;color:#6B6455;border-bottom:2px solid #14110c;padding-bottom:9px}}
.folio span:last-child{{text-align:right}}

.title{{position:absolute;top:78px;left:46px;right:46px;text-align:center}}
.title h1{{margin:0;font-size:58px;line-height:.95;font-weight:700;letter-spacing:-.01em}}
.title p{{margin:8px 0 0;font-size:21px;color:#6B6455}}

/* nodes */
.n{{position:absolute;transform:translate(-50%,-50%);text-align:center;line-height:1.08;
 white-space:nowrap}}
.n.q{{font-weight:700;letter-spacing:-.01em}}
.n.a{{font-weight:700}}
.n.s{{font-weight:600;color:#3C362A;line-height:1.15}}

/* the answer */
.ans{{position:absolute;left:50%;top:1036px;transform:translateX(-50%);text-align:center;width:760px}}
.ansin{{border:4px solid #14110c;border-radius:6px;padding:20px 26px 16px;background:#FFF7D6;
 transform:rotate(-.5deg)}}
.ansq{{font-size:34px;font-weight:700;line-height:1.05}}
.anss{{font-size:23px;color:#3C362A;margin-top:4px}}
.ansr{{font-family:"Avenir Next",sans-serif;font-size:10px;font-weight:900;letter-spacing:.22em;
 text-transform:uppercase;color:#6B6455;margin-top:9px}}
.ansyou{{margin-top:11px;font-size:26px;font-weight:700;color:#D62F1F;transform:rotate(.6deg)}}

.loopnote{{flex:0 0 auto;width:216px;font-size:18px;color:#14110c;line-height:1.2;
 transform:rotate(-1.2deg)}}
.foot{{position:absolute;left:46px;right:46px;bottom:34px;border-top:2px solid #14110c;padding-top:12px;
 display:flex;justify-content:space-between;gap:26px;align-items:flex-start}}
.foot .rule{{font-size:16px;max-width:470px;line-height:1.3;color:#3C362A}}
.foot .pg{{font-family:"Avenir Next",sans-serif;font-size:10px;font-weight:900;letter-spacing:.2em;
 text-transform:uppercase;color:#6B6455;white-space:nowrap}}
</style></head>
<body><main class="page">
<div class="paper"></div>
<svg class="wires" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
 {ARROWS}
</svg>
<div class="layer">
 <div class="folio"><span>Games · No pencil required<br/>Issue 001</span>
  <span>Follow it honestly<br/>Genesis 28:16</span></div>
 <div class="title">
  <h1>FIND THE CERTAIN PLACE</h1>
  <p>a flow chart · answer truthfully · there is no wrong route</p>
 </div>
 {"".join(nodes)}
 {ANSWER}
 <div class="foot">
  <div class="loopnote">in case of doubt,<br/>back to the top. <b>same answer.</b></div>
  <div class="rule">Every branch on this page ends in the same box. That is not a printing error —
  it is the entire point of Genesis 28. Jacob answered every question wrong and woke up there anyway.</div>
  <span class="pg">Page 32</span>
 </div>
</div>
</main></body></html>'''

open(os.path.join(OUT, "between-sundays-page-32.html"), "w").write(DOC)
print("wrote public/lab/between-sundays-page-32.html")
print(f"  {len([k for k in N if N[k][4]!='x'])} nodes · {len(A)} hand-drawn arrows · all paths converge")
