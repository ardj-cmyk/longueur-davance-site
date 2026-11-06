"""Référencement des pages ressources : données structurées, page /ressources, sitemap.

À relancer après chaque nouvelle page ressource (ressources.py l'appelle à la fin).
Idempotent : réécrit le bloc JSON-LD marqué id="ld-ressource", la page /ressources
et sitemap.xml à partir des fichiers présents et de leurs dates dans git.

    python3 seo_ressources.py          # pages + sitemap
    python3 seo_ressources.py --og     # et l'image de partage de /ressources
"""
import html, json, re, subprocess, sys
from pathlib import Path

ICI = Path(__file__).parent
SITE = "https://longueur-davance.fr"
ORG = SITE + "/#org"
AUTEUR = {"@type": "Person", "@id": SITE + "/#amdy", "name": "Amdy Richard Diop Jouanguy",
          "url": SITE + "/", "sameAs": ["https://www.instagram.com/ardj.87/"]}
EDITEUR = {"@type": "Organization", "@id": ORG, "name": "Longueur d'avance",
           "url": SITE + "/", "logo": SITE + "/assets/logo-512.png"}
HUB = {
    "title": "Les guides IA pas à pas : Claude, ChatGPT et les outils",
    "desc": "Tous les guides de mes vidéos : installer Claude Code, choisir son forfait, réduire sa facture, écrire un skill, vérifier un outil. Pas à pas, vérifiés à la source.",
    "og_titre": "Les guides IA, pas à pas",
    "og_pill": "Ressources",
    "marque": "Ressources",
    "h1": "Les guides, <em>pas à pas</em>",
    "chapo": "Chaque vidéo a sa page : les étapes, les consignes à copier et les liens officiels. Les faits sont vérifiés à la source, la date est en bas de chaque guide.",
}
# Pages hors sitemap et hors liste, quoi qu'il arrive.
EXCLUES = {"index", "ressources"}

# Ordre et priorité des pages du site qui ne sont pas des ressources.
PRINCIPALES = [("", 1.0)] + [(m, 0.9) for m in (
    "avocat", "comptable", "batiment", "immobilier", "architecte", "medical", "traiteur", "garage",
    "transport", "camping", "recrutement", "communication", "commercial", "solo")] + [
    ("automatisation", 0.7), ("formation", 0.7), ("verdict", 0.6), ("ressources", 0.7)]


def git_date(f, premiere=False):
    args = ["git", "log", "--format=%cs", "--", f.name]
    if not premiere:
        args[2:2] = ["-1"]
    out = subprocess.run(args, cwd=ICI, capture_output=True, text=True).stdout.split()
    if not out:
        return None
    return out[-1] if premiere else out[0]


def lire(f):
    h = f.read_text(encoding="utf-8")
    g = lambda p: (re.search(p, h, re.S) or [None, None])[1]
    return h, {
        "title": html.unescape(g(r"<title>(.*?)</title>") or ""),
        "desc": html.unescape(g(r'<meta name="description" content="([^"]*)"') or ""),
        "marque": html.unescape(g(r'<div class="marque">Longueur d\'avance · (.*?)</div>') or ""),
        "sources": re.findall(r'<a href="(https?://[^"]+)"', g(r'<p class="sources">(.*?)</p>') or ""),
        "noindex": 'name="robots"' in h,
    }


def ressources():
    """Les pages du gabarit ressources, indexables, triées par nom."""
    pages = {}
    for f in sorted(ICI.glob("*.html")):
        slug = f.stem
        if slug.startswith("_") or slug in EXCLUES:
            continue
        h, m = lire(f)
        if m["marque"] and not m["noindex"]:
            pages[slug] = (f, h, m)
    return pages


def ld(objets):
    texte = json.dumps({"@context": "https://schema.org", "@graph": objets}, ensure_ascii=False, separators=(",", ":"))
    return f'<script type="application/ld+json" id="ld-ressource">{texte}</script>\n'


