// POST /api/brief  {page, text}
const { auth, cors, putFile, appendLine, bad } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { page, text } = req.body || {};
  const n = parseInt(page, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!text || String(text).length < 20) return bad(res, 400, "text required (a real brief)");
  const p = String(n).padStart(2, "0");
  const doc = `# Brief — Page ${p}\n*By ${who} · ${new Date().toISOString()}*\n\n${String(text).slice(0,6000)}\n`;
  await putFile(`briefs/p${p}.md`, doc, `brief p${n} · ${who}`, "main", process.env.STATE_REPO || "state");
  await appendLine("feed.jsonl",
    JSON.stringify({ at: new Date().toISOString(), by: who, page: n, event: "brief" }),
    `[data] feed: brief p${n} · ${who}`);
  res.status(201).json({ ok: true });
};
