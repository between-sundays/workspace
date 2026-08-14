# The variance rule

Adrian, 2026-08-14: *"MIX UP THE STYLES. Need a ton of variance in our work to
keep it fresh... always mix styles, fonts, colors, patterns between concepts."*

He is right, and the reason Issue 001's first draft felt flat is simple: **48
pages, one style system.** Same two typefaces, same palette, same layout logic,
same flat process, every page. A reader senses that instantly even if they cannot
name it. It is the same failure as the AI tell, one level up.

## The rule

> **No page may share a style system with either page it faces or follows.**
> Every page declares its system before it is built, and the gate rejects a
> repeat.

Twenty-four systems are registered in `public/data/style-register.json` — Didone
newsprint, riso fluoro, wood-type letterpress, supermarket circular, Swiss quiet,
brush hand-lettered, hand-drawn data, data essay, one-ink comic, mail-order,
Riviera, cut-and-redacted, found paper, trade catalogue, puzzle page, neon,
woven, darkroom, shop vernacular, instrument panel, identity system, yearbook,
ledger, night field.

Each carries its own **typeface pairing, palette, ink count, and press process.**
Picking a system is picking all four at once — that is what stops variance
becoming random.

## What must actually change between neighbours

At minimum **three of these five**:

1. **Typeface pairing** — not just a different weight of the same family.
2. **Palette** — different hues, not a tint of the last one.
3. **Ink count** — one-ink pages next to four-colour pages is a rhythm, not an inconsistency.
4. **Process** — halftone, riso grain, letterpress impression, flat litho,
   photographed object, physically cut.
5. **Layout logic** — grid, poster, collage, table, panel, form, map.

## What holds it together instead of uniformity

A newspaper is coherent because of its **furniture**, not its skin. What stays
constant across every page, always:

- the folio: page number, section name, issue line
- the rule under the folio
- the Source Rule — a named verse, printed
- the trim, the margins, the fold
- the voice

Everything else is allowed — and expected — to change.

## Where new systems come from

`public/data/style-sources.json` — 35 curated sources: The Pudding, Information
is Beautiful, Dear Data, Fonts In Use, Archives.design, and the Cosmos boards
(posters, menus, colour, Olympic identities, neon, credits, cinematography,
portraiture), plus vernacular searches (classic advertising, shop signage,
Riviera, crossword, weaving, camera interfaces).

**Before designing any page, open a source you have not used recently.** A system
you have never borrowed from is worth more than a better execution of the one you
used last time.

## The gate

`tools/check_variance.py` reads the declared system of every page in reading
order and fails on:

- two consecutive pages sharing a system
- facing pages sharing a system
- any system used on more than 3 of 48 pages
- fewer than 12 distinct systems across the issue

A rule nobody enforces is how we got 48 identical pages the first time.
