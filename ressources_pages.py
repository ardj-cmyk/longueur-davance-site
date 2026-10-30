# Contenu des pages ressources (une par vidéo Instagram). Gabarit : ressources.py
# Règles : chiffres vérifiés à la source avec la date, zéro tiret cadratin, zéro point-virgule dans le texte.

SRC_TARIFS_API = ("Tarifs API d'Anthropic", "https://platform.claude.com/docs/en/about-claude/pricing")
SRC_FORFAITS = ("Formules Claude", "https://claude.com/fr/pricing")
SRC_LIMITES = ("Aide Claude : bien utiliser ses limites", "https://support.claude.com/en/articles/9797557-usage-limit-best-practices")

PAGES = {}

# ─────────────────────────────── 11 · LE TOKEN
PAGES["token"] = dict(
    video="11 · Le token",
    title="Trois façons de réduire ta facture Claude (tokens)",
    desc="Le token expliqué simplement, et trois façons concrètes de dépenser moins de jetons avec Claude, sur un abonnement comme en API.",
    og_pill="Les bases de l'IA · 11", og_titre="Trois façons de réduire ta facture de tokens",
    marque="Les bases de l'IA · 11",
    h1="Trois façons de <em>réduire ta facture</em>",
    chapo="Chaque échange avec Claude se paie en jetons, les fameux tokens : ta question, sa réponse, et tout ce qui est déjà écrit dans la conversation. Voici comment en dépenser moins, sans rien perdre en qualité.",
    verifie="13/10/2026",
    sources=[SRC_LIMITES, SRC_FORFAITS, SRC_TARIFS_API],
    corps="""
<section>
  <h2>D'abord, ce que tu paies vraiment</h2>
  <div class="encadre"><b>Sur un abonnement (Free, Pro, Max)</b>Tu ne paies pas au jeton, mais chaque jeton remplit ta limite. Elle se recharge sur une fenêtre de 5 heures, et les formules payantes ont en plus une limite par semaine. Moins de jetons, c'est plus de travail avant d'être bloqué.</div>
  <div class="encadre"><b>En API (pour brancher Claude dans tes outils)</b>Tu paies chaque million de jetons. Et les jetons de sa réponse coûtent 5 fois plus cher que ceux de ta question : sur Sonnet 5.5, 2 $ le million en entrée, 10 $ en sortie.</div>
  <div class="encadre"><b>Le piège que personne ne voit</b>À chaque nouveau message, Claude reprend toute la conversation depuis le début. Ton dixième message coûte donc ton message, plus les neuf échanges d'avant. La longueur de la conversation fait partie des choses qui pèsent sur ta limite, c'est écrit noir sur blanc dans l'aide officielle.</div>
</section>

<section>
  <h2><span class="num">1</span>Une conversation par sujet</h2>
  <ul class="liste">
    <li><b>Nouveau sujet, nouvelle conversation.</b> Ne pose pas ta question sur ta compta à la suite d'une conversation sur ton site internet. Tu paierais toute l'histoire du site à chaque message.</li>
    <li><b>La conversation s'étire ?</b> Demande-lui un résumé, puis repars à zéro avec ce résumé.</li>
  </ul>
  <pre><code>Résume en 10 lignes ce qu'on a décidé et ce qu'il reste à faire.</code></pre>
  <p>Copie le résumé, ouvre une nouvelle conversation, colle-le, et continue. Tu gardes l'essentiel et tu laisses le poids derrière toi.</p>
  <ul class="liste">
    <li><b>Un document que tu utilises souvent ?</b> Mets-le dans un Projet au lieu de le recoller à chaque fois. Les documents d'un projet sont mis en cache : quand Claude les réutilise, ils comptent moins dans ta limite. Le gratuit en permet jusqu'à 5.</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Le bon modèle pour la tâche</h2>
  <p>Le modèle choisi fait partie de ce qui pèse sur ta limite. En API, Opus 5.5 coûte deux fois plus cher que Sonnet 5.5, et Haiku 5.5 vingt fois moins cher que Sonnet.</p>
  <div class="regle" style="margin-top:14px">
    <h2>La règle simple</h2>
    <ol class="etapes">
      <li><b>Sonnet par défaut.</b> Rédiger, résumer, corriger, la grande majorité des tâches.</li>
      <li><b>Opus quand il faut réfléchir.</b> Un plan, une décision, un dossier compliqué.</li>
      <li><b>Haiku quand tu répètes.</b> La même tâche simple, cent fois.</li>
    </ol>
  </div>
  <p class="note">Même logique pour le niveau d'effort et la réflexion approfondie : pour reformuler un mail, pas besoin que Claude réfléchisse à fond. Le détail des modèles et de leurs prix : <a href="/modeles">l'antisèche des modèles</a>.</p>
</section>

<section>
  <h2><span class="num">3</span>Tout dire en un seul message</h2>
  <p>Chaque aller-retour te coûte toute la conversation une fois de plus. Le meilleur moyen d'économiser, c'est d'avoir la bonne réponse du premier coup.</p>
  <ul class="liste">
    <li><b>Regroupe tes questions.</b> Trois questions dans un message, plutôt que trois messages.</li>
    <li><b>Donne le contexte dès le départ</b> : pour qui, dans quel but, quel format tu veux. Claude n'aura pas à te poser de questions.</li>
    <li><b>Relis avant d'envoyer.</b> Un oubli, c'est un message de plus.</li>
  </ul>
  <h3>Exemple</h3>
  <div class="avant-apres">
    <div class="av"><small>3 messages, 3 réponses</small>« Écris un mail de relance. » Puis « Plus court. » Puis « Plus poli, c'est un bon client. »</div>
    <div class="ap"><small>1 message, 1 réponse</small>« Écris un mail de relance pour une facture de 1 200 € en retard de 15 jours. C'est un bon client, reste poli. 5 lignes maximum. »</div>
  </div>
  <p class="note">Et le français ? Il consomme un peu plus de jetons que l'anglais, c'est vrai. Ce n'est pas une raison pour écrire en anglais : un message clair en français vaut mieux qu'un message approximatif suivi de trois relances.</p>
</section>

<section>
  <h2>Bonus si tu passes par l'API</h2>
  <ul class="liste">
    <li><b>Le cache.</b> Si tu envoies souvent le même long début de message (des consignes, un document), mets-le en cache. Relire un contenu en cache coûte 5 % du prix normal sur Opus 5.5 et Sonnet 5.5.</li>
    <li><b>Le traitement par lot (Batch).</b> Si la réponse peut attendre, l'API Batch coûte 50 % moins cher, en entrée comme en sortie.</li>
  </ul>
</section>

<section>
  <h2>Où voir ce que tu consommes</h2>
  <p>Sur claude.ai : <b>Paramètres, puis Utilisation</b>. Tu y vois où tu en es de ta fenêtre de 5 heures et de ta limite de la semaine.</p>
</section>
""",
    fin="Réduire sa facture, c'est bien. Savoir quelles tâches confier à l'IA, c'est mieux. Ce que je fais avec les entreprises : je chiffre ce que leurs tâches répétitives leur coûtent, et je les accompagne pour les réduire. Sans jargon, sans dépendance.",
)

