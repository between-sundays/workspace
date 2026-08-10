// POST /api/page {page, status, note?}  — where a page stands in the editorial pipeline.
// "locked" comes last, and only after a print proof: a page can look right alone and
// still fail once it sits next to its facing page.
const { auth, cors, appendLine, bad } = require("../_lib");
const S = ["not-ready","brief-in-progress","brief-ready","exploring","direction-chosen",
           "build","team-review","issue-ready","locked"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  const n = parseInt(b.page, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!S.includes(b.status)) return bad(res, 400, "status must be one of " + S.join("|"));
  // Only the founder declares a page issue-ready or locked.
  if (["issue-ready","locked"].includes(b.status) && who !== "ADRIAN")
    return bad(res, 403, "only Adrian can mark a page issue-ready or locked");
  const rec = { at: new Date().toISOString(), by: who, page: n, status: b.status,
    note: String(b.note || "").slice(0, 600) };
  await appendLine("pagestatus.jsonl", JSON.stringify(rec), `page ${n} → ${b.status} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
