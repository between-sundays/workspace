#!/usr/bin/env python3
"""The remaining 29 pages, on the approved chassis."""
import json,re,html,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from anchor_chassis import *
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(B,"public","anchor")
V=json.load(open(os.path.join(B,"tools","anchor-verses-nlt.json")))
def t(bk,v):
    for x in V.get(bk,[]):
        if x["verse"]==v: return re.sub(r"<[^>]+>","",html.unescape(x["text"])).strip()
    return ""
def col(bk,a,b,drop=False):
    o=[]
    for n in range(a,b+1):
        s=t(bk,n)
        if not s: continue
        o.append(f'<p class="lead"><span class="dc">{s[0]}</span><span class="vn">{n}</span>{s[1:]}</p>'
                 if (n==a and drop) else f'<p><span class="vn">{n}</span>{s}</p>')
    return "".join(o)
def box(bg,lab,head,body,lc=None):
    return (f'<div style="background:{bg};padding:17px 19px 19px;margin-bottom:14px">'
            f'<div class="lab" style="color:{lc or NAVY}">{lab}</div>'
            + (f'<div style="font-family:\'Playfair Display\',serif;font-size:20px;font-weight:700;'
               f'line-height:1.13;margin:7px 0 6px">{head}</div>' if head else '')
            + f'<div style="font-size:13.5px;line-height:1.45;margin-top:7px">{body}</div></div>')
def reading(n,part,kicker,hed,bk,a,b,ref,boxes,nxt):
    return page(f"{n:02d}",f"{ref} (NLT)",f"""
 {folio(f"{n:02d}",f"The Reading  {part}/7",left=(n%2==1))}
 <div style="position:absolute;left:52px;top:96px;width:600px">
  <div class="kicker">{kicker}</div>
  <div class="display" style="font-size:40px;margin-top:8px">{hed}</div></div>
 <div style="position:absolute;left:52px;right:52px;top:186px;padding:7px 0;border-top:1px solid {BR};
  border-bottom:1px solid {BR};font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;
  letter-spacing:.19em;text-transform:uppercase;display:flex">
  <span>{ref}</span><span style="flex:1"></span><span>New Living Translation</span></div>
 <div class="body" style="position:absolute;left:52px;top:226px;width:560px;height:980px;
  column-count:2;column-gap:26px;column-rule:1px solid rgba(44,26,18,.16)">{col(bk,a,b,True)}</div>
 <div style="position:absolute;right:52px;top:226px;width:250px">{boxes}</div>
 <div class="jump" style="left:52px;bottom:56px">{nxt}</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: {ref}, NLT</div>""",hed)
def essay(n,sec,kicker,hed,field,lede,cols,side,ref,left=True):
    return page(f"{n:02d}",f"{ref} (NLT)",f"""
 {'<div class="field" style="background:%s"></div>'%field if field else ''}
 {folio(f"{n:02d}",sec,left=left)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">{kicker}</div>
  <div class="display" style="font-size:52px;margin-top:10px">{hed}</div>
  <div style="font-size:16.6px;line-height:1.46;margin-top:14px;width:540px">{lede}</div></div>
 <div style="position:absolute;left:52px;right:52px;top:400px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:52px;top:432px;width:560px;column-count:2;column-gap:26px;
  font-size:14.9px;line-height:1.5;text-align:justify;hyphens:auto">{cols}</div>
 <div style="position:absolute;right:52px;top:432px;width:250px">{side}</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: {ref}, NLT</div>""",hed)
P={}

# ── The Reading 10, 11, 12 ──
P[10]=reading(10,3,"The promise, in his own words",
 "What God actually said","gen28",13,15,"Genesis 28:13–15",
 box(SKY,"Stop here a second","Count the conditions.","There are none. Not one clause begins with <em>if you</em>. Jacob's own vow in verse 20 does — God's promise does not.")
 +box(SAGE,"Words &amp; meaning","","<strong>I am with you</strong><br/>Present tense. Not a plan to arrive.<br/><br/><strong>I will not leave you</strong><br/>The same phrase turns up in Deuteronomy 31, Joshua 1 and Hebrews 13. It is the sentence the whole Bible keeps repeating.","#25401f"),
 "The Reading continues on page 11 →")
P[11]=reading(11,4,"What he does when he wakes",
 "Afraid, and not sorry","gen28",16,19,"Genesis 28:16–19",
 box(BUT,"Stop here a second","His first feeling is fear, not gratitude.","Verse 17 says he was afraid. The Bible reports this without correcting him. Nobody in the text tells him he should feel differently.")
 +box("#fff","A question to carry","When did you last notice something after it had already happened?","Page 43 has room to write it down."),
 "The Reading continues on page 12 →")
P[12]=reading(12,5,"The bargain","He tries to make a deal","gen28",20,22,"Genesis 28:20–22",
 box(SKY,"Stop here a second","He negotiates with God, and it is left in.","Verse 20 begins with <em>if</em>. He has just been promised everything unconditionally and he still tries to strike terms. The text does not tidy this up, and neither will we.")
 +box(SAGE,"Words &amp; meaning","","<strong>Vow</strong><br/>A promise said out loud where others can hear it.<br/><br/><strong>A tenth</strong><br/>His own idea, offered before anyone asked for it.","#25401f")
 +box("#fff","Where this lands","Twenty years pass before he keeps it.","Genesis 35, on page 13."),
 "The Reading ends on page 13 →")

# ── 04 Geography of nowhere ──
STOPS=[("Beersheba","Home","Where he starts. He will not see it again for twenty years."),
 ("Open country","Nowhere","No name in the text. Somewhere between two places, which is where this happens."),
 ("Luz","A town that did not notice","People lived here. They called it Luz. They slept through the same night."),
 ("Bethel","The name he gives it","Same ground. New name. Nothing about the field changed."),
 ("Haran","Where he was going","Four hundred miles. Twenty years. Two wives and a limp.")]
