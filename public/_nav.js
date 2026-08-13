/* Between Sundays HQ — shared structure. One source for nav, hubs and blank spaces. */
const ICONS={
 hq:'<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/>',
 well:'<path d="M4 8h16"/><path d="M6 8v11a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V8"/><path d="M12 3v5"/>',
 build:'<path d="M4 4h16v16H4z"/><path d="M4 9h16"/><path d="M9 9v11"/>',
 grow:'<path d="M3 17l5-5 4 3 8-8"/><path d="M15 7h5v5"/>',
 operate:'<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/>',
 finance:'<path d="M12 2v20"/><path d="M17 6H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 company:'<path d="M4 21V6l8-4 8 4v15"/><path d="M9 21v-7h6v7"/>',
 inbox:'<path d="M3 12h5l2 3h4l2-3h5"/><path d="M5 5h14l2 7v7H3v-7z"/>',
 activity:'<path d="M3 12h4l3 8 4-16 3 8h4"/>',
 book:'<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M18 20a2 2 0 0 0 2-2V6"/>'};
const RAIL=[
 {id:"index", href:"/", icon:"hq", label:"HQ"},
 {id:"queue", href:"/queue.html", icon:"activity", label:"Decisions"},
 {id:"well",  href:"/well.html", icon:"well", label:"The Well"},
 {id:"build", href:"/build.html", icon:"build", label:"Build", children:[
   {id:"spread",  href:"/spread.html",       label:"Anchor spreads"},
   {id:"issue",   href:"/control-room.html", label:"The Newspaper"},
   {id:"library", href:"/library.html",      label:"Reference Library"},
   {id:"sources", href:"/sources.html",      label:"Source Systems"},
   {id:"verses",  href:"/verse-bank.html",   label:"Verse Bank"},
   {id:"template",href:"/issue-template.html",label:"Issue Template"},
   {id:"assets",  href:"/space.html?s=assets", label:"Design System & Assets"}]},
 {id:"grow", href:"/grow.html", icon:"grow", label:"Grow", children:[
   {id:"atlas",  href:"/atlas.html",  label:"Audience Atlas"},
   {id:"desk",   href:"/desk.html",   label:"Relationship Desk"},
   {id:"signals",href:"/signals.html",label:"The Signal List"},
   {id:"lab",    href:"/message-lab.html", label:"Message Lab"}]},
 {id:"operate", href:"/operate.html", icon:"operate", label:"Operate", children:[
   {id:"printer",  href:"/printer-brief.html", label:"Printer Brief"},
   {id:"decisions",href:"/decisions.html",     label:"Decision Log"},
   {id:"risks",    href:"/space.html?s=risks",     label:"Risks & blockers"}]},
 {id:"company", href:"/company.html", icon:"company", label:"Company", children:[
   {id:"believe",href:"/brain.html",      label:"What We Believe"},
   {id:"how",    href:"/how-we-work.html",label:"How We Work"}]},
 {id:"inbox",   href:"/inbox.html",   icon:"inbox",    label:"Inbox"},
 {id:"activity",href:"/activity.html",icon:"activity", label:"Activity"}];
const PILLARS=[
 {id:"build",   label:"Build",   href:"/build.html",   blurb:"Everything used to make what we publish."},
 {id:"operate", label:"Operate", href:"/operate.html", blurb:"Everything needed to run the company reliably."},
 {id:"grow",    label:"Grow",    href:"/grow.html",    blurb:"Finding, serving and keeping an audience."},
 {id:"finance", label:"Finance", href:"/finance.html", blurb:"What it costs, what it earns, what it becomes."},
 {id:"company", label:"Company", href:"/company.html", blurb:"The shared understanding behind every decision."}];