# ─────────────────────────────── 10 · LES FORFAITS
PAGES["forfaits"] = dict(
    video="10 · Les forfaits",
    title="Gratuit, Pro ou Max : le comparatif chiffré des forfaits Claude",
    desc="Free, Pro, Max 5x, Max 20x : prix en euros, ce que chaque forfait débloque, et lequel choisir selon ton usage.",
    og_pill="Les bases de l'IA · 10", og_titre="Gratuit, Pro ou Max : le comparatif chiffré",
    marque="Les bases de l'IA · 10",
    h1="Gratuit, Pro ou Max : <em>lequel est fait pour toi</em>",
    chapo="Quatre forfaits pour les particuliers et les indépendants. Le même Claude, mais pas les mêmes modèles, pas les mêmes outils, et surtout pas la même quantité. Voici le comparatif, prix relevés sur la page officielle.",
    verifie="13/10/2026",
    sources=[SRC_FORFAITS],
    corps="""
<section>
  <h2>Les quatre forfaits</h2>
  <div class="cartes">
    <div class="carte"><div class="nom">Free · <b>découvrir</b></div><p>Discuter, rédiger, chercher sur le web, créer des fichiers. Modèles Sonnet et Haiku. Mémoire entre les conversations, jusqu'à 5 projets.</p><div class="prix">0 €</div></div>
    <div class="carte"><div class="nom">Pro · <b>le vrai départ</b></div><p>Au moins 5 fois l'usage du gratuit. Débloque Opus, Claude Code, la recherche approfondie, Claude dans Chrome et Microsoft 365, les projets illimités.</p><div class="prix">18 € par mois, ou 15 € par mois à l'année (180 €)</div></div>
    <div class="carte"><div class="nom">Max 5x · <b>tous les jours</b></div><p>5 fois l'usage de Pro. Accès à Fable jusqu'à 50 % des limites de la semaine, accès prioritaire aux heures de pointe, 100 $ de crédits API par mois.</p><div class="prix">À partir de 90 € par mois</div></div>
    <div class="carte"><div class="nom">Max 20x · <b>toute la journée</b></div><p>20 fois l'usage de Pro. Mêmes accès que Max 5x, 200 $ de crédits API par mois.</p><div class="prix">Plus cher que Max 5x, facturé au mois</div></div>
  </div>
  <p class="note">Prix affichés hors taxes. Max se paie uniquement au mois, Pro au mois ou à l'année.</p>
</section>

<section>
  <h2>Ce qui change vraiment</h2>
  <div class="tab"><table>
    <thead><tr><th></th><th>Free</th><th>Pro</th><th>Max</th></tr></thead>
    <tbody>
      <tr><td>Opus</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
      <tr><td>Fable</td><td>Non</td><td>En crédits payants</td><td>50 % des limites</td></tr>
      <tr><td>Claude Code</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
      <tr><td>Recherche approfondie</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
      <tr><td>Projets</td><td>5 max</td><td>Illimités</td><td>Illimités</td></tr>
      <tr><td>Crédits API inclus</td><td>Non</td><td>Non</td><td>100 à 200 $</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Comment marchent les limites</h2>
  <ul class="liste">
    <li><b>Une fenêtre de 5 heures</b> qui se recharge en continu, plus une <b>limite par semaine</b> sur les formules payantes.</li>
    <li><b>Pas de nombre de messages fixe.</b> Tout dépend de la longueur de tes conversations, du modèle et des outils utilisés.</li>
    <li><b>Un seul compteur</b> pour le chat (web, ordinateur, téléphone) et Claude Code.</li>
    <li><b>Limite atteinte ?</b> Tu attends, tu passes au forfait du dessus, ou sur une formule payante tu actives des crédits au tarif API.</li>
  </ul>
  <p class="note">Pour tenir plus longtemps avec le même forfait : <a href="/token">trois façons de réduire ta facture</a>.</p>
</section>

<section>
  <div class="regle">
    <h2>Comment choisir</h2>
    <ol class="etapes">
      <li><b>Commence gratuit</b> pour voir si l'outil te parle.</li>
      <li><b>Passe en Pro</b> dès que tu veux produire pour de vrai, ou utiliser Claude Code.</li>
      <li><b>Monte en Max</b> le jour où tu touches ta limite plusieurs fois par jour. Max 5x d'abord, 20x si tu vis dedans.</li>
    </ol>
  </div>
  <p class="note">Ne paie jamais un forfait que tu ne remplis pas encore. Pour une équipe, il existe les formules Team et Enterprise, elles ont leur propre vidéo.</p>
</section>
""",
)

# ─────────────────────────────── 03 · OÙ RÉCUPÉRER CLAUDE
PAGES["recuperer"] = dict(
    video="03 · Où récupérer Claude",
    title="Où récupérer Claude : les liens officiels et les étapes",
    desc="Créer ton compte Claude, installer l'application sur ordinateur et téléphone, uniquement depuis les liens officiels.",
    og_pill="Les bases de l'IA · 03", og_titre="Où récupérer Claude : les liens et les étapes",
    marque="Les bases de l'IA · 03",
    h1="Où récupérer Claude, <em>les liens officiels</em>",
    chapo="Claude est gratuit pour commencer, et il marche partout : dans ton navigateur, sur ton ordinateur et sur ton téléphone. Voici les étapes, et uniquement les liens officiels.",
    verifie="13/10/2026",
    sources=[("Téléchargements officiels", "https://claude.com/fr/download"), SRC_FORFAITS],
    corps="""
<section>
  <h2>Les étapes</h2>
  <ol class="etapes">
    <li><b>Crée ton compte</b> sur <a href="https://claude.ai">claude.ai</a>, avec ton adresse mail ou ton compte Google. C'est gratuit, aucune carte bancaire demandée.</li>
    <li><b>Commence dans ton navigateur.</b> Rien à installer, tu peux poser ta première question tout de suite.</li>
    <li><b>Installe l'application sur ton ordinateur</b> si tu l'utilises souvent : <a href="https://claude.com/fr/download">claude.com/fr/download</a>, version Mac ou Windows.</li>
    <li><b>Installe l'application sur ton téléphone</b> : <a href="https://apps.apple.com/app/claude-by-anthropic/id6473753684">iPhone (App Store)</a> ou <a href="https://play.google.com/store/apps/details?id=com.anthropic.claude">Android (Google Play)</a>.</li>
    <li><b>Connecte-toi avec le même compte</b> partout. Tes conversations te suivent d'un appareil à l'autre.</li>
  </ol>
</section>

<section>
  <h2>Attention aux fausses applis</h2>
  <div class="encadre"><b>Une seule source</b>Le vrai Claude est édité par Anthropic. Télécharge-le uniquement depuis claude.com ou depuis les stores officiels, avec Anthropic comme éditeur. Les applis « Claude IA chat » d'autres éditeurs ne sont pas Claude. Vérifie toujours le nom de l'éditeur avant d'installer.</div>
</section>

<section>
  <h2>Gratuit ou payant ?</h2>
  <p>Le gratuit suffit pour découvrir : discuter, rédiger, chercher sur le web. Le forfait Pro (18 € par mois, 15 € à l'année) débloque plus d'usage, le modèle Opus et Claude Code.</p>
  <p class="note">Le comparatif complet, chiffré : <a href="/forfaits">Gratuit, Pro ou Max</a>.</p>
</section>

<section>
  <h2>Ta première question</h2>
  <p>Pas besoin de formule magique. Parle-lui comme à un collègue, avec ton contexte :</p>
  <pre><code>Je suis [ton métier]. Quelles sont les 3 tâches répétitives de ma semaine que tu pourrais m'aider à faire plus vite ?</code></pre>
</section>
""",
)

