#!/usr/bin/env python3
"""Look at everything sitting in DROP/ and describe it so pages can be assigned."""
import os, glob, hashlib
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS=None
BASE=os.path.dirname(os.path.abspath(__file__))
D=os.path.join(BASE,"DROP"); OUT=os.path.join(BASE,"public","lab","art")
files=[f for f in sorted(glob.glob(D+"/*")) if os.path.splitext(f)[1].lower()
       in (".png",".jpg",".jpeg",".webp")]
if not files:
    print("DROP/ is empty — save the artwork into ~/Projects/bts-web/DROP/"); raise SystemExit
placed={hashlib.md5(open(p,'rb').read()).hexdigest() for p in glob.glob(OUT+"/*") if os.path.isfile(p)}
print(f"{len(files)} file(s) in DROP/\n")
C=6; TH=190
rows=(len(files)+C-1)//C
sheet=Image.new("RGB",(C*TH,rows*(TH+18)),(238,236,232)); d=ImageDraw.Draw(sheet)
for i,f in enumerate(files):
    im=Image.open(f).convert("RGB"); w,h=im.size
    dup=" ALREADY PLACED" if hashlib.md5(open(f,'rb').read()).hexdigest() in placed else ""
    dpi=w/(332/25.4)
    print(f"  [{i}] {os.path.basename(f)[:44]:46s} {w}x{h}  aspect {w/h:.3f}  {dpi:.0f}dpi{dup}")
    t=im.copy(); t.thumbnail((TH-8,TH-8))
    x,y=(i%C)*TH,(i//C)*(TH+18); sheet.paste(t,(x+4,y+4))
    d.text((x+5,y+TH+2), f"[{i}] {w}x{h}", fill=(20,20,20))
sheet.save(os.path.join(D,"_contact.jpg"),quality=90)
print(f"\ncontact sheet -> DROP/_contact.jpg")
