"""Référencement des pages en ligne : titres, descriptions, données structurées, liens.

Utilisé par build_v4_metiers.py --prod. Titres et descriptions écrits pour la
recherche (« IA pour [métier] ») ; les pages gardent leur accroche à l'écran.
"""
import html, json, re

SITE = "https://longueur-davance.fr"
ORG = SITE + "/#org"

# slug -> (titre de recherche, description 140-160 car., nom court pour le fil d'Ariane)
SEO = {
    "": ("Longueur d'avance · Audit IA et sites premium pour les PME",
         "Accompagnement IA pour PME, artisans et cabinets, depuis Nantes et en visio partout en France : on chiffre vos tâches répétitives, puis on les automatise avec vous.",
         "Accueil"),
    "avocat": ("IA pour cabinet d'avocat : courriers et synthèses de dossier",
               "Synthèses de dossier, courriers types, pièces à préparer, relances : l'IA mise au travail dans votre cabinet, avec vos modèles, sans que vos dossiers quittent vos outils.",
               "Avocats et notaires"),
    "comptable": ("IA pour cabinet comptable : relances de pièces et courriers",
                  "Relances de pièces client par client, courriers récurrents, synthèses avant rendez-vous : on automatise avec votre équipe ce qui n'est facturé nulle part.",
                  "Experts-comptables"),
    "batiment": ("IA pour artisan du bâtiment : devis et relances automatisés",
                 "Devis rédigés depuis vos notes de visite, relances au bon moment, comptes rendus dictés, impayés suivis : l'IA pour les artisans, installée avec vous en visio.",
                 "Artisans du bâtiment"),
    "immobilier": ("IA pour agence immobilière : annonces et comptes rendus",
                   "Annonces rédigées depuis le bien, comptes rendus de visite le soir même, demandes triées, portails déclinés : l'IA dans votre agence, dans votre style.",
                   "Agences immobilières"),
    "architecte": ("IA pour architecte : métré, comptes rendus, maquette 3D",
                   "Métré, dépouillement des devis, comptes rendus de chantier, pièces écrites : l'IA reprend l'administratif de l'agence. Et vos plans en maquette 3D pour vos clients.",
                   "Architectes"),
    "recrutement": ("IA pour le recrutement : tri de CV et comptes rendus",
                    "Annonces, tri et résumé des CV, comptes rendus d'entretien, réponses aux candidats : l'IA pour cabinets de recrutement et RH, installée sur vos vrais postes.",
                    "Recrutement"),
    "garage": ("IA pour garage automobile : devis, rappels et rendez-vous",
               "Devis expliqués simplement, rappels d'entretien, comptes rendus d'intervention, demandes de rendez-vous : l'IA au comptoir de votre garage, sans changer de logiciel.",
               "Garages"),
    "camping": ("IA pour camping et hôtellerie : avis, mails et descriptifs",
                "Réponses aux avis, mails de réservation, descriptifs traduits, planning et taxe de séjour : l'IA pour campings et hôtels, prête avant la pleine saison.",
                "Hôtellerie et campings"),
    "communication": ("IA pour agence de communication : reporting et comptes rendus",
                      "Reportings clients, comptes rendus, calendriers éditoriaux, relances de validation : l'IA reprend l'admin de l'agence et rend du temps au créatif.",
                      "Agences de communication"),
    "traiteur": ("IA pour traiteur : devis, relances et commandes",
                 "Devis événementiels chiffrés depuis un brief, relances, acomptes, fiches techniques, commandes fournisseurs : l'IA pour traiteurs, sur vos vraies prestations.",
                 "Traiteurs"),
    "transport": ("IA pour transport et logistique : cotations et litiges",
                  "Cotations chiffrées dans l'heure, relances, dossiers de litige, pièces de tournée, facturation : l'IA pour transporteurs et logisticiens, avec vos outils.",
                  "Transport et logistique"),
    "medical": ("IA pour cabinet médical : rendez-vous et courriers",
                "Rappels de rendez-vous, courriers aux confrères, reprogrammations, questions administratives : l'IA allège le secrétariat de votre cabinet, pas le soin.",
                "Cabinets médicaux"),
    "commercial": ("IA pour commercial indépendant : relances et CRM à jour",
                   "Comptes rendus dictés en sortant, relances sans oubli, tournée préparée, suivi à jour : l'IA pour commerciaux et agents, pour rester sur le terrain.",
                   "Commerciaux indépendants"),
    "solo": ("IA pour indépendant : devis, relances et admin allégés",
             "Devis et factures depuis vos notes, relances, mails récurrents, veille de votre secteur : l'IA pour indépendants seuls à tout faire, installée avec vous.",
             "Indépendants"),
}

