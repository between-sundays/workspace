#!/usr/bin/env python3
"""Verify every directory reference against bolls.life (NLT). Resumable."""
import json, urllib.request, re, time, os
from directory_data import DIRECTORY
BOOKS={b:i+1 for i,b in enumerate(
"Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|1 Samuel|2 Samuel|1 Kings|2 Kings|"
"1 Chronicles|2 Chronicles|Ezra|Nehemiah|Esther|Job|Psalm|Proverbs|Ecclesiastes|Song of Solomon|Isaiah|"
"Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|"
"Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|1 Corinthians|2 Corinthians|Galatians|"
"Ephesians|Philippians|Colossians|1 Thessalonians|2 Thessalonians|1 Timothy|2 Timothy|Titus|Philemon|"
"Hebrews|James|1 Peter|2 Peter|1 John|2 John|3 John|Jude|Revelation".split("|"))}
CACHE="directory_cache.json"
cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def fetch(ref):
    if ref in cache: return cache[ref]
    m=re.match(r"^(.+?)\s+(\d+):(\d+)$",ref)
    if not m: cache[ref]=[False,"unparseable"]; return cache[ref]
    bk,ch,vs=m.group(1).strip(),int(m.group(2)),int(m.group(3))
    if bk not in BOOKS: cache[ref]=[False,"unknown book: "+bk]; return cache[ref]
    url=f"https://bolls.life/get-verse/NLT/{BOOKS[bk]}/{ch}/{vs}/"
    for attempt in range(4):
        try:
            d=json.load(urllib.request.urlopen(url,timeout=25))
            t=re.sub("<[^>]+>"," ",d.get("text","")).strip()
            if t: cache[ref]=[True,t]; break
            cache[ref]=[False,"empty"]; break
        except Exception as e:
            if attempt==3: cache[ref]=[False,str(e)[:60]]
            else: time.sleep(2*(attempt+1))
    time.sleep(0.2); return cache[ref]

rows=[]; bad=[]
for cat,entries in DIRECTORY:
    for desc,ref in entries:
        ok,txt=fetch(ref)
        (rows if ok else bad).append((cat,desc,ref,txt))
json.dump(cache,open(CACHE,"w"))
print(f"VERIFIED {len(rows)} / {len(rows)+len(bad)} references")
if bad:
    print("\nFAILED:")
    for c,d,r,t in bad: print(f"  {c:18s} {r:24s} {t[:60]}")
json.dump([{"cat":c,"desc":d,"ref":r,"text":t} for c,d,r,t in rows],
          open("directory_verified.json","w"),indent=1)
