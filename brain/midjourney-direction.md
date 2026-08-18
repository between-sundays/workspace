# Directing Midjourney for Between Sundays

Adrian generates the imagery, Claude lays it out. This is the division that fixes
the illustration gap — see `print-craft.md`.

## The one rule that matters most

> **Never ask Midjourney for text.** Not a word, not a label, not a headline.

Its lettering is unreliable and it is the fastest way to make a page look
generated. **All typography is added in layout, by us, in real typefaces.** Ask
Midjourney for the photograph only. That also keeps the Source Rule honest —
scripture must be set from fetched text, never rendered by an image model.

## What we ask it for, and what we never ask it for

**Ask for:** places, crowds seen from above or behind, ordinary objects, weather,
light, empty rooms, textures, aerial geometry, hands.

**Never ask for:** anyone from the Bible (standing rule — choosing a face means
choosing skin, features and era), recognisable individuals, anything presented as
documentary fact, or a scene that implies a real event happened.

## Technical direction that actually changes the output

- `--ar 4:5` for a full page, `--ar 3:2` for a half-landscape, `--ar 2:3` for a
  half-portrait. Match the module, not the mood.
- `--style raw` — removes the house prettiness that reads as AI.
- `--v 7`
- Say the **camera position and lens** ("from a sixth-floor window, 35mm"), the
  **light** ("flat overcast, no hard shadows"), and the **ground** ("wet asphalt,
  worn crosswalk paint"). Those three do more than any adjective.
- Ask for **negative space**: "wide gaps of empty pavement between groups" — the
  labels need somewhere to sit.
- **Flat overcast light is the correct choice** for a labelled page. Hard shadow
  fights typography and makes label placement look accidental.

## Then it goes through the press

Every generated plate is halftoned into the page's ink before it prints —
`tools/press.py`. A raw Midjourney image dropped into a newspaper looks like a
raw Midjourney image. Screened into one or two inks on newsprint, it looks like a
photograph that was printed.
