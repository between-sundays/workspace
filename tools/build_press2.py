#!/usr/bin/env python3
"""
PRESS SLATE 2 — twelve more chassis pages, twelve different newspaper layouts.
Voice rule on every page: we are sharers, not scholars. Nothing preaches.
Easier translations (NIV/NLT) used with attribution; imprint notice on p02.
"""
import os, re
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
W,H=941,1346
INK="#191713"; CREAM="#F6F2E8"; RED="#B8412A"; INDIGO="#2A3A8C"; GOLD="#C79A3A"
GREEN="#185C3C"; BLUE="#24509E"; BROWN="#7A4A20"; PLUM="#5E2A54"

src=open("build_press.py",encoding="utf-8").read()
CHASSIS=src.split('CHASSIS=f"""')[1].split('"""')[0]
CHASSIS=CHASSIS.replace("{W}",str(W)).replace("{H}",str(H)).replace("{INK}",INK)\
 .replace("{CREAM}",CREAM).replace("{RED}",RED).replace("{{","{").replace("}}","}")
def page(n,body,extra=""):
    doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays</title><link rel="stylesheet" href="fonts.css">
<style>{CHASSIS}{extra}</style></head><body><main class="page">{body}</main></body></html>"""
    open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc); print("  p"+n)

def slug(name,sub,right,sec):
    return (f'<div class="slugband" style="--sec:{sec}"><span class="slug" style="color:{sec}">{name}'
            f'<small>{sub}</small></span><span>{right}</span></div>')
def folio(sec,pg):
    return (f'<div class="folio"><span>Between Sundays &#183; {sec}</span>'
            f'<span>Issue 001</span><span>Page {pg}</span></div>')

# ═══ 02 · ABOUT THIS PAPER (masthead page — the positioning, said plainly) ═══
page("02", slug("About this paper","who makes it, and why","Page 02 of 48",RED)+f"""
<div style="display:grid;grid-template-columns:1fr 292px;gap:28px">
 <div class="body">
  <div class="kicker" style="--sec:{RED}">First, the honest part</div>
  <h2 class="hl" style="font-size:40px;max-width:20ch">We are not scholars. We are mostly just the mail carriers.</h2>
  <p class="deck" style="max-width:60ch">This paper is made by people who are still learning,
  for people who are still learning. Here is what we can promise, and what we can&rsquo;t.</p>
  <div class="cols2" style="margin-top:14px">
   <p class="first">We did not write the good part of this paper. The good part is very old and
   holds up fine without us. Our job is smaller: pick it up, print it clearly, and hand it to you
   without smudging it.</p>
   <p>So you will not find much preaching in here. When we understand something, we print it.
   When we do not, we say so and print the verse anyway, because the verse does not need us
   to be finished with it before it can be useful to you.</p>
   <p><span class="rh">Most of what is in this issue is here because it helped us first.</span>
   The forecast page exists because one of us needed it in March. The write-it-down page exists
   because writing it down is the only way some of us remember anything.</p>
   <p>If you use this the way people use a verse-of-the-day app &mdash; one page with your coffee,
   most mornings &mdash; it will do its job. If you only ever read the middle four pages and then
   give them away, honestly, that is the job too.</p>
  </div>
 </div>
 <div>
  <div class="panel"><h4>A week of mornings &#183; clip this</h4>
   <div class="row"><b>Mon</b><span>Genesis 28:10&ndash;15 &mdash; the dream</span></div>
   <div class="row"><b>Tue</b><span>Genesis 28:16&ndash;17 &mdash; waking up</span></div>
   <div class="row"><b>Wed</b><span>Psalm 121 &mdash; for the road</span></div>
   <div class="row"><b>Thu</b><span>Genesis 28:18&ndash;19 &mdash; the stone</span></div>
   <div class="row"><b>Fri</b><span>Psalm 139:7&ndash;12 &mdash; nowhere too far</span></div>
   <div class="row"><b>Sat</b><span>Genesis 28:20&ndash;22 &mdash; the vow</span></div>
   <div class="row"><b>Sun</b><span>John 1:43&ndash;51 &mdash; the dream, quoted</span></div>
  </div>
  <div class="godeeper" style="margin-top:14px;--sec:{RED}">
   <h5>The translations we print</h5>
   <p style="font-size:11.5px;line-height:1.5">We mostly use plain-language Bibles, because that
   is how we read too. Verses marked NIV or NLT are used by permission under their publishers&rsquo;
   quotation terms; unmarked verses are World English Bible, public domain. Full notices below.</p>
   <p style="font-size:9.5px;line-height:1.5;opacity:.7;margin-top:8px">Scripture marked NIV taken from the Holy
   Bible, New International Version&reg;. Scripture marked NLT taken from the Holy Bible, New
   Living Translation. Used by permission. All rights reserved by their respective publishers.</p>
  </div>
 </div>
