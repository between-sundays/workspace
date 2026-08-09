// POST /api/score  {page, version, score}
const { auth, cors, appendLine, bad } = require("./_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { page, version, score } = req.body || {};
  const n = parseInt(page, 10), s = parseInt(score, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!version) return bad(res, 400, "version required (render src)");
  if (!s || s < 1 || s > 10) return bad(res, 400, "score must be 1-10");
  const rec = { at: new Date().toISOString(), by: who, page: n,
    version: String(version).slice(0, 300), score: s };
  await appendLine("scores.jsonl", JSON.stringify(rec),
    `[data] score p${n}=${s} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
