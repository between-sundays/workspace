/* Shared furniture for every workspace page. */
const SPACES=[
 {id:"index",   href:"/",                 label:"Front"},
 {id:"brain",   href:"/brain.html",       label:"What We Believe"},
 {id:"issue",   href:"/control-room.html",label:"Issue 001"},
 {id:"growth",  href:"/space.html?s=growth",   label:"Growth"},
 {id:"logistics",href:"/space.html?s=logistics",label:"Logistics"},
 {id:"revenue", href:"/space.html?s=revenue",  label:"Revenue"},
 {id:"products",href:"/space.html?s=products", label:"Future Products"},
 {id:"how",     href:"/how-we-work.html", label:"How We Work"},
];
function plate(cur,{kicker,title,sub}={}){
 const d=new Date().toLocaleDateString("en-US",{weekday:"long",year:"numeric",month:"long",day:"numeric"});
 return `<div class="wrap"><div class="plate">
   <div class="kicker">${kicker||"The internal workspace"}</div>
   <h1>${title||"Between Sundays"}</h1>
   <div class="sub">${sub||"Good news. Printed."}</div></div>
  <div class="dateline"><span>${d}</span><span>Issue 001 · I Am With You</span>
   <span>Adrian · Lacey · Claude · Manus · Codex</span></div>
  <nav class="spaces">${SPACES.map(s=>
    `<a href="${s.href}" class="${s.id===cur?"on":""}">${s.label}</a>`).join("")}</nav></div>`;
}
function foot(){
 return `<div class="wrap"><footer>
  <span>Between Sundays — internal. Nothing here is deleted, only added and superseded.</span>
  <span><a href="https://github.com/between-sundays/workspace">Repo</a> ·
   <a href="/archive/">Archive</a> · <a href="/how-we-work.html">Contribute</a></span>
 </footer></div>`;
}
function mount(cur,opts){
 document.body.insertAdjacentHTML("afterbegin",plate(cur,opts));
 document.body.insertAdjacentHTML("beforeend",foot());
}
