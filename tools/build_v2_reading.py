#!/usr/bin/env python3
"""Build v2 of The Reading — full Scripture passages, not fragments."""
import json, os, html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "public", "v2")
os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(BASE, "scripture-web.json")))
THREAD = json.load(open(os.path.join(BASE, "thread-web.json")))
esc = html.escape

CSS = """
*{box-sizing:border-box;letter-spacing:0}
:root{
  --page-w:941px; --page-h:1346px;
  --paper:#f8f3e6; --ink:#17100d; --muted:#71695c;
  --blue:#143653; --pale:#c7ddeb; --yellow:#eff36a; --red:#f15139;
  --rule:rgba(23,16,13,.28);
}
@page{size:13.07in 18.69in;margin:0}
body{margin:0;display:grid;place-items:center;padding:28px;background:#cfc3b3;
  color:var(--ink);font-family:"Avenir Next","Gill Sans",sans-serif}
.page{position:relative;width:var(--page-w);height:var(--page-h);overflow:hidden;
  background:radial-gradient(rgba(23,16,13,.11) .5px,transparent .8px) 0 0/6px 6px,
    linear-gradient(180deg,rgba(255,255,255,.54),transparent 36%,rgba(20,54,83,.06)),var(--paper);
  box-shadow:0 30px 58px rgba(17,16,13,.26);isolation:isolate}
.page:before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;mix-blend-mode:multiply;
  background:linear-gradient(90deg,transparent 0 48.9%,rgba(23,16,13,.07) 49.2% 50.1%,transparent 50.4%),
             linear-gradient(180deg,transparent 0 51.2%,rgba(23,16,13,.08) 51.45%,transparent 51.7%)}
.sheet{position:absolute;z-index:1;inset:46px 54px 44px;display:flex;flex-direction:column}

.folio{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;
  border-bottom:1px solid var(--ink);padding-bottom:10px}
.folio p{margin:0;font-size:11px;font-weight:900;text-transform:uppercase;line-height:1.5}
.folio p:last-child{text-align:right}
.folio img{height:30px;align-self:center}

.band{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;
  border-bottom:3px solid var(--blue);padding:16px 0 12px;margin-bottom:4px}
.band .kick{margin:0 0 6px;font-size:11px;font-weight:900;text-transform:uppercase;color:var(--red);letter-spacing:.06em}
.band h1{margin:0;font-size:64px;line-height:.9;font-weight:900;text-transform:uppercase;letter-spacing:-.02em}
.band .count{flex:0 0 auto;text-align:right;font-size:11px;font-weight:900;text-transform:uppercase;color:var(--muted);line-height:1.5}
.band .count b{display:block;font-size:34px;color:var(--blue);line-height:1}

.why{margin:14px 0 0;padding:12px 16px;background:rgba(199,221,235,.5);border-left:4px solid var(--blue)}
.why p{margin:0;font-size:13.5px;line-height:1.5;font-family:Georgia,serif}

.cols{flex:1;min-height:0;margin-top:16px;column-count:2;column-gap:38px;column-rule:1px solid var(--rule)}
.scripture{font-family:Georgia,"Iowan Old Style",serif;font-size:15.2px;line-height:1.62;text-align:justify;hyphens:auto}
.scripture p{margin:0 0 .62em}
.scripture sup{font-family:"Avenir Next",sans-serif;font-size:9.5px;font-weight:900;color:var(--red);
  vertical-align:super;margin-right:3px}
.scripture .ref{break-inside:avoid;font-family:"Avenir Next",sans-serif;font-size:10.5px;font-weight:900;
  text-transform:uppercase;color:var(--blue);border-bottom:2px solid var(--blue);
  padding-bottom:4px;margin:0 0 10px;display:block}
.scripture .ref.later{margin-top:16px}
.pull{break-inside:avoid;margin:12px 0;padding:12px 0;border-top:2px solid var(--ink);border-bottom:1px solid var(--rule);
  font-family:Georgia,serif;font-size:20px;line-height:1.3;font-style:italic}

/* thread page */
.thread{flex:1;min-height:0;margin-top:12px;column-count:3;column-gap:22px;overflow:hidden}
.tr{break-inside:avoid;margin:0 0 9px;padding-bottom:8px;border-bottom:1px solid var(--rule)}
.tr b{display:block;font-size:9.5px;font-weight:900;text-transform:uppercase;color:var(--red);margin-bottom:2px}
.tr p{margin:0;font-family:Georgia,serif;font-size:11.2px;line-height:1.42}
.tr em{font-style:normal;background:var(--yellow);padding:0 2px}

.foot{border-top:1px solid var(--ink);padding-top:9px;margin-top:12px;display:flex;
  justify-content:space-between;font-size:10.5px;font-weight:900;text-transform:uppercase;color:var(--muted)}
"""

