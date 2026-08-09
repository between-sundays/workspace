#!/usr/bin/env python3
"""
Page 04 — THE ROUTE.  My plans vs God's plan.
TWO stacked half-landscape modules (941 x 673 each) per MODULES.md.
All geometry is MODULE-LOCAL (0..673), never page-global.
"""
import os, html
BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "public", "lab")
esc  = html.escape

W, H, HALF = 941, 1346, 673
PLAN = "#E8A317"
INK  = "#141210"
CRM  = "#F4EFE3"

# ── waypoints: (name, note, label-side) ──────────────────────────────────────
WP = [
 ("BEERSHEBA",       "leaves under threat",                       "dn"),
 ("A CERTAIN PLACE", "one stone · one night · the promise",        "dn"),
 ("HARAN",           "the plan ends here",                         "dn"),
 ("SEVEN YEARS",     "worked for the wrong daughter",              "up"),
 ("SEVEN MORE",      "worked again for the right one",             "dn"),
 ("SIX MORE",        "wages changed ten times",                    "up"),
 ("THE ESCAPE",      "twenty years in, he runs again",             "dn"),
 ("PENIEL",          "wrestles till daybreak · limps after",       "up"),
 ("ESAU",            "the reunion he dreaded for two decades",     "dn"),
 ("BETHEL AGAIN",    "same ground · this time he builds an altar", "up"),
 ("ISRAEL",          "he is given a different name",               "up"),
 ("",                "",                                           ""),
]
R1, R2, R3 = 268, 412, 556
ROWS = [
  [(96, R1), (272, R1), (448, R1), (624, R1), (800, R1)],
  [(806, R2), (630, R2), (454, R2), (278, R2)],
  [(300, R3), (520, R3), (740, R3)],
]
PTS = [p for r in ROWS for p in r]

# the turns loop OUT past the label field (x 878 right, x 60 left) so no
# connector ever crosses a waypoint label
big = (f"M 96 {R1} L 800 {R1} L 878 {R1} "
       f"C 906 {R1} 906 {R2} 878 {R2} "
       f"L 806 {R2} L 278 {R2} L 60 {R2} "
       f"C 32 {R2} 32 {R3} 60 {R3} "
       f"L 300 {R3} L 740 {R3}")
plan_seg = f"M {PTS[0][0]} {PTS[0][1]} L {PTS[2][0]} {PTS[2][1]}"

dots, labels = [], []
for i, (x, y) in enumerate(PTS):
    name, note, side = WP[i]
    inplan = i <= 2
    dots.append(f'<circle cx="{x}" cy="{y}" r="{9 if inplan else 7}" '
                f'fill="{PLAN if inplan else CRM}"/>')
    if not side:
        continue
    ly = y - 24 if side == "up" else y + 26
    tr = "translate(-50%,-100%)" if side == "up" else "translate(-50%,0)"
    labels.append(
      f'<div class="wp{" pl" if inplan else ""}" style="left:{x}px;top:{ly}px;transform:{tr}">'
      f'<b>{esc(name)}</b><span>{esc(note)}</span></div>')

# ── top map: graticule + ticks ───────────────────────────────────────────────
grat = "".join(
  f'<line x1="{x}" y1="0" x2="{x}" y2="180" stroke="{INK}" stroke-width="1" '
  f'opacity=".09" stroke-dasharray="3 6"/>' for x in range(0, 880, 72))
ticks = "".join(
  f'<line x1="{70 + i*144}" y1="96" x2="{70 + i*144}" y2="108" stroke="{INK}" '
  f'stroke-width="2" opacity=".5"/>' for i in range(6))

DOC = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 04 · The Route</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{CRM};color:{INK}}}

.mod{{position:absolute;left:0;right:0;height:{HALF}px;overflow:hidden}}
.mod.top{{top:0}}
.mod.bot{{top:{HALF}px;background:{INK};color:{CRM}}}
.modtag{{position:absolute;top:13px;right:16px;font-size:8.5px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;opacity:.35}}
.strip{{position:absolute;left:40px;right:40px;top:44px;display:flex;justify-content:space-between;
 font-size:9.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
 padding-bottom:8px;border-bottom:1px solid currentColor}}
