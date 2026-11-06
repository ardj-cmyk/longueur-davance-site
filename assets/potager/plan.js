/* Plan perso du potager : carte (photo aérienne IGN + dessin du terrain) et calcul du plan.
   Le calcul est une règle de trois sur le modèle 2 personnes sourcé (donnees.js), rien d'autre. */
(function () {
  var D = window.POTAGER_DONNEES;
  var R = 6378137;
  var NB = " ";

  /* ---------- Outils ---------- */
  /* Règle d'écriture : un nombre et son unité ne sont jamais séparés. */
  function colle(h) { return h.replace(/(\d) (?=(cm|m²|m|kg|g|€|%|°C|jours|mois|ans|semaines|kcal|L|plants|graines)(?![A-Za-zÀ-ÿ]))/g, "$1\u00a0"); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function nb(x, dec) {
    if (x == null || isNaN(x)) return "";
    var d = dec == null ? (Math.abs(x) >= 100 ? 0 : 1) : dec;
    var s = Number(x).toFixed(d);
    if (d > 0) s = s.replace(/\.?0+$/, "");
    var p = s.split(".");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, NB);
    return p.join(",");
  }
  function euros(x) {
    var s = Number(x).toFixed(2).split(".");
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, NB);
    return s.join(",") + NB + "€";
  }
  function lien(u, t) { return '<a href="' + esc(u) + '" target="_blank" rel="noopener">' + t + "</a>"; }
  var MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];

  /* ---------- Carte ---------- */
  function merc(lon, lat) {
    return [R * lon * Math.PI / 180, R * Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360))];
  }
  function demerc(x, y) {
    return [x / R * 180 / Math.PI, (2 * Math.atan(Math.exp(y / R)) - Math.PI / 2) * 180 / Math.PI];
  }
  function anneaux(geom) {
    if (!geom) return [];
    if (geom.type === "Polygon") return [geom.coordinates[0]];
    if (geom.type === "MultiPolygon") return geom.coordinates.map(function (p) { return p[0]; });
    return [];
  }
  /* Surface vraie d'un polygone lon/lat, en m² (projection Mercator corrigée de cos²(latitude)). */
  function surface(pts) {
    if (!pts || pts.length < 3) return 0;
    var lat0 = pts.reduce(function (a, p) { return a + p[1]; }, 0) / pts.length;
    var m = pts.map(function (p) { return merc(p[0], p[1]); });
    var a = 0;
    for (var i = 0; i < m.length; i++) { var j = (i + 1) % m.length; a += m[i][0] * m[j][1] - m[j][0] * m[i][1]; }
    var c = Math.cos(lat0 * Math.PI / 180);
    return Math.abs(a) / 2 * c * c;
  }

  /* Affiche la photo aérienne autour d'un point (ou d'une parcelle) dans `boite`.
     options : { lon, lat, parcelle (GeoJSON), zone ([[lon,lat]...]), dessin (bool), surChange(fn) } */
  function carte(boite, o) {
    var TAILLE = 640;
    var c = merc(o.lon, o.lat), cosl = Math.cos(o.lat * Math.PI / 180);
    var minx = c[0], maxx = c[0], miny = c[1], maxy = c[1];
    var tous = [];
    anneaux(o.parcelle).forEach(function (a) { tous = tous.concat(a); });
    if (o.zone) tous = tous.concat(o.zone);
    tous.forEach(function (p) { var m = merc(p[0], p[1]); minx = Math.min(minx, m[0]); maxx = Math.max(maxx, m[0]); miny = Math.min(miny, m[1]); maxy = Math.max(maxy, m[1]); });
    var cote = Math.max(maxx - minx, maxy - miny) * 1.35;
    cote = Math.max(cote, (o.minCote || 70) / cosl);
    var cx = (minx + maxx) / 2, cy = (miny + maxy) / 2;
    var b = [cx - cote / 2, cy - cote / 2, cx + cote / 2, cy + cote / 2];
    var url = "https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:3857&BBOX=" +
      b.map(function (v) { return v.toFixed(2); }).join(",") + "&WIDTH=" + TAILLE + "&HEIGHT=" + TAILLE + "&FORMAT=image/jpeg";
    function px(p) { var m = merc(p[0], p[1]); return [(m[0] - b[0]) / cote * TAILLE, (b[3] - m[1]) / cote * TAILLE]; }
    function geo(x, y) { return demerc(b[0] + x / TAILLE * cote, b[3] - y / TAILLE * cote); }
    var zone = (o.zone || []).slice();
    boite.innerHTML = '<div class="carte-img"><img alt="Photo aérienne IGN du terrain" src="' + url + '" width="' + TAILLE + '" height="' + TAILLE + '">' +
      '<svg viewBox="0 0 ' + TAILLE + " " + TAILLE + '" xmlns="http://www.w3.org/2000/svg"></svg></div>' +
      '<p class="carte-src">Photo aérienne © IGN Géoplateforme' + (o.parcelle ? ", contour cadastral API Carto IGN" : "") + ". Échelle : " + Math.round(cote * cosl) + NB + "m de côté.</p>";
    var svg = boite.querySelector("svg");
    function trace() {
      var h = "";
      anneaux(o.parcelle).forEach(function (a) {
        h += '<polygon points="' + a.map(function (p) { return px(p).join(","); }).join(" ") + '" fill="none" stroke="#fdfcf9" stroke-width="3" stroke-dasharray="10 6"/>';
      });
      if (zone.length) {
        var pts = zone.map(function (p) { return px(p).join(","); }).join(" ");
        if (o.sansZone) h += '<polygon points="' + pts + '" fill="none" stroke="#fdfcf9" stroke-width="3"/>';
        else {
          h += zone.length >= 3 ? '<polygon points="' + pts + '" fill="rgba(163,70,26,.35)" stroke="#a3461a" stroke-width="4"/>' : '<polyline points="' + pts + '" fill="none" stroke="#a3461a" stroke-width="4"/>';
          zone.forEach(function (p) { var q = px(p); h += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="8" fill="#a3461a" stroke="#fdfcf9" stroke-width="3"/>'; });
        }
      }
      svg.innerHTML = h;
      if (o.surChange) o.surChange(zone.slice(), surface(zone));
    }
    if (o.dessin) {
      svg.style.cursor = "crosshair";
      svg.addEventListener("click", function (e) {
        var r = svg.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width * TAILLE, y = (e.clientY - r.top) / r.height * TAILLE;
        if (zone.length >= 60) return;
        zone.push(geo(x, y).map(function (v) { return Math.round(v * 1e7) / 1e7; }));
        trace();
      });
    }
    trace();
    return {
      annuler: function () { zone.pop(); trace(); },
      effacer: function () { zone = []; trace(); },
      zone: function () { return zone.slice(); },
      pixels: function (pts) { return pts.map(px); }
    };
  }

  /* ---------- Calcul du plan ---------- */
  function calculer(cmd) {
    var K = D.K, N = cmd.personnes, f0 = N / 2, lots = Math.ceil(N / 2);
    var choisies = D.CULTURES.filter(function (c) { return cmd.cultures.indexOf(c.id) >= 0; });

    /* Poules : de quoi couvrir la consommation moyenne d'œufs (224 par personne et par an, VetAgro Sup),
       au bas de la fourchette de ponte (280 par poule et par an). Enclos de 4,5 m² par poule (m2A : 8 à 10 m² pour 2),
       plafonné au quart du terrain (notre règle). Moins de 2 poules : pas de poules. */
    var poulesVoulues = cmd.poules ? Math.max(2, Math.ceil(N * K.oeufsParPersonne / K.oeufsParPouleMin)) : 0;
    var poulesMax = Math.floor(cmd.surface_m2 * K.partMaxEnclos / K.enclosParPoule);
    var poules = Math.min(poulesVoulues, poulesMax);
    if (poules < 2) poules = 0;
    var poulesLimitees = cmd.poules && poules < poulesVoulues;
    var enclos = poules * K.enclosParPoule;

    /* Allées : 20 % du terrain cultivé (Ecology Action : 2 000 sq ft de planches, 2 500 avec les allées). */
    var cultivable = Math.max(0, cmd.surface_m2 - enclos);
    var dispo = cultivable * (1 - K.partAllees);
    var besoin = choisies.reduce(function (a, c) { return a + (c.m2 ? c.m2 * f0 : 0); }, 0);
    var echelle = besoin > 0 ? Math.min(1, dispo / besoin) : 1;
    var reste = Math.max(0, dispo - besoin);
    var surfaceIdeale = besoin / (1 - K.partAllees) + poulesVoulues * K.enclosParPoule;

    var lignes = choisies.map(function (c) {
      var e = c.m2 ? echelle : 1;
      var besoinGraines = c.besoin2 * f0 * e;
      function lot(a) {
        var n = a.qte ? Math.max(1, Math.ceil(besoinGraines / a.qte - 1e-9)) : 1;
        return { n: n, prix: n * a.prix, a: a };
      }
      return {
        c: c, kg: c.kg2 ? c.kg2 * f0 * e : null, m2: c.m2 ? c.m2 * f0 * e : null,
        kcal: c.kg2 && c.kcal ? c.kg2 * f0 * e * c.kcal * 10 : 0,
        graines: besoinGraines, bas: lot(c.achat.bas), haut: lot(c.achat.haut)
      };
    });

    var kcalLegumes = lignes.reduce(function (a, l) { return a + l.kcal; }, 0);
    var bonusKg = reste * K.rendementPdt;
    var bonusKcal = bonusKg * 805; // pomme de terre crue sans peau, Ciqual 4008 (80,5 kcal/100 g)
    var oeufsMin = poules * K.oeufsParPouleMin, oeufsMax = poules * K.oeufsParPouleMax;
    var kcalOeuf = K.poidsOeuf / 100 * K.kcalOeuf;
    var besoinAn = N * (K.kcalHomme + K.kcalFemme) / 2 * 365;

    var budget = { graines: { bas: 0, haut: 0 }, postes: [] };
    lignes.forEach(function (l) { budget.graines.bas += l.bas.prix; budget.graines.haut += l.haut.prix; });
    ["outils", "arrosage", "stockage", "poules"].forEach(function (k) {
      if (k === "poules" && !poules) return;
      var m = D.MATERIEL[k], mult = k === "poules" ? Math.ceil(poules / 4) : (m.par2 ? lots : 1);
      var bas = 0, haut = 0;
      m.items.forEach(function (i) {
        if (i[5] === "parPoule") { bas += i[1] * poules + (i[6] || 0); haut += i[3] * poules; }
        else { bas += i[1] * mult; haut += i[3] * mult; }
      });
      budget.postes.push({ k: k, titre: m.titre, mult: mult, bas: bas, haut: haut });
    });
    budget.total = { bas: budget.graines.bas, haut: budget.graines.haut };
    budget.postes.forEach(function (p) { budget.total.bas += p.bas; budget.total.haut += p.haut; });

    return {
      N: N, lots: lots, lignes: lignes, besoin: besoin, dispo: dispo, echelle: echelle, reste: reste, enclos: enclos,
      poules: poules, poulesVoulues: poulesVoulues, poulesLimitees: poulesLimitees, allees: cultivable * K.partAllees,
      surfaceIdeale: surfaceIdeale,
      kcalLegumes: kcalLegumes, bonusKg: bonusKg, bonusKcal: bonusKcal,
      oeufsMin: oeufsMin, oeufsMax: oeufsMax, kcalOeufsMin: oeufsMin * kcalOeuf, kcalOeufsMax: oeufsMax * kcalOeuf,
      besoinAn: besoinAn, pctLegumes: kcalLegumes / besoinAn * 100,
      pctAvecBonus: (kcalLegumes + bonusKcal) / besoinAn * 100,
      jeavons: N * K.m2ParPersonneJeavons, pctJeavons: cmd.surface_m2 / (N * K.m2ParPersonneJeavons) * 100,
      longues: D.LONGUES.filter(function (l) { return (cmd.longues || []).indexOf(l.id) >= 0; }),
      budget: budget
    };
  }

  /* ---------- Rendu du plan ---------- */
  function src(k) { var s = D.SOURCES[k]; return lien(s.u, esc(s.t)); }
  function ligneSrc(c) { return c.src.map(function (u, i) { return lien(u, "source" + (c.src.length > 1 ? " " + (i + 1) : "")); }).join(", "); }

  function rendre(cmd, p) {
    var h = "";
    var personnes = p.N + NB + "personne" + (p.N > 1 ? "s" : "");
    var surf = nb(cmd.surface_m2, 0) + NB + "m²";
    var origine = { dessin: "dessiné sur la photo aérienne", cadastre: "surface de la parcelle au cadastre", saisie: "surface que tu as indiquée", modele: "la place qu'il faut pour tes légumes" }[cmd.surface_source] || "";

    var prenom = cmd.prenom ? esc(String(cmd.prenom).slice(0, 40)) : "";
    var commune = cmd.parcelle && cmd.parcelle.commune ? " à " + esc(cmd.parcelle.commune) : "";
    var noms = p.lignes.map(function (l) { return l.c.nom.toLowerCase().replace(/ \(.*\)/, ""); });
    var fav = noms.slice(0, 3).join(", ") + (noms.length > 3 ? " et " + (noms.length - 3) + " autres" : "");
    h += '<section class="intro-perso"><p class="lettre">' + (prenom ? prenom + ", voici" : "Voici") + " le potager calculé pour " + (p.N > 1 ? "vous " + p.N : "toi") + ", sur " + (cmd.surface_source === "modele" ? "la place qu'il faut" : "tes " + surf) + commune + ". " +
      "Tu as gardé " + p.lignes.length + " culture" + (p.lignes.length > 1 ? "s" : "") + " que vous aimez : " + esc(fav) + "." +
      (p.longues.length ? " Et tu anticipes : " + p.longues.map(function (l) { return esc(l.nom.toLowerCase()); }).join(", ") + "." : "") +
      (p.poules ? " Avec " + p.poules + " poules." : "") + "</p></section>";
    h += '<section><h2>' + (prenom ? "Le terrain de " + prenom : "Ton terrain et ton foyer") + '</h2><div class="chiffres">' +
      '<div><b>' + surf + '</b><span>' + esc(origine) + '</span></div>' +
      '<div><b>' + personnes + '</b><span>à nourrir</span></div>' +
      '<div><b>' + nb(p.pctLegumes, 1) + NB + '%</b><span>des calories du foyer avec tes légumes</span></div>' +
      '<div><b>' + euros(p.budget.total.bas) + '</b><span>pour démarrer, petit budget</span></div></div>' +
      (p.echelle < 1 ? '<div class="alerte" style="margin-top:12px"><p><b>C\'est le maximum pour ta surface.</b> Sur ' + surf + ", ton potager donne " + nb(p.echelle * 100, 0) + NB + "% des légumes que ton foyer mange en un an. Pour tout loger, il faudrait environ " + nb(p.surfaceIdeale, 0) + NB + "m², allées" + (cmd.poules ? " et poules" : "") + " comprises.</p></div>" : "");
    if (cmd.parcelle && cmd.parcelle.idu) h += '<p class="note">Parcelle cadastrale ' + esc(cmd.parcelle.idu) + (cmd.parcelle.contenance ? ", " + nb(cmd.parcelle.contenance, 0) + NB + "m² au cadastre" : "") + ".</p>";
    h += '<h3 class="titre-vue">' + (prenom ? "Le jardin de " + prenom + " en 3D" : "Ton jardin en 3D") + '</h3><div id="vue-3d" class="noprint"></div><h3 class="titre-vue">Le plan, planche par planche</h3><div id="vue-jardin"></div></section>';

    /* L'essentiel, honnête */
    h += '<section><div class="alerte"><p><b>À savoir d\'abord.</b> ';
    if (p.echelle < 1) {
      h += "Ton terrain ne loge pas tous les légumes choisis en quantité normale : il faudrait environ " + nb(p.surfaceIdeale, 0) + NB + "m². Le plan réduit chaque culture à " + nb(p.echelle * 100, 0) + NB + "% de ce que ton foyer consomme. ";
    } else {
      h += "Tes légumes prennent " + nb(p.besoin, 0) + NB + "m² de planches, plus les allées" + (p.enclos ? ", les poules " + nb(p.enclos, 0) + NB + "m²" : "") + ". Il te reste " + nb(p.reste, 0) + NB + "m² de planches libres. ";
    }
    h += "Ces légumes couvrent environ " + nb(p.pctLegumes, 1) + NB + "% des calories dont ton foyer a besoin. ";
    if (p.reste > 1) h += "Si tu mets les " + nb(p.reste, 0) + NB + "m² restants en pommes de terre, tu montes à environ " + nb(p.pctAvecBonus, 0) + NB + "% (" + nb(p.bonusKg, 0) + NB + "kg de plus par an). ";
    h += "Les allées pour marcher prennent " + nb(p.allees, 0) + NB + "m², soit 20" + NB + "% du terrain cultivé, la proportion d'Ecology Action. ";
    if (p.poulesLimitees) h += p.poules ? "Les poules sont limitées à " + p.poules + " pour que leur enclos ne prenne pas plus du quart du terrain. " : "Ton terrain est trop petit pour un enclos de 2 poules sans dépasser le quart de la surface : pas de poules dans ce plan. ";
    h += "Pour vivre entièrement d'un jardin, Ecology Action compte environ 232" + NB + "m² par personne, jardinier expérimenté, sans viande : " + nb(p.jeavons, 0) + NB + "m² pour ton foyer. Ton terrain en représente " + nb(Math.min(p.pctJeavons, 999), 0) + NB + "%.</p>";
    h += '<p class="note">Sources : ' + src("jeavons") + ", calories " + src("ciqual") + ", besoins " + src("anses") + ". Calcul sur la moyenne des deux repères ANSES, soit 2" + NB + "350" + NB + "kcal par personne et par jour.</p></div></section>";

    /* Cultures */
    h += '<section><h2>1. Tes cultures et leur place</h2><div class="tab"><table><thead><tr><th>Culture</th><th>Par an</th><th>Surface</th><th>Graines ou plants</th></tr></thead><tbody>';
    p.lignes.forEach(function (l) {
      var g = l.c.unite === "plants" ? nb(Math.ceil(l.graines - 1e-9), 0) + " plants" : (l.graines >= 1000 ? nb(l.graines / 1000, 2) + NB + "kg" : nb(l.graines, l.graines < 1 ? 2 : 1) + NB + "g");
      h += "<tr><td>" + esc(l.c.nom) + "</td><td class=n>" + (l.kg != null ? nb(l.kg, 0) + NB + "kg" : "<small>non chiffré</small>") + "</td><td class=n>" + (l.m2 != null ? nb(l.m2, 1) + NB + "m²" : "<small>non chiffré</small>") + "</td><td class=n>" + g + "</td></tr>";
    });
    h += '<tr class="tot"><td>Total</td><td></td><td class=n>' + nb(p.besoin * p.echelle, 0) + NB + "m²</td><td></td></tr></tbody></table></div>";
    h += '<p class="note">Quantités : consommation annuelle d\'une famille de quatre ramenée à ' + personnes + ", surfaces et semences au rendement d'un maraîcher en culture extensive (" + src("jardin30") + "). En culture serrée, la même source donne environ deux fois moins de place. Fraisiers : " + nb(6 * p.N, 0) + " plants, notre choix de départ (6 par personne), pas un chiffre sourcé.</p></section>";

    /* Calendrier */
    var saisons = [["Printemps", [3, 4, 5]], ["Été", [6, 7, 8]], ["Automne", [9, 10, 11]], ["Hiver", [12, 1, 2]]];
    h += '<section><h2>2. Ton calendrier, saison par saison</h2><div class="saisons">';
    saisons.forEach(function (s) {
      var rec = p.lignes.filter(function (l) { return l.c.recolte.some(function (m) { return s[1].indexOf(m) >= 0; }); }).map(function (l) { return esc(l.c.nom); });
      var pla = p.lignes.filter(function (l) { return l.c.plantation && /printemps|mars|avril|mai/.test(l.c.plantation) && s[0] === "Printemps"; }).map(function (l) { return esc(l.c.nom) + " (" + esc(l.c.plantation) + ")"; });
      if (s[0] === "Automne") pla = pla.concat(p.lignes.filter(function (l) { return l.c.id === "fraisier"; }).map(function () { return "Fraisier (fin d'été)"; }));
      if (s[0] === "Automne") pla = pla.concat(p.longues.filter(function (l) { return l.id === "pommier"; }).map(function () { return "Pommier (l'automne est la meilleure période)"; }));
      if (s[0] === "Printemps") pla = pla.concat(p.longues.filter(function (l) { return l.id === "asperge"; }).map(function () { return "Asperge (février à avril)"; }));
      h += '<div class="saison"><h3>' + s[0] + '</h3><p><b>À récolter :</b> ' + (rec.length ? rec.join(", ") : "rien de ta liste") + "</p>" +
        (pla.length ? "<p><b>À planter :</b> " + pla.join(", ") + "</p>" : "") + "</div>";
    });
    h += "</div><div class=\"tab\"><table><thead><tr><th>Culture</th><th>Avant la récolte</th><th>Mois de récolte</th></tr></thead><tbody>";
    p.lignes.forEach(function (l) {
      h += "<tr><td>" + esc(l.c.nom) + "</td><td>" + esc(l.c.delai) + "</td><td>" + l.c.recolte.map(function (m) { return MOIS[m - 1]; }).join(", ") + " <small>" + ligneSrc(l.c) + "</small></td></tr>";
    });
    h += '</tbody></table></div><p class="note">Pour savoir quand semer, compte le délai à rebours depuis le mois où tu veux récolter. Associations de plantes : la plupart des tableaux qui circulent ne sont pas prouvés, ils seront ajoutés quand ils seront sourcés.</p></section>';

    /* Longues */
    if (p.longues.length) {
      h += '<section><h2>3. Fruits et plantes à anticiper</h2><div class="cartes">';
      p.longues.forEach(function (l) {
        h += '<div class="carte' + (l.long ? " longue" : "") + '"><div class="nom">' + esc(l.nom) + (l.long ? ' <span class="tag">long, à anticiper</span>' : "") + "</div><p><b>Première récolte :</b> " + esc(l.delai) + ".</p><p>" + esc(l.detail) + '</p><p class="src">' + ligneSrc(l) + "</p></div>";
      });
      h += '</div><p class="note">Ces plantes ne sont pas comptées dans les calories ni dans le budget : les sources ne donnent pas de rendement fiable pour un jardin. C\'est pour ça qu\'il faut les planter maintenant, avant d\'en avoir besoin.</p></section>';
    }

    /* Conservation */
    h += '<section><h2>' + (p.longues.length ? 4 : 3) + ". Garder tes récoltes sans frigo</h2><div class=\"tab\"><table><thead><tr><th>Culture</th><th>Conservation</th></tr></thead><tbody>";
    p.lignes.forEach(function (l) { h += "<tr><td>" + esc(l.c.nom) + "</td><td>" + esc(l.c.garde) + "</td></tr>"; });
    h += "</tbody></table></div></section>";

    var n = p.longues.length ? 5 : 4;
    h += "<section><h2>" + n + ". Pourquoi chaque culture, et comment la semer</h2>" + (window.PotagerPlan.fiches ? window.PotagerPlan.fiches(p, false) : "") + '<p class="note">Calories au m² : kg par an et surface du modèle (un-jardin-bio.com) multipliés par les calories Ciqual. Conseils de semis relevés sur la fiche Truffaut du sachet recommandé ou sur jardiner-malin, lien sous chaque fiche. Ce qu\'aucune source ne donne est écrit « non chiffré ».</p></section>';
    n++;
    /* Graines */
    h += "<section><h2>" + n + ". Les graines et les plants à acheter</h2><div class=\"tab\"><table><thead><tr><th>Culture</th><th>Petit budget</th><th>Bio ou plus</th></tr></thead><tbody>";
    p.lignes.forEach(function (l) {
      function cell(x) { return lien(x.a.u, euros(x.prix)) + "<br><small>" + x.n + " x " + esc(x.a.lib) + "</small>"; }
      h += "<tr><td>" + esc(l.c.nom) + "</td><td>" + cell(l.bas) + "</td><td>" + cell(l.haut) + "</td></tr>";
    });
    h += '<tr class="tot"><td>Total</td><td class=n>' + euros(p.budget.graines.bas) + "</td><td class=n>" + euros(p.budget.graines.haut) + "</td></tr></tbody></table></div>";
    h += '<p class="note">Prix en ligne chez Truffaut, relevés les 5 et 6 novembre 2026, hors livraison, ils peuvent changer.</p></section>';

    /* Matériel et poules */
    n++;
    h += "<section><h2>" + n + ". Le matériel" + (cmd.poules ? " et les poules" : "") + "</h2>";
    p.budget.postes.forEach(function (po) {
      var m = D.MATERIEL[po.k];
      h += "<h3>" + esc(m.titre) + (po.k === "poules" ? " : " + p.poules + " poules" + (po.mult > 1 ? ", " + po.mult + " poulaillers" : "") : (po.mult > 1 ? " (x" + po.mult + ")" : "")) + (po.k === "poules" ? "" : "") + '</h3><div class="tab"><table><thead><tr><th>Article</th><th>Petit budget</th><th>Durable</th></tr></thead><tbody>';
      m.items.forEach(function (i) {
        var lib = i[5] === "parPoule" ? i[0].replace(" (prix à la poule)", "") + " x" + p.poules : i[0];
        var bas = i[5] === "parPoule" ? i[1] * p.poules + (i[6] || 0) : i[1], haut = i[5] === "parPoule" ? i[3] * p.poules : i[3];
        h += "<tr><td>" + esc(lib) + "</td><td class=n>" + lien(i[2], euros(bas)) + "</td><td class=n>" + lien(i[4], euros(haut)) + "</td></tr>";
      });
      h += "</tbody></table></div>";
    });
    if (p.poules) {
      h += '<p class="note">' + p.poules + " poules : de quoi couvrir la consommation moyenne d'œufs, 224 par personne et par an en France, comptée au bas de la ponte, 280 œufs par poule. Elles pondent " + nb(p.oeufsMin, 0) + " à " + nb(p.oeufsMax, 0) + " œufs par an au mieux (280 à 320 par poule en élevage, " + src("vetagro") + "). La ponte ralentit à l'automne et s'arrête presque en hiver. Enclos couvert : 8 à 10" + NB + "m² minimum pour 2 poules (" + src("m2a") + "), soit 4,5" + NB + "m² par poule et " + nb(p.enclos, 0) + NB + "m² ici (notre estimation), jamais plus du quart du terrain (notre règle). Déclaration en mairie : plus obligatoire partout depuis 2023 (" + src("legifrance") + "), conseillée, et obligatoire si la préfecture la demande en cas de grippe aviaire (Cerfa 15472).</p>";
    }
    h += "<p class=\"note\">Prix Castorama et Truffaut relevés les 5 et 6 novembre 2026. Un jeu d'outils pour le foyer, stockage multiplié par lot de 2 personnes, un poulailler de 4 places par groupe de 4 poules (notre règle de calcul). Non chiffrés : terreau, paillage, voile d'hivernage, marmite pour les bocaux, raccords d'arrosage.</p></section>";

    /* Budget */
    n++;
    h += "<section><h2>" + n + '. Le budget pour démarrer</h2><div class="tab"><table><thead><tr><th>Poste</th><th>Petit budget</th><th>Durable</th></tr></thead><tbody>';
    h += "<tr><td>Graines et plants</td><td class=n>" + euros(p.budget.graines.bas) + "</td><td class=n>" + euros(p.budget.graines.haut) + "</td></tr>";
    p.budget.postes.forEach(function (po) { h += "<tr><td>" + esc(po.titre) + (po.mult > 1 ? " x" + po.mult : "") + "</td><td class=n>" + euros(po.bas) + "</td><td class=n>" + euros(po.haut) + "</td></tr>"; });
    h += '<tr class="tot"><td>Total</td><td class=n>' + euros(p.budget.total.bas) + "</td><td class=n>" + euros(p.budget.total.haut) + "</td></tr></tbody></table></div></section>";

    h += '<section><h2>Les hypothèses de ce plan</h2><ul class="lim">' +
      "<li>Quantités : règle de trois sur le modèle 2 personnes (" + lien("/potager", "longueur-davance.fr/potager") + ").</li>" +
      "<li>Besoin en calories : moyenne homme et femme de l'ANSES, sans tenir compte de l'âge ni de l'activité.</li>" +
      "<li>Blette et fraisier comptés à 0" + NB + "kcal (pas de valeur fiable).</li>" +
      (p.poules ? "<li>Œuf de 58" + NB + "g, enclos de 4,5" + NB + "m² par poule, au plus un quart du terrain.</li>" : "") + "<li>Allées : 20" + NB + "% du terrain cultivé (proportion d'Ecology Action).</li>" +
      "<li>Culture extensive, rendement d'un maraîcher. Un débutant récolte souvent moins.</li></ul></section>";
    return colle(h);
  }

  /* Floute un plan déjà affiché : le texte est remplacé, pas seulement caché. */
  function flouter(racine) {
    racine.querySelectorAll("td, .saison p, .carte p, .alerte p, .note, ul.lim li, .chiffres div:nth-child(n+3) b").forEach(function (el) {
      var w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nds = [], x;
      while ((x = w.nextNode())) nds.push(x);
      nds.forEach(function (tn) { tn.nodeValue = tn.nodeValue.replace(/[A-Za-zÀ-ÿ0-9]/g, "x"); });
      el.querySelectorAll("a").forEach(function (a) { a.removeAttribute("href"); });
      el.classList.add("flou");
    });
  }

  /* La 3D se charge à part (module three.js) : on attend qu'elle soit prête. */
  function vue3d(el, cmd, plan, o) {
    if (!el) return;
    if (window.PotagerPlan.monter3d) window.PotagerPlan.monter3d(el, cmd, plan, o);
    else (window.__potager3dEnAttente = window.__potager3dEnAttente || []).push([el, cmd, plan, o]);
  }

  window.PotagerPlan = { vue3d: vue3d, colle: colle, carte: carte, surface: surface, calculer: calculer, rendre: rendre, flouter: flouter, nb: nb, euros: euros, esc: esc };
})();

