# BTS Issue 001 — brightness correction + p18 rejected

**Date:** 2026-08-01

## Decisions

1. **Page 18 (THE OFFER / THE COUNTER-OFFER) is rejected.** Built, never deployed, moved to
   `public/lab/rejected/`. Adrian: "i don't like this one...don't use it."

2. **STANDING ART DIRECTION: stop making dark pages.** Adrian: "we need to get away from
   everything being dark and gloomy."

## The measurement behind it

Mean page brightness (0–255) across rendered versions:

| version | mean |
|---|---|
| v1 | 186.2 |
| v2 | 186.8 |
| v3 | 164.1 |
| v4 | 160.5 |
| lab (recent concept pages) | 158.5 |

The recent lab builds are the darkest work in the issue: p14 = 34 (93% of pixels near-black),
p18 = 70, p19 = 103, p04 = 130. Each new concept page was darker than the last. The paper was
sliding toward one continuous night.

## The rule going forward

- Default ground is **light** — cream/white — with black ink. Dark pages are a deliberate
  exception used for contrast, not the house style.
- Target: no more than ~1 in 6 pages predominantly dark, and never two dark pages adjacent.
- Colour comes from content and from pale colour-field blocks, not from darkness.
- Photography grades **high-key and airy** by default. The v4 duotone-into-shadow desk is
  retired as the default look.
- Check with the brightness script before shipping a page; anything under ~110 mean needs a
  reason.

This sits alongside the existing law: modern never vintage, no Bible characters depicted,
every page its own visual world.
