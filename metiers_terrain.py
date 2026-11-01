"""Contenu propre à chaque page métier : section « Sur le terrain » et questions fréquentes du métier.

Source : ~/ARDJ/content/FICHES-METIERS.md (audits réels, anonymisés).
Règles : aucun chiffre qui ne vienne d'un audit, aucun nom de client, aucune citation mot pour mot,
vouvoiement, zéro tiret cadratin, zéro point-virgule. Injecté par terrain_metiers.py.

Chaque entrée :
  titre   : h2 (le <em> est autorisé)
  intro   : le vrai point de douleur
  cas     : (ce qu'on met en place, concrètement, la limite qu'on vous dit)
  refus   : ce qu'on ne fera pas chez vous
  reperes : facultatif, chiffres d'audits réels (valeur, libellé), plus une note de source
  faq     : questions propres au métier (question, réponse)
"""

TERRAIN = {
    "avocat": {
        "titre": "Ce que l'IA fait dans un cabinet, <em>et ce qu'elle ne fait pas.</em>",
        "intro": "Dans un cabinet, le temps part dans l'écrit répétitif : relire, résumer, remettre en forme. Et la question qui bloque tout est la confidentialité, avant même l'efficacité.",
        "cas": [
            ("Un espace par dossier", "Les pièces du dossier sont lues une fois, puis vous l'interrogez en langage courant : qui a écrit quoi, à quelle date, ce qui manque.", "Elle ne connaît rien par elle-même. Elle relit ce que vous lui donnez, rien de plus."),
            ("La chronologie des pièces", "Des dizaines de pages deviennent une chronologie datée, avec la pièce source à chaque ligne.", "Elle peut inverser deux dates. La chronologie se vérifie avant d'être utilisée."),
            ("Le premier jet de courrier", "Mise en demeure, relance, note de synthèse, à partir de vos modèles et de votre façon d'écrire.", "Le fond reste votre responsabilité. Le premier jet fait gagner la forme, jamais le raisonnement."),
        ],
        "refus": [
            "Citer une jurisprudence sans l'avoir vérifiée à la source. Les outils d'IA inventent des références qui ont l'air vraies.",
            "Faire passer un dossier sensible par un outil dont on ne sait pas où il traite les données.",
        ],
        "faq": [
            ("L'IA peut-elle faire ma recherche juridique ?", "Elle peut dégrossir un sujet avant que vous ouvriez vos bases. Mais elle invente des références qui ont l'air vraies. On vous montre comment l'utiliser pour préparer, et la règle qu'on applique : aucune référence citée sans vérification à la source."),
            ("Où sont traitées les pièces de mes dossiers ?", "C'est la première chose qu'on décide avec vous. Selon la sensibilité, un traitement hébergé en Europe ou un outil qui tourne sur votre propre poste. Et une règle écrite de ce qui passe par l'outil et de ce qui n'y passe jamais."),
        ],
    },
    "comptable": {
        "titre": "Du volume, du répétitif, <em>et zéro droit à l'erreur.</em>",
        "intro": "Le temps perdu est dans les relances de pièces et la saisie. Ce sont des données clients : il faut savoir où elles passent, et pouvoir le prouver.",
        "cas": [
            ("La tâche montrée une fois", "Vous montrez une saisie ou un classement une fois, l'outil le refait sur tout le lot.", "On teste sur dix pièces avant d'en lancer mille. Une erreur répétée mille fois devient un incident."),
            ("Les documents remis en données", "PDF, Word et tableurs reçus des clients convertis en données propres, prêtes à contrôler.", "Un document scanné passe par une lecture automatique des caractères, moins fiable qu'un fichier natif."),
            ("Les relances qui partent seules", "Les retards repérés client par client, la relance préparée dans votre ton, envoyée après votre validation.", "Rien ne part sans un clic de votre part."),
        ],
        "refus": [
            "Toucher à la production comptable ou au calcul fiscal. La validation engage votre responsabilité, elle reste humaine.",
            "Automatiser sans garde-fou : chaque traitement garde une trace, et un échec déclenche une alerte.",
        ],
        "faq": [
            ("Et si l'automatisation se trompe sur un lot entier ?", "C'est pour ça qu'on ne lance jamais un lot sans test. Dix pièces d'abord, contrôlées par vous. Ensuite chaque passage garde une trace et vous prévient en cas d'échec, pour qu'une erreur ne se répète pas en silence."),
            ("Vous travaillez avec notre logiciel de production ?", "On ne le remplace pas et on ne le modifie pas. On travaille autour : les pièces qui arrivent, les relances, les courriers. Quand le logiciel permet un export ou une connexion, on s'en sert, sinon on part des fichiers que vous utilisez déjà."),
        ],
    },
    "batiment": {
        "titre": "Pas d'usine à gaz. <em>Deux outils, au plus.</em>",
        "intro": "Sur un chantier, le temps n'est pas perdu au bureau, il est volé le soir : les devis, les relances, les comptes rendus. Un artisan n'a pas besoin d'un système compliqué, il a besoin que ça marche depuis son téléphone.",
        "cas": [
            ("Le devis depuis la visite", "Vos notes, vos métrés ou un vocal pris sur place deviennent un devis rédigé, avec votre grille de prix.", "Les prix restent les vôtres. L'outil applique votre grille, il ne chiffre pas à votre place."),
            ("La relance au bon moment", "Les devis restés sans réponse sont relancés à date, dans votre ton.", "Un artisan se vend sur l'humain : le message reste le vôtre, relu avant de partir."),
            ("Les demandes triées", "Appels manqués et mails rangés par urgence, avec une réponse préparée.", "La réponse type sert de base. Un client qui a un problème mérite un vrai mot."),
        ],
        "refus": [
            "Vous vendre un site lourd et animé. Vos clients cherchent un numéro de téléphone sur leur mobile, la vitesse passe avant tout.",
            "Empiler les logiciels. Si une tâche demande un troisième outil, on cherche d'abord à s'en passer.",
        ],
        "faq": [
            ("Je fais tout depuis mon téléphone, ça marche quand même ?", "Oui, c'est le point de départ. Un vocal sur le chantier, et le devis ou le compte rendu est prêt quand vous rentrez. On installe tout pour qu'il se pilote depuis le téléphone."),
            ("L'IA va-t-elle fixer mes prix ?", "Non. Elle applique votre grille de prix et vos marges à vos métrés. Si un prix manque, elle vous le signale au lieu de l'inventer."),
        ],
    },
    "immobilier": {
        "titre": "Le métier où l'IA crée <em>le plus de risques.</em>",
        "intro": "Ce qui coûte, d'après le terrain : le même bien ressaisi dans plusieurs logiciels, le compte rendu de visite écrit de mémoire le soir, et le contact entrant qui refroidit faute d'être traité vite. Et c'est aussi le métier où une IA mal utilisée expose le plus l'agence.",
        "cas": [
            ("Le compte rendu de visite", "Le résumé de l'échange après la visite devient un compte rendu à votre trame, prêt pour le vendeur et pour votre logiciel.", "Ça doit rester simple pour toute l'équipe, sinon personne ne s'en sert. Relu avant envoi."),
            ("La fin de la ressaisie", "Un bien saisi une fois, reporté dans les autres outils, et la fiche client reconstituée depuis les pièces.", "On se branche à côté de votre logiciel métier, on ne le remplace pas. Souvent par export, quand il n'offre pas de connexion directe."),
            ("La demande d'estimation traitée tout de suite", "Le négociateur est prévenu dès l'arrivée du contact, avec un premier message prêt à partir.", "Rien ne part sans validation humaine. Mais la réponse est prête pendant que le vendeur attend encore."),
        ],
        "refus": [
            "La pige par aspiration des sites d'annonces. Leurs conditions d'utilisation l'interdisent.",
            "Une photo retouchée ou meublée virtuellement sans la mention qui le signale.",
            "Lire dans un dossier de location autre chose que les pièces que la loi autorise à demander.",
        ],
        "faq": [
            ("L'IA peut-elle analyser les dossiers de nos candidats locataires ?", "Elle peut vérifier qu'un dossier est complet et recouper les pièces entre elles en quelques minutes. Uniquement sur la liste des pièces que la réglementation autorise à demander, et la décision reste toujours humaine."),
            ("Nos négociateurs ne sont pas technophiles. Ça tiendra ?", "C'est le premier critère qu'on retient. Si un outil demande plus d'effort que la tâche qu'il remplace, il ne sera pas utilisé. On installe le minimum, sur ce que l'équipe fait déjà."),
        ],
    },
    "architecte": {
        "titre": "Ce que cinq audits d'agences <em>nous ont appris.</em>",
        "intro": "Nous avons audité cinq structures : agences en commande publique, architecte seul en maison individuelle, associés en commande mixte, maître d'œuvre récemment installée. Le temps ne part presque jamais dans la conception. Il part dans tout ce qui se refait à l'identique d'une opération à l'autre.",
        "reperes": {
            "items": [
                ("jusqu'à 5 jours", "pour un dossier d'appel d'offres en procédure adaptée, quand une simple candidature prend une demi-journée"),
                ("1 journée par mois", "pour pointer les situations de travaux contre les comptes rendus de chantier"),
                ("½ à 3 jours", "pour une proposition d'honoraires privée, souvent passés à collecter les éléments des bureaux d'études"),
                ("½ journée", "par diagnostic de site (urbanisme, patrimoine, archives), deux fois par mois chez des associés"),
            ],
            "note": "Durées données par les architectes eux-mêmes en audit, anonymisées.",
        },
        "cas": [
            ("Le dossier d'appel d'offres", "Mémoire, organigramme, répartition des missions : on réécrit dans vos mots à partir de vos dossiers déjà déposés, et on remet en page à la trame de chaque acheteur.", "Un mémoire repérable comme généré par une IA se paie en note. On part de votre écriture, jamais d'un texte neuf."),
            ("Le pointage des situations", "Ce que l'entreprise déclare, croisé ligne à ligne avec le compte rendu de chantier, et les écarts signalés.", "Le contrôle final reste le vôtre, c'est votre visa."),
            ("Le planning qui se recale", "Les fiches remplies par les entreprises au démarrage alimentent le planning, qui se recalcule quand une date bouge.", "L'estimation des durées de travaux n'est crédible que bâtie sur vos chantiers passés."),
        ],
        "refus": [
            "Concevoir à votre place ou produire des plans techniques réglementaires. Vous engagez votre responsabilité, ça reste chez vous.",
            "Brancher sur vos fichiers de production des outils non vérifiés trouvés en ligne.",
            "Vous parler de démarches en mairie comme d'un gouffre : avec le dépôt en ligne, c'est souvent un quart d'heure.",
        ],
        "faq": [
            ("Les acheteurs publics repèrent-ils les mémoires écrits par IA ?", "Certains disent les reconnaître à leurs tournures. C'est pour ça qu'on n'écrit pas de mémoire neuf : on part de vos mémoires déjà déposés et de votre façon d'écrire, et vous relisez tout."),
            ("Faut-il travailler en BIM ou sur maquette 3D ?", "Non. Une des agences que nous avons auditées travaille en 2D et refuse le BIM en connaissance de cause. On part de vos outils, quels qu'ils soient. Et si vous voulez montrer un projet, vos plans peuvent devenir une maquette 3D que votre client visite en ligne."),
        ],
    },
    "medical": {
        "titre": "L'administratif, oui. <em>Le dossier patient, jamais.</em>",
        "intro": "Un cabinet perd du temps au secrétariat, pas en consultation : rendez-vous, reprogrammations, courriers, questions qui reviennent. Mais une donnée de santé ne se traite pas comme une autre, et c'est par là qu'on commence.",
        "cas": [
            ("Les rappels qui réduisent les absences", "Un rappel avant chaque rendez-vous, avec un moyen simple d'annuler ou de déplacer.", "On s'appuie sur votre agenda existant. Si votre logiciel le fait déjà, on ne refait rien."),
            ("Les courriers aux confrères", "Vos modèles de courrier remis en forme et préparés, sans contenu médical saisi dans un outil externe.", "Le contenu médical reste rédigé par vous, dans vos outils."),
            ("Les questions administratives", "Horaires, documents à apporter, remboursements : des réponses prêtes, dans votre ton.", "Aucune réponse médicale. Une question de santé est toujours renvoyée vers vous."),
        ],
        "refus": [
            "Faire passer une donnée de santé par un outil qui n'est pas hébergé chez un hébergeur certifié pour les données de santé.",
            "Répondre à un patient sur une question médicale, même simple.",
        ],
        "faq": [
            ("Quels outils peut-on utiliser avec des données de santé ?", "En France, l'hébergement de données de santé exige un hébergeur certifié. C'est pour ça qu'on ne construit que sur l'administratif, qui ne contient aucune donnée de santé, et qu'on vérifie avec vous où chaque information est stockée."),
            ("Mon logiciel de gestion de cabinet fait déjà des rappels.", "Alors on ne touche pas aux rappels. On regarde ce qui reste à la main autour : courriers, questions récurrentes, documents manquants. Le chiffrage vous dit si ça vaut le coup, ou non."),
        ],
    },
    "traiteur": {
        "titre": "Ce que la salle ne voit pas : <em>la gestion d'après.</em>",
        "intro": "Chez un restaurateur que nous avons audité, la gestion une fois la salle fermée prenait une journée entière par semaine. En traiteur s'ajoute le devis : chaque demande est un brief différent, et un devis non relancé est une prestation perdue.",
        "reperes": {
            "items": [
                ("1 journée par semaine", "de gestion après fermeture chez un restaurateur audité, deux établissements"),
                ("environ 2 %", "de démarque seulement : tout était retravaillé. Les pertes n'étaient pas le problème"),
            ],
            "note": "Chiffres donnés par le dirigeant en audit, anonymisés.",
        },
        "cas": [
            ("Les pièces comptables rangées", "Les factures repérées dans la boîte mail, classées par mois, avec la liste de ce qui manque.", "Les factures qui ne vivent que sur le site d'un fournisseur restent à télécharger une fois par mois."),
            ("Le tableau du mois", "Chiffre de caisse, achats et coût matière comparés à votre plafond.", "Le coût matière global ne dit pas quel plat mange la marge. Pour ça, il faut vos fiches techniques."),
            ("La demande de groupe ou de privatisation", "Une réponse prête le jour même, adaptée à l'occasion, avec la disponibilité vérifiée.", "Le devis d'un mariage reste une discussion humaine."),
        ],
        "refus": [
            "Automatiser des commandes fournisseurs qui marchent déjà toutes seules. On ne touche pas à ce qui fonctionne.",
            "Publier une réponse à un avis sans votre relecture. Votre ton est ce que vos clients viennent chercher.",
        ],
        "faq": [
            ("On jette peu, est-ce que ça vaut quand même le coup ?", "Les pertes sont rarement le vrai gouffre. Chez le restaurateur que nous avons audité, la démarque était faible. Le temps partait dans la gestion du soir et les demandes de groupe. C'est là qu'on chiffre en premier."),
            ("Vous gérez les allergènes ?", "On prépare les étiquettes et la liste des allergènes depuis vos fiches techniques. La vérification reste la vôtre, c'est votre responsabilité envers le client."),
        ],
    },
    "garage": {
        "titre": "Le comptoir prend du temps <em>à l'atelier.</em>",
        "intro": "Dans un garage, l'écrit se fait au comptoir, entre deux clients : expliquer un devis, rappeler un entretien, répondre à une demande de rendez-vous. Chaque minute passée là est une minute de moins à l'atelier.",
        "cas": [
            ("Le devis expliqué", "Le devis ou l'ordre de réparation traduit en français clair pour le client : ce qui est urgent, ce qui peut attendre, pourquoi.", "Le diagnostic et le prix restent les vôtres. L'outil reformule, il ne diagnostique pas."),
            ("Les rappels d'entretien", "Révision, contrôle technique, pneus : un rappel envoyé au bon moment, client par client.", "Ça suppose que vos dates d'intervention soient notées quelque part. On part de ce que vous avez."),
            ("Le compte rendu d'intervention", "Ce qui a été fait, en quelques lignes claires, envoyé au client avec la facture.", "Relu par vous avant l'envoi, comme tout ce qui part à un client."),
        ],
        "refus": [
            "Remplacer votre logiciel de garage. On travaille à côté, par export quand il ne permet pas de connexion directe.",
            "Envoyer des relances commerciales en masse. Un rappel utile fidélise, un rappel insistant fait fuir.",
        ],
        "faq": [
            ("Mes clients ne lisent pas leurs mails.", "Alors on passe par le canal qu'ils lisent, souvent le SMS, avec un message court. Le canal se choisit selon votre clientèle, pas selon l'outil."),
            ("Ça demande de tout ressaisir ?", "Non. On part de ce que votre logiciel sait exporter : clients, véhicules, dates d'intervention. Si rien ne s'exporte, on vous le dit avant de commencer."),
        ],
    },
    "transport": {
        "titre": "Ce qu'un modèle de langage sait faire, <em>et ce qu'il ne sait pas faire.</em>",
        "intro": "Le temps part dans la paperasse : cotations, documents de transport, litiges, questions des donneurs d'ordre. Ce qu'on entend souvent, c'est que l'IA va optimiser les tournées. Ce n'est pas son travail.",
        "cas": [
            ("Les documents de transport lus", "Lettres de voiture, bons et preuves de livraison lus automatiquement, les données reportées là où il faut.", "Les quantités et les références se vérifient par un humain avant de faire foi."),
            ("La question « où en est ma livraison ? »", "Une réponse prête pour le donneur d'ordre, tirée de vos vraies données de suivi.", "Branchée sur vos données réelles uniquement. Sans elles, une IA invente une réponse plausible."),
            ("Le dossier de litige", "Le courrier, les pièces à joindre et les délais rappelés, dès que le litige est ouvert.", "Le fond du litige reste votre appréciation."),
        ],
        "refus": [
            "Vous promettre d'optimiser vos tournées. Votre logiciel d'exploitation le fait déjà avec un vrai calcul, un modèle de langage ne le remplace pas.",
            "Vous annoncer une connexion automatique à votre logiciel avant d'avoir vérifié qu'il le permet. Sur le terrain, beaucoup ne le permettent pas sans développement.",
        ],
        "faq": [
            ("L'IA peut-elle optimiser nos tournées ?", "Non, et méfiez-vous de qui le promet. L'optimisation de tournée est un calcul mathématique que votre logiciel d'exploitation fait déjà. L'IA travaille autour : lire, rédiger, classer, répondre."),
            ("Notre logiciel d'exploitation n'a pas de connexion ouverte.", "C'est fréquent. On le vérifie dès le premier échange, et si c'est le cas on part de ses exports, ou on vous chiffre un connecteur sur mesure. Vous savez le coût avant de vous engager."),
        ],
    },
    "camping": {
        "titre": "La saison ne laisse pas <em>le temps d'apprendre.</em>",
        "intro": "En camping comme en hôtellerie, tout arrive en même temps : les avis, les réservations, les clients étrangers, le planning. Ce qui s'installe, s'installe avant la saison.",
        "cas": [
            ("Les réponses aux avis", "Une réponse préparée pour chaque avis, dans votre ton, y compris pour les mauvais.", "Une réponse automatique à un avis négatif fait pire que pas de réponse. Elle est relue et ajustée par vous."),
            ("Les descriptifs traduits", "Hébergements, règlement, informations d'arrivée, traduits pour votre clientèle étrangère.", "Une traduction se relit au moins une fois par quelqu'un qui parle la langue, surtout sur le règlement."),
            ("La taxe de séjour", "La déclaration préparée depuis votre registre des nuitées.", "Les montants se contrôlent avant envoi. C'est vous qui déclarez."),
        ],
        "refus": [
            "Écrire de faux avis ou en solliciter contre une contrepartie. C'est interdit et ça se repère.",
            "Installer un nouvel outil en pleine saison. On prépare hors saison, ou on attend.",
        ],
        "faq": [
            ("C'est trop tard pour cette saison ?", "Une tâche simple, comme les réponses aux avis ou les mails de pré-séjour, s'installe en une séance. Le reste se prépare à l'intersaison, pour être prêt avant l'ouverture."),
            ("Le planning du personnel aussi ?", "On prépare le planning et on le vérifie contre les règles de repos que vous appliquez. La décision et la validation restent les vôtres."),
        ],
    },
    "recrutement": {
        "titre": "Trier des CV avec une IA, <em>c'est encadré.</em>",
        "intro": "Le temps part dans le tri, les comptes rendus et les réponses aux candidats. Mais l'IA appliquée au recrutement est classée à haut risque par le règlement européen sur l'IA, et un candidat a le droit de ne pas être écarté par une machine seule.",
        "cas": [
            ("Le résumé des CV", "Chaque CV résumé face aux critères du poste que vous avez définis, avec les points à vérifier en entretien.", "C'est une aide à la lecture. La décision d'écarter ou de retenir reste humaine, toujours."),
            ("Le compte rendu d'entretien", "Vos notes ou un vocal après l'entretien deviennent un compte rendu à votre trame.", "On prévient le candidat avant tout enregistrement."),
            ("La réponse à chaque candidat", "Une réponse personnalisée aux candidats non retenus, préparée en quelques secondes.", "Relue avant envoi. Une réponse soignée fait partie de votre marque employeur."),
        ],
        "refus": [
            "Écarter un candidat automatiquement, sans regard humain sur sa candidature.",
            "Utiliser des critères que la loi interdit, même indirectement : âge, origine, situation de famille.",
        ],
        "faq": [
            ("Est-ce légal d'utiliser l'IA pour présélectionner ?", "L'aide au tri l'est, avec des règles : critères liés au poste, transparence envers les candidats, et une décision qui reste humaine. Le règlement européen sur l'IA classe ces usages à haut risque. On met en place ce cadre avec vous, par écrit."),
            ("Les CV de nos candidats sortent-ils de nos outils ?", "On choisit avec vous des outils qui ne réutilisent pas les données, et on ne garde rien de notre côté. Les CV restent dans vos outils."),
        ],
    },
    "communication": {
        "titre": "On ne touche pas à la créa. <em>On prend ce qui l'étouffe.</em>",
        "intro": "Dans une agence, l'administratif se répète à l'identique d'un client à l'autre : reportings, comptes rendus, relances de validation, déclinaisons. Rarement facturé à son vrai prix.",
        "cas": [
            ("Le reporting du mois", "Les chiffres de chaque client rassemblés et mis en forme au même format, avec le commentaire préparé.", "Le commentaire stratégique reste le vôtre. L'outil prépare, vous interprétez."),
            ("La déclinaison par plateforme", "Un message décliné aux formats de chaque réseau, avec les contraintes de longueur respectées.", "Pas de déclinaison sans votre ligne éditoriale écrite. Sinon, tout finit par se ressembler."),
            ("La relance de validation", "Le client relancé au bon moment, avec ce qu'il doit valider et la date limite.", "Le ton s'adapte à chaque client, vous gardez la main."),
        ],
        "refus": [
            "Produire de la créa générique à votre place. Votre différence est ce que vos clients paient.",
            "Utiliser des visuels générés sans vérifier les droits et sans le signaler quand c'est nécessaire.",
        ],
        "faq": [
            ("Nos clients doivent-ils savoir qu'on utilise l'IA ?", "Ça dépend de l'usage et de vos contrats. On regarde avec vous ce qui doit être dit, et à qui. Un reporting préparé par un outil n'a pas le même statut qu'un visuel généré."),
            ("Et pour les appels d'offres d'agence ?", "On part de vos recommandations déjà gagnées pour préparer la structure et les blocs qui reviennent. La stratégie et l'angle restent les vôtres."),
        ],
    },
    "commercial": {
        "titre": "Le métier où l'on vend <em>le plus de solutions illégales.</em>",
        "intro": "Prospection, relances, comptes rendus : tout ce qui éloigne du terrain. C'est aussi le domaine où l'on voit passer le plus d'offres d'automatisation qui ne respectent ni la loi ni les conditions des plateformes.",
        "cas": [
            ("La préparation du rendez-vous", "Une synthèse sur l'entreprise avant l'appel : activité, actualité, ce qui a déjà été échangé.", "À partir de sources publiques et de votre historique, uniquement."),
            ("Le compte rendu dicté", "Un vocal en sortant du rendez-vous devient un compte rendu, et votre suivi se met à jour.", "Si vous enregistrez un échange, on prévient la personne et on obtient son accord avant."),
            ("La relance au bon moment", "Les échanges restés sans suite repérés, la relance préparée et personnalisée.", "L'envoi reste manuel. Une relance automatique se sent, et elle abîme la relation."),
        ],
        "refus": [
            "Aspirer des profils sur les réseaux professionnels. C'est contraire au RGPD et aux conditions des plateformes, et les comptes finissent bannis.",
            "Envoyer des messages en masse. On cible sur des données publiques officielles, et on écrit à moins de gens, mieux.",
        ],
        "faq": [
            ("D'où viennent les listes de prospects, alors ?", "De données publiques officielles, comme le répertoire des entreprises, croisées avec votre connaissance du terrain. Moins de contacts, mieux choisis, et dans les règles."),
            ("Puis-je enregistrer mes appels pour les comptes rendus ?", "Oui, à condition de prévenir votre interlocuteur et d'obtenir son accord avant. Sinon, un vocal dicté juste après l'appel fait le même travail sans enregistrer personne."),
        ],
    },
    "solo": {
        "titre": "Seul à tout faire : <em>ce qu'on a mesuré.</em>",
        "intro": "Nous avons audité des indépendants seuls, dans des métiers très différents. Le constat revient à chaque fois : le cœur du métier est aimé, c'est tout ce qui l'entoure qui déborde sur les soirées.",
        "reperes": {
            "items": [
                ("3 à 4 h", "pour ressaisir un devis de travaux à la main chez un concepteur paysagiste seul, par dossier signé"),
                ("environ 1 h par jour", "d'administratif pour ce même indépendant"),
                ("jusqu'à 1 journée", "pour les visuels de présentation d'un dossier complexe chez une maître d'œuvre installée depuis moins d'un an"),
            ],
            "note": "Durées données par les indépendants eux-mêmes en audit, anonymisées.",
        },
        "cas": [
            ("Une base au lieu de la ressaisie", "Vos prestations, vos fournisseurs et vos prix réunis une fois, le devis se compose depuis cette base.", "Les prix bougent. La base se met à jour, sinon le devis se trompe."),
            ("La dictée qui sort propre", "Vous dictez, le texte sort mis en forme dans votre style, vous relisez au lieu de réécrire.", "La relecture reste, surtout pour ce qui vous engage."),
            ("Les mails qui reviennent", "Les réponses que vous écrivez toujours, préparées à partir de vos réponses passées.", "Rien ne part sans vous."),
        ],
        "refus": [
            "Vous vendre un système que vous n'aurez pas le temps de faire tourner. On commence par une seule tâche.",
            "Vous promettre de gros gains si vous débutez : sans volume, on installe d'abord la méthode, avant que le volume arrive.",
        ],
        "faq": [
            ("Je n'ai pas de durées moyennes à donner.", "C'est normal quand on débute. On part de votre dernier dossier, pas d'une moyenne. Le chiffrage sera plus modeste, et il sera juste."),
            ("Par quoi commencer quand on est seul ?", "Par la tâche qui revient le plus souvent et que vous aimez le moins. Une seule, installée et utilisée, vaut mieux que cinq à moitié."),
        ],
    },
}
