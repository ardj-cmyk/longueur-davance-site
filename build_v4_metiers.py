#!/usr/bin/env python3
"""Pages métier au design v4 (prototype, noindex) : _v4-<slug>.html.

Lit les données de build_metiers.py SANS l'exécuter en entier (il réécrit les
pages en ligne à l'import). Le modèle est _proto-v4.html : même page que
l'accueil, en mode métier (body data-metier) : accroche du métier, écrans du
métier juste en dessous, puis « Ce qu'on vous retire », méthode, sites, contact.
"""
from pathlib import Path
import html, re
ICI = Path(__file__).parent
src = (ICI / "build_metiers.py").read_text(encoding="utf-8")
fin = src.index("\n}\n", src.index("METIERS = {")) + 3
ns = {"__file__": str(ICI / "build_metiers.py")}
exec(src[:fin], ns)
METIERS = ns["METIERS"]

# slug de page -> profil des écrans de démonstration (PROF dans _proto-v4.html)
PROFIL = {"avocat": "avocat", "comptable": "compta", "batiment": "btp", "immobilier": "immo",
          "architecte": "archi", "medical": "sante", "traiteur": "resto", "transport": "transport",
          "garage": "garage", "communication": "comm", "commercial": "commercial",
          "camping": "tourisme", "recrutement": "rh", "solo": "solo"}

modele = (ICI / "_proto-v4.html").read_text(encoding="utf-8")
CHECK = ('<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M5 9.5l2.5 2.5L13 6.5" '
         'stroke="#b4551e" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>')


M3D = """<section class="pad m3d-sec" id="maquette">
  <div class="wrap">
    <span class="eyebrow rv">Votre projet en 3D</span>
    <h2 class="title rv d1">Du plan à la maison, <em>avant le premier coup de pelle.</em></h2>
    <p class="lead rv d2">À partir de vos plans, votre client tourne autour de son projet sur son téléphone, enlève le toit, sépare les étages, regarde la lumière du matin au soir. Démonstration sur une maison fictive.</p>
    <div class="m3d rv" id="m3d">
      <canvas aria-label="Maquette 3D interactive d'une maison contemporaine"></canvas>
      <div class="m3d-ui">
        <button type="button" data-vue="3d" aria-pressed="true">Vue 3D</button>
        <button type="button" data-vue="plan" aria-pressed="false">Voir le plan</button>
        <button type="button" data-vue="coupe" aria-pressed="false">Voir la coupe</button>
        <button type="button" id="m3d-rejouer">Du plan à la 3D</button>
        <button type="button" id="m3d-toit" aria-pressed="false">Retirer le toit</button>
        <button type="button" id="m3d-etages" aria-pressed="false">Séparer les étages</button>
        <div class="m3d-sl">
          <label class="m3d-h">Lumière <input type="range" id="m3d-heure" min="7" max="21" step="0.25" value="16"><b id="m3d-heure-v">16 h</b></label>
          <label class="m3d-h">Coupe <input type="range" id="m3d-coupe" min="0.4" max="13.6" step="0.1" value="7.2"><b id="m3d-coupe-v">7,2 m</b></label>
        </div>
      </div>
      <p class="m3d-hint">Faites glisser pour tourner autour</p>
    </div>
  </div>
</section>
<script type="importmap">{"imports":{"three":"/assets/three/three.module.js"}}</script>
<script type="module" src="/assets/maquette-ld.js"></script>
"""
M3D_CSS = """<style>
.m3d{position:relative;margin-top:34px;border-radius:var(--r-lg);overflow:hidden;background:#f3ede2;border:1px solid var(--line);box-shadow:var(--sh)}
.m3d canvas{display:block;width:100%;height:clamp(380px,58vh,620px);touch-action:none;cursor:grab}
.m3d-ui{position:absolute;left:12px;right:12px;bottom:12px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.m3d-ui button,.m3d-h{font:600 13.5px var(--sans);background:rgba(253,252,249,.94);border:1px solid var(--line);border-radius:999px;padding:9px 14px;color:var(--ink);cursor:pointer;backdrop-filter:blur(6px);min-height:40px;display:inline-flex;align-items:center;gap:8px}
.m3d-ui button[aria-pressed=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}\n.m3d-ui{max-height:46%;overflow:auto}
.m3d-ui #m3d-rejouer{background:var(--accent);color:#fff;border-color:var(--accent)}
.m3d-h input{width:110px;accent-color:var(--accent)}\n.m3d-sl{flex-basis:100%;display:flex;gap:8px;flex-wrap:nowrap}\n.m3d-sl .m3d-h{flex:1;min-width:0;justify-content:space-between}.m3d-sl input{flex:1;min-width:60px;width:auto}
.m3d-hint{position:absolute;top:12px;left:50%;transform:translateX(-50%);font-size:12px;color:var(--muted);background:rgba(253,252,249,.85);padding:5px 12px;border-radius:999px;pointer-events:none}
@media(max-width:640px){.m3d canvas{height:380px}.m3d-ui{position:static;max-height:none;padding:10px;background:var(--paper);border-top:1px solid var(--line)}.m3d-sl{flex-wrap:wrap}.m3d-sl .m3d-h{flex:1 1 100%}.m3d-ui{gap:6px}.m3d-ui button,.m3d-h{font-size:12.5px;padding:8px 11px;min-height:38px}.m3d-h input{width:80px}}
</style>"""

