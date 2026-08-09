// POST /api/seed {word, note?}  — drop something in The Well. Raw is fine. Rambling is fine.
const { auth, cors, appendLine, bad } = require("../_lib");
const slug = s => String(s).toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"").slice(0,42);
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { word, note = "" } = req.body || {};
  if (!word || String(word).trim().length < 2) return bad(res, 400, "word required");
  const id = slug(word) + "-" + Math.random().toString(36).slice(2, 6);
  const rec = { id, at: new Date().toISOString(), by: who, word: String(word).trim().slice(0, 120),
    note: String(note).slice(0, 6000), status: "raw" };
  await appendLine("well.jsonl", JSON.stringify(rec), `well: ${rec.word} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "seed", body: rec.word }), `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
