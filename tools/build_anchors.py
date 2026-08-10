#!/usr/bin/env python3
"""The seven anchors, built against the grid approved with Anchor 1."""
import json,re,html,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from anchor_chassis import *
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(B,"public","anchor")
V=json.load(open(os.path.join(B,"tools","anchor-verses-nlt.json")))
def txt(book,v):
    for x in V[book]:
        if x["verse"]==v: return re.sub(r"<[^>]+>","",html.unescape(x["text"])).strip()
    return ""
G=lambda v: txt("gen28",v)

# ───────────────────────── p01 COVER ─────────────────────────
teas_top=[("Genesis 28","The night Jacob slept on a stone","07"),
          ("Words & meaning","Bethel, Luz, and a ramp to heaven","16"),
          ("Games","Find the certain place","32"),
          ("But God","210 verses, sorted by what's wrong","34")]
teas_bot=[("Weather","Forecast for the middle","20"),
          ("Music","Songs for walking home","40"),
          ("Write it down","One page. One question.","43"),
          ("Coupons","Redeemable at no cost","22")]
def strip(items,top):
    w=(941-104)/4
    out=[]
    for i,(k,t,p) in enumerate(items):
        x=52+i*w
        out.append(f'''<div style="position:absolute;left:{x:.0f}px;top:{top}px;width:{w-16:.0f}px">
         <div class="kicker" style="font-size:9.5px;letter-spacing:.18em">{k}</div>
         <div style="font-size:15.5px;line-height:1.24;margin-top:6px;font-weight:500">{t}</div>
         <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.13em;
          margin-top:8px;color:rgba(44,26,18,.55)">PAGE {p}</div></div>''')
        if i: out.append(f'<div style="position:absolute;left:{x-8:.0f}px;top:{top}px;width:1px;'
                         f'height:78px;background:rgba(44,26,18,.22)"></div>')
    return "".join(out)
steps="".join(
 f'<div style="position:absolute;left:{372+i*58}px;top:{1040-i*54}px;width:{240-i*9}px;height:13px;'
 f'background:{CREAM}"></div>'
 f'<div style="position:absolute;left:{372+i*58}px;top:{1053-i*54}px;width:{240-i*9}px;height:41px;'
 f'background:rgba(44,26,18,.10)"></div>' for i in range(9))
p01=page("01","Genesis 28:16 (NLT)",f"""
 <div class="field" style="background:{BUT}"></div>
 <div class="arc" style="width:430px;height:430px;right:-130px;top:470px;background:{SKY};opacity:.55"></div>
 {steps}
 <div style="position:absolute;left:52px;right:52px;top:30px;text-align:center">
  <div class="kicker" style="font-size:10px">Issue 001 &nbsp;·&nbsp; Good news. Printed.</div>
  <div style="font-family:'Playfair Display',serif;font-size:92px;font-weight:700;line-height:.9;
   letter-spacing:-.03em;margin-top:8px">Between</div>
  <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:112px;font-weight:700;
   line-height:.82;letter-spacing:-.03em;margin-top:-6px">Sundays</div>
  <div class="kicker" style="font-size:9.5px;margin-top:14px;color:rgba(44,26,18,.6)">
   A newspaper for the days in between &nbsp;·&nbsp; 48 pages</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:330px;height:1px;background:{BR}"></div>
 {strip(teas_top,346)}
 <div style="position:absolute;left:52px;right:52px;top:444px;height:1px;background:rgba(44,26,18,.35)"></div>
 <div style="position:absolute;left:52px;top:500px;width:560px">
  <div class="kicker" style="color:{NAVY}">I am with you</div>
  <div class="display" style="font-size:56px;margin-top:12px">Surely the LORD<br/>is in this place,<br/>
   <em>and I wasn&rsquo;t even<br/>aware of it.</em></div>
  <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.15em;
   margin-top:18px;color:rgba(44,26,18,.6)">GENESIS 28:16 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
  <div style="font-size:18.5px;line-height:1.44;margin-top:20px;width:452px">He was running for his
   life and stopped because it got dark. He picked a rock for a pillow. Nothing about the place was
   special, and God was already there.</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:1156px;height:1px;background:rgba(44,26,18,.35)"></div>
 {strip(teas_bot,1174)}
 <div class="credit" style="left:52px;bottom:24px">Between Sundays · Issue 001 · I Am With You</div>
 <div class="credit" style="right:52px;bottom:24px">Free. Take one.</div>
""","Cover")

