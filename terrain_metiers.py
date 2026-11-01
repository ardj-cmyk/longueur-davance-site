"""Injecte la section « Sur le terrain » et les questions du métier dans les 14 pages métier.

Idempotent : la section porte id="terrain", les questions ajoutées portent data-terrain,
le style porte id="terrain-css". Contenu dans metiers_terrain.py.

    python3 terrain_metiers.py
"""
import html, json, re
from pathlib import Path
from metiers_terrain import TERRAIN

ICI = Path(__file__).parent
e = html.escape

CSS = """<style id="terrain-css">
.terrain .cas{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:36px}
.terrain .cas article{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:24px;display:flex;flex-direction:column;gap:10px}
.terrain .cas h3{font-family:var(--serif);font-size:21px;line-height:1.2;margin:0}
.terrain .cas p{margin:0;color:var(--muted);font-size:15.5px}
.terrain .cas .limite{margin-top:auto;padding-top:12px;border-top:1px dashed var(--line);font-size:14.5px;color:var(--ink)}
.terrain .cas .limite b{color:var(--accent);font-weight:600}
.terrain .reperes{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px;margin-top:36px}
.terrain .reperes div{border-left:3px solid var(--accent);padding:4px 0 4px 16px}
.terrain .reperes b{display:block;font-family:var(--serif);font-size:26px;line-height:1.1;color:var(--accent)}
.terrain .reperes span{display:block;margin-top:6px;color:var(--muted);font-size:14.5px}
.terrain .source{margin-top:12px;font-size:13px;color:var(--muted)}
.terrain .refus{margin-top:36px;background:var(--accent-soft);border-radius:18px;padding:22px 24px}
.terrain .refus h3{font-family:var(--serif);font-size:20px;margin:0 0 10px}
.terrain .refus ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:8px}
@media(max-width:860px){.terrain .cas{grid-template-columns:1fr}}
</style>
"""


def section(m, t):
    reperes = ""
    if t.get("reperes"):
        r = t["reperes"]
        items = "".join(f"<div><b>{e(v)}</b><span>{e(l)}</span></div>" for v, l in r["items"])
        reperes = f'\n    <div class="reperes rv d2">{items}</div>\n    <p class="source rv">{e(r["note"])}</p>'
    cas = "".join(
        f'<article class="rv"><h3>{e(titre)}</h3><p>{e(fait)}</p><p class="limite"><b>La limite qu\'on vous dit :</b> {e(limite)}</p></article>'
        for titre, fait, limite in t["cas"])
    refus = "".join(f"<li>{e(x)}</li>" for x in t["refus"])
    return f"""
<section class="pad terrain" id="terrain" style="background:var(--surface);border-block:1px solid var(--line)">
  <div class="wrap">
    <span class="eyebrow rv">Sur le terrain</span>
    <h2 class="title rv d1">{t["titre"]}</h2>
    <p class="lead rv d2">{e(t["intro"])}</p>{reperes}
    <div class="cas">{cas}</div>
    <div class="refus rv"><h3>Ce qu'on ne fera pas chez vous</h3><ul>{refus}</ul></div>
  </div>
</section>
"""


def appliquer(m, t):
    f = ICI / f"{m}.html"
    h = f.read_text(encoding="utf-8")
    # nettoyage d'un passage précédent
    h = re.sub(r'<style id="terrain-css">.*?</style>\n', "", h, flags=re.S)
    h = re.sub(r'\n<section class="pad terrain" id="terrain".*?</section>\n', "", h, flags=re.S)
    h = re.sub(r'\s*<details class="rv" data-terrain>.*?</details>', "", h, flags=re.S)

    h = h.replace("</head>", CSS + "</head>", 1)
    fin_taches = h.index("</section>", h.index('id="taches"')) + len("</section>")
    h = h[:fin_taches] + "\n" + section(m, t) + h[fin_taches:]

    # questions du métier, juste après la première question (ouverte)
    faq = "".join(f'\n      <details class="rv" data-terrain><summary>{e(q)}<i></i></summary><p>{e(r)}</p></details>' for q, r in t["faq"])
    ouverte = h.index("</details>", h.index('<div class="faq">')) + len("</details>")
    h = h[:ouverte] + faq + h[ouverte:]

    # même questions dans les données structurées FAQPage
    def ld(mt):
        d = json.loads(mt.group(2))
        for x in d.get("@graph", [d]):
            if x.get("@type") == "FAQPage":
                noms = {q["name"] for q in x["mainEntity"]}
                for q, r in t["faq"]:
                    if q not in noms:
                        x["mainEntity"].insert(1, {"@type": "Question", "name": q,
                                                   "acceptedAnswer": {"@type": "Answer", "text": r}})
        return mt.group(1) + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + mt.group(3)
    h = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', ld, h, count=1, flags=re.S)
    f.write_text(h, encoding="utf-8")


if __name__ == "__main__":
    for m, t in TERRAIN.items():
        appliquer(m, t)
        print("terrain", m)
