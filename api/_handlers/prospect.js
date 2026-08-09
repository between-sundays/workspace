// POST /api/prospect {handle, persona, url, signal, note?, stage?}
// A staging list, NOT a CRM — it exports. Record what was publicly observed and why they fit;
// do not store inferences about someone's beliefs, health, politics or anything like it.
const { auth, cors, appendLine, bad } = require("../_lib");
const STAGE = ["found","researched","engaged","replied","warm","reader","passed"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.handle) return bad(res, 400, "handle required");
  if (!b.persona) return bad(res, 400, "persona required");
  if (b.stage && !STAGE.includes(b.stage)) return bad(res, 400, "stage must be " + STAGE.join("|"));
  const rec = { at: new Date().toISOString(), by: who,
    handle: String(b.handle).slice(0, 80), persona: String(b.persona).slice(0, 40),
    url: String(b.url || "").slice(0, 400),
    signal: String(b.signal || "").slice(0, 500),   // what was publicly posted that made them a fit
    note: String(b.note || "").slice(0, 1200),
    stage: b.stage || "found", next: String(b.next || "").slice(0, 200) };
  await appendLine("prospects.jsonl", JSON.stringify(rec), `prospect: ${rec.handle} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