</div>
<div class="coupon" style="position:absolute;left:40px;right:40px;bottom:56px">
 <div style="display:flex;gap:24px;align-items:center">
  <div style="flex:1">
   <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#B8412A">When you are done with this copy</div>
   <p style="font-size:13px;margin:6px 0 0;line-height:1.45">Do not recycle it. Write your first name below and
   leave it somewhere deliberate &mdash; a break room, a bus seat, a waiting room. This paper is designed
   to be second-hand.</p>
  </div>
  <div class="sans" style="width:250px;font-size:9px;font-weight:800;letter-spacing:.14em;text-transform:uppercase">
   Passed on by<div style="border-bottom:1.5px solid #191713;height:22px;margin-top:4px"></div>
   <div style="margin-top:8px">And then by</div><div style="border-bottom:1.5px solid #191713;height:22px;margin-top:4px"></div>
  </div>
 </div>
</div>"""+folio("About","02"))

# ═══ 13 · THE BRIDGE (marginalia layout — notes in the margin, not a lesson) ═══
NOTES=[("v.11","&ldquo;a certain place&rdquo; &mdash; it has no name yet. We liked that it starts nameless."),
("v.11","He used a rock because he had nothing better. Nobody packs for the night that changes things."),
("v.12","A stairway, not a wall. The traffic on it goes both directions."),
("v.15","&ldquo;I am with you&rdquo; comes while he is asleep. He did nothing to start this."),
("v.16","He says &ldquo;I was not aware of it.&rdquo; That is the whole paper in one line."),
("v.17","He is afraid AND calls it awesome. Page 16 looks at why those are the same word.")]
notes="".join(f'<div class="mn"><b>{a}</b><span>{b}</span></div>' for a,b in NOTES)
page("13", slug("The bridge","what we noticed, reading it slow","after the Reading &#183; before the feature",INDIGO)+f"""
<div class="kicker" style="--sec:{INDIGO}">Not a lesson &#183; just margin notes</div>
<h2 class="hl" style="font-size:38px;max-width:24ch">We read it slower the second time. Here is what we underlined.</h2>
<p class="deck" style="max-width:64ch">Six small things we noticed in Genesis 28. We are not
telling you what it means. We are showing you where we stopped.</p>
<div style="display:grid;grid-template-columns:1fr 330px;gap:30px;margin-top:16px">
 <div class="body">
  <p class="vs2"><sup>11</sup>He came to a certain place, and stayed there all night, because the
  sun had set. He took one of the stones of the place, and put it under his head&hellip;</p>
  <p class="vs2"><sup>12</sup>He dreamed. Behold, a stairway set upon the earth, and its top reached
  to heaven&hellip;</p>
  <p class="vs2"><sup>15</sup>Behold, I am with you, and will keep you, wherever you go&hellip;</p>
  <p class="vs2"><sup>16</sup>Jacob awakened out of his sleep, and he said, &ldquo;Surely Yahweh is
  in this place, and I didn&rsquo;t know it.&rdquo;</p>
  <p class="vs2"><sup>17</sup>He was afraid, and said, &ldquo;How awesome this place is! This is none
  other than God&rsquo;s house, and this is the gate of heaven.&rdquo;</p>
  <p style="font-size:11px;opacity:.6;margin-top:10px">Genesis 28, World English Bible, shortened
  here &mdash; printed whole on pages 07&ndash;08.</p>
 </div>
 <div class="mrail">{notes}</div>
</div>
<div style="border-top:3px solid {INDIGO};margin-top:20px;padding-top:12px;max-width:70ch">
 <p style="font-size:14px;line-height:1.5;margin:0">If you underlined something different, that is
 not a problem with you or with us. Keep your pencil out. The feature starts on the next page.</p>
</div>
<div style="position:absolute;left:40px;right:40px;bottom:56px;border:2px solid #2A3A8C;padding:14px 16px">
 <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#2A3A8C">Your margin &#183; what did you stop at?</div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;margin-top:10px">
  <div><div class="sans" style="font-size:9px;font-weight:800;opacity:.5">v.____</div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div></div>
  <div><div class="sans" style="font-size:9px;font-weight:800;opacity:.5">v.____</div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div></div>
  <div><div class="sans" style="font-size:9px;font-weight:800;opacity:.5">v.____</div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:26px"></div></div>
 </div>
</div>"""+folio("The bridge","13"),
f""".vs2{{font-size:18px;line-height:1.6;margin:0 0 14px}}
.vs2 sup{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;color:{INDIGO};margin-right:5px}}
.mrail{{border-left:2.5px solid {INDIGO};padding-left:18px}}
.mn{{margin-bottom:15px}}
.mn b{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;letter-spacing:.14em;
 color:{INDIGO};display:block;margin-bottom:2px}}
