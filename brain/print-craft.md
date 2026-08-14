# Print craft — why our pages read as machine-made, and the fix

Adrian, 2026-08-14: *"AI has this obvious tell... there's no emotion, character,
feel, uniqueness. A lot of what we're making feels made for web, not print."*

He is right, and the diagnosis is not "try harder." It is structural.

## What actually gives it away

Every page so far was **drawn by CSS in a browser**. That means:

- **Perfect geometry.** True circles, exact rectangles, mathematically even
  spacing. Nothing in a printed object is that exact.
- **Flat, opaque colour.** One layer, no overlap. Real ink is transparent —
  where two inks cross they make a third colour. Every page we made has zero
  overprint, so it reads as screen.
- **No substrate.** No paper tooth, no show-through from the reverse, no
  absorbency. The white is #ffffff, which is a colour paper has never been.
- **No process.** No halftone rosette, no dot gain, no misregistration, no
  impression, no ink starvation at the edge of a heavy solid.
- **No hand.** Every letter is a font placed at a computed coordinate. No
  drawn letterform, no uneven baseline, no pressure change.
- **Web-native shapes.** Rounded corners, drop shadows, uniform stroke weight,
  the flat-vector idiom. This is the tell people recognise instantly.

The reference library proves the point: the pieces with the most life —
*THIS IS YOUR ASSIGNMENT*, the canoe on a sea of painted words, the Grant Snider
comics, the cut-away poem, the taped notes, the vision-board of found paper —
contain **almost no typesetting at all.** They are photographs of physical things
or entirely hand-drawn.

## The rule that follows

> **If a page could have been produced by asking a machine for it, it is not
> finished.**

Pinned in the library as ref 195 — an AI-generated comic panel. Technically
competent, zero authorship, indistinguishable from every other one of its kind.
That is the standard we measure against, in the negative.

## Three ways a page earns its life

1. **Photograph a real object.** A stone. A guest check with PAID IN FULL written
   across it. A taped note on a bus shelter. Scanned, not simulated.
2. **Draw or letter it by hand.** Adrian's brush, Adrian's pen. Uneven is the
   point — the wobble in the border is the personality.
3. **Print through a real process.** Halftone the image into one ink. Overprint
   two inks and let the third colour happen. Allow the register to slip.

Anything else is placement, not design.

## What we stop doing

- No CSS circles standing in for illustration.
- No flat colour fields without ink behaviour underneath them.
- No "shape as picture" — nine bars are not a staircase.
- No page whose whole visual argument is typography on a coloured rectangle.

## Standing rule, non-negotiable

> **We never draw or depict any person from the Bible.** Not Jacob, not Jesus,
> not the disciples, not the angels as figures. It becomes political the moment
> a face is chosen — skin, features, era, all of it — and that argument is not
> ours to start. We show places, objects, hands, crowds from behind, empty rooms,
> the aftermath. The absence is our discipline, and it is also why the
> ordinary-places photography and the object pages matter so much: they are the
> whole visual language available to us, so they have to be excellent.

## Web vs print — the working distinction

The workspace (bts-workspace.vercel.app) is software: screens, hover states,
a design system. **The paper is not software.** It is ink on newsprint at
332 × 475 mm, read at arm's length, in a hand, once. Nothing about how the
workspace looks should influence how the paper looks, and until now it has.


## Variance is part of craft, not separate from it

One style system across 48 pages reads as flat even when each page is competent.
See `style-variance.md` and `public/data/style-register.json` — 24 systems, each
bundling typeface, palette, ink count and process. No page may share a system
with its neighbour or the page it faces. Enforced by `tools/check_variance.py`.

Its first run over Issue 001's draft: **48 pages, 0 distinct systems declared.**
That number is the flatness, measured.