def verses(key, rng=None, chapter_label=None):
    """Render verses as one flowing scripture block."""
    vs = S[key]
    if rng:
        vs = [v for v in vs if rng[0] <= v["n"] <= rng[1]]
    return "".join(f'<sup>{v["n"]}</sup>{esc(v["t"])} ' for v in vs)

def page(num, of, kicker, title, ref_line, wordcount, why, blocks, foot_l, foot_r, pull=None, fs="15.2px", lh="1.62"):
    body = []
    for i, (label, content) in enumerate(blocks):
        cls = "ref later" if i else "ref"
        body.append(f'<span class="{cls}">{label}</span><p>{content}</p>')
    inner = "".join(body)
    if pull:
        inner += f'<div class="pull">{pull}</div>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays v2 - Page {num:02d} The Reading {of}</title>
<style>{CSS}</style></head>
<body><main class="page">
<section class="sheet">
  <header class="folio">
    <p>The Reading / {of} of 07<br/>{esc(ref_line)}</p>
    <img src="assets/between-sundays-logo-official-espresso.png" alt="Between Sundays"/>
    <p>No ads in this section<br/>World English Bible</p>
  </header>
  <div class="band">
    <div><p class="kick">{esc(kicker)}</p><h1>{title}</h1></div>
    <div class="count"><b>{wordcount}</b>verses<br/>printed in full</div>
  </div>
  <div class="why"><p>{why}</p></div>
  <div class="cols"><div class="scripture" style="font-size:{fs};line-height:{lh}">{inner}</div></div>
  <footer class="foot"><span>{esc(foot_l)}</span><span>{esc(foot_r)}</span></footer>
