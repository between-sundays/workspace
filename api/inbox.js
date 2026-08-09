// POST /api/inbox {kind, text, url?}  — the dump zone. Anything can enter fast, get sorted later.
const { auth, cors, appendLine, bad } = require("./_lib");
const KINDS = ["link","idea","screenshot","note","social","product","creator","prospect",
               "story","scripture","question","risk"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { kind = "note", text, url = null } = req.body || {};
  if (!KINDS.includes(kind)) return bad(res, 400, "kind must be one of " + KINDS.join("|"));
  if (!text || String(text).length < 2) return bad(res, 400, "text required");
  const rec = { at: new Date().toISOString(), by: who, kind,
    text: String(text).slice(0, 4000), url, status: "unsorted" };
  await appendLine("inbox.jsonl", JSON.stringify(rec), `inbox: ${kind} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "inbox", kind, body: rec.text.slice(0,140) }),
    `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
