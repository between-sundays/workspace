#!/usr/bin/env python3
"""
Page 34 — THE BETHEL DIRECTORY. Yellow-pages spread, one page.
Look yourself up by what is wrong. The phone-number column is the verse column.
Content is flowed into columns HERE, in Python, so (Cont'd) lands exactly right.
"""
import json, math, os, re
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
rows=json.load(open(os.path.join(BASE,"directory_verified.json")))

W,H=941,1346
YELLOW="#F5DE21"; INK="#141308"; RED="#C6261C"; BLUE="#1B3E8F"; GREEN="#15653A"
MARGIN=28; HEADTOP=64; FOOTH=74
COLS=4; GUT=13
CW=(W-2*MARGIN-(COLS-1)*GUT)/COLS
COLTOP=HEADTOP+30
COLH=H-COLTOP-FOOTH

ABB={"Genesis":"Gen","Exodus":"Ex","Deuteronomy":"Deut","Joshua":"Josh","1 Samuel":"1 Sam",
"2 Samuel":"2 Sam","1 Kings":"1 Kgs","2 Kings":"2 Kgs","Psalm":"Ps","Proverbs":"Prov",
"Ecclesiastes":"Eccl","Isaiah":"Isa","Jeremiah":"Jer","Lamentations":"Lam","Joel":"Joel",
"Habakkuk":"Hab","Zechariah":"Zech","Matthew":"Matt","Mark":"Mark","Luke":"Luke","John":"John",
"Romans":"Rom","1 Corinthians":"1 Cor","2 Corinthians":"2 Cor","Galatians":"Gal",
"Ephesians":"Eph","Philippians":"Phil","Colossians":"Col","1 Thessalonians":"1 Thess",
"Hebrews":"Heb","James":"Jas","1 Peter":"1 Pet","2 Peter":"2 Pet","1 John":"1 Jn",
"Revelation":"Rev","Ruth":"Ruth"}
def abb(ref):
    m=re.match(r"^(.+?)\s+(\d+:\d+)$",ref)
    return f"{ABB.get(m.group(1),m.group(1))} {m.group(2)}" if m else ref

# cross-references, directory grammar
XREF={"AFRAID":"See also WORRIED, this page","ANXIOUS":"See also OVERWHELMED, this page",
"BURNED OUT":"See also TIRED, this page","GRIEVING":"See also THE READING, page 07",
"LONELY":"See also Genesis 28 in full, page 07","LOST":"See also THE MAP, page 04",
"STUCK":"See also WAITING, this page","WAITING":"See also FORECAST, page 20",
"TIRED":"See also BURNED OUT, this page","UNSEEN":"See also SPORTS, page 19"}

# display ads — boxed, sit inside the columns
ADS=[
 dict(h=132,html=f"""<div class="ad" style="border:3px double {RED}">
  <div class="ak" style="color:{RED}">Actual size &#8595;</div>
  <div style="text-align:center;font-size:26px;line-height:.5;padding:4px 0 7px">&#183;</div>
  <b>MUSTARD SEED</b><p>Faith this size moves mountains.<br/>No purchase necessary.</p>
  <div class="anum" style="color:{RED}">Matt 17:20</div></div>"""),
 dict(h=138,html=f"""<div class="ad" style="border:3px solid {BLUE};background:#E7ECF7">
  <div class="ak" style="color:{BLUE}">Free &#183; no-risk home trial</div>
  <b>GRACE</b><p>Send no money. You could not afford it
  anyway &mdash; that is the point. Inspect and enjoy at home. You risk nothing.</p>
  <div class="anum" style="color:{BLUE}">Rom 6:23</div></div>"""),
 dict(h=126,html=f"""<div class="ad" style="border:3px solid {GREEN};background:#E4EFE8">
  <div class="ak" style="color:{GREEN}">Help wanted &#183; all shifts</div>
  <b>HARVEST WORKERS</b><p>Large harvest, short staff.
  No experience required. Training on the job. Apply anywhere.</p>
  <div class="anum" style="color:{GREEN}">Luke 10:2</div></div>"""),
 dict(h=120,html=f"""<div class="ad" style="border:3px solid {INK}">
  <div class="ak">Learn at home &#183; 10 minutes</div>
  <b>BE STILL</b><p>The fastest way to slow down.
  Results reported in as little as one sitting.</p>
  <div class="anum">Ps 46:10</div></div>"""),
]

