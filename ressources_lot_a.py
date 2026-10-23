# Lot A des pages ressources (vidéos 12, 17 à 27). S'exécute à la suite de ressources_pages.py (PAGES existe déjà).
# Règles : faits vérifiés à la source le 15/10/2026, zéro tiret cadratin, zéro point-virgule dans le texte affiché.

SRC_PROMPT = ("Anthropic : Prompting best practices", "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices")
SRC_MEMOIRE_FR = ("Aide Claude : la recherche et la mémoire", "https://support.claude.com/fr/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context")
SRC_PROJETS = ("Aide Claude : créer et gérer des projets", "https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects")
SRC_CC_MEMORY = ("Claude Code : How Claude remembers your project", "https://code.claude.com/docs/en/memory")
SRC_GH_REPO = ("GitHub : About repositories", "https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories")
SRC_GH_LICENCE = ("GitHub : Licensing a repository", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository")
SRC_GH_SECURITY = ("GitHub : Adding a security policy", "https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository")
SRC_BOOK_NOTICE = ("Avis de sécurité du projet book-to-skill", "https://github.com/virgiliojr94/book-to-skill/blob/master/SECURITY-NOTICE.md")
SRC_SKILLS_FR = ("Aide Claude : utiliser les compétences (skills)", "https://support.claude.com/fr/articles/12512180-using-skills-in-claude")
SRC_SKILLS_ENT = ("Anthropic : Skills for enterprise (liste de vérification)", "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise")
SRC_SKILLS_REPO = ("Dépôt officiel anthropics/skills", "https://github.com/anthropics/skills")
SRC_CC_SKILLS = ("Claude Code : Skills", "https://code.claude.com/docs/en/skills")
SRC_API_KEYS = ("Aide Claude : bonnes pratiques des clés API", "https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure")
SRC_GET_KEY = ("Anthropic : créer sa clé API", "https://platform.claude.com/docs/en/get-api-key")
SRC_API_FUITE = ("Aide Claude : clé API compromise", "https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised")
SRC_CC_AUTH = ("Claude Code : Authentication", "https://code.claude.com/docs/en/authentication")
SRC_GH_IGNORE = ("GitHub : Ignoring files", "https://docs.github.com/en/get-started/git-basics/ignoring-files")
SRC_REGISTER = ("The Register : clé Gemini volée, 82 314 $", "https://www.theregister.com/2026/03/03/gemini_api_key_82314_dollar_charge/")
SRC_MCP_INTRO = ("Model Context Protocol : introduction", "https://modelcontextprotocol.io/docs/getting-started/intro")
SRC_CONNECTEURS_FR = ("Aide Claude : connecteurs personnalisés (MCP distant)", "https://support.claude.com/fr/articles/11175166-get-started-with-custom-connectors-using-remote-mcp")
SRC_CONNECTEURS_LABELS = ("Claude : vérification des connecteurs", "https://claude.com/docs/connectors/verification")
SRC_CC_MCP = ("Claude Code : MCP", "https://code.claude.com/docs/en/mcp")
SRC_HOOKS_GUIDE = ("Claude Code : Automate actions with hooks", "https://code.claude.com/docs/en/hooks-guide")
SRC_HOOKS_REF = ("Claude Code : Hooks reference", "https://code.claude.com/docs/en/hooks")
SRC_CC_SECURITY = ("Claude Code : Security", "https://code.claude.com/docs/en/security")
SRC_CC_MODES = ("Claude Code : Choose a permission mode", "https://code.claude.com/docs/en/permission-modes")
SRC_CC_PERMS = ("Claude Code : Permissions", "https://code.claude.com/docs/en/permissions")
SRC_CC_DATA = ("Claude Code : Data usage", "https://code.claude.com/docs/en/data-usage")
SRC_PRIVACY_REGLAGE_FR = ("Confidentialité Claude : changer le réglage d'amélioration", "https://privacy.claude.com/fr/articles/12109829-how-do-i-change-my-model-improvement-privacy-setting")
SRC_PRIVACY_DUREE = ("Confidentialité Claude : durée de conservation", "https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data")
SRC_PRIVACY_FAQ = ("Aide Claude : FAQ confidentialité", "https://support.claude.com/en/articles/8325621-claude-data-privacy-faq")
SRC_PRIVACY_PRO = ("Confidentialité Claude : données et entraînement", "https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training")
SRC_CONDITIONS = ("Anthropic : mise à jour des conditions grand public", "https://www.anthropic.com/news/updates-to-our-consumer-terms")
SRC_CC_VSCODE = ("Claude Code : Use Claude Code in VS Code", "https://code.claude.com/docs/en/vs-code")
SRC_VSCODE_FAQ = ("VS Code : FAQ", "https://code.visualstudio.com/docs/supporting/faq")
SRC_VERCEL_START = ("Vercel : Getting started", "https://vercel.com/docs/getting-started-with-vercel")
SRC_VERCEL_HOBBY = ("Vercel : Hobby plan", "https://vercel.com/docs/plans/hobby")
SRC_VERCEL_FAIR = ("Vercel : Fair use (usage commercial)", "https://vercel.com/docs/limits/fair-use-guidelines")
SRC_VERCEL_DOMAINES = ("Vercel : Working with domains", "https://vercel.com/docs/domains/working-with-domains")
SRC_NETLIFY = ("Netlify : Create deploys", "https://docs.netlify.com/deploy/create-deploys/")
SRC_CLOUDFLARE = ("Cloudflare Pages : Get started", "https://developers.cloudflare.com/pages/get-started/")
SRC_PLANIFIEES_FR = ("Aide Claude : tâches planifiées", "https://support.claude.com/fr/articles/13854387-schedule-recurring-tasks-in-claude-cowork")


# 12 · LE PROMPT
PAGES["prompt"] = dict(
    video="12 · Le prompt",
    title="Les trois règles d'un bon prompt, avec un exemple",
    desc="Le prompt expliqué simplement : les trois règles de base (le rôle, le contexte, le format) et un exemple avant et après à copier, d'après les recommandations d'Anthropic.",
    og_pill="Les bases de l'IA · 12", og_titre="Les trois règles d'un bon prompt",
    marque="Les bases de l'IA · 12",
    h1="Les trois règles <em>d'un bon prompt</em>",
    chapo="L'IA te répond à côté ? Souvent, ce n'est pas elle, c'est la consigne. Un prompt, c'est ta consigne. Trois règles suffisent pour passer d'une réponse passe-partout à une réponse qui te sert vraiment.",
    verifie="16/10/2026",
    sources=[SRC_PROMPT, SRC_PROJETS],
    corps="""
<section>
  <h2>Le test du collègue</h2>
  <div class="encadre"><b>Ce que conseille Anthropic</b>Vois Claude comme un nouvel employé brillant, mais qui ne connaît ni ton métier ni tes habitudes. Avant d'envoyer ton prompt, imagine-le lu par un collègue qui ne connaît pas le dossier. S'il serait perdu, Claude le sera aussi.</div>
</section>

<section>
  <h2><span class="num">1</span>Dis le rôle</h2>
  <p>Dis-lui qui il est pour cette tâche. D'après Anthropic, une seule phrase suffit à changer le ton et le niveau de la réponse.</p>
  <pre><code>Tu es mon assistant comptable.</code></pre>
  <ul class="liste">
    <li><b>Autres exemples :</b> « Tu es un juriste qui relit un contrat », « Tu es un commercial qui prépare un rendez-vous », « Tu es un correcteur exigeant ».</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Dis le contexte</h2>
  <p>Qui tu es, pour qui tu travailles, et pourquoi tu demandes. Anthropic insiste sur ce dernier point : expliquer le pourquoi d'une consigne aide Claude à viser juste.</p>
  <pre><code>Je suis plombier, j'ai 3 salariés, mes clients sont des particuliers.
Je veux relancer les devis envoyés il y a plus de 15 jours,
sans paraître insistant.</code></pre>
</section>

<section>
  <h2><span class="num">3</span>Dis le format voulu</h2>
  <p>Longueur, forme, ton. Sinon, Claude choisit pour toi. Et dis ce que tu veux plutôt que ce que tu ne veux pas : « écris en paragraphes courts » marche mieux que « pas de listes ».</p>
  <pre><code>En cinq points, une phrase chacun, ton cordial.</code></pre>
</section>

<section>
  <h2>L'exemple complet</h2>
  <div class="encadre"><b>Avant</b>« Écris-moi un mail de relance. »</div>
  <p>Réponse générique, à reprendre trois fois.</p>
  <p><b>Après</b>, les trois règles dans un seul message :</p>
  <pre><code>Tu es mon assistant commercial.
Je suis plombier, 3 salariés, clients particuliers.
J'ai envoyé un devis de 2 400 € pour une salle de bain
il y a 3 semaines, sans réponse. Je veux relancer
sans paraître insistant.
Écris le mail : 6 lignes maximum, ton cordial,
termine par une question simple.</code></pre>
  <p class="note">Le bonus, si tu veux aller plus loin : colle un exemple de mail dont tu es content. D'après Anthropic, un exemple est l'un des moyens les plus fiables d'obtenir le bon ton et la bonne forme.</p>
</section>

<section>
  <div class="regle">
    <h2>Pour ne plus le répéter</h2>
    <ol class="etapes">
      <li><b>Crée un Projet</b> dans Claude, un par grand sujet.</li>
      <li><b>Écris le rôle et le contexte dans les instructions du projet.</b> Claude les applique à toutes les conversations de ce projet.</li>
      <li><b>Dans chaque conversation, tu n'as plus qu'à donner la tâche et le format.</b></li>
    </ol>
  </div>
  <p class="note">Précis à l'entrée, précis à la sortie. Avec Claude Code, l'équivalent des instructions de projet, c'est le fichier CLAUDE.md : <a href="/claude-md">ta trame CLAUDE.md</a>.</p>
</section>
""",
)

# 17 · LA MÉMOIRE
PAGES["memoire"] = dict(
    video="17 · La mémoire",
    title="Bien organiser la mémoire de Claude : le guide",
    desc="Où trouver la mémoire de Claude, comment la lire, la corriger et la ranger par projet, ce qu'elle ne retient jamais, et comment ça marche dans Claude Code.",
    og_pill="Les bases de l'IA · 17", og_titre="Bien organiser la mémoire de Claude",
    marque="Les bases de l'IA · 17",
    h1="Bien organiser <em>la mémoire</em> de Claude",
    chapo="Le modèle, lui, ne retient rien d'une conversation à l'autre. Ce qui se souvient, c'est l'appli autour : elle prend des notes, et elle les relit. Bonne nouvelle, ces notes, tu peux les lire, les corriger et les ranger.",
    verifie="16/10/2026",
    sources=[SRC_MEMOIRE_FR, SRC_PROJETS, SRC_CC_MEMORY],
    corps="""
<section>
  <h2><span class="num">1</span>Où la trouver</h2>
  <ul class="liste">
    <li><b>Paramètres, puis Mémoire.</b> Sur les forfaits Gratuit, Pro et Max, elle est activée par défaut, sur le web, l'ordinateur et le téléphone. L'interrupteur s'appelle « Générer une mémoire à partir des chats ».</li>
    <li><b>Tes souvenirs y sont rangés par sujets.</b> Tu ouvres un sujet, tu modifies ou tu supprimes.</li>
    <li><b>Tu peux aussi lui parler directement.</b> La correction s'applique à ta conversation suivante.</li>
  </ul>
  <pre><code>Retiens que je suis passé en freelance en janvier.
Oublie l'ancien nom de ma société.</code></pre>
  <p class="note">Les comptes plus anciens trouvent ces réglages dans Paramètres, puis Capacités. La recherche dans tes anciennes conversations est réservée aux forfaits payants.</p>
</section>

<section>
  <h2><span class="num">2</span>Range-la par projet</h2>
  <p>Chaque Projet a sa propre mémoire. Dans un projet, Claude utilise la mémoire de ce projet et ta mémoire générale, jamais celle des autres projets.</p>
  <ul class="liste">
    <li><b>Un projet par client ou par grand sujet.</b> Ce que Claude apprend sur le client A ne déborde pas chez le client B.</li>
    <li><b>Un projet à isoler complètement ?</b> Dans ses réglages, désactive « Utiliser la mémoire du compte ».</li>
    <li><b>Sur le gratuit,</b> tu as droit à 5 projets.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Ce qu'elle ne retient pas, et les pièges</h2>
  <ul class="liste">
    <li><b>Les sujets sensibles</b> (santé, politique) ne sont pas enregistrés par défaut. C'est une option : « Inclure les sujets sensibles en mémoire ».</li>
    <li><b>Jamais enregistrés, même si tu le demandes :</b> numéros de pièce d'identité, antécédents judiciaires, numéros de compte, statut d'immigration.</li>
    <li><b>Le piège :</b> supprimer une conversation n'efface pas les souvenirs qu'elle a créés. Il faut les supprimer un par un dans Paramètres, Mémoire.</li>
    <li><b>Une conversation sans trace ?</b> Le chat incognito, l'icône fantôme en haut à droite. Rien ne va dans l'historique ni dans la mémoire.</li>
  </ul>
</section>

<section>
  <h2><span class="num">4</span>Dans Claude Code</h2>
  <div class="encadre"><b>Le fichier CLAUDE.md, c'est toi qui l'écris</b>Tes règles permanentes, relues à chaque session. Anthropic conseille de rester sous les 200 lignes : plus il est long, moins il est suivi. La trame : <a href="/claude-md">ta trame CLAUDE.md</a>.</div>
  <div class="encadre"><b>La mémoire automatique, c'est lui qui l'écrit</b>Claude note tout seul ce qu'il apprend de tes corrections, dans un dossier par projet sous ~/.claude/projects/. Le fichier MEMORY.md sert de sommaire : ses 200 premières lignes (ou 25 Ko) sont lues à chaque démarrage.</div>
  <p>Pour tout voir et tout corriger, tape <b>/memory</b> dans une session. Ce sont de simples fichiers texte.</p>
</section>

<section>
  <div class="regle">
    <h2>Le rangement en 3 réflexes</h2>
    <ol class="etapes">
      <li><b>Relis ta mémoire une fois par mois.</b> Corrige ce qui est faux, supprime ce qui est dépassé.</li>
      <li><b>Un projet par client.</b> La mémoire reste à sa place.</li>
      <li><b>Incognito pour le ponctuel.</b> Une question qui ne doit rien laisser derrière elle.</li>
    </ol>
  </div>
</section>
""",
)

# 18 · C'EST QUOI GITHUB
PAGES["verifier-un-repo"] = dict(
    video="18 · C'est quoi GitHub",
    title="Vérifier un repo GitHub avant de l'installer : ma méthode",
    desc="Ce qu'est un repo GitHub, et les vérifications à faire avant d'installer le code de quelqu'un d'autre : propriétaire, étoiles, licence, avis de sécurité, scripts. Avec le prompt pour le faire faire par Claude.",
    og_pill="Les bases de l'IA · 18", og_titre="Vérifier un repo avant de l'installer",
    marque="Les bases de l'IA · 18",
    h1="Vérifier un repo <em>avant de l'installer</em>",
    chapo="Un repo, c'est le dossier d'un projet : tous ses fichiers, et l'historique de chaque modification. Un repo public, tout le monde peut le voir et le télécharger. Mais c'est le code de quelqu'un d'autre. Voici ce que je vérifie avant qu'il touche à mon ordinateur.",
    verifie="16/10/2026",
    sources=[SRC_GH_REPO, SRC_GH_LICENCE, SRC_GH_SECURITY, SRC_BOOK_NOTICE],
    corps="""
<section>
  <h2>Pourquoi c'est sérieux</h2>
  <div class="encadre"><b>Même nom, autre propriétaire</b>En août 2026, un projet populaire, book-to-skill, a été recopié par un autre compte, sous le même nom. La copie ajoutait du code qui fouillait les portefeuilles de cryptomonnaies et envoyait des fichiers vers l'extérieur. L'auteur original a publié un avis de sécurité dans son repo. Le détail du cas : <a href="/installer-un-skill">installer un skill sans risque</a>.</div>
</section>

<section>
  <h2><span class="num">1</span>Les 6 vérifications, sur la page du repo</h2>
  <ul class="liste">
    <li><b>Le propriétaire.</b> Le nom du projet se copie en une seconde, le compte qui le publie, non. Va sur le site officiel de l'outil et regarde vers quel compte il renvoie.</li>
    <li><b>Les étoiles et la date de création.</b> Mille étoiles pour un repo créé la semaine dernière, ce n'est pas un succès, c'est une anomalie.</li>
    <li><b>La dernière activité.</b> Un outil qui dépend d'un autre service et qui n'a pas bougé depuis des mois est sans doute déjà cassé.</li>
    <li><b>La licence.</b> D'après GitHub, sans licence, les droits d'auteur s'appliquent par défaut : personne n'a le droit de reproduire, distribuer ou modifier le code.</li>
    <li><b>Le fichier SECURITY.md.</b> C'est la politique de sécurité du projet : les versions suivies, et comment signaler une faille. Certains auteurs publient aussi un avis de sécurité dans leur repo pour signaler les copies piégées de leur projet, comme celui de book-to-skill.</li>
    <li><b>Les issues.</b> L'onglet où les utilisateurs signalent les problèmes. Cherche « ne marche pas », « malware », ou le nom de ton système.</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Ce que fait vraiment le code</h2>
  <p>Les fichiers à regarder : ceux qui s'exécutent à l'installation. Un seul de ces signaux, et je n'installe pas :</p>
  <ul class="liste">
    <li>Une commande qui télécharge et exécute du code sans le montrer (du type curl, puis bash).</li>
    <li>On te demande de coller une clé API dans la conversation.</li>
    <li>La vérification des certificats de sécurité est désactivée.</li>
    <li>Le code va lire tes clés SSH, ton trousseau, tes portefeuilles crypto ou les mots de passe de ton navigateur.</li>
    <li>Des données partent vers un serveur dont la documentation ne parle pas.</li>
    <li>Du code caché (illisible, encodé) qui s'exécute.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Fais-le faire par Claude, sans rien installer</h2>
  <p>Tu n'as pas besoin de savoir lire le code. Claude peut le lire pour toi, sans rien exécuter :</p>
  <pre><code>Audite ce dépôt GitHub sans rien installer ni exécuter : [colle le lien].
Dis-moi :
- qui est le propriétaire, et si le site officiel renvoie vers lui
- la date de création, le nombre d'étoiles, la dernière modification
- la licence, et s'il existe un fichier SECURITY.md
- ce que font les scripts d'installation : envoi de données,
  accès à mes fichiers, commandes administrateur.
Termine par un verdict : vert, orange ou rouge, avec la raison.</code></pre>
</section>

<section>
  <div class="regle">
    <h2>Les 3 règles</h2>
    <ol class="etapes">
      <li><b>Installe depuis la source officielle,</b> jamais depuis un lien reçu en commentaire ou en message.</li>
      <li><b>Teste dans un dossier sans rien de sensible,</b> pas là où sont tes dossiers clients.</li>
      <li><b>Dans le doute, tu n'installes pas.</b> Il existe presque toujours une alternative plus sûre.</li>
    </ol>
  </div>
  <p class="note">La même méthode vaut pour un skill et pour un MCP : <a href="/installer-un-skill">installer un skill</a>, <a href="/mcp">brancher un MCP</a>.</p>
</section>
""",
)

# 19 · LE SKILL
PAGES["installer-un-skill"] = dict(
    video="19 · Le skill",
    title="Installer un skill Claude sans risque : ma méthode",
    desc="Ce qu'est un skill, où trouver les skills officiels, et l'audit à faire avant d'en installer un autre, tiré des recommandations d'Anthropic. Avec un cas réel de skill piégé.",
    og_pill="Les bases de l'IA · 19", og_titre="Installer un skill sans risque",
    marque="Les bases de l'IA · 19",
    h1="Installer un skill <em>sans risque</em>",
    chapo="Un skill, c'est une compétence que tu ajoutes à Claude : des instructions, et parfois des scripts qui s'exécutent. Anthropic l'écrit noir sur blanc dans son aide : n'installe des skills que depuis des sources fiables. Voici comment faire le tri.",
    verifie="16/10/2026",
    sources=[SRC_SKILLS_FR, SRC_SKILLS_ENT, SRC_SKILLS_REPO, SRC_CC_SKILLS, SRC_BOOK_NOTICE],
    corps="""
<section>
  <h2>Le cas qui montre pourquoi</h2>
  <div class="encadre"><b>book-to-skill, août 2026</b>Un skill populaire a été recopié par un autre compte GitHub, sous le même nom. D'après l'avis de sécurité publié le 17 août par l'auteur original, la copie désactivait la vérification des certificats, envoyait les informations de la machine vers un serveur externe, fouillait les données de portefeuilles de cryptomonnaies, et sur Windows embarquait un programme qu'elle pouvait lancer toute seule. Les gens ont été piégés parce que la copie ressemblait exactement à l'original.</div>
</section>

<section>
  <h2><span class="num">1</span>D'abord, les skills officiels</h2>
  <ul class="liste">
    <li><b>Dans l'appli Claude,</b> Anthropic fournit déjà des skills pour Excel, Word, PowerPoint et PDF. Claude s'en sert tout seul quand ta demande s'y prête. Il faut que l'exécution de code soit activée : Paramètres, puis Capacités.</li>
    <li><b>Pour voir, activer ou ajouter des skills :</b> Personnaliser, puis Compétences.</li>
    <li><b>Dans Claude Code,</b> le dépôt officiel d'Anthropic s'ajoute avec cette commande :</li>
  </ul>
  <pre><code>/plugin marketplace add anthropics/skills</code></pre>
  <p class="note">Anthropic présente ces skills comme des exemples, à tester avant de t'y fier pour une tâche importante.</p>
</section>

<section>
  <h2><span class="num">2</span>Pour tous les autres, l'audit en 6 points</h2>
  <p>C'est la version simplifiée de la liste qu'Anthropic donne aux entreprises :</p>
  <ul class="liste">
    <li><b>La provenance.</b> Qui l'a fait, et est-ce le bon compte ? La méthode : <a href="/verifier-un-repo">vérifier un repo</a>.</li>
    <li><b>Tout le dossier, pas seulement SKILL.md.</b> Les scripts (.py, .sh, .js) s'exécutent avec un accès complet à ton environnement.</li>
    <li><b>Les appels vers internet.</b> Une adresse web, curl, fetch, requests : c'est une porte de sortie possible pour tes données.</li>
    <li><b>Les consignes louches.</b> Ignorer les règles de sécurité, cacher une action, envoyer des données : on n'installe pas.</li>
    <li><b>Aucun mot de passe ni clé écrit dedans.</b></li>
    <li><b>Dans Claude Code, le champ allowed-tools.</b> Il liste les outils que Claude peut utiliser sans te demander quand le skill est lancé. Relis-le avant de l'utiliser.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Fais-le vérifier par Claude, à chaque fois</h2>
  <p>Écris la règle une fois dans ton fichier CLAUDE.md, ou dans les instructions d'un projet :</p>
  <pre><code>Avant d'installer le moindre skill, audite-le :
qui l'a fait, ce que font ses scripts,
s'il contacte internet, s'il lit des fichiers hors de son dossier.
Ne me propose l'installation qu'après ton verdict.</code></pre>
  <p class="note">Pour aller plus loin, un hook peut rendre cette vérification obligatoire : <a href="/hooks">des exemples de hooks</a>.</p>
</section>

<section>
  <div class="regle">
    <h2>Tu as déjà installé un skill douteux ?</h2>
    <ol class="etapes">
      <li><b>Ne le relance pas.</b> Désactive-le dans Personnaliser, Compétences, ou avec /plugin dans Claude Code.</li>
      <li><b>Un portefeuille crypto sur la machine ?</b> Suis la procédure de récupération de ton éditeur, depuis un autre appareil.</li>
      <li><b>Change les mots de passe enregistrés dans ton navigateur,</b> depuis un appareil sain.</li>
    </ol>
  </div>
</section>
""",
)

# 20 · LA CLÉ API
PAGES["cle-api"] = dict(
    video="20 · Clé API",
    title="Où ranger ta clé API, pas à pas",
    desc="Ce qu'est une clé API, les quatre interdits, où la ranger pas à pas (coffre, variable d'environnement, .gitignore) et quoi faire si elle a fuité, d'après l'aide officielle d'Anthropic.",
    og_pill="Les bases de l'IA · 20", og_titre="Où ranger ta clé API, pas à pas",
    marque="Les bases de l'IA · 20",
    h1="Où ranger ta clé API, <em>pas à pas</em>",
    chapo="Une clé API, c'est un mot de passe entre deux logiciels. Un badge d'accès. Qui a ta clé peut l'utiliser à ta place, et payer avec ton compte. Voici où la ranger, et quoi faire si elle fuit.",
    verifie="16/10/2026",
    sources=[SRC_API_KEYS, SRC_GET_KEY, SRC_API_FUITE, SRC_CC_AUTH, SRC_GH_IGNORE, SRC_REGISTER],
    corps="""
<section>
  <h2>Ce que ça peut coûter</h2>
  <div class="encadre"><b>Un cas réel, février 2026</b>Une startup de trois personnes s'est fait voler sa clé Google. Résultat : 82 314 $ de facture d'IA en environ 48 heures, pour une dépense habituelle d'environ 180 $ par mois.</div>
  <div class="encadre"><b>Côté Anthropic</b>Si une clé Claude est repérée dans un dépôt GitHub public, GitHub prévient Anthropic, qui la désactive automatiquement. Une sécurité utile, mais ne compte pas dessus : la fuite peut venir d'ailleurs.</div>
</section>

<section>
  <h2><span class="num">1</span>Les 4 interdits</h2>
  <ul class="liste">
    <li><b>Jamais dans une conversation,</b> même avec Claude.</li>
    <li><b>Jamais dans un mail, un forum ou un ticket de support,</b> même adressé à Anthropic.</li>
    <li><b>Jamais écrite dans ton code ou un fichier de réglages.</b></li>
    <li><b>Jamais partagée.</b> Une clé par personne, et une par usage (test, production).</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Où la ranger, pas à pas (Mac)</h2>
  <ol class="etapes">
    <li><b>Crée ta clé</b> dans la Console Claude, page API keys (platform.claude.com/settings/keys). Elle ne s'affiche qu'une fois : copie-la.</li>
    <li><b>Range-la dans le coffre de ton Mac</b>, le trousseau. Colle cette commande dans le Terminal, puis colle ta clé quand il te la demande :
      <pre><code>security add-generic-password -a "$USER" -s ANTHROPIC_API_KEY -w</code></pre></li>
    <li><b>Dis à ton ordinateur où la chercher.</b> Ajoute cette ligne à la fin du fichier ~/.zshrc (la clé reste dans le coffre, le fichier ne contient que le chemin pour la retrouver) :
      <pre><code>export ANTHROPIC_API_KEY="$(security find-generic-password -a "$USER" -s ANTHROPIC_API_KEY -w)"</code></pre></li>
    <li><b>Dans un projet qui utilise un fichier .env,</b> ajoute .env dans le fichier .gitignore du projet. Git ignorera ce fichier, et il ne partira jamais sur GitHub.</li>
  </ol>
  <p class="note">Sur Windows ou si tu bloques, demande à Claude : « Explique-moi comment ranger ma clé API dans le coffre de mon système, sans jamais me demander de te la coller. »</p>
</section>

<section>
  <h2><span class="num">3</span>Le piège avec Claude Code</h2>
  <p>Avec un forfait Pro ou Max, Claude Code n'a pas besoin de clé API : tu te connectes avec ton compte. Mais si la variable ANTHROPIC_API_KEY existe sur ta machine, Claude Code te propose de l'utiliser. Si tu acceptes, il passe par la clé, donc par la facturation API, au lieu de ton abonnement.</p>
  <p>Pour vérifier ce qu'il utilise, tape <b>/status</b> dans Claude Code.</p>
</section>

<section>
  <div class="regle">
    <h2>Ta clé a fuité ?</h2>
    <ol class="etapes">
      <li><b>Supprime-la tout de suite :</b> Console Claude, page API keys, les trois points à côté de la clé, puis « Delete API Key ».</li>
      <li><b>Crée une nouvelle clé</b> avec « Create Key », et range-la dans le coffre.</li>
      <li><b>Si l'activité suspecte continue,</b> contacte le support d'Anthropic.</li>
    </ol>
  </div>
  <p class="note">Le bon réflexe, même sans fuite : changer tes clés régulièrement. Anthropic donne l'exemple de tous les 90 jours.</p>
</section>
""",
)

# 21 · LE MCP
PAGES["mcp"] = dict(
    video="21 · Le MCP",
    title="Brancher un MCP en toute sécurité",
    desc="Le MCP expliqué simplement, les trois types de connecteurs (vérifié, communauté, personnalisé), les vérifications à faire avant d'en brancher un, et le pas à pas dans Claude et Claude Code.",
    og_pill="Les bases de l'IA · 21", og_titre="Brancher un MCP en toute sécurité",
    marque="Les bases de l'IA · 21",
    h1="Brancher un MCP <em>en toute sécurité</em>",
    chapo="MCP veut dire Model Context Protocol. C'est un standard ouvert pour relier une IA à tes outils, que ses créateurs comparent à une prise USB-C. Une fois branché, Claude lit et agit directement dans l'outil. Voici comment le brancher sans ouvrir la porte à n'importe quoi.",
    verifie="16/10/2026",
    sources=[SRC_MCP_INTRO, SRC_CONNECTEURS_LABELS, SRC_CONNECTEURS_FR, SRC_CC_MCP],
    corps="""
<section>
  <h2>Les deux risques</h2>
  <div class="encadre"><b>Tes données chez un tiers</b>Un connecteur hébergé ailleurs, c'est un service qui voit passer ce que Claude lui envoie. Anthropic ne contrôle pas comment un connecteur tiers traite tes données.</div>
  <div class="encadre"><b>Des instructions cachées</b>Un serveur MCP malveillant peut glisser des consignes cachées pour pousser Claude à faire autre chose que ce que tu as demandé. On appelle ça une injection d'invite. Et un MCP que tu télécharges, c'est en plus du code qui tourne chez toi.</div>
</section>

<section>
  <h2><span class="num">1</span>Lis l'étiquette</h2>
  <p>L'annuaire des connecteurs de Claude affiche trois niveaux :</p>
  <ul class="liste">
    <li><b>Vérifié (une coche).</b> Anthropic a testé ses outils. Ce n'est pas pour autant un audit de sécurité ni une garantie : le développeur peut changer ses outils après.</li>
    <li><b>Communauté.</b> Fait par un développeur tiers, filtré par Anthropic mais pas examiné en profondeur.</li>
    <li><b>Personnalisé.</b> Tu l'as ajouté toi-même avec son adresse. Anthropic ne l'a pas examiné du tout.</li>
  </ul>
</section>

<section>
  <h2><span class="num">2</span>Les 5 vérifications avant de brancher</h2>
  <ul class="liste">
    <li><b>Qui le développe ?</b> Uniquement des organisations en qui tu as confiance. Idéalement, l'éditeur de l'outil lui-même.</li>
    <li><b>Les autorisations demandées.</b> À la connexion, lis ce qu'il demande. Refuse ce qui semble inutile.</li>
    <li><b>Lecture ou écriture ?</b> Désactive les outils dont tu n'as pas besoin, surtout ceux qui peuvent écrire ou envoyer.</li>
    <li><b>« Toujours autoriser » avec parcimonie.</b> Seulement pour un serveur et un outil de confiance.</li>
    <li><b>Un MCP à télécharger ?</b> Même audit qu'un repo : <a href="/verifier-un-repo">vérifier un repo</a>.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Le pas à pas</h2>
  <p><b>Dans l'appli Claude :</b> Personnaliser, puis Connecteurs. Clique « + Ajouter », puis « Ajouter un connecteur personnalisé ». Donne un nom et l'adresse du serveur, puis « Ajouter ». Ensuite, tu l'actives conversation par conversation avec le bouton « + ». Sur le gratuit, un seul connecteur personnalisé.</p>
  <p><b>Pour le retirer :</b> Personnaliser, Connecteurs, puis « Supprimer » ou les trois points à côté du connecteur.</p>
  <p><b>Dans Claude Code :</b> l'exemple officiel, avec le serveur de Notion :</p>
  <pre><code>claude mcp add --transport http notion https://mcp.notion.com/mcp</code></pre>
  <p>Tape <b>/mcp</b> pour voir l'état de tes serveurs, et <b>claude mcp remove notion</b> pour en retirer un. Si un projet que tu as téléchargé contient ses propres serveurs (fichier .mcp.json), Claude Code te demande ton accord avant de les lancer. Lis la demande avant d'accepter.</p>
</section>

<section>
  <div class="regle">
    <h2>Les 3 réflexes</h2>
    <ol class="etapes">
      <li><b>L'officiel d'abord.</b> Le connecteur de l'éditeur, ou un connecteur vérifié.</li>
      <li><b>Le minimum d'accès.</b> Juste ce dont la tâche a besoin.</li>
      <li><b>Débranche ce que tu n'utilises plus.</b> Un accès inutile reste un accès.</li>
    </ol>
  </div>
</section>
""",
)

# 22 · LE HOOK
PAGES["hooks"] = dict(
    video="22 · Le hook",
    title="Des exemples de hooks utiles pour Claude Code",
    desc="Le hook expliqué simplement, cinq exemples utiles (notification, fichiers protégés, vérification avant installation), comment les créer sans coder, et les précautions à prendre.",
    og_pill="Les bases de l'IA · 22", og_titre="Des exemples de hooks utiles",
    marque="Les bases de l'IA · 22",
    h1="Des exemples de <em>hooks utiles</em>",
    chapo="Un hook, c'est un réflexe : « à chaque fois que ça se passe, fais ça ». Tu le règles une fois, Claude Code l'exécute à chaque fois. La différence avec une règle : une règle, Claude peut l'oublier. Un hook, non. C'est mécanique.",
    verifie="16/10/2026",
    sources=[SRC_HOOKS_GUIDE, SRC_HOOKS_REF, SRC_CC_MEMORY],
    corps=r"""
<section>
  <h2>Règle ou hook ?</h2>
  <div class="encadre"><b>Ce que dit Anthropic</b>Ton fichier CLAUDE.md, Claude le prend comme du contexte, pas comme une obligation. Pour bloquer une action quoi que Claude décide, la documentation renvoie vers un hook. Les hooks sont une fonction de Claude Code, donc d'un forfait payant.</div>
</section>

<section>
  <h2><span class="num">1</span>Le plus simple : demande-le à Claude</h2>
  <p>Pas besoin de savoir coder. La documentation officielle le dit : tu peux décrire le hook voulu à Claude, il l'écrit pour toi. Trois demandes à copier dans Claude Code :</p>
  <pre><code>Crée-moi un hook qui m'envoie une notification sur mon Mac
quand tu attends une réponse de ma part.</code></pre>
  <pre><code>Crée-moi un hook qui bloque toute modification du fichier .env
et du dossier .git, et qui t'explique pourquoi.</code></pre>
  <pre><code>Crée-moi un hook qui, avant chaque commande d'installation
(npm install, pip install, brew install), t'arrête
et t'oblige à vérifier l'outil d'abord.</code></pre>
  <p>Ensuite, tape <b>/hooks</b> : tu vois tous tes hooks, rangés par moment de déclenchement.</p>
</section>

<section>
  <h2><span class="num">2</span>Cinq hooks utiles</h2>
  <ul class="liste">
    <li><b>Être prévenu quand Claude attend.</b> Une notification dès qu'il a besoin de toi. Tu fais autre chose pendant qu'il travaille.</li>
    <li><b>Protéger tes fichiers sensibles.</b> Avant chaque modification, le hook vérifie le fichier visé. Si c'est .env ou .git, il bloque.</li>
    <li><b>Vérifier avant d'installer.</b> Le réflexe de la vidéo : aucune installation sans audit d'abord.</li>
    <li><b>Remettre en forme après chaque modification.</b> Ton code reste propre sans que tu y penses.</li>
    <li><b>Rappeler tes consignes après un résumé.</b> Quand la conversation est compactée, des détails se perdent. Le hook réinjecte l'essentiel. Le pourquoi : <a href="/contexte">l'antisèche du contexte</a>.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>À quoi ça ressemble</h2>
  <p>L'exemple de la documentation officielle, la notification sur Mac, à placer dans ~/.claude/settings.json :</p>
  <pre><code>{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}</code></pre>
  <ul class="liste">
    <li><b>~/.claude/settings.json</b> : le hook vaut pour tous tes projets.</li>
    <li><b>.claude/settings.json</b> dans un dossier : il vaut pour ce projet seulement.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>Les 3 précautions</h2>
    <ol class="etapes">
      <li><b>Un hook a tous tes droits.</b> D'après Anthropic, il peut modifier, supprimer ou lire n'importe quel fichier de ton compte. Relis-le et teste-le avant de l'adopter.</li>
      <li><b>Un hook trouvé sur internet</b> se vérifie comme un skill : <a href="/installer-un-skill">la méthode</a>.</li>
      <li><b>Dossier inconnu, prudence.</b> Claude Code ne lance les hooks d'un dossier qu'après que tu as accepté de lui faire confiance. Ne clique pas « oui » par réflexe.</li>
    </ol>
  </div>
</section>
""",
)

# 23 · LA PEUR : TES DOCUMENTS PRIVÉS
PAGES["acces-dossiers"] = dict(
    video="23 · La peur : tes documents privés",
    title="Comment Claude Code gère l'accès à tes dossiers",
    desc="Ce que Claude Code peut lire et modifier sur ton ordinateur, les modes de permission (Manuel et automatique), les réglages pour garder la main, et ce qui part chez Anthropic.",
    og_pill="Les bases de l'IA · 23", og_titre="Comment Claude gère l'accès à tes dossiers",
    marque="Les bases de l'IA · 23",
    h1="Comment Claude gère <em>l'accès à tes dossiers</em>",
    chapo="« Il va avoir accès à mes documents privés. » C'est la phrase que j'entends le plus. Au début, moi aussi ça m'inquiétait. Voici comment Claude Code fonctionne vraiment, et les réglages pour garder la main.",
    verifie="16/10/2026",
    sources=[SRC_CC_SECURITY, SRC_CC_MODES, SRC_CC_PERMS, SRC_CC_DATA],
    corps="""
<section>
  <h2><span class="num">1</span>Il travaille dans le dossier que tu lui ouvres</h2>
  <p>Claude Code démarre dans le dossier où tu le lances. C'est son terrain de travail. En mode Manuel, il te demande ton accord avant de lire ou d'écrire en dehors de ce dossier.</p>
  <div class="encadre"><b>La nuance à connaître</b>Cette limite est une demande d'autorisation, pas un mur. Une commande que tu acceptes peut agir partout où ton compte a accès. D'où la règle : lis avant de valider.</div>
  <p class="note">Lance-le toujours dans un dossier de projet, jamais à la racine de ton ordinateur ni dans tout ton dossier Documents.</p>
</section>

<section>
  <h2><span class="num">2</span>Qui valide les actions ?</h2>
  <div class="encadre"><b>Le mode Manuel : c'est toi</b>Il démarre en lecture seule. Avant de modifier un fichier, de lancer une commande ou d'aller sur internet, il te demande. Tu acceptes une fois, ou pour la suite.</div>
  <div class="encadre"><b>Le mode automatique : un second modèle</b>Bon à savoir : sur les versions récentes, c'est le mode de départ dans le terminal et dans VS Code. Un second modèle vérifie chaque action à ta place et bloque ce qui dépasse ta demande : télécharger et exécuter du code, envoyer des données sensibles à l'extérieur, détruire des fichiers qui existaient avant la session. Anthropic le précise : ce mode réduit les demandes, il ne garantit pas la sécurité.</div>
</section>

<section>
  <h2><span class="num">3</span>Les réglages pour garder la main</h2>
  <ol class="etapes">
    <li><b>Change de mode à tout moment.</b> Maj + Tab dans le terminal, le sélecteur de mode dans l'appli Claude et dans VS Code.</li>
    <li><b>Démarre toujours en Manuel, et interdis un fichier.</b> Dans le fichier ~/.claude/settings.json :
      <pre><code>{
  "permissions": {
    "defaultMode": "manual",
    "deny": ["Read(./.env)"]
  }
}</code></pre>
      La première ligne le fait démarrer en Manuel. La seconde lui interdit de lire ton fichier .env, celui qui contient souvent tes clés.</li>
    <li><b>Tu préfères ne pas toucher aux fichiers ?</b> Demande-le-lui :
      <pre><code>Règle-moi le mode Manuel par défaut, et interdis-toi
de lire le fichier .env de mes projets.</code></pre></li>
  </ol>
</section>

<section>
  <h2><span class="num">4</span>Ce qui part chez Anthropic</h2>
  <p>Claude Code tourne sur ton ordinateur. Mais pour réfléchir, il envoie tes messages et ce qu'il lit aux serveurs d'Anthropic, chiffrés pendant le trajet. Sur les forfaits Gratuit, Pro et Max, c'est gardé 30 jours si tu as refusé l'entraînement, jusqu'à 5 ans si tu l'as accepté.</p>
  <p class="note">Le réglage à vérifier : <a href="/donnees">tes données, les réglages</a>. Et la règle simple : ne lui ouvre pas un dossier que tu ne voudrais pas envoyer.</p>
</section>

<section>
  <div class="regle">
    <h2>Les 3 réflexes</h2>
    <ol class="etapes">
      <li><b>Un dossier dédié par projet.</b> Il voit ce dossier, pas le reste.</li>
      <li><b>Le mode Manuel pour le sensible.</b> Tu valides chaque action.</li>
      <li><b>Lis avant de valider.</b> Tu gardes la main, et les clés.</li>
    </ol>
  </div>
</section>
""",
)

# 24 · TES DONNÉES
PAGES["donnees"] = dict(
    video="24 · Tes données",
    title="Tes données dans Claude : les réglages à vérifier",
    desc="Ce qu'Anthropic fait de tes conversations, le réglage d'entraînement (5 ans ou 30 jours), le chat incognito, la mémoire, et la différence entre forfaits grand public et Team ou Enterprise.",
    og_pill="Les bases de l'IA · 24", og_titre="Tes données : les réglages à vérifier",
    marque="Les bases de l'IA · 24",
    h1="Tes données : <em>les réglages à vérifier</em>",
    chapo="Ce que tu montres à Claude part sur les serveurs d'Anthropic pour être traité, comme avec toute IA en ligne. La vraie question, c'est ce qu'il en fait ensuite. Sur les forfaits grand public, c'est un réglage. Voici lesquels vérifier.",
    verifie="16/10/2026",
    sources=[SRC_PRIVACY_REGLAGE_FR, SRC_CONDITIONS, SRC_PRIVACY_DUREE, SRC_PRIVACY_FAQ, SRC_PRIVACY_PRO, SRC_CC_DATA],
    corps="""
<section>
  <h2><span class="num">1</span>Le réglage d'entraînement</h2>
  <p>Il concerne les forfaits Gratuit, Pro et Max, y compris quand tu utilises Claude Code avec ces comptes. Oui, même sur le Pro.</p>
  <ol class="etapes">
    <li><b>Clique sur ton nom,</b> puis <b>Paramètres</b>.</li>
    <li><b>Ouvre Confidentialité.</b> Lien direct : claude.ai/settings/data-privacy-controls.</li>
    <li><b>Regarde l'interrupteur « Aider à améliorer nos modèles d'IA ».</b></li>
  </ol>
  <div class="encadre"><b>Activé</b>Tes nouvelles conversations et sessions de code peuvent servir à entraîner les prochains modèles. Elles sont conservées jusqu'à 5 ans, sous une forme qui ne te nomme pas.</div>
  <div class="encadre"><b>Désactivé</b>Tes nouvelles conversations ne servent pas à l'entraînement, et la conservation standard est de 30 jours. Ce qui a déjà servi à un entraînement en cours reste dedans.</div>
</section>

<section>
  <h2><span class="num">2</span>Les autres gestes à connaître</h2>
  <ul class="liste">
    <li><b>Le chat incognito.</b> L'icône fantôme en haut à droite d'une nouvelle conversation. Il ne sert jamais à l'entraînement, même si le réglage est activé, et rien ne va dans ta mémoire.</li>
    <li><b>La mémoire.</b> Paramètres, puis Mémoire : relis ce que Claude retient de toi. Le guide : <a href="/memoire">bien organiser la mémoire</a>.</li>
    <li><b>Les pouces.</b> Un pouce levé ou baissé envoie la conversation à Anthropic, qui garde ce retour 5 ans.</li>
    <li><b>Supprimer une conversation.</b> Elle disparaît de ton historique tout de suite, des serveurs sous 30 jours, et ne sert plus aux entraînements futurs.</li>
    <li><b>L'exception sécurité.</b> Une conversation signalée par les filtres de sécurité d'Anthropic peut être utilisée pour la sécurité, même réglage désactivé.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Team, Enterprise et API</h2>
  <p>Ces offres relèvent des conditions commerciales : par défaut, Anthropic n'entraîne pas ses modèles sur tes échanges. Exception : les pouces, qui peuvent transmettre la conversation liée. Les administrateurs d'une formule Team ou Enterprise peuvent les désactiver pour leurs membres.</p>
  <p class="note">Tu manipules des données clients, de santé ou couvertes par le secret professionnel ? C'est un argument pour une formule professionnelle, et pour bien régler ton compte avant de commencer.</p>
</section>

<section>
  <h2><span class="num">4</span>Ce qu'on ne colle pas</h2>
  <p>Même bien réglé, Anthropic recommande la prudence avec : les coordonnées bancaires, les dossiers médicaux, les mots de passe et identifiants, les documents confidentiels. Pour les clés et mots de passe, la méthode : <a href="/cle-api">où ranger une clé API</a>.</p>
</section>

<section>
  <div class="regle">
    <h2>Les 3 vérifications</h2>
    <ol class="etapes">
      <li><b>Confidentialité :</b> l'interrupteur d'entraînement, dans la position que tu as choisie.</li>
      <li><b>Mémoire :</b> rien dedans que tu ne veux pas voir retenu.</li>
      <li><b>Incognito :</b> pour toute question qui ne doit laisser aucune trace.</li>
    </ol>
  </div>
</section>
""",
)

# 25 · VS CODE
PAGES["vscode"] = dict(
    video="25 · VS Code",
    title="VS Code et Claude Code : quand tu en as besoin, et quand non",
    desc="VS Code et Claude Code ne sont pas concurrents. Ce que VS Code t'apporte vraiment, les cinq signaux qui disent qu'il est temps de l'installer, et comment brancher l'extension officielle.",
    og_pill="Les bases de l'IA · 25", og_titre="VS Code : quand tu en as besoin, et quand non",
    marque="Les bases de l'IA · 25",
    h1="VS Code : <em>quand tu en as besoin</em>, et quand non",
    chapo="Tu veux créer ton site avec l'IA, et on te dit d'installer VS Code ? Pour démarrer, ce n'est pas ce qu'il te faut. Ce qu'il te faut, c'est Claude Code. VS Code, c'est un éditeur gratuit qui affiche tes fichiers : utile plus tard, quand ton projet grossit.",
    verifie="23/10/2026",
    sources=[SRC_VSCODE_FAQ, SRC_CC_VSCODE],
    corps="""
<section>
  <div class="regle">
    <h2>Pour démarrer : l'appli Claude, onglet Code</h2>
    <ol class="etapes">
      <li><b>Télécharge l'appli Claude</b> sur claude.com/download, pour Mac ou Windows, et connecte-toi.</li>
      <li><b>Ouvre l'onglet Code</b> et choisis le dossier de ton projet sur ton ordinateur.</li>
      <li><b>Décris ce que tu veux</b>, en français. Claude Code crée et modifie les fichiers dans ce dossier.</li>
    </ol>
  </div>
  <p class="note">Claude Code demande un forfait payant (Pro ou Max). Pas de VS Code à installer pour ça.</p>
</section>

<section>
  <h2><span class="num">1</span>Deux outils, deux rôles</h2>
  <div class="encadre"><b>VS Code, l'atelier</b>Un éditeur de code de Microsoft, gratuit pour un usage privé comme professionnel, sur Mac, Windows et Linux.</div>
  <div class="encadre"><b>Claude Code, celui qui construit</b>Il tourne dans le terminal, dans l'appli Claude, ou dans VS Code grâce à l'extension officielle d'Anthropic.</div>
  <p>Le code produit est le même dans les trois cas. VS Code ne fait pas coder Claude mieux. Il te fait, toi, mieux voir et mieux piloter.</p>
</section>

<section>
  <h2><span class="num">2</span>Ce que l'extension t'apporte</h2>
  <ul class="liste">
    <li><b>Les modifications côte à côte.</b> L'original à gauche, sa proposition à droite.</li>
    <li><b>Accepter ou refuser chaque changement,</b> un par un.</li>
    <li><b>Relire et corriger son plan</b> avant qu'il passe à l'action.</li>
    <li><b>Lui montrer un fichier précis</b> avec @, même quelques lignes seulement.</li>
    <li><b>Plusieurs conversations en onglets,</b> une par chantier.</li>
  </ul>
</section>

<section>
  <h2><span class="num">3</span>Quand tu n'en as pas besoin</h2>
  <p>Pour démarrer, rien d'obligatoire. Moi-même, je travaille surtout en Claude Code direct. Tu peux t'en passer si :</p>
  <ul class="liste">
    <li>tu débutes,</li>
    <li>ton projet tient en quelques fichiers,</li>
    <li>tu fais surtout du texte, des documents, des tâches de bureau.</li>
  </ul>
</section>

<section>
  <h2><span class="num">4</span>Les 5 signaux pour passer à VS Code</h2>
  <p>Pas de chiffre magique. Tu passes à VS Code quand le projet ne tient plus dans ta tête :</p>
  <ul class="liste">
    <li><b>Une vraie arborescence,</b> des dizaines de fichiers rangés dans des dossiers.</li>
    <li><b>Tu ajustes du visuel</b> et tu relances le rendu dix fois.</li>
    <li><b>Tu commences à toucher le code toi-même,</b> même un petit réglage.</li>
    <li><b>Tu reviens sur le projet plusieurs jours de suite.</b></li>
    <li><b>Tu te perds :</b> tu ne sais plus où est quoi, ni ce qui a changé.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>L'installer en 3 étapes</h2>
    <ol class="etapes">
      <li><b>Télécharge VS Code</b> uniquement sur code.visualstudio.com. Il faut la version 1.94 ou plus récente.</li>
      <li><b>Ouvre les extensions</b> (Cmd + Maj + X sur Mac, Ctrl + Maj + X sur Windows), cherche « Claude Code », vérifie qu'il est publié par Anthropic, puis Installer.</li>
      <li><b>Clique sur l'icône en forme d'étincelle</b> en haut à droite d'un fichier ouvert, et connecte-toi avec ton compte Claude (forfait payant).</li>
    </ol>
  </div>
  <p class="note">Et pour mettre ton site en ligne une fois construit, c'est une autre étape : <a href="/publier-un-site">publier ton premier site</a>.</p>
</section>
""",
)

# 26 · VERCEL
PAGES["publier-un-site"] = dict(
    video="26 · Vercel",
    title="Publier ton premier site : le guide pas à pas",
    desc="Mettre ton site en ligne avec Vercel, pas à pas, avec Claude Code ou depuis GitHub. Le piège de l'offre gratuite pour un site d'entreprise, et les alternatives Netlify et Cloudflare.",
    og_pill="Les bases de l'IA · 26", og_titre="Publier ton premier site, pas à pas",
    marque="Les bases de l'IA · 26",
    h1="Publier ton <em>premier site</em>",
    chapo="Ton site marche sur ton ordinateur. Pour qu'il soit en ligne pour le monde entier, avec une vraie adresse, tu passes par un hébergeur comme Vercel. Voici le chemin le plus simple, et le piège à connaître si c'est le site de ton entreprise.",
    verifie="16/10/2026",
    sources=[SRC_VERCEL_START, SRC_VERCEL_DOMAINES, SRC_VERCEL_HOBBY, SRC_VERCEL_FAIR, SRC_NETLIFY, SRC_CLOUDFLARE],
    corps="""
<section>
  <h2>Ce que fait Vercel</h2>
  <p>Chaque mise en ligne reçoit automatiquement une adresse qui finit par .vercel.app, tirée du nom de ton projet. Toute personne à qui tu donnes le lien voit ton site. Ensuite, tu peux brancher ton propre nom de domaine dans les réglages du projet (Settings, puis Domains).</p>
  <div class="encadre"><b>Le piège : le gratuit, c'est pour le perso</b>L'offre gratuite de Vercel (Hobby) est réservée à un usage personnel et non commercial. Est commercial, par exemple, un site qui fait la promotion d'un produit ou d'un service, qui encaisse des paiements, qui affiche de la pub, ou que quelqu'un est payé pour créer. Le site de ton activité entre dans ce cas : il faut l'offre Pro, à 20 $ par développeur et par mois, hors taxes.</div>
</section>

<section>
  <h2><span class="num">1</span>Le plus simple : avec Claude Code</h2>
  <p>Ouvre Claude Code dans le dossier de ton site, et demande :</p>
  <pre><code>Publie ce site sur Vercel.
Installe ce qu'il faut, explique-moi chaque étape
avant de la lancer, et donne-moi l'adresse en ligne à la fin.</code></pre>
  <p>Il fera, en gros, ce que décrit la documentation de Vercel :</p>
  <pre><code>npm i -g vercel
vercel login
vercel
vercel --prod</code></pre>
  <p class="note">Installer l'outil, te connecter à ton compte Vercel, publier une version d'aperçu, puis la version définitive. Il faut Node.js 18 ou plus récent, Claude Code peut te l'installer.</p>
</section>

<section>
  <h2><span class="num">2</span>L'autre chemin : depuis GitHub</h2>
  <ol class="etapes">
    <li><b>Ton site est sur GitHub ?</b> Va sur vercel.com/new.</li>
    <li><b>Connecte ton compte GitHub,</b> choisis le dépôt, clique « Deploy ».</li>
    <li><b>C'est en ligne.</b> Et chaque modification envoyée sur GitHub remet le site à jour automatiquement.</li>
  </ol>
</section>

<section>
  <h2><span class="num">3</span>Les alternatives</h2>
  <ul class="liste">
    <li><b>Netlify Drop</b> (app.netlify.com/drop) : tu glisses le dossier de ton site, il est en ligne tout de suite, même sans compte. Sans compte, les fichiers sont publiés tels quels : si ton site doit être construit avant, dépose le dossier final (souvent dist ou build). Connecté, Netlify sait lancer la construction pour toi.</li>
    <li><b>Cloudflare</b> : sa documentation conseille désormais Workers plutôt que Pages pour un nouveau projet.</li>
  </ul>
</section>

<section>
  <div class="regle">
    <h2>Avant d'envoyer le lien</h2>
    <ol class="etapes">
      <li><b>Aucune clé ni mot de passe</b> dans les fichiers du site. Tout ce qui est publié est lisible. <a href="/cle-api" style="color:inherit">Où ranger une clé</a>.</li>
      <li><b>Le bon forfait</b> si le site sert ton activité.</li>
      <li><b>Ouvre l'adresse sur ton téléphone.</b> C'est là que la plupart des gens le verront.</li>
    </ol>
  </div>
</section>
""",
)

# 27 · PREMIÈRE AUTOMATISATION
PAGES["premiere-automatisation"] = dict(
    video="27 · Première automatisation",
    title="Ta première automatisation avec Claude : le guide pour te lancer",
    desc="Choisir la bonne tâche, la décrire comme à un nouvel assistant avec une trame prête à remplir, puis la faire tourner dans un Projet ou en tâche planifiée.",
    og_pill="Les bases de l'IA · 27", og_titre="Ta première automatisation : le guide",
    marque="Les bases de l'IA · 27",
    h1="Ta première <em>automatisation</em>",
    chapo="C'est le moment où l'IA arrête d'être un gadget. Une seule tâche, celle que tu répètes le plus, décrite une fois, précisément, comme si tu formais un nouvel assistant. Voici comment passer de l'idée à la tâche qui tourne.",
    verifie="16/10/2026",
    sources=[SRC_PROMPT, SRC_PROJETS, SRC_PLANIFIEES_FR],
    corps="""
<section>
  <h2><span class="num">1</span>Choisis la bonne tâche</h2>
  <p>Tes devis, tes relances, tes comptes rendus. La bonne candidate coche ces cases :</p>
  <ul class="liste">
    <li><b>Elle revient souvent,</b> chaque semaine ou plus.</li>
    <li><b>Elle suit toujours le même chemin.</b> Les mêmes étapes, le même format à la fin.</li>
    <li><b>Tu sais à quoi ressemble un bon résultat.</b> Tu en as déjà des exemples.</li>
    <li><b>Une erreur se rattrape.</b> Pour commencer, évite ce qui engage ta responsabilité sans relecture.</li>
  </ul>
  <p class="note">Le test : si tu peux l'expliquer à un stagiaire en dix minutes, Claude peut la faire.</p>
</section>

<section>
  <h2><span class="num">2</span>Décris-la comme à un nouvel assistant</h2>
  <p>La trame, à remplir une fois :</p>
  <pre><code>Tâche : [son nom]
Quand : [chaque lundi, à chaque nouvelle demande...]
Ce que je te donne : [mes notes, un tableau, le mail du client]
Ce que tu produis : [le format exact, la longueur, le ton]
Les règles : [ce qui ne doit jamais arriver]
Un exemple réussi : [colle un ancien résultat dont tu es content]</code></pre>
  <p>La dernière ligne compte plus que les autres. D'après Anthropic, un exemple est l'un des moyens les plus fiables d'obtenir le bon format et le bon ton. Les bases du prompt : <a href="/prompt">les trois règles</a>.</p>
</section>

<section>
  <h2><span class="num">3</span>Fais-la tourner</h2>
  <div class="encadre"><b>Niveau 1 : un Projet (même en gratuit)</b>Crée un projet, colle ta trame dans ses instructions, et ajoute tes modèles dans ses fichiers. Ensuite, chaque nouvelle conversation du projet, c'est la tâche faite en un message : tu colles les éléments du jour, Claude produit. Le gratuit permet jusqu'à 5 projets.</div>
  <div class="encadre"><b>Niveau 2 : une tâche planifiée (forfaits payants)</b>Pour une tâche qui doit tourner toute seule à heure fixe. Dans une conversation, décris la tâche et sa fréquence, réponds aux questions de Claude, vérifie, puis clique « Planifier ». Tu la retrouves dans « Planifiées », dans la barre latérale. Fréquences possibles : toutes les heures, chaque jour, chaque semaine, les jours de semaine, ou à la demande. Elle tourne à distance, même si ton ordinateur est en veille ou l'appli fermée, sauf si elle a besoin de fichiers ou d'applis de ton ordinateur.</div>
</section>

<section>
  <div class="regle">
    <h2>Les 3 règles pour te lancer</h2>
    <ol class="etapes">
      <li><b>Une tâche. Une seule.</b> La deuxième viendra quand la première tournera sans toi.</li>
      <li><b>Relis tout ce qui part chez un client,</b> au moins les premières fois. Tu restes responsable de ce qui sort.</li>
      <li><b>Note le temps avant et après.</b> La première fois qu'elle te rend une heure, tu ne reviens plus en arrière.</li>
    </ol>
  </div>
</section>
""",
)
