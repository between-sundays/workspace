#!/usr/bin/env python3
"""
Page 03 — LOST IS NOT ALONE.
No rubric bar, no cream, no serif column. Full-bleed art; type reversed into the
sky the illustration already left empty; one hard coral card sitting on the grass.
Palette lifted straight off the artwork.
"""
import os
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","lab")
W,H=941,1346
SKY="#4FBDE3"; CREAM="#F9EBD0"; GRASS="#9AB334"; CORAL="#E85E3F"; NIGHT="#15303B"

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 03 · Lost Is Not Alone</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}} html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{SKY}}}
.bleed{{position:absolute;inset:0}}
.bleed img{{width:100%;height:100%;object-fit:cover;object-position:center;display:block}}

/* type reversed into the sky the drawing already left empty */
.kick{{position:absolute;left:52px;top:58px;font-size:11px;font-weight:800;letter-spacing:.3em;
 text-transform:uppercase;color:{CREAM}}}
.kick:after{{content:"";display:block;width:64px;height:4px;background:{CORAL};margin-top:12px}}
h1{{position:absolute;left:48px;top:118px;margin:0;font-size:96px;font-weight:800;line-height:.84;
 letter-spacing:-.045em;text-transform:uppercase;color:#fff}}
h1 em{{font-style:normal;color:{CORAL}}}

/* one hard card on the grass — no rounding, flush to the left trim */
.card{{position:absolute;left:0;bottom:96px;width:452px;background:{CORAL};color:{CREAM};
 padding:26px 30px 26px 52px}}
.card p{{margin:0 0 11px;font-size:16.5px;line-height:1.45;font-weight:500}}
.card p:last-of-type{{margin-bottom:0}}
.card b{{display:block;margin-top:16px;padding-top:14px;border-top:2px solid rgba(249,235,208,.55);
 font-size:20px;font-weight:800;line-height:1.12;letter-spacing:-.01em;text-transform:uppercase;color:#fff}}

/* second hard card — staggered, never level with the coral one */
.night{{position:absolute;right:0;bottom:268px;width:392px;background:{NIGHT};color:{CREAM};
 padding:24px 52px 24px 28px}}
.night .lab{{font-size:10px;font-weight:800;letter-spacing:.26em;text-transform:uppercase;color:{GRASS}}}
.night p{{margin:12px 0 0;font-size:17px;line-height:1.4;font-weight:600}}
.night .verse{{margin-top:16px;padding-top:13px;border-top:2px solid rgba(249,235,208,.4);
 font-size:14.5px;line-height:1.4;font-style:italic}}
.night .verse i{{display:block;font-style:normal;font-size:10px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;margin-top:7px;color:{GRASS}}}

.fol{{position:absolute;left:0;bottom:0;right:0;height:56px;background:{NIGHT};color:{CREAM};
 display:flex;align-items:center;justify-content:space-between;padding:0 52px;
 font-size:10px;font-weight:800;letter-spacing:.22em;text-transform:uppercase}}
.fol em{{font-style:normal;color:{GRASS}}}
</style></head><body><main class="page">
  <div class="bleed"><img src="art/p03-city-park.png" alt="A city skyline behind a green hill covered in small figures"/></div>

  <div class="kick">Lost is not alone</div>
  <h1>You are<br/>not the<br/><em>only one</em><br/>on the hill.</h1>

  <div class="card">
    <p>Look at the hill again. Every person on it came from somewhere else.</p>
    <p>One of them just got bad news. One is waiting on a call. One sat down
    because they did not know where else to go.</p>
    <p>None of them know that about each other. They all picked the same hill anyway.</p>
    <b>You have been one of those dots. You might be one today.</b>
  </div>

  <div class="night">
    <div class="lab">Try this</div>
    <p>Count the people on the hill. Now count how many you can see well enough
    to know one single thing about.</p>
    <div class="verse">&ldquo;&hellip;though he is not far from each one of us.&rdquo;
      <i>Acts 17:27</i></div>
  </div>

  <div class="fol"><span>Between Sundays &#183; <em>Issue 001</em></span><span>Page 03</span></div>
</main></body></html>"""
open(os.path.join(OUT,"between-sundays-page-03.html"),"w").write(DOC)
print("wrote lab/between-sundays-page-03.html — full bleed, reversed type, coral card")
