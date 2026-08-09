# BTS — The positioning, the origin, and THE SOURCE RULE

**Date:** 2026-08-08 · stated by Adrian, in his own words

## Who BTS is (and is not)

We are NOT positioning as experts. Not Bible scholars. Not teachers.

- We are simply **messengers**. We are **the friend**.
- We are going on the journey too. We can be travel guides because we're not
  clueless — but we don't know it all.
- We're building this for **our own journey as believers**.
- A lot of what we share can literally be **"things we are learning."**
- We are not experts. But **we do know God. And we want to know him better.
  We want to make him proud. And we want other people to know him like we do.**

## The origin (Adrian, verbatim in substance)

The original reason BTS exists: **Adrian doesn't like reading.** Never learned to
like it; never learned to learn from a scholarly POV. Learned the system and
worked the system from 8th grade through college. But he wants to just
**"get in the word" and understand.** There have to be more ways to view and
dive into it — there are — **BTS (paper & future products) are that.**

This is now printed as the paper itself: press p03, "A Letter Before You Start,"
in Adrian's voice, signed Adrian & Lacey, anchored on Acts 4:13 ("ordinary men
with no special training in the Scriptures… recognized as men who had been
with Jesus").

## THE SOURCE RULE (hard rule, permanent)

> Everything created in the paper — full-page design or lengthy reading page —
> must be tied back to **at least 1 Bible verse**, sourced on the page.
> **"If it's Bible Sourced… we can not be wrong."**

The magic: there is no scenario in life that cannot be traced back to the Bible.

### Enforcement (built same day)

- `bts-web/check_sourced.py` — scans every built page for a named verse
  reference; exits 1 on any page without one. Runs with `check_overflow.py`
  as pre-deploy checks.
- Placed artwork carries its verse in the pixels; `place_art.py` now emits
  `<meta name="bible-source">` recording what the art says, so those pages are
  machine-checkable without altering the art.
- First audit: 14 pages flagged → 6 were placed art already sourced in-image
  (incl. p21, Psalm 105:5, verified by looking); 8 genuinely lacked a verse
  (press 28, 29; lab 05, 27, 32, 35, 42) — all fixed with real, fetched verses
  (Prov 27:17, Matt 13:34, Gen 32:10, Ps 139:7-12, Gen 28:11, 1 Kgs 19:12,
  Gal 6:2). All 40+ built pages now pass.