# ── measure ──────────────────────────────────────────────────────────────────
INNER=CW-8
CPL=int(INNER*0.62/3.45)          # chars per line in the descriptor column
BAR_H, ENT_H, XR_H = 21, 11.4, 13
def entry_h(d): return ENT_H*max(1,math.ceil(len(d)/CPL))

cats=[]
for r in rows:
    if not cats or cats[-1][0]!=r["cat"]: cats.append((r["cat"],[]))
    cats[-1][1].append((r["desc"],r["ref"]))

# ── flow into columns ────────────────────────────────────────────────────────
items=[]   # (kind, payload, height)
for name,ents in cats:
    items.append(("bar",name,BAR_H))
    for d,ref in ents: items.append(("ent",(d,ref),entry_h(d)))
    if name in XREF: items.append(("xref",XREF[name],XR_H))
    items.append(("gap",None,7))

adq=list(ADS)
cols=[[] for _ in range(COLS)]; ci=0; used=0.0
TOTAL=sum(h for _,_,h in items)+sum(a["h"]+8 for a in ADS)
TARGET=min(COLH-2, TOTAL/COLS)
ad_in_col=[False]*COLS
def lookahead(i):
    """height of this bar plus its first two entries — keeps heads off column feet"""
    tot=items[i][2]
    for j in range(i+1,min(i+3,len(items))):
        if items[j][0]!="ent": break
        tot+=items[j][2]
    return tot
for idx,it in enumerate(items):
    kind,payload,h=it
    # a category head must never strand at the foot of a column
    need = lookahead(idx) if kind=="bar" else h
    # a cross-reference must never start a column — it belongs to what came before
    if kind=="xref" and used+h>TARGET and ci<COLS-1:
        cols[ci].append(it); used+=h; continue
    if used+need>TARGET and ci<COLS-1:
        ci+=1; used=0.0
        if kind=="ent":                       # split mid-category -> repeat the head
            prev=[x for x in cols[ci-1] if x[0]=="bar"]
            if prev:
                head=prev[-1][1].replace(" (Cont'd)","")
                cols[ci].append(("bar",head+" (Cont'd)",BAR_H)); used+=BAR_H
        if kind=="gap": continue
    cols[ci].append(it); used+=h
    # ads ONLY at a category boundary, one per column, never mid-list
    if (kind=="gap" and adq and not ad_in_col[ci]
        and used>TARGET*0.55 and used+adq[0]["h"]+8<=COLH):
        ad=adq.pop(0); cols[ci].append(("ad",ad["html"],ad["h"]))
        used+=ad["h"]+8; ad_in_col[ci]=True
# anything left over goes to whichever column still has room
for ad in list(adq):
    for c2 in range(COLS):
        if not ad_in_col[c2] and sum(x[2] for x in cols[c2])+ad["h"]+8<=COLH:
            cols[c2].append(("ad",ad["html"],ad["h"])); ad_in_col[c2]=True; adq.remove(ad); break
def render(col):
    o=""
    for kind,p,h in col:
        if kind=="bar": o+=f'<div class="cbar">{p}</div>'
        elif kind=="ent":
            d,ref=p
            o+=(f'<div class="ent"><span class="d">{d}</span>'
                f'<span class="dots"></span><span class="r">{abb(ref)}</span></div>')
        elif kind=="xref": o+=f'<div class="xr">{p}</div>'
        elif kind=="gap": o+='<div style="height:7px"></div>'
        elif kind=="ad": o+=p
    return o
colhtml="".join(f'<div class="col">{render(c)}</div>' for c in cols)
placed=sum(1 for c in cols for x in c if x[0]=="ent")
print(f"  {len(cats)} categories, {placed} entries placed, "
      f"{len(ADS)-len(adq)} display ads, {COLS} columns")
