#!/usr/bin/env python3
"""
Page 22 — THE MANUFACTURER'S COUPONS. Pre-Spine campaign page.
Eight vintage grocery coupons. Guilloche borders and rosettes are generated
procedurally (hypotrochoid spirograph maths), not drawn — same way real
security printing made them.
"""
import json, math, os, random
BASE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(BASE,"public","press")
CV=json.load(open(os.path.join(BASE,"coupon_verses.json")))
ADS=json.load(open(os.path.join(BASE,"ads_verses.json")))
DIR=json.load(open(os.path.join(BASE,"directory_cache.json")))
W,H=941,1346
PAPER="#F4EFE0"; M=24
CW,CH=442,286; GAP=7

def hypo(cx,cy,R,r,d,turns=1,step=.06):
    """spirograph path — the rosette in the middle of a banknote"""
    pts=[]
    t=0.0; tmax=2*math.pi*turns*(r/math.gcd(int(R),int(r)) if r else 1)
    tmax=2*math.pi*turns*6
    while t<=tmax:
        k=(R-r)/r
        x=cx+(R-r)*math.cos(t)+d*math.cos(k*t)
        y=cy+(R-r)*math.sin(t)-d*math.sin(k*t)
        pts.append(f"{x:.1f} {y:.1f}"); t+=step
    return "M "+" L ".join(pts)

def band(x,y,w,amp,freq,col,n=3,sw=.55):
    """interlacing sine waves — the classic engraved border strip"""
    o=""
    for k in range(n):
        ph=k*2*math.pi/n
        pts=[]
        xx=0.0
        while xx<=w:
            pts.append(f"{x+xx:.1f} {y+amp*math.sin(freq*xx+ph):.1f}"); xx+=2.0
        o+=f'<path d="M {" L ".join(pts)}" fill="none" stroke="{col}" stroke-width="{sw}" opacity=".85"/>'
    return o

def frame(w,h,col,amp,freq,seed):
    r=random.Random(seed)
    o=f'<rect x="2" y="2" width="{w-4}" height="{h-4}" fill="none" stroke="{col}" stroke-width="1.4"/>'
    o+=band(6,11,w-12,amp,freq,col)
    o+=band(6,h-11,w-12,amp,freq*1.1,col)
    # verticals drawn as rotated bands
    o+=f'<g transform="translate(11,{h-6}) rotate(-90)">{band(0,0,h-12,amp,freq*1.05,col)}</g>'
    o+=f'<g transform="translate({w-11},{h-6}) rotate(-90)">{band(0,0,h-12,amp,freq*.95,col)}</g>'
    # corner rosettes
    for (cx,cy) in ((13,13),(w-13,13),(13,h-13),(w-13,h-13)):
        o+=f'<path d="{hypo(cx,cy,9,3.4,4.2,turns=.5,step=.14)}" fill="none" stroke="{col}" stroke-width=".5" opacity=".9"/>'
    return o

def rosette(cx,cy,col,R=34,r=8.6,d=17,sw=.45):
    return f'<path d="{hypo(cx,cy,R,r,d,turns=1,step=.045)}" fill="none" stroke="{col}" stroke-width="{sw}" opacity=".55"/>'

# object art — flat, slightly crude, like the product cuts
def obj_ledger(c1,c2):
    return f'''<g><rect x="6" y="8" width="52" height="64" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 14 22 h 36 M 14 32 h 36 M 14 42 h 28" stroke="{c1}" stroke-width="1.6"/>
 <path d="M 4 60 L 60 14" stroke="{c2}" stroke-width="5" stroke-linecap="round"/>
 <path d="M 32 4 v 20 M 24 12 h 16" stroke="{c2}" stroke-width="3.4"/></g>'''
def obj_cloth(c1,c2):
    return f'''<g><path d="M 8 66 Q 18 20 34 22 Q 52 24 58 66 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 14 52 Q 32 44 54 52" stroke="{c2}" stroke-width="2"/>
 <circle cx="52" cy="18" r="8" fill="{c2}"/><path d="M 48 18 l 3 4 l 6 -8" stroke="#fff" stroke-width="2" fill="none"/></g>'''
def obj_cup(c1,c2):
    return f'''<g><path d="M 12 20 h 40 l -5 50 h -30 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 52 28 q 12 2 10 14 q -2 10 -12 10" fill="none" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 16 34 q 16 8 32 0" stroke="{c2}" stroke-width="3"/>
 <path d="M 24 10 q 3 -6 0 -9 M 34 8 q 3 -6 0 -9" stroke="{c2}" stroke-width="2"/></g>'''
