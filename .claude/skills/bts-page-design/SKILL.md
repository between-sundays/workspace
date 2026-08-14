---
name: bts-page-design
description: Design a page for the Between Sundays newspaper. Use whenever building, rebuilding or art-directing any page of the paper, any poster, ad, cover, spread or printed artefact for BTS. Enforces the variance rule (never repeat a style system), the print-craft rules (real ink behaviour, never CSS-flat), the Source Rule (a named verse, fetched), and the no-depiction rule (never draw anyone from the Bible).
---

# Designing a Between Sundays page

Read this before laying out anything printed. The paper's failures have all come
from skipping one of these four steps.

## 1. Pick a style system you have not just used

`public/data/style-register.json` holds 24 systems. Each one bundles a **typeface
pairing, palette, ink count and press process** — picking a system picks all four,
which is what stops variance turning into randomness.

**Hard rule: no page may share a system with the page before it or the page it
faces.** At minimum three of these five must change between neighbours:
typeface pairing · palette · ink count · process · layout logic.

Declare it in the page's head, or the gate rejects the build:

```html
<meta name="style-system" content="riso-fluoro"/>
```

Then run `python3 tools/check_variance.py`.

**Before designing, open a source you have not used recently** —
`public/data/style-sources.json` has 35 (The Pudding, Dear Data, Fonts In Use,
Archives.design, the Cosmos boards, vernacular searches). A system you have never
borrowed from beats a better execution of the one you used last time.

## 2. Make it behave like ink, not like a screen

Never ship a flat CSS render. Run it through `tools/press.py`:

```python
import press
out = press.press(render, inks=[(36,26,18),(168,50,30)], angles=[15,75],
                  cell=4.0, solid_at=0.78, paper_tone=(247,242,231))
```

- **Type and rules are line art at 100%.** Only photographs and tints get a
  halftone screen. Screening the body text is the single most obvious tell.
- **Ink is transparent** — overlaps make a third colour.
- **The register slips.** A pixel or two per ink.
- **Paper is never `#ffffff`.**

## 3. Do not fake illustration

A shape standing in for a drawing always reads as a shape. Nine bars are not a
staircase; a gradient is not a night. If a page needs an illustration, either it
gets a real one (Adrian's hand, or commissioned) or **choose a concept that does
not need one** — type-led pages, object photography, found paper, physical
cutting, forms, grids, tables. Roughly a third of the concepts in
`public/data/concept-ledger.json` need no drawing at all.

Leave art slots **labelled and empty** rather than filled with a substitute.

## 4. Source it, and do not depict anyone

- **Every page carries at least one named Bible verse, printed.** Always *fetch*
  the text (`bolls.life`, NLT/MSG) — never quote from memory. Verses already
  fetched live in `public/data/verses-full.json`.
- **Never draw or depict any person from the Bible.** Not Jacob, not Jesus, not
  the disciples, not angels as figures. Choosing a face means choosing skin,
  features and era. Show places, objects, hands, crowds from behind, empty rooms,
  the aftermath.

## Before you call a page done

```bash
python3 tools/render_pages.py <dir> <page>
python3 tools/check_overflow.py public/<dir>      # nothing clipped
python3 tools/check_sourced.py public/<dir>       # a named verse present
python3 tools/check_variance.py                   # no repeated system
python3 tools/check_js.py                         # if the page carries script
```

Then **look at the render.** Every real defect in this project — the squashed
route, the vanished panel, the mushy type, the soft red — was found by looking,
not by reading the code.

## The constants that make it one newspaper

Variance is expected everywhere except here: the folio (page number, section,
issue line), the rule beneath it, the trim and margins, the Source Rule, and the
voice — messengers, not experts; the friend, not the teacher.
