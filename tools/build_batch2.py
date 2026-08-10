#!/usr/bin/env python3
"""Batch 2 — ten pages across every department, on the approved chassis."""
import json,re,html,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from anchor_chassis import *
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(B,"public","anchor")
V=json.load(open(os.path.join(B,"tools","anchor-verses-nlt.json")))
def t(book,v):
    for x in V[book]:
        if x["verse"]==v: return re.sub(r"<[^>]+>","",html.unescape(x["text"])).strip()
    return ""
def col(book,a,b,drop=None):
    out=[]
    for n in range(a,b+1):
        s=t(book,n)
        if not s: continue
        if n==a and drop:
            out.append(f'<p class="lead"><span class="dc">{s[0]}</span><span class="vn">{n}</span>{s[1:]}</p>')
        else:
            out.append(f'<p><span class="vn">{n}</span>{s}</p>')
    return "".join(out)
def box(bg,lab,head,body,labcol=None):
    return (f'<div style="background:{bg};padding:17px 19px 19px;margin-bottom:14px">'
            f'<div class="lab" style="color:{labcol or NAVY}">{lab}</div>'
            f'<div style="font-family:\'Playfair Display\',serif;font-size:20px;font-weight:700;'
            f'line-height:1.13;margin:7px 0 6px">{head}</div>'
            f'<div style="font-size:13.5px;line-height:1.45">{body}</div></div>')

P={}
# ── 03 · Lost Is Not Alone (opening essay, loud) ──
P["03"]=page("03","Genesis 27:41-45 (NLT)",f"""
 <div class="field" style="background:{SKY}"></div>
 <div class="arc" style="width:600px;height:600px;left:-230px;bottom:-220px;background:{NAVY};opacity:.14"></div>
 {folio("03","Opening",left=True)}
 <div style="position:absolute;left:52px;top:150px;width:600px">
  <div class="kicker">The state you are probably in</div>
  <div class="display" style="font-size:74px;margin-top:14px">Lost is not
   <em>the same thing<br/>as alone.</em></div>
 </div>
 <div class="panel" style="left:52px;top:520px;width:470px">
  <div class="lab">Where this issue starts</div>
  <div style="font-size:16.4px;line-height:1.5;margin-top:9px">There is a difference between not
   knowing where you are and nobody being with you. Most of us treat them as one feeling. The whole
   of Genesis 28 turns on the fact that they are not.</div>
  <div style="font-size:16.4px;line-height:1.5;margin-top:9px">Jacob was genuinely lost. He was also
   never once by himself. He simply did not know it until the morning.</div>
 </div>
 <div style="position:absolute;right:52px;top:520px;width:320px">
  {box("#fff","What he was running from","His brother had decided to kill him.",
   f"&ldquo;{t('gen27',41)[:190]}&rdquo;<div style='font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.1em;color:{NAVY};margin-top:7px'>GENESIS 27:41 · NLT</div>")}
  {box(BUT,"What he was running to","An uncle he had never met, four hundred miles away.",
   "His mother told him to leave for a few days. He was gone twenty years.")}
 </div>
 <div style="position:absolute;left:52px;right:52px;top:880px;height:1px;background:{BR}"></div>
 <div style="position:absolute;left:52px;top:912px;width:838px;column-count:3;column-gap:26px;
  font-size:14.8px;line-height:1.5;text-align:justify;hyphens:auto">
  <p style="margin-bottom:8px">If you are reading this in the middle of something, you are the target
  audience. Not the person with the answer — the person in transit.</p>
  <p style="margin-bottom:8px;text-indent:14px">This paper is made by two people and three machines,
  none of whom are Bible scholars. We are not going to pretend to be. What we can do is put the text
  in front of you in a way that does not assume you already know it, and get out of the way.</p>
  <p style="margin-bottom:8px;text-indent:14px">Everything in here is tied to a verse you can look up
  yourself. If we ever say something the Bible does not, we want you to catch us. Page 28 is where you
  write to us about it.</p>
  <p style="margin-bottom:8px;text-indent:14px">Start anywhere. Do the crossword first if you want.
  Nothing in this paper is a course, and nothing in it requires the page before.</p>
 </div>
 <div class="jump" style="left:52px;bottom:56px">The Reading begins on page 07 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 27:41–45, NLT</div>
""","Lost is not alone")

