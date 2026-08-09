#!/usr/bin/env python3
"""
Pages 16-17 — WORDS & MEANING. A facing sketchbook spread.
One blue ballpoint, cream paper, hand-lettering, wobbly rules, small ink
drawings. Seven Hebrew words from Genesis 28, defined factually from
public-domain lexicons (Strong's / BDB). No opinions printed.
"""
import os, random
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
INK="#2438B4"; PAPER="#F8F4E9"
random.seed(1617)
def j(a=1.6): return random.uniform(-a,a)

def uline(x1,x2,y,sw=2.6):
    return (f'<path d="M {x1+j()} {y+j()} Q {(x1+x2)/2} {y+j(3)+2} {x2+j()} {y+j()}" '
            f'fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>')
def box(x,y,w,h,sw=2.2):
    return (f'<path d="M {x+j()} {y+j()} L {x+w+j()} {y+j(2)} L {x+w+j()} {y+h+j()} '
            f'L {x+j(2)} {y+h+j()} Z" fill="none" stroke="{INK}" stroke-width="{sw}" '
            f'stroke-linejoin="round"/>')
def arrow(x1,y1,x2,y2,bend=8):
    mx,my=(x1+x2)/2+bend,(y1+y2)/2
    return (f'<path d="M {x1} {y1} Q {mx} {my} {x2} {y2}" fill="none" stroke="{INK}" '
            f'stroke-width="2" stroke-linecap="round"/>'
            f'<path d="M {x2-7} {y2-6} L {x2} {y2} L {x2-8} {y2+5}" fill="none" stroke="{INK}" '
            f'stroke-width="2" stroke-linecap="round"/>')

# small ink drawings, all jittered paths
DRAW={
"almond":f'''<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round">
 <path d="M 20 96 Q 34 54 56 30 Q 66 20 78 14"/>
 <path d="M 40 62 q -16 -8 -18 -24 q 16 2 22 16 z"/>
 <path d="M 58 40 q -4 -18 8 -30 q 10 14 2 28 z"/>
 <path d="M 66 52 q 18 -6 30 4 q -14 10 -28 4 z"/></g>''',
"stairs":f'''<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">
 <path d="M 12 100 L 34 100 L 34 82 L 56 82 L 56 64 L 78 64 L 78 46 L 100 46 L 100 28"/>
 <path d="M 30 20 L 44 20 M 37 13 L 37 27"/>
 <text x="58" y="22" font-size="15" fill="{INK}" font-family="Shantell Sans">?</text></g>''',
"pin":f'''<g fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round">
 <circle cx="50" cy="38" r="20"/><circle cx="50" cy="38" r="4" fill="{INK}"/>
 <path d="M 50 58 Q 48 76 50 96"/>
 <path d="M 30 96 L 70 96"/></g>''',
"envelope":f'''<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">
 <path d="M 14 30 L 96 26 L 98 82 L 16 86 Z"/>
 <path d="M 14 30 L 56 60 L 96 26"/>
 <path d="M 74 12 q 10 8 14 18" stroke-width="1.8"/></g>''',
"eye":f'''<g fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round">
 <path d="M 10 56 Q 55 18 100 56 Q 55 92 10 56 Z"/>
 <circle cx="55" cy="55" r="15"/><circle cx="55" cy="55" r="5" fill="{INK}"/>
 <path d="M 55 22 L 55 10 M 30 30 L 22 20 M 80 30 L 88 20"/></g>''',
"stone":f'''<g fill="none" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round">
 <path d="M 42 96 L 38 30 Q 38 18 50 16 Q 64 16 64 30 L 62 96 Z"/>
 <path d="M 22 96 L 84 96"/>
 <path d="M 44 42 L 58 40 M 45 58 L 59 56" stroke-width="1.6"/></g>''',
"house":f'''<g fill="none" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round">
 <path d="M 20 92 L 22 48 L 55 22 L 88 46 L 88 92 Z"/>
 <path d="M 12 52 L 55 18 L 98 50"/>
 <path d="M 46 92 L 46 66 L 64 66 L 64 92"/></g>'''}