# ───────────────────────── p02 CONTENTS ─────────────────────────
SEC=[("The Reading","07–13","Genesis 28, printed in full, with room to breathe."),
     ("Words &amp; Meaning","16–17","Five words, defined plainly. No assumed knowledge."),
     ("Field guide","17","One idea taken apart visually."),
     ("Sports · Weather · Movies","19–21","The desks you already know, read through the theme."),
     ("Obituaries &amp; Coupons","22","Yes, really. Both are about what is still redeemable."),
     ("The Spine","23–26","A removable section. Lift it out and keep it."),
     ("Comics &amp; Games","30–32","A crossword, a connect-the-dots, and a place to get lost."),
     ("But God","33–35","210 verses, sorted by what is actually wrong."),
     ("Write it down","43","One page. One question. Room for your handwriting."),
     ("Where this paper went","46–48","And what is coming next.")]
rows="".join(f'''<div style="display:flex;gap:16px;align-items:baseline;padding:11px 0;
 border-bottom:1px solid rgba(44,26,18,.16)">
 <div style="font-family:'Playfair Display',serif;font-size:21px;font-weight:700;width:96px;
  flex:0 0 96px;color:{NAVY}">{p}</div>
 <div style="flex:1"><div style="font-size:19px;font-weight:600;line-height:1.2">{t}</div>
  <div style="font-size:14px;color:rgba(44,26,18,.66);margin-top:3px">{d}</div></div></div>'''
 for t,p,d in SEC)
p02=page("02","Genesis 28:15 (NLT)",f"""
 {folio("02","Contents",left=False)}
 <div style="position:absolute;left:52px;top:96px;width:560px">
  <div class="kicker">What is in here</div>
  <div class="display" style="font-size:46px;margin-top:10px">A field guide<br/>to the middle
   <em>of the week.</em></div>
  <div style="margin-top:22px">{rows}</div>
 </div>
 <div style="position:absolute;right:52px;top:96px;width:250px">
  <div style="background:{SKY};padding:18px 20px 20px">
   <div class="lab">Start anywhere</div>
   <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;line-height:1.14;
    margin-top:7px">No page needs the page before it.</div>
   <div style="font-size:13.6px;line-height:1.45;margin-top:7px">Open it in the middle. Do the
    crossword first. Nothing in here is a course.</div>
  </div>
  <div style="background:{SAGE};padding:18px 20px 20px;margin-top:14px">
   <div class="lab" style="color:#25401f">The one rule we hold</div>
   <div style="font-size:13.6px;line-height:1.45;margin-top:7px">Every page in this paper is tied to
    at least one named Bible verse, printed where you can see it. If we cannot source it, we do not
    print it.</div>
  </div>
  <div style="border:1px solid {BR};padding:18px 20px 20px;margin-top:14px">
   <div class="lab">Translations</div>
   <div style="font-size:13.2px;line-height:1.45;margin-top:7px">Scripture is quoted from the
    <strong>New Living Translation</strong> and <strong>The Message</strong>, chosen because they
    are easy to read out loud. Public-domain text is the World English Bible. Every quotation was
    fetched from the text, never from memory.</div>
  </div>
  <div style="margin-top:16px;font-size:13.4px;line-height:1.45;color:rgba(44,26,18,.7)">
   <strong>Who makes this.</strong> Two people and three machines, none of whom are Bible scholars.
   We are not experts. We are going on the journey too.</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">The Reading begins on page 07 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:15, NLT</div>
""","Contents")

os.makedirs(OUT,exist_ok=True)
for n,doc in [("01",p01),("02",p02)]:
    open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc)
print("built p01, p02")

# ───────────────────────── p17 VISUAL EXPLAINER ─────────────────────────
MOVES=[("He runs","Genesis 27:43","A brother wants him dead. His mother tells him to go."),
       ("The sun sets","28:11","Not a destination. He stops because he cannot see."),
       ("A stone","28:11","No bed, no shelter, no plan. He uses what is on the ground."),
       ("The ramp","28:12","Traffic in both directions, all night, while he is unconscious."),
       ("The promise","28:15","I am with you. I will not leave you until I have finished."),
       ("He wakes","28:16","And finds out where he already was."),
       ("He names it","28:19","Bethel. It had been called Luz. Nobody there noticed.")]