# ── 06 · Gate to The Reading ──
P["06"]=page("06","Genesis 28:10-22 (NLT)",f"""
 <div class="field" style="background:{BR}"></div>
 {folio("06","The Reading",left=True)}
 <div style="position:absolute;left:52px;right:52px;top:34px;color:{CREAM};
  font-family:Inter,sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.17em;
  text-transform:uppercase;display:flex"><span style="font-family:'Playfair Display',serif;
  font-size:19px">06</span>&nbsp;&nbsp;<span style="color:{BUT}">The Reading</span>
  <span style="flex:1"></span><span>Between Sundays &nbsp;·&nbsp; Issue 001</span></div>
 <div style="position:absolute;left:52px;right:52px;top:64px;height:1px;background:rgba(247,243,236,.4)"></div>
 <div style="position:absolute;left:76px;right:76px;top:420px;color:{CREAM};text-align:center">
  <div class="kicker" style="color:{BUT}">Pages 07 to 13</div>
  <div class="display" style="font-size:80px;margin-top:20px;color:{CREAM}">Genesis 28,
   <em>all of it,<br/>out loud.</em></div>
  <div style="font-size:19px;line-height:1.5;margin-top:32px;width:600px;margin-left:auto;
   margin-right:auto;color:rgba(247,243,236,.85)">Thirteen verses. About four minutes if you read
   them slowly. There is no study attached, no questions at the end, and nothing you are supposed to
   have understood already.</div>
 </div>
 <div style="position:absolute;left:76px;right:76px;bottom:150px;display:flex;gap:0;
  border-top:1px solid rgba(247,243,236,.35);padding-top:22px;color:rgba(247,243,236,.8)">
  <div style="flex:1"><div style="font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;
   letter-spacing:.15em;color:{BUT}">TRANSLATION</div>
   <div style="font-size:14.6px;margin-top:6px">New Living, chosen because it reads out loud without
    tripping you up.</div></div>
  <div style="flex:1;padding-left:28px"><div style="font-family:Inter,sans-serif;font-size:9.5px;
   font-weight:800;letter-spacing:.15em;color:{BUT}">IF YOU ONLY READ ONE LINE</div>
   <div style="font-size:14.6px;margin-top:6px">Verse 16. It is on page 08, and it is the whole
    issue.</div></div>
 </div>
 <div style="position:absolute;left:76px;bottom:70px;font-family:Inter,sans-serif;font-size:11px;
  font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{BUT}">Turn the page →</div>
""","Gate")

# ── 09 · The Reading 03 — what he was running from ──
P["09"]=page("09","Genesis 27:41-46 (NLT)",f"""
 {folio("09","The Reading  2/7",left=False)}
 <div style="position:absolute;left:52px;top:96px;width:560px">
  <div class="kicker">Before the stone</div>
  <div class="display" style="font-size:38px;margin-top:8px">What he was running from</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:174px;padding:7px 0;border-top:1px solid {BR};
  border-bottom:1px solid {BR};font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;
  letter-spacing:.19em;text-transform:uppercase;display:flex">
  <span>Genesis 27 : 41–46</span><span style="flex:1"></span><span>New Living Translation</span></div>
 <div class="body" style="position:absolute;left:52px;top:214px;width:560px;height:990px;
  column-count:2;column-gap:26px;column-rule:1px solid rgba(44,26,18,.16)">{col("gen27",41,46,drop=True)}</div>
 <div style="position:absolute;right:52px;top:214px;width:250px">
  {box(SKY,"Stop here a second","He lied to a blind man to get this.",
   "The blessing Jacob is running with was taken by pretending to be his brother. The paper is not going to tidy that up.")}
  {box(SAGE,"Words &amp; meaning","","<strong>Blessing</strong><br/>Not a nice wish. A legal transfer of the family's future to one son.<br/><br/><strong>Beersheba</strong><br/>Home. The last safe place he sees for twenty years.",
   "#25401f")}
  {box("#fff","A question to carry","Does God only turn up for people who deserve it?",
   "Hold that until page 12. The answer in the text is uncomfortable.")}
 </div>
 <div class="jump" style="left:52px;bottom:56px">The Reading continues on page 10 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 27:41–46, NLT</div>
""","The Reading 03")

