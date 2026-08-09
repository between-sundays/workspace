#!/usr/bin/env python3
"""LIGHT photo desk — natural colour, lifted shadows, airy. Replaces the duotone desk."""
from PIL import Image, ImageEnhance
import os, warnings
warnings.simplefilter("ignore")
Image.MAX_IMAGE_PIXELS=None
RAW="photos/raw"; OUT="public/lab/photos"; os.makedirs(OUT,exist_ok=True)

def curve():                      # lift blacks, hold highlights
    t=[]
    for i in range(256):
        v=i/255
        v=0.13+0.87*(v**0.86)     # shadow lift + gentle gamma
        t.append(min(255,int(v*255)))
    return t
C=curve()

def light(src,dst,box,sat=1.14,warm=(1.035,1.005,0.965),grain=.022):
    im=Image.open(src).convert("RGB")
    W,H=box; ar=W/H; w,h=im.size
    if w/h>ar: nw=int(h*ar); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else:      nh=int(w/ar); im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
    im=im.resize((W,H),Image.LANCZOS)
    r,g,b=im.split()
    r=r.point(lambda v:min(255,int(C[v]*warm[0])))
    g=g.point(lambda v:min(255,int(C[v]*warm[1])))
    b=b.point(lambda v:min(255,int(C[v]*warm[2])))
    im=Image.merge("RGB",(r,g,b))
    im=ImageEnhance.Color(im).enhance(sat)
    im=ImageEnhance.Contrast(im).enhance(1.04)
    n=Image.effect_noise((W,H),11).convert("L")
    im=Image.blend(im,Image.merge("RGB",(n,n,n)),grain)
    im.save(os.path.join(OUT,dst),quality=93)
    px=list(im.convert("L").getdata())
    print(f"  {dst:22s} {W}x{H}  mean {sum(px)/len(px):5.1f}")

CELL=(232,333)
print("light desk:")
light(f"{RAW}/stone__5966a0aab2.jpg",  "l_stone.jpg",  CELL)
light(f"{RAW}/motel__56bd25ccdb.jpg",  "l_motel.jpg",  CELL, sat=1.22)
light(f"{RAW}/waiting__40482c3e4b.jpg", "l_window.jpg", CELL, sat=1.10)
light(f"{RAW}/stadium__ed88aea978.jpg", "l_seats.jpg",  CELL, sat=1.18)
