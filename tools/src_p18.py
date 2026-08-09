#!/usr/bin/env python3
"""Source CC0/PD frames for p18 THE VOW filmstrip."""
import urllib.request, urllib.parse, json, os, time
UA = {"User-Agent": "BetweenSundays/1.0 (adrianmarcus360@gmail.com)"}
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos", "p18raw")
os.makedirs(RAW, exist_ok=True)

SLOTS = {
 "flatlay": ["desk from above","overhead desk notebook","flat lay desk paper","writing desk top view",
             "notebook pencil overhead","paper pen table above","workspace from above","desk knolling"],
 "room":    ["storage room boxes","cluttered room night","small room lamp night","warehouse boxes dark",
             "stockroom shelves","messy bedroom night","cardboard boxes room","dim room interior"],
 "writing": ["man writing at desk night","person writing lamp","writing by lamplight","student studying night",
             "man at desk dark room","person reading lamp night","desk lamp night study"],
 "macro":   ["pencil on paper close up","hand writing pencil","pencil tip paper","writing hand macro",
             "hand pen paper close","filling out form","pencil marking paper","signing paper close up"],
 "ashtray": ["ashtray cigarettes","full ashtray","cigarette butts ashtray","ashtray table"],
}
def search(q, n=8):
    u = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": q, "license": "cc0,pdm", "page_size": n, "mature": "false"})
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25)).get("results", [])
    except Exception as e:
        print("  !", q, e); return []

meta = {}
for slot, queries in SLOTS.items():
    got = 0
    for q in queries:
        for r in search(q):
            url = r.get("url"); 
            if not url: continue
            w, h = r.get("width") or 0, r.get("height") or 0
            if w < 1200: continue
            fn = f"{slot}_{got:02d}.jpg"
            try:
                d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
                if len(d) < 40000: continue
                open(os.path.join(RAW, fn), "wb").write(d)
                meta[fn] = {"slot":slot,"q":q,"title":r.get("title"),"creator":r.get("creator"),
                            "license":r.get("license"),"src":r.get("foreign_landing_url"),"w":w,"h":h}
                got += 1
            except Exception: pass
            if got >= 14: break
        time.sleep(.3)
        if got >= 14: break
    print(f"{slot:9s} {got}")
json.dump(meta, open(os.path.join(RAW,"_meta.json"),"w"), indent=1)