# ── 13 · The Reading 07 / bridge out ──
P["13"]=page("13","Genesis 35:1-7 (NLT)",f"""
 {folio("13","The Reading  7/7",left=False)}
 <div style="position:absolute;left:52px;top:96px;width:600px">
  <div class="kicker">Twenty years later</div>
  <div class="display" style="font-size:44px;margin-top:8px">He goes back
   <em>to the same place.</em></div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:196px;padding:7px 0;border-top:1px solid {BR};
  border-bottom:1px solid {BR};font-family:Inter,sans-serif;font-size:9.5px;font-weight:800;
  letter-spacing:.19em;text-transform:uppercase;display:flex">
  <span>Genesis 35 : 1–7</span><span style="flex:1"></span><span>New Living Translation</span></div>
 <div class="body" style="position:absolute;left:52px;top:236px;width:560px;height:820px;
  column-count:2;column-gap:26px;column-rule:1px solid rgba(44,26,18,.16)">{col("gen35",1,7,drop=True)}</div>
 <div style="position:absolute;right:52px;top:236px;width:250px">
  {box(BUT,"What changed","Nothing about the place. Everything about him.",
   "Same ground. Same stone country. He arrives with a family, a limp and a new name — and this time he builds something before he sleeps.")}
  {box(SKY,"Stop here a second","God did not need him to come back.",
   "The promise in 28:15 had no conditions attached. Jacob returns anyway. That is what being kept actually does to a person.")}
 </div>
 <div style="position:absolute;left:52px;right:52px;top:1084px;background:{SAGE};padding:22px 26px">
  <div class="lab" style="color:#25401f">Where the reading leaves you</div>
  <div style="font-size:16.4px;line-height:1.5;margin-top:8px">He was told <em>I am with you</em> on
   the worst night of his life, while asleep, having earned none of it. Two decades later he is still
   being kept. Nothing in between suggests he got better at deserving it.</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">After the reading — page 14 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 35:1–7, NLT</div>
""","The Reading 07")

# ── 16 · Words & Meaning ──
WORDS=[("Bethel","BETH-el","House of God.","The name Jacob gave a field after one night. Before that it had no name anybody kept."),
 ("Luz","LOOZ","Almond tree.","What the locals already called it. They lived there and never noticed a thing."),
 ("Stairway","—","A ramp, not a rung ladder.","The old word suggests a built ramp with traffic in both directions. Not something to climb — something already in use."),
 ("Vow","—","A promise made in the open.","Jacob's vow in verse 20 begins with <em>if</em>. The Bible records the bargaining without correcting it."),
 ("Pillar","matstsebah","A stone stood upright.","A marker so you can find the spot again. The paper's whole idea of a mark you leave comes from here.")]
