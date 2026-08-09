// POST /api/space  {space, text}  — write a business space (Growth, Logistics, Revenue, Products).
const { auth, cors, putFile, appendLine, bad } = require("./_lib");
const OK = ["growth","logistics","revenue","products"];
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { space, text } = req.body || {};
  if (!OK.includes(space)) return bad(res, 400, "space must be one of " + OK.join("|"));
  if (!text || String(text).length < 20) return bad(res, 400, "text required");
  const doc = `${String(text).slice(0, 20000)}\n\n— ${who}, ${new Date().toISOString().slice(0,10)}\n`;
  await putFile(`spaces/${space}.md`, doc, `space: ${space} · ${who}`, "main",
    process.env.STATE_REPO || "state");
  await appendLine("feed.jsonl",
    JSON.stringify({ at: new Date().toISOString(), by: who, event: "space", space }),
    `feed: space ${space} · ${who}`);
  res.status(201).json({ ok: true, space });
};
