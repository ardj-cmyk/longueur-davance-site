#!/usr/bin/env python3
"""Genere une page d'atterrissage par metier depuis une source unique.

Le mail et le SMS envoient vers /avocat, /batiment, /immobilier... : le
prospect tombe sur une page qui parle de SON quotidien, pas d'une page
generique. Une seule source de verite ici, N fichiers statiques en sortie.
"""
from pathlib import Path

ICI = Path(__file__).parent
AGENDA = "https://calendar.app.google/S5K8G7FLFWj4d4sF7"

METIERS = {
"batiment": dict(
  titre="Artisan du bâtiment : devis et relances · Longueur d'avance",
  nom="Bâtiment", pill="Artisans du bâtiment",
  h1="Vos devis, le soir, après le chantier.",
  sub="Vous rentrez à 19 h et il reste trois devis à écrire. Pendant ce temps, "
      "ceux du mois dernier attendent une réponse que personne n'ira chercher. "
      "On automatise ça ensemble, en 45 minutes, sur vos vrais dossiers.",
  taches=["le devis chiffré et rédigé à partir de vos notes et métrés de visite, ou d'un vocal pris sur place",
          "la relance des devis restés sans réponse, au bon moment",
          "le compte rendu de chantier dicté à la voix et mis en forme tout seul",
          "votre fiche Google remplie et vivante, là où vos clients vous cherchent"],
  bas=2, haut=4, taux=45, taux_lbl="votre heure de main d'œuvre",
  punch="Vous mesurez sur place, comme toujours. Ce qui disparaît, c'est le report des "
        "cotes, le calcul des surfaces, l'application de votre grille de prix et la mise "
        "en forme. Une heure récupérée le soir, c'est une heure de plus sur le chantier "
        "le lendemain, ou une heure de moins volée à votre famille.",
  reve="Et le rendu du projet avant travaux, celui qui transforme un devis hésitant "
       "en chantier signé.",
  faq=("Je n'ai pas de site internet, c'est bloquant ?",
       "Non, et ce n'est pas le plus urgent. Ce qui vous coûte des chantiers aujourd'hui, "
       "c'est votre fiche Google : deux photos, aucune description, des avis auxquels "
       "personne ne répond. C'est gratuit, c'est là que vos clients cherchent, et ça se "
       "règle en une séance.")),

"immobilier": dict(
  titre="Agence immobilière : annonces, visites · Longueur d'avance",
  nom="Immobilier", pill="Agences immobilières",
  h1="L'annonce, le compte rendu, les portails. Chaque fois.",
  sub="Le bien change, le travail d'écriture ne change pas. On le fait produire "
      "tout seul, à partir de vos données, dans votre style, et vous relisez.",
  taches=["l'annonce rédigée depuis les caractéristiques du bien",
          "le compte rendu de visite envoyé au vendeur le soir même",
          "le tri et la qualification des demandes entrantes",
          "la déclinaison d'une annonce pour chaque portail et pour les réseaux"],
  bas=4, haut=6, taux=60, taux_lbl="la valeur de votre heure",
  punch="Ce n'est pas du temps facturable en plus, c'est du volume de mandats traité "
        "en plus, à effectif constant.",
  reve="Et le réaménagement virtuel d'une pièce vide, ou la vidéo verticale tirée "
       "des photos de l'annonce.",
  faq=("Vous faites de la visite 3D ?",
       "Non, et personne ne peut le faire sans caméra sur place : une visite virtuelle "
       "est un problème de captation, pas de génération. En revanche, le réaménagement "
       "virtuel d'une photo existante et la vidéo tirée des photos de l'annonce, oui.")),

"avocat": dict(
  titre="Avocat : courriers, synthèses de dossier · Longueur d'avance",
  nom="Avocats et notaires", pill="Cabinets d'avocats et offices notariaux",
  h1="Le temps que prend l'écrit, dans un cabinet.",
  sub="La synthèse, le courrier type, la préparation des pièces. Rien de tout cela "
      "n'est du droit, et tout cela prend vos heures.",
  taches=["la synthèse d'un dossier ou d'un rendez-vous",
          "les courriers et actes types, à partir de vos propres modèles",
          "la préparation des pièces avant un rendez-vous client",
          "les relances de documents manquants"],
  bas=3, haut=5, taux=200, taux_lbl="votre heure facturée",
  punch="Le secret professionnel est le premier sujet qu'on traite, pas le dernier : "
        "on cadre en début de séance ce qui peut passer par un outil externe et ce qui "
        "ne doit jamais en sortir.",
  reve="",
  faq=("Et le secret professionnel ?",
       "C'est le point de départ de la séance. On identifie ensemble ce qui peut sortir "
       "du cabinet et ce qui ne le peut pas, et on construit uniquement sur la première "
       "catégorie. Aucune donnée de dossier ne transite par nous, jamais.")),

"comptable": dict(
  titre="Expert-comptable : relances de pièces · Longueur d'avance",
  nom="Experts-comptables", pill="Cabinets d'expertise comptable",
  h1="Courir après les pièces, tous les mois, chez tous les clients.",
  sub="Ce n'est pas de la production comptable, ce n'est facturé nulle part, "
      "et ça mange les journées de votre équipe.",
  taches=["les relances de pièces manquantes, client par client",
          "les courriers et mails récurrents, à partir de vos modèles",
          "la synthèse d'un dossier avant un rendez-vous client",
          "les réponses aux questions que vos clients posent tous les mois"],
  bas=3, haut=5, taux=90, taux_lbl="le coût horaire d'un collaborateur",
  punch="On ne touche pas à la production comptable ni au calcul fiscal. On prend ce "
        "qui l'entoure et qui n'est facturé nulle part.",
  reve="",
  faq=("Vous touchez à la saisie ou au fiscal ?",
       "Non, jamais. Ce sont des domaines où une erreur plausible mais fausse coûte "
       "très cher, et où votre responsabilité est engagée. On travaille exclusivement "
       "sur l'écrit qui entoure la production.")),

"architecte": dict(
  titre="Architecte : métré, comptes rendus · Longueur d'avance",
  nom="Architectes", pill="Agences d'architecture",
  h1="Ce qui vous prend du temps n'est pas le projet.",
  sub="Le dessin, c'est votre métier, et personne ne va vous le prendre. Mais le métré, "
      "le dépouillement, les comptes rendus et les pièces écrites reviennent à chaque "
      "opération, et ceux-là peuvent se produire tout seuls.",
  taches=["le métré et les quantitatifs, chute comprise, avec le calcul visible ligne à ligne",
          "le dépouillement des devis d'entreprises, poste par poste, avec les oublis signalés",
          "les comptes rendus de réunion de chantier, par lot, avec les points en attente",
          "les manipulations répétitives dans Revit ou Rhino, automatisées par script",
          "les notices descriptives et les pièces écrites, dans le vocabulaire de l'agence",
          "les relances des entreprises et des maîtres d'ouvrage"],
  bas=4, haut=7, taux=80, taux_lbl="la valeur de votre heure",
  punch="Le projet reste le vôtre, et le dessin aussi. On prend ce qui se répète "
        "d'une opération à l'autre : le métré, le dépouillement, l'écrit et les "
        "manipulations qu'on refait cent fois dans le logiciel.",
  reve="",
  faq=("Vous produisez des images de projet ?",
       "On peut, mais c'est un sujet à part et vous jugerez le rendu en professionnel. "
       "L'essentiel du gain est ailleurs : dans l'écrit qui accompagne chaque opération.")),

"recrutement": dict(
  titre="Recrutement : tri de CV et comptes rendus · Longueur d'avance",
  nom="Recrutement", pill="Cabinets de recrutement et agences d'intérim",
  h1="Le tri des CV, poste après poste.",
  sub="C'est le métier où l'écrit répétitif pèse le plus lourd de tous ceux "
      "qu'on accompagne. C'est aussi celui où le gain se voit le plus vite.",
  taches=["la rédaction des annonces, poste par poste",
          "le tri et le résumé des CV reçus",
          "les comptes rendus d'entretien",
          "les réponses aux candidats non retenus"],
  bas=5, haut=8, taux=60, taux_lbl="le coût horaire d'un consultant",
  punch="Répondre à tous les candidats devient possible. C'est votre marque employeur "
        "qui change, pas seulement votre planning.",
  reve="",
  faq=("Une IA qui trie des CV, ce n'est pas risqué ?",
       "Si, quand elle décide. Ici elle résume et ordonne, vous décidez. On cadre en "
       "séance ce qui doit rester un jugement humain, et les critères qu'on n'automatise "
       "jamais.")),

"garage": dict(
  titre="Garage : devis, ordres de réparation · Longueur d'avance",
  nom="Garages", pill="Garages et réparation automobile",
  h1="Le temps passé au comptoir, sur de l'écrit.",
  sub="Le devis à expliquer, le rappel d'entretien à envoyer, la demande de "
      "rendez-vous à traiter entre deux interventions.",
  taches=["le devis et l'ordre de réparation, expliqués en français compréhensible",
          "les rappels d'entretien, client par client",
          "le compte rendu de l'intervention envoyé au client",
          "les réponses aux demandes de rendez-vous"],
  bas=2, haut=3, taux=55, taux_lbl="votre heure d'atelier",
  punch="Le temps gagné au comptoir, c'est du temps rendu à l'atelier.",
  reve="",
  faq=("Ça se branche sur mon logiciel de garage ?",
       "Parfois oui, parfois non, et on le vérifie avant de vous engager. Beaucoup de "
       "gains ne demandent aucun branchement : ils se font à côté de votre logiciel, "
       "pas dedans.")),

"camping": dict(
  titre="Camping : avis, mails, descriptifs · Longueur d'avance",
  nom="Hôtellerie et campings", pill="Hôtels, campings et hébergements",
  h1="Les avis, les mails, les descriptifs. En pleine saison.",
  sub="C'est le moment où personne n'a le temps, et c'est exactement le moment "
      "où ça compte le plus.",
  taches=["les réponses aux avis, une par une, y compris les mauvais",
          "les mails de réservation et de pré-séjour",
          "les descriptifs traduits pour la clientèle étrangère",
          "les réponses aux demandes qui reviennent chaque saison"],
  bas=3, haut=5, taux=40, taux_lbl="le coût horaire d'un membre de l'équipe",
  punch="En pleine saison, c'est le temps que personne n'a. C'est exactement là que "
        "ça se voit.",
  reve="Et la vidéo de l'établissement, tirée de vos photos existantes.",
  faq=("On répond déjà aux avis, mais pas à tous.",
       "C'est le cas de tout le monde. L'enjeu n'est pas d'écrire mieux, c'est de "
       "répondre à tous, vite, sans que ce soit une corvée. La réponse est préparée, "
       "vous relisez et vous publiez.")),

"communication": dict(
  titre="Agence de com : reporting et comptes rendus · Longueur d'avance",
  nom="Agences de communication", pill="Studios et agences de com",
  h1="L'admin qui mange le temps créatif.",
  sub="Le reporting, les comptes rendus, les calendriers. Rien de tout cela n'est "
      "du créatif, et tout cela se facture mal.",
  taches=["les reportings clients, mois après mois, au même format",
          "les comptes rendus de réunion et les relevés de décisions",
          "les calendriers éditoriaux et les déclinaisons par plateforme",
          "les relances de validation, côté client",
          "les réponses aux appels d'offres et les recommandations"],
  bas=8, haut=12, taux=70, taux_lbl="votre taux journalier ramené à l'heure",
  punch="Le créatif reste le vôtre. On prend ce qui se répète à l'identique d'un "
        "client à l'autre, et qui n'a jamais été facturé à son vrai prix.",
  reve="",
  faq=("Est-ce que ça va standardiser notre créa ?",
       "Non, parce qu'on ne touche pas à la création. On automatise le reporting, "
       "les comptes rendus et les relances. Ce qui fait votre valeur reste écrit "
       "par vous, avec vos idées.")),

"medical": dict(
  titre="Cabinet médical : rendez-vous, courriers · Longueur d'avance",
  nom="Cabinets médicaux", pill="Praticiens et cabinets de santé",
  h1="Le secrétariat qui déborde sur les consultations.",
  sub="Les rendez-vous, les rappels, la coordination, les courriers confrères. "
      "Ce n'est pas du soin, et ça prend le temps du soin.",
  taches=["les rappels de rendez-vous, pour réduire les absences",
          "les courriers aux confrères, à partir de vos modèles",
          "la coordination des rendez-vous et des reprogrammations",
          "les réponses aux questions administratives qui reviennent",
          "les relances de documents manquants"],
  bas=4, haut=8, taux=90, taux_lbl="la valeur de votre heure de consultation",
  punch="Les données de santé ne sortent jamais du cabinet. On ne construit que sur "
        "l'administratif : agenda, rappels, courriers types. Aucun contenu de dossier "
        "patient ne passe par un outil externe, jamais.",
  reve="",
  faq=("Et le secret médical ?",
       "C'est la première chose qu'on cadre, avant tout le reste. Les données de santé "
       "sont des données sensibles au sens du RGPD et leur hébergement est réglementé. "
       "On travaille uniquement sur ce qui n'en contient pas : la prise de rendez-vous, "
       "les rappels, les modèles de courriers. Si un usage exige de toucher au dossier "
       "patient, on vous le dit et on ne le fait pas.")),

"commercial": dict(
  titre="Commercial indépendant : relances et CRM · Longueur d'avance",
  nom="Commerciaux indépendants", pill="Agents commerciaux et apporteurs d'affaires",
  h1="Le temps passé loin du terrain.",
  sub="La prospection, les relances, le CRM tenu à jour le soir. "
      "Tout ce qui n'est pas devant un client ne rapporte rien.",
  taches=["les comptes rendus de rendez-vous, dictés en sortant",
          "les relances de prospects, au bon moment et sans en oublier",
          "la préparation de la tournée : l'ordre des visites, et pour chacune qui c'est, où on en était, ce qui a été promis",
          "les mails de prospection personnalisés, pas les copiés-collés",
          "la mise à jour du suivi après chaque échange"],
  bas=6, haut=10, taux=65, taux_lbl="ce que vaut une heure devant un client",
  punch="Chaque heure reprise à l'administratif est une heure rendue au terrain. "
        "C'est le seul métier de cette liste où le calcul est aussi direct.",
  reve="",
  faq=("Est-ce que vous automatisez la prospection en masse ?",
       "Non. On automatise la préparation et le suivi, pas l'envoi en masse. "
       "Un message générique envoyé à mille personnes ne rapporte rien et abîme "
       "votre nom. On vous fait gagner du temps sur ce qui entoure la vente, "
       "pas sur la vente elle-même.")),

"solo": dict(
  titre="Indépendant : devis, relances, admin · Longueur d'avance",
  nom="Indépendants et créateurs", pill="Solo, freelances, créateurs d'entreprise",
  h1="Vous êtes seul à tout faire.",
  sub="Le devis, la relance, le contenu, l'admin, la veille. Personne à qui déléguer, "
      "et des journées qui ne rentrent pas.",
  taches=["les devis et les factures, rédigés depuis vos notes",
          "les relances de ce qui n'a pas eu de réponse",
          "les mails qui reviennent toujours, à partir de vos réponses passées",
          "les comptes rendus et les prises de notes",
          "la veille de votre secteur, filtrée et sourcée"],
  bas=6, haut=10, taux=50, taux_lbl="ce que vaut votre heure",
  punch="Vous n'avez pas les moyens d'embaucher un assistant. C'est exactement pour "
        "ça que ces heures-là sont les plus rentables à récupérer.",
  reve="",
  faq=("Je débute, est-ce que c'est trop tôt ?",
       "C'est plutôt le bon moment. Installer les bons réflexes quand vous avez dix "
       "clients coûte une séance. Les installer quand vous en avez cent, c'est un "
       "chantier. Et l'échange de 30 minutes vous dira si ça vaut le coup, gratuitement.")),
}


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{nom} : on automatise en 45 minutes une tâche répétitive de votre semaine, sur vos vrais dossiers. Aucun logiciel à acheter, vos données restent chez vous.">
<meta property="og:title" content="{h1}">
<meta property="og:description" content="{sub_court}">
<meta property="og:url" content="https://longueur-davance.fr/{slug}.html">
<link rel="canonical" href="https://longueur-davance.fr/{slug}.html">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23b4551e'/%3E%3Cpath d='M14 44 L30 28 L38 36 L52 18' stroke='%23fdfcf9' stroke-width='6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/site.css">
<style>
.lp-head {{ padding: 14px 0; }}
.lp-head .nav-wrap {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; }}
.calc {{ background:#fff; border:2px solid var(--accent); border-radius:var(--r-lg);
  box-shadow:0 0 0 8px var(--accent-d); padding:30px 24px 24px; position:relative;
  max-width:620px; margin:36px auto 0; }}