P[4]=page("04","Genesis 28:10-19 (NLT)",f"""
 <div class="field" style="background:{CREAM}"></div>
 {folio("04","The map",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:560px">
  <div class="kicker">The route</div>
  <div class="display" style="font-size:54px;margin-top:10px">The geography
   <em>of nowhere.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:14px;width:520px">Five places, only two of
   which have names anybody used. The important one is the one in the middle with no name at all.</div>
 </div>
 {"".join(f'''<div style="position:absolute;left:{88+i*172}px;top:398px;width:150px">
  <div style="width:19px;height:19px;border-radius:50%;background:{[BR,NAVY,STONE,BUT,NAVY][i]};
   border:3px solid {CREAM};box-shadow:0 0 0 1px rgba(44,26,18,.3)"></div>
  <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;margin-top:12px;
   line-height:1.1">{nm}</div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.11em;
   color:{NAVY};margin-top:5px">{sub.upper()}</div>
  <div style="font-size:13px;line-height:1.42;margin-top:7px;color:rgba(44,26,18,.72)">{d}</div>
 </div>''' for i,(nm,sub,d) in enumerate(STOPS))}
 <div style="position:absolute;left:96px;right:96px;top:406px;height:2px;background:rgba(44,26,18,.25)"></div>
 <div style="position:absolute;left:52px;right:52px;top:700px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:52px;top:734px;width:520px;background:{SKY};padding:24px 26px">
  <div class="lab">The point of the map</div>
  <div style="font-family:'Playfair Display',serif;font-size:27px;font-weight:700;line-height:1.14;
   margin-top:8px">The only place on this line God speaks is the one with no name.</div>
  <div style="font-size:15.4px;line-height:1.5;margin-top:10px">Not at home. Not at the destination.
   In the gap, at night, unplanned. If you are between two places right now, you are standing on the
   part of the map this issue is about.</div>
 </div>
 <div style="position:absolute;right:52px;top:734px;width:310px;border:1px solid {BR};padding:24px 26px">
  <div class="lab">Distance</div>
  <div style="font-size:15px;line-height:1.5;margin-top:9px">Beersheba to Haran is roughly
   <strong>800 kilometres</strong> on foot. At twenty-five kilometres a day that is about a month of
   walking, alone, with whatever he could carry.<br/><br/>The Bible gives that entire journey one
   sentence. It gives the night in the middle thirteen verses.</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">The Reading begins on page 07 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:10–19, NLT</div>
""","Geography of nowhere")

# ── 05 Wayfarer / baggage claim ──
BAGS=[("What he carried","A stolen blessing, his brother's rage, and no plan past the next town."),
 ("What he did not carry","Food, shelter, a tent, or anybody's phone number."),
 ("What he picked up","A rock."),
 ("What he left with","A promise he had not asked for and could not repay.")]
P[5]=essay(5,"Baggage claim","Before we start","What are you<br/><em>carrying?</em>",None,
 "Everyone arrives at a paper like this holding something. It is worth naming it before you read, "
 "because the man in this story is carrying more than he can admit to.",
 "".join(f'<p style="margin-bottom:10px"><strong>{h}.</strong> {d}</p>' for h,d in BAGS)
 +"<p style='margin-bottom:10px'>The list is short because his situation was simple and terrible. "
  "Yours is probably more complicated and less dramatic, which somehow makes it heavier.</p>"
  "<p style='margin-bottom:10px'>You do not have to put any of it down to read this. He did not.</p>",
 box(BUT,"An invitation, not an instruction","","Nothing in this paper requires you to have sorted anything out first. That is not us being generous. It is what the text says.")
 +box("#fff","Read this if you read nothing else","","&ldquo;"+t("mat11",28)[:150]+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>MATTHEW 11:28 · NLT</div>"),
 "Matthew 11:28",left=False)
for n,doc in P.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P))