# ─────────────────────────────── 04 · C'EST QUOI CLAUDE CODE
PAGES["claude-code"] = dict(
    video="04 · C'est quoi Claude Code",
    title="Installer Claude Code : le guide pas à pas",
    desc="Claude Code expliqué simplement : où le trouver, comment l'installer sur Mac ou Windows, et tes premières commandes.",
    og_pill="Les bases de l'IA · 04", og_titre="Installer Claude Code : le guide pas à pas",
    marque="Les bases de l'IA · 04",
    h1="Installer Claude Code, <em>pas à pas</em>",
    chapo="Claude Code, c'est Claude qui ne se contente plus de te répondre : il agit sur les fichiers de ton ordinateur. Il les lit, les modifie, en crée, et te demande la permission avant. Voici comment l'installer et faire tes premiers pas.",
    verifie="13/10/2026",
    sources=[("Documentation officielle Claude Code", "https://code.claude.com/docs/en/quickstart"), SRC_FORFAITS],
    corps="""
<section>
  <h2>Avant de commencer</h2>
  <ul class="liste">
    <li><b>Un forfait payant</b> (Pro, Max, Team ou Enterprise). Claude Code n'est pas dans le gratuit.</li>
    <li><b>Un dossier de test.</b> Pour tes premiers essais, crée un dossier vide sur ton bureau. Tu ne risques rien.</li>
  </ul>
</section>

<section>
  <h2>Trois façons de l'utiliser</h2>
  <div class="cartes">
    <div class="carte"><div class="nom">Dans l'application Claude · <b>le plus simple</b></div><p>Sur ordinateur, l'application Claude intègre Claude Code. Aucune commande à taper.</p></div>
    <div class="carte"><div class="nom">Dans le navigateur · <b>rien à installer</b></div><p>Sur <a href="https://claude.ai/code">claude.ai/code</a>, il travaille sur tes projets en ligne.</p></div>
    <div class="carte"><div class="nom">Dans le terminal · <b>le plus puissant</b></div><p>La version d'origine. C'est celle qu'on installe ci-dessous.</p></div>
  </div>
</section>

<section>
  <h2>L'installer dans le terminal</h2>
  <ol class="etapes">
    <li><b>Ouvre le terminal.</b> Sur Mac : la loupe en haut à droite, tape « Terminal ». Sur Windows : menu Démarrer, tape « PowerShell ».</li>
    <li><b>Colle la commande de ton système</b> et appuie sur Entrée.
      <p style="margin-top:6px"><small><b>Mac ou Linux</b></small></p>
      <pre><code>curl -fsSL https://claude.ai/install.sh | bash</code></pre>
      <p><small><b>Windows (PowerShell)</b></small></p>
      <pre><code>irm https://claude.ai/install.ps1 | iex</code></pre>
      L'installation n'affiche rien pendant le téléchargement, c'est normal.</li>
    <li><b>Ferme et rouvre le terminal</b>, puis vérifie :
      <pre><code>claude --version</code></pre>
      Un numéro de version s'affiche ? C'est installé.</li>
    <li><b>Va dans ton dossier de test et lance Claude Code</b> :
      <pre><code>cd Desktop/test
claude</code></pre></li>
    <li><b>Connecte-toi.</b> Au premier lancement, ton navigateur s'ouvre : connecte-toi avec ton compte Claude. C'est à faire une seule fois.</li>
  </ol>
  <p class="note">Ces commandes viennent de la documentation officielle d'Anthropic. Ne colle jamais dans ton terminal une commande d'installation trouvée ailleurs.</p>
</section>

<section>
  <h2>Tes premiers essais</h2>
  <p>Tu lui parles en français, normalement. Quelques idées pour commencer :</p>
  <pre><code>Crée un fichier liste-courses.txt avec 10 idées de repas rapides pour la semaine.</code></pre>
  <pre><code>Range les fichiers de ce dossier dans des sous-dossiers par type.</code></pre>
  <pre><code>Explique-moi ce que contient ce dossier.</code></pre>
  <p>Avant de modifier quoi que ce soit, il te montre ce qu'il va faire et te demande ton accord. Lis, puis valide.</p>
</section>

<section>
  <h2>Les commandes à connaître</h2>
  <div class="tab"><table>
    <thead><tr><th>Commande</th><th>Ce qu'elle fait</th></tr></thead>
    <tbody>
      <tr><td><code>claude</code></td><td>Lance Claude Code dans le dossier où tu es</td></tr>
      <tr><td><code>claude -c</code></td><td>Reprend ta dernière conversation</td></tr>
      <tr><td><code>/help</code></td><td>Affiche l'aide</td></tr>
      <tr><td><code>/clear</code></td><td>Repart d'une conversation vide</td></tr>
      <tr><td><code>/exit</code></td><td>Quitte Claude Code</td></tr>
      <tr><td>Maj + Tab</td><td>Change le niveau d'autonomie (demander avant d'agir, ou non)</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Les trois règles de sécurité</h2>
  <ol class="etapes">
    <li><b>Commence dans un dossier de test</b>, jamais directement dans tes documents importants.</li>
    <li><b>Lis avant de valider.</b> Il te demande la permission, ce n'est pas pour la forme.</li>
    <li><b>Fais une copie</b> de ce qui compte avant de lui confier un vrai dossier.</li>
  </ol>
</section>
""",
)

