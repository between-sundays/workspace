// POST /api/message — the Message Lab. One record per hypothesis, and one per real response.
// Turns what people actually said back into the language library.
const { auth, cors, appendLine, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.persona) return bad(res, 400, "persona required");
  if (!b.hypothesis) return bad(res, 400, "hypothesis required — say what you think will resonate");
  const rec = { at: new Date().toISOString(), by: who,
    persona: String(b.persona).slice(0,40),
    moment: String(b.moment||"").slice(0,200),
    hypothesis: String(b.hypothesis).slice(0,700),
    headline: String(b.headline||"").slice(0,200),
    opening: String(b.opening||"").slice(0,600),
    offer: String(b.offer||"").slice(0,300),
    channel: String(b.channel||"").slice(0,40),
    sent: parseInt(b.sent,10)||0, replies: parseInt(b.replies,10)||0,
    worked: String(b.worked||"").slice(0,700),
    flat: String(b.flat||"").slice(0,700),
    theirWords: (b.theirWords||[]).slice(0,12).map(s=>String(s).slice(0,300)),
    learned: String(b.learned||"").slice(0,900) };
  await appendLine("messages.jsonl", JSON.stringify(rec), `message lab: ${rec.persona} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "message", body: rec.persona+" — "+rec.hypothesis.slice(0,90) }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
