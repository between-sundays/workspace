// POST /api/version  {page, filename?, html_b64?, url?, notes?}
const { auth, cors, appendLine, putFile, bad } = require("./_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { page, filename, html_b64, url, notes = "" } = req.body || {};
  const n = parseInt(page, 10);
  if (!n || n < 1 || n > 48) return bad(res, 400, "page must be 1-48");
  if (!html_b64 && !url) return bad(res, 400, "provide html_b64 or url");
  let stored = url || null;
  if (html_b64) {
    if (html_b64.length > 4_500_000) return bad(res, 413, "file too large (3MB max)");
    const safe = (filename || `page-${String(n).padStart(2,"0")}.html`)
      .replace(/[^a-zA-Z0-9._-]/g, "-");
    const path = `public/agents/${who.toLowerCase()}/${Date.now()}-${safe}`;
    await putFile(path, Buffer.from(html_b64, "base64"),
      `version: p${n} by ${who}\n\n${String(notes).slice(0,300)}`, "main");
    stored = "/" + path.replace(/^public\//, "");
  }
  const rec = { at: new Date().toISOString(), by: who, page: n, src: stored,
    notes: String(notes).slice(0, 1000) };
  await appendLine("versions.jsonl", JSON.stringify(rec),
    `[data] version p${n} · ${who}`);
  await appendLine("feed.jsonl", JSON.stringify({ at: rec.at, by: who, event: "version", page: n, src: stored }), `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec,
    note: html_b64 ? "committed to main — auto-deploys in ~1 min" : "recorded" });
};
