#!/usr/bin/env python3
"""Verse Bank: every scripture reference actually printed in Issue 001, mined from the
built pages themselves. Source of truth is the shipped HTML, not a hand-kept list."""
import re, os, json, glob, html
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB=os.path.join(BASE,"public")
BOOKS=("Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|1 Samuel|2 Samuel|"
 "1 Kings|2 Kings|1 Chronicles|2 Chronicles|Ezra|Nehemiah|Esther|Job|Psalm|Psalms|Proverbs|"
 "Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|"
 "Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|"
 "Acts|Romans|1 Corinthians|2 Corinthians|Galatians|Ephesians|Philippians|Colossians|"
 "1 Thessalonians|2 Thessalonians|1 Timothy|2 Timothy|Titus|Philemon|Hebrews|James|1 Peter|"
 "2 Peter|1 John|2 John|3 John|Jude|Revelation")
REF=re.compile(r"\b(%s)\s+(\d{1,3}):(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?" % BOOKS)
def pagenum(p):
    m=re.search(r"page-(\d+)",os.path.basename(p)); return int(m.group(1)) if m else None
bank={}
for f in sorted(glob.glob(f"{PUB}/*/between-sundays-page-*.html")):
    ver=os.path.basename(os.path.dirname(f)); n=pagenum(f)
    if n is None: continue
    txt=open(f,errors="ignore").read()
    meta=re.search(r'<meta name="bible-source" content="([^"]+)"',txt)
    body=html.unescape(re.sub(r"<[^>]+>"," ",re.sub(r"<(script|style)[\s\S]*?</\1>"," ",txt)))
    refs=set()
    if meta: refs.update(m.group(0) for m in REF.finditer(meta.group(1)))
    for m in REF.finditer(body):
        bk=m.group(1).replace("Psalms","Psalm")
        refs.add(f"{bk} {m.group(2)}:{m.group(3)}"+(f"-{m.group(4)}" if m.group(4) else ""))
    for r in refs:
        e=bank.setdefault(r,{"ref":r,"book":REF.match(r).group(1),"pages":set(),"versions":set()})
        e["pages"].add(n); e["versions"].add(ver)
out=[]
for r,e in bank.items():
    m=REF.match(r)
    out.append({"ref":r,"book":e["book"],"chapter":int(m.group(2)),"verse":int(m.group(3)),
                "pages":sorted(e["pages"]),"versions":sorted(e["versions"])})
ORDER={b:i for i,b in enumerate(BOOKS.split("|"))}
out.sort(key=lambda x:(ORDER.get(x["book"],99),x["chapter"],x["verse"]))
os.makedirs(f"{PUB}/data",exist_ok=True)
json.dump(out,open(f"{PUB}/data/verses.json","w"))
pages=sorted({p for v in out for p in v["pages"]})
print(f"verse bank: {len(out)} distinct references across {len(pages)} pages")
dupes=[v for v in out if len(v["pages"])>1]
print(f"used on more than one page: {len(dupes)}")
for v in dupes[:8]: print("  ",v["ref"],"→ pages",v["pages"])