wrows="".join(f'''<div style="break-inside:avoid;padding:16px 0;border-bottom:1px solid rgba(44,26,18,.18)">
 <div style="display:flex;align-items:baseline;gap:12px">
  <div style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;line-height:1">{w}</div>
  <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.13em;
   color:rgba(44,26,18,.5)">{p}</div></div>
 <div style="font-size:16px;font-weight:600;margin-top:6px;color:{NAVY}">{d}</div>
 <div style="font-size:14.4px;line-height:1.48;margin-top:5px;color:rgba(44,26,18,.78)">{e}</div>
</div>''' for w,p,d,e in WORDS)
P["16"]=page("16","Genesis 28:17-22 (NLT)",f"""
 {folio("16","Words &amp; meaning",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:560px">
  <div class="kicker">Five words from this issue</div>
  <div class="display" style="font-size:50px;margin-top:10px">Nobody is going
   <em>to test you on this.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:14px;width:520px">Church words are usually
   explained by people who already know them. Here is the plain version, with no assumed knowledge and
   nothing left out to make it simpler than it is.</div>
 </div>
 <div style="position:absolute;left:52px;top:326px;width:560px">{wrows}</div>
 <div style="position:absolute;right:52px;top:326px;width:250px">
  {box(SKY,"Why this page exists","Not knowing a word is not a character flaw.",
   "The founder of this paper never liked reading and worked the school system to get through it. Every page here is another door in.")}
  {box("#fff","Where these come from","","All five appear in Genesis 28:17–22, printed in full on pages 08 and 09. Look them up in the text and see whether we got them right.")}
 </div>
 <div class="jump" style="left:52px;bottom:56px">The field guide continues on page 17 →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Genesis 28:17–22, NLT</div>
""","Words and meaning")
for n,doc in P.items(): open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc)
print("batch 2a:",", ".join(sorted(P)))

P2={}
# ── 19 · Sports — Away Team Advantage ──
STAND=[("Home","0","games this season"),("Away","28","chapters, all of them"),
       ("Nights on the road","20","years, in Jacob's case"),("Record","1–0","and he slept through it")]
P2["19"]=page("19","Deuteronomy 31:6 (NLT)",f"""
 <div class="field" style="background:{SAGE}"></div>
 {folio("19","Sports",left=False)}
 <div style="position:absolute;left:52px;top:110px;width:520px">
  <div class="kicker">The desk you were not expecting</div>
  <div class="display" style="font-size:78px;margin-top:14px">Away<br/>team<br/><em>advantage.</em></div>
 </div>
 <div class="panel" style="left:52px;top:520px;width:520px">
  <div class="lab">The report</div>
  <div style="font-size:16.2px;line-height:1.5;margin-top:9px">Nobody wants the away fixture. No
   crowd, no familiar ground, no routine. Every serious thing that happens to Jacob happens away —
   the dream, the wrestling, the name change. He is never once at home when God shows up.</div>
  <div style="font-size:16.2px;line-height:1.5;margin-top:9px">If you are reading this somewhere you
   did not plan to be, the record says that is the fixture where it happens.</div>
 </div>
 <div style="position:absolute;right:52px;top:110px;width:280px;background:#fff;padding:20px 22px 22px">
  <div class="lab">The line-up</div>
  {"".join(f'''<div style="display:flex;align-items:baseline;gap:12px;padding:11px 0;
   border-bottom:1px solid rgba(44,26,18,.16)">
   <div style="font-family:'Playfair Display',serif;font-size:27px;font-weight:700;width:62px;
    flex:0 0 62px;color:{NAVY}">{v}</div>
   <div><div style="font-size:14.6px;font-weight:600">{k}</div>
   <div style="font-size:12.4px;color:rgba(44,26,18,.6)">{s}</div></div></div>''' for k,v,s in STAND)}
 </div>
 <div style="position:absolute;right:52px;top:452px;width:280px;background:{NAVY};color:{CREAM};
  padding:20px 22px 22px">
  <div class="lab" style="color:{BUT}">Coach's line</div>
  <div style="font-size:17px;line-height:1.42;margin-top:9px">&ldquo;{t('deu31',6)[:200]}&rdquo;</div>
  <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.12em;
   margin-top:10px;color:{BUT}">DEUTERONOMY 31:6 · NLT</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:880px;background:#fff;padding:24px 28px">
  <div class="lab">Fixture notes</div>
  <div style="font-size:15.4px;line-height:1.5;margin-top:9px;column-count:3;column-gap:26px">
   <p style="margin-bottom:8px">Bethel is not a stadium. It is a field somebody was passing through.</p>
   <p style="margin-bottom:8px">The promise is made before any performance. There is no film study,
    no camp, no proving period.</p>
   <p style="margin-bottom:8px">And the away run lasts two decades. Nobody in this story gets a short
    season.</p></div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Deuteronomy 31:6, NLT</div>
""","Sports")