/* ---------- Vue du jardin : terrain découpé en bandes, une par culture, et saisons ---------- */
(function () {
  var P = window.PotagerPlan, D = window.POTAGER_DONNEES, NB = " ";
  var COULEURS = ["#c9a227", "#d9822b", "#8c5a2b", "#5f8d3a", "#e07a2e", "#3f7d5c", "#b8a07a", "#2f6b3a", "#7a9a3b", "#9bbf4a", "#7b2d3b", "#6f8f72", "#c0392b", "#d0506e"];
  var SAISONS = [["printemps", "Printemps", [3, 4, 5]], ["ete", "Été", [6, 7, 8]], ["automne", "Automne", [9, 10, 11]], ["hiver", "Hiver", [12, 1, 2]]];

  function aire(pts) { var a = 0; for (var i = 0; i < pts.length; i++) { var j = (i + 1) % pts.length; a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]; } return Math.abs(a) / 2; }
  /* Coupe un polygone par un demi-plan axe-aligné (Sutherland-Hodgman). garde(p) vrai = côté gardé. */
  function couper(pts, axe, v, inf) {
    var out = [];
    function dedans(p) { return inf ? p[axe] <= v : p[axe] >= v; }
    for (var i = 0; i < pts.length; i++) {
      var a = pts[i], b = pts[(i + 1) % pts.length], da = dedans(a), db = dedans(b);
      if (da) out.push(a);
      if (da !== db) { var t = (v - a[axe]) / (b[axe] - a[axe]); var q = [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])]; out.push(q); }
    }
    return out;
  }
  /* Découpe `poly` (pixels) en bandes d'aires proportionnelles à `parts` (somme = 1). */
  function decouper(poly, parts) {
    var xs = poly.map(function (p) { return p[0]; }), ys = poly.map(function (p) { return p[1]; });
    var axe = (Math.max.apply(null, xs) - Math.min.apply(null, xs)) >= (Math.max.apply(null, ys) - Math.min.apply(null, ys)) ? 0 : 1;
    var vals = axe ? ys : xs, mn = Math.min.apply(null, vals), mx = Math.max.apply(null, vals);
    var total = aire(poly), cum = 0, prec = mn, bandes = [];
    parts.forEach(function (f, i) {
      cum += f;
      var cible = cum * total, lo = prec, hi = mx;
      if (i === parts.length - 1) lo = hi = mx;
      for (var k = 0; k < 40 && hi - lo > 0.01; k++) {
        var mid = (lo + hi) / 2, a = aire(couper(poly, axe, mid, true));
        if (a < cible) lo = mid; else hi = mid;
      }
      var cut = (lo + hi) / 2;
      var b = couper(couper(poly, axe, prec, false), axe, cut, true);
      bandes.push(b);
      prec = cut;
    });
    return bandes;
  }
  /* Découpage en carrés (façon planches de potager) : on coupe en deux groupes d'aire égale
     le long du côté le plus long, puis on recommence dans chaque moitié. Ordre conservé. */
  function arbre(poly, parts) {
    if (parts.length === 1) return [poly];
    var tot = parts.reduce(function (a, b) { return a + b; }, 0), cum = 0, k = 0, best = 1, ecart = Infinity;
    for (var i = 0; i < parts.length - 1; i++) { cum += parts[i]; var e = Math.abs(cum - tot / 2); if (e < ecart) { ecart = e; best = i + 1; } }
    var g = parts.slice(0, best), d = parts.slice(best);
    var fg = g.reduce(function (a, b) { return a + b; }, 0) / tot;
    var deux = decouper(poly, [fg, 1 - fg]);
    return arbre(deux[0], g).concat(arbre(deux[1], d));
  }
  /* Forme en coordonnées 0..1 vers pixels 640, proportions gardées. */
  function formeEnPixels(f, marge) {
    var xs = f.map(function (p) { return p[0]; }), ys = f.map(function (p) { return p[1]; });
    var x0 = Math.min.apply(null, xs), y0 = Math.min.apply(null, ys);
    var w = Math.max.apply(null, xs) - x0 || 1, h = Math.max.apply(null, ys) - y0 || 1;
    var e = (640 - 2 * marge) / Math.max(w, h), dx = (640 - w * e) / 2, dy = (640 - h * e) / 2;
    return f.map(function (p) { return [dx + (p[0] - x0) * e, dy + (p[1] - y0) * e]; });
  }
  function centre(pts) {
    if (!pts.length) return null;
    var x = 0, y = 0; pts.forEach(function (p) { x += p[0]; y += p[1]; });
    return [x / pts.length, y / pts.length];
  }
  function masque(s) { return String(s).replace(/[A-Za-zÀ-ÿ0-9]/g, "x"); }

  /* Les morceaux du jardin, dans l'ordre : cultures, poules, reste. Surfaces en m². */
  function morceaux(cmd, plan) {
    var m = [];
    var kA = 1 / (1 - D.K.partAllees);
    plan.lignes.forEach(function (l, i) { if (l.m2) m.push({ id: l.c.id, nom: l.c.nom, m2: l.m2, place: l.m2 * kA, recolte: l.c.recolte, coul: COULEURS[D.CULTURES.indexOf(l.c) % COULEURS.length] }); });
    if (plan.enclos) m.push({ id: "poules", nom: plan.poules + " poules (enclos)", m2: plan.enclos, place: plan.enclos, recolte: [3, 4, 5, 6, 7, 8, 9], coul: "#8a7f72" });
    var occupe = m.reduce(function (a, x) { return a + x.place; }, 0);
    if (cmd.surface_m2 - occupe > 0.5) m.push({ id: "reste", nom: "Libre (pommes de terre en plus ?)", m2: (cmd.surface_m2 - occupe) * (1 - D.K.partAllees), place: cmd.surface_m2 - occupe, recolte: [], coul: "#e9e2d3" });
    return m;
  }

  /* Dessine le jardin dans `boite`. o = { flou, saison } */
  function vue(boite, cmd, plan, o) {
    var forme = cmd.surface_source === "saisie" || cmd.surface_source === "modele";
    return vueMorceaux(boite, { zone: forme ? null : cmd.zone, forme: forme ? cmd.zone : null, surface: cmd.surface_m2 }, morceaux(cmd, plan), o);
  }

  /* Entrée générique, indépendante du potager : n'importe quelle base de plantes peut s'y brancher.
     cadre = { zone: [[lon,lat]...] ou null, forme: [[x,y] entre 0 et 1] ou null, surface }   (ni l'un ni l'autre : carré schématique)
     m = [{ id, nom, m2 (surface plantée), place (m² avec sa part d'allées, facultatif), recolte: [mois 1..12 où la plante « se voit » ou se récolte], coul }]
     o = { flou, saison, motSaison (« en récolte » par défaut, « en fleur » pour un jardin d'agrément) } */
  function vueMorceaux(boite, cadre, m, o) {
    o = o || {};
    var saison = o.saison || "ete";
    var cmd = { zone: cadre.zone };
    var place = function (x) { return x.place || x.m2; };
    var total = m.reduce(function (a, x) { return a + place(x); }, 0) || 1;
    var parts = m.map(function (x) { return place(x) / total; });
    boite.innerHTML = '<div class="saisons-btn noprint" role="group" aria-label="Saison">' + SAISONS.map(function (s) {
      return '<button type="button" data-s="' + s[0] + '" aria-pressed="' + (s[0] === saison) + '">' + s[1] + "</button>";
    }).join("") + '</div><div class="vue"></div><ul class="legende"></ul>';
    var zoneVue = boite.querySelector(".vue");
    var ctrl, poly;
    if (cmd.zone && cmd.zone.length >= 3) {
      var lon = 0, lat = 0; cmd.zone.forEach(function (p) { lon += p[0]; lat += p[1]; });
      ctrl = P.carte(zoneVue, { lon: lon / cmd.zone.length, lat: lat / cmd.zone.length, zone: cmd.zone, dessin: false, sansZone: true, minCote: 20 });
      poly = ctrl.pixels(cmd.zone);
    } else if (cadre.forme && cadre.forme.length >= 3) {
      /* Forme dessinée à main levée, mise à l'échelle de la surface indiquée. */
      poly = formeEnPixels(cadre.forme, 40);
      var sm = cadre.surface || total;
      zoneVue.innerHTML = '<div class="carte-img schema"><svg viewBox="0 0 640 640" xmlns="http://www.w3.org/2000/svg"></svg></div><p class="carte-src">Forme dessinée à main levée, mise à l\'échelle de ' + P.nb(sm, 0) + NB + "m².</p>";
    } else {
      /* Pas de contour : un carré schématique de la bonne surface. */
      var cote = Math.sqrt(total), marge = 40;
      zoneVue.innerHTML = '<div class="carte-img schema"><svg viewBox="0 0 640 640" xmlns="http://www.w3.org/2000/svg"></svg></div><p class="carte-src">Schéma : un carré de ' + P.nb(total, 0) + NB + "m² (" + P.nb(cote, 1) + NB + "m de côté).</p>";
      poly = [[marge, marge], [640 - marge, marge], [640 - marge, 640 - marge], [marge, 640 - marge]];
    }
    var svg = zoneVue.querySelector("svg");
    /* Chaque planche est rétrécie autour de son centre : l'écart visible, ce sont les allées. */
    var bandes = arbre(poly, parts).map(function (b, i) {
      var x = m[i], f = x.place && x.place > x.m2 ? Math.sqrt(x.m2 / x.place) : 1, c = centre(b);
      return f === 1 || !c ? b : b.map(function (p) { return [c[0] + (p[0] - c[0]) * f, c[1] + (p[1] - c[1]) * f]; });
    });
    function dessiner(s) {
      var mois = SAISONS.filter(function (x) { return x[0] === s; })[0][2];
      var h = "";
      bandes.forEach(function (b, i) {
        if (b.length < 3) return;
        var x = m[i], actif = x.id === "reste" || x.recolte.some(function (mm) { return mois.indexOf(mm) >= 0; });
        h += '<polygon points="' + b.map(function (p) { return p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + '" fill="' + x.coul + '" fill-opacity="' + (actif ? 0.92 : 0.28) + '" stroke="#fdfcf9" stroke-width="2"/>';
      });
      bandes.forEach(function (b, i) {
        var c = centre(b); if (!c || aire(b) < 140) return;
        h += '<circle cx="' + c[0].toFixed(1) + '" cy="' + c[1].toFixed(1) + '" r="13" fill="#12192b"/><text x="' + c[0].toFixed(1) + '" y="' + (c[1] + 5).toFixed(1) + '" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="14" fill="#fdfcf9">' + (i + 1) + "</text>";
      });
      svg.innerHTML = (cmd.zone ? svg.innerHTML.split("<!--b-->")[0] : "") + "<!--b-->" + h;
      boite.querySelector(".legende").innerHTML = m.map(function (x, i) {
        var actif = x.id === "reste" || x.recolte.some(function (mm) { return mois.indexOf(mm) >= 0; });
        var nom = o.flou && x.id !== "reste" && x.id !== "poules" ? '<span class="flou">' + masque(x.nom) + "</span>" : P.esc(x.nom);
        return '<li class="' + (actif ? "" : "eteint") + '"><i style="background:' + x.coul + '"></i><b>' + (i + 1) + ".</b> " + nom +
          ' <small>' + (o.flou ? '<span class="flou">' + masque(P.nb(x.m2, 1)) + "</span>" : P.nb(x.m2, 1)) + NB + "m²" + (actif && x.id !== "reste" && x.id !== "poules" ? ", " + (o.motSaison || "en récolte") : "") + "</small></li>";
      }).join("");
      boite.querySelectorAll(".saisons-btn button").forEach(function (bt) { bt.setAttribute("aria-pressed", String(bt.dataset.s === s)); });
    }
    boite.querySelectorAll(".saisons-btn button").forEach(function (bt) { bt.addEventListener("click", function () { dessiner(bt.dataset.s); }); });
    dessiner(saison);
  }

  /* Fiches semis, une par culture choisie. */
  /* « Pourquoi elle est là » : uniquement à partir des chiffres sourcés (kg, surface, calories Ciqual, conservation). */
  function pourquoi(plan, l) {
    var parM2 = function (x) { return x.c.kg2 && x.c.kcal && x.c.m2 ? x.c.kg2 * x.c.kcal * 10 / x.c.m2 : 0; };
    var k = parM2(l);
    var classes = plan.lignes.filter(function (x) { return parM2(x) > 0; }).sort(function (a, b) { return parM2(b) - parM2(a); });
    var t = "Tu l'as choisie. ";
    if (k > 0) {
      var rang = classes.indexOf(l) + 1;
      t += "Environ " + P.nb(k, 0) + " kcal par m² et par an" + (rang === 1 ? ", la plus nourrissante au m² de ton plan" : ", " + rang + "e sur " + classes.length + " de ton plan pour les calories au m²") + ". ";
    } else t += "Pas de valeur calorique fiable pour elle, elle compte pour le goût et la variété. ";
    t += "Conservation : " + l.c.garde.charAt(0).toLowerCase() + l.c.garde.slice(1) + ".";
    return t;
  }

  function fiches(plan, flou) {
    var h = '<div class="cartes">';
    plan.lignes.forEach(function (l) {
      var s = D.SEMIS[l.c.id]; if (!s) return;
      var f = function (t) { return flou ? '<span class="flou">' + masque(t) + "</span>" : P.esc(t); };
      h += '<div class="carte"><div class="nom">' + P.esc(l.c.nom) + "</div><p><b>Pourquoi elle est là :</b> " + f(pourquoi(plan, l)) + "</p><p><b>Quand :</b> " + f(s.quand) + ".</p><p><b>Comment :</b> " + f(s.comment) + "</p>" +
        (s.expo ? "<p><b>Exposition :</b> " + f(s.expo) + "</p>" : "") + '<p class="src">' + (flou ? "" : s.src.map(function (u, i) { return '<a href="' + P.esc(u) + '" target="_blank" rel="noopener">source' + (s.src.length > 1 ? " " + (i + 1) : "") + "</a>"; }).join(", ")) + "</p></div>";
    });
    return h + "</div>";
  }

  /* Estimation honnête du nombre de pages A4 du plan imprimé. */
  function pages(html) {
    var d = document.createElement("div");
    d.style.cssText = "position:absolute;left:-9999px;top:0;width:680px;font:400 15px/1.5 Inter,sans-serif";
    d.innerHTML = html; document.body.appendChild(d);
    var n = Math.max(1, Math.ceil(d.scrollHeight / 980));
    d.remove();
    return n;
  }

  P.vue = vue; P.vueMorceaux = vueMorceaux; P.morceaux = morceaux; P.arbre = arbre; P.formeEnPixels = formeEnPixels; P.COULEURS = COULEURS; P.fiches = fiches; P.pages = pages; P.masque = masque; P.SAISONS = SAISONS;
})();

