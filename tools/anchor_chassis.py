"""The press chassis every anchor inherits — approved with Anchor 1, 2026-08-09."""
W,H=941,1346
BR="#2c1a12"; NAVY="#12233b"; BUT="#f2d79b"; SKY="#b0cfe8"; SAGE="#b6d3b0"; CREAM="#f7f3ec"
STONE="#8d7b6d"
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,800;1,500;1,700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Inter:wght@500;600;700;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Newsreader',Georgia,serif;background:#fff;color:%(BR)s}
.page{position:relative;width:%(W)spx;height:%(H)spx;overflow:hidden;background:#fff}
.folio{position:absolute;left:52px;right:52px;top:34px;display:flex;align-items:baseline;
 font-family:'Inter',sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.17em;
 text-transform:uppercase;z-index:5}
.folio .n{font-family:'Playfair Display',serif;font-size:19px;font-weight:700;letter-spacing:0}
.folio .sec{color:%(NAVY)s}
.folio .sp{flex:1}
.rule{position:absolute;left:52px;right:52px;height:1px;background:%(BR)s;opacity:.85;z-index:5}
.field{position:absolute;inset:0}
.arc{position:absolute;border-radius:50%%}
.kicker{font-family:'Inter',sans-serif;font-size:11px;font-weight:800;letter-spacing:.22em;
 text-transform:uppercase;color:%(NAVY)s}
.lab{font-family:'Inter',sans-serif;font-size:10px;font-weight:800;letter-spacing:.2em;
 text-transform:uppercase;color:%(NAVY)s}
.display{font-family:'Playfair Display',serif;font-weight:700;letter-spacing:-.024em;line-height:.95}
.display em{font-style:italic}
.body{font-size:15.4px;line-height:1.5;text-align:justify;hyphens:auto}
.body p{margin-bottom:8px;text-indent:14px}
.body p.lead{text-indent:0}
.vn{font-family:'Inter',sans-serif;font-size:8.8px;font-weight:800;vertical-align:.36em;
 color:%(NAVY)s;margin-right:2.5px}
.dc{font-family:'Playfair Display',serif;font-size:66px;line-height:.78;float:left;
 padding:6px 9px 0 0;font-weight:700}
.panel{background:#fff;padding:24px 28px 26px;position:absolute}
.credit{position:absolute;font-family:'Inter',sans-serif;font-size:9px;font-weight:700;
 letter-spacing:.14em;text-transform:uppercase;color:rgba(44,26,18,.5)}
.jump{position:absolute;font-family:'Inter',sans-serif;font-size:11px;font-weight:800;
 letter-spacing:.14em;text-transform:uppercase;color:%(NAVY)s}
.slot{border:1px dashed rgba(44,26,18,.34);display:flex;align-items:center;justify-content:center;
 text-align:center;font-family:'Inter',sans-serif;font-size:10px;font-weight:800;letter-spacing:.16em;
 text-transform:uppercase;color:rgba(44,26,18,.45);position:absolute}
""" % dict(W=W,H=H,BR=BR,NAVY=NAVY)

def folio(n, sec, left=True):
    if left:
        return (f'<div class="folio"><span class="n">{n}</span>&nbsp;&nbsp;'
                f'<span class="sec">{sec}</span><span class="sp"></span>'
                f'<span>Between Sundays &nbsp;·&nbsp; Issue 001</span></div>'
                f'<div class="rule" style="top:64px"></div>')
    return (f'<div class="folio"><span>Between Sundays &nbsp;·&nbsp; Issue 001</span>'
            f'<span class="sp"></span><span class="sec">{sec}</span>&nbsp;&nbsp;'
            f'<span class="n">{n}</span></div>'
            f'<div class="rule" style="top:64px"></div>')

def page(n, src_meta, inner, title):
    return f"""<!doctype html><html><head><meta charset="utf-8"/>
<meta name="bible-source" content="{src_meta}"/>
<title>BTS 001 — page {n}</title><style>{CSS}</style></head><body>
<div class="page">{inner}</div></body></html>"""
