#!/usr/bin/env python3
"""Find where a label can sit on a photograph without covering anybody.

Labels must land on empty ground, not on people. Detail = people; flat = asphalt.
So: measure local variance, blur it into a 'busy' map, then greedily place label
boxes in the quietest regions that do not collide with each other.
"""
import numpy as np
from PIL import Image, ImageFilter

def busy_map(img, blur=9):
    g = np.asarray(img.convert("L").filter(ImageFilter.GaussianBlur(0.6)), np.float32) / 255.0
    # local standard deviation = detail
    m = np.array(Image.fromarray((g * 255).astype(np.uint8)).filter(ImageFilter.BoxBlur(6)), np.float32) / 255.0
    sq = np.array(Image.fromarray(((g ** 2) * 255).astype(np.uint8)).filter(ImageFilter.BoxBlur(6)), np.float32) / 255.0
    var = np.clip(sq - m ** 2, 0, None)
    b = np.sqrt(var)
    b = np.array(Image.fromarray((b / (b.max() + 1e-6) * 255).astype(np.uint8))
                 .filter(ImageFilter.GaussianBlur(blur)), np.float32) / 255.0
    return b

def place(img, boxes, margin=18, tries=4000, seed=5):
    """boxes: list of (w,h). Returns [(x,y)] on the quietest non-overlapping spots."""
    W, H = img.size
    b = busy_map(img)
    rng = np.random.default_rng(seed)
    taken = []
    out = []
    for (bw, bh) in boxes:
        best = None
        for _ in range(tries):
            x = int(rng.integers(margin, max(margin + 1, W - bw - margin)))
            y = int(rng.integers(margin, max(margin + 1, H - bh - margin)))
            if any(not (x + bw + 14 < tx or tx + tw + 14 < x or
                        y + bh + 10 < ty or ty + th + 10 < y) for tx, ty, tw, th in taken):
                continue
            cost = float(b[y:y + bh, x:x + bw].mean())
            # nudge toward the edges so the centre of the picture stays open
            cx, cy = (x + bw / 2) / W - 0.5, (y + bh / 2) / H - 0.5
            cost -= 0.05 * (abs(cx) + abs(cy))
            if best is None or cost < best[0]:
                best = (cost, x, y)
        if best:
            _, x, y = best
            taken.append((x, y, bw, bh))
            out.append((x, y))
        else:
            out.append((margin, margin))
    return out