# ─────────────────────────────── 05 · C'EST QUOI COWORK
_METIERS = [
    ("Cabinet d'avocat", ["Résumer un dossier de 200 pages en note de synthèse.", "Préparer une trame de conclusions à partir de tes modèles.", "Comparer deux versions d'un contrat et lister les changements.", "Trier et renommer les pièces d'un dossier.", "Faire le point hebdomadaire des échéances et délais de procédure."],
     ["Un outil interne de suivi des dossiers (statut, échéances, alertes).", "Générer automatiquement les courriers types.", "Remonter les mails urgents chaque matin.", "Une base interne interrogeable : modèles, notes, procédures.", "Un tableau de bord de l'activité du cabinet."]),
    ("Agence immobilière", ["Rédiger les annonces à partir des caractéristiques du bien.", "Préparer les dossiers de visite en PDF.", "Faire un comparatif de biens pour un acheteur.", "Trier et classer les photos par bien.", "Faire le point hebdomadaire des mandats, visites et offres."],
     ["Un outil qui rapproche acheteurs et biens.", "Relancer automatiquement les prospects par mail.", "Un tableau de bord : délai de vente, prix au m².", "Une veille des nouveaux biens du secteur.", "Un mini-site de présentation pour un bien d'exception."]),
    ("Cabinet comptable", ["Préparer un tableau de bord financier client (Excel avec formules).", "Rédiger la note de synthèse d'un bilan.", "Trier et classer les pièces comptables reçues.", "Lister les pièces manquantes et rédiger les relances.", "Faire le rapport mensuel de chaque client."],
     ["Importer et catégoriser les relevés bancaires.", "Automatiser les rapprochements simples.", "Une alerte sur les échéances fiscales.", "Un tableau de bord de rentabilité par client.", "Extraire les données de ton logiciel de compta."]),
    ("Artisan, bâtiment", ["Rédiger et chiffrer un devis à partir de tes tarifs.", "Sortir une facture propre en PDF.", "Faire le compte-rendu de chantier pour le client.", "Ranger et nommer les photos de chantier.", "Préparer les réponses aux demandes de devis."],
     ["Un suivi des chantiers et de la marge.", "Relancer automatiquement les devis non signés.", "Un planning simple des interventions.", "Un formulaire de demande de devis sur ton site.", "Un tableau des achats de matériaux."]),
    ("Restaurant, traiteur", ["Calculer le coût de revient d'une fiche recette.", "Rédiger la carte et ses descriptions.", "Répondre aux avis clients dans ton ton.", "Préparer le planning de la semaine à partir des disponibilités.", "Faire le point du mois : chiffre d'affaires, achats, coût matière."],
     ["Un tableau qui suit le coût matière en continu.", "Rassembler les factures fournisseurs au même endroit.", "Un formulaire de devis pour les groupes et événements.", "Une alerte quand un produit dépasse son prix habituel.", "Un tableau de bord de la semaine."]),
    ("Agence de communication", ["Décliner un brief en plan de contenu.", "Proposer des variantes de posts et d'accroches.", "Faire le rapport de performance des campagnes.", "Préparer les présentations client.", "Organiser les fichiers par client et par projet."],
     ["Un outil de planification des contenus.", "Automatiser le reporting de plusieurs plateformes.", "Générer des pages d'atterrissage pour tes clients.", "Une veille concurrentielle automatique.", "Un tableau de suivi des projets."]),
    ("Cabinet médical, santé", ["Mettre en forme des comptes-rendus à partir de tes notes.", "Rédiger les courriers types (confrères, patients).", "Faire le rapport d'activité de la semaine.", "Organiser les protocoles et la documentation interne.", "Préparer des fiches d'information patient."],
     ["Un outil de rappel des rendez-vous.", "Préparer automatiquement la journée du lendemain.", "Un tableau de bord d'activité.", "Un formulaire de pré-consultation.", "Un annuaire interne des correspondants."]),
    ("Architecte", ["Rédiger les notices descriptives à partir de tes modèles.", "Préparer les dossiers de présentation projet.", "Faire le rapport d'avancement de chantier.", "Organiser plans et documents par projet.", "Comparer les devis des entreprises dans un tableau."],
     ["Un suivi de projet : phases, échéances, budget.", "Générer les documents administratifs.", "Un tableau de rentabilité par projet.", "Un espace client pour valider les étapes.", "Une veille sur les normes."]),
    ("Commercial", ["Préparer une proposition commerciale.", "Faire le compte-rendu d'un rendez-vous à partir de tes notes.", "Faire le point hebdomadaire de ton portefeuille.", "Personnaliser tes mails de prospection.", "Résumer une fiche prospect avant un appel."],
     ["Un fichier clients simple et sur mesure.", "Automatiser les relances.", "Classer tes prospects par priorité.", "Un tableau de bord des ventes.", "Envoyer tes mails directement dans ton fichier clients."]),
    ("Indépendant, solo", ["Tenir une compta simplifiée dans un tableau.", "Rédiger tes contenus (site, réseaux).", "Préparer factures et relances.", "Organiser tes fichiers et ta documentation.", "Résumer ta veille et tes lectures."],
     ["Automatiser ta facturation.", "Un mini-site ou un portfolio.", "Un suivi de tes missions.", "Une veille automatique sur ton secteur.", "Un tableau de bord de ton activité."]),
]


def _metiers_html():
    blocs = []
    for nom, app, code in _METIERS:
        items = "".join(f'<li><span class="tag app">Appli</span>{x}</li>' for x in app)
        items += "".join(f'<li><span class="tag code">Claude Code</span>{x}</li>' for x in code)
        blocs.append(f'<details><summary>{nom}</summary><div class="dedans"><ol>{items}</ol></div></details>')
    return "\n    ".join(blocs)


PAGES["cowork"] = dict(
    video="05 · C'est quoi Cowork",
    title="Cowork : 10 exemples concrets par métier",
    desc="Ce que Claude peut faire de ton travail de bureau : 10 exemples concrets pour 10 métiers, de l'avocat à l'artisan.",
    og_pill="Les bases de l'IA · 05", og_titre="Cowork : 10 exemples concrets par métier",
    marque="Les bases de l'IA · 05",
    h1="10 exemples concrets <em>par métier</em>",
    chapo="Cowork, c'est Claude qui fait ton travail de bureau à ta place : il ouvre tes fichiers, produit des documents, trie, prépare des rapports. Voici ce que ça donne, métier par métier.",
    verifie="13/10/2026",
    sources=[SRC_FORFAITS],
    corps=f"""
<section>
  <div class="encadre"><b>Ça a changé de nom</b>Depuis peu, Anthropic a fondu Cowork dans Claude : « Claude Cowork est désormais simplement Claude ». Le déploiement commence par les forfaits Pro et Max. Les exemples ci-dessous restent valables, ils se font simplement dans l'application Claude.</div>
</section>

<section>
  <h2>Choisis ton métier</h2>
  <p style="margin-bottom:14px"><span class="tag app">Appli</span>se fait dans l'application Claude, sans rien installer. <span class="tag code">Claude Code</span>construit un outil qui tourne tout seul ensuite.</p>
    {_metiers_html()}
</section>

<section>
  <h2>Les deux règles d'or</h2>
  <ol class="etapes">
    <li><b>Tu vérifies ce qui engage ta responsabilité.</b> Un chiffre, une date, une clause : Claude prépare, tu valides.</li>
    <li><b>Données sensibles, prudence.</b> Secret professionnel, données de santé, données clients : jamais dans un compte personnel sans avoir vérifié les réglages et la formule adaptée. Demande avant.</li>
  </ol>
</section>
""",
    fin="Ton métier n'est pas dans la liste, ou tu ne sais pas par où commencer ? C'est exactement le point de départ de mon accompagnement : je regarde tes tâches, je chiffre ce qu'elles te coûtent, et on commence par celle qui rapporte le plus.",
)

