// Shared helpers for the Between Sundays agent API.
const OWNER = "between-sundays", REPO = "workspace";
// Confidential shared state (briefs, comments, scores, finals) lives in a PRIVATE repo.
// The public workspace repo holds only the site and the page-review lab.
const STATE = process.env.STATE_REPO || "state";
const GH = "https://api.github.com";

function agents() {
  try { return JSON.parse(process.env.AGENT_KEYS || "{}"); } catch { return {}; }
}
// OPEN MODE — Adrian, 2026-08-09: "just unlock it for me right now, we can lock it
// down later." With OPEN_MODE on, a request with no key is treated as OPEN_AS
// (default ADRIAN) so the workspace needs no sign-in at all. A real key still wins
// and is still attributed to its owner. Turn this off by setting OPEN_MODE=off in
// Vercel and redeploying — nothing else changes.
function openMode() { return (process.env.OPEN_MODE || "on").toLowerCase() !== "off"; }
function auth(req) {
  const h = req.headers["x-agent-key"] ||
    (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  const who = agents()[h];
  if (who) return who;
  if (h) return null;                       // a wrong key is still a wrong key
  return openMode() ? (process.env.OPEN_AS || "ADRIAN") : null;
}
function cors(res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "content-type,x-agent-key,authorization");
  res.setHeader("Access-Control-Allow-Methods", "POST,GET,OPTIONS");
}
async function gh(path, opts = {}) {
  const r = await fetch(GH + path, {
    ...opts,
    headers: {
      Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "User-Agent": "bts-workspace-api",
      ...(opts.headers || {}),
    },
  });
  return r;
}
// Append one line to a JSONL file on the `data` branch (create if missing).
async function appendLine(path, line, message) {
  for (let attempt = 0; attempt < 4; attempt++) {
    const cur = await gh(`/repos/${OWNER}/${STATE}/contents/${path}?ref=main`);
    let sha, body = "";
    if (cur.status === 200) {
      const j = await cur.json();
      sha = j.sha;
      body = Buffer.from(j.content, "base64").toString("utf8");
      if (body.length && !body.endsWith("\n")) body += "\n";
    }
    const put = await gh(`/repos/${OWNER}/${STATE}/contents/${path}`, {
      method: "PUT",
      body: JSON.stringify({
        message, branch: "main",
        content: Buffer.from(body + line + "\n").toString("base64"),
        ...(sha ? { sha } : {}),
        committer: { name: "BTS Workspace API", email: "api@workspace.between-sundays" },
      }),
    });
    if (put.status === 200 || put.status === 201) return true;
    if (put.status !== 409 && put.status !== 422) {
      throw new Error(`github put ${put.status}: ${await put.text()}`);
    }
    await new Promise(r => setTimeout(r, 300 * (attempt + 1)));
  }
  throw new Error("append conflict retries exhausted");
}
// Write/overwrite a whole file on a branch.
async function putFile(path, content, message, branch, repo) {
  const R = repo || REPO;
  const cur = await gh(`/repos/${OWNER}/${R}/contents/${path}?ref=${branch}`);
  const sha = cur.status === 200 ? (await cur.json()).sha : undefined;
  const put = await gh(`/repos/${OWNER}/${R}/contents/${path}`, {
    method: "PUT",
    body: JSON.stringify({
      message, branch,
      content: Buffer.from(content).toString("base64"),
      ...(sha ? { sha } : {}),
      committer: { name: "BTS Workspace API", email: "api@workspace.between-sundays" },
    }),
  });
  if (put.status !== 200 && put.status !== 201)
    throw new Error(`github put ${put.status}: ${await put.text()}`);
}
function bad(res, code, msg) { res.status(code).json({ ok: false, error: msg }); }
module.exports = { auth, cors, appendLine, putFile, bad, openMode };
