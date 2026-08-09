#!/usr/bin/env python3
"""Emit public/data/versions.json — the static baseline the Control Room reads."""
import glob, os, re, json, hashlib
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB=os.path.join(BASE,"public")
NAMES={1:"Cover",2:"Contents / Field guide",3:"Lost Is Not Alone",4:"The Geography of Nowhere",
5:"Wayfarer / Baggage claim",6:"Gate to The Reading",7:"The Reading 01",8:"The Reading 02",
9:"The Reading 03",10:"The Reading 04",11:"The Reading 05",12:"The Reading 06",13:"The Reading 07 / Bridge",
14:"After the Reading / Feature",15:"The Place You Almost Walked Past",16:"Luz Local / Words & Meaning",
17:"Field Guide",18:"Modern Parallel",19:"Sports — Away Team Advantage",
20:"Weather — Forecast for the Middle",21:"Movies / Cast of Note",22:"Obituaries / Coupons",
23:"The Spine 01",24:"The Spine 02",25:"The Spine 03",26:"The Spine 04",
27:"If the Middle Is Missing, Good",28:"Letters",29:"Fiction",30:"Comics",
31:"Games — Crossword",32:"Games — Find the Certain Place",33:"But God / Back of the Book",
34:"But God / Bethel Directory",35:"No Dead Zones / Most Looked Up",36:"Classifieds",
37:"Food",38:"Home — Give Them the Tour",39:"Poster — Surely God Is in This Place",
40:"Music — Songs for Walking Home",41:"House Ads / Supply Co.",42:"Work / Small Ads",
43:"Stay With What Is True / Write It Down",44:"Photo Essay",45:"Mark the Place / Games",
46:"Where This Paper Went / Games",47:"Next Issue",48:"Back Cover"}
VER={"v1":"V1","v2":"V2","v3":"V3","v4":"V4","v5":"V5","lab":"NEW","labb":"NEW B",
     "codex":"CODEX","manus":"MANUS","press":"PRESS"}
def phash(p,n=14):
    im=Image.open(p).convert("L").resize((n,n),Image.LANCZOS)
    px=list(im.getdata()); avg=sum(px)/len(px)
    return f"{int(''.join('1' if x>avg else '0' for x in px),2):x}"
def pagenum(fn):
    b=os.path.basename(fn)
    if "Cover" in b: return 1
    m=re.search(r"Page(\d+)",b)
    return int(m.group(1)) if m else None
inv={}
for v in VER:
    for f in sorted(glob.glob(f"{PUB}/{v}/BetweenSundays-Issue001-*.jpg")+
                    glob.glob(f"{PUB}/{v}/BetweenSundays-Issue001-*.png")):
        if "Contact-Sheet" in f: continue
        n=pagenum(f)
        if not n: continue
        try: h=phash(f)
        except Exception: h=hashlib.md5(open(f,"rb").read()).hexdigest()[:12]
        inv.setdefault(n,[]).append((v,os.path.relpath(f,PUB),h))
out=[]
for n in sorted(inv):
    groups={}; order=[]
    for v,rel,h in inv[n]:
        if h not in groups: groups[h]={"src":"/"+rel,"vers":[]}; order.append(h)
        if v not in groups[h]["vers"]: groups[h]["vers"].append(v)
    NEWV={"lab","labb","codex","press","manus"}
    order.sort(key=lambda h:(0 if NEWV&set(groups[h]["vers"]) else 1,sorted(groups[h]["vers"])[-1]))
    out.append({"n":n,"name":NAMES.get(n,""),
        "variants":[{"src":groups[h]["src"],"vers":[VER[x] for x in sorted(groups[h]["vers"])]}
                    for h in order]})
os.makedirs(f"{PUB}/data",exist_ok=True)
json.dump(out,open(f"{PUB}/data/versions.json","w"))
print(f"versions.json: {len(out)} pages, {sum(len(p['variants']) for p in out)} variants")