SRC_CONNECTEURS_FR = ("Aide Claude : connecteurs personnalisés (MCP distant)", "https://support.claude.com/fr/articles/11175166-get-started-with-custom-connectors-using-remote-mcp")
SRC_PLANIFIEES_FR = ("Aide Claude : tâches planifiées", "https://support.claude.com/fr/articles/13854387-schedule-recurring-tasks-in-claude-cowork")
PAGES["jarvis"] = dict(
    video="29 · Mon Jarvis",
    title="Ton Jarvis personnel avec Claude : le premier à copier",
    desc="Un assistant qui te briefe chaque matin, construit avec Claude, sans installer de projet inconnu. La règle, le brief du matin prêt à copier, et les pièges à éviter.",
    og_pill="Les bases de l'IA · 29", og_titre="Ton Jarvis personnel : le premier à copier",
    marque="Les bases de l'IA · 29",
    h1="Ton <em>Jarvis</em> personnel",
    chapo="Pas besoin d'installer un projet GitHub inconnu. Un Jarvis, c'est Claude, des tâches programmées, et une règle. Voici comment j'ai construit le mien, et le premier à copier dès ce soir.",
    verifie="26/10/2026",
    sources=[SRC_FORFAITS, SRC_PLANIFIEES_FR, SRC_CONNECTEURS_FR],
    corps="""
<section>
  <h2><span class="num">1</span>Ce qu'il te faut</h2>
  <ul class="liste">
    <li><b>Un forfait Claude payant</b> (Pro, environ 18 € par mois) : les tâches planifiées et Claude Code y sont inclus.</li>
    <li><b>L'appli Claude sur ton ordinateur.</b></li>
    <li><b>Tes outils branchés</b> : dans Claude, active les connecteurs de ton agenda et de ta boîte mail (Paramètres, Connecteurs).</li>
  </ul>
  <p class="note">Rien d'autre à installer. Pas de clé à coller, pas de projet inconnu.</p>
</section>

<section>
  <h2><span class="num">2</span>La règle, avant tout</h2>
  <p>Colle-la une fois dans les instructions de ton projet, ou au début de chaque tâche :</p>
  <pre><code>Tu prépares, tu n'envoies jamais.
Tu ne réponds jamais à ma place, tu n'achètes rien, tu ne supprimes rien.
Tu me montres ce que tu as préparé, et c'est moi qui décide.</code></pre>
  <p>C'est ce qui fait la différence entre un assistant et un risque.</p>
</section>

<section>
  <h2><span class="num">3</span>Ton premier Jarvis : le brief du matin</h2>
  <p>Dans une conversation Claude, colle ceci, puis clique « Planifier » et choisis « les jours de semaine, à 8 h » :</p>
  <pre><code>Chaque matin :
1. Lis mon agenda d'aujourd'hui : heure, titre, lieu ou lien de visio.
2. Regarde mes mails non lus des dernières 24 heures.
   Garde les 3 plus importants (clients et prospects d'abord),
   ignore les newsletters et les notifications.
3. Écris-moi un brief de 5 phrases maximum :
   mes rendez-vous, les 3 mails à traiter, et la priorité du jour.
Tu ne réponds à aucun mail. Tu prépares seulement.</code></pre>
  <div class="encadre"><b>Le bonus : qu'il te le dise à voix haute</b>Le Mac sait lire un texte avec une voix française gratuite, déjà installée (Thomas). Si tu fais tourner la tâche dans Claude Code sur ton ordinateur, ajoute à la fin : « Puis lis le brief à voix haute avec la commande say -v Thomas ». Pour ça, l'ordinateur doit être allumé à 8 h.</div>
</section>

<section>
  <h2><span class="num">4</span>Les autres Jarvis que j'ai construits</h2>
  <ul class="liste">
    <li><b>Les mails clients</b> : il prépare la réponse en brouillon, je relis et j'envoie.</li>
    <li><b>Les alertes</b> : il me prévient sur un canal Telegram privé quand quelque chose d'important arrive.</li>
    <li><b>La veille</b> : il trie ce que je me mets de côté et me résume ce qui compte.</li>
  </ul>
  <p>Chacun repose sur la même règle : il prépare, je décide.</p>
</section>

<section>
  <h2>Ce qu'il ne faut pas faire</h2>
  <ol class="etapes">
    <li><b>Installer un projet GitHub sans le lire.</b> C'est du code qui tourne sur ta machine, avec tes accès. Vérifie d'où il vient avant.</li>
    <li><b>Lui donner le droit d'envoyer seul.</b> Un mail piégé peut contenir des consignes cachées. Tant que c'est toi qui appuies sur Envoyer, il ne peut rien faire à ta place.</li>
  </ol>
</section>
""",
    fin="Tu veux ton Jarvis construit sur mesure, sur tes outils et ton métier ? Écris-moi sur Instagram, @ardj.87 : on regarde ensemble ce qu'il peut te faire gagner.",
)

SRC_CODEX_PLUGIN = ("OpenAI : extension Codex pour Claude Code (README officiel)", "https://github.com/openai/codex-plugin-cc")
SRC_CODEX_PRIX = ("OpenAI : limites d'usage de Codex", "https://developers.openai.com/codex/pricing")
SRC_ARENA = ("Classement Arena (votes à l'aveugle)", "https://arena.ai/leaderboard")
PAGES["claude-chatgpt"] = dict(
    video="30 · Claude + ChatGPT",
    title="Connecter ChatGPT à Claude : l'installation pas à pas",
    desc="L'extension officielle d'OpenAI pour Claude Code : Claude confie du code et des relectures à ChatGPT, sur ton compte ChatGPT. Ce qu'il te faut, les 4 commandes, et les règles à garder.",
    og_pill="Les bases de l'IA · 30", og_titre="Connecter ChatGPT à Claude, pas à pas",
    marque="Les bases de l'IA · 30",
    h1="Connecter <em>ChatGPT</em> à Claude",
    chapo="Claude reste ton tableau de bord. ChatGPT devient son renfort : Claude lui confie du code ou une relecture, et ce travail est décompté sur ton compte ChatGPT. L'outil est officiel, publié par OpenAI. Voici exactement comment je l'ai installé.",
    verifie="27/10/2026",
    sources=[SRC_CODEX_PLUGIN, SRC_CODEX_PRIX, SRC_FORFAITS, SRC_ARENA],
    corps="""
<section>
  <h2><span class="num">1</span>Ce qu'il te faut</h2>
  <ul class="liste">
    <li><b>Un forfait Claude payant</b> (Pro, environ 18 € par mois) : Claude Code y est inclus.</li>
    <li><b>Un compte ChatGPT.</b> D'après OpenAI, même le compte gratuit marche. Le travail confié est décompté sur tes limites Codex (Codex, c'est l'agent de ChatGPT).</li>
    <li><b>Claude Code dans un terminal</b>, et Node.js 18.18 ou plus récent sur ton ordinateur.</li>
  </ul>
  <p class="note"><b>Pas besoin d'installer Codex avant.</b> Les 4 commandes ci-dessous suffisent : si Codex manque, <b>/codex:setup</b> propose de l'installer pour toi.</p>
</section>

<section>
  <h2><span class="num">2</span>L'installer : 4 commandes</h2>
  <p>Dans Claude Code, tape ces commandes une par une :</p>
  <pre><code>/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup</code></pre>
  <p><b>/codex:setup</b> vérifie que tout est prêt. S'il manque Codex, il propose de l'installer pour toi. S'il te demande de te connecter, tape <b>!codex login</b> et connecte-toi avec ton compte ChatGPT.</p>
  <p class="note">Avant d'installer, vérifie toujours la source : ici, c'est le dépôt <b>openai/codex-plugin-cc</b>, publié par OpenAI. Méfie-toi des copies au nom proche.</p>
</section>

<section>
  <h2><span class="num">3</span>L'utiliser</h2>
  <ul class="liste">
    <li><b>/codex:review</b> : ChatGPT relit le travail en cours, sans rien modifier. Un deuxième avis.</li>
    <li><b>/codex:rescue</b> : Claude lui confie une tâche (écrire du code, chercher la cause d'un bug).</li>
    <li><b>/codex:status</b> et <b>/codex:result</b> : où il en est, et ce qu'il a rendu.</li>
  </ul>
  <p>Tu peux aussi le dire en français à Claude : « confie ça à Codex, puis relis ce qu'il a fait ».</p>
</section>

<section>
  <h2><span class="num">4</span>Mes règles</h2>
  <ol class="etapes">
    <li><b>Claude a le dernier mot.</b> Tout ce que ChatGPT rend, Claude le relit avant de l'utiliser.</li>
    <li><b>Aucune donnée client chez OpenAI.</b> Ce que tu confies à Codex part sur les serveurs d'OpenAI, sous ton compte. Jamais de contrat, de fichier client ou de donnée personnelle.</li>
    <li><b>Pas de relecture automatique à chaque fin de tâche.</b> L'option existe, elle est coupée par défaut : laisse-la coupée, elle vide tes limites très vite.</li>
  </ol>
</section>

<section>
  <h2>Pourquoi Claude au centre</h2>
  <p>Au classement Arena, où les utilisateurs votent à l'aveugle, relevé le 27/10/2026 : en création de sites et d'applis, Claude Opus 5.5 est premier et GPT-6 Astra deuxième. En conversation, le meilleur modèle d'OpenAI est 21e (Gemini 4 est premier, Claude deuxième). Ces classements bougent chaque mois : vérifie la date.</p>
</section>
""",
    fin="Tu veux une organisation comme la mienne, adaptée à ton métier ? Écris-moi sur Instagram, @ardj.87 : on regarde ensemble ce que ça peut te faire gagner.",
)