# ── 20 · Weather — Forecast for the middle ──
DAYS=[("Mon","Low cloud","No visibility past the next thing you have to do."),
      ("Tue","Same","It does not lift. This is normal and not a verdict on you."),
      ("Wed","Brief clearing","Something small goes right. Do not build a religion on it."),
      ("Thu","Wind","Somebody says the thing you needed to hear, badly."),
      ("Fri","Overcast","You will consider quitting at about four in the afternoon."),
      ("Sat","Still","The hardest day to be alone with. Also the most useful."),
      ("Sun","Bright, briefly","Then Monday. Which is what this paper is for.")]
P2["20"]=page("20","Psalm 42:5 (NLT)",f"""
 {folio("20","Weather",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Seven-day outlook</div>
  <div class="display" style="font-size:56px;margin-top:10px">Forecast for
   <em>the middle of the week.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:14px;width:540px">Sunday is not the
   problem. Sunday has music and people and somewhere to sit. This is the forecast for the other six,
   which is where most of your life is filed.</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:326px;height:1px;background:{BR}"></div>
 {"".join(f'''<div style="position:absolute;left:{52+i*120}px;top:348px;width:108px">
  <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.16em;
   color:{NAVY}">{d.upper()}</div>
  <div style="height:74px;margin-top:10px;background:{[SKY,SKY,BUT,SAGE,SKY,CREAM,BUT][i]};
   border:1px solid rgba(44,26,18,.14)"></div>
  <div style="font-family:'Playfair Display',serif;font-size:17px;font-weight:700;margin-top:9px;
   line-height:1.12">{c}</div>
  <div style="font-size:12.4px;line-height:1.38;margin-top:5px;color:rgba(44,26,18,.7)">{n}</div>
 </div>''' for i,(d,c,n) in enumerate(DAYS))}
 <div style="position:absolute;left:52px;right:52px;top:700px;height:1px;background:rgba(44,26,18,.3)"></div>
 <div style="position:absolute;left:52px;top:734px;width:540px;background:{SKY};padding:24px 26px">
  <div class="lab">Long-range</div>
  <div style="font-family:'Playfair Display',serif;font-size:27px;font-weight:700;line-height:1.14;
   margin-top:8px">The middle does not clear because you finally believed hard enough.</div>
  <div style="font-size:15.4px;line-height:1.5;margin-top:10px">Psalm 42 is a man asking himself, out
   loud, why he is so far down — and then telling himself to wait anyway. He does not talk himself out
   of it. He just keeps going in the weather.</div>
 </div>
 <div style="position:absolute;right:52px;top:734px;width:290px;border:1px solid {BR};padding:24px 26px">
  <div class="lab">Today's reading</div>
  <div style="font-size:16.4px;line-height:1.48;margin-top:9px">&ldquo;{t('psa42',5)[:230]}&rdquo;</div>
  <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.12em;
   margin-top:10px;color:{NAVY}">PSALM 42:5 · NLT</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:1030px;background:{BR};color:{CREAM};
  padding:24px 28px">
  <div class="lab" style="color:{BUT}">Severe weather advisory</div>
  <div style="font-size:16.4px;line-height:1.5;margin-top:9px;width:720px">If the forecast has read
   the same for months and you cannot see it ending, that is not a spiritual failure and this paper is
   not equipped to be your only help. Page 34 has the directory. Page 35 has the numbers people
   actually call.</div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Psalm 42:5, NLT</div>
""","Weather")

# ── 35 · Most looked up ──
Q=[("does God still love me","Romans 8:38–39","Nothing in creation can separate you from it. The list in the verse is exhaustive on purpose."),
   ("why do I feel nothing when I pray","Psalm 42:3","The Bible has a whole book of people praying while feeling nothing."),
   ("is it too late for me","Joel 2:25","God offers to give back the years the locusts ate. Not to explain them. To give them back."),
   ("what if I don't believe hard enough","Mark 9:24","A man says he believes and asks for help with his unbelief in the same sentence. Jesus helps him."),
   ("does God hear me","Psalm 34:17","The verse says he hears and rescues. It does not promise he does it on your timeline."),
   ("am I too far gone","Luke 15:20","The father runs. That is the detail everyone skips — the running.")]
