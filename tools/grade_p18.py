#!/usr/bin/env python3
"""Grade p18 frames into ONE look: warm tungsten inside green-black dark."""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import os, json, random
RAW="photos/p18raw"; OUT="public/lab/photos"; os.makedirs(OUT, exist_ok=True)
random.seed(28)

# tungsten-in-green-dark ramp  (stop, rgb)
# split-tone: green-black shadows -> olive mids -> tungsten amber highlights
RAMP=[(0.00,(9,17,14)),(0.22,(22,38,30)),(0.45,(58,68,42)),
      (0.68,(140,104,44)),(0.86,(206,156,72)),(1.00,(244,214,158))]
def lut():
    t=[]
    for i in range(256):
        v=i/255
        for j in range(len(RAMP)-1):
            a,ca=RAMP[j]; b,cb=RAMP[j+1]
            if a<=v<=b:
                f=(v-a)/(b-a)
                t.append(tuple(int(ca[k]+(cb[k]-ca[k])*f) for k in range(3))); break
        else: t.append(RAMP[-1][1])
    return t
LUT=lut()

def grade(src, dst, box, keep=0.22, vig=0.72, lift=1.0):
    im=Image.open(src).convert("RGB")
    W,H=box; ar=W/H; w,h=im.size
    if w/h > ar: nw=int(h*ar); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else: nh=int(w/ar); im=im.crop((0,max(0,(h-nh)//2-int(h*.05)),w,max(0,(h-nh)//2-int(h*.05))+nh))
    im=im.resize((W,H), Image.LANCZOS)
    im=ImageEnhance.Brightness(im).enhance(lift)
    lum=im.convert("L")
    lum=ImageEnhance.Contrast(lum).enhance(1.38)
    px=lum.load()
    ton=Image.new("RGB",(W,H)); tp=ton.load()
    for y in range(H):
        for x in range(W): tp[x,y]=LUT[px[x,y]]
    out=Image.blend(ton, im, keep)
    # vignette
    v=Image.new("L",(W,H),0); d=ImageDraw.Draw(v)
    d.ellipse((-W*0.34,-H*0.40,W*1.34,H*1.40), fill=255)
    v=v.filter(ImageFilter.GaussianBlur(min(W,H)*0.20))
    dark=Image.new("RGB",(W,H),(6,9,8))
    out=Image.composite(out, Image.blend(out,dark,vig), v)
    # grain
    g=Image.effect_noise((W,H), 13).convert("L")
    out=Image.blend(out, Image.merge("RGB",(g,g,g)), 0.045)
    out.save(os.path.join(OUT,dst), quality=92)
    print(f"  {dst:24s} {W}x{H}")

print("grading p18 frames (only the two that are actually true):")
grade(f"{RAW}/macro_02.jpg", "p18_hand.jpg",    (402,178), keep=.20, vig=.80, lift=.92)
grade(f"{RAW}/ashtray_10.jpg","p18_ashtray.jpg",(402,150), keep=.20, vig=.74, lift=.96)

m=json.load(open(f"{RAW}/_meta.json"))
cr={k:m[k] for k in ["macro_02.jpg","ashtray_10.jpg"] if k in m}
json.dump(cr, open("public/lab/photos/p18_credits.json","w"), indent=1)
print("credits ->", list(cr))
