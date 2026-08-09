// POST /api/constellation {name, ids[], note?}  — several drops turn out to be one story.
const { auth, cors, appendLine, bad } = require("./_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { name, ids, note = "" } = req.body || {};
  if (!name || String(name).length < 3) return bad(res, 400, "name required");
  const list = (Array.isArray(ids) ? ids : []).filter(i => /^[a-z0-9-]{3,60}$/.test(i));
  if (list.length < 2) return bad(res, 400, "a constellation needs at least two drops");
  const rec = { at: new Date().toISOString(), by: who, name: String(name).slice(0,120),
    ids: list, note: String(note).slice(0, 4000) };
  await appendLine("constellations.jsonl", JSON.stringify(rec), `constellation: ${rec.name} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