def obj_clock(c1,c2):
    return f'''<g><circle cx="34" cy="40" r="26" fill="#fff" stroke="{c1}" stroke-width="2.6"/>
 <path d="M 34 40 V 22 M 34 40 l 14 8" stroke="{c2}" stroke-width="2.6"/>
 <circle cx="34" cy="40" r="2.6" fill="{c1}"/>
 <path d="M 20 12 l 6 6 M 48 12 l -6 6" stroke="{c1}" stroke-width="2.6"/>
 <path d="M 56 62 l 8 8" stroke="{c2}" stroke-width="3"/></g>'''
def obj_map(c1,c2):
    return f'''<g><path d="M 6 18 L 24 12 L 44 20 L 62 12 L 62 62 L 44 70 L 24 62 L 6 68 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 24 12 V 62 M 44 20 V 70" stroke="{c1}" stroke-width="1.4"/>
 <path d="M 14 50 Q 30 36 46 46" stroke="{c2}" stroke-width="2" stroke-dasharray="4 3"/>
 <circle cx="46" cy="46" r="4" fill="{c2}"/></g>'''
def obj_tag(c1,c2):
    return f'''<g><path d="M 10 30 L 40 8 L 62 30 L 40 72 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <circle cx="40" cy="26" r="6" fill="none" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 24 44 h 30 M 28 54 h 22" stroke="{c2}" stroke-width="2.4"/></g>'''
def obj_stone(c1,c2):
    return f'''<g><path d="M 8 60 Q 4 32 26 22 Q 52 14 62 36 Q 66 58 42 66 Q 18 70 8 60 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 20 40 l 18 -5 M 22 50 l 24 -6" stroke="{c2}" stroke-width="2"/></g>'''
def obj_bell(c1,c2):
    return f'''<g><path d="M 34 10 q 20 0 20 26 v 22 h 6 v 6 H 8 v -6 h 6 V 36 q 0 -26 20 -26 Z" fill="#fff" stroke="{c1}" stroke-width="2.4"/>
 <circle cx="34" cy="70" r="5" fill="{c2}"/><path d="M 34 4 v 6" stroke="{c1}" stroke-width="2.4"/>
 <path d="M 22 34 q 12 -8 24 0" stroke="{c2}" stroke-width="2"/></g>'''

