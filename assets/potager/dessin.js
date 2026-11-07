/* Plan de potager : le jardin dessiné, vu de biais (perspective isométrique), saison par saison.
   Même découpage que le plan 2D (cultures, allées, poules, clapiers), posé sur la forme réelle du terrain.
   Les volumes sont simples (planches surélevées, socle de terre) mais chaque face reçoit une texture peinte
   (bois, terre, gravier, paille, herbe) et chaque plante, animal ou abri est une illustration détourée,
   posée debout à sa place. Illustrations : générées pour Longueur d'avance (fal.ai Seedream, détourage BiRefNet).
   Les saisons défilent seules jusqu'à ce qu'on touche un bouton. */
(function () {
  var P = window.PotagerPlan, NS = "http://www.w3.org/2000/svg";
  var BASE = "/assets/potager/dessin/";
  function img(n) { var M = window.POTAGER_DESSIN_IMAGES; return M && M[n] ? M[n] : BASE + n + ".webp"; }
  var K = 40;                                    // unités SVG par mètre
  var C30 = Math.cos(Math.PI / 6), S30 = 0.5;
  var TEX = 384;                                 // côté des textures en pixels
  var SAISONS = [
    { id: "printemps", nom: "Printemps", mois: [3, 4, 5], sol: "1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0" },
    { id: "ete", nom: "Été", mois: [6, 7, 8], sol: "1.03 0.03 0 0 0  0.01 0.99 0 0 0  0 0 0.94 0 0  0 0 0 1 0" },
    { id: "automne", nom: "Automne", mois: [9, 10, 11], sol: "1.04 0.1 0 0 0  0.04 0.93 0 0 0  0 0.02 0.85 0 0  0 0 0 1 0" },
    { id: "hiver", nom: "Hiver", mois: [12, 1, 2], sol: "0.75 0.18 0.07 0 0.05  0.14 0.78 0.08 0 0.05  0.14 0.18 0.68 0 0.06  0 0 0 1 0" }
  ];
  /* Largeur et hauteur des illustrations (pixels), pour garder leurs proportions. */
  var DIMS = { ail: [83, 256], betterave: [161, 256], blette: [222, 256], carotte: [166, 256], chou: [256, 213], clapier: [256, 246], courge: [247, 256], courgette: [256, 224], couvert: [256, 244], feve: [138, 256], fraisier: [256, 200], haricot_vert: [132, 256], lapin: [216, 256], oignon: [96, 256], personne: [83, 256], poireau: [195, 256], pomme_de_terre: [256, 233], poulailler: [193, 256], poule: [225, 256], pousse: [256, 251], sec: [237, 256], tomate: [184, 256] };
  /* Écart entre deux pieds (m) : sert à placer et à dimensionner chaque dessin. */
  var PAS = { tomate: 0.6, courge: 1.0, pomme_de_terre: 0.5, feve: 0.35, haricot_vert: 0.55, poireau: 0.3, chou: 0.55, ail: 0.25, oignon: 0.28,
    carotte: 0.3, betterave: 0.3, blette: 0.45, courgette: 0.9, fraisier: 0.4, couvert: 0.35, pousse: 0.3, sec: 0.35 };
  /* Largeur réelle d'un pied adulte vu de biais (m), plafond du dessin : une courge n'est pas plus large qu'une planche. */
  var LARG = { courge: 0.85, courgette: 0.8, pomme_de_terre: 0.55, tomate: 0.5, chou: 0.5, blette: 0.45, haricot_vert: 0.45, feve: 0.35, poireau: 0.28,
    ail: 0.22, oignon: 0.26, carotte: 0.28, betterave: 0.32, fraisier: 0.38, couvert: 0.32, pousse: 0.22, sec: 0.28 };
  /* Les dessins de plantes n'ont que quelques miettes de terre : le pied est presque au bas de l'image. */
  var LIBELLES = { poule: "Poule", lapin: "Lapin", poulailler: "Poulailler", clapier: "Clapier", personne: "Jardinier, 1,75 m pour l'échelle" };
  var D = window.POTAGER_DONNEES;
  var PIED = { personne: 0.98, poule: 0.97, lapin: 0.96, poulailler: 0.97, clapier: 0.98 };
  var ENCRE = "#4a3626";               // trait d'encre commun (style illustration éditoriale)

  /* ---------- Géométrie ---------- */
  function aire(pts) { var a = 0; for (var i = 0; i < pts.length; i++) { var j = (i + 1) % pts.length; a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]; } return a / 2; }
  function centre(pts) { return [pts.reduce(function (a, p) { return a + p[0]; }, 0) / pts.length, pts.reduce(function (a, p) { return a + p[1]; }, 0) / pts.length]; }
  function dedans(pt, poly) {
    var c = false;
    for (var i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      var xi = poly[i][0], zi = poly[i][1], xj = poly[j][0], zj = poly[j][1];
      if ((zi > pt[1]) !== (zj > pt[1]) && pt[0] < (xj - xi) * (pt[1] - zi) / (zj - zi) + xi) c = !c;
    }
    return c;
  }
  /* Contour du terrain en mètres (x vers l'est, z vers le sud), centré sur 0. Même règle que la 3D. */
  function contourMetres(cmd) {
    var S = cmd.surface_m2, pts;
    var forme = cmd.surface_source === "saisie" || cmd.surface_source === "modele";
    if (cmd.zone && cmd.zone.length >= 3 && !forme) {
      var lat = cmd.zone.reduce(function (a, p) { return a + p[1]; }, 0) / cmd.zone.length;
      var lon0 = cmd.zone.reduce(function (a, p) { return a + p[0]; }, 0) / cmd.zone.length;
      var kx = 111320 * Math.cos(lat * Math.PI / 180), kz = 110540;
      pts = cmd.zone.map(function (p) { return [(p[0] - lon0) * kx, -(p[1] - lat) * kz]; });
    } else if (cmd.zone && cmd.zone.length >= 3) {
      var e = Math.sqrt(S / Math.abs(aire(cmd.zone)));
      pts = cmd.zone.map(function (p) { return [p[0] * e, p[1] * e]; });
    } else {
      var c = Math.sqrt(S);
      pts = [[0, 0], [c, 0], [c, c], [0, c]];
    }
    var cc = centre(pts);
    return pts.map(function (p) { return [p[0] - cc[0], p[1] - cc[1]]; });
  }
  /* Projection isométrique : vue depuis le sud-est, y vers le haut. */
  function iso(x, z, y) { return [(x - z) * C30 * K, ((x + z) * S30 - (y || 0)) * K]; }
  function f1(v) { return v.toFixed(1); }
  function chemin(pts, y) { return "M" + pts.map(function (p) { var q = iso(p[0], p[1], y); return f1(q[0]) + " " + f1(q[1]); }).join("L") + "Z"; }
  function decaler(pts, d) {
    var c = centre(pts);
    return pts.map(function (p) { var dx = p[0] - c[0], dz = p[1] - c[1], l = Math.hypot(dx, dz) || 1; return [p[0] + dx / l * d, p[1] + dz / l * d]; });
  }

  /* Motifs : une texture posée à plat (dessus) ou debout le long d'un bord (côtés), en mètres. */
  function motifDessus(id, fichier, metres, tourne) {
    /* tourne : rotation de la texture dans le plan du sol (degrés), pour casser la répétition quand on superpose deux couches. */
    var s = TEX / metres, t = (tourne || 0) * Math.PI / 180, cs = Math.cos(t) / s, sn = Math.sin(t) / s;
    var a = (cs - sn) * C30 * K, b = (cs + sn) * S30 * K, c = (-sn - cs) * C30 * K, d = (-sn + cs) * S30 * K;
    return '<pattern id="' + id + '" width="' + TEX + '" height="' + TEX + '" patternUnits="userSpaceOnUse" patternTransform="matrix(' + [a, b, c, d, 0, 0].map(function (v) { return v.toFixed(4); }).join(" ") + ')">' +
      '<image href="' + img(fichier) + '" width="' + TEX + '" height="' + TEX + '"/></pattern>';
  }
  function motifCote(id, fichier, metres, sens) {   // sens 1 : le long de x, -1 : le long de z
    var s = TEX / metres;
    return '<pattern id="' + id + '" width="' + TEX + '" height="' + TEX + '" patternUnits="userSpaceOnUse" patternTransform="matrix(' + [sens * C30 * K / s, S30 * K / s, 0, K / s, 0, 0].map(function (v) { return v.toFixed(4); }).join(" ") + ')">' +
      '<image href="' + img(fichier) + '" width="' + TEX + '" height="' + TEX + '"/></pattern>';
  }
  /* Faces de côté visibles d'un bloc posé entre y0 et y1, texturées selon leur orientation. */
  function cotes(pts, y0, y1, matiere, ombre) {
    var s = "", sens = aire(pts) > 0 ? 1 : -1;
    for (var i = 0; i < pts.length; i++) {
      var a = pts[i], b = pts[(i + 1) % pts.length];
      var nx = (b[1] - a[1]) * sens, nz = -(b[0] - a[0]) * sens;      // normale extérieure
      if (nx + nz <= 0) continue;
      var q = [iso(a[0], a[1], y0), iso(b[0], b[1], y0), iso(b[0], b[1], y1), iso(a[0], a[1], y1)];
      var d = "M" + q.map(function (p) { return f1(p[0]) + " " + f1(p[1]); }).join("L") + "Z";
      var leLongDeX = Math.abs(nz) >= Math.abs(nx);
      s += (matiere === "terre" ? '<path d="' + d + '" fill="#a07a56"/>' : "") + '<path d="' + d + '" fill="url(#' + matiere + (leLongDeX ? "-x" : "-z") + ')"' + (matiere === "terre" ? ' opacity=".6"' : "") + "/>" +
        
        '<path d="' + d + '" fill="#5a3e28" opacity="' + (leLongDeX ? ombre : ombre + 0.12) + '"/>' +
        '<path d="' + d + '" fill="none" stroke="' + ENCRE + '" stroke-width="1" stroke-linejoin="round" opacity=".7"/>';
    }
    return s;
  }

  /* ---------- Le dessin ---------- */
  function monterDessin(boite, cmd, plan, o) {
    o = o || {};
    if (!boite) return;
    if (boite.__arret) boite.__arret();
    var pts = contourMetres(cmd);
    var m = P.morceaux(cmd, plan);
    var tot = m.reduce(function (a, x) { return a + (x.place || x.m2); }, 0) || 1;
    var blocs = P.arbre(pts, m.map(function (x) { return (x.place || x.m2) / tot; }));
    var hautPlanche = 0.28, epais = 0.45;

    var bord = decaler(pts, 1.4);
    var proj = bord.map(function (p) { return iso(p[0], p[1], 0); }).concat(bord.map(function (p) { return iso(p[0], p[1], -epais); })).concat(pts.map(function (p) { return iso(p[0], p[1], 2.2); }));
    var minX = Math.min.apply(null, proj.map(function (q) { return q[0]; })) - 10, maxX = Math.max.apply(null, proj.map(function (q) { return q[0]; })) + 10;
    var minY = Math.min.apply(null, proj.map(function (q) { return q[1]; })) - 10, maxY = Math.max.apply(null, proj.map(function (q) { return q[1]; })) + 26;

    boite.innerHTML = '<div class="saisons-btn noprint" role="group" aria-label="Saison du dessin"></div><div class="dessin-jardin"><div class="bulle" hidden></div></div>' +
      '<p class="carte-src">Ton terrain dessiné vu de biais, à l\'échelle : planches, allées' + (plan.poules ? ", poulailler" : "") + (plan.lapines ? ", clapiers" : "") +
      ". Le jardinier mesure 1,75 m. Touche une saison pour la voir. Illustrations créées pour Longueur d'avance.</p>";
    var btns = boite.querySelector(".saisons-btn"), zone = boite.querySelector(".dessin-jardin");
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", [minX, minY, maxX - minX, maxY - minY].map(function (v) { return v.toFixed(0); }).join(" "));
    svg.setAttribute("role", "img"); svg.setAttribute("aria-label", "Dessin du jardin vu de biais");
    svg.style.cssText = "display:block;width:100%;height:auto";
    zone.appendChild(svg);

    var defs = "<defs>" +
      motifDessus("t-terre", "tex-terre", 2.4) + motifDessus("t-gravier", "tex-gravier", 3.2) + motifDessus("t-herbe", "tex-herbe", 4.4) + motifDessus("t-herbe2", "tex-herbe", 2.9, 37) + motifDessus("t-terre2", "tex-terre", 1.7, 61) + motifDessus("t-paille", "tex-paille", 2.4) +
      motifCote("bois-x", "tex-bois", 1.4, 1) + motifCote("bois-z", "tex-bois", 1.4, -1) + motifCote("terre-x", "tex-terre", 2.8, 1) + motifCote("terre-z", "tex-terre", 2.8, -1) + motifCote("terre2-x", "tex-terre", 1.9, 1) + motifCote("terre2-z", "tex-terre", 1.9, -1) +
      '<filter id="d-saison" color-interpolation-filters="sRGB"><feColorMatrix id="d-saison-m" type="matrix" values="' + SAISONS[0].sol + '"/></filter>' +
      '<filter id="d-flou"><feGaussianBlur stdDeviation="7"/></filter></defs>';

    var lits = [];
    blocs.forEach(function (b, i) {
      if (b.length < 3) return;
      var x = m[i], c = centre(b);
      var f = x.place && x.place > x.m2 ? Math.sqrt(x.m2 / x.place) : 1;
      lits.push({ x: x, c: c, bed: b.map(function (p) { return [c[0] + (p[0] - c[0]) * f, c[1] + (p[1] - c[1]) * f]; }) });
    });

    /* Une illustration debout, pied en (x, z) à la hauteur y, large de `larg` mètres. */
    /* nomLu : ce qui s'affiche au survol (ou au toucher sur téléphone). */
    function dessin(nom, x, z, y, larg, miroir, nomLu) {
      var dm = DIMS[nom], q = iso(x, z, y), w = larg * K, h = w * dm[1] / dm[0], pied = PIED[nom] || 0.96;
      var X = q[0] - w / 2, Y = q[1] - h * pied, lu = P.esc(nomLu || LIBELLES[nom] || nom);
      return { prof: x + z, s: '<image href="' + img(nom) + '" x="' + f1(X) + '" y="' + f1(Y) + '" width="' + f1(w) + '" height="' + f1(h) + '" data-nom="' + lu + '"' +
        (miroir ? ' transform="matrix(-1 0 0 1 ' + f1(2 * q[0]) + ' 0)"' : "") + "><title>" + lu + "</title></image>" };
    }
    function grille(bed, pas, max) {
      var a = Math.abs(aire(bed)); pas = Math.max(pas, Math.sqrt(a / max));
      var xs = bed.map(function (p) { return p[0]; }), zs = bed.map(function (p) { return p[1]; }), out = [], ligne = 0;
      for (var z = Math.min.apply(null, zs) + pas / 2; z < Math.max.apply(null, zs); z += pas, ligne++)
        /* Quinconce : un rang sur deux décalé d'un demi-pas, les rangs restent droits mais deux pieds ne se cachent plus l'un l'autre. */
        for (var x = Math.min.apply(null, xs) + pas / 2 + (ligne % 2 ? pas / 2 : 0); x < Math.max.apply(null, xs); x += pas)
          if (dedans([x, z], bed)) out.push([x, z, ligne]);
      return { pos: out, pas: pas };
    }

    function dessiner(sid) {
      var S = SAISONS.filter(function (s) { return s.id === sid; })[0];
      var fond = "", objets = [];
      fond += '<ellipse cx="' + ((minX + maxX) / 2).toFixed(0) + '" cy="' + (maxY - 30).toFixed(0) + '" rx="' + ((maxX - minX) * 0.42).toFixed(0) + '" ry="24" fill="#5a3e28" opacity=".14" filter="url(#d-flou)"/>';
      /* Socle en coupe, herbe autour, allées en gravier. */
      fond += cotes(bord, -epais, 0, "terre", 0.28);
      var herbe = function (d) { return '<path d="' + d + '" fill="#c4cb9c"/><path d="' + d + '" fill="url(#t-herbe)" opacity=".9"/><path d="' + d + '" fill="url(#t-herbe2)" opacity=".25"/><path d="' + d + '" fill="none" stroke="' + ENCRE + '" stroke-width="1.2" stroke-linejoin="round" opacity=".55"/>'; };
      var sol = herbe(chemin(bord, 0)) + '<path d="' + chemin(pts, 0) + '" fill="#ece2cc"/><path d="' + chemin(pts, 0) + '" fill="url(#t-gravier)" opacity=".9"/>';

      lits.forEach(function (L) {
        var x = L.x, bed = L.bed, c = L.c;
        if (x.id === "reste") { sol += herbe(chemin(bed, 0)); return; }
        if (x.id === "poules") {
          sol += '<path d="' + chemin(bed, 0) + '" fill="#e8d098"/><path d="' + chemin(bed, 0) + '" fill="url(#t-paille)" opacity=".9" stroke="' + ENCRE + '" stroke-width="1" stroke-linejoin="round" stroke-opacity=".6"/>';
          objets.push(dessin("poulailler", c[0] - 0.3, c[1] - 0.3, 0, 1.5));
          for (var k = 0; k < (plan.poules || 0); k++) {
            var ang = k * 2.4 + 0.6, r = 1.0 + (k % 3) * 0.35, pt = [c[0] + Math.cos(ang) * r, c[1] + Math.sin(ang) * r];
            if (dedans(pt, bed)) objets.push(dessin("poule", pt[0], pt[1], 0, 0.5, k % 2 === 1));
          }
          clotures(bed).forEach(function (o2) { objets.push(o2); });
          return;
        }
        if (x.id === "lapins") {
          sol += '<path d="' + chemin(bed, 0) + '" fill="#e8d098"/><path d="' + chemin(bed, 0) + '" fill="url(#t-paille)" opacity=".9" stroke="' + ENCRE + '" stroke-width="1" stroke-linejoin="round" stroke-opacity=".6"/>';
          var n2 = (plan.lapines || 1) + 1;
          for (var j = 0; j < n2; j++) {
            var t = j - (n2 - 1) / 2;
            objets.push(dessin("clapier", c[0] + t * 0.6, c[1] - t * 0.6, 0, 0.95, j % 2 === 1));
          }
          objets.push(dessin("lapin", c[0] + 0.55, c[1] + 0.55, 0, 0.42));
          return;
        }
        /* Planche surélevée : côtés en bois, dessus en terre (ou engrais vert l'hiver). */
        objets.push({ prof: -1e6 + c[0] + c[1], s: cotes(bed, 0, hautPlanche, "bois", 0.05) +
          '<path d="' + chemin(bed, hautPlanche) + '" fill="#a67c58"/>' + '<path d="' + chemin(bed, hautPlanche) + '" fill="url(#t-terre)" opacity=".95"/>' +
          '<path d="' + chemin(bed, hautPlanche) + '" fill="transparent" stroke="' + ENCRE + '" stroke-width="1.3" stroke-linejoin="round" data-nom="Planche : ' + P.esc(x.nom.toLowerCase()) + '"><title>' + P.esc(x.nom) + "</title></path>" });
        plantes(L, S).forEach(function (o2) { objets.push(o2); });
      });
      /* Le jardinier, au coin le plus proche, pour l'échelle. */
      var coin = pts.reduce(function (a, p) { return p[0] + p[1] > a[0] + a[1] ? p : a; }, pts[0]);
      var dp = DIMS.personne;
      objets.push(dessin("personne", coin[0] + 0.6, coin[1] + 0.6, 0, 1.75 * dp[0] / dp[1] / (PIED.personne)));

      objets.sort(function (a, b) { return a.prof - b.prof; });
      svg.innerHTML = defs + fond + '<g filter="url(#d-saison)">' + sol + "</g>" + objets.map(function (x) { return x.s; }).join("");
      svg.querySelector("#d-saison-m").setAttribute("values", S.sol);
      btns.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.s === sid)); });
    }

    function plantes(L, S) {
      var x = L.x, r = x.relais, out = [];
      var dans = function (rec) { return rec.some(function (mm) { return S.mois.indexOf(mm) >= 0; }); };
      var aOn = r ? dans(r.recA) : dans(x.recolte), bOn = r ? dans(r.recB) : false;
      var pousse = S.id === "printemps" || S.id === "ete";
      var id = r ? r.idA : x.id, etat = aOn ? "recolte" : pousse ? "pousse" : "sec";
      if (x.couvert && S.id === "hiver") { id = "couvert"; etat = "recolte"; }
      else if (x.couvert && S.id === "printemps" && !aOn) {
        out.push({ prof: -1e5 + L.c[0] + L.c[1], s: '<path d="' + chemin(L.bed, hautPlanche + 0.01) + '" fill="url(#t-paille)" data-nom="Engrais vert fauché, laissé en paillis"/>' });
        return out;
      } else if (r && bOn && !aOn) { id = r.idB; etat = "recolte"; }
      function vu(id, etat) {
        var nom = etat === "recolte" ? (DIMS[id] ? id : "pousse") : etat, taille = 1;
        if (etat === "pousse" && S.id === "ete" && DIMS[id]) { nom = id; taille = 0.75; }
        var c0 = D.CULTURES.filter(function (c) { return c.id === id; })[0], nc = c0 ? c0.nom.replace(/ \(.*\)/, "") : "";
        var lu = id === "couvert" ? "Engrais vert d'hiver (seigle, vesce, féveroles)" : etat === "recolte" ? nc + ", en récolte" : etat === "pousse" ? nc + ", en train de pousser" : nc + ", récolte finie";
        return { nom: nom, lu: lu, etat: etat, taille: taille };
      }
      var A = vu(id, etat), B = null, as = x.assoc;
      /* Association : le compagnon occupe un rang sur deux (rangs alternés) ou un sur trois (entre les pieds). */
      if (as && id !== "couvert") {
        A = vu(as.idA, dans(as.recA) ? "recolte" : pousse ? "pousse" : "sec");
        B = vu(as.idB, dans(as.recB) ? "recolte" : pousse ? "pousse" : "sec");
      }
      var pasG = Math.max(PAS[A.nom] || 0.35, B ? PAS[B.nom] || 0.35 : 0) * (A.etat === "recolte" ? 1.1 : 1);
      var g = grille(L.bed, pasG, B ? 36 : 26), pas = B ? (as.type === "rangs" ? 2 : 3) : 0;
      g.pos.forEach(function (p, k) {
        var V = B && p[2] % pas === 1 ? B : A;
        if (V.etat === "sec" && k % 2) return;
        var v = 0.92 + ((k * 37) % 10) / 60, larg = Math.min(g.pas * 0.95, LARG[V.nom] || 0.35) * v * V.taille;
        out.push(dessin(V.nom, p[0], p[1], hautPlanche, larg, (k * 7) % 3 === 0, V.lu));
      });
      return out;
    }
    function clotures(bed) {
      var out = [];
      for (var i = 0; i < bed.length; i++) {
        var a = bed[i], b = bed[(i + 1) % bed.length], L = Math.hypot(b[0] - a[0], b[1] - a[1]), n = Math.max(1, Math.round(L));
        for (var k = 0; k < n; k++) {
          var p0 = [a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n], p1 = [a[0] + (b[0] - a[0]) * (k + 1) / n, a[1] + (b[1] - a[1]) * (k + 1) / n];
          var q = [iso(p0[0], p0[1], 0), iso(p1[0], p1[1], 0), iso(p1[0], p1[1], 1.1), iso(p0[0], p0[1], 1.1)];
          out.push({ prof: (p0[0] + p1[0] + p0[1] + p1[1]) / 2 + 0.02, s: '<path d="M' + f1(q[3][0]) + " " + f1(q[3][1]) + "L" + f1(q[2][0]) + " " + f1(q[2][1]) + "M" + f1((q[0][0] + q[3][0]) / 2) + " " + f1((q[0][1] + q[3][1]) / 2) + "L" + f1((q[1][0] + q[2][0]) / 2) + " " + f1((q[1][1] + q[2][1]) / 2) + '" stroke="#8d8577" stroke-width="1" opacity=".8"/>' +
            '<path d="M' + f1(q[0][0]) + " " + f1(q[0][1]) + "L" + f1(q[3][0]) + " " + f1(q[3][1]) + '" stroke="#7d6a52" stroke-width="3" stroke-linecap="round"/>' });
        }
      }
      return out;
    }

    var courante = o.saison || "ete";
    SAISONS.forEach(function (S) {
      var b = document.createElement("button");
      b.type = "button"; b.dataset.s = S.id; b.textContent = S.nom;
      b.addEventListener("click", function () { arret(); courante = S.id; dessiner(S.id); });
      btns.appendChild(b);
    });
    var cine = o.fixe ? null : setInterval(function () {
      if (!document.body.contains(svg)) { arret(); return; }
      var i = SAISONS.findIndex(function (s) { return s.id === courante; });
      courante = SAISONS[(i + 1) % 4].id; dessiner(courante);
    }, 3800);
    function arret() { if (cine) { clearInterval(cine); cine = null; } }
    boite.__arret = arret;
    svg.addEventListener("pointerdown", arret);
    /* Bulle : le nom de ce qu'on survole à la souris, ou de ce qu'on touche du doigt (3 secondes). */
    var bulle = zone.querySelector(".bulle"), minuterie = null;
    function montrer(e) {
      var t = e.target.closest && e.target.closest("[data-nom]");
      if (!t) { if (e.pointerType !== "touch") bulle.hidden = true; return; }
      var r = zone.getBoundingClientRect();
      bulle.textContent = t.getAttribute("data-nom");
      bulle.style.left = Math.min(Math.max(e.clientX - r.left, 70), r.width - 70) + "px";
      bulle.style.top = (e.clientY - r.top) + "px";
      bulle.hidden = false;
      if (e.pointerType === "touch") { clearTimeout(minuterie); minuterie = setTimeout(function () { bulle.hidden = true; }, 3000); }
    }
    svg.addEventListener("pointermove", function (e) { if (e.pointerType !== "touch") montrer(e); });
    svg.addEventListener("pointerdown", montrer);
    svg.addEventListener("pointerleave", function (e) { if (e.pointerType !== "touch") bulle.hidden = true; });
    dessiner(courante);
  }

  P.monterDessin = monterDessin;
})();
