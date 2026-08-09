// POST /api/prospect {handle, persona, url, signal, note?, stage?}
// A staging list, NOT a CRM — it exports. Record what was publicly observed and why they fit;
// do not store inferences about someone's beliefs, health, politics or anything like it.
const { auth, cors, appendLine, bad } = require("../_lib");
const STAGE = ["discovered","learning","worth-knowing","engaging","conversation","invited",
               "reader","creator","partner","ongoing","do-not-contact"];
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
    handle: String(b.handle).slice(0, 80),
    // A person may RESEMBLE several persona groups. They are never reduced to one.
    personas: (Array.isArray(b.persona) ? b.persona : [b.persona]).slice(0,4).map(x=>String(x).slice(0,40)),
    persona: String(Array.isArray(b.persona) ? b.persona[0] : b.persona).slice(0, 40),
    role: String(b.role || "").slice(0, 120),
    place: String(b.place || "").slice(0, 120),
    reach: String(b.reach || "").slice(0, 60),
    owner: String(b.owner || who).slice(0, 20),
    permission: String(b.permission || "none").slice(0, 40),
    url: String(b.url || "").slice(0, 400),
    signal: String(b.signal || "").slice(0, 500),   // what was publicly posted that made them a fit
    note: String(b.note || "").slice(0, 1200),
    stage: b.stage || "found", next: String(b.next || "").slice(0, 200) };
  await appendLine("prospects.jsonl", JSON.stringify(rec), `prospect: ${rec.handle} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
