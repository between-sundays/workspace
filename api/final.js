// POST /api/final  {page, version}  — founder only.
const { auth, cors, appendLine, bad } = require("./_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  if (who !== "ADRIAN") return bad(res, 403, "select_final belongs to Adrian alone");
  const { page, version } = req.body || {};
  const n = parseInt(page, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!version) return bad(res, 400, "version required");
  const rec = { at: new Date().toISOString(), by: who, page: n,
    version: String(version).slice(0, 300) };
  await appendLine("finals.jsonl", JSON.stringify(rec),
    `[data] FINAL p${n} · founder`);
  await appendLine("feed.jsonl", JSON.stringify({ at: rec.at, by: who, event: "final", page: n }), `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
