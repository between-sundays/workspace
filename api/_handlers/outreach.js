// POST /api/outreach {handle, persona, channel, message, result?}
// One record per real attempt, so messaging gets tested instead of guessed at.
const { auth, cors, appendLine, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.handle || !b.persona) return bad(res, 400, "handle and persona required");
  if (!b.message) return bad(res, 400, "message required — record what was actually said");
  const rec = { at: new Date().toISOString(), by: who,
    handle: String(b.handle).slice(0, 80), persona: String(b.persona).slice(0, 40),
    channel: String(b.channel || "dm").slice(0, 30),
    message: String(b.message).slice(0, 2000),
    result: String(b.result || "sent").slice(0, 120) };
  await appendLine("outreach.jsonl", JSON.stringify(rec), `outreach: ${rec.handle} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "outreach", body: `${rec.persona} · ${rec.result}` }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
