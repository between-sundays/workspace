#!/usr/bin/env python3
"""
Page 18 — THE OFFER / THE COUNTER-OFFER.  Modern Parallel.
TWO half-portrait modules (470 x 1346 each), side by side.
LEFT  : Jacob's vow (Gen 28:20-22) as a betting slip, filled in over four hours.
RIGHT : God's promise (Gen 28:13-15) issued four hours earlier, no conditions.
All geometry MODULE-LOCAL.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H,HW = 941,1346,470
PLAN="#E8A317"; CRM="#F4EFE3"; DARK="#0E120F"; PAPER="#EFE6D2"

# each row: (printed line, the verbatim clause he writes in)
ROWS=[("bread to eat",              "bread to eat"),
      ("clothing to put on",        "clothing to put on"),
      ("this way that I go",        "kept"),
      ("my father's house",         "in peace")]

STATES=[("23:40","0","Twelve empty boxes. He has not written anything yet."),
        ("01:15","2","He starts with food and clothes. He is not asking for much."),
        ("02:52","4","Safe passage. Then he sits with it for ninety minutes."),
        ("04:06","4","He fills in what he is putting up, and signs it.")]

def slip(ts, filled, final):
    rows=""
    for i,(printed, hand) in enumerate(ROWS):
        on = i < int(filled)
        rows+=(f'<div class="row{" on" if on else ""}">'
               f'<span class="bx">{"&#10005;" if on else ""}</span>'
               f'<span class="pr">{printed}</span>'
               f'<span class="hw">{hand if on else ""}</span></div>')
    ret=('<span class="hw big">a tenth</span>' if final else '<span class="blank"></span>')
    band=('<div class="band"><span class="stamp">Conditional</span>'
          '<span class="hw sg">Jacob</span></div>' if final else '')
    return f'''<div class="slip">
  <div class="shd"><b>Terms</b><i>Slip No. 28</i></div>
  {rows}
  <div class="ret"><span class="pr">offered in return</span>{ret}</div>
  {band}
</div>'''

blocks=""
for (ts, filled, cap), _ in zip(STATES, STATES):
    blocks+=f'''<div class="st">
  <div class="tsr"><b>{ts}</b><span>{cap}</span></div>
  {slip(ts, filled, ts=="04:06")}
</div>'''

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 18 · The Offer &amp; The Counter-Offer</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{DARK};color:{CRM}}}
.mod{{position:absolute;top:0;width:{HW}px;height:{H}px;overflow:hidden}}
.mod.l{{left:0}} .mod.r{{left:{HW}px;border-left:1px solid rgba(244,239,227,.14)}}
.modtag{{position:absolute;top:12px;left:34px;font-size:7.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.28}}
.strip{{position:absolute;left:34px;right:34px;top:42px;display:flex;justify-content:space-between;
 font-size:8.5px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;
 padding-bottom:7px;border-bottom:1px solid rgba(244,239,227,.24)}}
.foot{{position:absolute;left:34px;right:34px;bottom:32px;display:flex;justify-content:space-between;
 border-top:1px solid rgba(244,239,227,.24);padding-top:7px;font-size:7.5px;font-weight:800;
 letter-spacing:.18em;text-transform:uppercase;opacity:.45}}
h1,h2{{margin:0;font-weight:800;letter-spacing:-.03em;line-height:.88;text-transform:uppercase}}
em{{font-style:normal;color:{PLAN}}}

/* ── LEFT · the counter-offer ── */
.l h1{{position:absolute;left:34px;top:76px;font-size:44px}}
.l .deck{{position:absolute;left:34px;right:34px;top:208px;margin:0;
 font-family:"Newsreader",Georgia,serif;font-size:12.5px;line-height:1.5;opacity:.6}}
.hand{{position:absolute;left:34px;top:282px;width:402px;height:178px;object-fit:cover}}
.stack{{position:absolute;left:34px;top:480px;width:402px}}
.st{{margin-bottom:9px}}
.tsr{{display:flex;gap:9px;align-items:baseline;padding-bottom:5px}}
.tsr b{{font-size:9px;font-weight:800;letter-spacing:.16em;color:{PLAN}}}
.close{{position:absolute;left:34px;right:34px;bottom:74px;margin:0;
 font-family:"Newsreader",serif;font-size:12.5px;line-height:1.5;opacity:.62;
 border-top:1px solid rgba(244,239,227,.24);padding-top:12px}}
.tsr span{{flex:1;font-family:"Newsreader",serif;font-size:9.5px;line-height:1.25;opacity:.55}}

.slip{{position:relative;background:{PAPER};color:#1B1913;padding:9px 12px 10px;
 box-shadow:0 5px 22px rgba(0,0,0,.55)}}
.shd{{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:1.5px solid #1B1913;padding-bottom:4px;margin-bottom:5px}}
.shd b{{font-size:10px;font-weight:800;letter-spacing:.22em;text-transform:uppercase}}
.shd i{{font-style:normal;font-size:7.5px;font-weight:800;letter-spacing:.14em;
 text-transform:uppercase;opacity:.5}}
.row{{display:flex;align-items:center;gap:8px;height:19px;border-bottom:1px dotted rgba(27,25,19,.32)}}
.bx{{width:13px;height:13px;border:1.4px solid #1B1913;flex:0 0 13px;font-size:11px;
 line-height:10px;text-align:center;color:#2A2720}}
.pr{{font-size:8.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;opacity:.52;
 width:132px;flex:0 0 132px}}
.hw{{font-family:"Shantell Sans","Bricolage Grotesque",cursive;font-size:13px;color:#2E2B22;
 transform:rotate(-.7deg);white-space:nowrap}}
.row.on .bx{{background:rgba(27,25,19,.06)}}
.ret{{display:flex;align-items:center;gap:8px;height:24px;margin-top:5px;
 border-top:1.5px solid #1B1913;padding-top:5px}}
.ret .pr{{opacity:.75}}
.blank{{flex:1;border-bottom:1.4px solid rgba(27,25,19,.5);height:12px;max-width:110px}}
.hw.big{{font-size:17px;transform:rotate(-1.4deg)}}
.band{{display:flex;justify-content:space-between;align-items:center;height:38px;margin-top:6px;
 border-top:1px dotted rgba(27,25,19,.32);padding-top:6px}}
.hw.sg{{font-size:16px;opacity:.7;transform:rotate(-4deg);display:inline-block;padding-right:4px}}
.stamp{{display:inline-block;transform:rotate(-6deg);border:2.5px solid #B8341F;color:#B8341F;
 padding:3px 10px;font-size:12.5px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 opacity:.85}}

/* ── RIGHT · the offer ── */
.r h2{{position:absolute;left:34px;top:76px;font-size:44px}}
.r .deck{{position:absolute;left:34px;right:34px;top:196px;margin:0;
 font-family:"Newsreader",Georgia,serif;font-size:12.5px;line-height:1.5;opacity:.6}}
.promise{{position:absolute;left:34px;right:34px;top:262px;margin:0;
 font-family:"Newsreader",Georgia,serif;font-size:17.5px;line-height:1.46}}
.promise sup{{font-family:"Bricolage Grotesque",sans-serif;font-size:8px;font-weight:800;
 color:{PLAN};vertical-align:super;margin-right:3px}}
.promise b{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:17px;
 letter-spacing:.01em;color:{PLAN};text-transform:uppercase}}
.nil{{position:absolute;left:34px;right:34px;top:606px;background:rgba(244,239,227,.05);
 border:1px solid rgba(244,239,227,.2);padding:11px 13px}}
.nil .shd{{border-bottom-color:rgba(244,239,227,.34)}}
.nil .shd b,.nil .shd i{{color:{CRM}}}
.nil p{{margin:7px 0 0;font-size:9px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 opacity:.42;line-height:1.9}}
.nil .none{{margin-top:9px;font-size:19px;font-weight:800;letter-spacing:.04em;color:{PLAN};
 text-transform:uppercase}}
.ash{{position:absolute;left:34px;top:772px;width:402px;height:150px;object-fit:cover}}
.acap{{position:absolute;left:34px;right:34px;top:934px;margin:0;
 font-family:"Newsreader",serif;font-size:11px;line-height:1.4;opacity:.55}}
.note{{position:absolute;left:34px;right:34px;top:1000px;padding-top:12px;
 border-top:1px solid rgba(244,239,227,.24)}}
.note p{{margin:0 0 9px;font-family:"Newsreader",serif;font-size:12.5px;line-height:1.5;opacity:.78}}
.kick{{position:absolute;left:34px;right:34px;bottom:78px;font-size:19px;font-weight:800;
 line-height:1.1;letter-spacing:-.015em;text-transform:uppercase}}
</style></head><body><main class="page">

<!-- ═══ MODULE 1 · HALF PORTRAIT · 166 × 475 mm ═══ -->
<section class="mod l">
  <span class="modtag">Half page · portrait</span>
  <div class="strip"><span>Modern Parallel</span><span>Genesis 28 : 20–22</span></div>
  <h1>The<br/><em>Counter-</em><br/>Offer</h1>
  <p class="deck">Jacob’s vow, set as what it actually is: a slip filled in across four hours
  of one night, by a man doing sums on a thing he has already been given for nothing.</p>
  <img class="hand" src="photos/p18_hand.jpg" alt=""/>
  <div class="stack">{blocks}</div>
  <p class="close">Four hours. Four terms. One signature. Every line of it answering
  an offer that had already been made in full.</p>
  <div class="foot"><span>Issue 001 · Page 18</span><span>Photograph · public domain</span></div>
</section>

<!-- ═══ MODULE 2 · HALF PORTRAIT · 166 × 475 mm ═══ -->
<section class="mod r">
  <span class="modtag">Half page · portrait</span>
  <div class="strip"><span>The Offer · 23:00</span><span>Genesis 28 : 13–15</span></div>
  <h2>The<br/><em>Offer</em></h2>
  <p class="deck">Issued four hours earlier, at the top of the same night, unprompted —
  to a man who was asleep on a rock at the time.</p>
  <p class="promise"><sup>13</sup>Behold, Yahweh stood above it, and said, “I am Yahweh, the God of
  Abraham your father, and the God of Isaac. The land whereon you lie, to you will I give it, and to
  your offspring. <sup>14</sup>Your offspring will be as the dust of the earth, and you will spread
  abroad to the west, and to the east, and to the north, and to the south. In you and in your offspring
  will all the families of the earth be blessed. <sup>15</sup>Behold, <b>I am with you</b>, and will keep
  you, wherever you go, and will bring you again into this land. For I will not leave you, until I have
  done that which I have spoken of to you.”</p>
  <div class="nil">
    <div class="shd"><b>Terms</b><i>Slip No. 28</i></div>
    <p>conditions · none<br/>required of the recipient · none<br/>expiry · none</p>
    <div class="none">Nothing asked</div>
  </div>
  <img class="ash" src="photos/p18_ashtray.jpg" alt=""/>
  <p class="acap">04:11. Not one thing in this photograph is the answer. The answer had already
  been given, four hours earlier, before he picked up the pencil.</p>
  <div class="note">
    <p>He had just seen heaven open. His reply was to itemise it — bread, clothing, safe passage —
    put a rate on it, and make the whole arrangement contingent on delivery.</p>
    <p>It is not a beautiful prayer. It is a man who has been handed everything, negotiating for
    slightly less, because he cannot yet believe the first offer was real.</p>
  </div>
  <p class="kick">Everybody bargains.<br/><em>Nobody has to.</em></p>
  <div class="foot"><span>The Geography of Nowhere</span><span>Two half-page modules · portrait</span></div>
</section>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-18.html"),"w").write(DOC)
print("wrote lab/between-sundays-page-18.html · 2 half-portrait modules · Gen 28:13-15 + 20-22")