/* ---------- Croquis à main levée : la forme du terrain quand on ne donne que la surface ---------- */
(function () {
  var P = window.PotagerPlan, NB = " ";
  function aire(pts) { var a = 0; for (var i = 0; i < pts.length; i++) { var j = (i + 1) % pts.length; a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]; } return Math.abs(a) / 2; }
  /* o = { forme: [[x,y] 0..1], surface: fn() -> m², surChange(forme) } */
  function croquis(boite, o) {
    var T = 640, forme = (o.forme || []).map(function (p) { return [p[0] * T, p[1] * T]; });
    var grille = "";
    for (var i = 1; i < 10; i++) grille += '<line x1="' + i * 64 + '" y1="0" x2="' + i * 64 + '" y2="640" stroke="#d9cfbd" stroke-width="1"/><line x1="0" y1="' + i * 64 + '" x2="640" y2="' + i * 64 + '" stroke="#d9cfbd" stroke-width="1"/>';
    boite.innerHTML = '<div class="carte-img schema"><svg viewBox="0 0 640 640" xmlns="http://www.w3.org/2000/svg" style="cursor:crosshair">' + grille + '<g class="trace"></g></svg></div><p class="carte-src croquis-txt"></p>';
    var svg = boite.querySelector("svg"), g = boite.querySelector(".trace"), txt = boite.querySelector(".croquis-txt");
    function maj() {
      var pts = forme.map(function (p) { return p.join(","); }).join(" ");
      g.innerHTML = (forme.length >= 3 ? '<polygon points="' + pts + '" fill="rgba(47,107,58,.25)" stroke="#2f6b3a" stroke-width="4"/>' : '<polyline points="' + pts + '" fill="none" stroke="#2f6b3a" stroke-width="4"/>') +
        forme.map(function (p) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="9" fill="#2f6b3a" stroke="#fdfcf9" stroke-width="3"/>'; }).join("");
      var S = o.surface ? o.surface() : 0;
      if (forme.length >= 3 && S > 0) {
        var e = Math.sqrt(S / aire(forme));
        var xs = forme.map(function (p) { return p[0]; }), ys = forme.map(function (p) { return p[1]; });
        txt.textContent = "Ton terrain : environ " + P.nb((Math.max.apply(null, xs) - Math.min.apply(null, xs)) * e, 0) + NB + "m sur " + P.nb((Math.max.apply(null, ys) - Math.min.apply(null, ys)) * e, 0) + NB + "m, pour " + P.nb(S, 0) + NB + "m².";
      } else txt.textContent = forme.length ? "Encore " + (3 - forme.length) + " coin" + (3 - forme.length > 1 ? "s" : "") + " au minimum." : "Touche la grille à chaque coin de ton terrain.";
      if (o.surChange) o.surChange(forme.length >= 3 ? forme.map(function (p) { return [Math.round(p[0] / T * 1e4) / 1e4, Math.round(p[1] / T * 1e4) / 1e4]; }) : null);
    }
    svg.addEventListener("click", function (ev) {
      if (forme.length >= 40) return;
      var r = svg.getBoundingClientRect();
      forme.push([(ev.clientX - r.left) / r.width * T, (ev.clientY - r.top) / r.height * T]);
      maj();
    });
    maj();
    return { annuler: function () { forme.pop(); maj(); }, effacer: function () { forme = []; maj(); }, maj: maj };
  }
  P.croquis = croquis;
})();
