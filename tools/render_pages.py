#!/usr/bin/env python3
"""
Render Between Sundays page HTML -> full-bleed review JPGs.
Each page renders in its OWN Chrome process so no CSS leaks between pages.
Usage:  python3 render_pages.py <dir> [pageNN ...]
"""
import re, os, sys, glob, subprocess, uuid
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

W, H = 941, 1346
PW, PH = W / 96, H / 96
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE = os.path.dirname(os.path.abspath(__file__))
WORKERS = 6

def strip_globals(css):
    # ONLY @page is stripped. Do NOT strip body/html rules — the page's body{}
    # carries font-family for everything that inherits, and deleting it silently
    # rendered the whole issue in Chrome's default serif instead of Bricolage.
    # OVERRIDE below already neutralises body layout via !important.
    out, i = [], 0
    while True:
        m = re.search(r'(?m)^\s*@page\s*\{', css[i:])
        if not m:
            out.append(css[i:]); break
        s = i + m.start()
        out.append(css[i:s])
        j = css.index("{", s); depth = 1
        while depth and j + 1 < len(css):
            j += 1
            if css[j] == "{": depth += 1
            elif css[j] == "}": depth -= 1
        i = j + 1
    return "".join(out)

OVERRIDE = """
<style>
  @page{size:%.4fin %.4fin;margin:0}
  html,body{margin:0!important;padding:0!important;background:#fff!important;
    display:block!important;place-items:initial!important}
  .page{position:relative!important;width:%dpx!important;height:%dpx!important;
    margin:0!important;box-shadow:none!important;overflow:hidden!important}
</style>""" % (PW, PH, W, H)

def one(args):
    d, f, n = args
    src = open(f).read()
    doc = re.sub(r"<style>(.*?)</style>",
                 lambda m: "<style>" + strip_globals(m.group(1)) + "</style>",
                 src, flags=re.S)
    doc = doc.replace("</head>", OVERRIDE + "</head>") if "</head>" in doc else doc + OVERRIDE
    uid = uuid.uuid4().hex[:8]
    tmp = os.path.join(d, "_r%s.html" % uid)
    pdf = os.path.join(d, "_r%s.pdf" % uid)
    open(tmp, "w").write(doc)
    try:
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        # fonts are embedded base64 with font-display:swap — without a virtual
                        # time budget Chrome prints BEFORE they decode and silently falls back
                        # to a system serif. Bit us on p18 (Shantell) and p02 (Bricolage).
                        "--virtual-time-budget=8000", "--run-all-compositor-stages-before-draw",
                        "--print-to-pdf=%s" % pdf, "file://%s" % tmp],
                       capture_output=True, timeout=420)
        subprocess.run(["pdftoppm", "-png", "-r", "132", "-f", "1", "-l", "1",
                        pdf, os.path.join(d, "_r%s" % uid)], capture_output=True, timeout=420)
        shot = os.path.join(d, "_r%s-1.png" % uid)
        if not os.path.exists(shot):
            return "  FAIL p%s" % n
        im = Image.open(shot).convert("RGB")
        if im.width > 1300:
            im = im.resize((1300, int(im.height * 1300 / im.width)), Image.LANCZOS)
        im.save(os.path.join(d, "BetweenSundays-Issue001-Page%s-Review.jpg" % n),
                "JPEG", quality=87, optimize=True, progressive=True)
        os.remove(shot)
        return "  p%s  %dx%d  %.3f" % (n, im.size[0], im.size[1], im.size[0]/im.size[1])
    finally:
        for p in (tmp, pdf):
            if os.path.exists(p):
                try: os.remove(p)
                except OSError: pass
        subprocess.run(["rm", "-rf", "/tmp/bts-%s" % uid], capture_output=True)

def render(dirpath, pages=None):
    d = os.path.join(BASE, "public", dirpath)
    files = sorted(glob.glob(os.path.join(d, "between-sundays-page-[0-9][0-9].html")))
    jobs = []
    for f in files:
        n = re.search(r"page-(\d+)", os.path.basename(f)).group(1).zfill(2)
        if pages and n not in set("%02d" % int(p) for p in pages):
            continue
        jobs.append((d, f, n))
    if not jobs:
        print("no pages found"); return
    print("%s: rendering %d pages, %d at a time" % (dirpath, len(jobs), WORKERS))
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for line in ex.map(one, jobs):
            print(line)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2:] or None)
