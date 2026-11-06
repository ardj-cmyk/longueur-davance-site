/* Plan perso du potager : toutes les données chiffrées, chacune avec sa source.
   Aucune donnée inventée : la base est le modèle 2 personnes publié sur /potager
   (recherche du 05 et 06/11/2026, détail dans PISTE.md). Les quantités pour N personnes
   sont la règle de trois de ce modèle. Les hypothèses sont marquées « hypothese ». */
(function () {
  var S = {
    jardin30: { t: "un-jardin-bio.com, surfaces pour 30 familles (consommation d'une famille de 4, rendements à l'are)", u: "https://www.un-jardin-bio.com/wp-content/uploads/filebase/doc-pdf-espace-privilege/maraichage/surfaces-cultures-30familles.pdf" },
    ciqual: { t: "Ciqual ANSES 2020", u: "https://www.data.gouv.fr/datasets/table-de-composition-nutritionnelle-des-aliments-ciqual-2020" },
    usdaCourge: { t: "USDA FoodData Central, courge butternut crue (fdcId 169295)", u: "https://fdc.nal.usda.gov/food-details/169295/nutrients" },
    anses: { t: "ANSES 2016, repères nutritionnels (2 600 kcal par jour pour un homme, 2 100 pour une femme)", u: "https://www.anses.fr/fr/system/files/NUT2012SA0103Ra-1.pdf" },
    jeavons: { t: "Ecology Action, FAQ calories 2019 (environ 232 m² par personne, allées comprises)", u: "https://growbiointensive.org/Enewsletter/Summer2019/caloriesFAQ.html" },
    vetagro: { t: "VetAgro Sup, chaire bien-être animal, juin 2025", u: "https://chaire-bea.vetagro-sup.fr/wp-content/uploads/2025/06/25-06-Une-poule-pond-elle-un-oeuf-par-jour.pdf" },
    m2a: { t: "Guide de l'adoptant de poules, Mulhouse Alsace Agglomération, 2026", u: "https://www.m2a.fr/wp-content/uploads/2026/04/Guide-de-ladoptant-poules-m2A-2026.pdf" },
    legifrance: { t: "Arrêté du 25 septembre 2023, article 51 (Légifrance)", u: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048110961" },
    pdtFiche: { t: "jardiner-malin, pomme de terre", u: "https://www.jardiner-malin.fr/fiche/pomme-de-terre.html" },
    yu: { t: "Yu et al. 2015, Field Crops Research, méta-analyse des cultures associées (en moyenne autant de récolte sur environ 18 % de terrain en moins, gain plus fort quand les cultures n'occupent pas la terre au même moment)", u: "https://doi.org/10.1016/j.fcr.2015.09.010" }
  };

  function jm(f) { return "https://www.jardiner-malin.fr/fiche/" + f + ".html"; }

  /* Cultures rapides (moins d'un an). base2 = modèle 2 personnes de /potager.
     kg2 : kg par an pour 2, m2 : surface en culture extensive pour 2, kcal : pour 100 g,
     besoin2 : semences ou plants pour 2, achat : sachet ou lot le moins cher (bas) et bio ou plus fourni (haut),
     recolte : mois de récolte (1 = janvier). */
  var CULTURES = [
    { id: "pomme_de_terre", nom: "Pomme de terre", kg2: 48, m2: 19.2, kcal: 80.5, kcalSrc: "ciqual",
      besoin2: 85, unite: "plants", achat: {
        bas: { prix: 6.99, qte: 25, lib: "étui de 25 plants Celtiane", u: "https://www.truffaut.com/pomme-terre-celtiane-calibre-25-32-etui-25-plants-543477.html" },
        haut: { prix: 3.99, qte: 10, lib: "filet de 10 plants Charlotte", u: "https://www.truffaut.com/pomme-terre-charlotte-filet-10-plants-319468.html" } },
      delai: "80 jours en primeur, à maturité quand le feuillage a jauni", recolte: [5, 6, 7, 9, 10, 11],
      plantation: "au printemps",
      garde: "À l'abri de la lumière, au sec, au frais, aéré", src: [jm("pomme-de-terre"), "https://www.truffaut.com/pomme-terre-celtiane-calibre-25-32-etui-25-plants-543477.html"] },
    { id: "courge", nom: "Courge butternut", kg2: 30, m2: 7.5, kcal: 45, kcalSrc: "usdaCourge",
      besoin2: 1.1, unite: "g", achat: {
        bas: { prix: 2.79, qte: 3, lib: "sachet de 3 g", u: "https://www.truffaut.com/courge-butternut-en-sachet-726048.html" },
        haut: { prix: 3.69, qte: 2, lib: "sachet bio de 2 g", u: "https://www.truffaut.com/courge-musquee-waltham-butternut-bio-858956.html" } },
      delai: "110 à 120 jours", recolte: [9, 10, 11, 12],
      garde: "Jusqu'en mars dans une pièce à 12 à 15 °C, après 10 jours de séchage à 20 °C", src: [jm("courge")] },
    { id: "oignon", nom: "Oignon (bulbilles)", kg2: 21, m2: 7.0, kcal: 37.8, kcalSrc: "ciqual",
      besoin2: 700, unite: "g", achat: {
        bas: { prix: 6.90, qte: 500, lib: "500 g de bulbilles", u: "https://www.truffaut.com/shakespeare-bulbes-oignons-a-repiquer-500-gr.html" },
        haut: { prix: 6.90, qte: 500, lib: "500 g de bulbilles (seule offre trouvée)", u: "https://www.truffaut.com/shakespeare-bulbes-oignons-a-repiquer-500-gr.html" } },
      delai: "3 à 6 mois", recolte: [7, 8, 9], plantation: "en mars-avril",
      garde: "Séché 2 à 3 semaines, puis 6 à 8 mois près de 0 °C, sans gel", src: [jm("oignon")] },
    { id: "haricot_vert", nom: "Haricot vert", kg2: 9, m2: 6.0, kcal: 28, kcalSrc: "ciqual",
      besoin2: 120, unite: "g", achat: {
        bas: { prix: 5.69, qte: 200, lib: "boîte de 200 g", u: "https://www.truffaut.com/haricot-nain-mangetout-contender-boite-200g-726194.html" },
        haut: { prix: 5.99, qte: 50, lib: "sachet bio de 50 g", u: "https://www.truffaut.com/graines-potageres-haricot-vert-nain-rugally-bio-696462.html" } },
      delai: "60 à 70 jours", recolte: [6, 7, 8, 9],
      garde: "Une semaine au frais", src: ["https://www.truffaut.com/graines-de-haricot-nain-vert-signal-bio-5-metres.html"] },
    { id: "carotte", nom: "Carotte", kg2: 26, m2: 5.2, kcal: 40.2, kcalSrc: "ciqual",
      besoin2: 1.6, unite: "g", achat: {
        bas: { prix: 2.79, qte: 4, lib: "sachet de 4 g", u: "https://www.truffaut.com/carotte-touchon-en-sachet-726041.html" },
        haut: { prix: 3.69, qte: 2, lib: "sachet bio de 2 g", u: "https://www.truffaut.com/carotte-berlikumer-2-g-726128.html" } },
      delai: "90 à 100 jours", recolte: [7, 8, 9, 10, 11, 12],
      garde: "4 à 5 mois en caisse de sable, pièce à 0 à 4 °C", src: ["https://www.truffaut.com/vilmorin-carotte-nantaise-amelioree-3.html", jm("carotte-chantenay-conservation")] },
    { id: "poireau", nom: "Poireau", kg2: 13, m2: 5.2, kcal: 32.3, kcalSrc: "ciqual",
      besoin2: 2.6, unite: "g", achat: {
        bas: { prix: 1.79, qte: 3, lib: "sachet de 3 g", u: "https://www.truffaut.com/poireau-monstrueux-carentan-2-en-sachet-726028.html" },
        haut: { prix: 3.79, qte: 1.3, lib: "sachet bio de 1,3 g", u: "https://www.truffaut.com/graines-potageres-poireau-carentan-bio-1-3g-822976.html" } },
      delai: "semé de mars à mai, récolté de septembre à mars selon la variété", recolte: [9, 10, 11, 12, 1, 2, 3], plantation: "semis de mars à mai",
      garde: "Reste en terre l'hiver", src: [jm("poireau")] },
    { id: "ail", nom: "Ail", kg2: 3, m2: 4.3, kcal: 111, kcalSrc: "ciqual",
      besoin2: 430, unite: "g", achat: {
        bas: { prix: 9.49, qte: 500, lib: "500 g de caïeux", u: "https://www.truffaut.com/ail-edenrose-500-g.html" },
        haut: { prix: 9.90, qte: 500, lib: "500 g d'ail violet", u: "https://www.truffaut.com/germidour-violet-ail-a-repiquer-500gr.html" } },
      delai: "récolte quand le feuillage jaunit", recolte: [6, 7, 8],
      garde: "En tresses, au sec, à l'obscurité, jamais au frigo", src: [jm("ail")] },
    { id: "chou", nom: "Chou pommé", kg2: 20, m2: 2.9, kcal: 36.5, kcalSrc: "ciqual",
      besoin2: 0.1, unite: "g", achat: {
        bas: { prix: 1.99, qte: null, lib: "sachet Vilmorin (grammage non affiché, un sachet compté)", u: "https://www.truffaut.com/vilmorin-chou-cabus-de-brunswick.html" },
        haut: { prix: 3.50, qte: 2, lib: "sachet de 2 g", u: "https://www.truffaut.com/chou-cabus-chou-pomme-nantais-hatif-le-sachet-de-400-graines-environ-2g.html" } },
      delai: "2 à 3 mois après plantation (précoce), 6 à 7 mois (tardif)", recolte: [6, 7, 8, 9, 10, 11, 12, 1, 2, 3],
      garde: "Cave fraîche ou en place au jardin, sous paillage", src: [jm("chou-pomme")] },
    { id: "blette", nom: "Blette", kg2: 8, m2: 2.7, kcal: null, kcalSrc: null,
      besoin2: 2, unite: "g", achat: {
        bas: { prix: 2.79, qte: 5, lib: "sachet de 5 g", u: "https://www.truffaut.com/poiree-blonde-carde-blanche-2-en-sachet-726070.html" },
        haut: { prix: 3.79, qte: 3, lib: "sachet bio de 3 g", u: "https://www.truffaut.com/graines-potageres-blette-ou-carde-blanche-ampuis-bio-681478.html" } },
      delai: "10 semaines, puis au fil des besoins jusqu'aux gelées", recolte: [7, 8, 9, 10, 11, 12],
      garde: "Une semaine au frais, se congèle", src: ["https://www.truffaut.com/graines-potageres-blette-ou-carde-blanche-ampuis-bio-681478.html"] },
    { id: "courgette", nom: "Courgette", kg2: 10, m2: 2.5, kcal: 16.5, kcalSrc: "ciqual",
      besoin2: 0.5, unite: "g", achat: {
        bas: { prix: 1.79, qte: 4, lib: "sachet de 4 g", u: "https://www.truffaut.com/courgette-verte-petite-alger-4-g-726014.html" },
        haut: { prix: 3.69, qte: 3, lib: "sachet bio de 3 g", u: "https://www.truffaut.com/courgette-verte-noire-maraichere-bio-en-sachet-726136.html" } },
      delai: "6 à 10 semaines", recolte: [7, 8, 9, 10],
      garde: "Une semaine au frais", src: [jm("courgette")] },
    { id: "betterave", nom: "Betterave", kg2: 9, m2: 2.2, kcal: 42.8, kcalSrc: "ciqual",
      besoin2: 0.18, unite: "g", achat: {
        bas: { prix: 1.79, qte: 4, lib: "sachet de 4 g", u: "https://www.truffaut.com/betterave-noire-egypte-en-sachet-726004.html" },
        haut: { prix: 3.69, qte: 4, lib: "sachet bio de 4 g", u: "https://www.truffaut.com/betterave-noire-egypte-bio-en-sachet-726125.html" } },
      delai: "4,5 à 5 mois", recolte: [7, 8, 9, 10, 11],
      garde: "En silo, dans du sable", src: ["https://www.truffaut.com/graines-potageres-betterave-noire-plate-egypte-bio-681453.html", "https://ecoconso.be/fr/node/1975/printable/pdf"] },
    { id: "feve", nom: "Fève", kg2: 6, m2: 2.0, kcal: 82.9, kcalSrc: "ciqual",
      besoin2: 40, unite: "g", achat: {
        bas: { prix: 5.99, qte: 70, lib: "sachet bio de 70 g", u: "https://www.truffaut.com/graines-potageres-feve-aguadulce-tres-longues-cosses-bio-645156.html" },
        haut: { prix: 7.99, qte: 242, lib: "sachet de 242 g", u: "https://www.truffaut.com/feve-seville-longue-cosse-242-g-750765.html" } },
      delai: "60 jours (semis de printemps)", recolte: [4, 5, 6, 7],
      garde: "Se mange fraîche, 2 à 3 jours après la récolte", src: ["https://www.truffaut.com/graines-potageres-feve-aguadulce-tres-longues-cosses-bio-645156.html"] },
    { id: "tomate", nom: "Tomate (abri)", kg2: 12, m2: 1.2, kcal: 19.3, kcalSrc: "ciqual",
      besoin2: 3, unite: "plants", hypothese: "3 plants pour 2 personnes", achat: {
        bas: { prix: 5.79, qte: 3, lib: "barquette de 3 plants", u: "https://www.truffaut.com/tomate-marmande-barquette-3-plants-282452.html" },
        haut: { prix: 6.29, qte: 3, lib: "barquette bio de 3 plants", u: "https://www.truffaut.com/plants-tomates-marmande-bio-barquette-3-plants-764726.html" } },
      delai: "plants à repiquer au printemps", recolte: [7, 8, 9, 10], plantation: "au printemps",
      garde: "Finit de mûrir à l'intérieur avant les gelées", src: [jm("tomate"), "https://www.truffaut.com/plants-tomates-marmande-bio-barquette-3-plants-764726.html"] },
    { id: "fraisier", nom: "Fraisier", kg2: null, m2: null, kcal: null, kcalSrc: null,
      besoin2: 12, unite: "plants", hypothese: "12 plants pour 2 personnes", achat: {
        bas: { prix: 7.99, qte: 6, lib: "barquette de 6 plants Gariguette", u: "https://www.truffaut.com/fraisier-gariguette-barquette-6-plants-60385.html" },
        haut: { prix: 16.10, qte: 6, lib: "barquette de 6 godets Gariguette", u: "https://www.truffaut.com/plant-de-fraisier-gariguette-barquette-de-6-godets.html" } },
      delai: "plantation au printemps ou en fin d'été", recolte: [5, 6, 7, 8, 9, 10], plantation: "au printemps ou en fin d'été",
      garde: "Se garde peu : frais, confiture ou congélation", src: [jm("fraisier")] }
  ];

  var SEMIS = {
 "pomme_de_terre": {
  "quand": "Plantation au printemps",
  "comment": "Sillons de 15 cm de profondeur environ, 30 à 40 cm entre chaque tubercule, 60 à 70 cm entre les sillons. Butter quand la plante atteint 10 à 15 cm.",
  "expo": "Soleil",
  "src": [
   "https://www.jardiner-malin.fr/fiche/pomme-de-terre.html"
  ]
 },
 "courge": {
  "quand": "Semis de mars à mai",
  "comment": "4 à 5 graines en mai dans des petits trous peu profonds, distants de 60 x 80 cm. Pour récolter plus tôt, semer sous abri en mars-avril.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/courge-butternut-en-sachet-726048.html"
  ]
 },
 "oignon": {
  "quand": "Plantation des bulbilles en mars-avril",
  "comment": "Bulbilles espacées de 10 à 15 cm, 25 à 35 cm entre les rangs.",
  "expo": "",
  "src": [
   "https://www.jardiner-malin.fr/fiche/oignon.html"
  ]
 },
 "haricot_vert": {
  "quand": "Semis de fin avril à juillet",
  "comment": "4 à 5 graines par poquet, poquets à 40 cm en tous sens, ou lignes à 40 cm avec une graine tous les 5 cm. Pas plus de 2 à 3 cm de profondeur.",
  "expo": "",
  "src": [
   "https://www.truffaut.com/haricot-nain-mangetout-contender-boite-200g-726194.html"
  ]
 },
 "carotte": {
  "quand": "Semis sous abri en février-mars, en pleine terre d'avril à juillet",
  "comment": "Rangs espacés de 25 à 30 cm. Semis de février-mars pour l'été, d'avril à juillet pour l'automne.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/carotte-touchon-en-sachet-726041.html"
  ]
 },
 "poireau": {
  "quand": "Semis de mars à mai",
  "comment": "Semer sous abri, en pépinière, puis repiquer.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/poireau-monstrueux-carentan-2-en-sachet-726028.html"
  ]
 },
 "ail": {
  "quand": "Date de plantation non chiffrée par nos sources",
  "comment": "Récolte de juin à août quand le feuillage jaunit.",
  "expo": "",
  "src": [
   "https://www.jardiner-malin.fr/fiche/ail.html"
  ]
 },
 "chou": {
  "quand": "Semis en pépinière puis repiquage",
  "comment": "Semis en lignes espacées de 10 à 15 cm. Repiquage tous les 50 cm en tous sens, sol travaillé sur 20 à 25 cm.",
  "expo": "",
  "src": [
   "https://www.jardiner-malin.fr/fiche/chou-pomme.html"
  ]
 },
 "blette": {
  "quand": "Semis de mars à juin",
  "comment": "En pleine terre, en lignes distantes de 40 cm. Couper les feuilles les plus fortes.",
  "expo": "Plein soleil",
  "src": [
   "https://www.truffaut.com/poiree-blonde-carde-blanche-2-en-sachet-726070.html"
  ]
 },
 "courgette": {
  "quand": "Semis de mars à mai",
  "comment": "4 à 5 graines en mai dans des petits trous peu profonds, distants de 60 x 80 cm.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/courgette-verte-petite-alger-4-g-726014.html"
  ]
 },
 "betterave": {
  "quand": "Semis d'avril à juillet",
  "comment": "En pleine terre dès que les gelées ne sont plus à craindre. Lignes espacées de 20 à 30 cm, éclaircir à 20 à 25 cm.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/betterave-noire-egypte-en-sachet-726004.html"
  ]
 },
 "feve": {
  "quand": "Semis de mars à avril",
  "comment": "Par 3 graines, à 5 à 6 cm de profondeur, 25 cm entre les plants. Levée en 9 à 12 jours. Récolte 60 jours après le semis, 2 à 3 fois par semaine.",
  "expo": "Soleil",
  "src": [
   "https://www.truffaut.com/graines-potageres-feve-aguadulce-tres-longues-cosses-bio-645156.html"
  ]
 },
 "tomate": {
  "quand": "Semis de février à avril sous abri, plantation après les dernières gelées",
  "comment": "Dans une grande partie de la France, la plantation se fait au cours du mois de mai. Exposition ensoleillée et chaude, sol riche, meuble et drainé.",
  "expo": "Plein soleil",
  "src": [
   "https://www.jardiner-malin.fr/fiche/tomate.html"
  ]
 },
 "fraisier": {
  "quand": "Plantation au printemps ou en fin d'été",
  "comment": "Espacer les fraisiers d'environ 30 à 40 cm.",
  "expo": "Plein soleil",
  "src": [
   "https://www.jardiner-malin.fr/fiche/fraisier.html"
  ]
 }
};

  /* Planches partagées dans l'année : une culture récoltée tôt laisse la place à une culture semée en juillet.
     fin = dernier mois de récolte de la première, jusqua = dernier mois de semis de la seconde (fiches des sachets). */
  var RELAIS = {
    avant: {
      feve: { fin: 6, txt: "récolte d'avril à juin", u: "https://www.truffaut.com/graines-potageres-feve-aguadulce-tres-longues-cosses-bio-645156.html" },
      pomme_de_terre: { fin: 7, txt: "pommes de terre nouvelles en 80 jours, récolte de mai à juillet", u: "https://www.truffaut.com/pomme-terre-celtiane-calibre-25-32-etui-25-plants-543477.html" }
    },
    apres: {
      carotte: { jusqua: 7, txt: "semis en pleine terre d'avril à juillet pour une récolte d'automne", u: "https://www.truffaut.com/carotte-touchon-en-sachet-726041.html" },
      haricot_vert: { jusqua: 7, txt: "semis de fin avril à juillet", u: "https://www.truffaut.com/haricot-nain-mangetout-contender-boite-200g-726194.html" },
      betterave: { jusqua: 7, txt: "semis d'avril à juillet", u: "https://www.truffaut.com/betterave-noire-egypte-en-sachet-726004.html" }
    }
  };

  /* L'hiver nourrit l'été : un engrais vert d'hiver sur chaque planche libérée avant novembre.
     Terre & Humanisme (association de Pierre Rabhi), Mas de Beaulieu : mélange seigle, vesce d'hiver, féveroles,
     fauché avant floraison au printemps, étalé, racines en place, couvert 4 à 6 semaines, puis on plante. */
  var HIVER = {
    finRecolteMax: 10,          // la vesce d'hiver se sème d'août à octobre (Kokopelli)
    doseGm2: 15,                // vesce d'hiver : environ 15 g par m² (Kokopelli)
    sachet: { prix: 3.40, g: 80, lib: "Vesce d'hiver, sachet de 80 g (Kokopelli, bio)", u: "https://kokopelli-semences.fr/fr/p/V0008-D-Hiver" },
    src: [
      { t: "Terre & Humanisme, « Un potager agroécologique à l'approche de l'automne », 4 septembre 2024", u: "https://formation.terre-humanisme.org/un-potager-agroecologique-a-lapproche-de-lautomne/" },
      { t: "Terre & Humanisme, « Comment organiser les rotations de culture ? », 11 novembre 2023", u: "https://formation.terre-humanisme.org/comment-organiser-les-rotations-de-culture/" },
      { t: "Kokopelli, fiche vesce d'hiver (semis août à octobre, 15 g par m², fauchée avant les premières cultures)", u: "https://kokopelli-semences.fr/fr/p/V0008-D-Hiver" }
    ]
  };

  /* Entretien minimum : uniquement des gestes sourcés. */
  var ENTRETIEN = [
    { titre: "Pailler", txt: "Environ 7 cm de paillis (tontes séchées, feuilles mortes, paille), sur une terre déjà désherbée, sans couvrir le collet des plants. À 10 cm, le paillis empêche les mauvaises herbes de germer entre les légumes. Il limite aussi l'arrosage et le binage. Au printemps, on l'écarte pour que la terre se réchauffe.", src: { t: "DRAAF Auvergne-Rhône-Alpes, fiche « Paillage du potager »", u: "https://draaf.auvergne-rhone-alpes.agriculture.gouv.fr/IMG/pdf/FICHE_TECH_PAILLAGE_AU_POTAGER-1_cle082e1d.pdf" } },
    { titre: "Ne jamais laisser la terre nue l'hiver", txt: "Après la récolte d'été, un engrais vert d'hiver (seigle, vesce d'hiver, féveroles). Au printemps, on le fauche avant la floraison, on l'étale en laissant les racines, on le couvre 4 à 6 semaines (carton, paillage épais ou bâche), puis on ameublit légèrement et on plante.", src: { t: "Terre & Humanisme, 4 septembre 2024", u: "https://formation.terre-humanisme.org/un-potager-agroecologique-a-lapproche-de-lautomne/" } },
    { titre: "Ameublir sans retourner", txt: "À la grelinette, sans mélanger les couches de terre.", src: { t: "Terre & Humanisme, « Les engrais verts : quésaco ? », 15 avril 2021", u: "https://formation.terre-humanisme.org/les-engrais-verts-quesaco/" } },
    { titre: "Compost tous les deux ans", txt: "3 à 6 kg de compost par m² en tête de rotation, au moment de planter les légumes les plus gourmands (tomate, courge).", src: { t: "Terre & Humanisme, rotation du Mas de Beaulieu, 11 novembre 2023", u: "https://formation.terre-humanisme.org/comment-organiser-les-rotations-de-culture/" } },
    { titre: "Faire tourner les familles", txt: "Un légume gourmand puis un sobre : la courge suivie d'une fève, qui fixe l'azote de l'air, la tomate suivie de carottes d'hiver. Les familles n'attirent pas les mêmes maladies.", src: { t: "Terre & Humanisme, 11 novembre 2023", u: "https://formation.terre-humanisme.org/comment-organiser-les-rotations-de-culture/" } }
  ];

  /* Semences recommandées : Kokopelli (bio, libres de droits, reproductibles). */
  var KOKOPELLI = {
    u: "https://kokopelli-semences.fr/fr/c/semences/potageres",
    prixType: 3.40, releve: "6 novembre 2026",
    loi: { t: "Loi n° 2020-699 du 10 juin 2020, article 10 (vente de semences de variétés du domaine public aux jardiniers amateurs)", u: "https://www.quechoisir.org/actualite-jardinage-les-semences-paysannes-restent-autorisees-pour-les-amateurs-n80839/" }
  };

  /* Mois de garde après la dernière récolte, quand une source les chiffre (sinon : mangé seulement au mois de récolte). */
  var GARDE_MOIS = {
    courge: { mois: 3, txt: "jusqu'en mars" },            // jardiner-malin, fiche courge
    oignon: { mois: 6, txt: "6 à 8 mois, on compte 6" },  // jardiner-malin, fiche oignon
    carotte: { mois: 4, txt: "4 à 5 mois en sable, on compte 4" } // jardiner-malin, carottes au sable
  };

  /* Cultures longues : délai avant la première récolte, sourcé. long = plus de 2 ans (grisé). */
  var LONGUES = [
    { id: "framboisier", nom: "Framboisier", long: false,
      delai: "les cannes donnent leurs fruits leur 2e année (variétés non remontantes)",
      detail: "80 cm entre chaque pied. Vit 10 à 12 ans, à renouveler tous les 5 à 7 ans.", src: [jm("framboisier")] },
    { id: "rhubarbe", nom: "Rhubarbe", long: false,
      delai: "pas de récolte la 1re année",
      detail: "Récolte d'avril à septembre-octobre. Produit 10 à 15 ans.", src: [jm("rhubarbe")] },
    { id: "cassissier", nom: "Cassissier", long: true,
      delai: "récolte maximale à partir de la 4e année",
      detail: "Produit 10 à 15 ans.", src: [jm("cassissier-cassis")] },
    { id: "prunier", nom: "Prunier", long: true,
      delai: "2 à 4 ans après la plantation",
      detail: "Selon le porte-greffe, la variété et les conditions de culture. Certaines variétés ont besoin d'un arbre compagnon pour la pollinisation.", src: [jm("prunier")] },
    { id: "asperge", nom: "Asperge", long: true,
      delai: "première récolte au bout de 3 ans",
      detail: "Plantation de février à avril, 50 à 60 cm entre les plants, 1,5 m entre les lignes. Produit environ 15 ans.", src: [jm("asperge")] },
    { id: "pommier", nom: "Pommier", long: true,
      delai: "plusieurs années, la source ne donne pas de chiffre",
      detail: "Le délai dépend du porte-greffe, de la variété et de l'âge de l'arbre à la plantation. Meilleure période de plantation : l'automne.", src: [jm("pommier-pommier")] },
    { id: "poirier", nom: "Poirier", long: true,
      delai: "plusieurs années, la source ne donne pas de chiffre",
      detail: "Dépend surtout du porte-greffe, de l'âge du plant, de la variété et de la forme. La source déconseille de retenir la règle « 5 à 10 ans ».", src: [jm("poirier")] }
  ];

  /* Matériel : un jeu pour le foyer (outils, arrosage), stockage et poules par lot de 2 personnes. */
  var MATERIEL = {
    outils: { titre: "Outils", par2: false, items: [
      ["Bêche", 9.99, "https://www.castorama.fr/beche-senlis-a-manche-pomme-en-bois-l-100-cm/3454975184529_CAFR.prd", 40.90, "https://www.castorama.fr/beche-a-rebord-28-cm-leborgne-duopro-avec-manche-bequille-novagrip/3157333142871_CAFR.prd"],
      ["Fourche à bêcher", 15.90, "https://www.castorama.fr/fourche-a-becher-4-dents-manche-pomme/3454975184505_CAFR.prd", 37.90, "https://www.castorama.fr/fourche-a-becher-ergonomique-fiskars-132-3-cm/6411501705570_CAFR.prd"],
      ["Râteau", 5.99, "https://www.castorama.fr/rateau-de-jardin-14-dents-soudees-bois-et-metal/3454975184611_CAFR.prd", 27.50, "https://www.castorama.fr/rateau-14-dents-courbes-leborgne-duopro/3157333751028_CAFR.prd"],
      ["Binette", 9.69, "https://www.castorama.fr/binette-14cm-avec-manche-en-bois-en-acier-et-textilene/3454975184659_CAFR.prd", 27.90, "https://www.castorama.fr/binette-duopro-16cm-manche-en-bois-leborgne/3157334670212_CAFR.prd"],
      ["Serfouette", 9.69, "https://www.castorama.fr/serfouette-panne-langue-26-x-100-cm-manche-en-bois/3454975184543_CAFR.prd", 28.90, "https://www.castorama.fr/serfouette-forgee-panne-et-langue-leborgne-a-douille-ovale-duopro/3157333113017_CAFR.prd"],
      ["Transplantoir", 2.09, "https://www.castorama.fr/transplantoir-a-main-performance-power-plastique-et-acier/5063022731807_CAFR.prd", 15.50, "https://www.castorama.fr/transplantoir-leborgne-duopro-manche-en-bois-l30-x-l-8-cm/3157334500304_CAFR.prd"],
      ["Cordeau", 3.99, "https://www.castorama.fr/cordeau-de-macon-en-fil-de-coton-blanc-diall-2-5-mm-30-m/3663602919520_CAFR.prd", 9.49, "https://www.castorama.fr/cordeau-a-tracer-jaune-haute-visibilite-75-m/5059340002408_CAFR.prd"],
      ["Brouette", 69.90, "https://www.castorama.fr/brouette-roue-pneumatique-380-mm-cuve-en-acier-galvanise-capacite-90l-haemmerlin-prems/3155032400315_CAFR.prd", 99.90, "https://www.castorama.fr/brouette-100-l-avec-roue-increvable-400-mm-cuve-en-acier-galvanise-aktiv-premium-haemmerlin/3155030501038_CAFR.prd"],
      ["Gants x2", 3.20, "https://www.castorama.fr/gants-de-jardinage-verve-taille-8-m-/3663602672685_CAFR.prd", 19.98, "https://www.castorama.fr/gants-de-jardin-special-plantation-taille-8-m-/3353090089842_CAFR.prd"]
    ] },
    arrosage: { titre: "Arrosage et compost", par2: false, items: [
      ["Arrosoir", 7.49, "https://www.castorama.fr/arrosoir-eda-plastiques-parisien-en-plastique-recycle-coloris-vert-metal-contenance-11-litres/3086960058067_CAFR.prd", 12.50, "https://www.castorama.fr/arrosoir-eda-luxe-vert-metal-12l-h-41-cm/3086960017002_CAFR.prd"],
      ["Tuyau 25 m", 19.90, "https://www.castorama.fr/tuyau-d-arrosage-20-mm-l-25-m-claber/8000625903733_CAFR.prd", 49.90, "https://www.castorama.fr/tuyau-15-mm-l-25-m-high-flex-gardena/4078500002134_CAFR.prd"],
      ["Récupérateur d'eau de pluie", 26.53, "https://www.castorama.fr/recuperateur-d-eau-de-pluie-200l-verve-coloris-vert-60-x-h-70-cm/5059340931531_CAFR.prd", 89.90, "https://www.castorama.fr/recuperateur-d-eau-de-pluie-520l-garantia-coloris-vert-l-124-x-l-80-x-h-93-cm/4023122143864_CAFR.prd"],
      ["Composteur", 39.90, "https://www.castorama.fr/composteur-cardon-en-bois-250-l-jardipolys/3443440026723_CAFR.prd", 59.90, "https://www.castorama.fr/composteur-plastique-effet-bois-400-l-verve/5063022039118_CAFR.prd"]
    ] },
    stockage: { titre: "Stockage des récoltes", par2: true, items: [
      ["Cagettes bois x6", 35.94, "https://www.truffaut.com/cagette-en-bois-ceruse-1027892.html", 39.00, "https://www.truffaut.com/cagette-en-bois.html"],
      ["Sable 25 kg (carottes, betteraves)", 8.29, "https://www.truffaut.com/sable-de-jardinage-25kg.html", 16.58, "https://www.truffaut.com/sable-de-jardinage-25kg.html"],
      ["Bocaux 1 L (6 ou 12)", 26.50, "https://www.truffaut.com/bocaux-le-parfait-super-1l-o85-pack-de-6-le-parfait.html", 53.00, "https://www.truffaut.com/bocaux-le-parfait-super-1l-o85-pack-de-6-le-parfait.html"]
    ] },
    poules: { titre: "Poules", par2: true, items: [
      ["Poulailler 4 poules", 139.00, "https://www.truffaut.com/poulailler-princesse-avec-pondoir-en-bois-marron.html", 490.00, "https://www.truffaut.com/poulailler-4-poules-solide-et-pratique-modele-houdan.html"],
      ["Grillage 20 m", 62.90, "https://www.castorama.fr/grillage-simple-torsion-blooma-maille-50-x-50-mm-vert-20-x-h-1-2-m/3663602728719_CAFR.prd", 78.90, "https://www.castorama.fr/grillage-simple-torsion-blooma-maille-50-x-50-mm-vert-20-x-h-1-5-m/3663602728726_CAFR.prd"],
      ["Poteaux en T x8", 57.12, "https://www.castorama.fr/poteau-grillage-longue-duree-profile-en-t-coloris-gris-l-30-mm-x-p-30-mm-x-h-1-45-m/5059340451510_CAFR.prd", 66.72, "https://www.castorama.fr/poteau-grillage-longue-duree-profile-en-t-coloris-gris-l-30-mm-x-p-30-mm-x-h-1-75-m/5059340451527_CAFR.prd"],
      ["Mangeoire", 10.22, "https://www.truffaut.com/mangeoire-poule-galvanisee-7x50cm-kerbl.html", 24.99, "https://www.truffaut.com/mangeoire-a-tremie-galvanisee-7-kg-17-x-18-x-39-cm.html"],
      ["Abreuvoir", 14.99, "https://www.truffaut.com/abreuvoir-poule-seau-metal-3l.html", 19.99, "https://www.truffaut.com/abreuvoir-poules-et-volailles-15-l-river-system.html"],
      ["Poules rousses prêtes à pondre (prix à la poule)", 14.00, "https://volailles-occitanie.com/produits/poules-pondeuses-demarrees/", 16.50, "https://lapiniere.com/Poule-pondeuse-Rousse", "parPoule", 2.00],
      ["Premier sac d'aliment", 18.99, "https://www.truffaut.com/melange-premium-poule-pondeuse-15kg-1059671.html", 28.49, "https://www.truffaut.com/aliment-complet-pour-poule-pondeuse-en-granule-regal-20kg-785054.html"]
    ] }
  };

  var CONSTANTES = {
    kcalHomme: 2600, kcalFemme: 2100,      // ANSES 2016
    m2ParPersonneJeavons: 232,              // Ecology Action 2019
    rendementPdt: 2.5,                      // kg/m², 48 kg sur 19,2 m² (un-jardin-bio.com, extensif)
    enclosParLot: 18,                       // m² pour 4 poules (hypothèse extrapolée de m2A : 8 à 10 m² pour 2)
    enclosParPoule: 4.5,                    // m² par poule, même hypothèse (18 / 4)
    partMaxEnclos: 0.25,                    // l'enclos ne prend jamais plus du quart du terrain (notre règle)
    oeufsParPersonne: 224,                  // œufs par Français en 2023 (VetAgro Sup, juin 2025)
    partAllees: 0.2,                        // Ecology Action : 2 000 sq ft de planches, 2 500 avec les allées
    oeufsParPouleMin: 280, oeufsParPouleMax: 320, // VetAgro Sup, élevage
    poidsOeuf: 58,                          // g, hypothèse
    kcalOeuf: 140                           // kcal/100 g, Ciqual 22000
  };

  window.POTAGER_DONNEES = { SOURCES: S, CULTURES: CULTURES, SEMIS: SEMIS, RELAIS: RELAIS, GARDE_MOIS: GARDE_MOIS, HIVER: HIVER, ENTRETIEN: ENTRETIEN, KOKOPELLI: KOKOPELLI, LONGUES: LONGUES, MATERIEL: MATERIEL, K: CONSTANTES };
})();