# Ordre d'affichage des liens métier en pied de page (tous en dur, lisibles sans JavaScript).
LIENS = [("avocat", "avocats et notaires"), ("comptable", "experts-comptables"), ("batiment", "artisans du bâtiment"),
         ("immobilier", "agences immobilières"), ("architecte", "architectes"), ("medical", "cabinets médicaux"),
         ("traiteur", "traiteurs"), ("garage", "garages"), ("transport", "transport et logistique"),
         ("camping", "campings et hôtels"), ("recrutement", "recrutement"), ("communication", "agences de communication"),
         ("commercial", "commerciaux"), ("solo", "indépendants")]


def org():
    return {
        "@type": "ProfessionalService", "@id": ORG,
        "name": "Longueur d'avance", "alternateName": ["Longueur d'avance IA", "longueur-davance.fr"],
        "url": SITE + "/", "logo": SITE + "/assets/logo-512.png", "image": SITE + "/og/accueil.png",
        "description": "Accompagnement des PME, artisans et professions libérales dans l'usage de l'intelligence artificielle : audit chiffré des tâches répétitives, automatisations installées avec le client, sites premium.",
        "email": "contact@longueur-davance.fr", "telephone": "+33743761687",
        "address": {"@type": "PostalAddress", "addressLocality": "Nantes", "postalCode": "44000",
                    "addressRegion": "Pays de la Loire", "addressCountry": "FR"},
        "areaServed": {"@type": "Country", "name": "France"},
        "founder": {"@type": "Person", "name": "Amdy Richard Diop Jouanguy"},
        "knowsAbout": ["intelligence artificielle en entreprise", "automatisation des tâches administratives",
                       "audit IA", "sites internet premium"],
        "sameAs": ["https://www.instagram.com/amdy.dpj/",
                   "https://www.facebook.com/profile.php?id=61594097434681"],
    }


def faq(t):
    qs = []
    for q, r in re.findall(r"<details[^>]*>\s*<summary>(.*?)<i></i></summary>\s*<p>(.*?)</p>", t, re.S):
        nettoie = lambda x: html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        qs.append({"@type": "Question", "name": nettoie(q),
                   "acceptedAnswer": {"@type": "Answer", "text": nettoie(r)}})
    return {"@type": "FAQPage", "mainEntity": qs} if qs else None


def jsonld(t, slug):
    titre, desc, court = SEO[slug]
    url = f"{SITE}/{slug}" if slug else SITE + "/"
    g = [org()]
    if not slug:
        g.append({"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Longueur d'avance",
                  "inLanguage": "fr-FR", "publisher": {"@id": ORG}})
    else:
        g.append({"@type": "Service", "name": f"Accompagnement IA pour {court.lower()}", "serviceType": "Accompagnement IA",
                  "description": desc, "provider": {"@id": ORG}, "areaServed": {"@type": "Country", "name": "France"},
                  "audience": {"@type": "BusinessAudience", "audienceType": court}, "url": url})
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": court, "item": url}]})
    f = faq(t)
    if f: g.append(f)
    data = json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))
    return f'<script type="application/ld+json">{data}</script>\n'


def head(slug, og_titre, og_desc):
    titre, desc, _ = SEO[slug]
    url = f"{SITE}/{slug}" if slug else SITE + "/"
    img = f"{SITE}/og/{slug or 'accueil'}.png"
    e = html.escape
    return (f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:site_name" content="Longueur d\'avance">\n'
            f'<meta property="og:locale" content="fr_FR">\n'
            f'<meta property="og:title" content="{e(og_titre)}">\n'
            f'<meta property="og:description" content="{e(og_desc)}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{img}">\n'
            f'<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            f'<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">\n'
            f'<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n')


def appliquer(t, slug, og_titre, og_desc):
    """Titre, description, balises de partage, données structurées et liens métier en dur."""
    titre, desc, _ = SEO[slug]
    e = html.escape
    t = re.sub(r"<title>.*?</title>", f"<title>{e(titre)}</title>", t, count=1, flags=re.S)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{e(desc)}">', t, count=1)
    t = re.sub(r'<link rel="icon" href="data:[^"]*">\n?', "", t, count=1)
    t = t.replace("</head>", head(slug, og_titre, og_desc) + jsonld(t, slug) + "</head>", 1)
    liens = " · ".join(f'<a href="/{s}">{n}</a>' for s, n in LIENS if s != slug)
    t = re.sub(r"© Longueur d'avance 2026 · Aussi pour : .*?</div>",
               f"© Longueur d'avance 2026 · Nantes et visio, partout en France · L'IA pour les {liens}</div>",
               t, count=1, flags=re.S)
    return t