.mn span{{font-size:13px;line-height:1.45;font-style:italic}}""")

# ═══ 14 · THE FEATURE (long-form, continued from p01) ═══
page("14", slug("The feature","continued from Page 01","part one of three",RED)+f"""
<div class="kicker" style="--sec:{RED}">Twenty years, reported</div>
<h2 class="hl" style="font-size:48px;max-width:18ch">The trip was 500 miles. The detour was twenty years.</h2>
<p class="byline">The story so far: a man fled his brother, slept on open ground, and woke up
with a promise he did not ask for. This is what happened next.</p>
<div class="body cols3" style="margin-top:14px">
 <p class="first">He got up the next morning and kept walking. That is the first thing worth
 saying about him: the biggest night of his life did not excuse him from the next five hundred
 miles. He still had to do the road.</p>
 <p>At the end of it he met his match. His uncle Laban was the one man in the region who could
 out-scheme him, and for the next twenty years, he did. Jacob worked seven years for the woman
 he loved and got handed her sister at the wedding. He worked seven more. Then six on top of
 that, while his wages changed ten times.</p>
 <p><span class="rh">Here is what the promise did not do.</span> It did not shorten the twenty
 years. It did not soften his uncle. It did not skip him past one single hard season. If you
 have ever been promised that faith fast-forwards the difficult part, this story quietly
 disagrees.</p>
 <p>Here is what it did do. It held. Through the wrong wedding, the changed wages, the years
 that looked like nothing was moving &mdash; the sentence from the dirt stayed true: <i>I am with
 you, and will keep you, wherever you go.</i> He left with a staff. He came back with a family,
 flocks, and a limp he picked up wrestling through one long night by a river.</p>
 <p>The limp matters. He did not come back unmarked. He came back kept. Those are different
 things, and this paper thinks the difference is most of the point.</p>
 <p>Twenty years after the stone, he stood on the same ground again and built an altar there.
 Same field. Same man, mostly. Every promise from the dream, kept &mdash; slowly, the way the
 real ones usually are. &nbsp;<span class="jump" style="color:{RED}">The vow he made that morning: Page 33 &#8594;</span></p>
</div>
<div style="border-top:3px solid {RED};margin-top:16px;padding-top:12px;display:flex;gap:26px;align-items:baseline">
 <div style="font-family:'Fraunces',serif;font-weight:900;font-size:30px;line-height:1.05;max-width:22ch">
  &ldquo;He did not come back unmarked. He came back kept.&rdquo;</div>
 <p style="font-size:12.5px;line-height:1.5;max-width:34ch;margin:0">Read it yourself &mdash; the
 whole stretch runs Genesis 29 to 33. It is shorter than you think and stranger than we could
 make it sound.</p>
</div>
<div style="position:absolute;left:40px;right:40px;bottom:56px;border:2px solid #191713">
 <h4 class="sans" style="margin:0;background:#B8412A;color:#F6F2E8;font-size:10px;font-weight:800;
  letter-spacing:.2em;text-transform:uppercase;padding:7px 12px">Twenty years, in agate</h4>
 <div class="sans" style="display:grid;grid-template-columns:repeat(6,1fr);padding:10px 12px;font-size:10.5px;line-height:1.45;gap:8px">
  <div><b>YR 0</b><br/>Sleeps on rock. Hears promise.</div>
  <div><b>YR 7</b><br/>Marries the wrong sister. Not his idea.</div>
  <div><b>YR 7 + 1WK</b><br/>Marries the right one. Owes seven more.</div>
  <div><b>YR 14&ndash;20</b><br/>Wages changed ten times. Flocks grow anyway.</div>
  <div><b>YR 20</b><br/>Leaves at night. Wrestles till dawn. Limps.</div>
  <div><b>AFTER</b><br/>Same field, new altar, new name.</div>
 </div>
</div>"""+folio("The feature","14"))

# ═══ 17 · FIELD GUIDE (knolling page — everything he had that night) ═══
def obj(x,y,w_,h_,svg,name,note):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w_}px;text-align:center">'
            f'<svg viewBox="0 0 100 74" style="width:{w_}px;height:{h_}px">{svg}</svg>'
            f'<div class="ol"><b>{name}</b><span>{note}</span></div></div>')
S=f'stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"'
objs=(
 obj(70,320,180,120,f'<path d="M 24 62 Q 20 34 42 26 Q 68 20 78 38 Q 84 54 68 62 Q 44 70 24 62 Z" {S}/><path d="M 34 44 L 52 40 M 38 54 L 58 50" stroke="{INK}" stroke-width="1.6"/>',"The stone","pillow, then landmark &#183; v.11, v.18"),
 obj(330,300,150,140,f'<path d="M 50 6 L 44 70 M 44 70 L 40 72 M 50 6 L 56 12" {S}/>',"The staff","his entire net worth &#183; Gen 32:10"),
 obj(560,310,160,130,f'<path d="M 38 20 L 62 20 L 66 30 L 58 30 L 58 62 Q 48 70 40 62 L 40 30 L 34 30 Z" {S}/><path d="M 44 40 L 54 40" stroke="{INK}" stroke-width="1.6"/>',"Oil","poured on the stone at sunrise &#183; v.18"),
 obj(70,548,180,120,f'<path d="M 20 30 Q 50 12 80 30 L 74 64 Q 50 74 26 64 Z" {S}/><path d="M 30 40 Q 50 30 70 40" stroke="{INK}" stroke-width="1.6"/>',"A coat","also the blanket &#183; also the tent"),
 obj(330,548,150,128,f'<path d="M 26 50 L 74 50 M 30 50 L 34 64 L 66 64 L 70 50 M 38 50 L 40 40 L 60 40 L 62 50" {S}/>',"Road dust","five hundred miles of it ahead"),
 obj(560,548,160,128,f'<circle cx="50" cy="38" r="24" stroke-dasharray="5 6" {S}/><text x="50" y="44" text-anchor="middle" font-size="17" fill="{INK}" font-family="Fraunces" font-weight="900">?</text>',"The promise","not packed &#183; not visible &#183; did the most work"))
page("17", slug("Field guide","everything he had that night","an inventory",GOLD)+f"""
<div class="kicker" style="--sec:#9A7522">Travel light &#183; involuntarily</div>
<h2 class="hl" style="font-size:40px;max-width:22ch">Complete inventory, night one.</h2>
<p class="deck" style="max-width:62ch">Laid out flat, everything the man in our cover story had
with him. We counted. It did not take long.</p>
<div style="position:relative;height:742px;border:2px solid {INK};margin-top:12px;background:#F1EBDC;overflow:hidden">
 <div class="sans" style="position:absolute;top:12px;left:14px;font-size:9px;font-weight:800;
  letter-spacing:.2em;text-transform:uppercase;opacity:.5">Fig. 1 &mdash; actual belongings, actual scale of ambition</div>
 {objs}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:14px">
 <p style="font-size:13.5px;line-height:1.5;margin:0">Years later he says it himself: &ldquo;with
 just my staff I crossed this Jordan&rdquo; (Genesis 32:10). One item. We have carry-ons with
 more redundancy than his whole life had.</p>
 <p style="font-size:13.5px;line-height:1.5;margin:0">We are not saying pack less. We are saying
 the shortest item on this list is the one that carried him, and it did not weigh anything.</p>