P2={}
# ── 14 After the reading / feature ──
P2[14]=essay(14,"Feature","After the reading","The morning<br/><em>after.</em>",BUT,
 "He wakes up, names a field, makes a bargain, and walks on. Nothing about his circumstances has "
 "changed. He is still running, still alone, still four hundred miles from anywhere.",
 "<p style='margin-bottom:9px'>This is the part nobody puts on a poster. The dream does not end the "
 "journey. It does not reconcile him with his brother, undo the lie, or shorten the walk.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>What changes is one fact: he now knows he is not "
 "alone in it. That is a smaller thing than a rescue and a larger thing than encouragement.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Most of the Bible works like this. People are kept, "
 "not extracted. Israel walks out of Egypt into a desert. Paul gets a thorn and a sentence about "
 "grace being enough. The company is the answer, not the exit.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>If you were hoping this paper would tell you the "
 "hard part is nearly over, it will not. It will keep telling you who is in it with you.</p>",
 box(SKY,"The line that does the work","","&ldquo;"+t("gen28",15)[:170]+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>GENESIS 28:15 · NLT</div>")
 +box("#fff","Elsewhere in this issue","","Page 20 forecasts the middle of the week. Page 35 has the questions people ask at midnight. Page 43 has room to write your own."),
 "Genesis 28:15")
# ── 15 The place you almost walked past ──
P2[15]=essay(15,"Feature","Second look","The place you<br/><em>almost walked past.</em>",None,
 "Luz was an ordinary town with an ordinary name and people who lived there their whole lives "
 "without noticing anything. That is the most unnerving detail in the chapter.",
 "<p style='margin-bottom:9px'>Somebody in Luz got up the next morning and had a completely normal "
 "day. The ramp had been there all night. The traffic had been going both directions. Nobody in the "
 "town wrote anything down.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>The difference between them and Jacob is not virtue. "
 "It is not that he prayed harder or lived better — he had just spent a chapter deceiving his "
 "father. The difference is that he happened to be lying on that ground when he woke up.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Which raises the question this page exists to ask: "
 "how many ordinary rooms have you already been in?</p>",
 box(SAGE,"The uncomfortable version","","If God is where we do not expect, then a lot of what we have already walked past mattered more than we noticed. That is not a nice thought. It is in the text anyway.","#25401f")
 +box(BUT,"Try this","","For one day, treat the room you are least interested in as the one worth looking at. Report back on page 28."),
 "Genesis 28:16",left=False)
# ── 18 Modern parallel ──
P2[18]=essay(18,"Modern parallel","The same night, now","A motel<br/><em>off the interstate.</em>",None,
 "If this happened this week it would not look like a painting. It would look like the cheapest room "
 "available, booked at eleven at night, because you could not drive any further.",
 "<p style='margin-bottom:9px'>You are not on a retreat. You did not choose the town. The ice "
 "machine is out and the light above the mirror hums. You lie down in your clothes.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Nothing about the room is sacred. It is a room "
 "somebody else will have tomorrow. And that is the whole point — the field Jacob slept in was "
 "somebody else's field the next week too.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>The modern parallel is not the dream. It is the "
 "ordinariness. A car park at dusk. A hospital corridor. A kitchen at 11:40pm when everyone else "
 "has gone up. Places you would never photograph, which is exactly why page 44 photographs them.</p>",
 box("#fff","What we are not saying","","That every bad night means something. Some nights are just bad. The text does not promise a dream — it reports one, once, to a man who was not expecting it.")
 +box(SKY,"What we are saying","","That the list of places God is willing to turn up is longer and less impressive than most of us assume."),
 "Genesis 28:11")
# ── 21 Movies / cast of note ──
CAST=[("The one who leaves in the night","Every road film opens this way. Nobody in them is running for the reason Jacob is."),
 ("The stranger who is already there","Turns up in the second act, usually at a diner. In Genesis he arrives while the lead is unconscious."),
 ("The place with no name","Where the important scene always happens. Screenwriters know this instinctively."),
 ("The return, twenty years on","The genre calls it the reckoning. Genesis 35 calls it building an altar.")]
P2[21]=page("21","Genesis 28:16 (NLT)",f"""
 {folio("21","Movies",left=False)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Cast of note</div>
  <div class="display" style="font-size:52px;margin-top:10px">Four characters
   <em>you already know.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:14px;width:540px">Every one of these turns
   up in films you have seen. They are in Genesis 28 first, which is either a coincidence or the
   reason the shapes work.</div></div>
 {"".join(f'''<div style="position:absolute;left:52px;right:52px;top:{356+i*152}px;
  border-top:1px solid rgba(44,26,18,.2);padding-top:18px;display:flex;gap:26px">
  <div style="width:56px;flex:0 0 56px;font-family:'Playfair Display',serif;font-size:34px;
   font-weight:700;color:{NAVY};line-height:1">{i+1}</div>
  <div style="width:400px;flex:0 0 400px;font-family:'Playfair Display',serif;font-size:26px;
   font-weight:700;line-height:1.14">{h}</div>
  <div style="flex:1;font-size:14.8px;line-height:1.48;padding-top:4px">{d}</div>
 </div>''' for i,(h,d) in enumerate(CAST))}
 <div style="position:absolute;left:52px;right:52px;top:990px;background:{BR};color:{CREAM};
  padding:24px 28px">
  <div class="lab" style="color:{BUT}">The one thing films get wrong</div>
  <div style="font-size:16.6px;line-height:1.5;margin-top:9px;width:720px">In a film the hero earns
   the encounter. There is training, a low point, a decision. Jacob does none of it. He is asleep for
   the entire scene and wakes up having missed his own turning point.</div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:16, NLT</div>
""","Movies")
for n,doc in P2.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P2))

P3={}
SPINE_MARK=f'''<div style="position:absolute;left:0;top:0;bottom:0;width:26px;background:{BUT}"></div>
 <div style="position:absolute;left:6px;top:50%;transform:rotate(-90deg);transform-origin:left center;
  white-space:nowrap;font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.3em;
  text-transform:uppercase;color:{BR}">The Spine &nbsp;·&nbsp; lift this section out</div>'''
def spine(n,part,kicker,hed,lede,bodyhtml,ref):
    return page(f"{n:02d}",f"{ref} (NLT)",f"""
 <div class="field" style="background:{CREAM}"></div>
 {SPINE_MARK}
 <div style="position:absolute;left:78px;right:52px;top:34px;display:flex;align-items:baseline;
  font-family:Inter,sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.17em;
  text-transform:uppercase"><span style="font-family:'Playfair Display',serif;font-size:19px">{n:02d}</span>
  &nbsp;&nbsp;<span style="color:{NAVY}">The Spine &nbsp;{part}/4</span><span style="flex:1"></span>
  <span>Between Sundays &nbsp;·&nbsp; Issue 001</span></div>
 <div style="position:absolute;left:78px;right:52px;top:64px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:78px;top:104px;width:560px">
  <div class="kicker">{kicker}</div>
  <div class="display" style="font-size:46px;margin-top:10px">{hed}</div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:14px;width:520px">{lede}</div></div>
 {bodyhtml}
 <div class="credit" style="right:52px;bottom:56px">Scripture: {ref}, NLT</div>""",hed)
DAYS=[("Day one","Genesis 28:10–11","He stops because it gets dark. Nothing spiritual happens yet.",
  "Where did you stop today, and was it your choice?"),
 ("Day two","Genesis 28:12","A ramp, with traffic going both ways, while he is asleep.",
  "What might already be going on that you are not awake for?"),
 ("Day three","Genesis 28:15","I am with you. I will not leave you until I have finished.",
  "Read it as said to you. Write down what you resist about that."),
 ("Day four","Genesis 28:16","He had to wake up to find out where he was.",
  "Name one ordinary place from this week. Just name it."),
 ("Day five","Genesis 28:20","He tries to strike a deal he does not need to.",
  "What are you still trying to earn?"),
 ("Day six","Genesis 35:1","Twenty years on, he is told to go back to the same place.",
  "Is there somewhere you are meant to return to?"),
 ("Day seven","Psalm 139:7–10","Nowhere is out of range. Not one place on the list.",
  "Rest. Nothing to write.")]
