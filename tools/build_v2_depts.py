#!/usr/bin/env python3
"""v2: convert three weak/redundant department pages into full-Scripture pages."""
import json, os, html
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "public", "v2")
D = json.load(open(os.path.join(BASE, "scripture-depts.json")))
esc = html.escape

CSS = """
*{box-sizing:border-box;letter-spacing:0}
:root{--paper:#f8f3e6;--ink:#17100d;--muted:#71695c;--blue:#143653;--red:#f15139;
--yellow:#eff36a;--rule:rgba(23,16,13,.28)}
@page{size:13.07in 18.69in;margin:0}
body{margin:0;display:grid;place-items:center;padding:28px;background:#cfc3b3;color:var(--ink);
font-family:"Avenir Next","Gill Sans",sans-serif}
.page{position:relative;width:941px;height:1346px;overflow:hidden;
background:radial-gradient(rgba(23,16,13,.11) .5px,transparent .8px) 0 0/6px 6px,
 linear-gradient(180deg,rgba(255,255,255,.5),transparent 40%),var(--paper);
box-shadow:0 30px 58px rgba(17,16,13,.26)}
.sheet{position:absolute;inset:46px 54px 44px;display:flex;flex-direction:column}
.folio{display:flex;justify-content:space-between;border-bottom:1px solid var(--ink);padding-bottom:10px}
.folio p{margin:0;font-size:11px;font-weight:900;text-transform:uppercase;line-height:1.5}
.folio p:last-child{text-align:right}
.hero{padding:18px 0 14px;border-bottom:3px solid var(--ink)}
.hero .kick{margin:0 0 8px;font-size:11px;font-weight:900;text-transform:uppercase;color:var(--red)}
.hero h1{margin:0;font-size:78px;line-height:.88;font-weight:900;text-transform:uppercase;letter-spacing:-.025em}
.hero .dek{margin:12px 0 0;font-family:Georgia,serif;font-size:19px;line-height:1.4;max-width:60ch}
.note{margin:14px 0 0;padding:11px 15px;background:var(--yellow);border:2px solid var(--ink)}
.note p{margin:0;font-size:12.5px;font-weight:900;text-transform:uppercase;line-height:1.5}
.cols{flex:1;min-height:0;margin-top:18px;column-count:2;column-gap:38px;column-rule:1px solid var(--rule)}
.scripture{font-family:Georgia,"Iowan Old Style",serif;text-align:justify;hyphens:auto}
.scripture p{margin:0 0 .6em}
.scripture sup{font-family:"Avenir Next",sans-serif;font-size:9.5px;font-weight:900;color:var(--red);vertical-align:super;margin-right:3px}
.scripture .ref{display:block;font-family:"Avenir Next",sans-serif;font-size:10.5px;font-weight:900;
text-transform:uppercase;color:var(--blue);border-bottom:2px solid var(--blue);padding-bottom:4px;margin:0 0 10px}
.scripture .ref.later{margin-top:18px}
.pull{break-inside:avoid;margin:14px 0 0;padding:14px 0;border-top:2px solid var(--ink);
font-family:Georgia,serif;font-size:22px;line-height:1.28;font-style:italic}
.foot{border-top:1px solid var(--ink);padding-top:9px;margin-top:12px;display:flex;justify-content:space-between;
font-size:10.5px;font-weight:900;text-transform:uppercase;color:var(--muted)}
"""

def vs(key):
    return "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in D[key])

def build(num, sec, refline, kick, title, dek, note, blocks, pull, foot_r, fs="17.4px", lh="1.6"):
    inner = ""
    for i,(lab,c) in enumerate(blocks):
        inner += f'<span class="ref{" later" if i else ""}">{lab}</span><p>{c}</p>'
    inner += f'<div class="pull">{pull}</div>'
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays v2 - Page {num} {esc(sec)}</title><style>{CSS}</style></head>
<body><main class="page"><section class="sheet">
<header class="folio"><p>{esc(sec)}<br/>{esc(refline)}</p>
<p>Scripture printed in full<br/>World English Bible</p></header>
<div class="hero"><p class="kick">{esc(kick)}</p><h1>{title}</h1><p class="dek">{dek}</p></div>
<div class="note"><p>{esc(note)}</p></div>
<div class="cols"><div class="scripture" style="font-size:{fs};line-height:{lh}">{inner}</div></div>
<footer class="foot"><span>Issue 001 / Page {num}</span><span>{esc(foot_r)}</span></footer>
</section></main></body></html>"""
    open(os.path.join(OUT, f"between-sundays-page-{num}.html"), "w").write(doc)
    print("wrote page", num, sec)

# 36 — was a redundant coverage ad. Now the passage the ad was gesturing at.
build("36", "Reading / Wherever", "Psalm 121 & Romans 8:31-39",
 "Psalm 121 & Romans 8:31-39 / printed in full",
 "Nothing<br/>Separates",
 "The old page 36 was a second cell-coverage ad, one page after the first. The joke was already made. "
 "This is the text the joke was pointing at, printed whole instead.",
 "Replaces the duplicate coverage ad — 17 verses where an ad used to be.",
 [("Psalm 121 / World English Bible", vs("psa121")),
  ("Romans 8:31-39", vs("rom8"))],
 "“Neither height, nor depth, nor any other created thing, will be able to separate us from the love of God.”",
 "Food / page 37", fs="17px", lh="1.58")

# 44 — was a "photo essay" with no photographs.
build("44", "Reading / The Body", "Romans 12:1-8",
 "Romans 12:1-8 / printed in full",
 "Present<br/>Your Bodies",
 "Page 44 called itself a photo essay and carried no photographs — five colored rectangles labelled "
 "as rooms. Until there are real pictures, the page holds the passage it was quoting instead.",
 "Replaces the placeholder photo essay — real text where placeholder art used to be.",
 [("Romans 12:1-8 / World English Bible", vs("rom12"))],
 "“Present your bodies a living sacrifice, holy, acceptable to God, which is your spiritual service.”",
 "Mark the place / page 45", fs="21px", lh="1.62")

# 20 — weather page gains the passage it quotes
build("20", "Weather / The Reading Beneath", "Lamentations 3:19-26",
 "Lamentations 3:19-26 / printed in full",
 "New Every<br/>Morning",
 "The weather page quoted one line of Lamentations 3. Here is the paragraph it came from — "
 "including the part about bitterness, which the quote alone leaves out.",
 "Added to v2 — the full passage behind the forecast page's single quoted line.",
 [("Lamentations 3:19-26 / World English Bible", vs("lam3"))],
 "“This I recall to my mind; therefore I have hope.”",
 "Movies / page 21", fs="23px", lh="1.64")
