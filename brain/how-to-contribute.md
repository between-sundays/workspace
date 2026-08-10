# How to contribute (humans and agents)

**Read `brain/brand-constitution.md` first.** It is the quality gate that has no CI check.

## The rules
1. **Additive only.** Add and supersede; never delete, never silently replace,
   never rewrite someone else's words. CI rejects deletions outside your namespace.
2. **Attributable.** Every version, comment, and flag carries its author:
   `CLAUDE` · `MANUS` · `CODEX` · `ADRIAN` · `LACEY`.
3. **Only Adrian selects finals.** A superseded final must be re-selected.
4. **Every page passes three gates before deploy:** overflow, collision, source-rule
   (`tools/check_overflow.py`, `tools/check_sourced.py`).
5. **A page needs a brief before an agent builds it.** Briefs live in `data/briefs/`.

## Namespaces
Agents write files under `public/<agent>/…` (e.g. `public/manus/`), shared page
variants under the version directories. The workspace code itself is maintained
by Claude; PRs welcome from Codex.

## Contribution paths
- **HTTP API** (standard, all agents) — LIVE at `https://bts-workspace.vercel.app/api/`.
  Auth: header `x-agent-key: <your key>`. All bodies JSON. Endpoints:
  - `GET  /api/whoami` — verify your key; returns links to this contract.
  - `POST /api/comment` `{page:1-48, type, body, re?}` — typed comment on a page.
  - `POST /api/score` `{page, version, score:1-10}` — `version` = the render src path.
  - `POST /api/version` `{page, filename?, html_b64?, url?, notes?}` — submit a page
    version (HTML ≤3MB commits to main and auto-deploys; or record an external URL).
  - `POST /api/brief` `{page, text}` — write/replace the page brief.
  - `POST /api/final` `{page, version}` — **founder key only.**
  - `GET  /api/state?path=…` — read shared state. **Requires your key.**
    Allowed paths: `comments/pNN.jsonl`, `scores.jsonl`, `versions.jsonl`,
    `finals.jsonl`, `feed.jsonl`, `briefs/pNN.md`.

  **Where things live.** Page renders and the review lab are public in
  `between-sundays/workspace`. Everything written by people and agents — briefs,
  comments, scores, finals — is append-only JSONL in the **private** repo
  `between-sundays/state`, reachable only through `/api/state` with a valid key.
  Never paste a key into a chat, an issue, a commit, or a page.

  **Submitted HTML is untrusted by default.** Anything posted to `/api/version`
  is served under `/agents/…` with a `Content-Security-Policy: sandbox` header:
  opaque origin, no scripts, no forms, no access to storage or the API. Build
  pages that stand on markup and CSS.
  Humans: the same actions via `/control-room.html` → Page Rooms.
- **Git** (power path): clone, commit in your namespace, push. Protected `main`,
  no force pushes.

## Comment types
`SCRIPTURE` · `FACT` · `LEGAL` · `DESIGN` · `VOICE` · `READABILITY` · `PRODUCTION` · `CONCEPT`
Flags are worked as review queues per page. An agent never approves its own work.

## The workspace itself

The site is the interface. `/` is the front page and lists every space:

| Space | What lives there |
|---|---|
| **What We Believe** | The constitution, the Source Rule, voice, the design law. Read first. |
| **Issue 001** | The Control Room (48 slots), Page Rooms, and the page-by-page comparison. |
| **Growth** | GTM, platforms, personas, messaging, creators. *Empty — questions only.* |
| **Logistics** | Print, packaging, unit costs, margin. *Empty — questions only.* |
| **Revenue** | Models, sponsorship, projections. *Empty — questions only.* |
| **Future Products** | Everything after the paper. *Empty — a parking lot with a roof.* |
| **How We Work** | This contract. |

The four business spaces are deliberately blank. They exist so the gaps are
visible instead of invisible, and each one carries the open questions it exists
to answer. Fill one with `POST /api/space {space, text}` — it renders
immediately, no deploy needed. Answer the questions in place; don't replace them
with a summary.

**House style for the workspace:** true white, black ink, grays between. Colour
only where content earns it. Newspaper structure. No dark dashboards.

## Issue 001 — the reset (2026-08-09)

All 48 pages are marked **not-ready**. Approved by Adrian: *"I don't think we
have any pages that are good enough for the 1st issue yet."*

Every existing version is preserved and reachable — nothing was deleted — but
**nothing is a finalist**. `compare.html` is now the Reference Archive, not the
working tool. The 1–10 scoring is retired: an 8.3 doesn't tell anyone what to do
next.

### The pipeline

`not-ready → brief-in-progress → brief-ready → exploring → direction-chosen →
build → team-review → issue-ready → locked`

Only Adrian can set **issue-ready** or **locked**, and locked comes last — after
a print proof. A page can look right alone and still fail beside its facing page.

### Verdicts, not scores

**Restart · Promising direction · Direction approved · Issue-ready.**
Every review answers four things: what's genuinely working (**keep**), what stops
it being ready (**change**), which standard it's missing (**why**), and what
should happen next (**next move**).

### The issue-ready gates

Red / amber / green, never percentages:

1. **Purpose** — it has a clear reason to exist
2. **Story** — it gives the reader something, not just something attractive
3. **Scripture** — rooted in at least one contextually valid passage
4. **Clarity** — a fifth-grade reader follows the main idea
5. **Newspaper DNA** — real hierarchy, structure and density (see `design-dna.md`)
6. **Originality** — doesn't read as generic or generated
7. **Rhythm** — works with the pages around it
8. **Production** — text, bleed, resolution and trim are correct

Gates 3 and 8 are already automated (`check_sourced.py`, `check_overflow.py`) and
report themselves. Humans judge 1, 2, 4, 5, 6 and 7 — don't spend a person on
what CI already does.

### The build order

**One anchor first, then seven, then the rest.** Serial until the language
exists; parallel after. The first anchor is **The Reading spread, pages 7–8** —
seven pages inherit its grid, type and rhythm, and if the reading experience
fails the paper fails regardless of the cover.

Then: cover, contents, visual explainer, activity page, directory, photo-led
spread, back cover. Those eight establish the system that finishes the other 40.

### Design against a named reference

Every page names the reference it's answering from `/library.html` and which of
the seven rules in `design-dna.md` it leans on. A page that can't name either is
a page nobody art-directed.

## Open mode (2026-08-09)

The workspace is **unlocked**. No sign-in, for reading *or* writing. Adrian:
*"just unlock it for me right now and we can lock it down later."*

- A request with no key is attributed to **ADRIAN** (`OPEN_AS`).
- A **valid key still wins** and is attributed to its owner — so agents keep their
  own byline by sending `x-agent-key`.
- A **wrong** key is still rejected.

**What this trades away:** the site is public and the URL is guessable, so anyone
who finds it can write, and it will be recorded as Adrian. Nothing here is
sensitive today, which is why this is fine for now — but it must be turned off
before the workspace holds anything that isn't.

**Agents must always send their key.** In open mode a keyless write is recorded
as *Adrian*, which quietly puts the founder's name on an agent's work. Claude did
exactly that with the first eight briefs and had to repost them. If you are an
agent, `x-agent-key` is not optional even though the door is open.

**To lock it down** — one setting, no code change:

```bash
vercel env add OPEN_MODE production   # value: off
```

Then redeploy. Keys go back to being required for every write, `select_final`
returns to founder-key-only, and reading stays public unless we change that too.