# ─────────────────────────────── 31 · LE MONTAGE AVEC CLAUDE
SRC_ADOBE_PODCAST = ("Adobe Podcast : offres et limites de la version gratuite", "https://podcast.adobe.com/en/plans")
SRC_HYPERFRAMES = ("HyperFrames (HeyGen), dépôt officiel, licence Apache 2.0", "https://github.com/heygen-com/hyperframes")
SRC_FAL_KONTEXT = ("fal.ai : modèle FLUX.1 Kontext (édition d'image)", "https://fal.ai/models/fal-ai/flux-pro/kontext")

PAGES["montage-ia"] = dict(
    video="31 · Le montage avec Claude",
    title="Monter ses vidéos avec Claude : le pas à pas complet",
    desc="Tout ce qu'il faut pour que Claude monte tes vidéos à partir de ta voix : les outils, les prix, les consignes à copier, et les pièges. Gratuit, sans rien à acheter en plus de Claude.",
    og_pill="Je te montre tout", og_titre="Monter ses vidéos avec Claude, pas à pas",
    marque="Je te montre tout",
    h1="Monter ses vidéos avec <em>Claude</em>",
    chapo="Mes vidéos, je ne les monte pas. J'enregistre ma voix, et Claude fabrique tout le reste : les coupes, les sous-titres, le personnage, les dessins, les bruitages. Voici exactement ce qu'il te faut, et les consignes que je lui donne.",
    verifie="28/10/2026",
    sources=[SRC_FORFAITS, SRC_ADOBE_PODCAST, SRC_HYPERFRAMES, SRC_FAL_KONTEXT],
    corps="""
<section>
  <h2><span class="num">1</span>Ce qu'il te faut</h2>
  <ul class="liste">
    <li><b>Un forfait Claude payant</b> (Pro, environ 18 € par mois) : Claude Code y est inclus.</li>
    <li><b>L'application Claude sur ton ordinateur, onglet Code.</b> Pas le site dans le navigateur : Claude doit pouvoir lire tes fichiers audio et écrire la vidéo sur ton disque.</li>
    <li><b>Adobe Podcast</b> (fonction Enhance Speech) pour nettoyer ta voix. Gratuit jusqu'à 1 heure d'audio par jour, 30 minutes maximum par fichier.</li>
    <li><b>Un personnage, si tu ne veux pas te filmer.</b> Dessine-le une fois (Canva, ou un illustrateur), puis fais fabriquer ses poses par une IA d'image : une clé <b>fal.ai</b>, payée à l'usage (0,04 $ l'image chez nous en octobre 2026), ou ton compte <b>Canva</b> (attention, son quota d'images IA s'épuise vite : 3 images chez nous).</li>
  </ul>
  <p class="note"><b>Le reste est gratuit, et c'est Claude qui l'installe :</b> FFmpeg (couper et assembler le son et l'image), Whisper (transcrire ta voix mot à mot, en local), Node.js et <b>HyperFrames</b> (l'outil open source de HeyGen qui transforme une page web animée en vidéo MP4).</p>
</section>

<section>
  <h2><span class="num">2</span>Installer les outils</h2>
  <p>Ouvre l'application Claude, onglet Code, choisis un dossier vide (par exemple « Montage »), et colle :</p>
  <pre><code>Installe sur mon ordinateur FFmpeg, whisper.cpp avec un modèle
qui comprend le français, Node.js, et HyperFrames (dépôt officiel
heygen-com/hyperframes). Vérifie chaque outil après l'installation
et dis-moi ce qui manque. Ne télécharge rien d'autre sans me demander.</code></pre>
  <p class="note">Avant chaque installation, vérifie la source : HyperFrames vient du dépôt <b>heygen-com/hyperframes</b>. Méfie-toi des copies au nom proche.</p>
</section>

<section>
  <h2><span class="num">3</span>Écrire le script</h2>
  <p>C'est l'étape qui fait la différence. Écris ton texte avec Claude, puis <b>relis-le en entier avant d'enregistrer ou de fabriquer la moindre image</b> : une phrase floue à l'oral donne une vidéo floue.</p>
  <ul class="liste">
    <li><b>Sois précis</b> : les vrais chiffres, les vrais noms d'outils, les vrais prix, avec la date.</li>
    <li><b>Tu ne trouves pas les mots ?</b> Envoie à Claude des vidéos qui t'inspirent (lien ou transcription) et demande-lui de s'en servir pour le ton et le rythme, sans les copier.</li>
    <li><b>Compte la durée</b> : à l'oral, on dit environ 3 mots par seconde. 250 mots, c'est à peu près 1 min 20.</li>
  </ul>
</section>

<section>
  <h2><span class="num">4</span>Enregistrer ta voix</h2>
  <ul class="liste">
    <li><b>Pièce calme, micro près de la bouche</b> (celui du téléphone suffit).</li>
    <li><b>Tu rates une phrase ? Tu la redis</b>, sans couper l'enregistrement. Claude gardera la dernière bonne version.</li>
    <li><b>Vise 75 à 85 secondes.</b> TikTok ne rémunère que les vidéos de plus d'une minute, et si tu accélères la vidéo au montage, elle raccourcit.</li>
  </ul>
  <p>Passe ensuite le fichier dans Adobe Podcast (Enhance Speech) : il enlève le souffle, l'écho et le bruit de la pièce. Télécharge le résultat dans ton dossier.</p>
</section>

<section>
  <h2><span class="num">5</span>Le montage de la voix</h2>
  <p>Mets ton texte et ta prise dans le dossier, puis colle :</p>
  <pre><code>Voici ma prise (voix.wav) et mon texte (texte.txt).
Transcris la prise mot à mot avec whisper, avec l'heure de chaque mot.
Pour chaque phrase du texte, garde ma dernière version sans erreur,
enlève les ratés, les hésitations et les silences trop longs,
et assemble un nouveau fichier.
Puis retranscris ce fichier et vérifie qu'il ne manque aucun mot.</code></pre>
</section>

<section>
  <h2><span class="num">6</span>La vidéo</h2>
  <p>Mets les poses de ton personnage dans un sous-dossier « poses », puis colle :</p>
  <pre><code>Fabrique une vidéo verticale 1080 x 1920 avec HyperFrames, sur ma voix montée.
Sous-titres mot à mot, calés sur la transcription.
Une pose du personnage par phrase, choisie selon le sens.
Une carte dessinée à chaque chiffre, outil ou étape que je cite,
qui apparaît exactement quand je prononce le mot.
Un fond qui change entre les parties.
Ajoute des bruitages discrets sur les apparitions,
règle le volume pour qu'il soit régulier, puis rends la vidéo en MP4.</code></pre>
  <p class="note">Sur un ordinateur de 8 Go, lance <b>un seul rendu à la fois</b>. Le rendu passe par un navigateur Chrome invisible : si l'ordinateur rame après, demande à Claude de fermer les Chrome restés ouverts.</p>
</section>

<section>
  <h2><span class="num">7</span>Relire et corriger</h2>
  <p>Regarde la vidéo en entier, comme un spectateur. Puis parle à Claude comme à un monteur, avec le moment précis :</p>
  <pre><code>À 0:12, la carte arrive trop tôt : cale-la sur le mot « gratuit ».
À 0:40, le sous-titre cache le personnage : remonte-le.
Le bruit de la coche n'est pas agréable : enlève-le.</code></pre>
  <p>Il corrige et refait le rendu. Une fois que tout te va, demande-lui aussi une image de couverture et la légende du post.</p>
  <p class="note"><b>Petit conseil : range tout au même endroit.</b> Demande à Claude un dossier sur ton Bureau avec trois sous-dossiers : « À tourner » (les scripts validés), « À poster » (vidéo, couverture et légende prêtes) et « Déjà posté ». Si ton Bureau est synchronisé avec iCloud (ou si tu prends un dossier Google Drive), tu retrouves tes vidéos sur ton téléphone pour les publier.</p>
</section>

<section>
  <h2>Mes règles</h2>
  <ol class="etapes">
    <li><b>C'est moi qui écris et qui décide.</b> Claude fabrique, il ne choisit pas le message.</li>
    <li><b>Chaque chiffre est vérifié à la source</b>, avec la date, avant d'être dit.</li>
    <li><b>Un vrai son ou rien.</b> Un bruitage qui sonne faux fait plus de mal que le silence.</li>
  </ol>
</section>
""",
    fin="Tu veux qu'on mette ça en place pour toi, adapté à ton métier ? Écris-moi sur Instagram, @ardj.87.",
)