</section></main></body></html>"""

# ---------------- the seven pages ----------------
PAGES = []

# 07 — why he was running (the context the old issue never gave)
PAGES.append((7, page(7, "01",
    "Genesis 27:41 – 28:9 / before the road",
    "Why He Was<br/>Running",
    "Genesis 27:41-28:9", 22,
    "The old issue started with Jacob already asleep. It never said why he was outdoors. "
    "Here is the part that comes first: a stolen blessing, a brother's threat, and a mother "
    "who sends her son away to keep him alive.",
    [("Genesis 27:41-46 / World English Bible", verses("gen27")),
     ("Genesis 28:1-9", verses("gen28a"))],
    "The Reading / 01 of 07", "Continues on page 08 / Genesis 28:10-22",
    "He is not on a pilgrimage. He is leaving town before his brother finds him.", fs="17.6px", lh="1.6")))

# 08 — the whole dream, complete, one page
PAGES.append((8, page(8, "02",
    "Genesis 28:10-22 / the certain place",
    "The Certain<br/>Place",
    "Genesis 28:10-22", 13,
    "Previously this passage was broken across seven pages, a verse or two at a time. "
    "It belongs together. Read it whole, in one sitting, before anyone explains it.",
    [("Genesis 28:10-22 / World English Bible", verses("gen28b"))],
    "The Reading / 02 of 07", "Continues on page 09 / Exodus 3",
    "“Surely Yahweh is in this place, and I didn't know it.”", fs="20.4px", lh="1.6")))

# 09 — Exodus 3 in full
PAGES.append((9, page(9, "03",
    "Exodus 3:1-15 / the same promise, another person",
    "Certainly I<br/>Will Be With You",
    "Exodus 3:1-15", 15,
    "Four hundred years later the same sentence arrives for a man who is herding "
    "someone else's sheep and has every reason to think his story is over.",
    [("Exodus 3:1-15 / World English Bible", verses("exo3"))],
    "The Reading / 03 of 07", "Continues on page 10 / Joshua 1",
    "“Who am I, that I should go?” — and the answer is not about him.", fs="18.4px", lh="1.58")))

# 10 — Joshua 1 in full
PAGES.append((10, page(10, "04",
    "Joshua 1:1-9 / handed forward",
    "Wherever<br/>You Go",
    "Joshua 1:1-9", 9,
    "The promise is transferable. Moses dies and the sentence does not. "
    "It is repeated four times in nine verses to a man who is clearly afraid.",
    [("Joshua 1:1-9 / World English Bible", verses("jos1"))],
    "The Reading / 04 of 07", "Continues on page 11 / Psalm 139",
    "Be strong and courageous — said three times, because once was not enough.", fs="23px", lh="1.62")))

# 11 — Psalm 139 in full
PAGES.append((11, page(11, "05",
    "Psalm 139:1-18 / the map that fails",
    "Where Can<br/>I Go?",
    "Psalm 139:1-18", 18,
    "A songwriter tries to find the edge of God's presence and cannot locate it. "
    "This is the longest single reading in the issue, and the most personal.",
    [("Psalm 139:1-18 / World English Bible", verses("psa139"))],
    "The Reading / 05 of 07", "Continues on page 12 / Isaiah 43",
    "“If I make my bed in Sheol, behold, you are there.”", fs="17.8px", lh="1.56")))

# 12 — Isaiah 43 + Matthew 1
PAGES.append((12, page(12, "06",
    "Isaiah 43:1-7 & Matthew 1:18-25 / through the water, then in person",
    "I Will Be<br/>With You",
    "Isaiah 43:1-7 / Matthew 1:18-25", 15,
    "Spoken first to people in exile, who had every evidence that they had been left. "
    "Then, centuries later, the same promise stops being a sentence and becomes a name.",
    [("Isaiah 43:1-7 / World English Bible", verses("isa43")),
     ("Matthew 1:18-25", verses("mat1"))],
    "The Reading / 06 of 07", "Continues on page 13 / Matthew 28",
    "They shall call his name Immanuel, which is, being interpreted, “God with us.”", fs="18.2px", lh="1.58")))

# 13 — Matthew 28 + the whole thread
thread_html = "".join(
    f'<div class="tr"><b>{esc(t["ref"])}</b><p>{esc(t["text"])}</p></div>'
    for t in THREAD if t["text"]
)
PAGES.append((13, f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Between Sundays v2 - Page 13 The Reading 07</title>
<style>{CSS}</style></head>
<body><main class="page">
<section class="sheet">
  <header class="folio">
    <p>The Reading / 07 of 07<br/>Matthew 28:16-20 &amp; the whole thread</p>
    <img src="assets/between-sundays-logo-official-espresso.png" alt="Between Sundays"/>
    <p>No ads in this section<br/>World English Bible</p>
  </header>
  <div class="band">
    <div><p class="kick">Matthew 28:16-20 / and every other time it is said</p>
    <h1>I Am With You<br/>Always</h1></div>
    <div class="count"><b>18</b>times, across<br/>the whole Bible</div>
  </div>
  <div class="why"><p>The sentence Jacob heard in the dirt is not a one-off. It is said to
  patriarchs, shepherds, soldiers, kings, prophets, a teenage girl, a tentmaker, and finally
  to everyone. Printed here in full, in the order it appears.</p></div>
  <div class="cols" style="flex:0 0 auto;column-count:2"><div class="scripture" style="font-size:15px;line-height:1.55">
    <span class="ref">Matthew 28:16-20 / World English Bible</span>
    <p>{verses("mat28")}</p>
    <div class="pull">Then it is said again, and again, and again —</div>
  </div></div>
  <div class="thread">{thread_html}</div>
  <footer class="foot"><span>The Reading / 07 of 07</span><span>After the Reading / page 14</span></footer>
</section></main></body></html>"""))

for num, doc in PAGES:
    fn = os.path.join(OUT, f"between-sundays-page-{num:02d}.html")
    open(fn, "w").write(doc)
    print("wrote", os.path.basename(fn), len(doc)//1024, "KB")

# count verses now printed
total = sum(len(S[k]) for k in ["gen27","gen28a","gen28b","exo3","jos1","psa139","isa43","mat1","mat28"])
print(f"\nv1 Reading: 13 verses across 7 pages")
print(f"v2 Reading: {total} verses across 7 pages + {len([t for t in THREAD if t['text']])} thread references")
