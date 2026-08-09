#!/usr/bin/env python3
"""
Page 16 — WORDS & MEANING, one dense sketchbook page (replaces the airy spread).
Sketch-first: every drawing is built with hatching and scribble weight, placed,
then the text is packed around them. One blue ink. No opinions, just lexicon.
"""
import os, random
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
INK="#2438B4"; PAPER="#F8F4E9"
random.seed(16)
def j(a=1.6): return random.uniform(-a,a)

def hatch(x,y,w_,h_,n=6,ang=24):
    o=""
    import math
    for k in range(n):
        t=k/(n-1) if n>1 else .5
        x1=x+t*w_; y1=y
        o+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x1-h_*0.45:.0f}" y2="{y1+h_:.0f}" stroke="{INK}" stroke-width="1.4"/>'
    return o

def arrow(x1,y1,x2,y2,bend=10):
    mx,my=(x1+x2)/2+bend,(y1+y2)/2
    return (f'<path d="M {x1} {y1} Q {mx} {my} {x2} {y2}" fill="none" stroke="{INK}" '
            f'stroke-width="2.2" stroke-linecap="round"/>'
            f'<path d="M {x2-8} {y2-6} L {x2} {y2} L {x2-9} {y2+5}" fill="none" stroke="{INK}" '
            f'stroke-width="2.2" stroke-linecap="round"/>')
def uline(x1,x2,y,sw=3):
    return (f'<path d="M {x1+j()} {y+j()} Q {(x1+x2)/2} {y+j(3)+2} {x2+j()} {y+j()}" '
            f'fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>')
def spark(x,y,r=9):
    import math
    o=""
    for k in range(4):
        a=math.radians(k*45+20)
        o+=(f'<line x1="{x-math.cos(a)*r:.0f}" y1="{y-math.sin(a)*r:.0f}" '
            f'x2="{x+math.cos(a)*r:.0f}" y2="{y+math.sin(a)*r:.0f}" stroke="{INK}" '
            f'stroke-width="2" stroke-linecap="round"/>')
    return o

def banner(x,y,w_,txt,rot=-2.4):
    return f'''<g transform="rotate({rot} {x} {y})">
 <path d="M {x} {y} L {x+w_} {y} L {x+w_} {y+30} L {x} {y+30} Z" fill="none" stroke="{INK}" stroke-width="2.4"/>
 <path d="M {x} {y+4} L {x-16} {y+15} L {x} {y+26} M {x+w_} {y+4} L {x+w_+16} {y+15} L {x+w_} {y+26}"
  fill="none" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>
 {hatch(x+2,y+24,w_-4,5,10)}
 <text x="{x+w_/2}" y="{y+21}" text-anchor="middle" font-size="15" fill="{INK}"
  font-family="Shantell Sans" font-weight="700" letter-spacing="2">{txt}</text></g>'''

