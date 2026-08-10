#!/usr/bin/env python3
"""Load every workspace page in headless Chrome at desktop AND mobile widths and
report what a person would actually see: JS errors, empty renders, horizontal
overflow, broken images, and any lingering lock state. Spot-checking missed all
of this; this does not."""
import json, subprocess, time, os, sys, urllib.request
import websocket
BASE = sys.argv[1] if len(sys.argv) > 1 else "https://bts-workspace.vercel.app"
PAGES = ["/", "/queue.html", "/well.html", "/seed.html?id=chosen", "/build.html",
         "/spread.html", "/control-room.html", "/room.html?p=7", "/compare.html",
         "/library.html", "/verse-bank.html", "/issue-template.html", "/grow.html",
         "/atlas.html", "/territory.html?id=faith-at-home", "/persona.html?id=quiet-seeker",
         "/desk.html", "/signals.html", "/message-lab.html", "/operate.html",
         "/printer-brief.html", "/decisions.html", "/finance.html", "/company.html",
         "/brain.html", "/how-we-work.html", "/inbox.html", "/activity.html",
         "/space.html?s=merch", "/space.html?s=growth"]
VIEWS = [("desktop", 1440, 900), ("mobile", 390, 844)]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9351
PROF = "/private/tmp/claude-501/-Users-adrianmarcus-ADMC-Brain/9dc2d67a-0fc3-475a-a7cc-75584c9b0a19/scratchpad/auditprof"
proc = subprocess.Popen([CHROME, "--headless=new", f"--remote-debugging-port={PORT}",
    f"--user-data-dir={PROF}", "--disable-gpu", "--hide-scrollbars",
    "--remote-allow-origins=*"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(3)
tabs = None
for _ in range(25):
    try:
        tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")); break
    except Exception: time.sleep(1)
ws = websocket.create_connection([t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"],
                                 timeout=90)
mid = [0]; errors = []
def cmd(m, p=None):
    mid[0] += 1
    ws.send(json.dumps({"id": mid[0], "method": m, "params": p or {}}))
    while True:
        r = json.loads(ws.recv())
        if r.get("method") == "Runtime.exceptionThrown":
            d = r["params"]["exceptionDetails"]
            errors.append(d.get("exception", {}).get("description") or d.get("text"))
        if r.get("id") == mid[0]:
            return r.get("result", {})
cmd("Page.enable"); cmd("Runtime.enable")
PROBE = """(()=>{const b=document.body;
 const txt=(b.innerText||"").trim();
 const imgs=[...document.images];
 return {
  chars: txt.length,
  hoverflow: Math.max(0, b.scrollWidth - window.innerWidth),
  imgsTotal: imgs.filter(i=>i.getAttribute('src')).length,
  imgsBroken: imgs.filter(i=>i.getAttribute('src') && i.complete && i.naturalWidth===0).length,
  locked: /(^|\\s)Locked\\.?(\\s|$)/.test(txt) || /Sign in above/.test(txt),
  signinOpen: !!document.querySelector("#signin.on"),
  emptyTables: [...document.querySelectorAll("table tbody")].filter(t=>!t.children.length).length,
  title: document.title
 };})()"""
rows = []
for path in PAGES:
    for name, w, h in VIEWS:
        cmd("Emulation.setDeviceMetricsOverride",
            {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": name == "mobile"})
        errors.clear()
        cmd("Page.navigate", {"url": BASE + path}); time.sleep(2.6)
        for _ in range(20):
            if cmd("Runtime.evaluate", {"expression": "document.readyState==='complete'"}).get("result", {}).get("value"):
                break
            time.sleep(0.4)
        time.sleep(1.4)
        r = cmd("Runtime.evaluate", {"expression": PROBE, "returnByValue": True}).get("result", {}).get("value", {})
        r = r or {}
        flags = []
        if errors: flags.append("JS:" + errors[0][:58].replace("\n", " "))
        if r.get("chars", 0) < 320: flags.append(f"THIN {r.get('chars',0)}ch")
        if r.get("hoverflow", 0) > 4: flags.append(f"HSCROLL +{r['hoverflow']}px")
        if r.get("imgsBroken"): flags.append(f"IMG {r['imgsBroken']}/{r['imgsTotal']} broken")
        if r.get("locked"): flags.append("LOCKED")
        if r.get("signinOpen"): flags.append("SIGNIN")
        if r.get("emptyTables"): flags.append(f"{r['emptyTables']} empty table")
        rows.append((path, name, flags))
        print(("  OK   " if not flags else "  FAIL ") + f"{path:38s} {name:8s} " + " · ".join(flags))
bad = [r for r in rows if r[2]]
print(f"\n{len(rows)-len(bad)}/{len(rows)} page-views clean")
try: ws.close()
except Exception: pass
proc.terminate()
sys.exit(1 if bad else 0)