P2["35"]=page("35","Psalm 34:17 (NLT)",f"""
 {folio("35","No dead zones",left=False)}
 <div style="position:absolute;left:52px;top:98px;width:600px">
  <div class="kicker">Most looked up</div>
  <div class="display" style="font-size:52px;margin-top:10px">What people type
   <em>at 11:40 at night.</em></div>
  <div style="font-size:16.2px;line-height:1.46;margin-top:14px;width:560px">These are real questions,
   asked in the dark, by people who would never say them out loud in a room. Each one has a verse next
   to it. Not an answer — a place to start.</div>
 </div>
 {"".join(f'''<div style="position:absolute;left:52px;right:52px;top:{330+i*128}px;
  border-top:1px solid rgba(44,26,18,.2);padding-top:16px;display:flex;gap:22px">
  <div style="width:404px;flex:0 0 404px">
   <div style="font-family:'Playfair Display',serif;font-size:25px;font-weight:700;line-height:1.14;
    font-style:italic">&ldquo;{q}&rdquo;</div></div>
  <div style="flex:1">
   <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.13em;
    color:{NAVY}">{r}</div>
   <div style="font-size:14.6px;line-height:1.46;margin-top:6px">{a}</div></div>
 </div>''' for i,(q,r,a) in enumerate(Q))}
 <div style="position:absolute;left:52px;right:52px;top:1114px;background:{SAGE};padding:22px 26px">
  <div class="lab" style="color:#25401f">If it is worse than a search bar</div>
  <div style="font-size:15.6px;line-height:1.5;margin-top:8px;width:720px">If you are thinking about
   hurting yourself, please tell a real person tonight — someone in your house, or 988 in the US. This
   is a newspaper. It is not enough, and it would rather say so than pretend.</div>
 </div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Psalm 34:17 and five others, NLT</div>
""","Most looked up")

# ── 22 · Obituaries & coupons ──
OBIT=[("The version of you that had it together","Died quietly, some time last year. Survived by the version that asks for help.","2 Corinthians 12:9"),
      ("The plan","Lived a short, confident life. Predeceased by three other plans.","Proverbs 19:21"),
      ("Sunday-only faith","Cause of death: a Tuesday.","James 2:17")]
COUP=[("ONE HONEST CONVERSATION","No expiry. Redeemable with anyone who has been waiting for you to start it.","Ephesians 4:25"),
      ("PERMISSION TO REST","Valid one full day. Cannot be earned. Non-transferable, though most people try.","Mark 2:27"),
      ("A SECOND ATTEMPT","Unlimited uses. Terms: you have to actually attempt it.","Lamentations 3:22–23")]
