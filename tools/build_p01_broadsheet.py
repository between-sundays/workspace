#!/usr/bin/env python3
"""
Page 01 — FRONT PAGE, broadsheet edition.
Badge nameplate + circular seal, one condensed headline, one flat-colour
illustration with display type set inside it, then six columns of news copy
and a right rail of boxed briefs. Illustration is a SIZED HOLD.
"""
import os, math
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
W,H=941,1346
CREAM="#F6F1E3"; INK="#171512"; RED="#C4402B"; GOLD="#C79A3A"; INDIGO="#2A3A8C"
M=30

def seal():
    txt="".join(
      f'<text x="0" y="0" font-size="7.2" font-weight="800" letter-spacing="1.4" fill="{INK}" '
      f'transform="rotate({-90+i*(360/34)}) translate(0,-30)" text-anchor="middle">{ch}</text>'
      for i,ch in enumerate("BETWEEN SUNDAYS · GOOD NEWS PRINTED · "))
    steps="".join(f'<rect x="{-14+i*6}" y="{8-i*5}" width="6" height="5" fill="{INK}"/>' for i in range(5))
    return (f'<svg viewBox="-40 -40 80 80" width="76" height="76">'
            f'<circle r="37" fill="none" stroke="{INK}" stroke-width="1.6"/>'
            f'<circle r="25" fill="none" stroke="{INK}" stroke-width="1"/>'
            f'<g>{txt}</g><g transform="translate(0,4)">{steps}</g></svg>')

BRIEFS=[("The forecast","Rain, and then you will see",
 "Seven days of weather for the middle of a hard season, and one honest note about how long it lasts. The paper's weather desk does not pretend to know the date it clears.","Page 20"),
("The Spine","Four pages that are not yours",
 "The centre of this paper lifts out. It was written for somebody who did not buy it. Take it out, leave it somewhere deliberate, and do not tell anyone it was you.","Pages 23–26"),
("The directory","Look yourself up by what is wrong",
 "Two hundred and ten entries, filed A to Z by feeling rather than by book. Afraid. Broke. Grieving. Tired. Waiting. Every reference checked before printing.","Pages 34–35"),
("Next issue","A table in the wilderness",
 "Issue 002 goes looking for the meals nobody expected to eat — manna, ravens, five loaves, and a breakfast on a beach.","Page 47")]
briefs="".join(
 f'<div class="brief"><div class="bk">{k}</div><h4>{h}</h4><p>{p}</p><div class="bp">{pg}</div></div>'
 for k,h,p,pg in BRIEFS)

BODY=["""He left Beersheba in a hurry and he left alone. His brother wanted him dead and his father
had just handed him a blessing meant for somebody else, which is a strange pair of facts to carry
out of a house at speed. He took a road north and he took no company.""",
"""Late in the day he ran out of light. Not out of road — out of light. The account is unusually
plain about this: he stopped where he stopped because the sun had set, and for no other reason.
The place had a name already, though he did not use it. It was called Luz.""",
"""<span class="rh">He took a stone.</span> There is no suggestion he chose it carefully. He put it
under his head, lay down in the open, and slept the way people sleep when they have been walking
since morning and have nowhere to be until tomorrow.""",
"""What happened then is the reason this newspaper exists. He dreamed a stairway standing on the
earth with its top reaching heaven, and traffic on it moving in both directions at once. And
above it, unprompted and unearned, a voice with a promise attached: <i>I am with you, and I will
protect you wherever you go.</i>""",
"""He had asked for nothing. He had built nothing, kept nothing, and promised nothing. He was, at
the moment the promise arrived, asleep in the dirt with a rock under his ear.""",
"""<span class="rh">He woke up afraid.</span> That detail survives every translation. And then he
said the sentence this paper is named for, which is not a sentence of triumph but of correction:
&ldquo;Surely the Lord is in this place, and I was not aware of it.&rdquo;""",
"""Nothing about the field had changed overnight. There was no monument, no marked road, no reason
for anyone walking past the following week to slow down. What changed was his information.""",
"""In the morning he stood the stone up on its end, poured oil over it, and gave the empty ground
a new name. Bethel: house of God. The town kept its old name on the maps for years afterward.
Both names were accurate.""",
"""<span class="rh">Before he left</span> he made a deal, and it is not a flattering one. If God
will be with me, he said, and give me bread to eat and clothing to put on, and bring me home in
one piece &mdash; then he will be my God. He had been promised everything unconditionally about
four hours earlier. His first instinct was to open negotiations.""",
"""The words in the account repay slowing down, and this edition slows down on seven of them
starting page sixteen. The one that carries the most weight is the plainest. The Hebrew for
<i>place</i> is maqom, and it appears six times in twelve verses.""",
"""Centuries after this night, HaMaqom &mdash; The Place &mdash; became one of the Jewish names
for God himself. A man said God was in <i>this place</i>, and the word for place eventually
became a word for God. Nobody planned that. It is simply what happened to the vocabulary.""",
"""The stairway is stranger still. The word is sullam, and it appears exactly once in the entire
Hebrew Bible. Here. Nowhere else. Translators have rendered it ladder, ramp, and staircase, and
have never fully agreed, because there is nothing to compare it to.""",
"""The figures on it are usually called angels. The word is mal&rsquo;akh, which plainly means
messenger, and four chapters later the same word describes ordinary men Jacob hires to carry
word ahead to his brother. The vocabulary does not distinguish. Only the traffic does.""",
"""<span class="rh">The town kept its name.</span> Luz means almond tree, and the record is careful
to say so twice &mdash; the place he renamed had a name already, and a meaning already, and
people who had been living in it the whole time he thought he was nowhere.""",
"""That is the argument of this paper, printed here at the start so nobody has to go looking for
it. The ground people cross to get somewhere else is not a lesser grade of ground. The night you
were only trying to get through was not filler. The place had a name before you got there.""",
"""He walked five hundred more miles after this, worked twenty years for a man who cheated him
ten times over, and came home limping from a fight he did not start. Every promise made over
that stone was kept. None of it arrived early.
<span class="jump">Continued on Page 14</span>"""]
body="".join(f"<p>{p}</p>" for p in BODY)

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 01</title><link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};color:{INK};
 padding:{M}px}}