band="".join(f'''<div style="position:absolute;left:{88+i*116}px;top:{510+ (i%2)*0}px;width:104px">
 <div style="width:26px;height:26px;border-radius:50%;background:{NAVY};color:{CREAM};
  font-family:Inter,sans-serif;font-size:12px;font-weight:800;display:flex;align-items:center;
  justify-content:center">{i+1}</div>
 <div style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;line-height:1.1;
  margin-top:10px">{t}</div>
 <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
  color:{NAVY};margin-top:5px">{r}</div>
 <div style="font-size:12.6px;line-height:1.4;margin-top:6px;color:rgba(44,26,18,.72)">{d}</div>
</div>''' for i,(t,r,d) in enumerate(MOVES))
conn="".join(f'<div style="position:absolute;left:{114+i*116}px;top:{522}px;width:{116-26}px;'
             f'height:1px;background:rgba(44,26,18,.3)"></div>' for i in range(len(MOVES)-1))
p17=page("17","Genesis 28:11-19 (NLT)",f"""
 {folio("17","Field guide",left=False)}
 <div style="position:absolute;left:52px;top:96px;width:600px">
  <div class="kicker">One night, taken apart</div>
  <div class="display" style="font-size:48px;margin-top:10px">Seven things happened
   <em>while he was asleep.</em></div>
  <div style="font-size:17px;line-height:1.46;margin-top:16px;width:560px">Read left to right. Five of
   the seven happen to him, not because of him. That is the shape of the whole chapter, and it is why
   this issue exists.</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:466px;height:1px;background:{BR}"></div>
 {conn}{band}
 <div style="position:absolute;left:52px;right:52px;top:742px;height:1px;background:rgba(44,26,18,.3)"></div>
 <div style="position:absolute;left:52px;top:786px;width:420px;background:{SKY};padding:22px 24px 24px">
  <div class="lab">The thing to notice</div>
  <div style="font-family:'Playfair Display',serif;font-size:26px;font-weight:700;line-height:1.12;
   margin-top:8px">Nothing on this line is a reward.</div>
  <div style="font-size:14.6px;line-height:1.48;margin-top:9px">He did not pray first. He did not
   build an altar first. He did not repent first — he had just finished lying to his father. The
   promise arrives anyway, in the middle of a getaway, to a man who is not awake for it.</div>
 </div>
 <div style="position:absolute;right:52px;top:786px;width:370px;background:{SAGE};padding:22px 24px 24px">
  <div class="lab" style="color:#25401f">Where this shows up again</div>
  <div style="font-size:14.6px;line-height:1.5;margin-top:9px">
   <strong>Exodus 3</strong> — a bush on an ordinary day at work.<br/>
   <strong>1 Kings 19</strong> — a man asleep under a tree, fed before he is fixed.<br/>
   <strong>Luke 24</strong> — two people walking, not recognising who is next to them.<br/><br/>
   Same shape every time. God turns up in transit, not at the destination.</div>
 </div>
 <div style="position:absolute;left:52px;top:1076px;width:838px;border:1px solid {BR};padding:22px 26px">
  <div class="lab">Read it yourself</div>
  <div style="font-size:16.4px;line-height:1.5;margin-top:8px">{G(15)}</div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.15em;
   margin-top:11px;color:rgba(44,26,18,.6)">GENESIS 28:15 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">The full reading is on pages 07–13 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:11–19, NLT</div>
""","Field guide")

# ───────────────────────── p43 WRITE IT DOWN ─────────────────────────
lines="".join(f'<div style="position:absolute;left:96px;right:96px;top:{436+i*46}px;height:1px;'
              f'background:rgba(44,26,18,.22)"></div>' for i in range(17))
p43=page("43","Habakkuk 2:2 (NLT)",f"""
 <div class="field" style="background:{CREAM}"></div>
 <div style="position:absolute;left:74px;top:0;bottom:0;width:1px;background:rgba(168,67,42,.42)"></div>
 {folio("43","Write it down",left=False)}
 <div style="position:absolute;left:96px;top:104px;width:600px">
  <div class="kicker">Habakkuk 2:2</div>
  <div class="display" style="font-size:52px;margin-top:10px">Write my answer
   <em>plainly on tablets,</em><br/>so that a runner<br/>can carry the<br/>correct message.</div>
 </div>
 <div style="position:absolute;right:96px;top:104px;width:196px;background:{BUT};padding:18px 20px 20px">
  <div class="lab">Page 08 asked you this</div>
  <div style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;line-height:1.14;
   margin-top:8px">Where have you already been, without knowing what was there?</div>
  <div style="font-size:13px;line-height:1.44;margin-top:8px">You do not have to be sure. Jacob was
   not. He only knew it afterwards.</div>
 </div>
 <div style="position:absolute;left:96px;top:392px;font-family:Inter,sans-serif;font-size:10px;
  font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:rgba(44,26,18,.5)">
  Write it here. Nobody else has to read it.</div>
 {lines}
 <div style="position:absolute;left:96px;right:96px;top:1232px;display:flex;align-items:baseline">
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.14em;
   text-transform:uppercase;color:rgba(44,26,18,.5)">Date</div>
  <div style="flex:1;border-bottom:1px solid rgba(44,26,18,.3);margin:0 18px 0 12px;height:14px"></div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.14em;
   text-transform:uppercase;color:rgba(44,26,18,.5)">Where you were</div>
  <div style="width:230px;border-bottom:1px solid rgba(44,26,18,.3);margin-left:12px;height:14px"></div>
 </div>
 <div class="credit" style="left:96px;bottom:44px">Scripture: Habakkuk 2:2, NLT</div>
 <div class="credit" style="right:96px;bottom:44px">Tear along the fold if you want to keep it</div>
""","Write it down")