P2["22"]=page("22","Lamentations 3:22-23 (NLT)",f"""
 {folio("22","Obituaries &amp; coupons",left=True)}
 <div style="position:absolute;left:52px;top:98px;width:400px">
  <div class="kicker">Obituaries</div>
  <div class="display" style="font-size:40px;margin-top:8px">Things that
   <em>had to die first.</em></div>
  {"".join(f'''<div style="border-top:1px solid rgba(44,26,18,.2);padding:15px 0">
   <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;line-height:1.16">{h}</div>
   <div style="font-size:14px;line-height:1.45;margin-top:6px;color:rgba(44,26,18,.75)">{d}</div>
   <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.11em;
    color:{NAVY};margin-top:6px">{r}</div></div>''' for h,d,r in OBIT)}
  <div style="font-size:13.4px;line-height:1.45;margin-top:14px;color:rgba(44,26,18,.6)">
   Notices are free. Nobody real has died in this column.</div>
 </div>
 <div style="position:absolute;left:492px;top:98px;bottom:100px;width:1px;background:{BR}"></div>
 <div style="position:absolute;left:530px;top:98px;width:360px">
  <div class="kicker">Coupons</div>
  <div class="display" style="font-size:40px;margin-top:8px">Redeemable
   <em>at no cost.</em></div>
  {"".join(f'''<div style="border:2px dashed rgba(44,26,18,.45);padding:18px 20px;margin-top:16px;
   background:{[BUT,SKY,SAGE][i]}">
   <div style="font-family:Inter,sans-serif;font-size:13px;font-weight:800;letter-spacing:.08em">{h}</div>
   <div style="font-size:13.8px;line-height:1.44;margin-top:7px">{d}</div>
   <div style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.11em;
    color:{NAVY};margin-top:9px">{r}</div></div>''' for i,(h,d,r) in enumerate(COUP))}
 </div>
 <div style="position:absolute;left:52px;right:52px;bottom:96px;border-top:1px solid {BR};padding-top:16px;
  font-size:15.4px;line-height:1.5">&ldquo;{t('lam3',22) if 'lam3' in V else 'The faithful love of the LORD never ends! His mercies never cease.'}&rdquo;
  <span style="font-family:Inter,sans-serif;font-size:9px;font-weight:800;letter-spacing:.12em;
  color:{NAVY};margin-left:8px">LAMENTATIONS 3:22–23 · NLT</span></div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Lamentations 3:22–23, NLT</div>
""","Obituaries and coupons")

# ── 47 · Next issue ──
P2["47"]=page("47","Isaiah 43:19 (NLT)",f"""
 <div class="field" style="background:{BUT}"></div>
 {folio("47","Next issue",left=False)}
 <div style="position:absolute;left:52px;top:150px;width:640px">
  <div class="kicker">Issue 002</div>
  <div class="display" style="font-size:66px;margin-top:14px">We do not know
   <em>what it is yet.</em></div>
  <div style="font-size:18.5px;line-height:1.48;margin-top:22px;width:560px">That is honest rather
   than coy. The next theme comes out of what people tell us after reading this one — which is a
   strange way to run a newspaper and the only way we know how to run this one.</div>
 </div>
 <div class="panel" style="left:52px;top:520px;width:520px">
  <div class="lab">What is already on the table</div>
  <div style="font-size:15.6px;line-height:1.5;margin-top:9px">
   <strong>Chosen.</strong> What makes you different may be the thing you were given.<br/><br/>
   <strong>Valley.</strong> The place nobody volunteers for and everybody passes through.<br/><br/>
   <strong>Voicemail.</strong> A message left for someone who was not there to pick up.</div>
 </div>
 <div style="position:absolute;right:52px;top:520px;width:320px;background:{NAVY};color:{CREAM};
  padding:22px 24px 24px">
  <div class="lab" style="color:{BUT}">Tell us</div>
  <div style="font-size:15.6px;line-height:1.5;margin-top:9px">Which page in this issue did you keep?
   Which one did you skip? Which word above is the one you would read next?</div>
  <div style="font-size:15.6px;line-height:1.5;margin-top:10px">Write to page 28, or say it to whoever
   handed you this.</div>
 </div>
 <div style="position:absolute;left:52px;right:52px;top:900px;border-top:1px solid {BR};padding-top:24px">
  <div style="font-size:26px;line-height:1.36;font-family:'Playfair Display',serif;font-weight:700;
   width:740px">&ldquo;{t('isa43',19)[:210]}&rdquo;</div>
  <div style="font-family:Inter,sans-serif;font-size:10px;font-weight:800;letter-spacing:.15em;
   margin-top:14px;color:{NAVY}">ISAIAH 43:19 &nbsp;·&nbsp; NEW LIVING TRANSLATION</div>
 </div>
 <div class="jump" style="left:52px;bottom:56px">Back cover →</div>
 <div class="credit" style="right:52px;bottom:56px">Scripture: Isaiah 43:19, NLT</div>
""","Next issue")

for n,doc in P2.items(): open(f"{OUT}/between-sundays-page-{n}.html","w").write(doc)
print("batch 2b:",", ".join(sorted(P2)))