rows="".join(f'''<div style="break-inside:avoid;border-top:1px solid rgba(44,26,18,.2);padding:15px 0">
 <div style="display:flex;gap:12px;align-items:baseline">
  <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700">{d}</div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.11em;
   color:{NAVY}">{r}</div></div>
 <div style="font-size:14.4px;line-height:1.45;margin-top:6px">{s}</div>
 <div style="font-size:13.6px;line-height:1.45;margin-top:6px;font-style:italic;
  color:rgba(44,26,18,.7)">{q}</div>
 <div style="border-bottom:1px solid rgba(44,26,18,.22);height:26px;margin-top:8px"></div>
</div>''' for d,r,s,q in DAYS)
P3[23]=spine(23,1,"A removable section","Seven days,<br/><em>one chapter.</em>",
 "Lift these four pages out and keep them somewhere you will see them. One reading a day, each about "
 "a minute. Nothing to sign up for and nobody checking.",
 f'<div style="position:absolute;left:78px;right:52px;top:352px">{rows[:len(rows)//2]}</div>',
 "Genesis 28:10–22")
P3[24]=spine(24,2,"Continued","The rest of<br/><em>the week.</em>",
 "Four more, then a day with nothing to do.",
 f'<div style="position:absolute;left:78px;right:52px;top:352px">{rows[len(rows)//2:]}</div>',
 "Genesis 35:1")
LINES="".join(f'<div style="position:absolute;left:78px;right:52px;top:{v}px;height:1px;'
              f'background:rgba(44,26,18,.2)"></div>' for v in range(470,1210,44))
P3[25]=spine(25,3,"Your part","Write it<br/><em>down here.</em>",
 "Whatever came up in the seven days. Nobody else has to read this page — that is the point of it "
 "being removable.",
 f'<div style="position:absolute;left:78px;top:414px;font-family:Inter,sans-serif;font-size:10px;'
 f'font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:rgba(44,26,18,.5)">'
 f'This week</div>{LINES}',"Habakkuk 2:2")
P3[26]=spine(26,4,"Keep this one","If you only<br/><em>keep one page.</em>",
 "Cut along the line. Put it where you will see it on a Tuesday.",
 f'''<div style="position:absolute;left:78px;right:52px;top:360px;border:2px dashed rgba(44,26,18,.4);
  padding:44px 46px;background:{BUT}">
  <div class="display" style="font-size:52px">I am with you,
   <em>and I will protect you<br/>wherever you go.</em></div>
  <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.16em;
   margin-top:24px;color:{NAVY}">GENESIS 28:15 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
  <div style="font-size:16px;line-height:1.5;margin-top:26px;width:600px">Said to a man who was
   running away, in the dark, on the ground, with a rock under his head. Not to somebody who had
   earned it.</div></div>
 <div style="position:absolute;left:78px;right:52px;bottom:120px;font-size:14px;
  color:rgba(44,26,18,.6);text-align:center">✂ &nbsp; cut here &nbsp; ✂</div>''',
 "Genesis 28:15")
for n,doc in P3.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built spine:",sorted(P3))

P4={}
# 27 If the middle is missing
P4[27]=essay(27,"Essay","The gap in the story","If the middle <em>is missing, good.</em>",SAGE,
 "Genesis gives the eight-hundred-kilometre walk one sentence and the night in the middle thirteen "
 "verses. Almost everything that happened to Jacob on that road is simply not recorded.",
 "<p style='margin-bottom:9px'>We tend to read that as an editing decision. It is worth reading it "
 "as a claim: the parts nobody wrote down were not wasted.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Most of your life is unrecorded middle. The years "
 "nobody will ask about. The Tuesdays. The job you had for a while. If the only meaningful part of a "
 "life were the parts worth writing down, almost none of it would count.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>The chapter says the opposite. The one night that "
 "gets thirteen verses is the night he was least productive, least impressive and least awake.</p>",
 box("#fff","The sentence that covers a month","","&ldquo;"+t("gen28",10)+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>GENESIS 28:10 · NLT</div>")
 +box(BUT,"If you are in the middle","","You are in the part of the story the Bible spends the most words on and the least explanation.")
 ,"Genesis 28:10",left=False)
# 28 Letters
LET=[("On not being experts","I liked that you said you are not Bible scholars. Most things I pick up assume I already know the words. — <em>a reader, by email</em>"),
 ("On the directory","Ten of the two hundred and ten were filed wrong and you printed that. Keep doing that. — <em>a reader</em>"),
 ("A correction we owe you","We have not published an issue before, so every letter on this page is one we expect rather than one we received. When Issue 002 prints, this page is yours.")]
P4[28]=page("28","James 1:19 (NLT)",f"""
 {folio("28","Letters",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:560px">
  <div class="kicker">Letters</div>
  <div class="display" style="font-size:52px;margin-top:10px">Tell us where
   <em>we got it wrong.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:14px;width:520px">This is the page where
   you correct us. Not a comment section — a printed correction, with your name on it if you want it
   there.</div></div>
 <div style="position:absolute;left:52px;top:352px;width:560px">
  {"".join(f'''<div style="border-top:1px solid rgba(44,26,18,.2);padding:16px 0">
   <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;line-height:1.14">{h}</div>
   <div style="font-size:14.8px;line-height:1.5;margin-top:8px">{d}</div></div>''' for h,d in LET)}
 </div>
 <div style="position:absolute;right:52px;top:352px;width:290px">
  {box(SKY,"How to write to us","","Say what page, say what is wrong, say why. If it is a scripture problem, name the verse and we will fetch it and check.")}
  {box("#fff","What we will print","","Corrections, disagreements, and anything that makes the paper more accurate. We will print the ones that make us look worst first.")}
  {box(SAGE,"Standard we hold","","&ldquo;"+t("jam1",19)[:150]+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;margin-top:8px'>JAMES 1:19 · NLT</div>","#25401f")}
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: James 1:19, NLT</div>
""","Letters")
# 29 Fiction
P4[29]=essay(29,"Fiction","Short fiction","The night<br/><em>clerk.</em>",None,
 "A short story. Nothing in it is true, which is the only page in this paper where that sentence is "
 "allowed.",
 "<p style='margin-bottom:9px'>The man came in at eleven and asked for the cheapest room. He paid "
 "cash and did not want a receipt. I gave him twelve because the light works.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>He asked how far it was to the county line. I said "
 "forty minutes. He looked at the clock like he was doing arithmetic, then said he would leave in "
 "the morning.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>People who are running always ask about distance. "
 "People on holiday ask about breakfast.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>At six he came down looking like he had not slept "
 "and also like something had happened. He asked what the town was called. I told him. He wrote it "
 "on the back of his hand.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Then he said, more to himself than to me: I did not "
 "know this place was here.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>I have worked this desk nine years. It has always "
 "been here.</p>",
 box(BUT,"Why fiction is in a faith paper","","Because a parable is fiction and Jesus used them constantly. The label is on this page so you always know which is which.")
 +box("#fff","The verse behind it","","&ldquo;"+t("gen28",16)[:140]+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>GENESIS 28:16 · NLT</div>"),
 "Genesis 28:16",left=False)
# 30 Comics
STRIPS=[("PANEL ONE","A man lies on the ground with a rock under his head. Caption: <em>nothing is happening.</em>"),
 ("PANEL TWO","Same drawing. Caption: <em>nothing is happening.</em>"),
 ("PANEL THREE","Same drawing, wider. Now you can see a ramp behind him, busy in both directions. Caption: <em>nothing is happening.</em>"),
 ("PANEL FOUR","Morning. The man sits up. Caption: <em>oh.</em>")]
P4[30]=page("30","Genesis 28:12-16 (NLT)",f"""
 {folio("30","Comics",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:560px">
  <div class="kicker">Four panels</div>
  <div class="display" style="font-size:48px;margin-top:10px">Nothing is
   <em>happening.</em></div></div>
 {"".join(f'''<div style="position:absolute;left:{52+(i%2)*430}px;top:{300+(i//2)*400}px;
  width:406px;height:372px;border:1px solid {BR};background:{[CREAM,CREAM,SKY,BUT][i]};padding:20px 22px">
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.16em;
   color:{NAVY}">{h}</div>
  <div class="slot" style="position:relative;left:0;top:0;width:100%;height:216px;margin-top:12px;
   border-color:rgba(44,26,18,.3)">Adrian&rsquo;s drawing</div>
  <div style="font-size:14.4px;line-height:1.45;margin-top:12px">{d}</div>
 </div>''' for i,(h,d) in enumerate(STRIPS))}
 <div style="position:absolute;left:52px;right:52px;bottom:96px;font-size:14px;
  color:rgba(44,26,18,.66)">The joke is the repetition, and the repetition is the theology. Art slots
  are for Adrian &mdash; nothing on this page is generated.</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:12–16, NLT</div>
""","Comics")
for n,doc in P4.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P4))