</div>
<div style="position:absolute;left:40px;right:40px;bottom:56px;border-top:3px solid #9A7522;padding-top:10px;
 display:flex;justify-content:space-between;gap:24px;align-items:baseline">
 <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap">
  Same inventory, twenty years later:</div>
 <p style="margin:0;font-size:13px;line-height:1.45;flex:1">two camps of people and animals, eleven sons, and
 the same staff &mdash; &ldquo;with just my staff I crossed this Jordan, and now I have become two camps.&rdquo;
 Genesis 32:10. The invisible line-item came through.</p>
</div>"""+folio("Field guide","17"),
f""".ol b{{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:12px;font-weight:800;
 letter-spacing:.08em;text-transform:uppercase;margin-top:6px}}
.ol span{{display:block;font-size:11px;line-height:1.35;opacity:.7}}""")

# ═══ 21 · CAST OF NOTE: JACOB (the Crooklyn data-card layout) ═══
page("21", slug("Cast of note","a file on the main character","clip &amp; collect &#183; No. 1",BLUE)+f"""
<div style="display:grid;grid-template-columns:330px 1fr;gap:28px;margin-top:4px">
 <div>
  <div class="panel" style="border-width:2.5px"><h4>Subject file</h4>
   <div class="row"><b>Name</b><span>Jacob, later Israel</span></div>
   <div class="row"><b>First seen</b><span>Genesis 25, holding his twin&rsquo;s heel</span></div>
   <div class="row"><b>Occupation</b><span>Shepherd &#183; negotiator &#183; runaway</span></div>
   <div class="row"><b>Genre</b><span>Family drama, with comedy</span></div>
   <div class="row"><b>Runtime</b><span>Genesis 25&ndash;50, about 90 minutes read aloud</span></div>
   <div class="row"><b>Distinguishing mark</b><span>A limp, from Genesis 32</span></div>
  </div>
  <div class="panel" style="margin-top:14px"><h4>Flag for</h4>
   <div class="row"><span>Deception (his, mostly)</span></div>
   <div class="row"><span>Family separation</span></div>
   <div class="row"><span>Workplace disputes, 20 years</span></div>
   <div class="row"><span>One all-night wrestling scene</span></div>
  </div>
 </div>
 <div class="body">
  <div class="kicker" style="--sec:{BLUE}">Why we keep his file on top</div>
  <h2 class="hl" style="font-size:38px">Not the hero type. Kept anyway.</h2>
  <p style="font-size:14px;line-height:1.55;margin-top:10px">We want to be careful here, because
  this is where papers like ours usually start preaching. So, just the record: he cheated his
  brother twice, lied to his blind father, got cheated himself for twenty years, and split town
  at least three times. The promise from page 07 was made to <i>that</i> man, mid-scheme,
  asleep on a rock.</p>
  <p style="font-size:14px;line-height:1.55">We do not fully understand why God works that way.
  We just notice that he does, over and over, and that it is good news for people like us.</p>
  <div class="panel" style="margin-top:16px"><h4>Trivia</h4>
   <div class="row"><span>&#9733; His name meant &ldquo;heel-grabber.&rdquo; He earned it twice
   before he could walk.</span></div>
   <div class="row"><span>&#9733; The stairway dream gets quoted by Jesus, by name, in John 1:51.</span></div>
   <div class="row"><span>&#9733; He is mentioned in roughly half the books of the Bible &mdash;
   usually as part of the phrase &ldquo;the God of Jacob.&rdquo; The scheming runaway became the
   reference point.</span></div>
  </div>
  <div class="godeeper" style="margin-top:16px;--sec:{BLUE}">
   <h5>If you liked this character, meet</h5>
   <p><b>Joseph</b> &mdash; his son. Genesis 37&ndash;50. The family drama goes up a level.</p>
   <p><b>Peter</b> &mdash; same energy, New Testament. Luke 22, John 21.</p>
  </div>
 </div>
