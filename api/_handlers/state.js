// GET /api/state?path=…  — authenticated read of the private state repo.
// Confidential material (briefs, comments, scores, finals) never leaves this endpoint
// unauthenticated. The page-review lab (renders) stays public and is NOT served here.
const { auth, cors, bad } = require("../_lib");
const OWNER = "between-sundays", STATE_REPO = process.env.STATE_REPO || "state";
const OK = /^(comments\/p[0-4][0-9]\.jsonl|scores\.jsonl|versions\.jsonl|finals\.jsonl|feed\.jsonl|briefs\/p[0-4][0-9]\.md|spaces\/[a-z-]+\.md|inbox\.jsonl|well\.jsonl|well\/[a-z0-9-]+\.jsonl|reactions\.jsonl|statuses\.jsonl|constellations\.jsonl|personas\.jsonl|prospects\.jsonl|outreach\.jsonl|territories\.jsonl|messages\.jsonl)$/;
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const path = String((req.query && req.query.path) || "");
  if (!OK.test(path)) return bad(res, 400, "path not allowed");
  const r = await fetch(
    `https://api.github.com/repos/${OWNER}/${STATE_REPO}/contents/${path}?ref=main`,
    { headers: { Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
        Accept: "application/vnd.github+json", "User-Agent": "bts-workspace-api" } });
  if (r.status === 404) { res.setHeader("content-type", "text/plain"); return res.status(200).send(""); }
  if (!r.ok) return bad(res, 502, `state read failed (${r.status})`);
  const j = await r.json();
  res.setHeader("content-type", "text/plain; charset=utf-8");
  res.setHeader("cache-control", "no-store");
  res.status(200).send(Buffer.from(j.content, "base64").toString("utf8"));
};
