#!/usr/bin/env python3
"""Pages ressources des vidéos Instagram (une page par vidéo, envoyée par ManyChat).
Contenu dans ressources_pages.py. Relancer : python3 ressources.py [slug ...] [--og]
Écrit <slug>.html (et og/<slug>.png avec --og). Même gabarit que modeles.html."""
import html, subprocess, sys, tempfile
from pathlib import Path
ICI = Path(__file__).parent
sys.path.insert(0, str(ICI))
from ressources_pages import PAGES

CSS = """@font-face{font-family:'Inter';font-style:normal;font-weight:400 800;font-display:swap;src:url(/assets/fonts/Inter-latin.woff2) format('woff2')}
@font-face{font-family:'Inter';font-style:normal;font-weight:400 800;font-display:swap;src:url(/assets/fonts/Inter-latinext.woff2) format('woff2');unicode-range:U+0100-02BA,U+1E00-1EFF}
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:600 900;font-display:swap;src:url(/assets/fonts/PlayfairDisplay-latin.woff2) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:600 900;font-display:swap;src:url(/assets/fonts/PlayfairDisplay-italic-latin.woff2) format('woff2')}
:root{--encre:#12192b;--ivoire:#fdfcf9;--fond:#faf6ee;--terra:#a3461a;--trait:#e3ded4;--doux:#5b6375;--vert:#2f6b45}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--fond);color:var(--encre);font:400 17px/1.6 'Inter',system-ui,sans-serif;padding:0 18px 64px}
main{max-width:640px;margin:0 auto}
a{color:var(--terra);font-weight:600}
header{padding:48px 0 28px;border-bottom:2px solid var(--encre);margin-bottom:28px}
.marque{font:700 13px/1 'Inter';letter-spacing:.14em;text-transform:uppercase;color:var(--terra)}
h1{font:800 clamp(32px,8.5vw,50px)/1.05 'Playfair Display',Georgia,serif;margin:14px 0 16px;text-wrap:balance}
h1 em{font-style:italic;color:var(--terra)}
.chapo{font-size:19px}
section{padding:28px 0;border-bottom:1px solid var(--trait)}
section>p+p,section>p+ul,section>ul+p,section>p+.cartes,section>.cartes+p{margin-top:12px}
h2{font:800 26px/1.15 'Playfair Display',Georgia,serif;margin-bottom:16px}
h2 .num{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:999px;background:var(--terra);color:var(--ivoire);font:800 19px 'Inter';margin-right:10px;vertical-align:4px}
h3{font:800 18px/1.25 'Inter';margin:18px 0 8px}
ul.liste{list-style:none;display:grid;gap:10px}
ul.liste li{padding-left:26px;position:relative}
ul.liste li::before{content:"";position:absolute;left:4px;top:.62em;width:9px;height:9px;border-radius:999px;background:var(--terra)}
.cartes{display:grid;gap:12px}
.carte{background:var(--ivoire);border:2px solid var(--encre);border-radius:16px;padding:14px 16px}
.carte .nom{font:800 18px/1.2 'Inter';margin-bottom:4px}
.carte .nom b{color:var(--terra)}
.carte p{font-size:16px}
.carte .prix{font:700 15px 'Inter';color:var(--terra);margin-top:6px}
.carte.ferme{background:#efeae0;border-style:dashed}
.encadre{background:var(--ivoire);border-left:5px solid var(--terra);border-radius:0 14px 14px 0;padding:14px 16px;font-size:16px}
.encadre+.encadre{margin-top:12px}
.encadre b:first-child{display:block;margin-bottom:2px}
.regle{background:var(--encre);color:var(--ivoire);border-radius:16px;padding:18px}
.regle h2{color:var(--ivoire);font-size:22px;margin-bottom:10px}
ol.etapes{list-style:none;display:grid;gap:12px;counter-reset:e}
ol.etapes>li{counter-increment:e;padding-left:40px;position:relative}
ol.etapes>li::before{content:counter(e);position:absolute;left:0;top:0;width:28px;height:28px;border-radius:999px;background:var(--terra);color:var(--ivoire);font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center}
.regle ol.etapes>li::before{background:var(--terra)}
pre{background:var(--encre);color:#f3efe6;border-radius:12px;padding:12px 14px;margin:8px 0;font:500 14px/1.5 ui-monospace,Menlo,monospace;white-space:pre-wrap;word-break:break-all}
code{font:500 .9em ui-monospace,Menlo,monospace;background:#efe8da;border-radius:6px;padding:1px 5px}
pre code{background:none;padding:0;font-size:inherit}
.avant-apres{display:grid;gap:10px}
.avant-apres div{border-radius:14px;padding:12px 14px;font-size:16px}
.avant-apres .av{background:#f3e3d6}
.avant-apres .ap{background:#e2efe5}
.avant-apres small{display:block;font:800 12px 'Inter';letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
.avant-apres .av small{color:var(--terra)}
.avant-apres .ap small{color:var(--vert)}
table{width:100%;border-collapse:collapse;font-size:15px;background:var(--ivoire);border:2px solid var(--encre);border-radius:16px;overflow:hidden}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--trait);vertical-align:top}
th{font:700 11px 'Inter';letter-spacing:.08em;text-transform:uppercase;color:var(--doux)}
td.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr:last-child td{border-bottom:0}
.tab{overflow-x:auto;-webkit-overflow-scrolling:touch}
details{background:var(--ivoire);border:2px solid var(--encre);border-radius:14px;margin-bottom:10px}
details summary{cursor:pointer;list-style:none;padding:13px 16px;font:800 17px 'Inter';display:flex;justify-content:space-between;align-items:center;gap:10px}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";font:800 22px 'Inter';color:var(--terra)}
details[open] summary::after{content:"–"}
details .dedans{padding:0 16px 14px}
details ol{padding-left:22px;display:grid;gap:6px;font-size:16px}
.tag{display:inline-block;font:700 11px 'Inter';letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin-right:6px;vertical-align:2px}
.tag.app{background:#e2efe5;color:var(--vert)}
.tag.code{background:#f3e3d6;color:var(--terra)}
.note{margin-top:12px;font-size:15px;color:var(--doux)}
.sources{font-size:14px;color:var(--doux)}
.sources a{font-weight:500;color:var(--doux)}
.fin h2{margin-bottom:10px}
.cta{display:inline-block;margin-top:18px;background:var(--encre);color:var(--ivoire);text-decoration:none;font:800 18px 'Inter';padding:16px 26px;border-radius:999px;box-shadow:0 6px 0 var(--terra)}
.signature{margin-top:26px;color:var(--doux);font-size:15px}"""