/* Rooms. live:true = built. Otherwise it renders as an honest blank space. */
const ROOMS=[
 // ---- BUILD ----
 {p:"build",id:"issue",label:"Issue 001 — the flatplan",href:"/control-room.html",live:1,
  d:"All 48 slots: versions, briefs, notes, scores, finals."},
 {p:"build",id:"compare",label:"Page-by-page comparison",href:"/compare.html",live:1,
  d:"Every version of every page, side by side."},
 {p:"build",id:"well",label:"The Well",href:"/well.html",live:1,
  d:"The drop space. Raw words and thoughts, built on by everyone, pulled into future work."},
 {p:"build",id:"spread",label:"Anchor spreads",href:"/spread.html",live:1,
  d:"The spreads that set the standard. Anchor 1 is The Reading, pages 07-08."},
 {p:"build",id:"sources",label:"Source Systems",href:"/sources.html",live:1,
  d:"Where pages come from — miracles, numbers, questions, places, names. Start at the text."},
 {p:"build",id:"library",label:"Reference Library",href:"/library.html",live:1,
  d:"Every newspaper we design against, and exactly what to take from each one."},
 {p:"build",id:"verses",label:"Verse Bank",href:"/verse-bank.html",live:1,
  d:"Every scripture printed in the issue, and where it lands."},
 {p:"build",id:"template",label:"The Issue Template",href:"/issue-template.html",live:1,
  d:"Which pages repeat, which rotate, which are open. The cadence machine."},
 {p:"build",id:"merch",label:"Merch Lab",
  purpose:"Where product ideas live before they're products — mood boards, references, rough costs.",
  q:["What would someone wear because they read this paper, not because it advertises it?",
     "What can we make that carries a verse without becoming slogan-on-cotton?",
     "What's the smallest first run we'd be proud of?"],
  owner:"Unassigned",inputs:"References, sketches, supplier quotes",outputs:"A product brief"},
 {p:"build",id:"products",label:"Future Products",
  purpose:"Everything after the paper. A parking lot with a roof — nothing here is committed to.",
  q:["What does Between Sundays make that isn't a newspaper?",
     "Does the Spine work as its own object?",
     "Is there a children's or teen edition?"],
  owner:"Unassigned",inputs:"Parked ideas from anyone",outputs:"Candidates for a real brief"},
 {p:"build",id:"assets",label:"Design System &amp; Assets",
  purpose:"The press chassis, the module sizes, the halftone pipeline, and where the artwork lives.",
  q:["What is the canonical module set and where is it documented?",
     "Where do Adrian's source exports live, and at what resolution?",
     "Which fonts are licensed for commercial print?"],
  owner:"Claude",inputs:"Builders in tools/, Adrian's exports",outputs:"A reusable chassis for 002"},
 // ---- OPERATE ----
 {p:"operate",id:"printer",label:"The Printer Brief",href:"/printer-brief.html",live:1,
  d:"What we hand a printer. Verified specs, and the questions still open."},
 {p:"operate",id:"decisions",label:"Decision Log",href:"/decisions.html",live:1,
  d:"What was decided, by whom, and why — so settled questions stay settled."},
 {p:"operate",id:"logistics",label:"Logistics & Fulfillment",
  purpose:"Getting a physical object from a press into somebody's hands, intact.",
  q:["How does a broadsheet ship without arriving creased?",
     "Does the removable Spine survive transit?",
     "Who packs and who ships — us, or the printer?",
     "What does a damaged or returned copy cost us?"],
  owner:"Adrian",inputs:"Printer quotes, packaging samples",outputs:"A fulfillment plan and a per-copy cost"},
 {p:"operate",id:"vendors",label:"Partners & Vendors",
  purpose:"An operating directory — printers, packers, illustrators, churches, retailers. Not a CRM.",
  q:["Which printers can run 332 × 475 mm, and what do they charge?",
     "Who have we actually talked to, and what did they say?"],
  owner:"Adrian",inputs:"Quotes, conversations, referrals",outputs:"A shortlist with real numbers"},
 {p:"operate",id:"risks",label:"Risks & Assumptions",
  purpose:"Everything we're assuming but haven't proven. Each gets an owner and a next action.",
  q:["Known today: every placed artwork is roughly 80 dpi at trim — print needs 3921 × 5610. Who re-exports, and by when?",
     "Are the conceptual ads legally distinct from real brands?",
     "Which scripture readings still need a human context check?"],
  owner:"Claude",inputs:"Anything anyone is nervous about",outputs:"Owned, dated, closed"},
 {p:"operate",id:"cadence",label:"Company Cadence",
  purpose:"The recurring rhythms that make Issue 002 faster than Issue 001.",
  q:["When is page review day?","When is founder decision day?",
     "What happens in the week after an issue ships?"],
  owner:"Unassigned",inputs:"How 001 actually went",outputs:"A repeatable calendar"},
 {p:"operate",id:"postmortem",label:"Postmortems",
  purpose:"After every issue: what worked, what dragged, what should become a rule.",
  q:["What took far longer than it should have?",
     "What should never happen again?","What should be automated before 002?"],
  owner:"Unassigned",inputs:"The whole of Issue 001",outputs:"Rules and automation"},
 // ---- GROW ----
 {p:"grow",id:"atlas",label:"Audience Atlas",href:"/atlas.html",live:1,
  d:"Territories, persona groups, life moments and the signals that find them. The model layer."},
 {p:"grow",id:"desk",label:"Relationship Desk",href:"/desk.html",live:1,
  d:"Real people — profile links, why they fit, and where each relationship stands."},
 {p:"grow",id:"signals",label:"The Signal List",href:"/signals.html",live:1,
  d:"Every signal on one page. The brief you hand an agent before it goes looking."},
 {p:"grow",id:"lab",label:"Message Lab",href:"/message-lab.html",live:1,
  d:"Message hypotheses, what landed, what fell flat, and the words people used back."},
 {p:"grow",id:"crm",label:"CRM connection",
  purpose:"The slot for a real CRM. Deliberately empty — the Desk exports into it when it exists.",
  q:["Which CRM, and when does the Desk stop being the system of record?",
     "What's the minimum field set that has to survive the migration?"],
  owner:"Adrian",inputs:"The Desk's export",outputs:"One system of record"},
 {p:"grow",id:"gtm",label:"Go-to-Market",
  purpose:"How Issue 001 reaches its first real readers.",
  q:["Who gets it first, and how does it physically arrive?",
     "Churches, coffee shops, subscription, hand-to-hand — which is the wedge?",
     "What has to be true for a stranger to pick it up?"],
  owner:"Adrian",inputs:"Distribution conversations",outputs:"A launch plan with a number attached"},
 {p:"grow",id:"messaging",label:"Messaging",
  purpose:"What we say about ourselves, in our own voice.",
  q:["The one line that explains this to a stranger in six seconds.",
     "How do we talk about faith without sounding like a sermon?",
     "What do we never say?"],
  owner:"Unassigned",inputs:"The constitution",outputs:"A messaging sheet"},
 {p:"grow",id:"platforms",label:"Platforms & Creators",
  purpose:"Where an audience for a print paper actually gets built.",
  q:["What does a page look like as a post without becoming a post?",
     "Who else makes something we'd be proud to sit beside?",
     "What does a contributor get from appearing in it?"],
  owner:"Unassigned",inputs:"Platform research",outputs:"A channel plan"},
 {p:"grow",id:"experiments",label:"Campaigns & Experiments",
  purpose:"Hypothesis, change, metric, timeline. Same as everything else Adrian runs.",
  q:["What's the first testable thing we could run before the issue prints?"],
  owner:"Unassigned",inputs:"Ideas from the Inbox",outputs:"Results worth keeping"},
 // ---- FINANCE ----
 {p:"finance",id:"unit",label:"Print Economics",
  purpose:"Cost per copy at each run length. Everything downstream depends on this.",
  q:["Cost per copy at 500 / 2,000 / 10,000?",
     "Shipping per copy and per box?","Which costs disappear in Issue 002?"],
  owner:"Adrian",inputs:"Printer quotes",outputs:"A real unit cost"},
 {p:"finance",id:"pricing",label:"Pricing",
  purpose:"What a reader pays, and what that says about us.",
  q:["What price would a reader not blink at?",
     "Single copy, subscription, bulk — which do we lead with?"],
  owner:"Adrian",inputs:"Unit cost, comparable objects",outputs:"A price"},
 {p:"finance",id:"sponsor",label:"Sponsorship",
  purpose:"The paper runs conceptual ads. Whether real sponsors ever appear is a brand decision first.",
  q:["Would a real sponsor break the voice?",
     "What would we refuse money for? Decide before someone offers."],
  owner:"Adrian",inputs:"The constitution",outputs:"A yes, a no, or a rule"},
 {p:"finance",id:"projections",label:"Projections",
  purpose:"What the next twelve months look like — after distribution is known, not before.",
  q:["A projection without a distribution assumption is a number we made up. What's the distribution answer?",
     "Cash needed before Issue 001 prints?","The number that means this works?"],
  owner:"Adrian",inputs:"Unit cost + distribution",outputs:"Base, best and worst case"},
 // ---- COMPANY ----
 {p:"company",id:"believe",label:"What We Believe",href:"/brain.html",live:1,
  d:"The constitution, the Source Rule, voice, and the design law."},
 {p:"company",id:"how",label:"How We Work",href:"/how-we-work.html",live:1,
  d:"The contributor contract — for people and agents."},
 {p:"company",id:"notdo",label:"What We Are Not",href:"/brain.html#not",live:1,
  d:"The boundaries. Not a sermon, not a study, not an app."},
 {p:"company",id:"glossary",label:"Glossary",
  purpose:"The words we use oddly — The Spine, The Reading, the press chassis, a module.",
  q:["What does a newcomer misread on their first day?"],
  owner:"Unassigned",inputs:"Confusion",outputs:"Shared language"},
];
function svg(k){return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">${ICONS[k]||""}</svg>`;}
function mount(cur,opts){
 const o=opts||{};
 const kept=document.createDocumentFragment();
 while(document.body.firstChild) kept.appendChild(document.body.firstChild);
 const me=localStorage.getItem("bts-who")||"ADRIAN";
 document.body.innerHTML=`<div class="app">
  <aside class="rail" id="rail">
   <div class="head"><div class="logo">S</div>
    <div class="wordmark"><span>Between</span><em>Sundays</em></div>
    <button class="pin" id="railpin" title="Keep the menu open">&#9776;</button></div>
   <nav>${RAIL.map(r=>{
    const kids=(r.children||[]).map(c=>
      `<a class="kid" href="${c.href}">${c.label}</a>`).join("");
    return `<div class="grp${r.id===cur?" on":""}${kids?" has":""}">
      <a class="lnk" href="${r.href}">${svg(r.icon)}<span class="lbl">${r.label}</span>
       ${kids?'<span class="car">&#8250;</span>':""}</a>
      ${kids?`<div class="kids">${kids}</div>`:""}</div>`;}).join("")}</nav>
   <div class="sp"></div>
   <div class="grp"><a class="lnk" href="/how-we-work.html">${svg("book")}
     <span class="lbl">How we work</span></a></div></aside>
  <div class="main">
   <header class="top">
    <div class="hi">Welcome to <span class="brand">Between Sundays</span> <b>HQ</b></div>
    <div class="grow"></div>
    <div class="search"><input id="gsearch" placeholder="Search the workspace\u2026"/>
     <button aria-label="Search">&#8594;</button></div>
    <button class="me" id="mebtn"><div class="av" id="avme">${me?me.slice(0,2):"+"}</div>
     <div class="who" id="whome">${me}<span>unlocked \u00b7 open mode</span></div>
    </button></header>
   <div class="page">
    <h1 class="title">${o.title||"Headquarters"}</h1>
    ${o.sub?`<p class="lede" style="margin-top:-8px">${o.sub}</p>`:""}
    <div id="__content"></div>
    <footer><span>Good news. Printed.</span>
     <a href="/how-we-work.html">How we work</a>
     <a href="/queue.html">What needs you</a></footer>
   </div></div></div>`;
 document.getElementById("__content").appendChild(kept);
 const gs=document.getElementById("gsearch");
 if(gs) gs.addEventListener("keydown",e=>{
  if(e.key==="Enter"&&e.target.value.trim())
   location.href="/search.html?q="+encodeURIComponent(e.target.value.trim());});
 const rail=document.getElementById("rail");
 if(localStorage.getItem("bts-rail")==="open") rail.classList.add("open");
 document.getElementById("railpin").onclick=()=>{
  rail.classList.toggle("open");
  localStorage.setItem("bts-rail",rail.classList.contains("open")?"open":"closed");};
 document.getElementById("mebtn").onclick=()=>signIn();
 const c=document.getElementById("__content");
 if(c && !c.textContent.trim()) c.insertAdjacentHTML("afterbegin",
  '<div id="__loading" class="blank"><div class="t">Loading</div><p>Fetching the latest from the team\u2026</p></div>');
 setTimeout(()=>{const l=document.getElementById("__loading");
  if(l && c && c.textContent.replace(l.textContent,"").trim().length>40) l.remove();},900);
 setTimeout(()=>{const l=document.getElementById("__loading"); if(l) l.remove();},6000);
 quickDrop(); addPerson();
 if(getKey()&&!localStorage.getItem("bts-who")){
  fetch("/api/whoami",{headers:{"x-agent-key":getKey()}}).then(r=>r.json()).then(j=>{
   if(j&&j.you){localStorage.setItem("bts-who",j.you);
    document.getElementById("avme").textContent=j.you.slice(0,2);
    document.getElementById("whome").firstChild.textContent=j.you;}}).catch(()=>{});}
}
/* Quick Drop — on every page in the workspace. Capture must be easier than organising. */
function quickDrop(){
 if(document.getElementById("qd")) return;
 document.body.insertAdjacentHTML("beforeend",`
  <button id="qdbtn" title="Drop a thought in The Well">Drop a thought</button>
  <div id="qd"><div class="box">
    <div class="hd">Drop it here. Draw from it later.</div>
    <textarea id="qdtxt" rows="4" placeholder="A word. A phrase. A ramble. No title needed."></textarea>
    <div class="row"><button id="qdgo">Drop it in</button>
     <button id="qdx" class="ghost">Cancel</button>
     <span id="qdmsg"></span></div>
  </div></div>`);
 const w=document.getElementById("qd");
 document.getElementById("qdbtn").onclick=()=>{
  w.classList.add("on");document.getElementById("qdtxt").focus();};
 document.getElementById("qdx").onclick=()=>w.classList.remove("on");
 w.onclick=e=>{if(e.target===w)w.classList.remove("on");};
 document.getElementById("qdgo").onclick=async()=>{
  const t=document.getElementById("qdtxt").value.trim();
  if(t.length<2){return;}
  const first=t.split(/[\n.!?]/)[0].trim();
  const word=first.length<=60?first:first.slice(0,60);
  const msg=document.getElementById("qdmsg");
  msg.textContent="dropping…";
  try{await api("seed",{word,note:t.length>word.length?t:""});
   msg.textContent="in the well ✓";
   document.getElementById("qdtxt").value="";
   setTimeout(()=>{w.classList.remove("on");msg.textContent="";},900);
  }catch{msg.textContent="";}};
 document.addEventListener("keydown",e=>{
  if(e.key==="Escape")w.classList.remove("on");});}
/* Add Person — paste a profile link anywhere in the workspace, pick the groups, done.
   An agent enriches it afterwards. Every record needs a written reason it fits. */
function addPerson(){
 if(document.getElementById("ap")) return;
 // Only where real people live — it was noise on the Verse Bank and the flatplan.
 if(!/\/(desk|atlas|persona|territory|signals|message-lab)\.html/.test(location.pathname)) return;
 document.body.insertAdjacentHTML("beforeend",`
  <button id="apbtn" title="Add a person to a group">Add person</button>
  <div id="ap"><div class="box">
   <div class="hd">Add a person</div>
   <input id="apname" placeholder="Name or @handle"/>
   <input id="apurl" placeholder="Profile URL — paste any social link"/>
   <div id="apgroups" style="margin:8px 0"></div>
   <textarea id="apwhy" rows="3" placeholder="Why do they fit? Quote the public post. Required."></textarea>
   <input id="apev" placeholder="Link(s) to the posts that prove it, comma separated"/>
   <div class="row"><button id="apgo">Add</button>
    <button id="apx" class="ghost">Cancel</button><span id="apmsg"></span></div>
  </div></div>`);
 const w=document.getElementById("ap");
 document.getElementById("apbtn").onclick=async()=>{
  const praw=(await state("personas.jsonl"))||[];
  const P={}; praw.forEach(p=>P[p.id]=p);
  document.getElementById("apgroups").innerHTML=Object.values(P).map(p=>
   `<label style="display:inline-flex;gap:5px;align-items:center;margin:0 12px 6px 0;
     font:13px var(--ser)"><input type="checkbox" value="${p.id}" style="width:auto"/>
     ${p.name}</label>`).join("")||"<em>No groups defined yet.</em>";
  w.classList.add("on"); document.getElementById("apname").focus();};
 document.getElementById("apx").onclick=()=>w.classList.remove("on");
 w.onclick=e=>{if(e.target===w)w.classList.remove("on");};
 document.getElementById("apgo").onclick=async()=>{
  const g=id=>document.getElementById(id).value.trim();
  const groups=[...document.querySelectorAll("#apgroups input:checked")].map(x=>x.value);
  const msg=document.getElementById("apmsg");
  if(!g("apname")){msg.textContent="who?";return;}
  if(!groups.length){msg.textContent="pick a group";return;}
  if(g("apwhy").length<10){msg.textContent="say why they fit";return;}
  msg.textContent="adding…";
  try{
   await api("prospect",{handle:g("apname"),persona:groups,url:g("apurl"),
    links:g("apurl")?[g("apurl")]:[],fit:g("apwhy"),signal:g("apwhy"),
    evidence:g("apev").split(",").map(x=>x.trim()).filter(Boolean),stage:"found"});
   msg.textContent="added ✓";
   ["apname","apurl","apwhy","apev"].forEach(i=>document.getElementById(i).value="");
   setTimeout(()=>{w.classList.remove("on");msg.textContent="";location.reload();},700);
  }catch{msg.textContent="";}};}

/* ---- feedback that cannot be suppressed by the browser ---- */
function toast(msg,kind){
 let t=document.getElementById("toast");
 if(!t){t=document.createElement("div");t.id="toast";document.body.appendChild(t);}
 t.textContent=msg; t.className="on"+(kind?" "+kind:"");
 clearTimeout(window.__tt); window.__tt=setTimeout(()=>t.className="",3200);
}
/* One place to sign in, reachable from anywhere. No popups. */
function signIn(msg){
 let w=document.getElementById("signin");
 if(!w){
  document.body.insertAdjacentHTML("beforeend",`
   <div id="signin"><div class="box">
    <div class="hd">Sign in to contribute</div>
    <p id="simsg">The workspace is <strong>unlocked</strong> — you do not need this. Everything you
     write is attributed to Adrian. Add a key only if you want your own name on your contributions.</p>
    <input id="sikey" placeholder="bsk_…" autocomplete="off"/>
    <div class="row"><button id="sigo">Sign in</button>
     <button id="six" class="ghost">Not now</button></div>
   </div></div>`);
  w=document.getElementById("signin");
  document.getElementById("six").onclick=()=>w.classList.remove("on");
  w.onclick=e=>{if(e.target===w)w.classList.remove("on");};
  document.getElementById("sigo").onclick=()=>{
   const v=document.getElementById("sikey").value.trim();
   if(!v){toast("Paste your key first");return;}
   localStorage.setItem(KEYST,v); localStorage.removeItem("bts-who"); location.reload();};
  document.getElementById("sikey").addEventListener("keydown",e=>{
   if(e.key==="Enter")document.getElementById("sigo").click();});
 }
 if(msg) document.getElementById("simsg").textContent=msg;
 w.classList.add("on"); setTimeout(()=>document.getElementById("sikey").focus(),40);
}
/* ---- shared key + private state ---- */
const KEYST="bts-agent-key";
function getKey(){return (localStorage.getItem(KEYST)||"").trim();}
async function state(path){
 const k=getKey();
 try{const r=await fetch("/api/state?path="+encodeURIComponent(path),
   k?{headers:{"x-agent-key":k}}:{});
  if(!r.ok) return [];
  const t=(await r.text()).trim();
  if(!t) return path.endsWith(".md")?"":[];
  if(path.endsWith(".md")) return t;
  return t.split("\n").filter(Boolean).map(l=>{try{return JSON.parse(l)}catch{return null}}).filter(Boolean);
 }catch{return [];}}
async function api(p,b){
 const r=await fetch("/api/"+p,{method:"POST",
  headers:{"content-type":"application/json","x-agent-key":getKey()},body:JSON.stringify(b)});
 const j=await r.json().catch(()=>({}));
 if(!r.ok){ if(r.status===401){signIn("That key was not recognised.");}
  else toast(j.error||("error "+r.status),"bad"); throw 0;}
 return j;}
function lockbar(){
 return "";
 return `<div class="blank">
  <div class="t">Reading as a guest</div>
  <p>Everything here is readable without signing in. Add your key to <strong>contribute</strong> —
   drop ideas, leave notes, add people, mark finals.</p>
  <p style="margin-top:10px"><input id="keyin" placeholder="bsk_…"
   style="width:320px;max-width:100%;border:1px solid var(--rule);padding:8px;font:14px var(--ser)"/>
   <button id="keygo" style="border:1px solid var(--ink);background:var(--ink);color:#fff;
    padding:9px 16px;font-family:var(--san);font-size:11px;font-weight:800;letter-spacing:.12em;
    text-transform:uppercase;cursor:pointer;margin-left:6px">Unlock</button></p></div>`;}
function wireLock(){
 const g=document.getElementById("keygo"); if(!g) return;
 g.onclick=()=>{const v=document.getElementById("keyin").value.trim();
  if(v){localStorage.setItem(KEYST,v);location.reload();}};
 document.getElementById("keyin").addEventListener("keydown",e=>{
  if(e.key==="Enter")g.click();});}