def cell(x,y,w_,h_,word,heb,strongs,pos,defn,facts,langs,draw,tilt=0):
    fl="".join(f'<div class="fx">{f}</div>' for f in facts)
    lg="".join(f'<span>{l}</span>' for l in langs)
    return f'''<div class="cell" style="left:{x}px;top:{y}px;width:{w_}px;height:{h_}px;
 transform:rotate({tilt}deg)">
  <div class="wd"><b>{word}</b><i>{heb}</i></div>
  <div class="pos">{pos} &#183; {strongs}</div>
  <div class="df">{defn}</div>
  {fl}
  <div class="lg">{lg}</div>
  <div class="dr"><svg viewBox="0 0 110 110">{draw}</svg></div>
</div>'''

SHELL=f"""<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Shantell Sans","Bricolage Grotesque",cursive}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
svg.rules{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
.cell{{position:absolute;padding:6px 10px}}
.wd b{{font-size:44px;font-weight:700;letter-spacing:.01em;text-transform:uppercase;line-height:1}}
.wd i{{font-style:normal;font-size:30px;margin-left:12px;
 font-family:"Arial Hebrew","SBL Hebrew","Times New Roman",serif}}
.pos{{margin-top:5px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;opacity:.75}}
.df{{margin-top:8px;font-size:15.5px;line-height:1.42;font-weight:600}}
.fx{{margin-top:8px;font-size:13px;line-height:1.4;padding-left:14px;position:relative}}
.fx:before{{content:"→";position:absolute;left:-2px}}
.lg{{margin-top:9px;font-size:11.5px;line-height:1.7;opacity:.85}}
.lg span{{display:block}}
.dr{{width:100px;height:100px;margin:10px 4px 0 auto}}
.dr svg{{width:100%;height:100%}}
.mast b{{font-size:74px;font-weight:700;line-height:.94;letter-spacing:.01em}}
.mast .sub{{margin-top:12px;font-size:14px;line-height:1.5;font-weight:600;max-width:34ch}}
.badge{{display:inline-block;border:2.2px solid {INK};padding:4px 12px;font-size:13px;
 letter-spacing:.1em;text-transform:uppercase;transform:rotate(-2deg);margin-top:14px}}
.pgno{{position:absolute;bottom:18px;font-size:12px;opacity:.6}}
.src{{position:absolute;left:40px;right:40px;bottom:36px;font-size:10.5px;line-height:1.5;opacity:.8}}
.contn{{position:absolute;right:36px;top:44px;font-size:12px;transform:rotate(2deg)}}
</style>"""

# ── PAGE 16 ──────────────────────────────────────────────────────────────────
R16=(uline(48,560,206,3)+uline(48,430,238,2.4)
 +box(560,66,180,34)+arrow(700,120,660,180,-14)
 +uline(60,300,700)+uline(500,880,700)+uline(60,430,1046))
P16=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 16 · Words &amp; Meaning</title>
<link rel="stylesheet" href="fonts.css">{SHELL}</head><body><main class="page">
<svg class="rules" viewBox="0 0 {W} {H}">{R16}</svg>
<div class="cell mast" style="left:40px;top:60px;width:470px;height:560px">
  <b>WORDS &amp;<br/>MEANING</b>
  <div class="sub">Seven words from Genesis 28, looked up &mdash; not explained.
  What each one meant, where it came from, and what different translations did with it.
  No opinions on this spread. Just the dictionary.</div>
  <div class="badge">Genesis 28 : 10&ndash;22</div>