# ───────────────────────── p48 BACK COVER ─────────────────────────
p48=page("48","Genesis 28:15 (NLT)",f"""
 <div class="field" style="background:{NAVY}"></div>
 <div class="arc" style="width:620px;height:620px;left:-190px;bottom:-230px;background:{SKY};opacity:.22"></div>
 <div class="arc" style="width:300px;height:300px;right:-80px;top:-90px;background:{BUT};opacity:.18"></div>
 <div style="position:absolute;left:52px;right:52px;top:34px;display:flex;align-items:baseline;
  font-family:Inter,sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.17em;
  text-transform:uppercase;color:rgba(247,243,236,.62)">
  <span>Between Sundays &nbsp;·&nbsp; Issue 001</span><span style="flex:1"></span>
  <span style="font-family:'Playfair Display',serif;font-size:19px;color:{CREAM}">48</span></div>
 <div style="position:absolute;left:52px;right:52px;top:64px;height:1px;background:rgba(247,243,236,.35)"></div>
 <div style="position:absolute;left:76px;right:76px;top:392px;color:{CREAM}">
  <div class="kicker" style="color:{BUT}">The last word</div>
  <div class="display" style="font-size:70px;margin-top:18px;color:{CREAM}">I am with you,
   <em>and I will protect you<br/>wherever you go.</em></div>
  <div style="font-family:Inter,sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.16em;
   margin-top:26px;color:{BUT}">GENESIS 28:15 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
  <div style="font-size:19px;line-height:1.46;margin-top:34px;width:560px;color:rgba(247,243,236,.86)">
   He said it to a man who was running away, in the dark, on the ground, with a rock under his head.
   Not to somebody who had earned it. Not on a Sunday.</div>
 </div>
 <div style="position:absolute;left:76px;bottom:104px;color:rgba(247,243,236,.6);
  font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.2em;
  text-transform:uppercase">Next issue &nbsp;·&nbsp; page 47</div>
 <div style="position:absolute;right:76px;bottom:104px;text-align:right;color:{CREAM};
  font-family:'Playfair Display',serif">
  <div style="font-size:22px;font-weight:700;line-height:1">Between</div>
  <div style="font-size:28px;font-style:italic;font-weight:700;line-height:1;margin-top:-2px">Sundays</div>
  <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.18em;
   margin-top:8px;color:rgba(247,243,236,.6)">GOOD NEWS. PRINTED.</div></div>
""","Back cover")

for n,doc in [("17",p17),("43",p43),("48",p48)]:
    open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc)
print("built p17, p43, p48")

# ───────────────────────── p34 THE DIRECTORY ─────────────────────────
DIR=json.load(open(os.path.join(B,"tools","directory_verified.json")))
bycat={}
for e in DIR: bycat.setdefault(e["cat"],[]).append(e)
cats=list(bycat.keys())[:26]
ent=[]
for c in cats:
    e=bycat[c][0]
    ent.append(f'''<div style="break-inside:avoid;margin-bottom:11px">
     <div style="display:inline-block;background:{BUT};padding:2px 9px;border-radius:99px;
      font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.11em">{c}</div>
     <div style="font-size:12.8px;line-height:1.36;margin-top:4px;color:rgba(44,26,18,.62)">{e["desc"]}</div>
     <div style="font-size:13.4px;line-height:1.4;margin-top:3px">{e["text"][:150]}{"…" if len(e["text"])>150 else ""}</div>
     <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
      color:{NAVY};margin-top:3px">{e["ref"]}</div></div>''')
