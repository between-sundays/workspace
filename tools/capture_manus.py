#!/usr/bin/env python3
"""
Capture Manus's pages EXACTLY as published. No CSS injection, no @page rewriting,
no DOM edits — we only navigate, wait for fonts/images, measure the .bs-page box,
and screenshot that rectangle. The design is untouched.
"""
import json, subprocess, time, base64, os, sys, urllib.request
import websocket
from PIL import Image
import io

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=9333
PROF="/private/tmp/claude-501/-Users-adrianmarcus-ADMC-Brain/9dc2d67a-0fc3-475a-a7cc-75584c9b0a19/scratchpad/chromeprof"
BASE="https://btsdesigns-sxdnjif4.manus.space"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"public","manus")

import sys as _s
ONLY=_s.argv[1:] 
PAGES=[(f"{i:02d}", f"{BASE}/page-{i:02d}") for i in range(1,25)]
PAGES.append(("25", f"{BASE}/page-everything-jacob-carried"))
if ONLY: PAGES=[p for p in PAGES if p[0] in ONLY]

proc=subprocess.Popen([CHROME,"--headless=new",f"--remote-debugging-port={PORT}",
  f"--user-data-dir={PROF}","--disable-gpu","--hide-scrollbars",
  "--window-size=1400,1500","--force-device-scale-factor=1","--remote-allow-origins=*"],
  stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(3)
for _ in range(30):
    try:
        tabs=json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")); break
    except Exception: time.sleep(1)
else:
    print("chrome did not start"); sys.exit(1)
ws_url=[t for t in tabs if t["type"]=="page"][0]["webSocketDebuggerUrl"]
ws=websocket.create_connection(ws_url, timeout=90)
mid=[0]
def cmd(method,params=None):
    mid[0]+=1
    ws.send(json.dumps({"id":mid[0],"method":method,"params":params or {}}))
    while True:
        m=json.loads(ws.recv())
        if m.get("id")==mid[0]: return m.get("result",{})
def ev(expr):
    r=cmd("Runtime.evaluate",{"expression":expr,"returnByValue":True})
    return r.get("result",{}).get("value")

cmd("Page.enable"); cmd("Runtime.enable")
cmd("Emulation.setDeviceMetricsOverride",
    {"width":1400,"height":1500,"deviceScaleFactor":2,"mobile":False})

ok=[]
for num,url in PAGES:
    cmd("Page.navigate",{"url":url})
    time.sleep(3.5)
    for _ in range(40):
        st=ev("document.readyState==='complete' && document.fonts.status==='loaded' && "
              "[...document.images].every(i=>i.complete)")
        if st: break
        time.sleep(0.5)
    time.sleep(1.2)
    box=ev("""(function(){
      var p=document.querySelector('.bs-page');
      if(!p){ // some pages use their own outer block — take the tallest sane one, as authored
        var c=[...document.querySelectorAll('div,section,main,article')]
          .map(function(e){var r=e.getBoundingClientRect();return {e:e,r:r};})
          .filter(function(o){return o.r.width>600&&o.r.width<1100&&o.r.height>700;})
          .sort(function(a,b){return b.r.height-a.r.height;});
        if(c.length) p=c[0].e;
      }
      if(!p)return null;
      var r=p.getBoundingClientRect();
      return {x:r.x+window.scrollX,y:r.y+window.scrollY,w:r.width,h:r.height};})()""")
    if not box or box["w"]<100:
        print(f"  p{num}  NO .bs-page FOUND — skipped"); continue
    shot=cmd("Page.captureScreenshot",{"format":"png","captureBeyondViewport":True,
      "clip":{"x":box["x"],"y":box["y"],"width":box["w"],"height":box["h"],"scale":2}})
    if "data" not in shot:
        print(f"  p{num}  capture failed"); continue
    im=Image.open(io.BytesIO(base64.b64decode(shot["data"]))).convert("RGB")
    im=im.resize((1295,int(im.height*1295/im.width)), Image.LANCZOS)
    dst=os.path.join(OUT,f"BetweenSundays-Issue001-Page{num}-Review.jpg")
    im.save(dst,"JPEG",quality=90,optimize=True,progressive=True)
    print(f"  p{num}  {int(box['w'])}x{int(box['h'])} css -> {im.size[0]}x{im.size[1]}  "
          f"aspect {im.size[0]/im.size[1]:.3f}")
    ok.append(num)
ws.close(); proc.terminate()
print(f"\ncaptured {len(ok)} of {len(PAGES)} pages")