</div>
<div style="position:absolute;left:40px;right:40px;bottom:56px;border:2px dashed #191713;padding:11px 14px;
 display:flex;gap:22px;align-items:baseline">
 <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#24509E;white-space:nowrap">
  Clip this file &#183; collect the set</div>
 <p class="sans" style="margin:0;font-size:10.5px;line-height:1.5;flex:1">COMING FILES &mdash; No. 2 JOSEPH (the son, the pit,
 the palace) &#183; No. 3 RUTH (the in-law who stayed) &#183; No. 4 PETER (the loud one) &#183; No. 5 THE WOMAN AT
 THE WELL (they never printed her name; we will not guess it)</p>
</div>"""+folio("Cast of note","21"))

# ═══ 28 · LETTERS (the page is honest about being empty) ═══
page("28", slug("Letters","to the paper","the mailbag, issue one",GREEN)+f"""
<div class="kicker" style="--sec:{GREEN}">A confession</div>
<h2 class="hl" style="font-size:40px;max-width:22ch">This page is for your letters. We have not received any.</h2>
<p class="deck" style="max-width:66ch">This is Issue 001 &mdash; it went to print before a single
reader had seen it. So instead of pretending, here is exactly what this page will be, and how
to get into it.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:16px">
 <div class="body">
  <p class="first">Every issue after this one, this page belongs to readers. Letters, questions,
  arguments, corrections. Especially corrections &mdash; we are new at this and we would rather
  be fixed than flattered.</p>
  <p>What we hope gets sent in: where you were when a verse landed. What you taped to the
  fridge. What you disagreed with. Where you left the Spine, and whether you saw who picked
  it up.</p>
  <p><span class="rh">What we will not print:</span> anything that makes another reader feel
  small. Life is doing enough of that.</p>
  <div class="panel" style="margin-top:14px"><h4>Prompts, if the page is blank at your house too</h4>
   <div class="row"><span>The place you almost walked past &mdash; where is yours?</span></div>
   <div class="row"><span>Your &ldquo;but God&rdquo; line, if you have one yet (p.33)</span></div>
   <div class="row"><span>One question you want asked in a future issue</span></div>
  </div>
 </div>
 <div>
  <div class="coupon">
   <div class="ah" style="color:{GREEN};font-family:'Bricolage Grotesque',sans-serif;font-size:10px;
    font-weight:800;letter-spacing:.18em;text-transform:uppercase">Write to us &#183; it will be read by a person</div>
   <p style="font-size:13px;margin:8px 0 12px">Post: The Mailbag, Between Sundays.<br/>
   Or the address printed on page 02.</p>
   <div class="fline"><span>Dear Between Sundays,</span><i></i></div>
   <div class="fline"><span></span><i></i></div>
   <div class="fline"><span></span><i></i></div>
   <div class="fline"><span></span><i></i></div>
   <div class="fline"><span></span><i></i></div>
   <div class="fline"><span>From</span><i></i></div>
  </div>
  <div class="godeeper" style="margin-top:14px;--sec:{GREEN}">
   <h5>Why letters matter to us</h5>
   <p>&ldquo;As iron sharpens iron, so a friend sharpens a friend&rdquo; &mdash; Proverbs 27:17.
   The other option is us talking to ourselves, and there is a name for papers that do that.
   We would rather be sharpened.</p>
  </div>
 </div>
</div>
<div style="position:absolute;left:40px;right:40px;bottom:56px;border:2px dashed #191713;padding:12px 16px">
 <div style="display:flex;gap:26px">
  <div style="flex:1">
   <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#185C3C">Or cut out this postcard &#183; a stamp finishes it</div>
   <p style="font-size:12.5px;margin:6px 0 0;line-height:1.45">One sentence is a real letter. &ldquo;It helped&rdquo;
   is a real letter. &ldquo;Page 20 was wrong about the rain&rdquo; is a real letter, and honestly one of our
   favorite kinds.</p>
  </div>
  <div style="width:300px;border-left:1.5px solid rgba(25,23,19,.4);padding-left:18px">
   <div style="border:1.5px solid #191713;width:52px;height:60px;margin-left:auto;display:flex;align-items:center;
    justify-content:center;font-size:8px;text-align:center;font-family:Bricolage Grotesque">STAMP<br/>HERE</div>
   <div class="sans" style="font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:6px">To: The Mailbag, Between Sundays</div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:20px"></div>
   <div style="border-bottom:1.2px solid rgba(25,23,19,.5);height:20px"></div>
  </div>
 </div>
