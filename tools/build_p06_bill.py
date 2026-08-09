#!/usr/bin/env python3
"""
Page 06 — THE BILL. Gate to The Reading as a tour poster.
Midnight indigo + electric gold on bone. One night, one venue, attendance one.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"press") if False else os.path.join(BASE,"public","press")
W,H=941,1346
BONE="#F4EEDE"; INDIGO="#1F2A5E"; GOLD="#C08A1E"; INK="#15182E"

TOPICS=[["Stairs","Angels","Dirt","Real estate","Sleep","Stones"],
        ["Family you are avoiding","Descendants","All four directions","Bread","Clothing","Coming home"],
        ["Fear","Oil","Renaming things","Promises","Being watched","Waking up"]]
topics="".join('<ul>'+"".join(f"<li>{t}</li>" for t in col)+'</ul>' for col in TOPICS)

OTHERS=[("MOSES","Roadside, Midian","A bush that would not stop burning.","Exodus 3"),
        ("SAMUEL","Asleep, Shiloh","Heard his name. Thought it was the old man.","1 Samuel 3"),
        ("PETER","Rooftop, Joppa","Hungry. Fell into a trance around noon.","Acts 10"),
        ("PAUL","Road to Damascus","Was on his way to do something else entirely.","Acts 9"),
        ("JOSEPH","Prison, Egypt","Two cellmates. Two dreams. One long wait.","Genesis 40")]
others="".join(f'<div class="oc"><b>{n}</b><i>{w}</i><p>{q}</p><u>{r}</u></div>' for n,w,q,r in OTHERS)

CHECK=[["Far from home","Slept badly","Running from someone","No plan you would admit to"],
       ["Told nobody where you were","Felt nothing at the time","Woke up different","Went back later"]]
checks="".join('<div class="ck">'+"".join(f'<label><i></i>{c}</label>' for c in col)+'</div>' for col in CHECK)

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 06 · The Bill</title><link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{BONE};color:{INDIGO};
 padding:24px 26px}}
.rule{{border-top:3px solid {INDIGO};margin:9px 0}}
.rule.thin{{border-top-width:1.5px}}

/* masthead */
.mast{{display:flex;gap:12px;align-items:stretch;height:206px}}
.namebox{{flex:1;background:{GOLD};padding:12px 16px;display:flex;flex-direction:column;justify-content:center}}
.namebox .buy{{font-size:8.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;
 color:{BONE};line-height:1.3}}
.namebox h1{{margin:4px 0 0;font-size:92px;font-weight:800;line-height:.82;letter-spacing:-.03em;
 color:{BONE};text-transform:uppercase}}
.right{{width:330px;display:flex;flex-direction:column;gap:8px}}
.tourbox{{background:{INDIGO};color:{BONE};padding:9px 12px}}
.tourbox .as{{font-size:8.5px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:{GOLD}}}
.tourbox b{{display:block;font-size:26px;font-weight:800;line-height:.94;text-transform:uppercase;margin:3px 0}}
.tourbox p{{margin:3px 0 0;font-size:9px;line-height:1.35}}
.live{{display:flex;align-items:center;gap:10px;flex:1}}
.live .lv{{font-size:58px;font-weight:800;letter-spacing:-.03em;color:{GOLD};line-height:.85;
 text-transform:uppercase}}
.live .cond{{font-size:14px;font-weight:800;line-height:1.12;text-transform:uppercase}}

/* venues */
.one{{font-size:38px;font-weight:800;text-transform:uppercase;letter-spacing:-.02em;line-height:1}}
.one small{{display:block;font-size:16px;font-weight:700;letter-spacing:0;text-transform:none;
 font-style:italic;margin-top:2px}}
.mid{{display:flex;gap:14px;margin-top:10px}}
.ven{{flex:1}}
.vhead{{display:flex;justify-content:space-between;font-size:9px;font-weight:800;letter-spacing:.14em;
 text-transform:uppercase;border-bottom:2px solid {INDIGO};padding-bottom:3px}}
.arrow{{height:20px;margin:6px 0}}
.ven h3{{margin:0;font-size:34px;font-weight:800;line-height:.9;text-transform:uppercase;color:{GOLD}}}
.ven .sub{{font-size:11.5px;font-weight:800;margin-top:4px}}
.ven .q{{font-size:11px;font-style:italic;margin-top:2px}}
.ven .when{{font-size:12px;font-weight:800;margin-top:6px;display:flex;justify-content:space-between;
 border-top:1.5px solid {INDIGO};padding-top:4px}}
.talent{{width:372px;flex:0 0 372px;border:3px solid {INDIGO};position:relative;background:{INDIGO}}}
.talent img{{display:block;width:100%;height:392px;object-fit:cover}}
.talent .tl{{position:absolute;top:6px;left:8px;background:{INDIGO};padding:2px 5px;font-size:8.5px;font-weight:800;letter-spacing:.12em;
 text-transform:uppercase;color:{GOLD}}}
.talent .tr{{position:absolute;top:6px;right:8px;background:{INDIGO};padding:2px 5px;font-size:8.5px;font-weight:800;letter-spacing:.12em;
 text-transform:uppercase;color:{GOLD}}}
.talent .cap{{position:absolute;top:22px;left:0;right:0;text-align:center}}
.talent .cap span{{background:{INDIGO};color:{BONE};font-size:19px;font-weight:800;
 text-transform:uppercase;padding:4px 14px;letter-spacing:.02em}}
.talent .no{{position:absolute;bottom:32px;left:0;right:0;text-align:center}}
.talent .no span{{background:{GOLD};color:{INDIGO};font-size:12.5px;font-weight:800;
 letter-spacing:.08em;text-transform:uppercase;padding:3px 11px}}
.talent .fc{{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:9.5px;
 color:{BONE};font-style:italic;background:{INDIGO};padding:5px 0}}

.venwrap{{flex:1;display:flex;flex-direction:column}}
.vens{{display:flex;gap:14px}}
.setlist{{margin-top:14px;border-top:2px solid {INDIGO};padding-top:6px}}
.slh{{font-size:10px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:{GOLD}}}
.setlist ol{{list-style:none;margin:6px 0 0;padding:0}}
.setlist li{{display:flex;gap:10px;font-size:11.5px;line-height:1.35;padding:4px 0;
 border-bottom:1px dotted rgba(31,42,94,.4)}}
.setlist li b{{flex:0 0 58px;font-size:9.5px;font-weight:800;letter-spacing:.1em;
 text-transform:uppercase;color:{GOLD};padding-top:1px}}
.blurb{{font-size:11.5px;line-height:1.42;margin:8px 0 0}}
.blurb b{{font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:{GOLD}}}

/* lower deck */
.deck{{display:flex;gap:14px;margin-top:9px}}
.col-t{{flex:1}}
.hd{{font-size:20px;font-weight:800;text-transform:uppercase;letter-spacing:-.01em;line-height:1}}
.hd.gold{{color:{GOLD}}}
.tcols{{display:flex;gap:12px;margin-top:5px}}
.tcols ul{{list-style:none;margin:0;padding:0;flex:1}}
.tcols li{{font-size:10.5px;font-weight:700;line-height:1.5;padding-left:9px;position:relative}}
.tcols li:before{{content:"\\2022";position:absolute;left:0;color:{GOLD}}}
.laugh{{flex:0 0 244px}}
.laugh .big{{font-size:34px;font-weight:800;color:{GOLD};text-transform:uppercase;line-height:.92}}
.laugh p{{margin:5px 0 0;font-size:10px;line-height:1.4}}
.checkbox{{border:3px solid {INDIGO};margin-top:7px;padding:8px 10px}}
.checkbox h4{{margin:0 0 5px;font-size:12.5px;font-weight:800;text-transform:uppercase;
 letter-spacing:.06em;color:{GOLD}}}
.cks{{display:flex;gap:10px}}
.ck{{flex:1}}
.ck label{{display:flex;gap:5px;align-items:flex-start;font-size:9.5px;font-weight:700;
 line-height:1.3;margin-bottom:4px}}
.ck i{{flex:0 0 9px;width:9px;height:9px;border:1.6px solid {INDIGO};margin-top:1px}}
.hence{{margin-top:5px;border-top:1.5px solid {INDIGO};padding-top:4px;font-size:11px;font-weight:800;
 text-transform:uppercase;color:{GOLD}}}

.others{{display:flex;gap:8px;margin-top:8px}}
.oc{{flex:1;border:2px solid {INDIGO};padding:6px 7px}}
.oc b{{display:block;font-size:12px;font-weight:800;color:{GOLD}}}
.oc i{{display:block;font-style:normal;font-size:8px;font-weight:700;letter-spacing:.08em;
 text-transform:uppercase;opacity:.75;margin-bottom:3px}}
.oc p{{margin:0;font-size:9.5px;line-height:1.32}}
.oc u{{display:block;text-decoration:none;font-size:8.5px;font-weight:800;letter-spacing:.06em;
 margin-top:3px;color:{GOLD}}}

.footrow{{display:flex;gap:12px;margin-top:8px;align-items:stretch}}
.ed{{flex:0 0 210px;font-size:9.5px;line-height:1.45}}
.ed b{{display:block;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em}}
.sign{{flex:1;border:2px dashed {INDIGO};padding:7px 10px}}
.sign b{{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:{GOLD}}}
.sign p{{margin:2px 0 0;font-size:9.5px;line-height:1.35}}
.sign .line{{border-bottom:1.5px solid {INDIGO};height:22px;margin-top:5px}}
.gate{{flex:0 0 232px;background:{INDIGO};color:{BONE};padding:8px 11px;text-align:center;
 display:flex;flex-direction:column;justify-content:center}}
.gate b{{font-size:15px;font-weight:800;line-height:1.06;text-transform:uppercase}}
.gate span{{font-size:9px;margin-top:4px;color:{GOLD};font-weight:800;letter-spacing:.14em;
 text-transform:uppercase}}
.folio{{position:absolute;left:26px;right:26px;bottom:8px;display:flex;justify-content:space-between;
 font-size:8px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;opacity:.7}}
</style></head><body><main class="page">

<div class="mast">
 <div class="namebox">
  <div class="buy">No tickets &#183; no doors<br/>no warning &#183; no cover</div>
  <h1>Jacob<br/>at Bethel</h1>
 </div>
 <div class="right">
  <div class="tourbox"><div class="as">As part of the</div>
   <b>Running-<br/>From-My-<br/>Brother Tour</b>
   <p>Beersheba to Haran &#183; approx. 500 miles &#183; on foot &#183; unaccompanied</p></div>
  <div class="live"><span class="lv">Live</span>
   <span class="cond">On the ground<br/>Asleep on a rock<br/>Attendance: one</span></div>
 </div>
</div>
<div class="rule"></div>

<div class="one">One night only<small>(in a place that did not have a name yet)</small></div>
<div class="mid">
 <div class="venwrap"><div class="vens">
 <div class="ven">
  <div class="vhead"><span>P-01</span><span>Before dark</span></div>
  <svg class="arrow" viewBox="0 0 120 20"><path d="M 0 6 L 88 6 L 88 0 L 120 10 L 88 20 L 88 14 L 0 14 Z" fill="{GOLD}"/></svg>
  <h3>Luz</h3>
  <div class="sub">The name on the map.</div>
  <div class="q">&ldquo;A town he was walking past.&rdquo;</div>
  <div class="when"><span>Sunset</span><span>Doors: none</span></div>
 </div>
 <div class="ven">
  <div class="vhead"><span>P-02</span><span>By morning</span></div>
  <svg class="arrow" viewBox="0 0 120 20"><path d="M 0 6 L 88 6 L 88 0 L 120 10 L 88 20 L 88 14 L 0 14 Z" fill="{GOLD}"/></svg>
  <h3>Bethel</h3>
  <div class="sub">The name by morning.</div>
  <div class="q">&ldquo;House of God.&rdquo;</div>
  <div class="when"><span>Sunrise</span><span>Same coordinates</span></div>
 </div>
 </div>
 <div class="setlist">
  <div class="slh">Running order &#183; one set, no interval</div>
  <ol>
   <li><b>Sunset</b>He stops walking. Not because he arrived &mdash; because the light went.</li>
   <li><b>&nbsp;</b>Takes a stone from the ground. Uses it as a pillow.</li>
   <li><b>Night</b>A stairway, earth to sky. Traffic moving in both directions.</li>
   <li><b>&nbsp;</b>A voice, unprompted, unearned: <i>&ldquo;I am with you.&rdquo;</i></li>
   <li><b>Dawn</b>He wakes up afraid. Says the line this whole paper is named after.</li>
   <li><b>&nbsp;</b>Stands the pillow on its end. Pours oil on it. Renames the town.</li>
  </ol>
 </div>
 </div>
 <div class="talent">
  <span class="tl">No. &ldquo;GEN-28&rdquo;</span><span class="tr">Luz, unincorporated</span>
  <div class="cap"><span>&ldquo;The Talent&rdquo;</span></div>
  <img src="img/stone-bill.jpg" alt=""/>
  <div class="no"><span>No known likeness exists</span></div>
  <div class="fc">The only surviving prop, pictured.</div>
 </div>
</div>

<p class="blurb"><b>Leave the light on, everybody:</b> a man left home in a hurry because his brother
wanted him dead, walked until the sun quit on him, and stopped in open country because he had run out
of daylight, not because he had arrived. He used a rock for a pillow. Nobody was told. Nobody sold a
ticket. What happened next got the place renamed and is printed in full, starting on the very next
page. <b>Doors were never opened. Anything can happen.</b></p>
<div class="rule thin"></div>

<div class="deck">
 <div class="col-t">
  <div class="hd">Possible range of topics:</div>
  <div class="tcols">{topics}</div>
 </div>
 <div class="laugh">
  <div class="big">Wake up.</div>
  <p>Come as you are, which in his case was filthy and afraid. Sleep badly. Miss the whole thing
  at the time. Work it out in the morning. <b>Could be the best night of your life.</b></p>
 </div>
</div>

<div class="checkbox">
 <h4>For internal use &#183; Bethel checklist: check all that apply</h4>
 <div class="cks">{checks}</div>
 <div class="hence">Hence, you &#8230; may already be in the place.</div>
</div>

<div class="others">{others}</div>

<div class="footrow">
 <div class="ed"><b>Very limited edition</b>
  Edition of one. Yours.<br/>Type: Between Sundays<br/>Place of residence: your wall,
  a fridge, or the seat behind you.</div>
 <div class="sign"><b>Were you there?</b>
  <p>Most people find out later. If you have had a night like this one, put your name on it.</p>
  <div class="line"></div></div>
 <div class="gate"><b>The Reading<br/>starts overleaf</b>
  <span>Pages 07&ndash;14 &#183; no ads</span></div>
</div>
<div class="folio"><span>Between Sundays &#183; Issue 001</span>
 <span>Genesis 28:19 &mdash; &ldquo;it was previously called Luz&rdquo; &#183; NLT</span><span>Page 06</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-06.html","w").write(DOC)
print("wrote press/between-sundays-page-06.html")