for i,c in enumerate(cols):
    print(f"   col{i+1}: {sum(x[2] for x in c):.0f}px of {COLH:.0f}px")

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 34 · The Bethel Directory</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{YELLOW};color:{INK}}}
.rh{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:26px;display:flex;
 justify-content:space-between;align-items:baseline;border-bottom:3px solid {INK};padding-bottom:5px}}
.rh b{{font-size:19px;font-weight:800;letter-spacing:.04em}}
.rh b em{{font-style:normal;font-weight:400}}
.rh .tag{{font-size:9px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.strap{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{HEADTOP}px;
 display:flex;justify-content:space-between;font-size:8.5px;font-weight:700;
 letter-spacing:.1em;text-transform:uppercase;border-bottom:1px solid {INK};padding-bottom:4px}}
.cols{{position:absolute;left:{MARGIN}px;top:{COLTOP}px;width:{W-2*MARGIN}px;height:{COLH}px;
 display:flex;gap:{GUT}px}}
.col{{width:{CW}px;position:relative}}
.col+.col:before{{content:"";position:absolute;left:-{GUT/2:.0f}px;top:0;bottom:0;
 border-left:1px solid rgba(20,19,8,.45)}}
.cbar{{background:{INK};color:{YELLOW};font-size:8.5px;font-weight:800;letter-spacing:.09em;
 padding:3px 5px;margin:0 0 3px}}
.ent{{display:flex;align-items:baseline;gap:2px;line-height:1.16;padding:1px 0 1px 4px}}
.ent .d{{font-size:8.2px;font-weight:500;flex:0 1 auto}}
.ent .dots{{flex:1 1 auto;border-bottom:1px dotted rgba(20,19,8,.6);
 transform:translateY(-2px);min-width:5px}}
.ent .r{{font-size:8.2px;font-weight:800;white-space:nowrap;font-variant-numeric:tabular-nums}}
.xr{{font-size:7.6px;font-style:italic;padding:2px 0 0 4px;opacity:.85}}
.ad{{margin:7px 0 3px;padding:7px 8px;background:{YELLOW}}}
.ad .ak{{font-size:6.6px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
.ad b{{display:block;font-family:"Fraunces",Georgia,serif;font-weight:900;font-size:15px;
 line-height:1;margin:3px 0 3px}}
.ad p{{margin:0;font-size:7.6px;line-height:1.3}}
.ad .anum{{font-family:"Fraunces",serif;font-weight:900;font-size:16px;margin-top:5px;
 text-align:right;letter-spacing:-.01em}}
.banner{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;bottom:34px;border:3px solid {INK};
 background:{INK};color:{YELLOW};padding:9px 14px;display:flex;justify-content:space-between;
 align-items:center;gap:18px}}
.banner b{{font-family:"Fraunces",serif;font-weight:900;font-size:19px;line-height:1.05}}
.banner p{{margin:0;font-size:9px;line-height:1.4;max-width:44ch}}
.banner .pg{{font-family:"Fraunces",serif;font-weight:900;font-size:26px;white-space:nowrap}}
.folio{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;bottom:14px;display:flex;
 justify-content:space-between;font-size:8px;font-weight:700;letter-spacing:.16em;
 text-transform:uppercase}}
</style></head><body><main class="page">
 <div class="rh"><b>34 &nbsp; AFRAID &mdash; WORRIED</b>
  <span class="tag">The Bethel Directory &#183; Issue 001</span></div>
 <div class="strap"><span>Look yourself up by what is wrong</span>
  <span>References: New Living Translation &#183; the thirty most looked up are printed whole on page 35</span>
  <span>Free &#183; take one</span></div>
 <div class="cols">{colhtml}</div>
 <div class="banner">
  <div><b>Is your need not listed?</b>
   <p style="margin-top:3px">We add more every issue. Tell us what to put in the next one &mdash;
   the letters page is on 28. Nothing in this directory costs anything, and nobody paid to be in it.</p></div>
  <div class="pg">PAGE 28</div>
 </div>
 <div class="folio"><span>Between Sundays &#183; Issue 001</span>
  <span>Every reference checked before printing</span><span>Page 34</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-34.html","w").write(DOC)
print("  wrote press/between-sundays-page-34.html")
