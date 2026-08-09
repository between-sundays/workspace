#!/usr/bin/env python3
"""
THE SOURCE RULE, enforced: every page must cite at least one Bible verse.
Scans built page HTML for book-name + chapter references. Exit 1 if none.
Usage: python3 check_sourced.py <file-or-dir> [...]
"""
import re, sys, os, html
BOOKS=("Genesis|Gen|Exodus|Ex|Leviticus|Lev|Numbers|Num|Deuteronomy|Deut|Joshua|Josh|Judges|Ruth|"
"1 Samuel|1 Sam|2 Samuel|2 Sam|1 Kings|1 Kgs|2 Kings|2 Kgs|1 Chronicles|2 Chronicles|Ezra|Nehemiah|"
"Esther|Job|Psalms|Psalm|Ps|Proverbs|Prov|Ecclesiastes|Eccl|Song of Solomon|Isaiah|Isa|Jeremiah|Jer|"
"Lamentations|Lam|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Hab|Zephaniah|"
"Haggai|Zechariah|Zech|Malachi|Matthew|Matt|Mark|Luke|John|Jn|Acts|Romans|Rom|1 Corinthians|1 Cor|"
"2 Corinthians|2 Cor|Galatians|Gal|Ephesians|Eph|Philippians|Phil|Colossians|Col|1 Thessalonians|"
"1 Thess|2 Thessalonians|1 Timothy|2 Timothy|Titus|Philemon|Hebrews|Heb|James|Jas|1 Peter|1 Pet|"
"2 Peter|2 Pet|1 John|1 Jn|2 John|3 John|Jude|Revelation|Rev")
PAT=re.compile(r"\b(?:"+BOOKS+r")\.?\s*[-–]?\s*\d+(?:\s*[:.]\s*\d+)?",re.I)
def refs(path):
    t=open(path,encoding="utf-8",errors="replace").read()
    m=re.search(r'name="bible-source" content="([^"]+)"',t)
    meta=[m.group(1)] if m else []
    t=re.sub(r"<script.*?</script>|<style.*?</style>","",t,flags=re.S)
    t=html.unescape(re.sub(r"<[^>]+>"," ",t))
    return meta+PAT.findall(t)
targets=[]
for a in sys.argv[1:]:
    if os.path.isdir(a):
        targets+=sorted(f"{a}/{f}" for f in os.listdir(a) if re.match(r"between-sundays-page-\d+\.html$",f))
    else: targets.append(a)
fail=0
for p in targets:
    r=refs(p)
    tag=os.path.basename(p)
    if r: print(f"  SOURCED  {tag:38s} {len(r):3d} refs  e.g. {', '.join(dict.fromkeys(r[:3]))}")
    else: print(f"  ✗ UNSOURCED  {tag} — NO BIBLE REFERENCE FOUND"); fail=1
sys.exit(fail)