.lbl{{position:absolute;left:38px;margin:0;font-weight:800;letter-spacing:-.035em;
 line-height:.86;text-transform:uppercase}}
.lbl em{{font-style:normal;color:{PLAN}}}

/* ── TOP ── */
.top .lbl{{top:78px;font-size:82px}}
.said{{position:absolute;left:40px;top:186px;width:470px;margin:0;
 font-family:"Newsreader",Georgia,serif;font-size:16.5px;line-height:1.5}}
.plancard{{position:absolute;right:40px;top:176px;width:330px;border:2px solid {INK};padding:15px 17px}}
.plancard h4{{margin:0 0 8px;font-size:9px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;color:#B57C05}}
.plancard p{{margin:0;font-family:"Newsreader",serif;font-size:15px;line-height:1.5}}
.map{{position:absolute;left:40px;right:40px;top:296px;height:180px}}
.map svg{{width:100%;height:100%;display:block;overflow:visible}}
.pin{{position:absolute;font-size:10.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
.pin span{{display:block;font-family:"Newsreader",serif;font-weight:400;font-size:12px;
 letter-spacing:0;text-transform:none;opacity:.55;margin-top:2px}}
.unnamed{{position:absolute;text-align:center;width:200px;font-family:"Newsreader",serif;
 font-size:11.5px;font-style:italic;opacity:.5;line-height:1.3}}
.assume{{position:absolute;left:40px;right:40px;bottom:92px;display:grid;
 grid-template-columns:1fr 1fr 1fr;gap:0}}
.assume div{{padding:0 22px;border-left:1px solid rgba(20,18,16,.22)}}
.assume div:first-child{{padding-left:0;border-left:0}}
.assume h5{{margin:0 0 5px;font-size:8.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.42}}
.assume p{{margin:0;font-family:"Newsreader",serif;font-size:13px;line-height:1.38}}
.scale{{position:absolute;left:40px;bottom:52px;font-size:9.5px;font-weight:800;
 letter-spacing:.16em;text-transform:uppercase;opacity:.5}}
.rule{{position:absolute;left:40px;right:40px;bottom:38px;border-top:1px solid {INK};opacity:.25}}

/* ── BOTTOM ── */
.bot .lbl{{top:80px;font-size:62px}}
.kicker{{position:absolute;right:40px;top:78px;width:420px;text-align:right}}
.kicker h3{{margin:0;font-size:25px;font-weight:800;letter-spacing:-.02em;line-height:1.02;
 text-transform:uppercase}}
.kicker h3 em{{font-style:normal;color:{PLAN}}}
.kicker p{{margin:9px 0 0;font-family:"Newsreader",serif;font-size:12.5px;line-height:1.45;opacity:.72}}
.route{{position:absolute;left:0;right:0;top:0;height:{HALF}px}}
.route svg{{position:absolute;inset:0;width:100%;height:100%;overflow:visible}}
.wp{{position:absolute;width:168px;text-align:center}}
.wp b{{display:block;font-size:10px;font-weight:800;letter-spacing:.07em;
 text-transform:uppercase;line-height:1.12}}
.wp span{{display:block;font-family:"Newsreader",serif;font-size:10px;line-height:1.22;
 opacity:.58;margin-top:2px}}
.wp.pl b{{color:{PLAN}}}
.bracket{{position:absolute;left:96px;width:352px;top:196px;text-align:center}}
.bracket p{{margin:0 0 6px;font-size:10px;font-weight:800;letter-spacing:.14em;
 text-transform:uppercase;color:{PLAN}}}
.bracket .bar{{height:10px;border-left:2px solid {PLAN};border-right:2px solid {PLAN};
 border-top:2px solid {PLAN}}}
.foot{{position:absolute;left:40px;right:40px;bottom:34px;display:flex;justify-content:space-between;
 border-top:1px solid currentColor;padding-top:9px;font-size:9px;font-weight:800;
 letter-spacing:.2em;text-transform:uppercase;opacity:.6}}
</style></head><body><main class="page">

<!-- ═══ MODULE 1 · HALF LANDSCAPE ═══ -->
<section class="mod top">
  <span class="modtag">Half page · landscape · 332 × 237.5 mm</span>
  <div class="strip"><span>Special Report · Page 04</span><span>Genesis 27:43 – 28:5</span></div>
  <h1 class="lbl"><em>My</em> Plans</h1>
  <p class="said">Four clauses. One direction. No surprises. This is the whole of what he set out
  to do, and by any reasonable measure it was a sensible plan — the kind you could draw on the back
  of something in about four seconds.</p>
  <div class="plancard"><h4>The plan, in full</h4>
    <p>Leave. Get to Haran. Find a wife. Come home when Esau has calmed down.</p></div>
  <div class="map">
    <svg viewBox="0 0 861 180">
      {grat}
      <line x1="0" y1="102" x2="861" y2="102" stroke="{INK}" stroke-width="1" opacity=".16"/>
      <line x1="70" y1="102" x2="790" y2="102" stroke="{PLAN}" stroke-width="11" stroke-linecap="round"/>
      {ticks}
      <circle cx="70" cy="102" r="12" fill="{INK}"/>
      <circle cx="790" cy="102" r="12" fill="{INK}"/>
      <circle cx="246" cy="102" r="7" fill="{CRM}" stroke="{INK}" stroke-width="2"/>
    </svg>
    <div class="pin" style="left:44px;top:36px">Beersheba<span>home — no longer safe</span></div>
    <div class="pin" style="left:764px;top:36px">Haran<span>his uncle's house</span></div>
    <div class="unnamed" style="left:146px;top:120px">an unnamed stop<br/>not on the itinerary</div>
  </div>
  <div class="assume">
    <div><h5>It assumed</h5><p>that he would be back in a few months.</p></div>
    <div><h5>It assumed</h5><p>that the important part was the destination.</p></div>
    <div><h5>It assumed</h5><p>that nothing much would happen in between.</p></div>
  </div>
  <div class="scale">◀ 500 miles ▶ · on foot · one direction · no stops planned</div>
  <div class="rule"></div>
</section>

<!-- ═══ MODULE 2 · HALF LANDSCAPE ═══ -->
<section class="mod bot">
  <span class="modtag">Half page · landscape · 332 × 237.5 mm</span>
  <div class="strip"><span>The same map · pulled back</span><span>Genesis 28 – 35 · twenty-plus years</span></div>
  <h1 class="lbl"><em>God's</em> Plan</h1>
  <div class="kicker">
    <h3>The plan was a line.<br/><em>The route was a life.</em></h3>
    <p>Everything past the third dot is the part he did not ask for, could not have drawn,
    and would not give back. Note where the promise was made — dot two, the stop that
    wasn't on the itinerary, before one single thing had gone the way he intended.</p>
  </div>
  <div class="route">
    <svg viewBox="0 0 {W} {HALF}">
      <path d="{big}" fill="none" stroke="{CRM}" stroke-width="3.5" stroke-linecap="round" opacity=".85"/>
      <path d="{plan_seg}" fill="none" stroke="{PLAN}" stroke-width="12" stroke-linecap="round"/>
      {''.join(dots)}
      <path d="M 752 {R3} L 878 {R3}" stroke="{CRM}" stroke-width="3.5" stroke-dasharray="9 10"
            stroke-linecap="round" opacity=".85"/>
      <path d="M 864 {R3-11} L 884 {R3} L 864 {R3+11}" fill="none" stroke="{CRM}"
            stroke-width="3.5" stroke-linecap="round" opacity=".85"/>
    </svg>
    {''.join(labels)}
    <div class="bracket"><p>↓ all of it — the entire plan</p><div class="bar"></div></div>
    <div class="wp" style="left:838px;top:{R3+24}px;transform:translate(-50%,0);width:150px">
      <b>and it does not</b><span>stop here</span></div>
  </div>
  <div class="foot"><span>Issue 001 · Page 04 · The Geography of Nowhere</span>
    <span>Two half-page modules · 332 × 475 mm</span></div>
</section>
</main></body></html>"""

open(os.path.join(OUT, "between-sundays-page-04.html"), "w").write(DOC)
print(f"wrote lab/between-sundays-page-04.html · {len(PTS)} waypoints, module-local geometry")
