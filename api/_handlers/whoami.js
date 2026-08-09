// GET /api/whoami — key check + onboarding pointer.
const { auth, cors } = require("../_lib");
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  const who = auth(req);
  res.status(who ? 200 : 401).json({
    ok: !!who, you: who || null,
    contract: "https://raw.githubusercontent.com/between-sundays/workspace/main/brain/how-to-contribute.md",
    constitution: "https://raw.githubusercontent.com/between-sundays/workspace/main/brain/brand-constitution.md",
  });
};
