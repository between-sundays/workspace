// POST /api/react {id, reaction}  — teaches the system what Between Sundays finds meaningful.
const { auth, cors, appendLine, bad } = require("../_lib");
const R = ["something-here","push-further","too-obvious","not-us","scripture-needs-work",
           "strong-visual","save-for-later","build-this"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { id, reaction } = req.body || {};
  if (!id || !/^[a-z0-9-]{3,60}$/.test(id)) return bad(res, 400, "valid seed id required");
  if (!R.includes(reaction)) return bad(res, 400, "reaction must be one of " + R.join("|"));
  const rec = { at: new Date().toISOString(), by: who, id, reaction };
  await appendLine("reactions.jsonl", JSON.stringify(rec), `react: ${reaction} on ${id} · ${who}`);
  res.status(201).json({ ok: true, posted: rec });
};
