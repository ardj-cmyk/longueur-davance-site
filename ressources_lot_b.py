# Lot B des pages ressources (vidéos 28 à 42, sauf 33 couverte par /modeles).
# Exécuté à la suite de ressources_pages.py : PAGES existe déjà, on ne fait qu'ajouter.
# Sources ouvertes et vérifiées le 15/10/2026.

SRC_ART1367 = ("Code civil, article 1367 (Légifrance)", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032042456")
SRC_DECRET_SIGNATURE = ("Décret n° 2017-1416 relatif à la signature électronique (Légifrance)", "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035676246")
SRC_EIDAS = ("Règlement eIDAS n° 910/2014, articles 3 et 25 (EUR-Lex)", "https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32014R0910")
SRC_ANSSI_CONFIANCE = ("ANSSI : les services de confiance (règlement eIDAS)", "https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/reglement-eidas/services-de-confiance/")
SRC_YOUTRUST = ("Youtrust : tarifs de l'application", "https://youtrust.com/fr-fr/prix-application")
SRC_CLAUDE_LEGAL = ("Anthropic : claude-for-legal (GitHub officiel)", "https://github.com/anthropics/claude-for-legal")
SRC_PROMPTING = ("Anthropic : bonnes pratiques de prompt", "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices")
SRC_FORFAITS_FR = ("Formules Claude (Team et Enterprise)", "https://claude.com/fr/pricing")
SRC_PRIVACY_TRAINING = ("Anthropic : mes données servent-elles à l'entraînement ?", "https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training")
SRC_PRIVACY_ROLES = ("Anthropic : responsable ou sous-traitant ?", "https://privacy.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller")
SRC_PRIVACY_DPA = ("Anthropic : le DPA (accord de traitement des données)", "https://privacy.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa")
SRC_PRIVACY_SERVEURS = ("Anthropic : où sont vos serveurs ?", "https://privacy.claude.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers")
SRC_RESIDENCE = ("Anthropic : résidence des données (API)", "https://platform.claude.com/docs/en/manage-claude/data-residency")
SRC_BEDROCK = ("Anthropic : Claude dans Amazon Bedrock, régions", "https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock")
SRC_OPENAI_MEMOIRE = ("OpenAI : Memory in ChatGPT", "https://help.openai.com/en/articles/8590148-memory-in-chatgpt")
SRC_CLAUDE_MEMOIRE = ("Aide Claude : recherche dans les conversations et mémoire", "https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context")
SRC_CLAUDE_MEMOIRE_FR = ("Aide Claude : la recherche et la mémoire (version française)", "https://support.claude.com/fr/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context")
SRC_CLAUDE_INCOGNITO = ("Aide Claude : les chats incognito", "https://support.claude.com/en/articles/12260368-use-incognito-chats")
SRC_SKILLS_CODE = ("Claude Code : les skills", "https://code.claude.com/docs/en/skills")
SRC_SKILLS_AIDE = ("Aide Claude : créer une skill personnalisée", "https://support.claude.com/en/articles/12512198-how-to-create-custom-skills")
SRC_ECON = ("Anthropic : Scenarios for our Economic Future", "https://www.anthropic.com/institute/econ-scenarios")
SRC_CNIL_PROSPECTION = ("CNIL : la prospection par courrier électronique", "https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel")
SRC_CNIL_KASPR = ("CNIL : sanction de 240 000 euros contre KASPR", "https://www.cnil.fr/fr/aspiration-de-donnees-sanction-de-240-000-euros-lencontre-de-la-societe-kaspr")
SRC_ANNUAIRE = ("DGCCRF : l'Annuaire des Entreprises, site public et gratuit", "https://www.economie.gouv.fr/dgccrf/actualites-dgccrf/decouvrez-lannuaire-des-entreprises-le-moteur-de-recherche-public-et-ouvert-qui-centralise-les-informations-legales-sur-les")
SRC_TWENTY_PRIX = ("Twenty : tarifs", "https://twenty.com/pricing")
SRC_TWENTY_GITHUB = ("Twenty : dépôt GitHub officiel et licence", "https://github.com/twentyhq/twenty")
SRC_TWENTY_DOCKER = ("Twenty : auto-hébergement avec Docker", "https://docs.twenty.com/developers/self-host/capabilities/docker-compose")
SRC_MIT = ("Open Source Initiative : licence MIT", "https://opensource.org/license/mit")
SRC_SUPERWHISPER = ("Superwhisper : site officiel et tarifs", "https://superwhisper.com/")
SRC_SW_MODELES = ("Superwhisper : choisir son modèle", "https://superwhisper.com/docs/get-started/choose-your-model")
SRC_SW_SENSIBLE = ("Superwhisper : données sensibles", "https://superwhisper.com/docs/security/sensitive-data")
SRC_SW_HISTORIQUE = ("Superwhisper : l'historique", "https://superwhisper.com/docs/get-started/interface-history")
SRC_STANFORD = ("Stanford HAI : 12 enseignements de l'AI Index 2026", "https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report")
SRC_MCK_2025 = ("McKinsey : AI at work but not at scale (enquête 2025)", "https://www.mckinsey.com/featured-insights/charts/ai-at-work-but-not-at-scale")
SRC_MCK_2026 = ("McKinsey : The State of AI, Global Survey 2026", "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai")


# ─────────────────────────────── 28 · CLAUDE A TUÉ DOCUSIGN ?
PAGES["signature-contrat"] = dict(
    video="28 · Claude a tué DocuSign ?",
    title="Faire signer un contrat avec Claude : le montage qui tient en cas de litige",
    desc="Claude rédige, un tiers de confiance fait signer. Les trois niveaux de signature électronique (eIDAS), ce que dit le Code civil, et comment choisir selon l'enjeu.",
    og_pill="Les bases de l'IA · 28", og_titre="Le montage propre pour faire signer un contrat",
    marque="Les bases de l'IA · 28",
    h1="Le montage propre, <em>celui qui tient</em>",
    chapo="Oui, Claude peut rédiger ton contrat et l'envoyer à signer. Mais une signature vaut par ce qu'elle prouve le jour d'un litige. Voici comment garder l'automatisation sans perdre la preuve.",
    verifie="16/10/2026",
    sources=[SRC_ART1367, SRC_DECRET_SIGNATURE, SRC_EIDAS, SRC_ANSSI_CONFIANCE, SRC_YOUTRUST],
    corps="""
<section>
  <h2>Ce que dit le droit</h2>
  <div class="encadre"><b>Une signature électronique est valable</b>Le Code civil (article 1367) la définit comme un procédé fiable d'identification, qui garantit son lien avec le document signé. Et le règlement européen eIDAS interdit de la refuser comme preuve au seul motif qu'elle est électronique.</div>
  <div class="encadre"><b>Mais toutes ne pèsent pas pareil</b>Le règlement européen eIDAS prévoit trois niveaux : simple, avancée, qualifiée. Seule la qualifiée a un effet juridique équivalent à une signature manuscrite. Et seule elle est présumée fiable (décret du 28 septembre 2017) : c'est alors à celui qui la conteste de prouver le contraire.</div>
  <div class="encadre"><b>Le piège du système maison</b>Ton outil enregistre l'heure, l'adresse IP, l'empreinte du document ? Très bien. Mais c'est toi qui as produit ces traces. En cas de litige, c'est à toi de prouver qu'elles sont fiables. Un témoin qui témoigne pour lui-même convainc mal.</div>
</section>

<section>
  <h2><span class="num">1</span>Le montage en trois étages</h2>
  <ol class="etapes">
    <li><b>Claude rédige</b> à partir de TON modèle de contrat, relu une fois par un avocat. Il remplit, il n'invente pas de clauses.</li>
    <li><b>Un prestataire de signature fait signer.</b> C'est lui le tiers de confiance : il identifie le signataire, horodate, et produit un dossier de preuves. Beaucoup proposent une API, donc l'envoi peut rester automatique.</li>
    <li><b>Tu archives le contrat signé avec le dossier de preuves du prestataire</b>, pas avec tes propres traces.</li>
  </ol>
  <p>La consigne à donner à Claude pour l'étape 1 :</p>
  <pre><code>Voici mon modèle de contrat, validé par mon avocat.
Remplis-le pour ce client avec ces informations : [infos].
Ne modifie, n'ajoute et ne supprime aucune clause.
À la fin, liste les champs remplis et ceux qui manquent.</code></pre>
</section>

<section>
  <h2><span class="num">2</span>Le bon niveau pour le bon enjeu</h2>
  <div class="tab"><table>
    <thead><tr><th>Niveau</th><th>Pour quoi</th></tr></thead>
    <tbody>
      <tr><td>Simple, via un prestataire</td><td>Devis, bon de commande, petit contrat de prestation</td></tr>
      <tr><td>Avancée</td><td>Contrat à enjeu, client que tu connais peu, risque de contestation</td></tr>
      <tr><td>Qualifiée</td><td>Très gros enjeu, ou quand un texte l'exige</td></tr>
    </tbody>
  </table></div>
  <p class="note">Pas besoin de DocuSign pour ça. Exemple français : Youtrust (l'ex-Yousign) a une formule gratuite limitée à 2 invitations à signer par mois. Sa première formule payante, One, coûte 9 € HT par mois en paiement annuel, pour 10 invitations à signer par mois en signature simple. La signature avancée est une option des formules Plus et Pro, en engagement annuel. Prix relevés sur leur page officielle.</p>
</section>

<section>
  <div class="regle">
    <h2>Tes 3 vérifications</h2>
    <ol class="etapes">
      <li><b>Ton modèle est relu par un pro</b> avant que Claude ne le réutilise.</li>
      <li><b>Pour une signature qualifiée</b>, le prestataire doit figurer sur la liste de confiance publiée par l'ANSSI. Vérifie-le avant de signer.</li>
      <li><b>Tu gardes le dossier de preuves</b> avec chaque contrat signé.</li>
    </ol>
  </div>
  <p class="note">Ceci n'est pas un conseil juridique. Le bon niveau dépend de ton contrat et de ton secteur, et certains actes obéissent à des règles propres (un acte notarié, par exemple). Pour un cas précis, demande à ton avocat.</p>
</section>
""",
)

# ─────────────────────────────── 29 · LES OUTILS JURIDIQUES D'ANTHROPIC
PAGES["outils-juridiques"] = dict(
    video="29 · Les outils juridiques d'Anthropic",
    title="Les outils juridiques gratuits d'Anthropic : le lien officiel et ce qu'il faut adapter pour la France",
    desc="claude-for-legal : les plugins juridiques open source d'Anthropic, où les trouver, comment les installer, et les quatre points à adapter pour travailler en droit français.",
    og_pill="Les bases de l'IA · 29", og_titre="Les outils juridiques d'Anthropic, adaptés à la France",
    marque="Les bases de l'IA · 29",
    h1="Les outils juridiques, <em>adaptés à la France</em>",
    chapo="Anthropic publie gratuitement des outils pour le travail juridique : relecture de contrats, tri des accords de confidentialité, RGPD. Un vrai cadeau, à condition de le régler pour ton droit et ta pratique.",
    verifie="16/10/2026",
    sources=[SRC_CLAUDE_LEGAL],
    corps="""
<section>
  <h2>Ce que c'est</h2>
  <div class="encadre"><b>Le lien officiel</b><a href="https://github.com/anthropics/claude-for-legal">github.com/anthropics/claude-for-legal</a>. C'est le dépôt d'Anthropic lui-même. N'en installe pas une copie trouvée ailleurs.</div>
  <div class="encadre"><b>Ce qu'il contient</b>Des plugins par domaine. Par exemple commercial-legal (revue de contrats fournisseurs, d'accords de confidentialité, de contrats SaaS) et privacy-legal (revue d'un accord de traitement des données, réponse à une demande d'accès RGPD).</div>
  <div class="encadre"><b>La licence</b>Le code est publié sous licence libre Apache 2.0. Attention : certains connecteurs de recherche juridique qu'il propose demandent leur propre abonnement.</div>
</section>

<section>
  <h2><span class="num">1</span>L'installer</h2>
  <ul class="liste">
    <li><b>Dans Cowork</b> (l'application Claude) : Customize, puis Browse plugins, et tu choisis ceux qui correspondent à ta pratique.</li>
    <li><b>Dans Claude Code</b> : tu ajoutes le dépôt comme catalogue, puis tu installes le plugin voulu, et tu redémarres.</li>
  </ul>
  <pre><code>/plugin marketplace add https://github.com/anthropics/claude-for-legal
/plugin install commercial-legal@claude-for-legal</code></pre>
  <p>Ensuite, une étape que presque tout le monde saute, et c'est la plus importante : l'entretien de départ.</p>
  <pre><code>/commercial-legal:cold-start-interview</code></pre>
  <p>10 à 20 minutes. Il t'interroge sur ta pratique, lit tes documents de référence, et écrit ton profil. Toutes les autres fonctions s'appuient dessus.</p>
</section>

<section>
  <h2><span class="num">2</span>Ce qu'il faut adapter pour la France</h2>
  <ol class="etapes">
    <li><b>Ton droit et tes règles.</b> Le contenu est très orienté États-Unis (droit du travail américain, recherches dans des bases juridiques américaines). C'est l'entretien de départ qui fixe ton droit applicable, tes clauses types et ce qui doit remonter à un humain.</li>
    <li><b>Tes vrais documents.</b> Donne-lui des contrats déjà signés et ta grille de négociation. Plus il en a, plus ses remarques collent à ta pratique.</li>
    <li><b>Les références juridiques.</b> Sans outil de recherche connecté, les citations sont marquées « à vérifier ». Tu les contrôles toi-même sur Légifrance.</li>
    <li><b>Le secret professionnel.</b> Avant d'y mettre un vrai dossier, vérifie ta formule et tes réglages. Le comparatif : <a href="/forfaits-equipe">Team et Enterprise, RGPD inclus</a>.</li>
  </ol>
  <p>Ce que tu peux répondre pendant l'entretien de départ :</p>
  <pre><code>Je travaille en droit français, pour [type de clients].
Les contrats que je relis le plus : [types].
Mes positions sur les clauses sensibles : responsabilité,
résiliation, confidentialité, juridiction compétente : [tes règles].
Ce qui doit toujours remonter à moi : [cas].
Réponds en français. Ne cite un article de loi
que si tu peux donner sa source exacte.</code></pre>
</section>

<section>
  <div class="regle">
    <h2>La règle qui ne bouge pas</h2>
    <ol class="etapes">
      <li><b>C'est un brouillon, pas un avis.</b> Anthropic l'écrit dans le dépôt : chaque résultat est un brouillon à relire par un juriste.</li>
      <li><b>Le responsable, c'est le professionnel</b> qui l'utilise. Pas l'outil, et pas Anthropic.</li>
      <li><b>Rien ne part chez le client</b> sans ta relecture.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 30 · LA MÉTHODE PRECISE
PAGES["precise"] = dict(
    video="30 · La méthode PRECISE",
    title="La trame PRECISE prête à copier : ma structure de prompt",
    desc="PRECISE : Persona, Rôle, Explicite, Contexte, Instructions, Steps, Exemples. La trame à copier, un exemple rempli, et comment t'en servir au quotidien.",
    og_pill="Les bases de l'IA · 30", og_titre="La trame PRECISE prête à copier",
    marque="Les bases de l'IA · 30",
    h1="La trame <em>PRECISE</em>",
    chapo="Un bon résultat ne dépend pas de la chance, il dépend de ce que tu mets dans ta demande. Voici la structure que j'utilise pour chacun de mes prompts sérieux. Sept lettres, sept questions à se poser.",
    verifie="16/10/2026",
    sources=[SRC_PROMPTING],
    corps="""
<section>
  <h2>Les 7 lettres</h2>
  <ul class="liste">
    <li><b>P, Persona :</b> qui il est. « Tu es un expert-comptable. »</li>
    <li><b>R, Rôle :</b> le livrable attendu. « Ta mission : analyser ce bilan. »</li>
    <li><b>E, Explicite :</b> la tâche, sans sous-entendu.</li>
    <li><b>C, Contexte :</b> les infos de fond. Ton activité, tes contraintes, ton historique.</li>
    <li><b>I, Instructions :</b> longueur, ton, format, ce qu'il faut éviter.</li>
    <li><b>S, Steps :</b> les étapes, pour les tâches complexes.</li>
    <li><b>E, Exemples :</b> à quoi ressemble le bon résultat.</li>
  </ul>
</section>

<section>
  <h2><span class="num">1</span>La trame, à copier et remplir</h2>
  <pre><code>[P] PERSONA
Tu es [un métier, une expertise précise].

[R] RÔLE
Ta mission : [ce que tu dois produire, en une phrase].

[E] EXPLICITE
[Dis exactement ce que tu attends. Rien d'implicite.]

[C] CONTEXTE
[Mon activité, ma situation, l'historique, les contraintes.]

[I] INSTRUCTIONS
Longueur : [...]. Ton : [...]. Format : [...]. À éviter : [...].

[S] STEPS
1. [...]
2. [...]
3. [...]

[E] EXEMPLES
[Colle un ou deux exemples du résultat que tu veux.]</code></pre>
</section>

<section>
  <h2><span class="num">2</span>Un exemple rempli</h2>
  <pre><code>[P] Tu es un expert-comptable rigoureux, habitué aux TPE.
[R] Ta mission : auditer le bilan joint et lister les points d'alerte.
[E] Repère les postes anormaux, explique pourquoi,
et propose une action concrète pour chacun.
[C] Je suis gérant d'une SARL de 4 personnes, activité de services.
Trésorerie tendue depuis 6 mois.
[I] 10 points maximum. Ton direct, sans jargon.
Format : un tableau (poste, alerte, action).
[S] 1. Repère les écarts. 2. Classe-les du plus urgent
au moins urgent. 3. Chiffre l'impact quand c'est possible.
[E] Un point attendu ressemble à ça : « Créances clients en forte
hausse, risque d'impayés, relancer sous 8 jours. »</code></pre>
</section>

<section>
  <h2><span class="num">3</span>Le levier le plus puissant : les exemples</h2>
  <p>Si tu ne remplis qu'une lettre à fond, prends le dernier E. Anthropic le dit dans sa documentation : les exemples sont l'un des moyens les plus fiables d'orienter le format, le ton et la structure de la réponse. Elle conseille d'en donner 3 à 5 pour les meilleurs résultats.</p>
  <ul class="liste">
    <li><b>Des exemples variés</b>, pour qu'il ne recopie pas bêtement le premier.</li>
    <li><b>Tes vrais documents</b> : un mail que tu as aimé, un compte rendu réussi.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>Comment t'en servir</h2>
    <ol class="etapes">
      <li><b>Pas besoin des 7 lettres pour une petite question.</b> PRECISE, c'est pour les tâches qui comptent ou qui reviennent.</li>
      <li><b>Garde tes prompts réussis</b> dans un fichier. Tu ne les réécris plus.</li>
      <li><b>Ne la remplis pas à la main</b> : fais-la remplir par Claude. La marche à suivre : <a href="/meta-prompt">le méta-prompt</a>.</li>
    </ol>
  </div>
  <p class="note">PRECISE est ma méthode de travail, pas une norme officielle. Elle reprend les principes qu'Anthropic recommande : être clair, donner du contexte, montrer des exemples.</p>
</section>
""",
)

# ─────────────────────────────── 31 · LE MÉTA-PROMPT
PAGES["meta-prompt"] = dict(
    video="31 · Le méta-prompt",
    title="Le méta-prompt : fais écrire tes prompts par Claude",
    desc="La trame à coller dans Claude et la marche à suivre en 5 étapes pour qu'il rédige lui-même un prompt complet à partir de ton histoire.",
    og_pill="Les bases de l'IA · 31", og_titre="Le méta-prompt : la trame et la marche à suivre",
    marque="Les bases de l'IA · 31",
    h1="Le méta-prompt, <em>la marche à suivre</em>",
    chapo="Le secret des bons prompts : tu ne les écris pas toi-même. Tu racontes ton besoin à Claude, avec tes mots, et tu lui demandes de remplir la trame à ta place. Voici exactement comment je fais.",
    verifie="16/10/2026",
    sources=[SRC_PROMPTING],
    corps="""
<section>
  <h2>Pourquoi ça marche</h2>
  <div class="encadre"><b>Tu racontes, il structure</b>Tu sais très bien ce que tu veux. Ce qui coince, c'est de l'écrire proprement. Claude, lui, sait ranger une histoire en vrac dans une structure claire.</div>
  <div class="encadre"><b>Le test d'Anthropic</b>Sa règle d'or : montre ton prompt à un collègue qui ne connaît rien au sujet. S'il serait perdu, Claude le sera aussi. Le méta-prompt sert à passer ce test.</div>
</section>

<section>
  <h2><span class="num">1</span>Le méta-prompt, à copier</h2>
  <pre><code>Je vais te raconter une tâche que je veux confier à une IA.
À partir de mon récit, rédige un prompt complet
en suivant cette trame PRECISE :

[P] Persona : qui l'IA doit être
[R] Rôle : le livrable attendu
[E] Explicite : la tâche, sans sous-entendu
[C] Contexte : les infos de fond
[I] Instructions : longueur, ton, format, à éviter
[S] Steps : les étapes
[E] Exemples : à quoi ressemble le bon résultat

S'il te manque une information pour remplir une lettre,
pose-moi la question au lieu de l'inventer.

Voici mon histoire :
[raconte en vrac : ton sujet, pour qui, pourquoi,
tes règles, un exemple de ce que tu aimes]</code></pre>
</section>

<section>
  <h2><span class="num">2</span>La marche à suivre</h2>
  <ol class="etapes">
    <li><b>Colle le méta-prompt</b> dans une conversation Claude.</li>
    <li><b>Raconte ton histoire</b> à la suite, sans te soucier de l'ordre. Tu peux même la dicter.</li>
    <li><b>Réponds à ses questions.</b> S'il en pose, c'est qu'il manquait une info.</li>
    <li><b>Relis le prompt qu'il te propose.</b> Un truc cloche ? Dis-le-lui : « Le ton est trop formel », « Ajoute que c'est pour un client pressé ». Il corrige.</li>
    <li><b>Quand il est parfait, copie-le dans une conversation neuve.</b> La conversation de rédaction est encombrée de brouillons. La neuve part propre.</li>
  </ol>
</section>

<section>
  <h2><span class="num">3</span>Où ranger ton prompt fini</h2>
  <ul class="liste">
    <li><b>Une tâche qui revient ?</b> Colle-le dans les instructions d'un Projet Claude. Il s'applique à chaque conversation du projet.</li>
    <li><b>Dans Claude Code ?</b> Mets-le dans ton fichier CLAUDE.md : <a href="/claude-md">ta trame CLAUDE.md</a>.</li>
    <li><b>Sinon</b>, garde-le dans un fichier « mes prompts ». Tu le ressors en dix secondes.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>Les 3 réflexes</h2>
    <ol class="etapes">
      <li><b>Donne-lui de vrais exemples.</b> C'est ce qui change le plus le résultat.</li>
      <li><b>Teste le prompt sur un cas réel</b> avant de l'utiliser pour de bon.</li>
      <li><b>Améliore-le au fil de l'eau.</b> Chaque réponse ratée t'apprend une règle à ajouter.</li>
    </ol>
  </div>
  <p class="note">La trame seule, avec un exemple rempli : <a href="/precise">la méthode PRECISE</a>.</p>
</section>
""",
)

# ─────────────────────────────── 32 · FORFAITS ÉQUIPE : TEAM ET ENTERPRISE
PAGES["forfaits-equipe"] = dict(
    video="32 · Forfaits équipe : Team et Enterprise",
    title="Claude Team ou Enterprise : le comparatif complet, RGPD inclus",
    desc="Prix, nombre de personnes, fonctions, données et RGPD : le comparatif des formules Claude Team et Enterprise, et comment choisir pour un cabinet ou une PME.",
    og_pill="Les bases de l'IA · 32", og_titre="Team ou Enterprise : le comparatif, RGPD inclus",
    marque="Les bases de l'IA · 32",
    h1="Team ou Enterprise, <em>RGPD inclus</em>",
    chapo="Dès que tu travailles à plusieurs, ou avec des données de clients, la question n'est plus seulement le prix. C'est aussi qui voit quoi, ce que deviennent tes données, et où elles sont stockées. Voici le comparatif.",
    verifie="16/10/2026",
    sources=[SRC_FORFAITS_FR, SRC_PRIVACY_TRAINING, SRC_PRIVACY_ROLES, SRC_PRIVACY_DPA, SRC_PRIVACY_SERVEURS, SRC_RESIDENCE, SRC_BEDROCK],
    corps="""
<section>
  <h2>Les deux formules</h2>
  <div class="cartes">
    <div class="carte"><div class="nom">Team · <b>travailler à plusieurs</b></div><p>De 2 à 150 personnes. Claude Code et Cowork, une facture unique, l'administration centralisée, la connexion unique (SSO), le partage de projets. Ton contenu ne sert pas à entraîner les modèles, par défaut.</p><div class="prix">Siège Standard : 18 € par mois à l'année, 21,04 € au mois. Siège Premium (5 fois plus d'usage) : 90 € à l'année, 105,23 € au mois.</div></div>
    <div class="carte"><div class="nom">Enterprise · <b>conformité critique</b></div><p>Tout Team, plus : accès par rôle, gestion des identités (SCIM), journaux d'audit, API de conformité, durée de conservation des données sur mesure, filtrage par adresse IP.</p><div class="prix">20 $ par siège et par mois, facturé à l'année, 20 sièges minimum, plus la consommation au tarif API</div></div>
  </div>
  <p class="note">Prix hors taxes, relevés sur la page officielle depuis la France. Les sièges Standard et Premium se mélangent dans une même équipe.</p>
</section>

<section>
  <h2>Ce qui change vraiment</h2>
  <div class="tab"><table>
    <thead><tr><th></th><th>Pro ou Max</th><th>Team</th><th>Enterprise</th></tr></thead>
    <tbody>
      <tr><td>Entraînement sur tes données</td><td>Désactivable</td><td>Non, par défaut</td><td>Non, par défaut</td></tr>
      <tr><td>Partage de projets</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
      <tr><td>Connexion unique (SSO)</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
      <tr><td>Journaux d'audit</td><td>Non</td><td>Non</td><td>Oui</td></tr>
      <tr><td>Conservation sur mesure</td><td>Non</td><td>Non</td><td>Oui</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Le volet RGPD</h2>
  <div class="encadre"><b>Qui est responsable de quoi</b>En Team et Enterprise, ton entreprise est responsable du traitement. Anthropic agit comme sous-traitant, et traite les données uniquement selon tes instructions.</div>
  <div class="encadre"><b>Le contrat</b>L'accord de traitement des données (DPA), avec les clauses contractuelles types pour les transferts hors d'Europe, est intégré automatiquement aux conditions commerciales d'Anthropic. Tu l'acceptes en même temps qu'elles.</div>
  <div class="encadre"><b>Le point que tout avocat va soulever</b>Pour ses offres professionnelles, Anthropic l'écrit : les données sont stockées aux États-Unis. Il n'y a pas, aujourd'hui, de case « Europe » à cocher dans Team.</div>
  <div class="encadre"><b>La solution si tu dois rester en Europe</b>Passer par Claude dans Amazon Bedrock, avec un point d'accès européen (EU) qui garde les requêtes dans des régions d'Europe : Paris, Francfort, Irlande et d'autres. Ce point d'accès régional coûte 10 % de plus que le point d'accès mondial. C'est un projet technique, à monter avec un prestataire, pas un simple abonnement.</div>
</section>

<section>
  <div class="regle">
    <h2>Comment choisir</h2>
    <ol class="etapes">
      <li><b>Seul ?</b> Reste sur Pro ou Max : <a href="/forfaits">le comparatif</a>.</li>
      <li><b>Un cabinet ou une PME qui partage des dossiers ?</b> Team, en commençant par des sièges Standard.</li>
      <li><b>Audit, traçabilité, conservation imposée par ton secteur ?</b> Enterprise.</li>
      <li><b>Données qui doivent rester en Europe ?</b> Un montage sur Bedrock en région européenne.</li>
    </ol>
  </div>
  <p class="note">Ceci n'est pas un avis juridique. Tes obligations dépendent de ton métier et de tes clients : fais valider le choix par ton DPO ou ton avocat.</p>
</section>
""",
)

# ─────────────────────────────── 34 · SUPPRIMER LA CONVERSATION NE SUFFIT PAS
PAGES["effacer-memoire"] = dict(
    video="34 · Supprimer la conversation ne suffit pas",
    title="Effacer la mémoire de ChatGPT et de Claude : où cliquer, pas à pas",
    desc="Supprimer une conversation n'efface pas ce que l'IA en a retenu. Les chemins exacts pour voir et effacer la mémoire dans ChatGPT et dans Claude, d'après leur aide officielle.",
    og_pill="Les bases de l'IA · 34", og_titre="Effacer la mémoire de ton IA, pas à pas",
    marque="Les bases de l'IA · 34",
    h1="Effacer la mémoire, <em>pas à pas</em>",
    chapo="Tu as collé le dossier d'un client, puis supprimé la conversation. Ce que l'IA en a retenu peut être resté dans sa mémoire. Les deux aides officielles le disent. Voici où regarder, et quoi effacer.",
    verifie="16/10/2026",
    sources=[SRC_OPENAI_MEMOIRE, SRC_CLAUDE_MEMOIRE, SRC_CLAUDE_MEMOIRE_FR, SRC_CLAUDE_INCOGNITO],
    corps="""
<section>
  <h2>Le principe</h2>
  <div class="encadre"><b>La conversation et la mémoire sont deux choses</b>La mémoire est rangée à part. Chez ChatGPT comme chez Claude, supprimer une conversation ne supprime pas forcément ce qui en a été retenu. Il faut effacer les deux.</div>
</section>

<section>
  <h2><span class="num">1</span>Dans ChatGPT</h2>
  <ol class="etapes">
    <li><b>Ouvre les Paramètres, puis Personnalisation, puis Mémoire.</b></li>
    <li><b>Regarde ce qu'il a gardé</b> : le résumé de la mémoire et les souvenirs enregistrés. Tu peux aussi lui demander « Qu'est-ce que tu sais de moi ? ».</li>
    <li><b>Supprime l'élément concerné.</b> Pour tout effacer d'un coup, l'option « Supprimer et désactiver la mémoire » est dans le menu à trois points.</li>
    <li><b>Supprime aussi la conversation d'origine</b>, et les fichiers concernés dans la Bibliothèque. OpenAI recommande de supprimer le souvenir ET la conversation.</li>
    <li><b>Option radicale</b> : désactive « Faire référence à l'historique des conversations ». Ce qu'il a retenu de tes anciennes conversations est alors programmé pour suppression sous 30 jours.</li>
  </ol>
  <p class="note">OpenAI précise que la suppression peut prendre un peu de temps, et qu'il peut garder une trace des souvenirs supprimés jusqu'à 30 jours, pour la sécurité. Les intitulés peuvent varier selon ton compte.</p>
</section>

<section>
  <h2><span class="num">2</span>Dans Claude</h2>
  <ol class="etapes">
    <li><b>Ouvre les Paramètres, puis Mémoire.</b></li>
    <li><b>Tout ce qu'il retient est rangé par sujets.</b> Ouvre un sujet pour le lire.</li>
    <li><b>Corrige-le</b> avec l'icône de modification, ou <b>supprime-le</b>.</li>
    <li><b>Chaque Projet a sa propre mémoire.</b> Fais la même vérification dans tes projets.</li>
    <li><b>Pour tout effacer</b> : désactive « Générer une mémoire à partir des chats », puis choisis « Réinitialiser la mémoire ». Attention, c'est définitif, projets compris.</li>
  </ol>
</section>

<section>
  <h2><span class="num">3</span>La prochaine fois, zéro trace</h2>
  <ul class="liste">
    <li><b>Claude : le chat incognito.</b> L'icône fantôme en haut à droite d'une nouvelle conversation. Rien n'est enregistré dans ton historique ni dans sa mémoire. La conversation est quand même conservée 30 jours côté Anthropic, et le mode n'existe pas dans les Projets.</li>
    <li><b>Dans un Projet Claude</b> : coupe « Mémoire » dans le menu « + » avant ton premier message.</li>
    <li><b>ChatGPT : le chat temporaire.</b> Il ne crée ni ne met à jour aucun souvenir.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>Ta routine</h2>
    <ol class="etapes">
      <li><b>Une fois par trimestre</b>, ouvre la mémoire de chaque IA que tu utilises, et fais le ménage.</li>
      <li><b>Dossier client sensible ?</b> Incognito ou temporaire, dès le départ.</li>
      <li><b>En équipe</b>, sur Claude Team et Enterprise, la mémoire reste coupée pour chaque membre tant qu'il ne l'active pas.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 35 · POURQUOI TON SKILL NE SE LANCE JAMAIS
PAGES["description-skill"] = dict(
    video="35 · Pourquoi ton skill ne se lance jamais",
    title="Écrire la description d'un skill pour que Claude s'en serve vraiment",
    desc="Claude choisit un skill en lisant sa description. La méthode pour l'écrire, la formule à copier, des exemples avant et après, et quoi faire quand il ne se déclenche toujours pas.",
    og_pill="Les bases de l'IA · 35", og_titre="La description qui fait vraiment lancer ton skill",
    marque="Les bases de l'IA · 35",
    h1="La description qui <em>fait lancer ton skill</em>",
    chapo="Ton skill peut être parfait : si sa description est floue, Claude ne l'ouvre jamais. Tout se joue en deux lignes, tout en haut du fichier. Voici ma méthode pour les écrire.",
    verifie="16/10/2026",
    sources=[SRC_SKILLS_CODE, SRC_SKILLS_AIDE],
    corps="""
<section>
  <h2>Comment Claude choisit</h2>
  <div class="encadre"><b>Il ne lit que la description</b>Les descriptions de tous tes skills sont chargées en permanence. Le reste du fichier SKILL.md n'est lu qu'une fois le skill choisi. Tant que la description ne correspond pas à ta demande, ton beau travail dort.</div>
  <div class="encadre"><b>Les limites de longueur</b>Sur claude.ai, le nom fait 64 caractères maximum et la description 200. Dans Claude Code, la description est coupée au-delà de 1 536 caractères : mets l'essentiel au début.</div>
</section>

<section>
  <h2><span class="num">1</span>La formule</h2>
  <p>Une bonne description dit deux choses : ce que fait le skill, et quand l'utiliser. Avec les mots que tu emploies vraiment.</p>
  <pre><code>[Verbe d'action] [ce qu'il produit] à partir de [ce que tu lui donnes].
À utiliser quand je parle de [mot 1], de [mot 2] ou de [mot 3].</code></pre>
  <p>Dans le fichier, ça donne :</p>
  <pre><code>---
name: redaction-devis
description: Rédige un devis à partir de mes notes d'appel. À utiliser quand je parle de devis, de chiffrage ou de proposition.
---</code></pre>
</section>

<section>
  <h2><span class="num">2</span>Avant, après</h2>
  <div class="avant-apres">
    <div class="av"><small>Ne se lance jamais</small>« Aide pour les devis. »</div>
    <div class="ap"><small>Se lance au bon moment</small>« Rédige un devis à partir de mes notes d'appel. À utiliser quand je parle de devis, de chiffrage ou de proposition. »</div>
  </div>
  <div class="avant-apres" style="margin-top:10px">
    <div class="av"><small>Trop vague</small>« Comptes rendus. »</div>
    <div class="ap"><small>Précis</small>« Transforme mes notes de chantier en compte rendu client d'une page. À utiliser quand je parle de compte rendu, de CR ou de point chantier. »</div>
  </div>
</section>

<section>
  <h2><span class="num">3</span>Le test des 5 phrases</h2>
  <ol class="etapes">
    <li><b>Écris 5 demandes</b> comme tu les formules vraiment, un mardi pressé : « fais-moi le chiffrage pour Dupont ».</li>
    <li><b>Lance-les une par une</b>, dans une conversation neuve.</li>
    <li><b>Le skill ne s'ouvre pas ?</b> Ajoute dans la description le mot que tu as employé.</li>
    <li><b>Il s'ouvre quand il ne devrait pas ?</b> Rends la description plus précise.</li>
  </ol>
</section>

<section>
  <div class="regle">
    <h2>Toujours rien ? Les vérifications officielles</h2>
    <ol class="etapes">
      <li><b>Demande à Claude</b> « Quels skills sont disponibles ? » pour voir s'il le connaît.</li>
      <li><b>Appelle-le directement</b> avec /nom-du-skill dans Claude Code.</li>
      <li><b>Vérifie l'en-tête</b> : les trois tirets doivent être sur la toute première ligne. Si l'en-tête est mal formé, Claude ne peut pas lire la description.</li>
    </ol>
  </div>
  <p class="note">Avant d'installer le skill de quelqu'un d'autre, vérifie qui l'a écrit et ce qu'il fait : <a href="/reperer-arnaque">repérer l'arnaque en dix secondes</a>.</p>
</section>
""",
)

# ─────────────────────────────── 36 · LE RAPPORT D'ANTHROPIC SUR L'EMPLOI
PAGES["rapport-emploi"] = dict(
    video="36 · Le rapport d'Anthropic sur l'emploi",
    title="Le rapport d'Anthropic sur l'avenir du travail, en une page",
    desc="Scenarios for our Economic Future : les trois scénarios d'Anthropic pour l'économie américaine d'ici 2030, la part des revenus du travail, les métiers touchés, et quoi en faire dès maintenant.",
    og_pill="Les bases de l'IA · 36", og_titre="Le rapport d'Anthropic sur l'emploi, en une page",
    marque="Les bases de l'IA · 36",
    h1="Le rapport sur l'emploi, <em>en une page</em>",
    chapo="En septembre 2026, Anthropic a publié trois scénarios pour l'économie américaine d'ici 2030. Ce n'est pas une prédiction, c'est un éventail. Voici ce qu'il dit, chiffres à l'appui, et ce que tu peux en faire.",
    verifie="16/10/2026",
    sources=[SRC_ECON],
    corps="""
<section>
  <h2>Les trois scénarios</h2>
  <div class="tab"><table>
    <thead><tr><th>Scénario</th><th>L'idée</th><th>PIB américain en 2030</th></tr></thead>
    <tbody>
      <tr><td>Modeste</td><td>Un effet comparable à celui d'internet, progressif</td><td class="n">34,1 billions de $ (+1,6 %)</td></tr>
      <tr><td>Substantiel</td><td>L'IA est capable de faire la moitié du travail intellectuel d'ici 2030</td><td class="n">36,3 billions de $ (+8,3 %)</td></tr>
      <tr><td>Extrême</td><td>L'IA dépasse l'humain sur la plupart des tâches intellectuelles</td><td class="n">44,4 billions de $ (+32,4 %)</td></tr>
    </tbody>
  </table></div>
  <p class="note">PIB en prix de 2025. Les pourcentages comparent chaque scénario à une trajectoire sans ce choc de l'IA.</p>
</section>

<section>
  <h2>Ce qu'il faut retenir</h2>
  <div class="encadre"><b>L'économie grossit dans les trois cas</b>Mais la part qui revient au travail baisse. Aujourd'hui, environ 60 centimes de chaque dollar vont aux travailleurs. En 2030 : 59,4 % dans le scénario modeste, 56,1 % dans le substantiel, 45,2 % dans l'extrême.</div>
  <div class="encadre"><b>Le travail intellectuel est en première ligne</b>Les salaires des métiers du savoir stagnent dans le scénario substantiel, et baissent de plus de 10 % d'ici 2030 dans l'extrême. Les exemples cités : les développeurs, les téléconseillers des centres d'appels.</div>
  <div class="encadre"><b>Ailleurs, les salaires montent</b>Hors travail intellectuel, la demande augmente. L'exemple du rapport : le bâtiment, porté par des projets conçus et autorisés plus vite.</div>
</section>

<section>
  <h2><span class="num">1</span>Classe tes tâches en quatre</h2>
  <p>Pour lire ce qui change dans un métier, le rapport range chaque tâche dans une des quatre cases : inchangée, augmentée par l'IA, automatisée, ou nouvelle. Fais l'exercice sur ta propre semaine :</p>
  <pre><code>Voici les tâches de ma semaine type : [liste].
Classe chacune dans une de ces 4 cases :
inchangée, augmentée par l'IA, automatisable, nouvelle.
Pour chaque tâche augmentée ou automatisable,
dis-moi comment commencer, avec un outil que j'ai déjà.
Présente le tout dans un tableau.</code></pre>
</section>

<section>
  <div class="regle">
    <h2>Pas de panique, un plan</h2>
    <ol class="etapes">
      <li><b>Le rapport parle des États-Unis.</b> La France n'est pas modélisée, mais le travail de bureau y ressemble beaucoup.</li>
      <li><b>Rien n'est écrit.</b> La dernière partie du rapport s'intitule « The future is not predetermined » : l'avenir n'est pas joué d'avance.</li>
      <li><b>Commence maintenant</b>, par une tâche répétitive de ta semaine, plutôt que dans deux ans.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 37 · « 10 000 LEADS EN UNE NUIT »
PAGES["prospection"] = dict(
    video="37 · « 10 000 leads en une nuit »",
    title="Ma méthode de prospection avec l'IA : ciblée, et dans les règles du RGPD",
    desc="Pourquoi « 10 000 leads en une nuit » ne fait pas de clients, la méthode ciblée qui marche, et les règles de la CNIL pour prospecter des professionnels.",
    og_pill="Les bases de l'IA · 37", og_titre="Ma méthode de prospection, celle qui marche",
    marque="Les bases de l'IA · 37",
    h1="La prospection <em>qui marche</em>",
    chapo="Récupérer des milliers de contacts en une nuit, c'est possible. En faire des clients, non. Je l'ai fait à grande échelle : une poignée de vraies adresses sur des centaines. Voici ce que je fais à la place.",
    verifie="16/10/2026",
    sources=[SRC_CNIL_PROSPECTION, SRC_CNIL_KASPR, SRC_ANNUAIRE],
    corps="""
<section>
  <h2>Pourquoi le volume échoue</h2>
  <div class="encadre"><b>Des noms, pas des clients</b>Tu récupères des noms et des sites, et une montagne d'adresses invalides. Les petites entreprises locales ont souvent peu de présence en ligne propre.</div>
  <div class="encadre"><b>Et le droit</b>Aspirer des données personnelles pour démarcher, ça se fait dans le cadre du RGPD. La CNIL a sanctionné la société KASPR de 240 000 euros en décembre 2024, notamment pour avoir collecté sans base légale des coordonnées sur LinkedIn, y compris celles que leurs titulaires avaient choisi de ne pas montrer.</div>
</section>

<section>
  <h2><span class="num">1</span>La méthode, en 6 étapes</h2>
  <ol class="etapes">
    <li><b>Un métier, une zone.</b> Pas « les entreprises » : les agences immobilières de ton département, par exemple.</li>
    <li><b>Une liste propre, depuis une source officielle.</b> L'<a href="https://annuaire-entreprises.data.gouv.fr/">Annuaire des Entreprises</a> de l'État donne les informations légales de chaque entreprise, gratuitement.</li>
    <li><b>Lis leur site.</b> Note ce qu'ils font vraiment, pas ce que dit leur code d'activité.</li>
    <li><b>Le téléphone d'abord.</b> Un appel court, poli, qui dit qui tu es et pourquoi tu appelles.</li>
    <li><b>Le mail ensuite</b>, court et personnalisé, avec leurs vraies tâches.</li>
    <li><b>Un « non » est définitif.</b> Tu retires la personne de ta liste et tu ne la recontactes plus.</li>
  </ol>
</section>

<section>
  <h2><span class="num">2</span>Ce que fait l'IA, ce que tu fais</h2>
  <p>Claude ne démarche personne à ta place. Il prépare, tu envoies.</p>
  <pre><code>Voici ce que fait cette entreprise, d'après son site : [notes].
Rédige un mail de 6 lignes maximum pour leur proposer [ton offre].
Cite une de leurs tâches réelles, sans rien inventer.
Ton simple, pas de formule commerciale.
Termine par une question, et ajoute une ligne
pour qu'ils puissent refuser d'autres messages.</code></pre>
  <p class="note">Relis chaque mail avant l'envoi. Une erreur sur le nom ou l'activité d'un prospect coûte plus cher qu'un mail de moins.</p>
</section>

<section>
  <div class="regle">
    <h2>Les règles de la CNIL pour prospecter des pros</h2>
    <ol class="etapes">
      <li><b>Pas besoin d'accord préalable</b> pour écrire à un professionnel, si ton message est en rapport avec son métier.</li>
      <li><b>Il doit avoir été informé</b> que son adresse peut servir à de la prospection, et pouvoir s'y opposer simplement.</li>
      <li><b>Chaque message dit qui l'envoie</b> et donne un moyen simple de ne plus en recevoir.</li>
    </ol>
  </div>
  <p class="note">Les adresses génériques (contact@, info@) ne sont pas concernées par ces règles, selon la CNIL, car elles visent l'entreprise et non une personne. Pour un cas précis, lis la page de la CNIL ou demande à un juriste.</p>
</section>
""",
)

# ─────────────────────────────── 38 · LE CRM GRATUIT
PAGES["twenty"] = dict(
    video="38 · Le CRM gratuit",
    title="Twenty, le CRM open source : le lien officiel et comment te lancer",
    desc="Twenty, l'alternative open source à Salesforce et HubSpot : le lien officiel, les prix vérifiés, la licence, et deux façons de démarrer, en ligne ou chez toi.",
    og_pill="Les bases de l'IA · 38", og_titre="Twenty, le CRM open source : comment te lancer",
    marque="Les bases de l'IA · 38",
    h1="Twenty, <em>le CRM open source</em>",
    chapo="Avant de payer un CRM cher chaque mois, regarde Twenty. Il est open source : tu peux l'héberger toi-même, gratuitement, et tes données restent chez toi. Ou prendre leur version en ligne. Voici les deux chemins.",
    verifie="16/10/2026",
    sources=[SRC_TWENTY_PRIX, SRC_TWENTY_GITHUB, SRC_TWENTY_DOCKER],
    corps="""
<section>
  <h2>Les liens officiels</h2>
  <div class="encadre"><b>Le site</b><a href="https://twenty.com">twenty.com</a></div>
  <div class="encadre"><b>Le code</b><a href="https://github.com/twentyhq/twenty">github.com/twentyhq/twenty</a>, plus de 58 000 étoiles. Licence AGPL v3 pour l'essentiel, avec quelques fichiers sous licence commerciale et quelques briques sous licence MIT.</div>
  <div class="encadre"><b>Ce qu'il fait</b>Objets et champs sur mesure, vues en tableau, en colonnes (Kanban) ou en calendrier, automatisations, import et export CSV, API.</div>
</section>

<section>
  <h2>Les prix</h2>
  <div class="cartes">
    <div class="carte"><div class="nom">Hébergé chez toi · <b>Pro</b></div><p>Le logiciel est gratuit. Tu paies seulement le serveur, et tu t'occupes des mises à jour et des sauvegardes.</p><div class="prix">0 $</div></div>
    <div class="carte"><div class="nom">En ligne · <b>Pro</b></div><p>Ils hébergent pour toi. Essai gratuit sans carte bancaire.</p><div class="prix">9 $ par utilisateur et par mois à l'année, 11 $ au mois</div></div>
    <div class="carte"><div class="nom">En ligne · <b>Organization</b></div><p>Ajoute la connexion unique (SSO), les droits par ligne, un domaine personnalisé.</p><div class="prix">19 $ par utilisateur et par mois à l'année, 22 $ au mois</div></div>
  </div>
</section>

<section>
  <h2><span class="num">1</span>Le chemin simple : la version en ligne</h2>
  <ol class="etapes">
    <li><b>Crée ton compte</b> sur twenty.com, en essai gratuit.</li>
    <li><b>Importe tes contacts</b> depuis un fichier CSV (un export Excel suffit).</li>
    <li><b>Crée tes étapes de vente</b> : premier contact, rendez-vous, devis, signé.</li>
    <li><b>Teste une semaine en vrai</b> avant de payer.</li>
  </ol>
</section>

<section>
  <h2><span class="num">2</span>Le chemin gratuit : l'héberger toi-même</h2>
  <p>Il te faut un serveur avec au moins 2 Go de mémoire, et Docker installé. La documentation officielle donne une commande d'installation en une ligne :</p>
  <pre><code>bash &lt;(curl -sL https://raw.githubusercontent.com/twentyhq/twenty/main/packages/twenty-docker/scripts/install.sh)</code></pre>
  <p>Claude Code peut t'accompagner pas à pas sur ton serveur, mais c'est la partie technique : nom de domaine, sauvegardes, sécurité, mises à jour. Si ces mots te font peur, commence par la version en ligne.</p>
</section>

<section>
  <div class="regle">
    <h2>Avant de te lancer</h2>
    <ol class="etapes">
      <li><b>Installe uniquement depuis les liens officiels</b> ci-dessus.</li>
      <li><b>Hébergé chez toi, la sécurité est à ta charge</b>, sauvegardes comprises.</li>
      <li><b>Exporte tes données régulièrement</b>, quelle que soit la version.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 39 · LES FAUX CRÉATEURS D'OUTILS
PAGES["reperer-arnaque"] = dict(
    video="39 · Les faux créateurs d'outils",
    title="Repérer le faux créateur d'outil IA en dix secondes",
    desc="« J'ai créé l'outil qui divise ta facture par cinq » : comment vérifier en dix secondes si l'outil existe déjà en open source, gratuit, et le récupérer à la source.",
    og_pill="Les bases de l'IA · 39", og_titre="Repérer l'arnaque en dix secondes",
    marque="Les bases de l'IA · 39",
    h1="Repérer l'arnaque <em>en dix secondes</em>",
    chapo="« J'ai créé l'outil qui divise ta facture par cinq. » Souvent, l'outil existe déjà, gratuit, écrit par quelqu'un d'autre. On l'a juste emballé pour te vendre une formation. Voici comment le voir tout de suite.",
    verifie="16/10/2026",
    sources=[SRC_MIT],
    corps="""
<section>
  <h2>La technique</h2>
  <div class="encadre"><b>Le montage</b>Prendre un projet open source gratuit, le renommer ou l'emballer, le présenter comme une invention personnelle. Puis : « commente, je t'envoie le lien », et au bout, une formation payante.</div>
  <div class="encadre"><b>Ce qui est permis, et ce qui ne l'est pas</b>Réutiliser un projet open source, et même le vendre, c'est souvent autorisé : la licence MIT, par exemple, le permet, à condition de garder la mention de l'auteur d'origine. Ce qui est malhonnête, c'est de cacher l'original et de dire « j'ai créé ».</div>
</section>

<section>
  <h2><span class="num">1</span>Les drapeaux rouges</h2>
  <ul class="liste">
    <li><b>« Open source » et « j'ai créé » dans la même phrase.</b></li>
    <li><b>Pas de nom d'outil précis</b>, juste une promesse : « l'outil qui... ».</li>
    <li><b>Le lien seulement en message privé</b>, après un commentaire.</li>
    <li><b>Un compte qui « crée » un nouvel outil miracle chaque semaine.</b></li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Le test des dix secondes</h2>
  <ol class="etapes">
    <li><b>Demande le nom exact de l'outil.</b> Pas de nom, pas de confiance.</li>
    <li><b>Cherche-le sur GitHub</b> ou dans ton moteur de recherche, avec le mot « github ».</li>
    <li><b>Regarde le propriétaire du dépôt.</b> C'est lui, le créateur ? Ou quelqu'un d'autre, depuis des mois ?</li>
    <li><b>Regarde la licence et la date de création.</b> Un dépôt ancien, chez un autre auteur : tu as trouvé l'original.</li>
  </ol>
</section>

<section>
  <h2><span class="num">3</span>Fais vérifier par Claude</h2>
  <pre><code>Un créateur présente cet outil comme son invention : [description].
Existe-t-il déjà un projet open source qui fait ça ?
Donne-moi le nom, le lien GitHub, l'auteur et la licence.
Si tu n'es pas sûr, dis-le. N'invente aucun lien.</code></pre>
  <p class="note">Clique sur chaque lien qu'il te donne. Un lien qui ne s'ouvre pas ne prouve rien.</p>
</section>

<section>
  <div class="regle">
    <h2>Le bon réflexe</h2>
    <ol class="etapes">
      <li><b>Récupère l'outil à la source</b>, sur le dépôt officiel, jamais depuis un lien reçu en message privé.</li>
      <li><b>Vérifie avant d'installer</b> : qui l'a écrit, ce qu'il fait, ce qu'il peut toucher sur ta machine.</li>
      <li><b>Le vrai créateur d'un outil open source ne te le vend pas.</b> Il te le donne.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 40 · L'OUTIL DE DICTÉE
PAGES["dictee"] = dict(
    video="40 · L'outil qui a changé ma façon de travailler",
    title="Superwhisper : l'outil de dictée que j'utilise, et les deux réglages pour rester privé",
    desc="L'appli qui écrit ce que tu dis, partout, ponctuation comprise. Le nom de l'outil, les prix vérifiés, et les deux réglages à activer pour que ta voix reste sur ta machine.",
    og_pill="Les bases de l'IA · 40", og_titre="Mon outil de dictée et les deux réglages à activer",
    marque="Les bases de l'IA · 40",
    h1="L'outil de dictée, <em>et ses deux réglages</em>",
    chapo="Je parle bien plus vite que je n'écris. Alors je dicte à Claude, à mes mails, à WhatsApp. L'outil s'appelle Superwhisper. Bien réglé, ta voix ne quitte jamais ton ordinateur. Voici comment.",
    verifie="16/10/2026",
    sources=[SRC_SUPERWHISPER, SRC_SW_MODELES, SRC_SW_SENSIBLE, SRC_SW_HISTORIQUE],
    corps="""
<section>
  <h2>L'outil</h2>
  <div class="encadre"><b>Superwhisper</b>Sur Mac, Windows, iPhone et Android. Télécharge-le uniquement sur <a href="https://superwhisper.com">superwhisper.com</a>.</div>
  <div class="encadre"><b>Le geste</b>Tu cliques là où tu veux écrire. Un raccourci clavier (le site montre Option + Espace sur Mac), tu parles, et le texte apparaît, ponctué.</div>
  <div class="encadre"><b>Les prix</b>Gratuit pour toujours avec les modèles Whisper, qui tournent sur ta machine, sans limite. La version Pro coûte 8,49 $ par mois ou 84,99 $ par an. Moi, j'utilise le modèle Parakeet Multilanguage, qui demande la version Pro.</div>
</section>

<section>
  <h2><span class="num">1</span>Réglage 1 : un modèle local</h2>
  <p>Superwhisper propose des modèles « cloud », qui envoient ta voix sur internet, et des modèles « locaux », qui restent sur ta machine. Les réglages de départ conseillés par l'éditeur (S1-Voice et S1-Language) sont des modèles cloud.</p>
  <ol class="etapes">
    <li><b>Ouvre les Réglages, puis Modes</b>, et ouvre le mode que tu utilises.</li>
    <li><b>Dans « Voice Model », choisis un modèle marqué Local</b> : Whisper (gratuit), ou Parakeet et Cohere Transcribe (Pro).</li>
    <li><b>Pour la mise en forme</b>, utilise le mode « Voice to Text », qui n'envoie rien à une IA. Ou choisis un modèle de langage local (S1-mini).</li>
  </ol>
  <p class="note">Les modèles locaux se téléchargent une fois, puis marchent sans internet. Sur un ordinateur ancien, l'éditeur conseille plutôt les modèles cloud.</p>
</section>

<section>
  <h2><span class="num">2</span>Réglage 2 : la durée de conservation</h2>
  <p>Par défaut, Superwhisper garde chaque enregistrement sur ton disque, pour toujours : l'audio, la transcription et le résultat.</p>
  <ol class="etapes">
    <li><b>Ouvre les Réglages, puis Configuration.</b></li>
    <li><b>Dans « Keep recordings for »</b>, choisis 1 jour ou 1 semaine au lieu de « Forever ».</li>
    <li><b>Pour effacer tout de suite</b> : dans l'historique, sélectionne les enregistrements, clic droit, Delete.</li>
  </ol>
</section>

<section>
  <div class="regle">
    <h2>La nuance honnête</h2>
    <ol class="etapes">
      <li><b>La voix reste chez toi, le texte va où tu le dictes.</b> Dicté dans ChatGPT, il part chez OpenAI. Dicté dans Claude, chez Anthropic.</li>
      <li><b>Ton jargon</b> (noms de clients, sigles de ton métier) s'ajoute dans Vocabulary. Avec un modèle local, cette liste ne quitte pas ta machine non plus.</li>
      <li><b>Commence par le gratuit</b> avec un modèle Whisper. Passe en Pro seulement si tu dictes tous les jours.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 41 · LE RAPPORT DE STANFORD
PAGES["stanford"] = dict(
    video="41 · Le rapport de Stanford",
    title="AI Index 2026 de Stanford : les chiffres clés, vérifiés à la source",
    desc="Les chiffres clés de l'AI Index 2026 de Stanford HAI et de l'enquête McKinsey sur l'IA en entreprise, avec la source exacte de chaque chiffre.",
    og_pill="Les bases de l'IA · 41", og_titre="Le rapport de Stanford : les chiffres clés",
    marque="Les bases de l'IA · 41",
    h1="Le rapport de Stanford, <em>les chiffres clés</em>",
    chapo="Chaque printemps, l'institut d'IA de Stanford publie l'AI Index, le grand bilan annuel de l'intelligence artificielle. Voici les chiffres à retenir de l'édition 2026, et ceux de McKinsey qu'on lui attribue souvent par erreur.",
    verifie="16/10/2026",
    sources=[SRC_STANFORD, SRC_MCK_2025, SRC_MCK_2026],
    corps="""
<section>
  <h2>Stanford HAI, AI Index 2026</h2>
  <p class="note" style="margin-top:0">Enseignements publiés le 13 avril 2026.</p>
  <div class="cartes">
    <div class="carte"><div class="nom">La course · <b>2,7 %</b></div><p>Les États-Unis n'ont presque plus d'avance sur la Chine. En mars 2026, le meilleur modèle d'Anthropic ne menait que de 2,7 %.</p></div>
    <div class="carte"><div class="nom">La valeur · <b>172 milliards de dollars</b></div><p>La valeur des outils d'IA générative pour les consommateurs américains, par an, début 2026. Souvent avec des outils gratuits ou presque.</p></div>
    <div class="carte"><div class="nom">L'argent · <b>581,7 milliards de dollars</b></div><p>Les investissements des entreprises dans l'IA dans le monde en 2025.</p></div>
    <div class="carte"><div class="nom">L'emploi · <b>près de 20 %</b></div><p>La baisse de l'emploi des développeurs de 22 à 25 ans depuis 2024, alors que leurs aînés sont plus nombreux.</p></div>
  </div>
</section>

<section>
  <h2>McKinsey, l'IA en entreprise</h2>
  <div class="encadre"><b>Attention à la source</b>Le chiffre de 88 % circule comme « le rapport de Stanford ». Il vient en réalité de l'enquête mondiale de McKinsey.</div>
  <ul class="liste" style="margin-top:12px">
    <li><b>88 % des répondants</b> disent que leur entreprise utilise l'IA dans au moins une fonction (enquête 2025, 1 993 participants). Mais seulement 7 % disent qu'elle est déployée à grande échelle dans toute l'organisation.</li>
    <li><b>Les agents, un service sur dix au plus</b> : dans chaque fonction de l'entreprise, pas plus de 10 % des répondants disent que leur organisation déploie des agents IA à grande échelle (enquête 2025).</li>
    <li><b>Édition 2026</b> : 40 % des répondants de grandes entreprises (plus d'un milliard de dollars de chiffre d'affaires) disent déployer des agents IA à grande échelle, contre 27 % l'an dernier. Dans les plus petites, c'est 22 %, sans progrès.</li>
    <li><b>Et l'impact ?</b> 37 % attribuent au moins un peu de leur résultat opérationnel à l'IA, à peu près comme l'an dernier.</li>
  </ul>
</section>

<section>
  <h2><span class="num">1</span>Ce que ça veut dire pour toi</h2>
  <p>L'outil n'est plus le problème : les meilleurs modèles se valent presque, et beaucoup sont gratuits ou peu chers. La différence se fait sur l'usage réel. Presque tout le monde a essayé. Peu l'ont branché sur une tâche précise qui tourne chaque semaine.</p>
  <pre><code>Voici mon métier : [métier].
Quelle tâche de ma semaine pourrais-je confier à l'IA
dès cette semaine, avec un gain de temps mesurable ?
Donne-moi une seule tâche, et les 3 étapes pour commencer.</code></pre>
</section>

<section>
  <div class="regle">
    <h2>Lire un chiffre sans se faire avoir</h2>
    <ol class="etapes">
      <li><b>Qui l'a mesuré ?</b> Stanford, McKinsey, ou un créateur de contenu qui mélange les deux.</li>
      <li><b>Quand, et sur qui ?</b> Une enquête auprès de dirigeants n'est pas une mesure de toute l'économie.</li>
      <li><b>Ouvre la source.</b> Tous les liens sont en bas de cette page.</li>
    </ol>
  </div>
</section>
""",
)

# ─────────────────────────────── 42 · MONTRE UNE TÂCHE À CLAUDE
PAGES["record-skill"] = dict(
    video="42 · Montre une tâche à Claude",
    title="Record a skill : montre une tâche à Claude, il la refait (pas à pas)",
    desc="Enregistre ton écran en expliquant ta tâche, Claude en fait une skill réutilisable. Les conditions (Mac, forfaits), le pas à pas officiel et les précautions pour tes données.",
    og_pill="Les bases de l'IA · 42", og_titre="Ta première skill en montrant la tâche à Claude",
    marque="Les bases de l'IA · 42",
    h1="Montre-lui une fois, <em>il la refait</em>",
    chapo="Avec Record a skill, tu fais ta tâche devant Claude en expliquant à voix haute. Il en tire une compétence, une skill, et la refait ensuite à ta place. Voici le pas à pas, tiré de l'aide officielle.",
    verifie="16/10/2026",
    sources=[SRC_SKILLS_AIDE],
    corps="""
<section>
  <h2>Avant de commencer</h2>
  <div class="encadre"><b>Les conditions</b>Dans Cowork, l'application Claude pour Mac. Forfaits Pro, Max ou Team. Pas dans le chat, pas sur Windows, pas en gratuit ni en Enterprise.</div>
  <div class="encadre"><b>Tout est capté</b>Pendant l'enregistrement, tout ce qui est à l'écran et tout ce que tu dis est enregistré. Ferme ce que tu ne veux pas montrer. Pas de mot de passe, pas de vraies données clients : fais ta démo avec de fausses données.</div>
</section>

<section>
  <h2><span class="num">1</span>Enregistrer</h2>
  <ol class="etapes">
    <li><b>Mets à jour Claude pour Mac.</b> Au premier essai, macOS te demande deux autorisations : Accessibilité et Enregistrement de l'écran. Accepte, puis relance Claude s'il le demande.</li>
    <li><b>Ouvre Cowork</b>, puis le bouton « + » dans la zone de saisie, et « Record a skill ». Autre chemin : Customize, Skills, Add, puis « Record your screen ».</li>
    <li><b>Clique sur « Start recording »</b>, micro allumé.</li>
    <li><b>Fais ta tâche normalement, en expliquant à voix haute</b> : pourquoi tu sautes une étape, comment tu choisis entre deux options. C'est ce que l'écran seul ne montre pas.</li>
    <li><b>Clique sur « Done »</b> quand c'est fini. Tu as environ 10 minutes, un compte à rebours s'affiche dans la dernière minute.</li>
  </ol>
</section>

<section>
  <h2><span class="num">2</span>Valider la skill</h2>
  <ol class="etapes">
    <li><b>Claude analyse ta démonstration</b> et te propose une skill.</li>
    <li><b>Ouvre « Content »</b> sur la carte proposée, et lis ce qu'il a compris.</li>
    <li><b>« Save » pour la garder</b>, « Dismiss » pour la jeter. Si elle ressemble à une skill existante, il propose plutôt de la mettre à jour.</li>
    <li><b>Tu la retrouves dans Customize, puis Skills.</b> Tu peux la modifier, la partager ou la supprimer.</li>
  </ol>
  <p class="note">La vidéo et le son ne sont pas conservés. Des captures d'écran restent dans la tâche Cowork : supprime la tâche pour les effacer.</p>
</section>

<section>
  <h2><span class="num">3</span>Qu'elle se lance au bon moment</h2>
  <p>Claude choisit une skill en lisant sa description. Relis celle qu'il a écrite, et ajoute les mots que tu emploies vraiment pour demander cette tâche. La méthode : <a href="/description-skill">pourquoi ton skill ne se lance jamais</a>.</p>
</section>

<section>
  <div class="regle">
    <h2>Mes 3 conseils</h2>
    <ol class="etapes">
      <li><b>Une tâche courte et répétée</b> pour ta première skill. Pas ton processus le plus compliqué.</li>
      <li><b>Teste sur un petit échantillon</b> avant de lui confier cent dossiers.</li>
      <li><b>Pour une tâche répétée des centaines de fois, demande-lui s'il y a plus simple</b> : un connecteur ou un script est souvent plus rapide et plus fiable que de rejouer des clics.</li>
    </ol>
  </div>
</section>
""",
)
