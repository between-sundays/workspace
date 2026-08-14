#!/usr/bin/env python3
"""Reject visual monotony. Reads each built page's declared style system and
fails if the issue repeats itself. See brain/style-variance.md."""
import re, glob, os, sys, json
from collections import Counter
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = {s["id"]: s for s in json.load(open(f"{BASE}/public/data/style-register.json"))}
pages = {}
for d in ("anchor", "press2", "press", "lab"):
    for f in glob.glob(f"{BASE}/public/{d}/*page-*.html") + glob.glob(f"{BASE}/public/{d}/ref*.html"):
        src = open(f, errors="ignore").read()
        m = re.search(r'<meta name="style-system" content="([^"]+)"', src)
        n = re.search(r"page-(\d+)", os.path.basename(f))
        if not n:
            continue
        pages[int(n.group(1))] = (m.group(1) if m else None, os.path.relpath(f, BASE))
if not pages:
    print("no built pages carry a style-system declaration yet"); sys.exit(0)
bad = []
undeclared = [f"p{n:02d} ({p})" for n, (s, p) in sorted(pages.items()) if not s]
unknown = [f"p{n:02d}: '{s}'" for n, (s, p) in sorted(pages.items()) if s and s not in REG]
order = sorted(pages)
for a, b in zip(order, order[1:]):
    sa, sb = pages[a][0], pages[b][0]
    if sa and sa == sb:
        bad.append(f"p{a:02d} and p{b:02d} both use '{sa}' — consecutive pages may not share a system")
    if b == a + 1 and a % 2 == 0 and sa and sa == sb:
        bad.append(f"p{a:02d}/p{b:02d} face each other and share '{sa}'")
counts = Counter(s for s, _ in pages.values() if s)
for s, c in counts.items():
    if c > 3:
        bad.append(f"'{s}' used on {c} pages — maximum is 3 across the issue")
if len(pages) >= 24 and len(counts) < 12:
    bad.append(f"only {len(counts)} distinct systems across {len(pages)} pages — minimum is 12")
for u in undeclared:
    print(f"UNDECLARED {u} — add <meta name=\"style-system\" content=\"…\">")
for u in unknown:
    print(f"UNKNOWN    {u} — not in style-register.json")
for b in bad:
    print(f"FAIL       {b}")
print(f"\n{len(pages)} pages · {len(counts)} distinct systems · {len(undeclared)} undeclared")
sys.exit(1 if (bad or unknown) else 0)