</div>"""+folio("Letters","28"),
f""".fline{{display:flex;gap:10px;align-items:baseline;margin-top:16px}}
.fline span{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;opacity:.6;white-space:nowrap}}
.fline i{{flex:1;border-bottom:1.5px solid {INK}}}""")

# ═══ 29 · FICTION ═══
page("29", slug("Fiction","a short story","complete in this issue",PLUM)+f"""
<div class="kicker" style="--sec:{PLUM}">The man who carried a chair</div>
<h2 class="hl" style="font-size:42px;max-width:20ch">The Man Who Carried a Chair</h2>
<p class="byline">A short story &#183; about six minutes</p>
<div class="body cols2" style="margin-top:12px">
 <p class="first">The man carried a folding chair everywhere he went, and our town never let
 him forget it. He carried it to the bus stop, to the bank line, to the school pickup, hooked
 over his shoulder like a doctor&rsquo;s bag. Kids called him Chair Guy. He waved.</p>
 <p>The strange part was that he almost never sat in it.</p>
 <p>He set it up for other people. The pregnant woman at the pharmacy, the old man whose bus
 was twenty minutes out, the girl crying on the curb outside the courthouse with nowhere to
 put herself. He would unfold it without a word, set it down, and step back. Then he stood,
 sometimes for an hour, a little way off, like a valet for one piece of furniture.</p>
 <p>My uncle asked him once why he did it. He thought about it longer than the question
 seemed to need.</p>
 <p>&ldquo;Somebody did it for me,&rdquo; he said. &ldquo;Worst year of my life, a stranger kept
 showing up with exactly what I needed, right when I needed it. Never explained. I never got
 to thank them properly.&rdquo; He tapped the chair. &ldquo;So now I go around being the
 stranger.&rdquo;</p>
 <p>My uncle said, &ldquo;That&rsquo;s it? That&rsquo;s the whole reason?&rdquo;</p>
 <p>&ldquo;That&rsquo;s the whole reason,&rdquo; Chair Guy said. &ldquo;It is not complicated.
 It is just heavy some days.&rdquo;</p>
 <p>He died the spring before last. The funeral was enormous and confused &mdash; hundreds of
 people who had each assumed they were one of maybe three or four. The chair was up front,
 unfolded, empty. Nobody sat in it, which felt right, and everybody understood at the same
 moment, which felt like something else.</p>
 <p>These days there are chairs all over town. Cheap folding ones, mostly, leaned against
 lampposts with little tags: <i>TAKE A SEAT. LEAVE IT FOR THE NEXT ONE.</i> The city took a
 vote about whether to clear them off the sidewalks.</p>
 <p>It did not go the city&rsquo;s way. &#9632;</p>
</div>
<div style="border-top:3px solid {PLUM};margin-top:14px;padding-top:10px;max-width:70ch">
 <p style="font-size:12px;line-height:1.5;margin:0;font-style:italic">Fiction lives here every issue.
 &ldquo;Jesus always used stories and illustrations like these&hellip; he never spoke to them without
 using such parables&rdquo; (Matthew 13:34, NLT). Stories get past our defenses in a way
 instructions do not. We are only copying the method.</p>
</div>"""+folio("Fiction","29"))

# ═══ 36 · CLASSIFIEDS (dense agate) ═══
def cls(head,items,sec=INK):
    rows="".join(f'<p class="ci">{i}</p>' for i in items)
    return f'<div class="cbl"><h6 style="background:{sec}">{head}</h6>{rows}</div>'
page("36", slug("Classifieds","notices &#183; lost &amp; found &#183; work","free listings, forever",RED)+f"""
<div class="clsgrid">
{cls("Lost &amp; found",[
 "<b>LOST:</b> One sheep. Answers to its name. Owner has left the other ninety-nine and is out looking. Luke 15:4.",
 "<b>FOUND:</b> One coin, after the whole house got swept. There was a party. Luke 15:9.",
 "<b>LOST, THEN FOUND:</b> One son. Was dead, is alive. His father saw him from a long way off. Luke 15:20.",
 "<b>MISLAID:</b> The point of most of our worrying. If seen, do not return."],RED)}
{cls("Work",[
 "<b>HELP WANTED:</b> Harvest hands. The harvest is plentiful, the workers are few. No experience needed. Luke 10:2.",
 "<b>SITUATION WANTED:</b> Former fisherman seeks people-fishing role. References: one, excellent. Matthew 4:19.",
 "<b>NOTICE TO OUR STAFF:</b> Whoever wants to be first must be the servant of all. This changes the org chart considerably. Mark 9:35."],BLUE)}
{cls("Housing",[
 "<b>ROOM AVAILABLE:</b> My Father&rsquo;s house has many rooms. One is being prepared now. John 14:2.",
 "<b>BUILD ADVISORY:</b> Sand lots are priced to move for a reason. Rock costs more and is worth it. Matthew 7:24&ndash;27.",
 "<b>FOR THE BIRDS:</b> Nests available in the branches of a tree that started as the smallest seed in the garden. Mark 4:32."],GREEN)}
{cls("Missed connections",[
 "<b>YOU:</b> at the well at noon, avoiding the morning crowd. <b>ME:</b> asked you for a drink and knew everything already. You left your jar. John 4.",
 "<b>YOU:</b> up a sycamore tree, too short to see over anyone. <b>ME:</b> stopped underneath and invited myself to dinner. Luke 19.",
 "<b>YOU:</b> on the road to Emmaus, talking about the weekend. <b>ME:</b> walked the whole way with you. You did not recognize me until the bread. Luke 24."],PLUM)}
{cls("Public notices",[
 "<b>NOTICE:</b> The middle four pages of this newspaper are missing from some copies. This is not a printing error. Someone left them for you somewhere, or you are meant to leave them for someone. Page 23.",
 "<b>CORRECTION:</b> In a previous life, this space would have sold you something. We are still getting used to it too.",
 "<b>ANNOUNCEMENT:</b> The editors of this paper do not fully understand everything they print. We ran it anyway. See page 02."],INK)}