P5={}
# 31 Crossword
CW=[("1 across","Where Jacob slept, later renamed (6)","BETHEL"),("4 across","What the locals called it (3)","LUZ"),
 ("6 across","What he used for a pillow (5)","STONE"),("8 across","What he saw in the dream (8)","STAIRWAY"),
 ("2 down","He was running from his ______ (7)","BROTHER"),("3 down","Where he was heading (5)","HARAN"),
 ("5 down","What God made him, with no conditions (7)","PROMISE"),("7 down","What he set up in the morning (6)","PILLAR")]
grid="".join(f'<div style="position:absolute;left:{78+(i%11)*46}px;top:{412+(i//11)*46}px;width:44px;'
             f'height:44px;border:1px solid {BR};background:{"#fff" if (i*7)%5 else BR}"></div>'
             for i in range(88))
P5[31]=page("31","Genesis 28:11-19 (NLT)",f"""
 {folio("31","Games",left=False)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Crossword</div>
  <div class="display" style="font-size:50px;margin-top:10px">Eight answers,
   <em>all of them in this issue.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:12px;width:520px">Every answer appears on
   a page you have already turned past. Answers are on page 46, upside down, like they should be.</div></div>
 {grid}
 <div style="position:absolute;left:78px;top:824px;width:390px">
  <div class="lab">Across</div>
  {"".join(f'<div style="font-size:14.6px;line-height:1.44;margin-top:9px"><strong>{c}</strong> &nbsp;{q}</div>' for c,q,a in CW if "across" in c)}
 </div>
 <div style="position:absolute;left:498px;top:824px;width:390px">
  <div class="lab">Down</div>
  {"".join(f'<div style="font-size:14.6px;line-height:1.44;margin-top:9px"><strong>{c}</strong> &nbsp;{q}</div>' for c,q,a in CW if "down" in c)}
 </div>
 <div style="position:absolute;left:78px;right:52px;bottom:96px;border-top:1px solid rgba(44,26,18,.25);
  padding-top:14px;font-size:14px;color:rgba(44,26,18,.7)">Grid is a placeholder layout — the real
  one gets set once the answers are locked. Nothing about the clues will change.</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:11–19, NLT</div>
""","Crossword")
# 32 Find the certain place
P5[32]=page("32","Genesis 28:11 (NLT)",f"""
 <div class="field" style="background:{SKY}"></div>
 {folio("32","Games",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">A search</div>
  <div class="display" style="font-size:52px;margin-top:10px">Find the
   <em>certain place.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:12px;width:540px">The old translations say
   he came to <em>a certain place</em>. Not a special one. A certain one. Somewhere in this drawing is
   a man asleep with a rock under his head. Everything else is an ordinary evening.</div></div>
 <div class="slot" style="left:52px;top:380px;right:52px;height:660px;border-color:rgba(44,26,18,.4);
  background:rgba(255,255,255,.5)">Adrian&rsquo;s drawing &nbsp;·&nbsp; a busy ordinary scene, one sleeping figure</div>
 <div style="position:absolute;left:52px;top:1074px;width:520px;background:#fff;padding:22px 24px">
  <div class="lab">Also find</div>
  <div style="font-size:14.8px;line-height:1.5;margin-top:8px">A ladder leaning on nothing. Two people
   who nearly look up. A dog that has noticed. The only lit window on the street.</div>
 </div>
 <div style="position:absolute;right:52px;top:1074px;width:290px;border:1px solid {BR};padding:22px 24px">
  <div class="lab">The verse</div>
  <div style="font-size:15px;line-height:1.48;margin-top:8px">&ldquo;{t('gen28',11)[:170]}&rdquo;</div>
  <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
   color:{NAVY};margin-top:8px">GENESIS 28:11 · NLT</div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:11, NLT</div>
""","Find the certain place")
# 33 But God — back of the book opener
BG=[("You are afraid","Psalm 23:4"),("You blew it","1 John 1:9"),("Nobody knows","Psalm 139:1"),
 ("You are worn out","Matthew 11:28"),("You cannot pray","Romans 8:26"),("It is late","Lamentations 3:22")]
