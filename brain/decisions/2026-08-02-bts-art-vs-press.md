# BTS — Adrian makes the art, Claude is the press (re-stated)

**Date:** 2026-08-02

Adrian sent three images (flowchart, "The bloom wasn't the beginning", "Keep the Evidence").
Claude treated them as style references and rebuilt two of them from scratch in CSS/SVG.

**Adrian:** "i did not want you recreating images... if you did that, it's wrong."

## The rule

An image from Adrian is **finished page artwork**. It gets placed, not redrawn.
Claude only builds a page from scratch when Adrian explicitly asks for it.

Placement flow: locate the export (usually `~/Downloads`, UUID-named) →
`public/lab/art/` → `place_art.py` → `render_pages.py`. Full bleed at 941×1346.
Nothing added — no masthead, no folio, no captions.

## Placed this session

| Page | Artwork |
|---|---|
| 14 | The bloom wasn't the beginning (Genesis 28:16) |
| 41 | A Flowchart for the In-Between (Psalm 32:8) |
| 45 | Keep the Evidence (Psalm 77:11) |

Claude's superseded rebuilds moved to `bts-web/superseded/`.

## Open blocker — print resolution

The exports are ~1049 × 1500 px = **~80 dpi** at 332 × 475 mm trim.
Press needs **3921 × 5610** (300 dpi). Good enough for the digital review build;
every placed artwork must be re-exported at full size before the print PDF is made.
