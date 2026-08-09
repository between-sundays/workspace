// POST /api/persona {id, name, ...}  — create or update a persona group.
// Personas describe OBSERVABLE PUBLIC SIGNALS ("posts about their small group"), never
// inferred protected attributes about a named individual. See brain/prospecting-ethics.md.
const { auth, cors, appendLine, putFile, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.id || !/^[a-z0-9-]{3,40}$/.test(b.id)) return bad(res, 400, "id required (kebab-case)");
  if (!b.name) return bad(res, 400, "name required");
  const rec = {
    at: new Date().toISOString(), by: who, id: b.id,
    name: String(b.name).slice(0, 80),
    ink: /^#[0-9a-f]{6}$/i.test(b.ink || "") ? b.ink : "#1b4f8a",
    who: String(b.who || "").slice(0, 900),
    signals: (b.signals || []).slice(0, 14).map(s => String(s).slice(0, 220)),
    where: (b.where || []).slice(0, 10).map(s => String(s).slice(0, 220)),
    recipes: (b.recipes || []).slice(0, 12).map(s => String(s).slice(0, 300)),
    angle: String(b.angle || "").slice(0, 700),
    ask: String(b.ask || "").slice(0, 400),
    objection: String(b.objection || "").slice(0, 500),
    refs: (b.refs || []).slice(0, 6).map(s => String(s).slice(0, 60)),
    size: String(b.size || "").slice(0, 120),
    territory: String(b.territory || "").slice(0, 40),
    moments: (b.moments || []).slice(0, 10).map(s => String(s).slice(0, 200)),
    theirWords: (b.theirWords || []).slice(0, 14).map(s => String(s).slice(0, 90)),
    avoidWords: (b.avoidWords || []).slice(0, 14).map(s => String(s).slice(0, 90)),
    notice: String(b.notice || "").slice(0, 500),
    distrust: String(b.distrust || "").slice(0, 500),
    reads: (b.reads || []).slice(0, 12).map(s => String(s).slice(0, 120)),
    offers: (b.offers || []).slice(0, 10).map(s => String(s).slice(0, 200)),
    open: (b.open || []).slice(0, 10).map(s => String(s).slice(0, 240)),
    // Every group stays a HYPOTHESIS until real conversations support it. Never quietly promoted.
    evidence: ["hypothesis","some-evidence","supported"].includes(b.evidence) ? b.evidence : "hypothesis",
    evidenceNote: String(b.evidenceNote || "").slice(0, 600),
  };
  await appendLine("personas.jsonl", JSON.stringify(rec), `persona: ${rec.name} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "persona", body: rec.name }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