</div>
<div class="contn">issue 001 &#183; wednesday</div>
{cell(538,120,370,540,"Luz","לוּז","Strong's H3870","proper noun",
 "The town&rsquo;s name before Jacob renamed it. The word means almond tree.",
 ["The place already had a name, and the name already had a meaning.",
  "He renames it in the morning (v.19). The old name gets one more mention &mdash; then history."],
 ["English: Luz &#183; almond","Hebrew root also behind &ldquo;almond wood&rdquo; (Gen 30:37)"],
 DRAW["almond"],-0.6)}
{cell(40,712,430,560,"Sullam","סֻלָּם","Strong's H5551","noun",
 "Translated ladder. It appears exactly once in the entire Hebrew Bible &mdash; here.",
 ["Root salal: to heap up, to raise a mound.",
  "Ladder, stairway, or ramp &mdash; translators have never fully agreed."],
 ["Greek (LXX): κλῖμαξ klimax","Latin: scala","KJV: ladder &#183; NIV: stairway"],
 DRAW["stairs"],0.5)}
{cell(496,712,410,560,"Maqom","מָקוֹם","Strong's H4725","noun",
 "Place. A standing-place. Used six times in this one short story.",
 ["From qum: to stand, to rise.",
  "Centuries later, HaMaqom &mdash; &ldquo;The Place&rdquo; &mdash; became one of the Jewish names for God."],
 ["Greek (LXX): τόπος topos","Latin: locus","v.16: &ldquo;God is in this maqom.&rdquo;"],
 DRAW["pin"],-0.4)}
<span class="pgno" style="left:44px">16</span>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-16.html","w").write(P16)

# ── PAGE 17 ──────────────────────────────────────────────────────────────────
R17=(uline(60,420,84,2.6)+uline(60,410,656)+uline(500,880,656)+uline(500,880,84))
P17=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 17 · Words &amp; Meaning</title>
<link rel="stylesheet" href="fonts.css">{SHELL}</head><body><main class="page">
<svg class="rules" viewBox="0 0 {W} {H}">{R17}</svg>
{cell(40,96,430,540,"Mal'akh","מַלְאָךְ","Strong's H4397","noun",
 "The word translated angel. Its plain meaning: messenger.",
 ["Four chapters later Jacob sends mal&rsquo;akhim &mdash; human ones &mdash; ahead to his brother (Gen 32:3). Same word.",
  "You cannot tell from the word alone whether the messenger is heavenly or hired."],
 ["Greek: ἄγγελος angelos &mdash; also just &ldquo;messenger&rdquo;","English &ldquo;angel&rdquo; comes straight from it"],
 DRAW["envelope"],0.4)}
{cell(496,116,410,520,"Yare","יָרֵא","Strong's H3372","verb",
 "To fear. Also the root of the word translated awesome.",
 ["v.17: &ldquo;He was afraid (yare), and said: How awesome (nora) is this place.&rdquo;",
  "Afraid and awesome &mdash; one root, both in the same verse."],
 ["KJV: &ldquo;How dreadful is this place&rdquo;","Modern English split the word in two."],
 DRAW["eye"],-0.5)}
{cell(40,690,430,540,"Matsevah","מַצֵּבָה","Strong's H4676","noun",
 "A standing stone. The pillow, stood up on its end and marked.",
 ["From natsab: to stand, to be set upright.",
  "Deuteronomy 16:22 later bans setting up a matsevah. Same word, no comment."],
 ["Greek (LXX): στήλη stele","English: pillar &#183; standing stone"],
 DRAW["stone"],0.6)}
{cell(496,690,410,470,"Beth-El","בֵּית־אֵל","Strong's H1008","place name",
 "Beth: house. El: God. The whole name is those two words.",
 ["Same beth as Beth-lehem &mdash; house of bread.",
  "v.17 is the first time the Bible uses the phrase &ldquo;house of God.&rdquo; It is about a patch of open ground."],
 ["Greek (LXX): Βαιθήλ","One more name for the same spot appears in v.19: &ldquo;but the name of the city was Luz at first.&rdquo;"],
 DRAW["house"],-0.4)}
<div class="src">Definitions &amp; roots: Strong&rsquo;s Concordance and Brown&ndash;Driver&ndash;Briggs lexicon (public domain).
Verses: Genesis 28, World English Bible. Where scholars disagree, this page says so and stops.</div>
<span class="pgno" style="right:44px">17</span>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-17.html","w").write(P17)
print("p16 + p17 · words & meaning spread · 7 words")