FIN = """<section class="fin">
  <h2>Et maintenant ?</h2>
  <p>{fin}</p>
  <a class="cta" href="/">Le premier échange est gratuit</a>
  <p class="signature">Amdy · Longueur d'avance. Suis-moi sur Instagram (<a href="https://www.instagram.com/ardj.87/">@ardj.87</a>), je décrypte l'IA sans bullshit, une notion par jour.</p>
</section>"""
FIN_DEFAUT = ("Ce que je fais avec les entreprises : je chiffre ce que leurs tâches répétitives leur coûtent, "
              "et je les accompagne pour les réduire avec l'IA. Sans jargon, sans dépendance.")


def page(slug, p):
    e = html.escape
    url = f"https://longueur-davance.fr/{slug}"
    sources = ""
    if p.get("sources"):
        liens = " · ".join(f'<a href="{u}">{e(t)}</a>' for t, u in p["sources"])
        sources = f'<section><p class="sources">Sources vérifiées le {p["verifie"]} : {liens}</p></section>'
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<style>
{CSS}
</style>
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(p["og_titre"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Longueur d'avance">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="https://longueur-davance.fr/og/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>
<body>
<main>
<header>
  <div class="marque">Longueur d'avance · {e(p["marque"])}</div>
  <h1>{p["h1"]}</h1>
  <p class="chapo">{p["chapo"]}</p>
</header>
{p["corps"].strip()}
{sources}
{FIN.format(fin=p.get("fin", FIN_DEFAUT))}
</main>
</body>
</html>
"""


def og(slugs):
    src = (ICI / "og_images.py").read_text(encoding="utf-8")
    debut = src.index("MARK = ")
    ns = {"ICI": ICI, "html": html, "subprocess": subprocess, "Path": Path,
          "CHROME": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
    exec(src[debut:src.index("CARTES = ")], ns)
    exec(src[src.index("def rendu"):src.index("(ICI / \"og\").mkdir")], ns)
    gabarit = src[src.index('    page = f"""'):src.index('    f = tmp / f"{slug}.html"')]
    tmp = Path(tempfile.mkdtemp())
    for slug in slugs:
        pill, titre = PAGES[slug]["og_pill"], PAGES[slug]["og_titre"]
        loc = dict(ns, pill=pill, titre=titre, taille=74 if len(titre) < 48 else 62 if len(titre) < 70 else 54)
        exec(gabarit.replace("    page = ", "page = ", 1).replace("\n    ", "\n"), loc)
        f = tmp / f"{slug}.html"; f.write_text(loc["page"], encoding="utf-8")
        ns["rendu"](f, ICI / "og" / f"{slug}.png", 1200, 630); print("og", slug)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    slugs = args or list(PAGES)
    for s in slugs:
        (ICI / f"{s}.html").write_text(page(s, PAGES[s]), encoding="utf-8"); print("page", s)
    if "--og" in sys.argv:
        og(slugs)
