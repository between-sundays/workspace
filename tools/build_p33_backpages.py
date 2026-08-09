#!/usr/bin/env python3
"""
Page 33 — THE BACK OF THE BOOK.
Comic-book mail-order small ads. Every ad prints its verse IN FULL.
Chaos is composed: seeded per-ad face/size/border/rotation, misregistered spot
colour, two ads rotated up the margins, three bleeding off the trim.
"""
import json, os, random, math
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
NLT=json.load(open(os.path.join(BASE,"ads_verses.json")))
MSG=json.load(open(os.path.join(BASE,"ads_verses_msg.json")))
_dc=json.load(open(os.path.join(BASE,"directory_cache.json")))
for _k in ["Isaiah 40:31","Matthew 6:26","Proverbs 3:5","Ephesians 2:10","Zechariah 4:10","Luke 15:20"]:
    NLT[_k]=_dc[_k][1]
W,H=941,1346
PAPER="#EFE7D2"; INK="#1A1713"
SALMON="#F0836B"; YELLOW="#F2D64B"; GREY="#C9CBC4"; BLUE="#8FB8D8"
random.seed(33)

def v(ref,tr):
    t=(MSG if tr=="MSG" else NLT)[ref]
    t=t.replace('"','&ldquo;',1).replace('"','&rdquo;',1) if t.count('"')>=2 else t
    return t

# (headline, kicker, pitch, ref, translation, tint)
ADS=[
 ("BE TALLER!","Amazing height increase","Add inches where it counts. No gimmicks, no lifts, no waiting.","James 4:10","MSG",None),
 ("X-RAY SPECS","See what is really there","Stop being fooled by the outside of people. Works instantly. Works on you too.","1 Samuel 16:7","MSG",SALMON),
 ("INSTANT LIFE","Just add water","Never thirst again. Not a novelty. Comes with its own spring.","John 4:14","MSG",None),
 ("100-PC. ARMY SET","Complete outfit","Belt, breastplate, shield, helmet, sword. One size. Assembly required daily.","Ephesians 6:13","NLT",None),
 ("SELF-DEFENSE AT HOME","Advanced technique","The move nobody expects. Costs you everything and wins anyway.","Matthew 5:39","NLT",None),
 ("GROW A GIANT","From one tiny seed","Smallest seed in the catalog. Results reported in mountains.","Matthew 17:20","NLT",YELLOW),
 ("SLEEP LEARNING","While you rest","Stop working your worried fingers to the bone. Delivered nightly.","Psalm 127:2","MSG",None),
 ("FREE!","Send no money","No coupon. No 6-8 weeks. No handling charge. Already paid.","Romans 6:23","NLT",None),
 ("LONELY?","Make friends by mail","No dues, no meetings, no fee. He does the placing.","Psalm 68:6","NLT",GREY),
 ("HEAR A VOICE","Guaranteed audible","Works behind you, at every fork in the road. Batteries not included.","Isaiah 30:21","NLT",None),
 ("STOP BEING PUSHED AROUND","Nothing to learn","Do nothing. Say nothing. Someone else handles it.","Exodus 14:14","MSG",None),
 ("NEW NAME","Change yours today","Brand new. Issued personally. No paperwork.","Isaiah 62:2","MSG",None),
 ("CARRY LESS","Instant relief","Hand the whole load over. Weight limit: none.","1 Peter 5:7","MSG",None),
 ("GLOW IN THE DARK","You already do","Cannot be hidden. Works best on a hill.","Matthew 5:14","NLT",YELLOW),
 ("SEE IN THE DARK","No equipment","Night and day are the same to him. Standard issue.","Psalm 139:12","MSG",None),
 ("WORN OUT?","Burned out on religion?","Get away with him. Recover your life.","Matthew 11:28","MSG",SALMON),
 ("WEAKNESS WANTED","Apply as you are","No strength required. That is the entry requirement.","2 Corinthians 12:9","MSG",None),
 ("LOST ITEM RECOVERY","One of one hundred","He leaves the ninety-nine. Search continues until found.","Luke 15:4","MSG",None),
 ("COME HOME","No questions asked","He is already watching the road. Terms: none.","Luke 15:20","NLT",SALMON),
 ("GENUINE MASTERPIECE","Collector&rsquo;s item","One of one. Signed by the maker. Not for resale.","Ephesians 2:10","NLT",None),
 ("FREE MEALS FOR LIFE","Ask the birds","They do not plant, harvest or store. Still eating.","Matthew 6:26","NLT",BLUE),
 ("START SMALL","Beginners welcome","Tiny beginnings accepted here. Nobody is laughing.","Zechariah 4:10","NLT",None),
 ("AMAZING FLIGHT","No lessons required","Soar without training. Also works at walking pace.","Isaiah 40:31","NLT",None),
 ("STOP FIGURING IT OUT","Guaranteed relief","Put the map down. Somebody else knows the road.","Proverbs 3:5","NLT",None),
]

FACES=['"Bricolage Grotesque",sans-serif','"Fraunces",Georgia,serif',
       '"Newsreader",Georgia,serif','"Shantell Sans",cursive']
BORDERS=["3px solid","2px dashed","4px double","2px dotted","5px solid","1.5px solid"]

