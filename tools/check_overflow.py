#!/usr/bin/env python3
"""
Load a built page in headless Chrome and report ANY element whose content
overflows its box. Catches clipped text before it ships.
Usage: python3 check_overflow.py public/press/between-sundays-page-41.html
"""
import json, subprocess, time, os, sys, urllib.request
import websocket
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=9344
PROF="/private/tmp/claude-501/-Users-adrianmarcus-ADMC-Brain/9dc2d67a-0fc3-475a-a7cc-75584c9b0a19/scratchpad/ovprof"
path=os.path.abspath(sys.argv[1])
proc=subprocess.Popen([CHROME,"--headless=new",f"--remote-debugging-port={PORT}",
  f"--user-data-dir={PROF}","--disable-gpu","--hide-scrollbars","--remote-allow-origins=*",
  "--window-size=1200,1500"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(3)
for _ in range(25):
    try: tabs=json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json")); break
    except Exception: time.sleep(1)
ws=websocket.create_connection([t for t in tabs if t["type"]=="page"][0]["webSocketDebuggerUrl"],timeout=60)
mid=[0]
def cmd(m,p=None):
    mid[0]+=1; ws.send(json.dumps({"id":mid[0],"method":m,"params":p or {}}))
    while True:
        r=json.loads(ws.recv())
        if r.get("id")==mid[0]: return r.get("result",{})
cmd("Page.enable"); cmd("Runtime.enable")
cmd("Page.navigate",{"url":"file://"+path}); time.sleep(3.5)
for _ in range(30):
    if cmd("Runtime.evaluate",{"expression":"document.readyState==='complete'&&document.fonts.status==='loaded'",
        "returnByValue":True}).get("result",{}).get("value"): break
    time.sleep(0.4)
time.sleep(1)
js="""(function(){
 var out=[];
 document.querySelectorAll('.page *').forEach(function(e){
   var cs=getComputedStyle(e);
   if(cs.overflow==='visible'&&cs.overflowY==='visible') return;
   var dy=e.scrollHeight-e.clientHeight, dx=e.scrollWidth-e.clientWidth;
   if(dy>2||dx>2){
     out.push({tag:e.tagName,cls:(e.className||'').toString().slice(0,40),
       overflowY:dy,overflowX:dx,text:(e.innerText||'').replace(/\\s+/g,' ').slice(0,70)});
   }});
 // also: any text node sitting past the page box
 var pg=document.querySelector('.page').getBoundingClientRect();
 document.querySelectorAll('.page *').forEach(function(e){
   var r=e.getBoundingClientRect();
   if(r.height>0&&(r.bottom>pg.bottom+1||r.right>pg.right+1)){
     out.push({tag:e.tagName,cls:(e.className||'').toString().slice(0,40),
       overflowY:Math.round(r.bottom-pg.bottom),overflowX:Math.round(r.right-pg.right),
       text:'PAST PAGE EDGE: '+(e.innerText||'').replace(/\\s+/g,' ').slice(0,50)});
   }});
 // COLLISION: only LEAF text blocks, and never inside a multi-column flow
 // (CSS columns make sibling paragraphs share a union bounding box — false positive)
 function inColumns(e){ for(var n=e;n&&n!==document.body;n=n.parentElement){
   var c=getComputedStyle(n).columnCount; if(c&&c!=='auto') return true; } return false; }
 function leafText(e){
   if(!e.children.length) return (e.innerText||'').trim();
   var t=''; for(var i=0;i<e.childNodes.length;i++){
     if(e.childNodes[i].nodeType===3) t+=e.childNodes[i].textContent; }
   return t.trim(); }
 var blocks=[].slice.call(document.querySelectorAll('.page p,.page li,.page h1,.page h2,.page h3,.page span,.page div'))
   .filter(function(e){ return leafText(e).length>10 && !inColumns(e)
     && e.getBoundingClientRect().height>6 && getComputedStyle(e).position!=='absolute'; });
 for(var i=0;i<blocks.length;i++){
  for(var j=i+1;j<blocks.length;j++){
   var a=blocks[i],b=blocks[j];
   if(a.contains(b)||b.contains(a)) continue;
   var ra=a.getBoundingClientRect(), rb=b.getBoundingClientRect();
   var ox=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left);
   var oy=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);
   if(ox>8&&oy>8){
     out.push({tag:'COLLISION',cls:(a.className||'?')+' x '+(b.className||'?'),
       overflowY:Math.round(oy),overflowX:Math.round(ox),
       text:leafText(a).replace(/\s+/g,' ').slice(0,32)+'  ||  '+leafText(b).replace(/\s+/g,' ').slice(0,32)});
   }}}
 return JSON.stringify(out);})()"""
res=cmd("Runtime.evaluate",{"expression":js,"returnByValue":True}).get("result",{}).get("value","[]")
ws.close(); proc.terminate()
bad=json.loads(res)
if not bad: print(f"CLEAN — no clipped or overflowing elements in {os.path.basename(path)}")
else:
    print(f"{len(bad)} OVERFLOW(S) in {os.path.basename(path)}:")
    for b in bad: print(f"  <{b['tag']} class='{b['cls']}'> +{b['overflowY']}px tall  |  {b['text']}")
    sys.exit(1)
