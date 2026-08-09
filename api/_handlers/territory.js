// POST /api/territory {id, name, blurb, ink?, questions?}
const { auth, cors, appendLine, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.id || !/^[a-z0-9-]{3,40}$/.test(b.id)) return bad(res, 400, "id required (kebab-case)");
  if (!b.name) return bad(res, 400, "name required");
  const rec = { at: new Date().toISOString(), by: who, id: b.id,
    name: String(b.name).slice(0,80), ink: /^#[0-9a-f]{6}$/i.test(b.ink||"") ? b.ink : "#1b4f8a",
    blurb: String(b.blurb||"").slice(0,900),
    moments: (b.moments||[]).slice(0,12).map(s=>String(s).slice(0,200)),
    questions: (b.questions||[]).slice(0,12).map(s=>String(s).slice(0,240)) };
  await appendLine("territories.jsonl", JSON.stringify(rec), `territory: ${rec.name} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