.calc-badge {{ position:absolute; top:-12px; left:24px; background:var(--accent); color:var(--paper);
  font-size:10px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase;
  padding:4px 14px; border-radius:99px; }}
.calc-row {{ margin-bottom:24px; }}
.calc-row label {{ display:flex; justify-content:space-between; align-items:baseline; gap:12px;
  font-size:11px; font-weight:700; letter-spacing:.8px; text-transform:uppercase;
  color:var(--muted); margin-bottom:12px; }}
.calc-val {{ font-family:'Playfair Display',Georgia,serif; font-size:20px; font-weight:700;
  color:var(--ink); letter-spacing:0; text-transform:none; }}
.calc input[type=range] {{ width:100%; -webkit-appearance:none; appearance:none; height:4px;
  border-radius:99px; background:var(--line); outline:none; }}
.calc input[type=range]::-webkit-slider-thumb {{ -webkit-appearance:none; appearance:none;
  width:26px; height:26px; border-radius:50%; background:var(--accent); cursor:pointer;
  border:3px solid #fff; box-shadow:0 2px 10px rgba(180,85,30,.45); }}
.calc input[type=range]::-moz-range-thumb {{ width:26px; height:26px; border:3px solid #fff;
  border-radius:50%; background:var(--accent); cursor:pointer; }}
.calc-out {{ background:var(--ink); border-radius:var(--r); color:var(--paper);
  margin-top:28px; padding:24px 20px; text-align:center; }}
.calc-out .amount-lbl {{ font-size:11px; font-weight:700; letter-spacing:2px;
  text-transform:uppercase; color:var(--gold); margin-bottom:12px; }}
.calc-out .amount {{ font-family:'Playfair Display',Georgia,serif; font-size:clamp(40px,11vw,62px);
  line-height:1; color:var(--paper); font-variant-numeric:tabular-nums lining-nums; }}
.calc-out .amount .plus {{ color:var(--gold); }}
.calc-out .amount-sub {{ font-size:14px; color:rgba(253,252,249,.72); margin-top:12px; }}
.calc-detail {{ font-size:12.5px; color:rgba(253,252,249,.5); margin-top:14px; line-height:1.6;
  border-top:1px solid rgba(253,252,249,.12); padding-top:14px; }}
.taches {{ list-style:none; margin-top:30px; }}
.taches li {{ display:flex; gap:14px; align-items:flex-start; padding:18px 0;
  border-bottom:1px solid var(--line); font-size:16px; line-height:1.6; }}
.taches li:last-child {{ border-bottom:none; }}
.taches li::before {{ content:'→'; color:var(--accent); font-weight:700; flex-shrink:0; font-size:17px; }}
.dark {{ background:var(--ink); color:var(--paper); }}
.dark h2 {{ color:var(--paper); }} .dark p {{ color:rgba(253,252,249,.76); }}
.dark .kicker {{ color:var(--gold); }} .dark .kicker::before {{ background:var(--gold); }}
.nope {{ display:grid; gap:14px; grid-template-columns:1fr; margin-top:26px; }}
@media (min-width:700px) {{ .nope {{ grid-template-columns:repeat(2,1fr); }} }}
.nope div {{ border-left:2px solid var(--accent); padding:4px 0 4px 16px; font-size:14.5px; line-height:1.65; }}
.nope strong {{ display:block; font-weight:600; margin-bottom:3px; }}
.tl {{ counter-reset:s; margin-top:30px; }}
.tl li {{ list-style:none; position:relative; padding-left:54px; padding-bottom:26px; }}
.tl li::before {{ counter-increment:s; content:counter(s); position:absolute; left:0; top:-2px;
  width:34px; height:34px; border-radius:50%; background:var(--accent-d); color:var(--accent);
  display:flex; align-items:center; justify-content:center; font-weight:700; font-size:14px; }}
.tl li::after {{ content:''; position:absolute; left:17px; top:36px; bottom:0; width:1px; background:var(--line); }}
.tl li:last-child {{ padding-bottom:0; }} .tl li:last-child::after {{ display:none; }}
.tl h3 {{ font-size:18px; margin-bottom:6px; }}
.tl p {{ font-size:14.5px; color:var(--muted); line-height:1.65; }}
.faq-q {{ border-top:1px solid var(--line); padding:18px 0; font-size:16px; font-weight:600;
  cursor:pointer; list-style:none; display:flex; justify-content:space-between;
  align-items:center; gap:16px; }}
.faq-q::-webkit-details-marker {{ display:none; }}
.faq-q::after {{ content:'+'; color:var(--accent); font-size:22px; font-weight:400; flex-shrink:0; }}
details[open] .faq-q::after {{ content:'−'; }}
details {{ background:none; border:none; box-shadow:none; }}
details p {{ font-size:14.5px; color:var(--muted); line-height:1.7; padding-bottom:18px; }}
.cta-band {{ text-align:center; }}
.cta-band h2 {{ font-size:clamp(26px,5.5vw,40px); max-width:18ch; margin:0 auto 16px; }}
.cta-band p {{ max-width:46ch; margin:0 auto 26px; }}
</style>
</head>
<body>

<header class="lp-head">
  <div class="wrap nav-wrap">
    <a class="logo" href="/" aria-label="Longueur d'avance, accueil">
      <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect width="64" height="64" rx="12" fill="#b4551e"/>
        <path d="M14 44 L30 28 L38 36 L52 18" stroke="#fdfcf9" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="logo-name">Longueur d'avance<span class="logo-sub">Audit IA · Accompagnement</span></div>
    </a>
    <a class="cta-text js-book" href="{agenda}" target="_blank" rel="noopener" data-loc="nav">
      Réserver 30 min
      <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
    </a>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <div class="hero-pill">{pill}</div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    <a class="btn js-book" href="{agenda}" target="_blank" rel="noopener" data-loc="hero">Réserver 30 minutes, gratuit</a>
    <div class="hero-trust">
      <span class="trust-item">Confirmation immédiate</span>
      <span class="trust-item">100 % visio</span>
      <span class="trust-item">Aucun logiciel à acheter</span>
    </div>
  </div>
</section>

<section style="background:var(--surface)">
  <div class="wrap rv">
    <div class="kicker">Ce qu'on vous retire</div>
    <h2 style="font-size:clamp(26px,5.5vw,40px);max-width:20ch">Ce qui revient à chaque opération.</h2>
    <ul class="taches">{taches_html}</ul>
    <p class="micro" style="margin-top:24px;font-size:15px;line-height:1.7;max-width:56ch">{punch}{reve_html}</p>
  </div>
</section>

<section id="calcul">
  <div class="wrap rv">
    <div class="kicker">Le calcul</div>
    <h2 style="font-size:clamp(26px,5.5vw,40px);max-width:20ch">Ce que ça vous coûte, sur une année.</h2>
    <p class="micro" style="max-width:56ch;font-size:15px;line-height:1.7;margin:16px 0 0">
      Sur ce métier, ces tâches pèsent en général entre {bas} et {haut} heures par semaine.
      Déplacez les curseurs sur votre situation réelle.
    </p>
    <div class="calc">
      <span class="calc-badge">Sur votre cas</span>
      <div class="calc-row">
        <label for="h">Heures répétitives par semaine <span class="calc-val" id="hv">{defaut_h} h</span></label>
        <input type="range" id="h" min="1" max="12" step="0.5" value="{defaut_h}">
      </div>
      <div class="calc-row">
        <label for="t">{taux_lbl} <span class="calc-val" id="tv">{taux} €</span></label>
        <input type="range" id="t" min="{taux_min}" max="{taux_max}" step="5" value="{taux}">
      </div>
      <div class="calc-out">
        <div class="amount-lbl">Ce que vous récupérez chaque année</div>
        <div class="amount"><span class="plus">+</span><span id="res">0</span> €</div>
        <div class="amount-sub">de temps de travail rendu à votre activité</div>
        <p class="calc-detail" id="det"></p>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--surface)">
  <div class="wrap rv">
    <div class="kicker">Le parcours</div>
    <h2 style="font-size:clamp(26px,5.5vw,40px);max-width:16ch">Comment ça se passe.</h2>
    <ol class="tl">
      <li><h3>L'échange découverte (30 min, gratuit)</h3>
        <p>Vous racontez votre semaine. On repère ensemble les tâches qui reviennent
           et ce qu'elles vous coûtent réellement. Vous ne repartez avec aucun devis.</p></li>
      <li><h3>L'audit, par écrit</h3>
        <p>Vous recevez ce qu'on a identifié, chiffré en heures et en euros.
           Il est à vous, que vous alliez plus loin ou non.</p></li>
      <li><h3>La proposition</h3>
        <p>Si ça vaut le coup, on vous dit ce que vous pouvez mettre en place, et ce que ça coûte.
           Si ça ne vaut pas le coup, on vous le dit tout de suite.</p></li>
      <li><h3>Les séances de travail (45 min chacune)</h3>
        <p>Une séance, ou plusieurs selon ce que vous voulez traiter. Tout est préparé
           en amont. Vous l'installez sur votre poste, on vous guide à chaque étape, et à la fin
           ça tourne sur vos vrais dossiers.</p></li>
    </ol>
  </div>
</section>

<section class="dark">
  <div class="wrap rv">
    <div class="kicker">La règle du jeu</div>
    <h2 style="font-size:clamp(26px,5.5vw,40px);max-width:20ch">Ce qu'on ne fera jamais.</h2>
    <div class="nope">
      <div><strong>On ne vend aucun logiciel.</strong> Pas d'abonnement à nous payer.
        Les outils restent les vôtres, vous pouvez les garder, les changer ou les arrêter sans nous.</div>
      <div><strong>On ne garde pas vos données.</strong> Vos dossiers, vos clients, vos documents
        restent chez vous. Nous n'hébergeons rien.</div>
      <div><strong>On ne vous rend pas dépendant.</strong> L'objectif de la séance est que vous
        sachiez le refaire seul.</div>
      <div><strong>On ne promet pas de miracle.</strong> Certaines tâches ne s'automatisent pas
        proprement, et certains calculs ne doivent surtout pas être confiés à une IA.
        Quand c'est le cas, on vous le dit.</div>
    </div>
  </div>
</section>

<section style="background:var(--surface)">
  <div class="wrap rv" style="max-width:760px">
    <div class="kicker">Questions</div>
    <h2 style="font-size:clamp(26px,5.5vw,40px);margin-bottom:24px">Avant de réserver.</h2>
    <details><summary class="faq-q">{faq_q}</summary><p>{faq_r}</p></details>
    <details><summary class="faq-q">Je n'y connais rien en informatique.</summary>
      <p>C'est le cas de la plupart des gens que j'accompagne. Rien à installer avant,
         rien à coder pendant, et la marche à suivre vous est remise par écrit.</p></details>
    <details><summary class="faq-q">Et mes données ?</summary>
      <p>Elles restent chez vous. On travaille sur votre écran, avec vos outils. Les outils
         mis en place sont choisis pour leur conformité au RGPD, avec un hébergement dans
         l'Union européenne en priorité. Quand un outil traite des données hors UE, vous le
         savez avant qu'il soit installé.</p></details>
    <details><summary class="faq-q">Combien ça coûte ?</summary>
      <p>Il n'y a pas de tarif affiché : trois courriers types à automatiser ou toute une
         chaîne de devis à reprendre, ce n'est pas le même travail. On regarde ensemble
         pendant 30 minutes, sans que ce soit facturé, et vous recevez un devis écrit.
         <a href="/formation.html" style="color:var(--accent)">Le détail est ici.</a></p></details>
    <details><summary class="faq-q">Et si ça ne marche pas chez moi ?</summary>
      <p>Certaines tâches ne s'automatisent pas proprement. Si c'est le cas de la vôtre,
         je vous le dis pendant l'échange de 30 minutes, avant que vous n'ayez payé quoi que ce soit.</p></details>
  </div>
</section>

<section class="dark cta-band">
  <div class="wrap rv">
    <div class="kicker">La suite</div>
    <h2>Une tâche en moins, dès cette semaine.</h2>
    <p>30 minutes en visio pour regarder votre cas. Si ça n'a pas de sens chez vous, je vous le dis.</p>
    <a class="btn btn-invert js-book" href="{agenda}" target="_blank" rel="noopener" data-loc="final">Réserver 30 minutes, gratuit</a>
    <p class="micro" style="margin-top:22px;color:rgba(253,252,249,.55)">Longueur d'avance · Nantes et sa région</p>
  </div>
</section>

<footer>
  <div class="wrap"><div class="footer-inner">
    <div class="footer-top">
      <div><div class="footer-brand">Longueur d'avance</div>
        <div class="footer-tagline">Audit IA · Accompagnement pour cabinets et PME</div></div>
      <a class="cta-text js-book" href="{agenda}" target="_blank" rel="noopener" data-loc="footer">
        Réserver 30 minutes, gratuit
        <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
      </a>
    </div>
    <div class="footer-bottom">
      <span>© Longueur d'avance 2026 · contact@longueur-davance.fr</span>
      <span><a href="/mentions-legales.html">Mentions légales</a> · <a href="/confidentialite.html">Confidentialité</a> · <a href="/">Accueil</a></span>
    </div>
  </div></div>
</footer>

<script defer src="/_vercel/insights/script.js"></script>
<script>
(function () {{
  var h=document.getElementById('h'),t=document.getElementById('t'),
      hv=document.getElementById('hv'),tv=document.getElementById('tv'),
      res=document.getElementById('res'),det=document.getElementById('det'),
      fmt=new Intl.NumberFormat('fr-FR');
  function maj() {{
    var hh=parseFloat(h.value),tt=parseInt(t.value,10),an=Math.round(hh*52),g=Math.round(an*tt);
    hv.textContent=(hh%1?hh.toString().replace('.',','):hh)+' h';
    tv.textContent=tt+' €';
    res.textContent=fmt.format(g);
    det.textContent=hv.textContent+" par semaine, soit "+fmt.format(an)+" h par an, valorisées à "+tt+" € de l'heure.";
  }}
  h.addEventListener('input',maj); t.addEventListener('input',maj); maj();

  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{
    if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.08}});
  document.querySelectorAll('.rv').forEach(function(el){{io.observe(el);}});

  var q=new URLSearchParams(location.search),ctx={{}};
  ['p','utm_source','utm_medium','utm_campaign','utm_content'].forEach(function(k){{
    if(q.get(k))ctx[k]=q.get(k);}});
  if(Object.keys(ctx).length){{try{{sessionStorage.setItem('lda_ctx',JSON.stringify(ctx));}}catch(e){{}}}}
  else{{try{{ctx=JSON.parse(sessionStorage.getItem('lda_ctx')||'{{}}');}}catch(e){{ctx={{}};}}}}
  function track(n,x){{if(window.va)window.va('event',{{name:n,data:Object.assign({{metier:'{slug}'}},ctx,x||{{}})}});}}
  document.querySelectorAll('.js-book').forEach(function(a){{
    a.addEventListener('click',function(){{track('clic_reservation',{{position:a.dataset.loc||''}});}});}});
  h.addEventListener('change',function(){{track('calculateur_utilise');}},{{once:true}});
  track('page_vue');
}})();
</script>
</body>
</html>
"""

for slug, m in METIERS.items():
    taches = "\n".join(f"      <li>{t}</li>" for t in m["taches"])
    reve = f" {m['reve']}" if m["reve"] else ""
    page = GABARIT.format(
        slug=slug, agenda=AGENDA, nom=m["nom"], pill=m["pill"], h1=m["h1"], sub=m["sub"],
        titre=m.get("titre") or (m["nom"] + " · Longueur d'avance"),
        sub_court=m["sub"][:150], taches_html="\n" + taches + "\n    ",
        punch=m["punch"], reve_html=reve, bas=m["bas"], haut=m["haut"],
        defaut_h=(m["bas"] + m["haut"]) / 2, taux=m["taux"], taux_lbl=m["taux_lbl"],
        # les bornes doivent etre des multiples de 5 alignes sur le pas, sinon la
        # valeur par defaut est arrondie a cote (45 affichait 47)
        taux_min=max(20, (int(m["taux"] * 0.5) // 5) * 5),
        taux_max=int(m["taux"] * 2),
        faq_q=m["faq"][0], faq_r=m["faq"][1])
    (ICI / f"{slug}.html").write_text(page, encoding="utf-8")
    print(f"  {slug}.html")
print(f"\n{len(METIERS)} pages metier generees")