</div>"""+folio("Classifieds","36"),
f""".clsgrid{{column-count:3;column-gap:22px;column-rule:1px solid rgba(25,23,19,.3);margin-top:6px}}
.cbl{{break-inside:avoid;margin-bottom:18px}}
.cbl h6{{margin:0 0 8px;color:{CREAM};font-family:"Bricolage Grotesque",sans-serif;font-size:9.5px;
 font-weight:800;letter-spacing:.2em;text-transform:uppercase;padding:6px 10px}}
.ci{{margin:0 0 9px;font-size:11.5px;line-height:1.45;border-bottom:1px dotted rgba(25,23,19,.3);
 padding-bottom:9px}}""")

# ═══ 37 · FOOD (a real recipe, devotionally used) ═══
page("37", slug("Food","one loaf, from scratch","the slowest page in the paper",BROWN)+f"""
<div style="display:grid;grid-template-columns:1fr 288px;gap:26px">
 <div>
  <div class="kicker" style="--sec:{BROWN}">Why bread, why here</div>
  <h2 class="hl" style="font-size:40px;max-width:20ch">Make the thing he told us to ask for.</h2>
  <p class="deck" style="max-width:56ch">&ldquo;Give us today the food we need&rdquo; (Matthew 6:11,
  NLT). We noticed we pray that fastest of any line in the prayer. So this page slows it down
  to about four hours, most of it waiting.</p>
  <div class="body cols2" style="margin-top:12px">
   <p><span class="rh">1.</span> Stir the yeast into the warm water and let it sit ten minutes,
   until it foams. If it does not foam, the yeast is dead; start over. (Some things you cannot
   rush or fake. This page is full of those.)</p>
   <p><span class="rh">2.</span> Add the flour and salt. Mix until shaggy, then knead ten
   minutes. It will be sticky and discouraging for the first five. Keep going.</p>
   <p><span class="rh">3.</span> Cover the bowl. Walk away for two hours. This is the part of
   the recipe we are worst at. Nothing you can do speeds it up; it rises on its own schedule,
   in the dark, while you do something else.</p>
   <p><span class="rh">4.</span> Punch it down, shape it, and let it rise once more, forty-five
   minutes. Bake at 450&deg; for 30 minutes, until it sounds hollow when you knock.</p>
   <p><span class="rh">5.</span> Eat it warm, with someone if you can manage it. Day-old bread
   is fine. Day-old is how manna worked too &mdash; enough for today, fresh again tomorrow
   (Exodus 16).</p>
  </div>
 </div>
 <div>
  <figure><img src="img/bread-half.jpg" alt="" style="width:100%"/>
   <figcaption><span>The finished loaf. Yours will look different, which is correct.</span>
   <i>Halftone: BS studio</i></figcaption></figure>
  <div class="panel" style="margin-top:14px"><h4>You need</h4>
   <div class="row"><b>Flour</b><span>500 g, plain</span></div>
   <div class="row"><b>Water</b><span>325 ml, warm</span></div>
   <div class="row"><b>Yeast</b><span>7 g &#183; one packet</span></div>
   <div class="row"><b>Salt</b><span>10 g</span></div>
   <div class="row"><b>Time</b><span>4 hours, mostly waiting</span></div>
  </div>
  <div class="godeeper" style="margin-top:14px;--sec:{BROWN}">
   <h5>While it rises</h5>
   <p><b>Exodus 16</b> &mdash; daily bread, the original test run.</p>
   <p><b>John 6:35</b> &mdash; where bread stops being about bread.</p>
  </div>
 </div>
</div>"""+folio("Food","37"))

# ═══ 40 · MUSIC — THE CHARTS ═══
CHART=[(1,"Psalm 121","I lift up my eyes to the mountains","18 weeks","&#9650;"),
(2,"Psalm 23","The LORD is my shepherd","3,000 years","&#9644;"),
(3,"Psalm 139","Where can I go from your Spirit?","12 weeks","&#9650;"),
(4,"Psalm 46","Be still, and know","9 weeks","&#9650;"),
(5,"Psalm 42","As the deer pants for streams","6 weeks","&#9660;"),
(6,"Psalm 30","Joy comes in the morning","5 weeks","&#9650;"),
(7,"Psalm 137","By the rivers of Babylon","4 weeks","new"),
(8,"Psalm 150","Let everything that has breath","2 weeks","&#9650;")]
rows="".join(f'<tr><td class="pos">{p}</td><td><b>{t}</b><br/><span>{l}</span></td>'
             f'<td>{w}</td><td class="mv">{m}</td></tr>' for p,t,l,w,m in CHART)
page("40", slug("Music","songs for walking home","the charts",BLUE)+f"""
<div style="display:grid;grid-template-columns:1fr 300px;gap:26px">
 <div>
  <div class="kicker" style="--sec:{BLUE}">This week&rsquo;s top eight &#183; unchanged for centuries</div>
  <h2 class="hl" style="font-size:38px;max-width:20ch">The oldest chart still running.</h2>
  <p class="deck" style="max-width:52ch">The Psalms are songs. People forget that. Here is the
  countdown as we would honestly rank it this week at our house.</p>
  <table class="chart">{rows}</table>
 </div>
 <div>
  <figure><img src="img/walkman-half.jpg" alt="" style="width:100%"/>
   <figcaption><span>Side A is 150 tracks long.</span><i>Halftone: BS studio</i></figcaption></figure>
  <div class="panel" style="margin-top:14px"><h4>Liner notes</h4>
   <div class="row"><span>Every one of these was written to be sung out loud, often while
   walking. Reading one on the way somewhere is the original use case.</span></div>
   <div class="row"><span>About half the chart is complaints. They kept those in. We find that
   very encouraging.</span></div>
  </div>
  <div class="godeeper" style="margin-top:14px;--sec:{BLUE}">
   <h5>Start with track one</h5>
   <p>&ldquo;I look up to the mountains &mdash; does my help come from there? My help comes from
   the LORD, who made heaven and earth!&rdquo; &mdash; Psalm 121:1&ndash;2, NLT</p>
  </div>
 </div>