P5[33]=page("33","Romans 8:26 (NLT)",f"""
 <div class="field" style="background:{BR}"></div>
 <div style="position:absolute;left:52px;right:52px;top:34px;color:{CREAM};
  font-family:Inter,sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.17em;
  text-transform:uppercase;display:flex"><span style="font-family:'Playfair Display',serif;
  font-size:19px">33</span>&nbsp;&nbsp;<span style="color:{BUT}">But God</span>
  <span style="flex:1"></span><span>Between Sundays &nbsp;·&nbsp; Issue 001</span></div>
 <div style="position:absolute;left:52px;right:52px;top:64px;height:1px;background:rgba(247,243,236,.4)"></div>
 <div style="position:absolute;left:76px;top:200px;width:640px;color:{CREAM}">
  <div class="kicker" style="color:{BUT}">The back of the book</div>
  <div class="display" style="font-size:92px;margin-top:18px;color:{CREAM}">But<br/><em>God.</em></div>
  <div style="font-size:19px;line-height:1.48;margin-top:26px;width:560px;color:rgba(247,243,236,.85)">
   Two words that turn up all over the Bible at exactly the moment a sentence should have ended badly.
   The next three pages are built around them: look up what is actually wrong, and read the line next
   to it.</div>
 </div>
 {"".join(f'''<div style="position:absolute;left:{76+(i%3)*280}px;top:{790+(i//3)*130}px;width:250px;
  border-top:1px solid rgba(247,243,236,.3);padding-top:14px;color:{CREAM}">
  <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;line-height:1.15">{h}</div>
  <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.12em;
   color:{BUT};margin-top:7px">{r}</div></div>''' for i,(h,r) in enumerate(BG))}
 <div style="position:absolute;left:76px;bottom:70px;font-family:Inter,sans-serif;font-size:11px;
  font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{BUT}">
  The full directory is on page 34 →</div>
""","But God")
for n,doc in P5.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P5))

P6={}
def ads(items,bg=None):
    return "".join(f'''<div style="break-inside:avoid;border:1px solid {BR};padding:15px 17px;
     margin-bottom:13px;background:{c or "#fff"}">
     <div style="font-family:Inter,sans-serif;font-size:11.5px;font-weight:800;letter-spacing:.09em">{h}</div>
     <div style="font-size:13.6px;line-height:1.45;margin-top:7px">{d}</div>
     <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
      color:{NAVY};margin-top:8px">{r}</div></div>''' for h,d,r,c in items)
CLASS=[("LOST — ONE SENSE OF DIRECTION","Last seen somewhere around age nineteen. Owner has stopped looking and started walking. Reward: none offered.","Proverbs 3:5–6",None),
 ("WANTED — SOMEONE TO SIT WITH","No advice required. Must be able to stay quiet for longer than is comfortable.","Job 2:13",BUT),
 ("FOR SALE — A PLAN","Barely used. Was going to change everything. Open to offers, or will accept a better one free.","Proverbs 19:21",None),
 ("FOUND — A PLACE THAT TURNED OUT TO MATTER","Ordinary field, no distinguishing features. Owner did not notice at the time.","Genesis 28:16",SKY),
 ("SERVICES — RUNNING AWAY","Long distance a speciality. Twenty years' experience. Results not guaranteed.","Jonah 1:3",None),
 ("NOTICE — THE DOOR IS NOT LOCKED","Repeated at the request of the management. It has never been locked.","Revelation 3:20",SAGE)]