def build(i,a):
    head,kick,pitch,ref,tr,tint=a
    r=random.Random(1000+i)
    face=r.choice(FACES); hsz=r.choice([21,24,27,30,33]); rot=round(r.uniform(-1.6,1.6),2)
    bd=r.choice(BORDERS); pad=r.choice([8,10,12])
    kickstyle=r.choice(["upper","ital","script"])
    hstyle=r.choice(["plain","knock","under"])
    kk={"upper":f'<div class="k up">{kick}</div>',
        "ital":f'<div class="k it">{kick}</div>',
        "script":f'<div class="k sc">{kick}</div>'}[kickstyle]
    hh={"plain":f'<div class="h" style="font-family:{face};font-size:{hsz}px">{head}</div>',
        "knock":f'<div class="h knock" style="font-family:{face};font-size:{hsz-2}px">{head}</div>',
        "under":f'<div class="h und" style="font-family:{face};font-size:{hsz}px">{head}</div>'}[hstyle]
    bg=f"background:{tint};" if tint else ""
    mis=(f'<span class="mis" style="background:{tint}"></span>' if tint else "")
    body=(f'{mis}{kk}{hh}<p class="p">{pitch}</p>'
          f'<div class="vs"><span class="q">{v(ref,tr)}</span>'
          f'<span class="rf">{ref} &#183; {tr}</span></div>')
    est=34+ (2 if kickstyle!="script" else 3)*9 + hsz*1.15 + len(pitch)/34*12 + len(v(ref,tr))/40*11.4 + pad*2
    return dict(html=f'<div class="ad" style="border:{bd} {INK};{bg}padding:{pad}px;'
                     f'transform:rotate({rot}deg)">{body}</div>', h=est)

built=[build(i,a) for i,a in enumerate(ADS)]

# pack into three columns, shortest-first, keeping catalogue order roughly intact
COLX=[62,342,622]; COLW=[268,268,268]
AVAIL=1346-40-34            # page minus column top and folio band
cols=[[] for _ in COLX]; ch=[0.0]*3; dropped=[]
for b,a in zip(built,ADS):
    j=ch.index(min(ch))
    if ch[j]+b["h"]+9>AVAIL: dropped.append(a[0]); continue
    cols[j].append(b["html"]); ch[j]+=b["h"]+9
print("  column heights:", [f"{x:.0f}" for x in ch], f"of {AVAIL}")
if dropped: print("  DROPPED (did not fit):", ", ".join(dropped))
colhtml="".join(f'<div class="col" style="left:{COLX[i]}px;width:{COLW[i]}px">{"".join(cols[i])}</div>'
                for i in range(3))

SIDE_L=('<div class="side l"><b>WRITE ADVERTISER DIRECT</b> &#183; every offer on this page is free, '
        'unlimited, and already paid for &#183; <b>NO COUPON REQUIRED</b>')
SIDE_R=('<div class="side r"><b>TELL THEM YOU SAW IT IN BETWEEN SUNDAYS</b> &#183; the full catalogue is '
        'Genesis 28, pages 07&ndash;08 &#183; <b>NOW SHIPPING</b>')

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 33 · The Back of the Book</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:{INK}}}
.page:after{{content:"";position:absolute;inset:0;pointer-events:none;
 background-image:radial-gradient(rgba(26,23,19,.16) .6px,transparent .7px);
 background-size:3px 3px;opacity:.5;mix-blend-mode:multiply}}
.rh{{position:absolute;left:62px;right:62px;top:10px;display:flex;justify-content:space-between;
 font-size:9px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 border-bottom:2px solid {INK};padding-bottom:4px;z-index:5}}
.col{{position:absolute;top:40px}}
.ad{{position:relative;margin-bottom:9px;overflow:hidden;background:transparent}}
.mis{{position:absolute;left:-3px;right:1px;top:-2px;bottom:2px;opacity:.55;z-index:0}}
.ad>*{{position:relative;z-index:1}}
.k{{font-size:9px;line-height:1.2;margin-bottom:2px}}
.k.up{{font-weight:800;letter-spacing:.16em;text-transform:uppercase}}
.k.it{{font-style:italic;font-family:"Newsreader",serif;font-size:11px}}
.k.sc{{font-family:"Shantell Sans",cursive;font-size:11.5px}}
.h{{font-weight:800;line-height:.98;letter-spacing:-.01em;text-transform:uppercase;margin-bottom:4px}}
.h.knock{{background:{INK};color:{PAPER};display:inline-block;padding:2px 6px}}
.h.und{{border-bottom:3px solid {INK};display:inline-block;padding-bottom:1px}}
.p{{margin:0 0 5px;font-size:10px;line-height:1.32;font-family:"Bricolage Grotesque",sans-serif}}
.vs{{border-top:1px solid rgba(26,23,19,.5);padding-top:4px}}
.q{{display:block;font-family:"Newsreader",Georgia,serif;font-size:10.5px;line-height:1.34;
 font-style:italic}}
.rf{{display:block;font-size:8px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
 margin-top:3px}}
.side{{position:absolute;top:34px;bottom:30px;width:40px;writing-mode:vertical-rl;
 font-size:9.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
 border-left:2px solid {INK};border-right:2px solid {INK};padding:16px 12px;line-height:1.15}}
.side.l{{left:10px;transform:rotate(180deg)}}
.side.r{{right:10px}}
.side b{{font-weight:800}}
.foot{{position:absolute;left:62px;right:62px;bottom:8px;display:flex;justify-content:space-between;
 border-top:2px solid {INK};padding-top:4px;font-size:8.5px;font-weight:800;letter-spacing:.14em;
 text-transform:uppercase;z-index:5}}
</style></head><body><main class="page">
 <div class="rh"><span>The back of the book</span>
  <span>Small advertisements &#183; every offer scripture-sourced &#183; nothing costs anything</span>
  <span>Page 33</span></div>
 {SIDE_L}</div>
 {SIDE_R}</div>
 {colhtml}
 <div class="foot"><span>Between Sundays &#183; Issue 001</span>
  <span>Verses printed whole &#183; MSG &amp; NLT &#183; notices page 02</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-33.html","w").write(DOC)
print(f"  {sum(len(c) for c in cols)} of {len(ADS)} ads placed, every one with its verse in full")
