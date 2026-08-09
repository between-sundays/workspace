// Single entry point for the whole agent API.
// Vercel's Hobby plan caps a deployment at 12 serverless functions, so every endpoint
// is dispatched from here instead of being its own file. Handlers live in _handlers/
// (the underscore keeps Vercel from routing them directly) and are unchanged otherwise.
const ROUTES = {
  whoami:        require("./_handlers/whoami"),
  state:         require("./_handlers/state"),
  comment:       require("./_handlers/comment"),
  score:         require("./_handlers/score"),
  version:       require("./_handlers/version"),
  final:         require("./_handlers/final"),
  brief:         require("./_handlers/brief"),
  space:         require("./_handlers/space"),
  inbox:         require("./_handlers/inbox"),
  seed:          require("./_handlers/seed"),
  grow:          require("./_handlers/grow"),
  react:         require("./_handlers/react"),
  status:        require("./_handlers/status"),
  constellation: require("./_handlers/constellation"),
  persona:       require("./_handlers/persona"),
  prospect:      require("./_handlers/prospect"),
  outreach:      require("./_handlers/outreach"),
};
module.exports = async (req, res) => {
  const action = String((req.query && req.query.action) || "").toLowerCase();
  const fn = ROUTES[action];
  if (!fn) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    return res.status(404).json({ ok: false, error: "no such endpoint",
      endpoints: Object.keys(ROUTES) });
  }
  try {
    return await fn(req, res);
  } catch (e) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    return res.status(500).json({ ok: false, error: String(e && e.message || e).slice(0, 300) });
  }
};