P6[36]=page("36","Proverbs 19:21 (NLT)",f"""
 {folio("36","Classifieds",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Classifieds</div>
  <div class="display" style="font-size:50px;margin-top:10px">Small ads
   <em>for large problems.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:12px;width:520px">Every notice below is
   invented. Every verse under one is not. Place your own on page 28.</div></div>
 <div style="position:absolute;left:52px;right:52px;top:330px;column-count:3;column-gap:22px">
  {ads(CLASS)}</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Proverbs 19:21 and five others, NLT</div>
""","Classifieds")
# 37 Food
P6[37]=essay(37,"Food","The table","Bread for people <em>who did not cook.</em>",None,
 "Elijah, at the lowest point of his life, asks to die under a tree. God's first response is not a "
 "lecture. It is a nap and something to eat.",
 "<p style='margin-bottom:9px'>He sleeps. An angel wakes him and there is bread. He eats and sleeps "
 "again. He is woken a second time and fed again, because the journey is too much for him.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Nobody asks him to explain himself. Nobody corrects "
 "his theology, which at that moment is bad. He is fed twice and allowed to rest before a single word "
 "of instruction arrives.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>It is the most practical passage in the Bible about "
 "helping somebody who is at the end of themselves. Feed them. Let them sleep. Talk later.</p>",
 box(BUT,"If you are the one who is worn out","","Eat something. This is not a metaphor and the text is not being poetic.")
 +box("#fff","The passage","","&ldquo;"+t("kg19",7)[:170]+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>1 KINGS 19:7 · NLT</div>")
 +box(SAGE,"If you are the friend","","Bring food before advice. Every time.","#25401f"),
 "1 Kings 19:5–8",left=False)
# 38 Home
P6[38]=essay(38,"Home","The tour","Give them <em>the tour.</em>",SKY,
 "Jacob turns a field into a house of God with a rock and a name. It is the least equipped act of "
 "worship in the Bible and it counts.",
 "<p style='margin-bottom:9px'>You do not need a room set aside. He had a stone, a night and no "
 "plan. Whatever you have is more than that.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>The practical version: pick one place in your home "
 "you pass every day — a step, a window, the kettle. Make it the spot. Not a shrine. A marker, the "
 "way the pillar was a marker so he could find the place again.</p>"
 "<p style='margin-bottom:9px;text-indent:14px'>Then tell somebody it is there. That is what turns a "
 "private habit into a house.</p>",
 box("#fff","Mark it","","Page 45 has the marks. Page 43 has the writing. Both are designed to be torn out and stuck up.")
 +box(BUT,"What Jacob used","","A rock he had already slept on. Nothing bought, nothing consecrated, nothing new."),
 "Genesis 28:18–19")
# 39 Poster
P6[39]=page("39","Genesis 28:16 (NLT)",f"""
 <div class="field" style="background:{BUT}"></div>
 <div class="arc" style="width:700px;height:700px;right:-240px;top:-220px;background:{SKY};opacity:.55"></div>
 <div class="arc" style="width:340px;height:340px;left:-120px;bottom:120px;background:{SAGE};opacity:.6"></div>
 {folio("39","Poster",left=False)}
 <div style="position:absolute;left:76px;right:76px;top:330px">
  <div class="display" style="font-size:104px;line-height:.92">Surely<br/>the LORD<br/>is in
   <em>this place.</em></div>
  <div style="font-family:Inter,sans-serif;font-size:12px;font-weight:800;letter-spacing:.2em;
   margin-top:40px;color:{NAVY}">GENESIS 28:16 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
  <div style="font-size:20px;line-height:1.45;margin-top:34px;width:520px">And I wasn&rsquo;t even
   aware of it.</div>
 </div>
 <div style="position:absolute;left:76px;bottom:96px;font-family:Inter,sans-serif;font-size:10px;
  font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:rgba(44,26,18,.55)">
  Tear this page out &nbsp;·&nbsp; it is meant for a wall</div>
 <div class="credit" style="right:76px;bottom:96px">Between Sundays · Issue 001</div>
""","Poster")
# 40 Music
SONGS=[("For the drive home when it did not go well","Psalm 42"),("For a Tuesday that feels like nothing","Psalm 23"),
 ("For when you cannot find the words","Romans 8:26"),("For the middle of the night","Psalm 121"),
 ("For starting again","Lamentations 3:22–23"),("For being kept rather than rescued","Genesis 28:15")]
P6[40]=page("40","Psalm 121:1-2 (NLT)",f"""
 {folio("40","Music",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">A list, not a playlist</div>
  <div class="display" style="font-size:52px;margin-top:10px">Songs for
   <em>walking home.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:12px;width:520px">We are not going to
   recommend six worship tracks you already know. These are six psalms, which is what people sang
   before anybody had a band. Read them out loud and you will hear the tune.</div></div>
 <div style="position:absolute;left:52px;top:350px;width:560px">
  {"".join(f'''<div style="border-top:1px solid rgba(44,26,18,.2);padding:15px 0;display:flex;gap:16px">
   <div style="font-family:'Playfair Display',serif;font-size:26px;font-weight:700;width:40px;
    color:{NAVY}">{i+1}</div>
   <div><div style="font-size:18px;font-weight:600;line-height:1.24">{h}</div>
   <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.12em;
    color:{NAVY};margin-top:5px">{r}</div></div></div>''' for i,(h,r) in enumerate(SONGS))}
 </div>
 <div style="position:absolute;right:52px;top:350px;width:250px">
  {box(SKY,"The one to start with","Psalm 121.","Eight verses. Written for people on a road, walking somewhere, looking up at hills they had to cross.")}
  {box("#fff","","","&ldquo;"+t("psa121",1)+" "+t("psa121",2)+"&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:"+NAVY+";margin-top:8px'>PSALM 121:1–2 · NLT</div>")}
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Psalm 121:1–2 and five others, NLT</div>
""","Music")
for n,doc in P6.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P6))

P7={}
SUP=[("THE STONE","A rock. You already have one. Free, wherever you are standing.","Genesis 28:11",BUT),
 ("THE MARK","Something to show you where you were. Chalk, a pen, a folded corner.","Genesis 28:18",SKY),
 ("THE PAPER","Forty-eight pages. Take one, leave one, pass one on.","Genesis 28:16",SAGE),
 ("THE MIDDLE OF THE WEEK","Supplied automatically. Non-refundable.","Psalm 42:5",None)]
P7[41]=page("41","Genesis 28:18 (NLT)",f"""
 <div class="field" style="background:{CREAM}"></div>
 {folio("41","House ads",left=False)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Between Sundays Supply Co.</div>
  <div class="display" style="font-size:52px;margin-top:10px">Everything you need
   <em>is already here.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:12px;width:520px">A catalogue of things we
   do not sell, because you have them. This is the only advertisement in the paper and it is for
   nothing.</div></div>
 {"".join(f'''<div style="position:absolute;left:{52+(i%2)*430}px;top:{356+(i//2)*300}px;width:406px;
  height:270px;border:2px solid {BR};padding:24px 26px;background:{c or "#fff"}">
  <div style="font-family:Inter,sans-serif;font-size:13px;font-weight:800;letter-spacing:.1em">{h}</div>
  <div style="font-size:16px;line-height:1.48;margin-top:12px">{d}</div>
  <div style="position:absolute;left:26px;bottom:22px;font-family:Inter,sans-serif;font-size:9.5px;
   font-weight:800;letter-spacing:.12em;color:{NAVY}">{r}</div>
  <div style="position:absolute;right:26px;bottom:22px;font-family:'Playfair Display',serif;
   font-size:26px;font-weight:700">$0</div>
 </div>''' for i,(h,d,r,c) in enumerate(SUP))}
 <div style="position:absolute;left:52px;right:52px;bottom:96px;border-top:1px solid {BR};
  padding-top:14px;font-size:14.4px;line-height:1.5">No stock, no shipping, no checkout. If you were
  hoping for merchandise, page 47 will tell you when there is any.</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:18, NLT</div>
""","Supply Co")
WORK=[("MONDAY","The day most people decide their life is not working. Statistically the worst hour is 11am.","Colossians 3:23"),
 ("THE COMMUTE","Forty minutes nobody counts as part of your life. It is about a tenth of your waking week.","Ephesians 5:16"),
 ("THE JOB YOU DID NOT PICK","Jacob worked seven years for the wrong outcome, then seven more. Genesis reports it without comment.","Genesis 29:20"),
 ("THE ONE WHO NOTICES","Every workplace has somebody holding it together quietly. It might be you and nobody has said so.","Matthew 6:4")]
