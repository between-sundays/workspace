// POST /api/assignment {persona, brief, target?, status?}
// A standing job an agent can pick up: "find 25 people who fit this group".
const { auth, cors, appendLine, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const b = req.body || {};
  if (!b.persona) return bad(res, 400, "persona required");
  if (!b.brief || String(b.brief).length < 20) return bad(res, 400, "brief required");
  const rec = { at: new Date().toISOString(), by: who,
    persona: String(b.persona).slice(0, 40), brief: String(b.brief).slice(0, 2000),
    target: parseInt(b.target, 10) || 25,
    assignee: String(b.assignee || "any").slice(0, 20),
    status: ["open","claimed","delivered","closed"].includes(b.status) ? b.status : "open",
    note: String(b.note || "").slice(0, 900) };
  await appendLine("assignments.jsonl", JSON.stringify(rec), `assignment: ${rec.persona} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "assignment", body: `${rec.persona} — find ${rec.target}` }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