/* badge strip */
.badges{{display:flex;align-items:stretch;gap:0;border:2px solid {INK};height:64px}}
.bx{{border-right:1.5px solid {INK};padding:7px 12px;display:flex;flex-direction:column;
 justify-content:center}}
.bx:last-child{{border-right:0}}
.bx .lab{{font-size:6.5px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;opacity:.65}}
.bx .val{{font-size:14px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;margin-top:2px}}
.bx.wide{{flex:1}}
.bx.wide .val{{font-size:11.5px;letter-spacing:.12em}}
.bx.sealbx{{padding:0 10px;justify-content:center;align-items:center}}
h1{{margin:14px 0 0;font-size:104px;font-weight:800;line-height:.82;letter-spacing:-.045em;
 text-transform:uppercase;transform:scaleY(1.06);transform-origin:left top}}
.deck{{margin:16px 0 0;font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 border-top:2px solid {INK};border-bottom:2px solid {INK};padding:6px 0}}
/* illustration hold */
.art{{position:relative;height:346px;margin-top:12px;background:{GOLD};overflow:hidden}}
.art .hold{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 flex-direction:column;gap:6px;color:{INK}}}
.art .hold b{{font-size:13px;font-weight:800;letter-spacing:.24em;text-transform:uppercase}}
.art .hold span{{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;opacity:.7}}
.art .num{{position:absolute;right:16px;top:-8px;font-size:196px;font-weight:800;line-height:1;
 color:{CREAM};letter-spacing:-.06em;opacity:.92}}
.art .numlab{{position:absolute;right:22px;bottom:14px;writing-mode:vertical-rl;font-size:12px;
 font-weight:800;letter-spacing:.34em;text-transform:uppercase;color:{CREAM}}}
.art .cred{{position:absolute;left:12px;bottom:9px;font-size:8px;font-weight:800;letter-spacing:.16em;
 text-transform:uppercase;color:{INK};opacity:.65}}
/* body */
.deckrow{{display:grid;grid-template-columns:1fr 232px;gap:20px;margin-top:12px}}
.news{{column-count:5;column-gap:13px;column-rule:.8px solid rgba(23,21,18,.35)}}
.news p{{margin:0 0 7px;font-family:"Newsreader",Georgia,serif;font-size:9.4px;line-height:1.4;
 text-align:justify;hyphens:auto}}
.news p:first-child:first-letter{{font-family:"Fraunces",serif;font-weight:900;font-size:34px;
 line-height:.78;float:left;padding:4px 5px 0 0}}
.news .rh{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:8.6px;
 letter-spacing:.04em;text-transform:uppercase}}
.news .jump{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:8px;
 letter-spacing:.1em;text-transform:uppercase;color:{RED}}}
.rail{{border-left:2px solid {INK};padding-left:14px}}
.railhd{{font-size:9px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;
 border-bottom:2px solid {INK};padding-bottom:4px;margin-bottom:8px}}
.brief{{border-bottom:1px solid rgba(23,21,18,.35);padding-bottom:8px;margin-bottom:8px}}
.brief:last-child{{border-bottom:0}}
.bk{{font-size:7.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:{RED}}}
.brief h4{{margin:2px 0 3px;font-size:14.5px;font-weight:800;line-height:1;letter-spacing:-.01em;
 text-transform:uppercase}}
.brief p{{margin:0;font-family:"Newsreader",Georgia,serif;font-size:9.2px;line-height:1.38}}
.bp{{font-size:8px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;margin-top:3px;
 opacity:.7}}
.foot{{position:absolute;left:{M}px;right:{M}px;bottom:12px;border-top:2px solid {INK};padding-top:5px;
 display:flex;justify-content:space-between;font-size:8px;font-weight:800;letter-spacing:.16em;
 text-transform:uppercase}}
</style></head><body><main class="page">

<div class="badges">
 <div class="bx"><span class="lab">Year</span><span class="val">One</span></div>
 <div class="bx"><span class="lab">Edition</span><span class="val">001</span></div>
 <div class="bx wide"><span class="lab">Filed from</span>
  <span class="val">A certain place &#183; between Beersheba and Haran</span></div>
 <div class="bx"><span class="lab">Price</span><span class="val">Free</span></div>
 <div class="bx sealbx">{seal()}</div>
</div>

<h1>Nowhere is<br/>somewhere</h1>
<div class="deck">A man stopped walking because the light went, not because he had arrived
&#183; what he said in the morning renamed the ground &#183; the whole account, printed from page seven</div>

<div class="art">
 <div class="hold"><b>Illustration to come</b><span>Flat colour &#183; 881 &#215; 346 &#183; hold</span></div>
 <div class="num">28</div>
 <div class="numlab">Genesis</div>
 <div class="cred">Illustration: Between Sundays</div>
</div>

<div class="deckrow">
 <div class="news">{body}</div>
 <div class="rail"><div class="railhd">Also in this edition</div>{briefs}</div>
</div>

<div class="foot"><span>Between Sundays &#183; the Sunday paper for the places between Sundays</span>
 <span>Genesis 28:15 &#183; NLT</span><span>Page 01</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-01.html","w").write(DOC)
print("wrote press/between-sundays-page-01.html")