P7[42]=page("42","Colossians 3:23 (NLT)",f"""
 {folio("42","Work",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Work</div>
  <div class="display" style="font-size:52px;margin-top:10px">Most of your life
   <em>happens at a desk.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:12px;width:520px">The Bible spends more
   time on people working than on people worshipping, which is not the impression most of us grew up
   with.</div></div>
 {"".join(f'''<div style="position:absolute;left:52px;right:52px;top:{352+i*168}px;
  border-top:1px solid rgba(44,26,18,.2);padding-top:16px;display:flex;gap:24px">
  <div style="width:200px;flex:0 0 200px">
   <div style="font-family:Inter,sans-serif;font-size:12px;font-weight:800;letter-spacing:.14em">{h}</div>
   <div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;letter-spacing:.11em;
    color:{NAVY};margin-top:8px">{r}</div></div>
  <div style="flex:1;font-size:16px;line-height:1.5">{d}</div>
 </div>''' for i,(h,d,r) in enumerate(WORK))}
 <div style="position:absolute;left:52px;right:52px;top:1058px;background:{SAGE};padding:22px 26px">
  <div class="lab" style="color:#25401f">The line</div>
  <div style="font-size:16.6px;line-height:1.5;margin-top:8px;width:720px">&ldquo;{t('col3',23)[:200]}&rdquo;
   <span style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.11em;
   margin-left:8px">COLOSSIANS 3:23 · NLT</span></div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Colossians 3:23, NLT</div>
""","Work")
MARKS=[("A stone on a windowsill","For the place you did not choose."),
 ("A corner folded down","For the page you want to find again."),
 ("A date written on a wall","For the night it changed."),
 ("A name said out loud","For the person who was there.")]
P7[45]=page("45","Genesis 28:18 (NLT)",f"""
 <div class="field" style="background:{SAGE}"></div>
 {folio("45","Mark the place",left=False)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Marks</div>
  <div class="display" style="font-size:54px;margin-top:10px">Leave something
   <em>so you can find it again.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:12px;width:540px">He stood the stone up. That
   is all a pillar is — a thing left behind so the place can be found later. Four small versions.</div></div>
 {"".join(f'''<div style="position:absolute;left:{52+(i%2)*430}px;top:{382+(i//2)*250}px;width:406px;
  background:#fff;padding:22px 24px;height:224px">
  <div style="font-family:'Playfair Display',serif;font-size:25px;font-weight:700;line-height:1.14">{h}</div>
  <div style="font-size:15px;line-height:1.48;margin-top:9px">{d}</div>
  <div style="border-bottom:1px solid rgba(44,26,18,.25);height:30px;margin-top:20px"></div>
  <div style="border-bottom:1px solid rgba(44,26,18,.25);height:30px"></div>
 </div>''' for i,(h,d) in enumerate(MARKS))}
 <div style="position:absolute;left:52px;right:52px;bottom:92px;font-size:15px;line-height:1.5">
  &ldquo;{t('gen28',18)[:190]}&rdquo;
  <span style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.11em;
  color:{NAVY};margin-left:8px">GENESIS 28:18 · NLT</span></div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:18, NLT</div>
""","Mark the place")
ANS=[("1 across","BETHEL"),("4 across","LUZ"),("6 across","STONE"),("8 across","STAIRWAY"),
 ("2 down","BROTHER"),("3 down","HARAN"),("5 down","PROMISE"),("7 down","PILLAR")]
P7[46]=page("46","Psalm 139:7-10 (NLT)",f"""
 {folio("46","Where this went",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Where this paper went</div>
  <div class="display" style="font-size:50px;margin-top:10px">Somebody left this
   <em>where you found it.</em></div>
  <div style="font-size:16.4px;line-height:1.46;margin-top:12px;width:540px">A break room. A waiting
   room. A church table. A bus seat. Whoever left it here did not know who would pick it up, which is
   the entire distribution strategy.</div></div>
 <div style="position:absolute;left:52px;top:400px;width:520px;background:{SKY};padding:24px 26px">
  <div class="lab">Pass it on</div>
  <div style="font-size:15.6px;line-height:1.5;margin-top:9px">When you are done, leave it somewhere
   ordinary. Not a person you have chosen — a place. That is closer to how this works in the story.
   Nobody handed Jacob anything. He lay down where he happened to be.</div>
 </div>
 <div style="position:absolute;right:52px;top:400px;width:290px;border:1px solid {BR};padding:24px 26px">
  <div class="lab">Left here by</div>
  <div style="border-bottom:1px solid rgba(44,26,18,.3);height:32px;margin-top:14px"></div>
  <div class="lab" style="margin-top:18px">Found by</div>
  <div style="border-bottom:1px solid rgba(44,26,18,.3);height:32px;margin-top:14px"></div>
  <div class="lab" style="margin-top:18px">Where</div>
  <div style="border-bottom:1px solid rgba(44,26,18,.3);height:32px;margin-top:14px"></div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:700px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:52px;top:732px;width:520px">
  <div class="lab">Crossword answers</div>
  <div style="transform:rotate(180deg);margin-top:12px;column-count:2;column-gap:22px;
   font-size:14.4px;line-height:1.7">
   {"".join(f'<div><strong>{c}</strong> &nbsp;{a}</div>' for c,a in ANS)}</div>
 </div>
 <div style="position:absolute;right:52px;top:732px;width:290px;background:{BUT};padding:22px 24px">
  <div class="lab">And wherever you take it</div>
  <div style="font-size:15px;line-height:1.48;margin-top:9px">&ldquo;{t('psa139',7)} {t('psa139',8)}&rdquo;</div>
  <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;
   color:{NAVY};margin-top:9px">PSALM 139:7–8 · NLT</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">Next issue — page 47 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Psalm 139:7–10, NLT</div>
""","Where this went")
for n,doc in P7.items(): open(f"{OUT}/between-sundays-page-{n:02d}.html","w").write(doc)
print("built:",sorted(P7))
