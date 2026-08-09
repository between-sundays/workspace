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