# ─────────────────────────────── 32 · LES CODES PROMO
SRC_CHROME = ("Aide Claude : démarrer avec Claude pour Chrome", "https://support.claude.com/fr/articles/12012173-demarrage-avec-claude-pour-chrome")
SRC_TG_BOTFATHER = ("Telegram : créer un bot avec BotFather", "https://core.telegram.org/bots/tutorial")
SRC_TG_API = ("Telegram : API des bots (getUpdates, sendMessage)", "https://core.telegram.org/bots/api")

PAGES["promo"] = dict(
    video="32 · Les codes promo avec Claude",
    title="Trouver les codes promo avec Claude : le pas à pas",
    desc="Claude cherche les codes promo, les teste un par un dans ton panier et te prévient sur Telegram dès qu'un code fait vraiment baisser le total. Le pas à pas et la consigne à copier.",
    og_pill="Je te montre tout", og_titre="Les codes promo avec Claude, pas à pas",
    marque="Je te montre tout",
    h1="Les codes promo avec <em>Claude</em>",
    chapo="Claude cherche les codes, les teste un par un dans ton panier, et te prévient sur Telegram dès qu'un code fait vraiment baisser le total. Toi, tu payes. Voici exactement comment je fais, et la consigne à copier.",
    verifie="30/10/2026",
    sources=[SRC_FORFAITS, SRC_CHROME, SRC_TG_BOTFATHER, SRC_TG_API],
    corps="""
<section>
  <h2><span class="num">1</span>Ce qu'il te faut</h2>
  <ul class="liste">
    <li><b>Un forfait Claude payant</b> (Pro, environ 18 € par mois).</li>
    <li><b>L'extension Claude pour Chrome.</b> Incluse dans tous les forfaits payants (Pro, Max, Team, Enterprise), pas dans le gratuit. Elle marche dans Google Chrome, sur ordinateur.</li>
    <li><b>Telegram</b>, gratuit, pour être prévenu sur ton téléphone.</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Créer ton bot Telegram (deux minutes)</h2>
  <ol class="etapes">
    <li>Dans Telegram, cherche <b>@BotFather</b> (le compte officiel, avec le badge bleu) et écris-lui <b>/newbot</b>.</li>
    <li>Donne un nom à ton bot, puis un identifiant qui finit par « bot » (par exemple « mespromos_bot »).</li>
    <li>BotFather te répond avec un <b>jeton</b> (une longue suite de chiffres et de lettres). Garde-le de côté.</li>
    <li>Ouvre la conversation avec ton nouveau bot et envoie-lui « bonjour ».</li>
    <li>Dans Chrome, ouvre cette adresse en remplaçant TON_JETON :<br><code>https://api.telegram.org/botTON_JETON/getUpdates</code><br>Repère <b>"chat":{"id":</b> suivi d'un nombre : c'est ton numéro de conversation.</li>
  </ol>
  <p class="note">Le jeton ne donne accès qu'à ton bot, pas à ton compte Telegram ni à tes messages. Ne le publie quand même nulle part : avec lui, n'importe qui peut écrire au nom de ton bot.</p>
</section>

<section>
  <h2><span class="num">3</span>Remplir ton panier, sans payer</h2>
  <p>Va sur le site, connecte-toi si tu as un compte, et mets dans le panier ce que tu veux vraiment acheter. Pas encore décidé ? Fais la liste des produits, toutes marques confondues, et donne-la à Claude.</p>
</section>

<section>
  <h2><span class="num">4</span>La consigne à copier</h2>
  <p>Sur l'onglet de ton panier, ouvre Claude (l'icône de l'extension), et colle en remplaçant TON_JETON et TON_NUMERO :</p>
  <pre><code>Je suis sur mon panier. Ne paie rien, ne valide aucune commande,
ne saisis aucune information de paiement.
1. Note le total actuel du panier, frais de port compris.
2. Cherche tous les codes promo de cette marque : sur le web
   (sites de codes compris), sur son compte Instagram et son compte X,
   et chez les influenceurs qui travaillent avec elle.
3. Teste les codes un par un dans le champ « code promo ».
   Retire le code précédent avant chaque essai.
4. Ne te fie jamais au message « code appliqué » : regarde le total.
   S'il ne baisse pas, le code ne marche pas, passe au suivant.
5. Garde dans le panier le code qui donne le plus petit total.
6. Dès qu'un code fait baisser le total, préviens-moi en ouvrant
   dans un nouvel onglet :
   https://api.telegram.org/botTON_JETON/sendMessage?chat_id=TON_NUMERO&amp;text=
   suivi du code et du nouveau total.
7. À la fin, fais-moi un tableau : code, où tu l'as trouvé, total obtenu.</code></pre>
  <p class="note">Claude te demande l'autorisation avant d'agir sur un nouveau site : accepte pour le site de la marque. Reste à côté pendant qu'il travaille, et ne lui donne jamais tes coordonnées bancaires. <b>C'est toujours toi qui payes.</b></p>
</section>

<section>
  <h2><span class="num">5</span>Ce que mon test m'a appris</h2>
  <ul class="liste">
    <li><b>Mon panier du 29/10</b> : 3 pots de whey de 1 kg chez Nutrimuscle, 212,85 € affichés. La promo du site retire 31,92 €, le code d'influenceur trouvé par Claude 9,04 € de plus. Total : <b>171,89 €</b>.</li>
    <li><b>Le chiffre annoncé n'est pas le vrai.</b> Les codes étaient annoncés à 10, 15 ou 20 % sur les sites de codes. Dans le panier, ils donnaient tous 5 %.</li>
    <li><b>Il n'y a pas toujours de code.</b> Sur le pot de 4 kg, aucun ne passait (« valide, mais non applicable »). Chez certaines marques, les remises sont liées à ton compte (étudiant, anniversaire, livraison).</li>
    <li><b>Les codes ne se cumulent pas entre eux</b>, mais un code peut s'ajouter à la promo du site. D'où l'intérêt de tester sur le vrai panier.</li>
  </ul>
</section>

<section>
  <h2>Mes règles</h2>
  <ol class="etapes">
    <li><b>C'est toujours moi qui paie.</b> Claude cherche et teste, il ne valide jamais la commande.</li>
    <li><b>Le total fait foi</b>, jamais le message du site.</li>
    <li><b>Un code réservé à quelqu'un d'autre, on ne force pas.</b> Je ne garde que les codes publics.</li>
  </ol>
</section>
""",
    fin="Tu veux qu'on automatise ce genre de tâche pour ton activité ? Écris-moi sur Instagram, @ardj.87.",
)


