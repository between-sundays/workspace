// POST /api/status {id, status}  — move a drop along. Nothing is ever deleted; "sleeping" is
// how an idea rests. "used" records where it finally appeared.
const { auth, cors, appendLine, bad } = require("../_lib");
const S = ["raw","developing","story-ready","ready-to-pull","sleeping","used"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { id, status, where = "" } = req.body || {};
  if (!id || !/^[a-z0-9-]{3,60}$/.test(id)) return bad(res, 400, "valid seed id required");
  if (!S.includes(status)) return bad(res, 400, "status must be one of " + S.join("|"));
  const rec = { at: new Date().toISOString(), by: who, id, status, where: String(where).slice(0,200) };
  await appendLine("statuses.jsonl", JSON.stringify(rec), `status: ${id} → ${status} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "status", seed: id, status }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
