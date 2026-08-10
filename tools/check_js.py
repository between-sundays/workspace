#!/usr/bin/env python3
"""Every browser and API JS file must parse. A syntax error in public/_nav.js blanks
the entire workspace, which is exactly how it shipped once. Never again."""
import subprocess, glob, sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(f"{BASE}/public/*.js") + glob.glob(f"{BASE}/api/*.js")
               + glob.glob(f"{BASE}/api/_handlers/*.js"))
bad = []
for f in files:
    r = subprocess.run(["node", "--check", f], capture_output=True, text=True)
    if r.returncode != 0:
        bad.append((os.path.relpath(f, BASE), r.stderr.strip().splitlines()[-1] if r.stderr else "?"))
for f, e in bad:
    print(f"FAIL {f}: {e}")
print(f"{len(files) - len(bad)}/{len(files)} JS files parse")
# Inline <script> blocks in the HTML pages, too.
import re
html_bad = []
for f in sorted(glob.glob(f"{BASE}/public/*.html")):
    src = open(f, errors="ignore").read()
    for m in re.finditer(r"<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>", src):
        r = subprocess.run(["node", "--check", "-"], input=m.group(1), capture_output=True, text=True)
        if r.returncode != 0:
            html_bad.append((os.path.relpath(f, BASE),
                             r.stderr.strip().splitlines()[-1] if r.stderr else "?"))
            break
for f, e in html_bad:
    print(f"FAIL {f} (inline script): {e}")
# A page's inline script runs in the SAME global scope as _nav.js. Redeclaring
# anything _nav.js already declares throws before a single line executes and the
# page renders empty — which is exactly how the Control Room shipped blank.
nav = open(f"{BASE}/public/_nav.js", errors="ignore").read()
navnames = set(re.findall(r"^(?:const|let|var|function)\s+([A-Za-z_$][\w$]*)", nav, re.M))
clash = []
for f in sorted(glob.glob(f"{BASE}/public/*.html")):
    src = open(f, errors="ignore").read()
    if "_nav.js" not in src:
        continue
    for m in re.finditer(r"<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>", src):
        names = set(re.findall(r"^(?:const|let|function)\s+([A-Za-z_$][\w$]*)", m.group(1), re.M))
        hit = sorted(names & navnames)
        if hit:
            clash.append((os.path.relpath(f, BASE), hit))
for f, names in clash:
    print(f"FAIL {f}: redeclares {', '.join(names)} — already defined in _nav.js")
if bad or html_bad or clash:
    sys.exit(1)
print("all inline page scripts parse, and none collide with _nav.js")