def fil(slug, nom):
    items = [("Accueil", SITE + "/"), ("Ressources", SITE + "/ressources")]
    if slug != "ressources":
        items.append((nom, f"{SITE}/{slug}"))
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def injecter(h, bloc):
    h = re.sub(r'<script type="application/ld\+json" id="ld-ressource">.*?</script>\n', "", h, flags=re.S)
    return h.replace("</head>", bloc + "</head>", 1)


def article(slug, f, m):
    url = f"{SITE}/{slug}"
    a = {"@type": "Article", "@id": url + "#article", "headline": m["title"][:110],
         "description": m["desc"], "url": url, "mainEntityOfPage": url,
         "image": f"{SITE}/og/{slug}.png", "inLanguage": "fr-FR",
         "author": AUTEUR, "publisher": EDITEUR}
    pub, mod = git_date(f, premiere=True), git_date(f)
    if pub:
        a["datePublished"] = pub
    if mod:
        a["dateModified"] = mod
    if m["sources"]:
        a["citation"] = m["sources"]
    return [a, fil(slug, m["title"])]


def groupe(marque):
    """« Les bases de l'IA · 11 » → (« Les bases de l'IA », 11)."""
    nom, _, num = marque.rpartition(" · ")
    if num.isdigit():
        return nom, int(num)
    return marque, 999


def page_hub(pages):
    from ressources import page  # gabarit commun des pages ressources
    groupes = {}
    for slug, (f, h, m) in pages.items():
        nom, num = groupe(m["marque"])
        groupes.setdefault(nom, []).append((num, m["title"], slug, m["desc"]))
    e = html.escape
    corps = []
    for nom in sorted(groupes, key=lambda n: (-len(groupes[n]), n)):
        cartes = "\n".join(
            f'    <a class="carte" href="/{slug}" style="text-decoration:none;color:inherit"><div class="nom"><b>{e(t)}</b></div><p>{e(d)}</p></a>'
            for _, t, slug, d in sorted(groupes[nom]))
        corps.append(f'<section>\n  <h2>{e(nom)}</h2>\n  <div class="cartes">\n{cartes}\n  </div>\n</section>')
    p = dict(HUB, corps="\n\n".join(corps))
    h = page("ressources", p)
    liste = {"@type": "CollectionPage", "@id": SITE + "/ressources#page", "name": HUB["title"],
             "description": HUB["desc"], "url": SITE + "/ressources", "inLanguage": "fr-FR",
             "publisher": EDITEUR, "mainEntity": {"@type": "ItemList", "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{s}", "name": pages[s][2]["title"]}
                 for i, s in enumerate(pages)]}}
    return injecter(h, ld([liste, fil("ressources", "")]))


def sitemap(pages):
    lignes = []
    for slug, prio in PRINCIPALES + [(s, 0.6) for s in pages]:
        f = ICI / f"{slug or 'index'}.html"
        if not f.exists():
            continue
        date = git_date(f) or "2026-11-01"
        lignes.append(f"  <url><loc>{SITE}/{slug}</loc><lastmod>{date}</lastmod><priority>{prio:.1f}</priority></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(lignes) + "\n</urlset>\n")


def main(og=False):
    pages = ressources()
    for slug, (f, h, m) in pages.items():
        neuf = injecter(h, ld(article(slug, f, m)))
        if neuf != h:
            f.write_text(neuf, encoding="utf-8")
    (ICI / "ressources.html").write_text(page_hub(pages), encoding="utf-8")
    (ICI / "sitemap.xml").write_text(sitemap(pages), encoding="utf-8")
    print(f"{len(pages)} pages ressources, /ressources et sitemap.xml écrits")
    if og:
        import ressources as gabarit
        gabarit.PAGES["ressources"] = HUB
        gabarit.og(["ressources"])


if __name__ == "__main__":
    main(og="--og" in sys.argv)