p34=page("34","Psalm 23:4 (NLT)",f"""
 {folio("34","But God",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:560px">
  <div class="kicker">The directory</div>
  <div class="display" style="font-size:52px;margin-top:10px">Look up what is
   <em>actually wrong.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:14px;width:520px">Forty-seven headings, two
   hundred and ten verses, every one checked against its context by a person. Find the word that
   matches your week and read the line next to it. That is the whole system.</div>
 </div>
 <div style="position:absolute;right:52px;top:98px;width:250px;background:{SAGE};padding:19px 21px 21px">
  <div class="lab" style="color:#25401f">How this was built</div>
  <div style="font-size:13.4px;line-height:1.45;margin-top:8px">Every reference was fetched from the
   text, then read in context to check it actually says what the heading claims. Ten were filed wrong
   the first time and two of those would have read as an accusation. They were fixed. If you find
   another, page 28 is the letters page.</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:296px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:52px;right:52px;top:318px;height:860px;column-count:4;
  column-gap:22px;column-rule:1px solid rgba(44,26,18,.14)">{"".join(ent)}</div>
 <div style="position:absolute;left:52px;right:52px;top:1198px;height:1px;background:rgba(44,26,18,.3)"></div>
 <div style="position:absolute;left:52px;top:1218px;width:560px;font-size:13.4px;line-height:1.45">
  <strong>The rest of the directory runs on page 35</strong>, along with the questions people actually
  type into a search bar at midnight.</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Psalm 23:4 and 209 others, NLT</div>
""","But God directory")

# ───────────────────────── p44 PHOTO ESSAY ─────────────────────────
p44=page("44","Genesis 28:16 (NLT)",f"""
 {folio("44","Photo essay",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:540px">
  <div class="kicker">Ordinary places</div>
  <div class="display" style="font-size:50px;margin-top:10px">Places nobody
   <em>would photograph.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:14px;width:500px">Jacob's place had no name
   worth keeping. Somebody else called it Luz and thought nothing of it. These are the modern version:
   a stairwell, a car park at dusk, a kitchen at 11:40pm. No people in them. Nothing staged.</div>
 </div>
 <div style="position:absolute;right:52px;top:98px;width:250px;border:1px solid {BR};padding:19px 21px">
  <div class="lab">A note on the pictures</div>
  <div style="font-size:13.4px;line-height:1.45;margin-top:8px">Every photograph in this paper is a
   real place somebody actually stood in. We do not use stock, we do not stage, and we do not
   generate. If we cannot photograph it honestly, the page becomes a drawing instead.</div>
 </div>
 <div class="slot" style="left:52px;top:300px;width:558px;height:372px">
  Adrian's photograph &nbsp;·&nbsp; full width &nbsp;·&nbsp; 2400 × 1600 min</div>
 <div class="slot" style="right:52px;top:300px;width:250px;height:372px">
  Photograph &nbsp;·&nbsp; portrait</div>
 <div style="position:absolute;left:52px;top:684px;width:558px;font-size:12.6px;line-height:1.4;
  color:rgba(44,26,18,.66)">A stairwell between the fourth and fifth floor. Nobody has ever stopped
  here on purpose.<span style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;
  letter-spacing:.1em;display:block;margin-top:4px;color:rgba(44,26,18,.45)">PHOTOGRAPH — CREDIT TK</span></div>
 <div style="position:absolute;right:52px;top:684px;width:250px;font-size:12.6px;line-height:1.4;
  color:rgba(44,26,18,.66)">The last lit window on a street where everyone else has gone to bed.
  <span style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
  display:block;margin-top:4px;color:rgba(44,26,18,.45)">PHOTOGRAPH — CREDIT TK</span></div>
 <div class="slot" style="left:52px;top:772px;width:268px;height:222px">Photograph</div>
 <div class="slot" style="left:336px;top:772px;width:268px;height:222px">Photograph</div>
 <div class="slot" style="right:52px;top:772px;width:250px;height:222px">Photograph</div>
 <div style="position:absolute;left:52px;right:52px;top:1030px;background:{SKY};padding:22px 26px">
  <div class="lab">Why these and not people</div>
  <div style="font-size:16px;line-height:1.5;margin-top:8px;width:700px">Because the verse is about a
   <em>place</em>, and because a photograph of a person praying tells you what to feel. A photograph of
   an empty stairwell asks you a question instead: how many of these have you walked through this
   week without looking up?</div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.15em;
   margin-top:12px;color:{NAVY}">GENESIS 28:16 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:16, NLT</div>
""","Photo essay")

for n,doc in [("34",p34),("44",p44)]:
    open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc)
print("built p34, p44")
