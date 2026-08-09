#!/usr/bin/env python3
"""
THE PRESS CHASSIS — one shared constitution, four proof pages.
  press/01  Front page       (SundayReview model: illustration + real columns + jump)
  press/07  The Reading 01   (Gen 28:10-15 + passage data panel + GO DEEPER)
  press/19  Sports           (halftoned hero, columns, agate box score)
  press/42  The small ads    (8 tiny gospel ads + mail-in coupon)
Every page: nameplate/slug band + folio. Newsreader body. Captions and credits
on every image. All scripture WEB, fetched.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
W,H=941,1346
INK="#191713"; CREAM="#F6F2E8"; RED="#B8412A"; INDIGO="#2A3A8C"; GOLD="#C79A3A"; GREEN="#185C3C"; BLUE="#24509E"

CHASSIS=f"""
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Newsreader",Georgia,serif;color:{INK}}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CREAM};
 padding:0 40px}}
.sans{{font-family:"Bricolage Grotesque","Avenir Next",sans-serif}}
/* nameplate + folio */
.nameplate{{text-align:center;padding:26px 0 10px}}
.nameplate h1{{margin:0;font-family:"Fraunces",Georgia,serif;font-weight:900;font-size:64px;
 letter-spacing:-.015em;line-height:1}}
.dateline{{display:flex;justify-content:space-between;border-top:2.5px solid {INK};
 border-bottom:1px solid {INK};padding:5px 0;margin-top:10px;font-family:"Bricolage Grotesque",sans-serif;
 font-size:9.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.slugband{{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:3px solid var(--sec,{INK});padding:22px 0 8px;margin-bottom:14px}}
.slug{{font-family:"Bricolage Grotesque",sans-serif;font-size:26px;font-weight:800;
 letter-spacing:.02em;text-transform:uppercase;color:var(--sec,{INK})}}
.slug small{{font-family:"Fraunces",serif;font-weight:600;font-size:13px;letter-spacing:.06em;
 color:{INK};margin-left:12px}}
.slugband span{{font-family:"Bricolage Grotesque",sans-serif;font-size:9.5px;font-weight:700;
 letter-spacing:.16em;text-transform:uppercase;opacity:.6}}
.folio{{position:absolute;left:40px;right:40px;bottom:20px;display:flex;justify-content:space-between;
 border-top:1px solid {INK};padding-top:7px;font-family:"Bricolage Grotesque",sans-serif;
 font-size:9px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;opacity:.65}}
/* editorial parts */
.kicker{{font-family:"Bricolage Grotesque",sans-serif;font-size:10.5px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;color:var(--sec,{RED})}}
.hl{{font-family:"Fraunces",Georgia,serif;font-weight:900;letter-spacing:-.015em;line-height:1.02;margin:6px 0 0}}
.deck{{font-size:17px;line-height:1.4;font-style:italic;margin:10px 0 0;color:#333026}}
.byline{{font-family:"Bricolage Grotesque",sans-serif;font-size:9.5px;font-weight:700;
 letter-spacing:.14em;text-transform:uppercase;margin:10px 0 0;opacity:.7}}
.cols2{{column-count:2;column-gap:26px;column-rule:1px solid rgba(25,23,19,.25)}}
.cols3{{column-count:3;column-gap:22px;column-rule:1px solid rgba(25,23,19,.25)}}
.body p{{margin:0 0 9px;font-size:13.5px;line-height:1.42;text-align:justify}}
.body p.first:first-letter{{font-family:"Fraunces",serif;font-weight:900;font-size:46px;
 line-height:.82;float:left;padding:5px 7px 0 0}}
.body .rh{{font-weight:700;font-style:normal}}
.jump{{font-family:"Bricolage Grotesque",sans-serif;font-size:9.5px;font-weight:800;
 letter-spacing:.1em;text-transform:uppercase}}
figure{{margin:0}}
figcaption{{font-family:"Bricolage Grotesque",sans-serif;font-size:9.5px;line-height:1.4;
 padding-top:6px;display:flex;justify-content:space-between;gap:14px}}
figcaption i{{font-style:normal;opacity:.55;white-space:nowrap}}
/* boxes */
.panel{{border:2px solid {INK};padding:0 0 6px}}
.panel h4{{margin:0 0 8px;background:{INK};color:{CREAM};font-family:"Bricolage Grotesque",sans-serif;
 font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;padding:7px 12px}}
.panel .row{{display:flex;justify-content:space-between;gap:12px;padding:5px 12px;
 border-bottom:1px dotted rgba(25,23,19,.35);font-size:12px}}
.panel .row:last-child{{border-bottom:0}}
.panel .row b{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;opacity:.6;padding-top:2px;white-space:nowrap}}
.panel .row span{{text-align:right}}
.godeeper{{border-top:3px solid var(--sec,{INK});padding-top:8px}}
.godeeper h5{{margin:0 0 6px;font-family:"Bricolage Grotesque",sans-serif;font-size:10px;
 font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--sec,{INK})}}
.godeeper p{{margin:0 0 5px;font-size:12.5px;line-height:1.4}}
.agate{{width:100%;border-collapse:collapse;font-family:"Bricolage Grotesque",sans-serif}}
.agate th{{font-size:8.5px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 text-align:left;border-bottom:2px solid {INK};padding:3px 4px}}
.agate td{{font-size:11.5px;padding:5px 4px;border-bottom:1px solid rgba(25,23,19,.2)}}
.agate td:last-child,.agate th:last-child{{text-align:right}}
.coupon{{border:2px dashed {INK};padding:11px 13px}}
"""

FRONT_CSS=f'''
.briefs{{position:absolute;left:40px;right:40px;bottom:52px;display:grid;
 grid-template-columns:1fr 1fr 1fr;gap:20px;border-top:2.5px solid {INK};padding-top:10px}}
.briefs b{{display:block;font-size:9.5px;font-weight:800;letter-spacing:.18em;
 text-transform:uppercase;color:{RED};margin-bottom:3px}}
.briefs span{{font-family:"Newsreader",serif;font-size:12.5px;line-height:1.35}}
'''
def pagewrap(body,extra=""):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays</title><link rel="stylesheet" href="fonts.css">
<style>{CHASSIS}{extra}</style></head><body><main class="page">{body}</main></body></html>"""

# ═══ 01 · FRONT PAGE ═════════════════════════════════════════════════════════
front=f"""
<div class="nameplate">
  <div style="display:flex;justify-content:space-between;align-items:flex-end">
    <div class="sans" style="font-size:9.5px;font-weight:700;letter-spacing:.1em;line-height:1.5;
      text-transform:uppercase;text-align:left;width:170px">Weather: rain for a while,<br/>then you&rsquo;ll see &#183; Page 20</div>
    <h1>Between Sundays</h1>
    <div class="sans" style="font-size:9.5px;font-weight:700;letter-spacing:.1em;line-height:1.5;
      text-transform:uppercase;text-align:right;width:170px">Good news.<br/>Printed.</div>
  </div>
  <div class="dateline"><span>Sunday edition</span><span>Issue 001 &#183; &ldquo;I am with you&rdquo;</span><span>Pass it on</span></div>
</div>

<div class="kicker" style="margin-top:16px">The geography of nowhere &#183; a special issue</div>
<h2 class="hl" style="font-size:47px;max-width:24ch">The middle of nowhere just got a new name.</h2>
<p class="deck" style="max-width:70ch">A man on the run spent one night on open ground with a stone
for a pillow. What he said when he woke up renamed the place &mdash; and started this newspaper.</p>

<figure style="margin-top:14px">
  <img src="img/front-hero.png" alt="" style="width:100%;height:432px;object-fit:cover;object-position:center 64%"/>
  <figcaption><span>Everybody on this hill came from somewhere else. Nobody is having the day
  you think they are.</span><i>Illustration: Between Sundays studio</i></figcaption>
</figure>

<div style="display:grid;grid-template-columns:1fr 292px;gap:26px;margin-top:16px">
  <div class="body cols2">
    <p class="first">A man left Beersheba in a hurry. He was not on vacation. His brother wanted
    him dead, and the fastest road out of town was the one he took.</p>
    <p>Around sunset he reached a stretch of open ground between towns. The Bible does not
    give it a name. It just says <i>a certain place</i> &mdash; the kind of spot nobody stops in
    unless the sun quits on them first. He found a stone, put it under his head, and slept
    in the dirt.</p>
    <p><span class="rh">What happened next</span> is the reason this paper exists. He dreamed of
    a stairway set on the earth with its top reaching to heaven, and heard a promise that
    followed him for the rest of his life: <i>I am with you, and will keep you, wherever you go.</i></p>
    <p>He woke up afraid and said a strange thing for a man alone in a field: &ldquo;Surely the Lord
    is in this place, and I was not aware of it.&rdquo; Then he stood his pillow up on its end,
    poured oil on it, and gave the empty ground a new name: the house of God.</p>
    <p>The place did not change overnight. His information did. &nbsp;<span class="jump">Continued on Page 14 &#8594;</span></p>
  </div>
  <div>
    <div class="panel">
      <h4>Inside today</h4>
      <div class="row"><span>The Reading &mdash; Genesis 28</span><span class="sans" style="font-weight:800">07</span></div>
      <div class="row"><span>Words &amp; Meaning &mdash; looked up</span><span class="sans" style="font-weight:800">16</span></div>
      <div class="row"><span>Sports &mdash; nobody saw this one</span><span class="sans" style="font-weight:800">19</span></div>
      <div class="row"><span>Weather for the middle</span><span class="sans" style="font-weight:800">20</span></div>
      <div class="row"><span>The Spine &mdash; tear it out</span><span class="sans" style="font-weight:800">23</span></div>
      <div class="row"><span>Games &mdash; connect the dots</span><span class="sans" style="font-weight:800">45</span></div>
    </div>
    <div class="godeeper" style="margin-top:14px;--sec:{RED}">
      <h5>How to read this paper</h5>
      <p>Read it. Skim it. Tear out the middle. Leave it somewhere on purpose.
      Play the games. Come back next Sunday.</p>
    </div>
  </div>
</div>
<div class="briefs sans">
  <div><b>Sports</b><span>The result nobody printed: every unwatched kilometre counted. Page 19</span></div>
  <div><b>Words</b><span>&ldquo;Ladder&rdquo; appears once in the whole Hebrew Bible. Once. Page 16</span></div>
  <div><b>Games</b><span>What&rsquo;s under the water? Connect dots 1&ndash;79 and see. Page 46</span></div>
</div>
<div class="folio"><span>Between Sundays &#183; Sunday edition</span><span>betweensundays.com</span><span>Page 01</span></div>
"""

# ═══ 07 · THE READING 01 ═════════════════════════════════════════════════════
verses=[(10,"Jacob went out from Beersheba, and went toward Haran."),
(11,"He came to a certain place, and stayed there all night, because the sun had set. He took one of the stones of the place, and put it under his head, and lay down in that place to sleep."),
(12,"He dreamed. Behold, a stairway set upon the earth, and its top reached to heaven. Behold, the angels of God ascending and descending on it."),
(13,"Behold, Yahweh stood above it, and said, “I am Yahweh, the God of Abraham your father, and the God of Isaac. The land whereon you lie, to you will I give it, and to your offspring."),
(14,"Your offspring will be as the dust of the earth, and you will spread abroad to the west, and to the east, and to the north, and to the south. In you and in your offspring will all the families of the earth be blessed."),
(15,"Behold, I am with you, and will keep you, wherever you go, and will bring you again into this land. For I will not leave you, until I have done that which I have spoken of to you.”")]
vhtml="".join(f'<p class="vs"><sup>{n}</sup>{t}</p>' for n,t in verses)
reading=f"""
<div style="--sec:{INDIGO}">
<div class="slugband"><span class="slug">The Reading<small>Genesis 28 : 10&ndash;15</small></span>
 <span>No ads &#183; no commentary &#183; part one of two</span></div>
<div style="display:grid;grid-template-columns:1fr 288px;gap:30px">
  <div>
    <div class="kicker">Night one</div>
    <h2 class="hl" style="font-size:46px;margin-bottom:14px">He lay down in that<br/>place to sleep.</h2>
    {vhtml}
    <p class="jump" style="margin-top:14px;color:{INDIGO}">The Reading continues on Page 08 &#8594;</p>
    <div style="border-top:3px solid {INDIGO};margin-top:16px;padding-top:12px">
      <div class="kicker" style="color:{INDIGO}">Verse 15 &#183; the five words this whole issue hangs on</div>
      <div style="font-family:'Fraunces',serif;font-weight:900;font-size:44px;line-height:1.0;
        letter-spacing:-.02em;margin-top:6px;color:{INDIGO}">&ldquo;I am with you.&rdquo;</div>
      <p style="margin:9px 0 0;font-size:12.5px;line-height:1.42;max-width:46ch">Said to a man asleep
      in the dirt, before he had done one thing right. The promise came first. It usually does.</p>
    </div>
  </div>
  <div>
    <div class="panel">
      <h4>The passage</h4>
      <div class="row"><b>Book</b><span>Genesis &mdash; first book of the Bible</span></div>
      <div class="row"><b>Verses</b><span>Chapter 28, verses 10&ndash;15</span></div>
      <div class="row"><b>Time to read</b><span>About two minutes</span></div>
      <div class="row"><b>Where you are</b><span>Night one of a twenty-year trip</span></div>
      <div class="row"><b>Cast of note</b><span>Jacob, on the run &#183; Yahweh, who speaks first</span></div>
      <div class="row"><b>Words to watch</b><span>&ldquo;place&rdquo; &mdash; six times. See Page 16.</span></div>
      <div class="row"><b>Translation</b><span>World English Bible</span></div>
    </div>
    <figure style="margin-top:14px">
      <img src="img/stone-half.jpg" alt="" style="width:100%"/>
      <figcaption><span>One of the stones of the place.</span><i>Photo: public domain</i></figcaption>
    </figure>
    <div class="godeeper" style="margin-top:14px">
      <h5>Go deeper</h5>
      <p><b>Genesis 32</b> &mdash; twenty years later, the wrestling match.</p>
      <p><b>Psalm 121</b> &mdash; a psalm for people on a road.</p>
      <p><b>John 1:51</b> &mdash; Jesus quotes this exact dream.</p>
      <p style="margin-top:8px"><i>One question: alone out there, what would you have asked for?</i></p>
    </div>
  </div>
</div>
<div class="folio"><span>Between Sundays &#183; The Reading</span><span>Issue 001</span><span>Page 07</span></div>
</div>
"""
reading_css=f""".vs{{margin:0 0 13px;font-size:23px;line-height:1.5}}
.vs sup{{font-family:"Bricolage Grotesque",sans-serif;font-size:10px;font-weight:800;color:{INDIGO};
 margin-right:6px}}"""

# ═══ 19 · SPORTS ═════════════════════════════════════════════════════════════
LOG=[("Monday","6.2 km","0","Counted"),("Tuesday","Rest","0","Counted"),
("Wednesday","8.0 km","0","Counted"),("Thursday","6.2 km","1 dog","Counted"),
("Friday","Rest","0","Counted"),("Saturday","14.5 km","0","Counted"),("Sunday","Walked","0","Counted")]
rows="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td style='color:{GREEN};font-weight:800'>{d}</td></tr>"
             for a,b,c,d in LOG)
sports=f"""
<div style="--sec:{GREEN}">
<div class="slugband"><span class="slug">Sports<small>Away team advantage</small></span>
 <span>Between Sundays &#183; Issue 001</span></div>
<div class="kicker">The season nobody watched</div>
<h2 class="hl" style="font-size:42px;max-width:22ch">Nobody saw this one. It counted anyway.</h2>
<p class="deck" style="max-width:66ch">No crowd, no clock, no result in any paper but this one.
One ordinary training week, reported like the event it actually was.</p>
<figure style="margin-top:12px">
  <img src="img/runner-half.jpg" alt="" style="width:100%"/>
  <figcaption><span>Tuesday, 5:50 a.m. Attendance: zero. The hill did not care either way.</span>
  <i>Halftone: Between Sundays studio</i></figcaption>
</figure>
<div style="display:grid;grid-template-columns:1fr 288px;gap:26px;margin-top:14px">
  <div class="body cols2">
    <p class="first">The biggest game of the week had no tickets. It started before sunrise on a
    hill with no name, and the only one keeping score was the one running it.</p>
    <p>That is how most of a season actually goes. The part people see &mdash; the race, the day
    it all works &mdash; lasts an hour. The part that decides it happens on dark mornings, in
    empty places, with nobody watching and nothing to prove it happened.</p>
    <p><span class="rh">The Bible is blunt about this.</span> It says the Father sees in secret.
    Not <i>might</i> see. Sees. Which means the empty hill on Tuesday had an attendance of one
    more than anybody thought, and the week counted &mdash; every unwatched kilometre of it.</p>
    <p>Whatever your version of the dark morning is, it is on the board. &nbsp;
    <span class="jump" style="color:{GREEN}">More sport next issue &#8594;</span></p>
  </div>
  <div>
    <table class="agate">
      <tr><th>This week</th><th>Distance</th><th>Witnesses</th><th>Counted</th></tr>
      {rows}
    </table>
    <div class="godeeper" style="margin-top:14px">
      <h5>Go deeper</h5>
      <p><b>Matthew 6:6</b> &mdash; &ldquo;seen in secret.&rdquo;</p>
      <p><b>Galatians 6:9</b> &mdash; on not quitting before harvest.</p>
      <p><b>1 Corinthians 9:24&ndash;27</b> &mdash; training, by a man who ran.</p>
    </div>
  </div>
</div>
<div style="border:2px solid {INK};margin-top:16px">
  <h4 class="sans" style="margin:0;background:{GREEN};color:{CREAM};font-size:10px;font-weight:800;
   letter-spacing:.2em;text-transform:uppercase;padding:7px 12px">Fixtures &#183; all week &#183; no tickets required</h4>
  <div class="sans" style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;padding:10px 12px;font-size:11px;line-height:1.5">
    <div><b>MON 5:50a</b><br/>The hill. Alone.</div>
    <div><b>WED 6:00a</b><br/>The bridge loop.</div>
    <div><b>SAT 7:00a</b><br/>The long one.</div>
    <div><b>SUN &mdash;</b><br/>A walk. Bring somebody.</div>
  </div>
</div>
<div class="folio"><span>Between Sundays &#183; Sports</span><span>Issue 001</span><span>Page 19</span></div>
</div>
"""

# ═══ 42 · THE SMALL ADS ══════════════════════════════════════════════════════
def ad(style,inner): return f'<div class="adcell" style="{style}">{inner}</div>'
ads="".join([
ad(f"border:3px double {RED}",f"""<div class="ah" style="color:{RED}">Actual size &#8595;</div>
 <div style="text-align:center;font-size:40px;line-height:.6;padding:2px 0 8px">&#183;</div>
 <b class="at">Mustard seed</b>
 <p>Faith this size moves mountains. No purchase necessary. Matthew 17:20.</p>"""),
ad(f"border:2.5px solid {BLUE};background:#E9EDF6",f"""<div class="ah" style="color:{BLUE}">Free &#183; no-risk home trial</div>
 <b class="at">Grace</b>
 <p>Send no money. You could not afford it anyway &mdash; that is the whole point.
 Inspect and enjoy in your own home. You risk nothing. Romans 6:23.</p>"""),
ad(f"border:2.5px solid {INK}",f"""<div class="ah">Complete kit &#183; one size fits all</div>
 <b class="at">The full armor</b>
 <p>Belt, breastplate, shoes, shield, helmet, sword. Free instructions with every
 order. Ephesians 6:13&ndash;17.</p>"""),
ad(f"border:3px solid {RED};background:#F6E7E2",f"""<div class="ah" style="color:{RED}">Unlimited supply</div>
 <b class="at">Living water</b>
 <p>&ldquo;Whoever drinks of the water that I will give him will never thirst
 again.&rdquo; John 4:14. While supplies last (they will).</p>"""),
ad(f"border:2.5px solid {BLUE}",f"""<div class="ah" style="color:{BLUE}">Learn at home</div>
 <b class="at">Be still</b>
 <p>The fastest way to slow down. &ldquo;Be still, and know that I am God.&rdquo;
 Psalm 46:10. Results in ten quiet minutes.</p>"""),
ad(f"border:2.5px solid {INK};background:#F0EBDD",f"""<div class="ah">Lost &amp; found</div>
 <b class="at">One sheep</b>
 <p>Answers to your name. Owner already out looking. If found, you were never
 actually lost. Luke 15:4&ndash;6.</p>"""),
ad(f"border:3px double {BLUE}",f"""<div class="ah" style="color:{BLUE}">Help wanted</div>
 <b class="at">Harvest workers</b>
 <p>Large harvest, short staff. No experience required &mdash; training on the job.
 Apply anywhere. Luke 10:2.</p>"""),
ad(f"border:2.5px solid {RED}",f"""<div class="ah" style="color:{RED}">One only &#183; everything must go</div>
 <b class="at">The pearl</b>
 <p>Man finds one pearl, sells all he has, buys it. Says it was underpriced.
 Matthew 13:45&ndash;46.</p>"""),
ad(f"border:3px solid {INK};background:#EDE9DB",f"""<div class="ah">Daily &#183; ask each morning</div>
 <b class="at">Bread</b>
 <p>Fresh every day. Yesterday&rsquo;s does not keep &mdash; that is on purpose.
 Matthew 6:11, Exodus 16:19&ndash;21.</p>"""),
ad(f"border:2.5px solid {BLUE};background:#E9EDF6",f"""<div class="ah" style="color:{BLUE}">Trade-in program</div>
 <b class="at">Rest</b>
 <p>Bring your heavy load. Take his light one. Uneven trade, in your favor,
 no questions. Matthew 11:28&ndash;30.</p>"""),
ad(f"border:3px double {RED}",f"""<div class="ah" style="color:{RED}">Factory replacement</div>
 <b class="at">New heart</b>
 <p>The old stone one swapped out entirely. Not a repair &mdash; a replacement.
 Ezekiel 36:26.</p>"""),
ad(f"border:2.5px solid {INK}",f"""<div class="ah">Guaranteed &#183; add zero inches</div>
 <b class="at">Worry</b>
 <p>Tested for centuries. Has never once made anyone taller, or a day longer.
 Discontinue freely. Matthew 6:27.</p>"""),
])
smallads=f"""
<div style="--sec:{RED}">
<div class="slugband"><span class="slug">The Back Pages<small>Special offers &#183; every one of them free</small></span>
 <span>Advertisement section</span></div>
<div class="adgrid">{ads}</div>
<div class="coupon" style="margin-top:18px">
  <div style="display:flex;gap:20px;align-items:flex-start">
    <div style="flex:1">
      <div class="ah" style="color:{RED};font-size:11px">Mail-in order form &#183; clip this</div>
      <p style="margin:6px 0 10px;font-size:12.5px">RUSH me everything on this page.
      I enclose nothing, because none of it is for sale. I understand supplies never run out.</p>
      <div class="fline"><span>Name</span><i></i></div>
      <div class="fline"><span>Where you are right now</span><i></i></div>
      <div class="fline"><span>What you actually need</span><i></i></div>
    </div>
    <div style="width:170px;border:2px solid {INK};padding:10px;text-align:center">
      <div class="ah">You pay</div>
      <div style="font-family:'Fraunces',serif;font-weight:900;font-size:40px;line-height:1">$0</div>
      <div style="font-size:10.5px;margin-top:4px">paid in full,<br/>some time ago</div>
    </div>
  </div>
</div>
<div class="folio"><span>Between Sundays &#183; The Back Pages</span><span>Issue 001</span><span>Page 42</span></div>
</div>
"""
ads_css=f"""
.adgrid{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.adcell{{padding:16px 18px;background:{CREAM}}}
.ah{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.18em;text-transform:uppercase}}
.at{{display:block;font-family:"Fraunces",serif;font-weight:900;font-size:27px;line-height:1;
 margin:5px 0 6px}}
.adcell p{{margin:0;font-size:13.5px;line-height:1.45}}
.fline{{display:flex;gap:10px;align-items:baseline;margin-top:12px}}
.fline span{{font-family:"Bricolage Grotesque",sans-serif;font-size:9px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;opacity:.6;white-space:nowrap}}
.fline i{{flex:1;border-bottom:1.5px solid {INK}}}
"""

open(f"{OUT}/between-sundays-page-01.html","w").write(pagewrap(front,FRONT_CSS))
open(f"{OUT}/between-sundays-page-07.html","w").write(pagewrap(reading,reading_css))
open(f"{OUT}/between-sundays-page-19.html","w").write(pagewrap(sports))
open(f"{OUT}/between-sundays-page-42.html","w").write(pagewrap(smallads,ads_css))
print("press pages: 01 front · 07 reading · 19 sports · 42 small ads")