</div>"""+folio("Music","40"),
f""".chart{{width:100%;border-collapse:collapse;margin-top:12px}}
.chart td{{padding:10px 8px;border-bottom:1px solid rgba(25,23,19,.25);font-size:13px;vertical-align:middle}}
.chart td b{{font-family:"Fraunces",serif;font-weight:900;font-size:17px}}
.chart td span{{font-style:italic;opacity:.75;font-size:12px}}
.chart .pos{{font-family:"Fraunces",serif;font-weight:900;font-size:26px;width:44px;color:{BLUE}}}
.chart td:nth-child(3){{font-family:"Bricolage Grotesque",sans-serif;font-size:10px;font-weight:700;
 letter-spacing:.08em;text-transform:uppercase;opacity:.6;width:80px}}
.chart .mv{{width:36px;text-align:center;color:{BLUE};font-size:12px}}""")

# ═══ 44 · PHOTO ESSAY ═══
CAPS=[("room1","A laundromat, mid-cycle. Prayed in more often than most buildings with steeples."),
("room2","A rented room, afterward. Nobody plans to pray in a motel. Then a phone rings."),
("room3","A stairwell, between floors. Held someone for twenty minutes last winter."),
("room4","A kitchen table, early. Where most of the important ones actually happen.")]
figs="".join(f'<figure class="pe"><img src="img/{f}-half.jpg" alt=""/>'
             f'<figcaption><span>{c}</span></figcaption></figure>' for f,c in CAPS)
page("44", slug("Photo essay","rooms that held the moment","four pictures, few words",PLUM)+f"""
<div class="kicker" style="--sec:{PLUM}">Places people prayed without planning to</div>
<h2 class="hl" style="font-size:38px;max-width:24ch">None of these rooms look like it.</h2>
<p class="deck" style="max-width:64ch">Ask people where they were the last time praying got real,
and almost nobody names a building with a spire. They name rooms like these.</p>
<div class="pegrid">{figs}</div>
<div style="border-top:3px solid {PLUM};margin-top:14px;padding-top:12px;display:flex;
 justify-content:space-between;gap:26px;align-items:baseline">
 <p style="font-size:13.5px;line-height:1.5;max-width:52ch;margin:0">&ldquo;I can never escape
 from your Spirit! I can never get away from your presence! If I go up to heaven, you are there;
 if I go down to the grave, you are there.&rdquo; &mdash; Psalm 139:7&ndash;8, NLT</p>
 <p class="sans" style="font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  opacity:.6;margin:0;white-space:nowrap">Photos: public domain &#183; halftones: BS studio</p>
</div>"""+folio("Photo essay","44"),
""".pegrid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:14px}
.pe{margin:0}.pe img{width:100%;display:block}
.pe figcaption span{font-size:12px;line-height:1.45}""")

# ═══ 48 · BACK COVER ═══
page("48", f"""
<div style="height:64px"></div>
<div class="kicker" style="--sec:{RED};text-align:center">You made it to the end of the paper. He made it the whole way with you.</div>
<div style="font-family:'Fraunces',serif;font-weight:900;font-size:118px;line-height:.95;
 letter-spacing:-.03em;text-align:center;margin-top:30px">I am<br/>with you<br/>and will<br/>watch<br/>over you<br/>wherever<br/>you go.</div>
<p class="sans" style="text-align:center;font-size:10.5px;font-weight:800;letter-spacing:.24em;
 text-transform:uppercase;margin-top:26px">Genesis 28:15 &#183; NIV</p>
<div style="position:absolute;left:40px;right:40px;bottom:52px;border-top:2.5px solid {INK};
 padding-top:12px;display:flex;justify-content:space-between;align-items:baseline">
 <div style="font-family:'Fraunces',serif;font-weight:900;font-size:22px">Between Sundays</div>
 <div class="sans" style="font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase">
  Good news. Printed. &#183; Pick it up. Pass it on.</div>
</div>"""+folio("Back page","48"))
print("slate 2 complete")
