// POST /api/comment  {page, type, body, re?}
const { auth, cors, appendLine, bad } = require("./_lib");
const TYPES = ["SCRIPTURE","FACT","LEGAL","DESIGN","VOICE","READABILITY","PRODUCTION","CONCEPT","GENERAL"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { page, type = "GENERAL", body, re = null } = req.body || {};
  const n = parseInt(page, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!body || String(body).length < 2) return bad(res, 400, "body required");
  if (!TYPES.includes(type)) return bad(res, 400, "type must be one of " + TYPES.join("|"));
  const rec = { at: new Date().toISOString(), by: who, page: n, type,
    body: String(body).slice(0, 4000), re };
  await appendLine(`comments/p${String(n).padStart(2,"0")}.jsonl`,
    JSON.stringify(rec), `[data] comment p${n} · ${type} · ${who}`);
  await appendLine("feed.jsonl", JSON.stringify({ at: rec.at, by: who, event: "comment", page: n, type, body: String(body).slice(0,140) }), `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
