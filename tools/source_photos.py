#!/usr/bin/env python3
"""Source CC0 / public-domain photography for Between Sundays Issue 001."""
import urllib.request, urllib.parse, json, time, os, hashlib

UA = {"User-Agent": "BetweenSundays/1.0 (adrianmarcus360@gmail.com)"}
BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "photos", "raw")
os.makedirs(RAW, exist_ok=True)

# slot -> list of queries (broad, because CC0 is a thin pool)
SLOTS = {
 "cover":      ["dark street night","night street lamp","empty parking lot night","street light fog",
                "road at night","bus stop","night city sidewalk","gas station night"],
 "waiting":    ["waiting room chairs","empty chairs row","hospital waiting","airport terminal seats",
                "empty seat row","clinic interior"],
 "corridor":   ["hospital corridor","empty hallway","school hallway","corridor light","hallway night"],
 "laundromat": ["laundromat","washing machines row","laundry room","launderette"],
 "kitchen":    ["kitchen table","kitchen morning light","empty kitchen","dining table home",
                "table crumbs","breakfast table"],
 "stone":      ["smooth stone","single stone","river stone","rock close up","pebble"],
 "road":       ["empty road dusk","highway sunset","desert road","country road evening","open road"],
 "stairwell":  ["stairwell","staircase looking up","concrete stairs","fire escape stairs"],
 "stadium":    ["stadium empty seats","empty bleachers","stadium tunnel","running track","empty arena"],
 "table":      ["table in field","picnic table field","table outdoors","set table","dinner table"],
 "window":     ["light through blinds","morning light window","window light room","curtain light"],
 "bread":      ["bread loaf","bakery bread","bread on table","loaf of bread"],
 "motel":      ["motel sign","neon motel","roadside motel","motel room"],
 "porch":      ["porch light","front door night","house at night","doorway light"],
 "alarm":      ["fire alarm box","emergency box","break glass","fire extinguisher wall"],
 "backcover":  ["sunrise horizon","dawn light field","first light landscape","sky dawn"],
}

def search(q, page_size=8):
    u = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": q, "license": "cc0,pdm", "page_size": page_size, "mature": "false"})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25))
        return d.get("results", [])
    except Exception:
        return []

seen = set()
manifest = []
for slot, queries in SLOTS.items():
    got = 0
    for q in queries:
        if got >= 10: break
        for r in search(q):
            if got >= 10: break
            url = r.get("url") or ""
            w, h = r.get("width") or 0, r.get("height") or 0
            if not url or w < 1200 or h < 800: continue
            key = hashlib.md5(url.encode()).hexdigest()[:10]
            if key in seen: continue
            seen.add(key)
            fn = f"{slot}__{key}.jpg"
            try:
                data = urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=40).read()
                if len(data) < 40_000: continue
                open(os.path.join(RAW, fn), "wb").write(data)
                manifest.append({"slot": slot, "file": fn, "license": r.get("license"),
                                 "title": r.get("title"), "source": r.get("foreign_landing_url"),
                                 "creator": r.get("creator"), "w": w, "h": h, "query": q})
                got += 1
            except Exception:
                continue
        time.sleep(0.4)
    print(f"{slot:11} {got} images")

json.dump(manifest, open(os.path.join(BASE, "photos", "manifest.json"), "w"), indent=1)
print(f"\nTOTAL {len(manifest)} images -> photos/raw/")
