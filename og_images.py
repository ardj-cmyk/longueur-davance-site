#!/usr/bin/env python3
"""Images de partage 1200x630 (og/<slug>.png) et icônes, rendues par Chrome sans écran.
Relancer après un changement d'accroche : python3 og_images.py"""
import html, subprocess, tempfile, sys
from pathlib import Path
ICI = Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
src = (ICI / "build_metiers.py").read_text(encoding="utf-8")
fin = src.index("\n}\n", src.index("METIERS = {")) + 3
ns = {"__file__": str(ICI / "build_metiers.py")}; exec(src[:fin], ns)
M = ns["METIERS"]
MARK = ('<svg viewBox="0 0 64 64" width="{s}" height="{s}"><rect width="64" height="64" rx="12" fill="#b4551e"/>'
        '<path d="M14 44 L30 28 L38 36 L52 18" stroke="#fdfcf9" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FONTS = "".join(f"@font-face{{font-family:'{f}';font-weight:400 800;{st}src:url({(ICI/'assets/fonts'/w).as_uri()})}}"
                for f, w, st in [("Inter", "Inter-latin.woff2", ""), ("Playfair Display", "PlayfairDisplay-latin.woff2", ""),
                                 ("Playfair Display", "PlayfairDisplay-italic-latin.woff2", "font-style:italic;")])
CARTES = {"accueil": ("Audit IA · Sites premium", "Votre entreprise perd du temps à l'intérieur, et des clients à l'extérieur."),
          "verdict": ("Le Verdict", "Une promesse IA vérifiée à la source, avant de l'acheter."),
          "modeles": ("Antisèche", "Quel modèle Claude pour quelle tâche, et à quel prix.")}
for slug, m in M.items():
    CARTES[slug] = (m["pill"], m["h1"])

def rendu(chemin_html, sortie, w, h):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", f"--screenshot={sortie}", chemin_html.as_uri()],
                   check=True, capture_output=True, timeout=60)

(ICI / "og").mkdir(exist_ok=True)
tmp = Path(tempfile.mkdtemp())
for slug, (pill, titre) in CARTES.items():
    taille = 74 if len(titre) < 48 else 62 if len(titre) < 70 else 54
    page = f"""<!doctype html><meta charset="utf-8"><style>{FONTS}
*{{margin:0;box-sizing:border-box}}html,body{{width:1200px;height:630px;overflow:hidden}}
body{{background:#fdfcf9;color:#12192b;font-family:Inter;padding:72px 84px;display:flex;flex-direction:column;justify-content:space-between;
background-image:radial-gradient(circle at 100% 0,#f3e3d6 0,transparent 46%)}}
.pill{{display:inline-flex;align-items:center;gap:12px;font:600 24px Inter;color:#b4551e;background:#f6e8dd;border-radius:999px;padding:12px 24px;align-self:flex-start}}
.pill i{{width:10px;height:10px;border-radius:50%;background:#b4551e}}
h1{{font:700 {taille}px/1.08 'Playfair Display';letter-spacing:-.01em;max-width:1000px}}
.pied{{display:flex;align-items:center;justify-content:space-between;font:600 26px Inter}}
.pied span{{display:flex;align-items:center;gap:16px}}.pied em{{font:500 24px Inter;font-style:normal;color:#6b6a66}}
.barre{{position:absolute;left:0;bottom:0;height:12px;width:100%;background:#b4551e}}</style>
<div class="pill"><i></i>{html.escape(pill)}</div><h1>{html.escape(titre)}</h1>
<div class="pied"><span>{MARK.format(s=52)}Longueur d'avance</span><em>longueur-davance.fr</em></div><div class="barre"></div>"""
    f = tmp / f"{slug}.html"; f.write_text(page, encoding="utf-8")
    rendu(f, ICI / "og" / f"{slug}.png", 1200, 630); print("og", slug)

# icônes : favicon.svg, 48 px, apple-touch 180 px, logo 512 px
(ICI / "favicon.svg").write_text(MARK.replace('width="{s}" height="{s}" ', 'xmlns="http://www.w3.org/2000/svg" '), encoding="utf-8")
for nom, s in [("favicon-48.png", 48), ("apple-touch-icon.png", 180), ("assets/logo-512.png", 512)]:
    f = tmp / "i.html"
    f.write_text(f'<!doctype html><style>*{{margin:0}}body{{background:#b4551e;width:{s}px;height:{s}px;overflow:hidden}}svg{{display:block}}</style>'
                 + MARK.format(s=s).replace('rx="12"', 'rx="0"' if nom != "favicon-48.png" else 'rx="12"'), encoding="utf-8")
    rendu(f, ICI / nom, s, s); print("icone", nom)
