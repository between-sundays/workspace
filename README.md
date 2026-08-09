# Between Sundays — Workspace

The shared workspace for **Between Sundays** ("Good news. Printed.") — Issue 001
production, the brain, and the multi-agent contribution system.

- **Humans** work through the website (deployed from this repo).
- **Agents** (CLAUDE · MANUS · CODEX) contribute through the shared HTTP API and,
  where able, through git.
- **Nothing is deleted, only added and superseded.** Git history is the guarantee.
- **`select_final` belongs to Adrian alone.**

## Layout
| Path | What |
|---|---|
| `public/` | The deployed site — Issue 001 pages, all versions, compare tool |
| `brain/` | The constitution, contribution contract, decisions |
| `tools/` | Page builders, renderers, and the three checkers (overflow, collision, source-rule) |
| `api/` | Shared agent API (serverless) |
| `data/` | Shared state (versions index, briefs) |

## The standing rule
Nothing runs in the paper unless it is tied to at least one named Bible verse,
printed on the page. `tools/check_sourced.py` enforces it in CI.

Read `brain/how-to-contribute.md` before writing anything.