def page(slug, m):
    e = html.escape
    t = modele
    t = re.sub(r"<title>.*?</title>", f"<title>{e(m['titre'])}</title>", t, count=1, flags=re.S)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{e(m["sub"][:155])}">', t, count=1)
    t = t.replace("<body>", f'<body data-metier="{PROFIL[slug]}">', 1)
    t = re.sub(r'(<span class="badge load" id="heroBadge"[^>]*><i></i>).*?(</span>)', lambda x: x.group(1) + e(m["pill"]) + x.group(2), t, count=1, flags=re.S)
    t = re.sub(r'(<h1 class="load" id="heroH1"[^>]*>).*?(</h1>)', lambda x: x.group(1) + e(m["h1"]) + x.group(2), t, count=1, flags=re.S)
    t = re.sub(r'(<p class="sub load" id="heroSub"[^>]*>).*?(</p>)', lambda x: x.group(1) + e(m["sub"]) + x.group(2), t, count=1, flags=re.S)
    items = "".join(f'<li class="rv">{CHECK}<span>{e(x[0].upper() + x[1:])}</span></li>' for x in m["taches"])
    bloc = f'''<section class="pad taches" id="taches">
  <div class="wrap">
    <span class="eyebrow rv">{e(m["nom"])}</span>
    <h2 class="title rv d1">Ce qu'on vous retire, <em>tâche par tâche.</em></h2>
    <p class="lead rv d2">{e(m.get("punch", ""))}</p>
    <ul class="tlist">{items}</ul>
    <div class="cta-row rv"><a class="btn" href="https://calendar.app.google/S5K8G7FLFWj4d4sF7" target="_blank" rel="noopener">Chiffrer les miennes en 30 min <span class="arr">→</span></a></div>
  </div>
</section>
'''
    if slug == "architecte":
        bloc = M3D + bloc
        t = t.replace("</head>", M3D_CSS + "\n</head>", 1)
    t = t.replace("<!--METIER-TACHES-->", bloc, 1)
    if m.get("faq"):
        q, r = m["faq"]
        t = t.replace('<div class="faq">', f'<div class="faq">\n      <details class="rv" open><summary>{e(q)}<i></i></summary><p>{e(r)}</p></details>', 1)
    return t

import sys
PROD = "--prod" in sys.argv
SITE = "https://longueur-davance.fr"

def prod(t, chemin, titre_og, desc_og):
    """Passe une page du prototype en page de production : indexable, canonical, partage, référencement, liens propres."""
    from seo import appliquer
    t = t.replace('<meta name="robots" content="noindex, nofollow">\n', '')
    t = appliquer(t, chemin.strip("/"), titre_og, desc_og)
    return t.replace('/_v4-', '/')

for slug, m in METIERS.items():
    if slug not in PROFIL: continue
    t = page(slug, m)
    if PROD:
        (ICI / f"{slug}.html").write_text(prod(t, f"/{slug}", m["h1"], m["sub"][:200]), encoding="utf-8")
        print("prod", slug)
    else:
        (ICI / f"_v4-{slug}.html").write_text(t, encoding="utf-8")
        print("ok", slug)

if PROD:
    accueil = prod(modele, "/", "Longueur d'avance · Audit IA et sites premium",
                   "On chiffre ce que vos tâches répétitives vous coûtent, puis on construit ce qui vous le rend : les bonnes automatisations, et un site qui fait venir les clients.")
    (ICI / "index.html").write_text(accueil, encoding="utf-8")
    print("prod index")
