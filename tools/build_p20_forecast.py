#!/usr/bin/env python3
"""
Page 20 — WEATHER · Forecast for the Middle.
The page IS a forecast table. Art full-bleed across the top with the headline
reversed into the storm; five data rows underneath; the last row is the payoff.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346; ART=941
STORM="#3B434B"; SLATE="#59636C"; MIST="#E4E6EA"; ORANGE="#E07B3C"; PAPER="#EDEEF0"

ROWS=[("Today","Rain.","Your coat.",0),
      ("Tomorrow","Rain.","Your coat.",0),
      ("This week","Rain, mostly.","Your coat.",0),
      ("This month","It starts to clear. You will not notice the day it happens.","Your coat, for now.",0),
      ("After that","Sun.","You will not need it.",1)]
rows="".join(
  f'<div class="r{" hot" if hot else ""}"><b>{w}</b><span>{c}</span><i>{n}</i></div>'
  for w,c,n,hot in ROWS)

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 20 · Forecast for the Middle</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{STORM}}}
.art{{position:absolute;left:0;top:0;width:{W}px;height:{ART}px;overflow:hidden}}
.art img{{width:100%;height:100%;object-fit:cover;display:block}}

.dept{{position:absolute;left:44px;top:40px;font-size:10.5px;font-weight:800;letter-spacing:.3em;
 text-transform:uppercase;color:{MIST}}}
.dept:after{{content:"";display:block;width:52px;height:4px;background:{ORANGE};margin-top:11px}}
h1{{position:absolute;left:40px;top:100px;margin:0;font-size:84px;font-weight:800;line-height:.85;
 letter-spacing:-.045em;text-transform:uppercase;color:#fff;text-shadow:0 2px 26px rgba(20,26,32,.45)}}
h1 em{{font-style:normal;color:{ORANGE}}}

.tbl{{position:absolute;left:0;right:0;top:{ART}px;bottom:56px;padding:0 40px}}
.note{{display:flex;justify-content:space-between;align-items:baseline;padding:11px 0 8px;
 border-bottom:3px solid {STORM}}}
.note b{{font-size:10px;font-weight:800;letter-spacing:.22em;text-transform:uppercase}}
.note span{{font-size:12.5px;font-weight:500;opacity:.75;max-width:62ch;text-align:right}}
.head{{display:grid;grid-template-columns:150px 1fr 190px;gap:16px;padding:8px 0 7px;
 border-bottom:1px solid rgba(59,67,75,.3);font-size:8.5px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;opacity:.5}}
.r{{display:grid;grid-template-columns:150px 1fr 190px;gap:16px;align-items:baseline;
 padding:9px 0;border-bottom:1px solid rgba(59,67,75,.22)}}
.r b{{font-size:17px;font-weight:800;letter-spacing:-.01em}}
.r span{{font-size:15px;font-weight:500;line-height:1.35}}
.r i{{font-style:normal;font-size:14px;font-weight:700;opacity:.7}}
.r.hot{{background:{ORANGE};color:#fff;border-bottom:0;margin:2px -14px 0;padding:12px 14px}}
.r.hot i{{opacity:1}}
.psalm{{margin:13px 0 0;font-size:12.5px;font-weight:600;font-style:italic;opacity:.62}}
.fol{{position:absolute;left:0;right:0;bottom:0;height:56px;background:{STORM};color:{MIST};
 display:flex;align-items:center;justify-content:space-between;padding:0 44px;
 font-size:10px;font-weight:800;letter-spacing:.22em;text-transform:uppercase}}
.fol em{{font-style:normal;color:{ORANGE}}}
</style></head><body><main class="page">
  <div class="art"><img src="art/p20-forecast.png" alt="Rain over a mountain town, and a child walking through it"/></div>
  <div class="dept">Weather</div>
  <h1>It is going<br/>to rain for<br/><em>a while.</em></h1>

  <div class="tbl">
    <div class="note"><b>Forecast for the middle</b>
      <span>The middle of a hard season does not get a real forecast. This is our best guess.</span></div>
    <div class="head"><span>When</span><span>What it will do</span><span>What you will need</span></div>
    {rows}
    <p class="psalm">&ldquo;Weeping may stay for the night, but joy comes in the morning.&rdquo;
      &mdash; Psalm 30:5</p>
  </div>
  <div class="fol"><span>Between Sundays &#183; <em>Issue 001</em></span><span>Page 20</span></div>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-20.html"),"w").write(DOC)
print("wrote lab/between-sundays-page-20.html — full-bleed art + 5-row forecast table")