SRC_CLAUDE_PROMPTS = ("Anthropic : bonnes pratiques de prompt (rôle, exemples)", "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices")
SRC_OPENAI_META = ("OpenAI Cookbook : améliorer ses prompts par le meta prompting", "https://developers.openai.com/cookbook/examples/enhance_your_prompts_with_meta_prompting")

PAGES["meta"] = dict(
    video="33 · La méthode PRECISE",
    title="La méthode PRECISE et le métaprompt : la trame à copier",
    desc="La trame PRECISE en 7 lettres, mon exemple rempli pour le montage de mes vidéos, et le métaprompt qui la remplit à ta place. Tout est à copier-coller.",
    og_pill="Je te montre tout", og_titre="La méthode PRECISE et le métaprompt",
    marque="Je te montre tout",
    h1="La méthode <em>PRECISE</em>",
    chapo="Deux minutes à mettre en place, et ce sont les fondations de ton projet. Sans elle, ta demande est floue, et le résultat est moyen. Voici la trame, mon exemple rempli, et le métaprompt qui la remplit à ta place.",
    verifie="30/10/2026",
    sources=[SRC_CLAUDE_PROMPTS, SRC_OPENAI_META],
    corps="""
<section>
  <h2><span class="num">1</span>Les 7 lettres</h2>
  <ul class="liste">
    <li><b>P, le persona</b> : qui l'IA doit être.</li>
    <li><b>R, le rôle</b> : ce qu'elle doit te rendre.</li>
    <li><b>E, explicite</b> : la tâche, dite sans sous-entendu.</li>
    <li><b>C, le contexte</b> : les infos de fond.</li>
    <li><b>I, les instructions</b> : longueur, ton, format, ce qu'il faut éviter.</li>
    <li><b>S, les steps</b> : les étapes, dans l'ordre.</li>
    <li><b>E, les exemples</b> : à quoi ressemble le bon résultat.</li>
  </ul>
  <p class="note">PRECISE, c'est ma méthode, pas une norme officielle. Les deux points qu'Anthropic met en avant dans ses conseils, donner un rôle et donner des exemples, sont dedans.</p>
</section>

<section>
  <h2><span class="num">2</span>La trame vide, à copier</h2>
  <pre><code>[P · PERSONA] Qui tu dois être.
Tu es [un métier, une expertise précise].

[R · RÔLE] Ce que tu dois me rendre.
Ta mission : [le livrable, en une phrase].

[E · EXPLICITE] La tâche, sans sous-entendu.
[Ce que j'attends exactement.]

[C · CONTEXTE] Les infos de fond.
[Mon activité, mon public, ma situation, mes contraintes.]

[I · INSTRUCTIONS] Les règles.
Longueur : [...]. Ton : [...]. Format : [...]. À éviter : [...].

[S · STEPS] Les étapes, dans l'ordre.
1) [...] 2) [...] 3) [...]

[E · EXEMPLES] Le modèle du bon résultat.
[Un ou deux exemples de ce que j'aime.]</code></pre>
</section>

<section>
  <h2><span class="num">3</span>Mon exemple rempli : le montage de mes vidéos</h2>
  <pre><code>[P] Tu es un réalisateur de reels Instagram,
spécialiste de la vidéo verticale.

[R] Ta mission : me rendre une vidéo montée, prête à poster.
Avoir une vision, caler chaque image sur ma voix,
varier les angles et les plans pour garder l'attention
jusqu'au bout.

[E] Nettoie le son avec Adobe Podcast, dans Chrome.
Garde ma meilleure prise de chaque phrase.
Coupe les ratés et les silences.

[C] Je parle d'IA à des entrepreneurs.
Vidéo verticale d'une minute, pour Instagram et TikTok.

[I] Sous-titres mot à mot. Une pose du personnage
par phrase. Une carte à chaque chiffre.
Des mouvements sobres : une image arrive, puis reste figée.

[S] 1) La voix  2) Les sous-titres  3) Les poses
4) Les cartes  5) Le rendu

[E] Je joins une vidéo que j'aime.
Inspire-toi de son rythme, sans la copier.</code></pre>
  <p>Ça marche pour tout. Un <b>devis</b>, un <b>contrat</b>, un <b>audit</b> : tu changes le persona, le livrable et le contexte, la trame reste la même.</p>
</section>

<section>
  <h2><span class="num">4</span>Le métaprompt : la trame se remplit sans toi</h2>
  <p>Un métaprompt, c'est un prompt qui écrit un prompt. OpenAI appelle ça le « meta prompting ». C'est le seul moment où j'utilise le chat, et pas Claude Code.</p>
  <ol class="etapes">
    <li>Ouvre une conversation dans le chat de Claude.</li>
    <li>Colle la consigne ci-dessous, suivie de la trame vide de la partie 2.</li>
    <li>Raconte ton besoin, en vrac, avec tes mots.</li>
    <li>Il rédige le prompt. Tu relis, tu corriges.</li>
    <li>Tu le colles au début de ton projet dans Claude Code.</li>
  </ol>
  <pre><code>Tu es un expert en rédaction de prompts.
Je vais te donner une trame en 7 parties (PRECISE),
puis te raconter mon besoin.
Remplis-moi ce prompt, partie par partie,
comme le ferait un expert de mon domaine.
S'il te manque une information importante,
pose-moi tes questions avant d'écrire.
Rends-moi le prompt final en un seul bloc, prêt à copier.

Voici la trame :
[colle ici la trame vide]

Mon besoin :
[raconte ici]</code></pre>
  <p class="note">Comme ça, chaque conversation démarre avec la trame d'un expert du domaine.</p>
</section>

<section>
  <h2>Mes règles</h2>
  <ol class="etapes">
    <li><b>Je relis toujours le prompt</b> avant de m'en servir. Un mot faux au départ, et tout le projet part de travers.</li>
    <li><b>Les exemples inspirent, ils ne se copient pas.</b> Je montre ce que j'aime, et je demande le même niveau, pas la même vidéo.</li>
    <li><b>Un projet, un prompt.</b> Chaque nouveau projet repart de la trame.</li>
  </ol>
</section>
""",
    fin="Tu veux qu'on écrive ensemble les prompts de ton activité ? Écris-moi sur Instagram, @ardj.87.",
)
