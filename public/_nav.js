/* Between Sundays HQ — shared structure. One source for nav, hubs and blank spaces. */
const PILLARS=[
 {id:"build",   label:"Build",   href:"/build.html",
  blurb:"Everything used to make what we publish."},
 {id:"operate", label:"Operate", href:"/operate.html",
  blurb:"Everything needed to run the company reliably."},
 {id:"grow",    label:"Grow",    href:"/grow.html",
  blurb:"Finding, serving and keeping an audience."},
 {id:"finance", label:"Finance", href:"/finance.html",
  blurb:"What it costs, what it earns, what it becomes."},
 {id:"company", label:"Company", href:"/company.html",
  blurb:"The shared understanding behind every decision."},
];
const EXTRA=[{id:"well",label:"The Well",href:"/well.html"},
             {id:"inbox",label:"Inbox",href:"/inbox.html"},
             {id:"activity",label:"Activity",href:"/activity.html"}];
/* Rooms. live:true = built. Otherwise it renders as an honest blank space. */
const ROOMS=[
 // ---- BUILD ----
 {p:"build",id:"issue",label:"Issue 001 — the flatplan",href:"/control-room.html",live:1,
  d:"All 48 slots: versions, briefs, notes, scores, finals."},
 {p:"build",id:"compare",label:"Page-by-page comparison",href:"/compare.html",live:1,
  d:"Every version of every page, side by side."},
 {p:"build",id:"well",label:"The Well",href:"/well.html",live:1,
  d:"The drop space. Raw words and thoughts, built on by everyone, pulled into future work."},
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
 {p:"build",id:"assets",label:"Design System & Assets",
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
 {p:"grow",id:"personas",label:"Persona Groups",href:"/personas.html",live:1,
  d:"The collections of people we're going after, one by one, with the signals that find them."},
 {p:"grow",id:"prospects",label:"Prospect List",href:"/prospects.html",live:1,
  d:"Named people, the public signal that flagged them, and where each one stands."},
 {p:"grow",id:"gtm",label:"Go-to-Market",
  purpose:"How Issue 001 reaches its first real readers.",
  q:["Who gets it first, and how does it physically arrive?",
     "Churches, coffee shops, subscription, hand-to-hand — which is the wedge?",
     "What has to be true for a stranger to pick it up?"],
  owner:"Adrian",inputs:"Distribution conversations",outputs:"A launch plan with a number attached"},
__NOPE__label:"Audience & Personas",
  purpose:"Who this is for. Start with the founder: the reader who never liked reading.",
  q:["Who buys it for someone else?","Who hands it out in bulk?",
     "Who is suspicious of church but curious about God?"],
  owner:"Manus",inputs:"Real conversations, not invented profiles",outputs:"Persona cards"},
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
function plate(cur,{kicker,title,sub}={}){
 const d=new Date().toLocaleDateString("en-US",{weekday:"long",year:"numeric",month:"long",day:"numeric"});
 const well=EXTRA[0];
 const nav=[{id:"index",label:"HQ",href:"/"},well,...PILLARS,...EXTRA.slice(1)];
 return `<div class="wrap"><div class="plate">
   <div class="kicker">${kicker||"Between Sundays HQ"}</div>
   <h1>${title||"Between Sundays"}</h1>
   <div class="sub">${sub||"Good news. Printed."}</div></div>
  <div class="dateline"><span>${d}</span><span>Issue 001 · I Am With You</span>
   <span>Adrian · Lacey · Claude · Manus · Codex</span></div>
  <nav class="spaces">${nav.map(s=>
    `<a href="${s.href}" class="${s.id===cur?"on":""}">${s.label}</a>`).join("")}</nav></div>`;
}
function foot(){return `<div class="wrap"><footer>
  <span>Between Sundays — internal. Nothing is deleted, only added and superseded.</span>
  <span><a href="https://github.com/between-sundays/workspace">Repo</a> ·
   <a href="/archive/site-index-legacy.html">Archive</a> ·
   <a href="/how-we-work.html">Contribute</a></span></footer></div>`;}
function mount(cur,opts){
 document.body.insertAdjacentHTML("afterbegin",plate(cur,opts));
 document.body.insertAdjacentHTML("beforeend",foot());
 quickDrop();}
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
  if(!getKey()){alert("Enter your workspace key on any page first.");return;}
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
/* ---- shared key + private state ---- */
const KEYST="bts-agent-key";
function getKey(){return (localStorage.getItem(KEYST)||"").trim();}
async function state(path){
 const k=getKey(); if(!k) return null;
 try{const r=await fetch("/api/state?path="+encodeURIComponent(path),{headers:{"x-agent-key":k}});
  if(r.status===401) return null;
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
 if(!r.ok){alert(j.error||("error "+r.status));throw 0;}
 return j;}
function lockbar(){
 if(getKey()) return "";
 return `<div class="blank"><div class="t">Locked</div>
  <p>Page renders are public. Notes, briefs, scores, finals and the business spaces are private.
   Paste your workspace key to unlock them — it stays in this browser.</p>
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
