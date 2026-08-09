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
if bad or html_bad:
    sys.exit(1)
print("all inline page scripts parse")
