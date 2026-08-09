#!/usr/bin/env python3
"""
Page 41 — BETHEL SUPPLY CO. v2.
Surplus-catalog kelly green (not Draplin's orange). Objects drawn with real
halftone shading + cream cut-line highlights. Copy closes its own loop:
nothing is for sale because it was already handed over — receipt on 07-08.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
W,H=941,1346
GREEN="#1F7F46"; INKK="#12100C"; PAPER="#F5F0E2"

def defs(p):
    """dot-screen patterns unique per artwork: coarse form-shadow + fine sheen"""
    return f'''<defs>
 <pattern id="{p}c" width="7" height="7" patternUnits="userSpaceOnUse">
   <rect width="7" height="7" fill="{INKK}"/><circle cx="3.5" cy="3.5" r="2" fill="{GREEN}"/></pattern>
 <pattern id="{p}f" width="5" height="5" patternUnits="userSpaceOnUse">
   <rect width="5" height="5" fill="{INKK}"/><circle cx="2.5" cy="2.5" r="0.9" fill="{PAPER}"/></pattern>
</defs>'''

def stone(p="st"):
    return f'''{defs(p)}
 <ellipse cx="62" cy="96" rx="46" ry="7" fill="{INKK}" opacity=".85"/>
 <path d="M 18 82 Q 8 52 34 36 Q 58 20 88 32 Q 112 42 106 68 Q 100 90 70 92 Q 38 94 18 82 Z" fill="{INKK}"/>
 <path d="M 34 38 Q 56 24 84 34 Q 74 46 52 48 Q 40 46 34 38 Z" fill="url(#{p}f)"/>
 <path d="M 20 74 Q 30 86 58 90 Q 40 92 24 84 Z" fill="url(#{p}c)"/>
 <path d="M 36 60 L 74 52 M 44 74 L 88 64" stroke="{PAPER}" stroke-width="3.4" fill="none" stroke-linecap="round"/>
 <path d="M 8 96 l 5 -8 M 116 96 l -5 -8 M 112 99 l 7 -5" stroke="{INKK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'''
def staff(p="sf"):
    return f'''{defs(p)}
 <ellipse cx="46" cy="112" rx="26" ry="5" fill="{INKK}" opacity=".85"/>
 <path d="M 26 36 Q 26 6 52 6 Q 80 6 80 34 Q 80 58 60 58 L 59 47 Q 70 46 70 33 Q 70 16 52 16 Q 36 16 36 36 L 45 36 L 40 112 L 30 112 Z" fill="{INKK}"/>
 <path d="M 30 24 Q 34 12 46 9 Q 38 16 37 26 Z" fill="url(#{p}f)"/>
 <path d="M 34 70 L 42 70 M 33 84 L 41 84 M 32 98 L 40 98" stroke="{PAPER}" stroke-width="2.6"/>
 <path d="M 41 56 L 44 56 L 43 64 L 40 64 Z" fill="{PAPER}"/>
 <path d="M 62 50 Q 74 48 76 38" stroke="{GREEN}" stroke-width="3" fill="none"/>'''
def oil(p="oi"):
    return f'''{defs(p)}
 <ellipse cx="52" cy="102" rx="34" ry="6" fill="{INKK}" opacity=".85"/>
 <path d="M 40 12 L 64 12 L 66 22 L 58 22 L 58 32 Q 88 40 88 68 Q 88 98 52 98 Q 16 98 16 68 Q 16 40 46 32 L 46 22 L 38 22 Z" fill="{INKK}"/>
 <path d="M 20 58 Q 24 42 44 36 Q 30 48 28 66 Z" fill="url(#{p}f)"/>
 <path d="M 78 82 Q 86 72 86 62 Q 90 80 72 92 Z" fill="url(#{p}c)"/>
 <path d="M 34 50 Q 40 42 50 44" stroke="{PAPER}" stroke-width="3.6" fill="none" stroke-linecap="round"/>
 <rect x="42" y="4" width="20" height="7" rx="2" fill="{INKK}"/>
 <path d="M 96 30 q 4 8 0 12 q -4 -4 0 -12 M 104 44 q 4 8 0 12 q -4 -4 0 -12" fill="{INKK}"/>'''
def stairs(p="sr"):
    zig="M 6 100 L 6 84 L 30 84 L 30 64 L 54 64 L 54 44 L 78 44 L 78 24 L 102 24 L 102 8 L 130 8 L 130 100 Z"
    return f'''{defs(p)}
 <ellipse cx="70" cy="104" rx="60" ry="5" fill="{INKK}" opacity=".85"/>
 <path d="{zig}" fill="{INKK}"/>
 <path d="M 30 84 L 30 64 L 38 64 L 38 84 Z M 54 64 L 54 44 L 62 44 L 62 64 Z M 78 44 L 78 24 L 86 24 L 86 44 Z M 102 24 L 102 8 L 110 8 L 110 24 Z" fill="url(#{p}c)"/>
 <path d="M 6 84 L 30 84 M 30 64 L 54 64 M 54 44 L 78 44 M 78 24 L 102 24" stroke="{PAPER}" stroke-width="2.6"/>
'''
def coat(p="ct"):
    return f'''{defs(p)}
 <path d="M 55 6 L 55 12" stroke="{INKK}" stroke-width="4"/><circle cx="55" cy="5" r="4" fill="none" stroke="{INKK}" stroke-width="3"/>
 <path d="M 30 22 L 47 12 Q 55 20 63 12 L 80 22 L 94 48 L 79 56 L 75 44 L 75 96 L 35 96 L 35 44 L 31 56 L 16 48 Z" fill="{INKK}"/>
 <path d="M 47 12 Q 55 20 63 12 L 58 26 L 52 26 Z" fill="url(#{p}f)"/>
 <path d="M 35 60 Q 42 66 35 74 M 75 58 Q 68 64 75 72" stroke="{PAPER}" stroke-width="2.4" fill="none"/>
 <path d="M 55 26 L 55 92" stroke="{PAPER}" stroke-width="2.8" stroke-dasharray="1 6"/>
 <rect x="60" y="70" width="12" height="12" fill="url(#{p}c)"/>
 <path d="M 60 70 h 12 v 12 h -12 Z M 60 76 h 12 M 66 70 v 12" stroke="{PAPER}" stroke-width="1.4" fill="none"/>'''
def spine(p="sp"):
    return f'''{defs(p)}
 <ellipse cx="60" cy="98" rx="48" ry="5" fill="{INKK}" opacity=".85"/>
 <path d="M 14 20 L 56 12 L 56 88 L 14 96 Z" fill="{INKK}"/>
 <path d="M 64 12 L 106 20 L 106 96 L 64 88 Z" fill="{INKK}"/>
 <path d="M 14 20 L 24 18 L 24 94 L 14 96 Z" fill="url(#{p}c)"/>
 <path d="M 30 32 L 50 28 M 30 42 L 50 38 M 30 52 L 50 48 M 30 62 L 46 59 M 72 30 L 96 34 M 72 40 L 96 44 M 72 50 L 92 54" stroke="{PAPER}" stroke-width="2.6" fill="none"/>
 <path d="M 60 10 L 60 90" stroke="{PAPER}" stroke-width="2" stroke-dasharray="4 5"/>
 <path d="M 54 2 l 5 6 l 5 -6 M 56 8 a 3 3 0 1 1 -2 1 M 62 8 a 3 3 0 1 0 2 1" stroke="{INKK}" stroke-width="2" fill="none"/>'''
def compass(p="cp"):
    ticks="".join(f'<path d="M 55 50 l {int(38*x)} {int(38*y)}" stroke="{PAPER}" stroke-width="1.6" opacity=".9"/>' for x,y in [])
    return f'''{defs(p)}
 <circle cx="55" cy="50" r="46" fill="{INKK}"/>
 <circle cx="55" cy="50" r="46" fill="none"/>
 <circle cx="55" cy="50" r="37" fill="{GREEN}"/>
 <circle cx="55" cy="50" r="37" fill="none" stroke="{PAPER}" stroke-width="1.6"/>
 <path d="M 55 16 L 62 46 L 55 42 L 48 46 Z" fill="{INKK}"/>
 <path d="M 55 84 L 48 54 L 55 58 L 62 54 Z" fill="url(#{p}c)"/>
 <path d="M 21 50 L 51 44 L 47 50 L 51 56 Z" fill="url(#{p}c)"/>
 <path d="M 89 50 L 59 44 L 63 50 L 59 56 Z" fill="{INKK}"/>
 <circle cx="55" cy="50" r="6" fill="{INKK}"/><circle cx="55" cy="50" r="2.4" fill="{PAPER}"/>
 <text x="55" y="12" text-anchor="middle" font-size="11" font-weight="800" fill="{PAPER}" font-family="Bricolage Grotesque">N</text>
 <text x="55" y="97" text-anchor="middle" font-size="11" font-weight="800" fill="{PAPER}" font-family="Bricolage Grotesque">S</text>
 <text x="8" y="54" font-size="11" font-weight="800" fill="{PAPER}" font-family="Bricolage Grotesque">W</text>
 <text x="95" y="54" font-size="11" font-weight="800" fill="{PAPER}" font-family="Bricolage Grotesque">E</text>'''
def dustbag(p="db"):
    return f'''{defs(p)}
 <ellipse cx="52" cy="100" rx="40" ry="6" fill="{INKK}" opacity=".85"/>
 <path d="M 36 24 L 70 24 Q 94 40 92 68 Q 90 96 53 96 Q 16 96 14 68 Q 12 40 36 24 Z" fill="{INKK}"/>
 <path d="M 24 52 Q 26 38 38 30 Q 28 44 28 60 Z" fill="url(#{p}f)"/>
 <path d="M 78 80 Q 86 68 85 56 Q 90 78 66 92 Z" fill="url(#{p}c)"/>
 <path d="M 32 26 Q 53 20 74 26" stroke="{PAPER}" stroke-width="4" fill="none"/><path d="M 44 22 L 44 12 Q 53 6 62 12 L 62 22" fill="none" stroke="{INKK}" stroke-width="4"/>
 
 <path d="M 38 56 h 9 M 52 48 h 9 M 62 60 h 9 M 44 70 h 9 M 58 74 h 9" stroke="{PAPER}" stroke-width="2.6"/>
 <path d="M 94 96 Q 102 90 110 96 Q 104 100 94 100 Z" fill="{INKK}"/><circle cx="98" cy="88" r="1.8" fill="{INKK}"/><circle cx="106" cy="90" r="1.4" fill="{INKK}"/><circle cx="103" cy="84" r="1.2" fill="{INKK}"/>'''
def sunrise(p="su"):
    import math
    rays=""
    for a in (-72,-48,-24,0,24,48,72):
        r=math.radians(a-90)
        x1,y1=55+38*math.cos(r),50+38*math.sin(r)
        x2,y2=55+52*math.cos(r),50+52*math.sin(r)
        rays+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INKK}" stroke-width="7" stroke-linecap="round"/>'
    return f'''{defs(p)}
 {rays}
 <path d="M 25 50 A 30 30 0 0 1 85 50 Z" fill="{INKK}"/>
 <path d="M 30 46 A 26 26 0 0 1 49 25 Q 36 32 34 50 Z" fill="url(#{p}f)"/>
 <path d="M -2 74 Q 26 58 56 68 Q 60 70 66 68 Q 88 58 112 70 L 112 78 L -2 78 Z" fill="{INKK}"/>
 <path d="M 62 70 Q 86 58 112 70 L 112 64 Q 88 54 64 66 Z" fill="url(#{p}c)"/>
 <path d="M 12 20 q 4 -5 8 0 q 4 -5 8 0" stroke="{INKK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
'''
def cell(style,inner): return f'<div class="cell" style="{style}">{inner}</div>'
def price(label,amt="$0"): return f'<div class="pr"><i>{label}</i><b>{amt}</b></div>'

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 41 · Bethel Supply Co.</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Futura","Avenir Next",sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{GREEN};color:{INKK};
 padding:26px 30px}}
.tiny{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;color:{PAPER}}}
.co{{text-align:center;font-size:15px;font-weight:800;letter-spacing:.3em;text-transform:uppercase;
 margin-top:8px;color:{PAPER}}}
h1{{margin:2px 0 0;text-align:center;font-size:62px;font-weight:800;letter-spacing:.01em;
 line-height:.95;text-transform:uppercase;transform:scaleY(1.08);color:{PAPER}}}
.tag{{text-align:center;margin-top:9px}}
.tag span{{background:{PAPER};padding:3px 12px;font-size:15px;font-weight:700;font-style:italic}}
.sub{{text-align:center;margin-top:7px;font-size:10.5px;font-weight:700;letter-spacing:.12em;
 text-transform:uppercase;color:{PAPER};opacity:.9}}
.grid{{position:absolute;left:30px;right:30px;top:252px;height:938px}}
.cell{{position:absolute;border:3px solid {INKK};padding:10px 12px;overflow:hidden;background:{GREEN}}}
.nm{{display:inline-block;background:{INKK};color:{PAPER};font-size:14.5px;font-weight:800;
 letter-spacing:.05em;text-transform:uppercase;padding:4px 9px}}
.nm.small{{font-size:12px}}
.pr i{{display:block;font-style:italic;font-weight:800;font-size:12px;text-transform:uppercase;color:{PAPER}}}
.pr b{{font-size:42px;font-weight:800;letter-spacing:-.03em;line-height:.9;color:{PAPER}}}
.itm{{font-size:9.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:{PAPER}}}
.quote{{font-size:11.5px;font-weight:700;font-style:italic;color:{PAPER}}}
.quote.knock{{background:{PAPER};color:{INKK};display:inline-block;padding:2px 7px}}
.burst{{font-family:"Shantell Sans",cursive;font-weight:700;font-size:19px;color:{PAPER}}}
.bar{{position:absolute;left:0;right:0;top:308px;text-align:center;font-size:12.5px;font-weight:800;
 letter-spacing:.09em;text-transform:uppercase;border-top:3px solid {INKK};
 border-bottom:3px solid {INKK};padding:7px 0;color:{PAPER}}}
.order{{position:absolute;left:30px;right:30px;bottom:60px;background:{INKK};color:{PAPER};
 padding:13px 18px;display:flex;gap:22px;align-items:center}}
.order .hd{{flex:0 0 148px;font-size:21px;font-weight:800;line-height:1;text-transform:uppercase}}
.order ol{{margin:0;padding:0;list-style:none;display:flex;gap:22px;flex:1}}
.order li{{font-size:11px;line-height:1.4;font-weight:600;flex:1}}
.order li b{{display:block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
 margin-bottom:2px;color:{GREEN};background:{PAPER};display:inline-block;padding:1px 7px}}
.last{{position:absolute;left:30px;right:30px;bottom:26px;text-align:center;font-size:15.5px;
 font-weight:800;font-style:italic;color:{PAPER}}}
.folio{{position:absolute;right:8px;top:50%;transform:rotate(90deg) translateX(-50%);
 transform-origin:right top;font-size:8.5px;font-weight:800;letter-spacing:.18em;
 text-transform:uppercase;color:{PAPER};opacity:.8}}
</style></head><body><main class="page">
<div class="tiny"><span>Every day</span><span>Est. Genesis 28</span></div>
<div class="co">Bethel Supply Co.</div>
<h1>Official<br/>Supply Store</h1>
<div class="tag"><span>&ldquo;Everything you need. Nothing for sale.&rdquo;</span></div>
<div class="sub">A house advertisement &#183; for the things no store can stock</div>

<div class="grid">
 {cell("left:0;top:0;width:392px;height:294px",
   f'<span class="nm">&ldquo;Certain Place Stone&rdquo;</span>'
   f'<div style="display:flex;gap:10px;align-items:center;margin-top:4px">'
   f'{price("Only")}'
   f'<svg width="212" height="168" viewBox="0 0 124 102">{stone()}</svg></div>'
   f'<div class="quote knock">Pillow at night. Landmark by morning.</div>'
   f'<div class="itm" style="margin-top:5px">Item&#35; GEN-28:11 &#183; one moving part &#183; already where you need it</div>')}
 {cell("left:404px;top:0;width:232px;height:294px",
   f'<span class="nm small">&ldquo;Travel Staff&rdquo;</span>'
   f'<div style="display:flex;gap:8px;align-items:center;margin-top:2px">'
   f'{price("Just")}'
   f'<svg width="102" height="142" viewBox="0 0 90 116">{staff()}</svg></div>'
   f'<div class="quote">&ldquo;With just my staff I crossed this Jordan.&rdquo;</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-32:10 &#183; his words &#183; miles left in it</div>')}
 {cell("left:648px;top:0;width:233px;height:186px",
   f'<span class="nm small">&ldquo;Anointing Oil&rdquo;</span>'
   f'<div style="display:flex;gap:6px;align-items:center">'
   f'<svg width="86" height="96" viewBox="0 0 112 108">{oil()}</svg>'
   f'<div>{price("Still","$0")}</div></div>'
   f'<div class="quote">&ldquo;Marks the spot.&rdquo;</div>'
   f'<div class="itm" style="margin-top:2px">Item&#35; GEN-28:18 &#183; lasts 20 years</div>')}
 {cell("left:648px;top:198px;width:233px;height:96px;background:"+PAPER,
   f'<div style="font-size:20px;font-weight:800;text-transform:uppercase;line-height:1">Free advice</div>'
   f'<div style="font-size:11px;font-weight:700;margin-top:3px;line-height:1.28">A person reads every letter. Page 28.</div>'
   f'<div class="nm" style="margin-top:4px;font-size:11.5px">Trust us!</div>')}

 <div class="bar">Tell &rsquo;em you saw it in &ldquo;Between Sundays&rdquo; &#183; every item taken from one night in Genesis 28</div>

 {cell("left:0;top:360px;width:302px;height:290px",
   f'<span class="nm">&ldquo;Stairway&rdquo;</span>'
   f'<svg width="238" height="152" viewBox="0 0 156 108" style="margin-top:4px">{stairs()}</svg>'
   f'<div style="display:flex;gap:10px;align-items:baseline"><span class="burst">Amazing!</span>'
   f'<span class="quote knock">Traffic in both directions.</span></div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-28:12 &#183; ladder? ramp? &mdash; translators still arguing</div>')}
 {cell("left:314px;top:360px;width:288px;height:290px",
   f'<span class="nm">&ldquo;Coat&rdquo;</span>'
   f'<div style="display:flex;gap:12px;align-items:center;margin-top:4px">'
   f'<svg width="150" height="134" viewBox="0 0 110 100">{coat()}</svg>'
   f'<div class="pr"><i>Square deal</i><b style="font-size:28px">PAID<br/>FOR</b></div></div>'
   f'<div class="quote knock">Coat by day. Blanket by night. Tent if it rains.</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-28:20 &#183; &ldquo;clothing to put on&rdquo; &#183; one size: yours</div>')}
 {cell("left:614px;top:360px;width:267px;height:290px",
   f'<span class="nm">&ldquo;The Spine&rdquo;</span>'
   f'<div style="display:flex;gap:8px;align-items:center;margin-top:4px">'
   f'<svg width="152" height="126" viewBox="0 0 120 104">{spine()}</svg>'
   f'{price("No charge","$0")}</div>'
   f'<div class="quote knock">Made to be left somewhere.</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; PGS-23&ndash;26 &#183; the middle of this paper &#183; take ours, seriously</div>')}

 {cell("left:0;top:662px;width:302px;height:276px",
   f'<span class="nm small">&ldquo;All Four Directions&rdquo;</span>'
   f'<div style="display:flex;gap:10px;align-items:center;margin-top:4px">'
   f'<svg width="132" height="122" viewBox="0 0 110 102">{compass()}</svg>'
   f'{price("The set","$0")}</div>'
   f'<div class="quote">&ldquo;You will spread west, east, north, south.&rdquo;</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-28:14 &#183; not sold separately</div>')}
 {cell("left:314px;top:662px;width:288px;height:276px",
   f'<span class="nm small">&ldquo;Dust of the Earth&rdquo;</span>'
   f'<div style="display:flex;gap:10px;align-items:center;margin-top:4px">'
   f'<svg width="134" height="122" viewBox="0 0 112 106">{dustbag()}</svg>'
   f'{price("Per bag","$0")}</div>'
   f'<div class="quote knock">Family size. He was not exaggerating.</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-28:14 &#183; &ldquo;offspring like the dust of the earth&rdquo;</div>')}
 {cell("left:614px;top:662px;width:267px;height:276px",
   f'<span class="nm small">&ldquo;Early Morning&rdquo;</span>'
   f'<div style="display:flex;gap:10px;align-items:center;margin-top:4px">'
   f'<svg width="140" height="112" viewBox="0 0 110 74">{sunrise()}</svg>'
   f'{price("Daily","$0")}</div>'
   f'<div class="quote">&ldquo;He got up early and got on with it.&rdquo;</div>'
   f'<div class="itm" style="margin-top:4px">Item&#35; GEN-28:18 &#183; restocked overnight, every night</div>')}
</div>

<div class="order">
 <div class="hd">How to order</div>
 <ol>
  <li><b>Step 1</b>You can&rsquo;t. None of this was ever for sale.</li>
  <li><b>Step 2</b>All of it was handed over free, in one night, to a man asleep on the floor.
  The receipt is printed in full on pages 07&ndash;08.</li>
  <li><b>Step 3</b>Walk out with it. It was already yours when you picked up this paper.</li>
 </ol>
</div>
<div class="last">Now shipping, everywhere, since Genesis 28. No shipping required.</div>
<div class="folio">Between Sundays &#183; Issue 001 &#183; Page 41 &#183; a house advertisement</div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-41.html","w").write(DOC)
print("v2: kelly green · shaded art · closed-loop copy")
