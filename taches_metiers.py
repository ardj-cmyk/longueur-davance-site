# -*- coding: utf-8 -*-
"""Listes de taches etendues, pretes pour les cases a cocher.

Principe : on affiche la liste realiste complete et c'est le client qui decoche.
Un chiffre qu'il a construit lui-meme ne se negocie plus ; un chiffre annonce, si.
Regle absolue : on charge en NOMBRE DE TACHES REELLES, jamais en heures par tache.

Chaque entree : (libelle, poids, coche_par_defaut, code catalogue)
  poids 5 = (2,5-4,0 h/sem) tache qui domine a elle seule la semaine du metier
        4 = (1,0-2,0)   3 = (0,6-1,2)   2 = (0,3-0,7)   1 = (0,15-0,4)
Decoche par defaut = ne concerne pas tout le monde (pas de site, pas de salaries,
pas de presence sociale). Sinon le total ment des l'ouverture de la page.
"""

TACHES = {

"batiment": [
 ("le devis chiffré depuis vos notes, vos métrés ou un vocal pris sur place", 5, True,  "B1"),
 ("la relance des devis restés sans réponse, au bon moment",                  3, True,  "B2"),
 ("la facture de situation et la relance des impayés",                        3, True,  "B6"),
 ("les demandes entrantes, triées et pré-répondues",                          2, True,  "B5"),
 ("le compte rendu de chantier dicté à la voix",                              3, True,  "B3"),
 ("le métré calculé depuis les surfaces relevées",                            3, True,  "M1"),
 ("le comparatif des devis fournisseurs, ligne à ligne",                      2, True,  "M2"),
 ("le temps de main-d'œuvre estimé avant de s'engager",                       2, True,  "M4"),
 ("le rétroplanning des commandes de matériaux",                              2, True,  "M5"),
 ("les mails qui reviennent toujours, écrits depuis vos réponses passées",    3, True,  "S1"),
 ("le dossier administratif de chantier et ses pièces",                       2, True,  "B8"),
 ("le rappel de fin de chantier et la demande d'avis",                        1, True,  "B4"),
 ("votre fiche Google remplie et vivante",                                    1, False, "—"),
 ("vos chantiers filmés découpés en clips sous-titrés",                       2, False, "PB2"),
],

"garage": [
 ("le devis et l'ordre de réparation, rédigés depuis vos constats",           5, True,  "G1"),
 ("l'explication de la réparation, en français, au client",                   3, True,  "G5"),
 ("le devis refusé, relancé une fois proprement",                             3, True,  "G7"),
 ("les rappels d'entretien périodique, client par client",                    3, True,  "G2"),
 ("les rappels de contrôle technique",                                        2, True,  "G3"),
 ("les rappels de rendez-vous, pour les oublis",                              2, True,  "G4"),
 ("le suivi des commandes de pièces",                                         3, True,  "G6"),
 ("la demande d'avis après intervention",                                     2, True,  "G8"),
 ("les appels et messages qui posent toujours la même question",              3, True,  "S7"),
 ("la facture et sa relance",                                                 2, True,  "S8"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("les réponses aux avis en ligne, y compris les mauvais",                    2, False, "S7"),
],

"camping": [
 ("les réponses aux demandes de réservation",                                 4, True,  "CA1"),
 ("les mails d'avant-séjour, envoyés au bon moment",                          3, True,  "CA2"),
 ("la relance des acomptes et des soldes",                                    3, True,  "CA3"),
 ("les questions qui reviennent chaque saison",                               3, True,  "CA4"),
 ("le planning du staff, pré-rempli et vérifié contre les règles de repos",   4, False, "CA9"),
 ("la déclaration de taxe de séjour depuis le registre des nuitées",          3, True,  "CA10"),
 ("le planning des arrivées et des départs du jour",                          2, True,  "CA7"),
 ("le message d'après-séjour et la demande d'avis",                           2, True,  "CA5"),
 ("les réponses aux avis en ligne, une par une",                              3, True,  "CA6"),
 ("la relance des réservataires de l'an dernier",                             2, True,  "CA8"),
 ("les descriptifs traduits pour la clientèle étrangère",                     2, True,  "S1"),
 ("la lettre d'information avant l'ouverture de saison",                      2, False, "S11"),
],

"avocat": [
 ("les courriers au confrère, au notaire, à l'expert",                        5, True,  "A1"),
 ("la synthèse d'un dossier avant rendez-vous ou audience",                   4, True,  "A2"),
 ("la synthèse des pièces adverses",                                          3, True,  "A4"),
 ("le bordereau de pièces",                                                   3, True,  "A3"),
 ("les relances de documents manquants",                                      3, True,  "S2"),
 ("le suivi des délais de procédure",                                         3, True,  "A6"),
 ("l'accueil d'un nouveau dossier et ses pièces",                             2, True,  "A8"),
 ("la note d'honoraires expliquée",                                           2, True,  "A7"),
 ("la veille jurisprudentielle sur vos matières",                             3, True,  "A5"),
 ("les questions que les clients posent tous les mois",                       2, True,  "S7"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("la lettre d'information aux clients, tirée de votre veille",               2, False, "S11"),
],

"comptable": [
 ("les relances de pièces manquantes, client par client",                     5, True,  "C1"),
 ("le traitement des documents reçus en masse",                               4, True,  "C3"),
 ("les courriers et mails types au client",                                   3, True,  "C2"),
 ("la préparation du rendez-vous bilan",                                      3, True,  "C6"),
 ("la note qui explique un bilan en français",                                3, True,  "C4"),
 ("le suivi des échéances déclaratives",                                      3, True,  "C5"),
 ("les réponses aux questions fiscales courantes",                            3, True,  "C7"),
 ("l'accueil d'un nouveau client et sa collecte de pièces",                   2, True,  "C8"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("la facture et sa relance",                                                 2, True,  "S8"),
 ("la veille fiscale, filtrée et sourcée",                                    2, True,  "S10"),
 ("la lettre d'information mensuelle, tirée du calendrier fiscal",            2, False, "S11"),
],

"immobilier": [
 ("l'annonce rédigée depuis les caractéristiques du bien",                    4, True,  "I1"),
 ("le compte rendu de visite envoyé au vendeur le soir même",                 4, True,  "I2"),
 ("le tri et la qualification des demandes entrantes",                        3, True,  "I3"),
 ("la déclinaison de l'annonce pour chaque portail",                          3, True,  "I1"),
 ("les photos d'un bien vide meublées virtuellement, mention comprise",       3, True,  "I9"),
 ("les photos transformées en clip vertical pour les réseaux",                2, True,  "I10"),
 ("le rapprochement entre les acheteurs du fichier et les biens",             3, True,  "I4"),
 ("le dossier de vente et ses pièces",                                        3, True,  "I6"),
 ("le contrôle des dossiers de location",                                     3, True,  "I12"),
 ("l'estimation documentée et ses comparables",                               3, True,  "I7"),
 ("le point vendeur et le suivi du mandat",                                   2, True,  "I5"),
 ("la relance des anciens contacts du fichier",                               2, True,  "I8"),
 ("le kit de publication à chaque nouveau mandat",                            2, False, "I11"),
 ("votre présence d'agent : visites et vocaux découpés en clips",             2, False, "PB2"),
],

"architecte": [
 ("le compte rendu de réunion de chantier",                                   5, True,  "AR1"),
 ("le dépouillement des offres d'entreprises",                                4, True,  "AR2"),
 ("la notice descriptive et le CCTP",                                         4, True,  "AR3"),
 ("le quantitatif sorti de la maquette",                                      3, True,  "AR12"),
 ("le contrôle de cohérence de la maquette",                                  3, True,  "AR11"),
 ("le placement des vues sur les feuilles",                                   3, True,  "AR10"),
 ("les scripts qui automatisent vos tâches répétitives dans le logiciel",     3, True,  "AR9"),
 ("la lecture ciblée du PLU d'une commune",                                   3, True,  "AR4"),
 ("le mémoire technique de réponse à concours",                              3, True,  "AR5"),
 ("le suivi des situations de travaux",                                       2, True,  "AR7"),
 ("les courriers d'affaire récurrents",                                       2, True,  "AR6"),
 ("la fiche de synthèse projet",                                              2, True,  "AR8"),
],

"recrutement": [
 ("le tri et le résumé des candidatures reçues",                              5, True,  "R2"),
 ("les comptes rendus d'entretien",                                           4, True,  "R3"),
 ("la fiche de poste écrite depuis un brief oral",                            3, True,  "R1"),
 ("la synthèse de candidature envoyée au client",                             3, True,  "R4"),
 ("les réponses aux candidats non retenus, personnalisées",                   3, True,  "R5"),
 ("la relance des candidats en cours de process",                             3, True,  "R6"),
 ("le point d'avancement au client",                                          2, True,  "R7"),
 ("la reprise du vivier sur un nouveau poste",                                3, True,  "R8"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("les mails qui reviennent toujours",                                        2, True,  "S1"),
 ("votre présence LinkedIn, alimentée par vos entretiens",                    2, False, "PB3"),
 ("la lettre d'information, une pour les candidats, une pour les clients",    2, False, "S11"),
],

"commercial": [
 ("la préparation de la tournée : qui, où on en était, ce qui a été promis",  4, True,  "CO1"),
 ("le débrief dicté en sortant du rendez-vous",                               4, True,  "CO2"),
 ("les relances de prospects, au bon moment et sans oubli",                   4, True,  "CO3"),
 ("les mails de prospection personnalisés, pas les copiés-collés",            3, True,  "CO4"),
 ("la mise à jour du suivi après chaque échange",                             3, True,  "CO5"),
 ("le devis rédigé depuis vos notes",                                         3, True,  "S5"),
 ("les réponses aux questions qui reviennent toujours",                       2, True,  "S7"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("le résumé d'un document long avant de décider",                            2, True,  "S4"),
 ("la veille de votre secteur, filtrée et sourcée",                           2, True,  "S10"),
 ("vos vidéos et vos vocaux découpés en posts",                               2, False, "PB2"),
 ("la lettre d'information à votre fichier",                                  2, False, "S11"),
],

"solo": [
 ("les devis rédigés depuis vos notes",                                       4, True,  "S5"),
 ("les factures et leurs relances",                                           4, True,  "S8"),
 ("la relance de tout ce qui n'a pas eu de réponse",                          3, True,  "S2"),
 ("les mails qui reviennent toujours",                                        3, True,  "S1"),
 ("les comptes rendus depuis une note vocale",                                3, True,  "S3"),
 ("le tri de la boîte de réception",                                          3, True,  "S6"),
 ("les réponses aux questions qui reviennent toujours",                       3, True,  "S7"),
 ("le suivi de ce qui est en cours",                                          2, True,  "S9"),
 ("le résumé d'un document long avant de décider",                            2, True,  "S4"),
 ("la veille de votre secteur, filtrée et sourcée",                           2, True,  "S10"),
 ("vos vidéos et vos vocaux découpés en posts",                               2, False, "PB2"),
 ("la lettre d'information à vos clients",                                    2, False, "S11"),
],

"communication": [
 ("les reportings clients, mois après mois, au même format",                  4, True,  "S1"),
 ("le montage : une prise de vue découpée en clips sous-titrés",              4, True,  "PB2"),
 ("les comptes rendus de réunion et les relevés de décisions",                4, True,  "S3"),
 ("les calendriers éditoriaux et les déclinaisons par plateforme",            3, True,  "PB4"),
 ("les textes tirés de ce qui a déjà été dit en vidéo",                       3, True,  "PB3"),
 ("les relances de validation, côté client",                                  3, True,  "S2"),
 ("les réponses aux appels d'offres et les recommandations",                  3, True,  "S4"),
 ("les réponses aux commentaires et aux messages privés",                     3, True,  "PB5"),
 ("le tri de la boîte de réception",                                          2, True,  "S6"),
 ("la facture et sa relance",                                                 2, True,  "S8"),
 ("le suivi de ce qui est en cours, client par client",                       2, True,  "S9"),
 ("la lettre d'information de l'agence",                                      2, False, "S11"),
],

"medical": [
 ("les courriers types au confrère et au correspondant",                      4, True,  "S1"),
 ("les comptes rendus dictés à la voix",                                      4, True,  "S3"),
 ("les rappels de rendez-vous et la réduction des oublis",                    3, True,  "S2"),
 ("les réponses aux questions que les patients posent tous les jours",        3, True,  "S7"),
 ("le tri des messages et des demandes entrantes",                            3, True,  "S6"),
 ("la préparation d'une consultation depuis le dossier",                      3, True,  "S4"),
 ("les relances de documents manquants",                                      2, True,  "S2"),
 ("la facturation et son suivi",                                              2, True,  "S8"),
 ("le suivi de ce qui est en cours",                                          2, True,  "S9"),
 ("la veille de votre spécialité, filtrée et sourcée",                        2, True,  "S10"),
],
}
