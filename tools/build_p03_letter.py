#!/usr/bin/env python3
"""Page 03 — the Publisher's Letter. Adrian's positioning, in his own voice."""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
W,H=941,1346
INK="#191713"; CREAM="#F6F2E8"; RED="#B8412A"
src=open("build_press.py",encoding="utf-8").read()
CHASSIS=src.split('CHASSIS=f"""')[1].split('"""')[0]
CHASSIS=CHASSIS.replace("{W}",str(W)).replace("{H}",str(H)).replace("{INK}",INK)\
 .replace("{CREAM}",CREAM).replace("{RED}",RED).replace("{{","{").replace("}}","}")

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 03 · A Letter Before You Start</title>
<link rel="stylesheet" href="fonts.css"><style>{CHASSIS}
.acts{{border:3px solid {RED};padding:16px 18px;margin-top:16px}}
.acts p{{margin:0;font-family:"Newsreader",Georgia,serif;font-size:16.5px;line-height:1.5}}
.acts i{{display:block;font-style:normal;font-family:"Bricolage Grotesque",sans-serif;
 font-size:9px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;opacity:.6;margin-top:8px}}
.acts b{{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:12.5px;font-weight:800;
 margin-top:10px;color:{RED};text-transform:uppercase;letter-spacing:.03em}}
.rulebox{{background:{INK};color:{CREAM};padding:14px 16px;margin-top:16px}}
.rulebox h5{{margin:0 0 7px;font-family:"Bricolage Grotesque",sans-serif;font-size:10px;
 font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:{RED}}}
.rulebox p{{margin:0;font-size:13px;line-height:1.5}}
.sig{{margin-top:18px;font-family:"Fraunces",serif;font-style:italic;font-size:19px}}
.sig span{{display:block;font-family:"Bricolage Grotesque",sans-serif;font-style:normal;
 font-size:9px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;opacity:.6;margin-top:4px}}
</style></head><body><main class="page">
<div style="--sec:{RED}">
<div class="slugband"><span class="slug">A letter before you start<small>from the people making this</small></span>
 <span>Issue 001 &#183; Page 03</span></div>
<div style="display:grid;grid-template-columns:1fr 300px;gap:30px">
 <div class="body">
  <div class="kicker">The honest version</div>
  <h2 class="hl" style="font-size:42px;max-width:20ch">I never learned to like reading.</h2>
  <p class="deck" style="max-width:58ch">That is a strange thing for the publisher of a newspaper
  to admit on page three. But it is the whole reason this paper exists, so you should have it first.</p>
  <div style="margin-top:14px">
  <p class="first">School taught me how to work the system &mdash; eighth grade straight through
  college. I learned how to pass. I never really learned how to learn, not the scholarly way,
  and I never fell in love with sitting still inside a wall of text.</p>
  <p>But I want to be in the Word. Not around it &mdash; in it. I want to just get in and
  understand. And I figured that if the front door never worked for me, there had to be more
  doors. There are. You are holding one of them: a paper full of games, charts, small ads,
  weather reports and stories that are all, every one of them, ways into the same book.</p>
  <p><span class="rh">So here is who is making this.</span> Not scholars. Not experts. Not your
  teachers. We are the friend on the trip &mdash; we have walked some of this road, so we can
  point at things, but we do not know it all and we are not going to pretend we do. We are
  building this for our own journey as believers, and printing it as we go. A lot of what you
  will read in here is, honestly, just what we are learning this week.</p>
  <p>Two things we do know. We know God. And we want to know him better. We want to make him
  proud, and we want you to know him the way we are getting to.</p>
  <p>Everything else in this paper is negotiable. That part is not.</p>
  </div>
  <div class="sig">&mdash; Adrian &amp; Lacey<span>The ones making this &#183; still learning</span></div>
 </div>
 <div>
  <div class="acts">
   <p>&ldquo;The members of the council were amazed when they saw the boldness of Peter and John,
   for they could see that they were ordinary men with no special training in the Scriptures.
   They also recognized them as men who had been with Jesus.&rdquo;</p>
   <i>Acts 4:13 &#183; NLT</i>
   <b>Ordinary. No special training. Been with Jesus. That is the whole job description,
   and we are applying.</b>
  </div>
  <div class="rulebox">
   <h5>The standing rule of this paper</h5>
   <p>Nothing runs in Between Sundays &mdash; no game, no ad, no chart, no story &mdash; unless
   it is tied to at least one named Bible verse, printed on the page. Check us. If it is
   Bible-sourced, it cannot be wrong. If it is just us talking, it will say so.</p>
  </div>
  <div class="godeeper" style="margin-top:16px">
   <h5>Hold us to it</h5>
   <p>Find a page without its verse, or a verse filed wrong? Write in &mdash; page 28.
   You would be doing exactly what this paper is for.</p>
  </div>
 </div>
</div>
<div class="folio"><span>Between Sundays &#183; A letter</span><span>Acts 4:13</span><span>Page 03</span></div>
</div></main></body></html>"""
open(f"{OUT}/between-sundays-page-03.html","w").write(DOC)
print("wrote press/between-sundays-page-03.html")
