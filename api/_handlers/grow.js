// POST /api/grow {id, lens, text, refs?}  — build on somebody's seed.
// The Source Rule applies: a seed can't reach "ready" without at least one named verse.
const { auth, cors, appendLine, bad } = require("../_lib");
const LENS = ["SOMETHING-HERE","SCRIPTURE","STORY","PARABLE","BLUE-SKY","CREATIVE","VISUAL",
              "CONNECTION","DESTINATION","QUESTION"];
const BOOK = /\b(Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|1 Samuel|2 Samuel|1 Kings|2 Kings|1 Chronicles|2 Chronicles|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|1 Corinthians|2 Corinthians|Galatians|Ephesians|Philippians|Colossians|1 Thessalonians|2 Thessalonians|1 Timothy|2 Timothy|Titus|Philemon|Hebrews|James|1 Peter|2 Peter|1 John|2 John|3 John|Jude|Revelation)\s+\d{1,3}:\d{1,3}/;
module.exports = async (req, res) => {
  cors(res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return bad(res, 405, "POST only");
  const who = auth(req);
  if (!who) return bad(res, 401, "unknown or missing x-agent-key");
  const { id, lens = "STORY", text, refs = [] } = req.body || {};
  if (!id || !/^[a-z0-9-]{3,60}$/.test(id)) return bad(res, 400, "valid seed id required");
  if (!LENS.includes(lens)) return bad(res, 400, "lens must be one of " + LENS.join("|"));
  if (!text || String(text).length < 10) return bad(res, 400, "text required");
  const list = (Array.isArray(refs) ? refs : [refs]).map(String).filter(r => BOOK.test(r));
  if (lens === "SCRIPTURE" && !list.length)
    return bad(res, 400, "a SCRIPTURE growth needs at least one named reference, e.g. Genesis 28:16");
  const rec = { at: new Date().toISOString(), by: who, lens,
    text: String(text).slice(0, 8000), refs: list };
  await appendLine(`well/${id}.jsonl`, JSON.stringify(rec), `well: ${lens} on ${id} · ${who}`);
  await appendLine("feed.jsonl",
    JSON.stringify({ at: rec.at, by: who, event: "grow", seed: id, lens }), `feed · ${who}`).catch(()=>{});
  res.status(201).json({ ok: true, posted: rec });
};