COUPONS=[
 dict(save="100%",unit="OFF",good="ANY DEBT YOU CANNOT PAY",name="THE RECORD",script="cancelled",
   cond="No balance too large. No payment plan offered or required.",
   ref="Colossians 2:14",fine="GOOD ON ANY PERSON. ANY ATTEMPT TO EARN IT CONSTITUTES MISUNDERSTANDING.",
   c1="#B5177E",c2="#1B3C8B",obj=obj_ledger,code="6200BF",litho="LITHO. IN U.S.A. 1241G"),
 dict(save="ALL",unit="OF IT",good="ONE (1) CLEAN SLATE",name="SCARLET",script="to snow",
   cond="Colourfast. Will not run, fade, or come back on wash day.",
   ref="Isaiah 1:18",fine="OFFER STANDS EVEN IF YOU HAVE READ THE TERMS AND STILL DO NOT BELIEVE THEM.",
   c1="#1E7A3C",c2="#1B3C8B",obj=obj_cloth,code="7779 LF",litho="LITHO. IN U.S.A. A-641"),
 dict(save="FREE",unit="",good="UNLIMITED REFILLS",name="THE WELL",script="never dry",
   cond="Becomes a spring inside the holder. No second purchase necessary, ever.",
   ref="John 4:14",fine="CASH REDEMPTION VALUE 1/20 OF 1¢. ACTUAL VALUE: SEE FINE PRINT ON PAGE 07.",
   c1="#C6261C",c2="#1E7A3C",obj=obj_cup,code="9067-RF",litho="LITHO. IN U.S.A. 1241G"),
 dict(save="NEW",unit="DAILY",good="NO EXPIRY DATE",name="MERCIES",script="every morning",
   cond="Restocked overnight. Yesterday's allotment does not carry over and does not need to.",
   ref="Lamentations 3:23",fine="THIS COUPON CANNOT EXPIRE. ATTEMPTS TO SAVE IT FOR LATER ARE UNNECESSARY.",
   c1="#1B3C8B",c2="#C6261C",obj=obj_clock,code="7818 AF",litho="LITHO. IN U.S.A. A-641"),
 dict(save="ANY",unit="STORE",good="REDEEMABLE AT ALL LOCATIONS",name="ANYWHERE",script="he is there",
   cond="Valid at altitude, at sea, in the dark, and in rooms with no windows.",
   ref="Psalm 139:12",fine="NO LOCATION HAS EVER BEEN FOUND OUTSIDE THE REDEMPTION AREA.",
   c1="#B5177E",c2="#B5177E",obj=obj_map,code="177-52019",litho="H-Q"),
 dict(save="ONE",unit="(1)",good="A BRAND-NEW NAME",name="ISSUED",script="personally",
   cond="Chosen by the manufacturer. No paperwork, no filing fee, no waiting period.",
   ref="Isaiah 62:2",fine="THE OLD NAME MAY REMAIN ON SOME MAPS. BOTH ARE ACCURATE. SEE PAGE 16.",
   c1="#C6261C",c2="#B5177E",obj=obj_tag,code="0T1EE",litho="LITHO. IN U.S.A. A-641"),
 dict(save="0¢",unit="DOWN",good="REST, FOR THE WORN OUT",name="COME TO ME",script="and rest",
   cond="No qualification required. Being tired is the entire eligibility test.",
   ref="Matthew 11:28",fine="THIS COUPON GOOD ONLY ON PEOPLE WHO ARE CARRYING SOMETHING. I.E. EVERYONE.",
   c1="#1E7A3C",c2="#D8A200",obj=obj_stone,code="7365-DF",litho="LITHO. IN U.S.A. 11-61G"),
 dict(save="ANY",unit="ONE",good="BEARER MAY BE ANYBODY",name="EVERYONE",script="who calls",
   cond="Not transferable, because it does not need to be. There is one for each holder.",
   ref="Romans 10:13",fine="NO NAME REQUIRED ON THIS LINE. THE MANUFACTURER ALREADY HAS IT.",
   c1="#1B3C8B",c2="#D8A200",obj=obj_bell,code="7109XF",litho="LITHO. IN U.S.A. A-641"),
]
def verse(ref):
    t=None
    for src in (CV,ADS):
        if ref in src: t=src[ref]; break
    if t is None: t=DIR[ref][1]
    t=t.strip()
    for a,b in (('\u201c',''),('\u201d','')):
        if t.startswith('\u201c'): t=t[1:]
    t=t.strip()
    if t.endswith('\u201d'): t=t[:-1]
    return t.strip()

def coupon(i,c):
    r=random.Random(700+i)
    amp=r.uniform(2.2,3.4); freq=r.uniform(.16,.26)
    return f'''<div class="cp">
 <svg class="fr" viewBox="0 0 {CW} {CH}">{frame(CW,CH,c["c1"],amp,freq,i)}
   {rosette(CW*0.62,CH*0.60,c["c2"],R=30,r=7.6,d=15)}</svg>
 <div class="banner" style="background:{c["c1"]}">Take this coupon anywhere</div>
 <div class="valtop" style="background:{c["c1"]}">{c["save"]}</div>
 <div class="valbot" style="background:{c["c1"]}">{c["save"]}</div>
 <div class="inner">
  <div class="obj"><svg viewBox="0 0 68 78" width="62" height="70">{c["obj"](c["c1"],c["c2"])}</svg></div>
  <div class="txt">
   <div class="save" style="color:{c["c2"]}">SAVE <b>{c["save"]}</b> <i>{c["unit"]}</i></div>
   <div class="good">Good for {c["good"]}</div>
   <div class="name" style="color:{c["c1"]}">{c["name"]}<em style="color:{c["c2"]}">{c["script"]}</em></div>
   <div class="cond">{c["cond"]}</div>
  </div>
 </div>
 <div class="vs">&ldquo;{verse(c["ref"])}&rdquo;</div>
 <div class="fine">{c["fine"]}</div>
 <div class="bar" style="background:{c["c1"]}">{c["ref"].upper()} &#183; NLT</div>
 <div class="code">{c["code"]}</div><div class="litho">{c["litho"]}</div>
</div>'''
cps="".join(coupon(i,c) for i,c in enumerate(COUPONS))