# ── the sketches (drawn first) ───────────────────────────────────────────────
def almond(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.6" stroke-linecap="round">
 <path d="M 8 108 Q 26 66 52 34 Q 64 20 82 10"/>
 <path d="M 34 66 q -22 -8 -26 -30 q 22 2 30 22 z"/><path d="M 20 46 l 16 14" stroke-width="1.6"/>
 <path d="M 56 34 q -6 -24 12 -38 q 12 18 0 36 z"/><path d="M 60 10 l 2 22" stroke-width="1.6"/>
 <path d="M 64 48 q 24 -10 42 4 q -18 14 -40 6 z"/>
 <path d="M 70 50 l 30 0 M 72 55 l 24 0" stroke-width="1.4"/>
 <path d="M 6 116 q 20 6 40 0" stroke-width="1.8"/></g>'''
def stairs(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.8" stroke-linejoin="round">
 <path d="M 6 118 L 34 118 L 34 96 L 62 96 L 62 74 L 90 74 L 90 52 L 118 52 L 118 30"/>
 <path d="M 6 118 L 6 128 L 126 128" stroke-width="2"/>
 {hatch(36,100,24,16,4)}{hatch(64,78,24,16,4)}{hatch(92,56,24,16,4)}
 <path d="M 96 22 q 10 -12 24 -6 q 12 -12 24 0 q 12 -4 12 8" stroke-width="2"/>
 <text x="128" y="46" font-size="20" fill="{INK}" font-family="Shantell Sans" font-weight="700">?</text>
 <path d="M 22 96 L 22 60 M 12 78 L 32 78 M 12 66 L 32 66" stroke-width="2"/>
 <text x="-14" y="44" font-size="13" fill="{INK}" font-family="Shantell Sans">a ladder?</text></g>'''
def pin(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.8" stroke-linecap="round">
 <circle cx="46" cy="34" r="22"/><circle cx="46" cy="34" r="7" fill="{INK}"/>
 <path d="M 46 56 Q 44 78 46 96"/>
 <path d="M 20 98 L 74 98" stroke-width="2.4"/>
 <path d="M 26 104 l 8 8 m 0 -8 l -8 8 M 60 104 l 8 8 m 0 -8 l -8 8" stroke-width="2"/>
 <circle cx="46" cy="34" r="30" stroke-dasharray="5 7" stroke-width="1.6"/>
 {spark(80,12)}</g>'''
def envelope(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.6" stroke-linejoin="round">
 <path d="M 8 26 L 96 20 L 100 78 L 12 84 Z"/>
 <path d="M 8 26 L 54 56 L 96 20"/>
 <rect x="78" y="28" width="14" height="16" stroke-width="1.8" transform="rotate(4 85 36)"/>
 {hatch(79,30,12,12,4)}
 <path d="M -12 40 q 8 -4 14 2 M -14 52 q 10 -4 16 2 M -10 64 q 8 -4 12 2" stroke-width="1.8"/></g>'''
def eye(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.8" stroke-linecap="round">
 <path d="M 6 46 Q 52 8 98 46 Q 52 84 6 46 Z"/>
 <circle cx="52" cy="45" r="16"/><circle cx="52" cy="45" r="6" fill="{INK}"/>
 <path d="M 52 45 m -16 0 a 16 16 0 0 1 10 -14" stroke-width="1.4"/>
 <path d="M 30 20 L 24 10 M 52 14 L 52 2 M 74 20 L 80 10 M 16 30 L 8 22 M 88 30 L 96 22"/>
 {hatch(24,58,56,14,8)}</g>'''
def stone(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.8" stroke-linejoin="round">
 <path d="M 34 104 L 30 26 Q 30 12 44 10 Q 60 10 60 26 L 58 104 Z"/>
 {hatch(34,32,10,64,5)}
 <path d="M 14 104 L 80 104 M 20 112 L 74 112" stroke-width="2.2"/>
 <path d="M 44 -8 q 3 6 0 10 M 52 -4 q 3 5 0 9 M 38 -2 q 2 4 0 8" stroke-width="2"/>
 <text x="66" y="-10" font-size="13" fill="{INK}" font-family="Shantell Sans">oil &#183; v.18</text></g>'''
def house(x,y,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}"
 stroke-width="2.8" stroke-linejoin="round">
 <path d="M 14 96 L 16 46 L 52 18 L 88 44 L 88 96 Z"/>
 <path d="M 4 52 L 52 12 L 100 48"/>
 {hatch(20,24,60,20,9)}
 <path d="M 42 96 L 42 66 L 62 66 L 62 96" stroke-width="2.4"/>
 <circle cx="58" cy="80" r="1.8" fill="{INK}"/></g>'''

# ── text blocks ──────────────────────────────────────────────────────────────
def blk(x,y,w_,word,heb,tag,defn,facts,langs,tilt=0):
    fx="".join(f'<div class="fx">{f}</div>' for f in facts)
    lg="".join(f'<div class="lg">{l}</div>' for l in langs)
    return f'''<div class="cell" style="left:{x}px;top:{y}px;width:{w_}px;transform:rotate({tilt}deg)">
  <span class="wd">{word}</span><span class="hb">{heb}</span>
  <div class="tag">{tag}</div><div class="df">{defn}</div>{fx}{lg}</div>'''

def headline():
    out=[]
    for line,size,top in (("WORDS &",92,0),("MEANING",92,96)):
        row=""
        for ch in line:
            if ch==" ": row+='<span style="display:inline-block;width:26px"></span>'; continue
            r=random.uniform(-4,4); ty=random.uniform(-3,3)
            row+=(f'<span style="display:inline-block;transform:rotate({r:.1f}deg) '
                  f'translateY({ty:.1f}px)">{ch}</span>')
        out.append(f'<div style="position:absolute;top:{top}px;left:0;font-size:{size}px;'
                   f'font-weight:800;letter-spacing:2px;line-height:1">{row}</div>')
    return "".join(out)

SK=(almond(742,352,0.85)+stairs(346,596,0.95)+pin(796,700,0.85)+envelope(80,762,0.95)
   +eye(462,668,0.9)+stone(646,1092,0.9)+house(336,1010,0.95))
DOODLE=(uline(44,368,214,3.4)+uline(44,300,238,2.4)
 +banner(56,452,220,"GENESIS 28 : 10–22")
 +arrow(546,128,598,142,-8)+arrow(568,486,604,510,10)+arrow(580,806,606,842,8)
 +arrow(262,760,300,782,-8)
 +uline(612,700,96,2.6)+spark(918,84,10)+spark(590,232,8)+spark(56,1230,9)+spark(902,1230,9)
 +f'<text x="930" y="640" font-size="12.5" fill="{INK}" font-family="Shantell Sans" '
  f'transform="rotate(90 930 640)" letter-spacing="1">no opinions on this page — just the dictionary</text>'
 +uline(44,896,1252,2.2))

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 16 · Words &amp; Meaning</title><link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Shantell Sans","Bricolage Grotesque",cursive}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
svg.lay{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
.hdl{{position:absolute;left:44px;top:34px;width:560px;height:200px}}
.intro{{position:absolute;left:44px;top:252px;width:252px;font-size:13.5px;line-height:1.42;
 font-weight:600}}
.date{{position:absolute;right:40px;top:38px;font-size:13px;transform:rotate(2deg)}}
.cell{{position:absolute}}
.wd{{font-size:34px;font-weight:800;text-transform:uppercase;letter-spacing:1px;line-height:1}}
.hb{{font-size:23px;margin-left:9px;font-family:"Arial Hebrew","SBL Hebrew",serif}}
.tag{{font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;opacity:.75;margin-top:2px}}
.df{{margin-top:5px;font-size:13.5px;line-height:1.35;font-weight:700}}
.fx{{margin-top:5px;font-size:12px;line-height:1.32;padding-left:13px;position:relative;font-weight:600}}
.fx:before{{content:"→";position:absolute;left:-1px}}
.lg{{margin-top:3px;font-size:10.5px;line-height:1.35;opacity:.85}}
.src{{position:absolute;left:44px;right:44px;bottom:26px;font-size:10px;line-height:1.45;opacity:.85}}
.pg{{position:absolute;left:44px;bottom:60px;font-size:12px;opacity:.6}}
</style></head><body><main class="page">
<div class="hdl">{headline()}</div>
<div class="date">issue 001 · wednesday</div>
<div class="intro">Seven words from Genesis 28, looked up — not explained. What each one meant,
where it came from, and what the translators did with it.</div>
{blk(612,110,300,"Luz","לוּז","proper noun · Strong's H3870",
 "The town's name before Jacob renamed it. It means almond tree.",
 ["The place already had a name, and the name already had a meaning.",
  "He renames it in the morning (v.19)."],
 ["English: Luz · almond — same root as the almond wood of Gen 30:37"])}
{blk(330,238,236,"Sullam","סֻלָּם","noun · Strong's H5551",
 "Translated ladder. It appears exactly once in the whole Hebrew Bible — here.",
 ["Root salal: to heap up, to raise a mound.",
  "Ladder, stairway or ramp — translators never fully agreed."],
 ["Greek: κλῖμαξ · Latin: scala · KJV ladder · NIV stairway"],-0.5)}
{blk(612,500,296,"Maqom","מָקוֹם","noun · Strong's H4725",
 "Place. A standing-place. Used six times in this one short story.",
 ["From qum: to stand, to rise.",
  "Centuries later HaMaqom — “The Place” — became one of the Jewish names for God."],
 ["Greek: τόπος · Latin: locus · v.16: “God is in this maqom.”"],0.4)}
{blk(44,530,252,"Mal'akh","מַלְאָךְ","noun · Strong's H4397",
 "The word translated angel. Its plain meaning: messenger.",
 ["Four chapters on, Jacob sends mal'akhim — human ones — to his brother. Same word (Gen 32:3).",
  "The word alone never says heavenly or hired."],
 ["Greek: ἄγγελος angelos — also just “messenger”"],-0.4)}
{blk(330,806,240,"Yare","יָרֵא","verb · Strong's H3372",
 "To fear. Also the root of the word translated awesome.",
 ["v.17: “He was afraid (yare), and said: How awesome (nora) is this place.”",
  "Afraid and awesome — one root, same verse."],
 ["KJV: “How dreadful is this place”"],0.5)}
{blk(612,836,296,"Matsevah","מַצֵּבָה","noun · Strong's H4676",
 "A standing stone. The pillow, stood up on its end and marked.",
 ["From natsab: to stand, to be set upright.",
  "He pours oil on it (v.18). Deuteronomy 16:22 later bans the matsevah. Same word, no comment."],
 ["Greek: στήλη stele · English: pillar, standing stone"],-0.3)}
{blk(44,886,252,"Beth-El","בֵּית־אֵל","place name · Strong's H1008",
 "Beth: house. El: God. The whole name is those two words.",
 ["Same beth as Beth-lehem — house of bread.",
  "v.17 is the Bible's first “house of God.” It is a patch of open ground."],
 ["Greek: Βαιθήλ · v.19: “but the name of the city was Luz at first.”"],0.4)}
<svg class="lay" viewBox="0 0 {W} {H}">{DOODLE}{SK}</svg>
<div class="pg">16</div>
<div class="src">Definitions &amp; roots: Strong's Concordance and Brown–Driver–Briggs lexicon
(public domain). Verses: Genesis 28, World English Bible. Where scholars disagree, this page says
so and stops.</div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-16.html","w").write(DOC)
print("p16 dense sketch page · 7 words · 7 drawings")