DOC=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<title>Between Sundays — Page 22 · The Manufacturer's Coupons</title>
<link rel="stylesheet" href="fonts.css">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
@page{{size:9.8021in 14.0208in;margin:0}}
body{{display:grid;place-items:center;padding:28px;background:#cfc3b3;
 font-family:"Bricolage Grotesque",Arial,sans-serif}}
.page{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{PAPER};color:#191510;
 padding:{M}px}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid #191510;
 padding-bottom:5px}}
.hd b{{font-size:21px;font-weight:800;letter-spacing:-.01em;text-transform:uppercase}}
.hd span{{font-size:8.5px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;opacity:.7}}
.note{{font-size:10px;line-height:1.35;margin:5px 0 8px;font-weight:600;max-width:96ch}}
.sheet{{display:grid;grid-template-columns:{CW}px {CW}px;gap:{GAP}px;justify-content:space-between}}
.cp{{position:relative;width:{CW}px;height:{CH}px;background:#FBF8EE;overflow:hidden}}
.fr{{position:absolute;inset:0;width:100%;height:100%}}
.banner{{position:absolute;left:20px;right:20px;top:9px;height:15px;color:#FBF8EE;font-size:8px;
 font-weight:800;letter-spacing:.18em;text-transform:uppercase;display:flex;align-items:center;
 justify-content:center}}
.valtop,.valbot{{position:absolute;width:44px;height:44px;border-radius:50%;color:#FBF8EE;
 display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;
 letter-spacing:-.02em}}
.valtop{{right:12px;top:6px}} .valbot{{left:10px;top:104px;width:38px;height:38px;font-size:12px}}
.inner{{position:absolute;left:20px;right:62px;top:32px;display:flex;gap:10px;align-items:flex-start}}
.obj{{flex:0 0 62px;padding-top:2px}}
.txt{{flex:1}}
.save{{font-size:19px;font-weight:800;letter-spacing:-.01em;line-height:1}}
.save b{{font-size:27px}} .save i{{font-style:normal;font-size:12px}}
.good{{font-size:8.5px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;margin-top:3px}}
.name{{font-family:"Fraunces",Georgia,serif;font-weight:900;font-size:24px;line-height:.98;margin-top:4px;
 letter-spacing:-.02em}}
.name em{{font-family:"Shantell Sans",cursive;font-style:normal;font-weight:700;font-size:15px;
 margin-left:7px}}
.cond{{font-size:9px;line-height:1.35;margin-top:4px;font-weight:600;max-width:31ch}}
.vs{{position:absolute;left:56px;right:20px;bottom:54px;font-family:"Newsreader",Georgia,serif;
 font-size:9.4px;line-height:1.32;font-style:italic}}
.fine{{position:absolute;left:20px;right:20px;bottom:34px;font-size:6.2px;font-weight:700;
 letter-spacing:.06em;line-height:1.3}}
.bar{{position:absolute;left:20px;right:20px;bottom:14px;height:14px;color:#FBF8EE;font-size:7.5px;
 font-weight:800;letter-spacing:.16em;display:flex;align-items:center;justify-content:center}}
.code{{position:absolute;right:22px;bottom:2px;font-size:6px;font-weight:800;letter-spacing:.1em;opacity:.8}}
.litho{{position:absolute;left:22px;bottom:2px;font-size:5.6px;font-weight:700;letter-spacing:.08em;opacity:.7}}
.foot{{position:absolute;left:{M}px;right:{M}px;bottom:8px;border-top:2px solid #191510;padding-top:4px;
 display:flex;justify-content:space-between;font-size:8px;font-weight:800;letter-spacing:.14em;
 text-transform:uppercase}}
</style></head><body><main class="page">
<div class="hd"><b>The manufacturer&rsquo;s coupons</b>
 <span>Cut along the border &#183; no store required &#183; page 22</span></div>
<p class="note">In a grocery coupon the shop does not absorb the discount &mdash; the manufacturer does.
The store hands the paper back up the chain and is paid in full by whoever made the thing.
That is the only reason a coupon works, and it is the reason these do.
<b>The next four pages lift out. Take them with you.</b></p>
<div class="sheet">{cps}</div>
<div class="foot"><span>Between Sundays &#183; Issue 001</span>
 <span>Every offer honoured by the manufacturer &#183; verses NLT</span><span>Page 22</span></div>
</main></body></html>"""
open(f"{OUT}/between-sundays-page-22.html","w").write(DOC)
print(f"  {len(COUPONS)} coupons, guilloche generated procedurally")
