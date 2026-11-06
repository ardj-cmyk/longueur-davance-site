/* Plan de potager : le jardin en 3D, saison par saison.
   Même découpage que le plan 2D (cultures, allées, enclos), posé sur la forme réelle du terrain.
   Cinématique : la caméra tourne doucement et les saisons défilent seules jusqu'à ce qu'on touche l'écran.
   Hauteur du soleil à midi : 90° - latitude + déclinaison (0° aux équinoxes, +23,44° en été, -23,44° en hiver). */
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const P = window.PotagerPlan, D = window.POTAGER_DONNEES;
const SAISONS = [
  { id: "printemps", nom: "Printemps", mois: [3, 4, 5], decl: 0, ciel: 0xdfeefa, herbe: 0x7fa65a },
  { id: "ete", nom: "Été", mois: [6, 7, 8], decl: 23.44, ciel: 0xcfe6fb, herbe: 0x8aa84e },
  { id: "automne", nom: "Automne", mois: [9, 10, 11], decl: 0, ciel: 0xe9e1d2, herbe: 0x9a9550 },
  { id: "hiver", nom: "Hiver", mois: [12, 1, 2], decl: -23.44, ciel: 0xe3e7ec, herbe: 0xa7ab9a },
];
const actives = [];
const VERT_HIVER = new THREE.Color(0x4f7a3a), PAILLE = new THREE.Color(0xc8b27a);
const HAUTEURS = { tomate: 1.1, courge: 0.45, pomme_de_terre: 0.55, feve: 0.8, haricot_vert: 0.45, poireau: 0.5, chou: 0.45, ail: 0.4, oignon: 0.35, carotte: 0.35, betterave: 0.35 };

/* Contour du terrain en mètres (x vers l'est, z vers le sud), centré sur 0. */
function contourMetres(cmd) {
  const S = cmd.surface_m2;
  const forme = cmd.surface_source === "saisie" || cmd.surface_source === "modele";
  let pts, lat = 46.5;
  if (cmd.zone && cmd.zone.length >= 3 && !forme) {
    lat = cmd.zone.reduce((a, p) => a + p[1], 0) / cmd.zone.length;
    const lon0 = cmd.zone.reduce((a, p) => a + p[0], 0) / cmd.zone.length;
    const kx = 111320 * Math.cos(lat * Math.PI / 180), kz = 110540;
    pts = cmd.zone.map((p) => [(p[0] - lon0) * kx, -(p[1] - lat) * kz]);
  } else if (cmd.zone && cmd.zone.length >= 3) {
    const a = aire(cmd.zone), e = Math.sqrt(S / a);
    pts = cmd.zone.map((p) => [p[0] * e, p[1] * e]);
  } else {
    const c = Math.sqrt(S);
    pts = [[0, 0], [c, 0], [c, c], [0, c]];
  }
  const cx = pts.reduce((a, p) => a + p[0], 0) / pts.length, cz = pts.reduce((a, p) => a + p[1], 0) / pts.length;
  return { pts: pts.map((p) => [p[0] - cx, p[1] - cz]), lat };
}
function aire(pts) { let a = 0; for (let i = 0; i < pts.length; i++) { const j = (i + 1) % pts.length; a += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]; } return Math.abs(a) / 2; }
function centre(pts) { return [pts.reduce((a, p) => a + p[0], 0) / pts.length, pts.reduce((a, p) => a + p[1], 0) / pts.length]; }
function dedans(pt, poly) {
  let c = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [xi, zi] = poly[i], [xj, zj] = poly[j];
    if ((zi > pt[1]) !== (zj > pt[1]) && pt[0] < (xj - xi) * (pt[1] - zi) / (zj - zi) + xi) c = !c;
  }
  return c;
}
function forme2D(pts) {
  const s = new THREE.Shape();
  pts.forEach((p, i) => (i ? s.lineTo(p[0], -p[1]) : s.moveTo(p[0], -p[1])));
  s.closePath();
  return s;
}
/* Plaque horizontale (sol, planche) à partir d'un polygone en mètres. */
function plaque(pts, hauteur, matiere, y0 = 0) {
  const g = new THREE.ExtrudeGeometry(forme2D(pts), { depth: hauteur, bevelEnabled: false });
  g.rotateX(-Math.PI / 2);
  const m = new THREE.Mesh(g, matiere);
  m.position.y = y0;
  m.receiveShadow = true; m.castShadow = hauteur > 0.05;
  return m;
}

export function monter3d(boite, cmd, plan, o = {}) {
  /* Nettoie une scène précédente dans la même boîte. */
  for (let i = actives.length - 1; i >= 0; i--) if (actives[i].boite === boite || !document.body.contains(actives[i].boite)) { actives[i].stop(); actives.splice(i, 1); }
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false }); } catch (e) { boite.innerHTML = ""; return; }

  boite.innerHTML = '<div class="saisons-btn noprint" role="group" aria-label="Saison en 3D"></div><div class="vue3d"><button type="button" class="lecture noprint" aria-label="Pause"></button></div><p class="carte-src">Vue 3D de ton terrain : glisse pour tourner, pince pour zoomer. Les allées sont les passages entre les planches. Le soleil est à sa hauteur de midi pour la saison.</p>';
  const cadre = boite.querySelector(".vue3d"), btns = boite.querySelector(".saisons-btn"), lecture = boite.querySelector(".lecture");
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  cadre.prepend(renderer.domElement);

  const { pts, lat } = contourMetres(cmd);
  const xs = pts.map((p) => p[0]), zs = pts.map((p) => p[1]);
  const taille = Math.max(Math.max(...xs) - Math.min(...xs), Math.max(...zs) - Math.min(...zs), 4);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(40, 1, 0.1, taille * 20);
  camera.position.set(taille * 0.9, taille * 0.85, taille * 1.1);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.maxPolarAngle = Math.PI * 0.47;
  controls.minDistance = taille * 0.4; controls.maxDistance = taille * 3;
  controls.autoRotate = true; controls.autoRotateSpeed = 0.7;

  const hemi = new THREE.HemisphereLight(0xffffff, 0x8a7a60, 0.75); scene.add(hemi);
  const soleil = new THREE.DirectionalLight(0xfff3dc, 1.6);
  soleil.castShadow = true;
  soleil.shadow.mapSize.set(1024, 1024);
  const sc = soleil.shadow.camera; sc.left = sc.bottom = -taille; sc.right = sc.top = taille; sc.far = taille * 6;
  scene.add(soleil, soleil.target);

  /* Sol autour, terrain, allées. */
  const matTour = new THREE.MeshLambertMaterial({ color: 0xc3cba6 });
  const tour = new THREE.Mesh(new THREE.CircleGeometry(taille * 3, 48), matTour);
  tour.rotation.x = -Math.PI / 2; tour.position.y = -0.02; tour.receiveShadow = true; scene.add(tour);
  const matAllee = new THREE.MeshLambertMaterial({ color: 0xd9cba8 });
  scene.add(plaque(pts, 0.02, matAllee));

  /* Planches, enclos, reste : même découpage que le plan 2D. */
  const m = P.morceaux(cmd, plan);
  const tot = m.reduce((a, x) => a + (x.place || x.m2), 0) || 1;
  const morceaux = P.arbre(pts, m.map((x) => (x.place || x.m2) / tot));
  const matTerre = new THREE.MeshLambertMaterial({ color: 0x6b4a32 });
  const matHerbe = new THREE.MeshLambertMaterial({ color: 0x8aa84e });
  const plantes = [];
  const geoFeuille = new THREE.SphereGeometry(1, 8, 6);
  const geoTige = new THREE.ConeGeometry(1, 1, 6);
  morceaux.forEach((b, i) => {
    if (b.length < 3) return;
    const x = m[i], c = centre(b);
    const f = x.place && x.place > x.m2 ? Math.sqrt(x.m2 / x.place) : 1;
    const bed = b.map((p) => [c[0] + (p[0] - c[0]) * f, c[1] + (p[1] - c[1]) * f]);
    if (x.id === "reste") { scene.add(plaque(bed, 0.04, matHerbe)); return; }
    if (x.id === "poules") {
      scene.add(plaque(bed, 0.03, new THREE.MeshLambertMaterial({ color: 0xb59f78 })));
      const piquet = new THREE.MeshLambertMaterial({ color: 0x5a5a5a });
      for (let k = 0; k < bed.length; k++) {
        const a = bed[k], z = bed[(k + 1) % bed.length], L = Math.hypot(z[0] - a[0], z[1] - a[1]);
        const g = new THREE.Mesh(new THREE.BoxGeometry(L, 1.2, 0.03), new THREE.MeshLambertMaterial({ color: 0x9aa39a, transparent: true, opacity: 0.45 }));
        g.position.set((a[0] + z[0]) / 2, 0.6, (a[1] + z[1]) / 2); g.rotation.y = -Math.atan2(z[1] - a[1], z[0] - a[0]); scene.add(g);
        const pq = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1.3, 6), piquet); pq.position.set(a[0], 0.65, a[1]); scene.add(pq);
      }
      const maison = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.8, 0.9), new THREE.MeshLambertMaterial({ color: 0x8c5a2b }));
      maison.position.set(c[0], 0.4, c[1]); maison.castShadow = true; scene.add(maison);
      const toit = new THREE.Mesh(new THREE.ConeGeometry(0.95, 0.5, 4), new THREE.MeshLambertMaterial({ color: 0x7b2d3b }));
      toit.position.set(c[0], 1.05, c[1]); toit.rotation.y = Math.PI / 4; toit.castShadow = true; scene.add(toit);
      const matPoule = new THREE.MeshLambertMaterial({ color: 0xb5651d });
      for (let k = 0; k < (plan.poules || 0); k++) {
        const pt = [c[0] + (Math.random() - 0.5) * 2.2, c[1] + (Math.random() - 0.5) * 2.2];
        if (!dedans(pt, bed)) continue;
        const pl = new THREE.Mesh(new THREE.SphereGeometry(0.16, 8, 6), matPoule); pl.position.set(pt[0], 0.18, pt[1]); pl.castShadow = true; scene.add(pl);
      }
      return;
    }
    scene.add(plaque(bed, 0.18, matTerre));
    /* Plants en quinconce dans la planche, 1 tous les 45 cm (au plus 220 par planche). */
    const bx = bed.map((p) => p[0]), bz = bed.map((p) => p[1]);
    const pas = Math.max(0.45, Math.sqrt(aire(bed) / 220));
    const pos = [];
    for (let px = Math.min(...bx) + pas / 2; px < Math.max(...bx); px += pas)
      for (let pz = Math.min(...bz) + pas / 2; pz < Math.max(...bz); pz += pas)
        if (dedans([px, pz], bed)) pos.push([px, pz]);
    if (!pos.length) return;
    const haut = HAUTEURS[x.id] || HAUTEURS[(x.relais || {}).idA] || 0.4;
    const mat = new THREE.MeshLambertMaterial({ color: new THREE.Color(x.coul) });
    const mesh = new THREE.InstancedMesh(x.id === "poireau" || x.id === "ail" || x.id === "oignon" ? geoTige : geoFeuille, mat, pos.length);
    mesh.castShadow = true;
    plantes.push({ mesh, pos, x, haut, mat, base: new THREE.Color(x.coul), baseB: x.relais ? new THREE.Color(x.relais.coulB) : null });
    scene.add(mesh);
  });

  const mat4 = new THREE.Matrix4(), q = new THREE.Quaternion(), v = new THREE.Vector3(), s3 = new THREE.Vector3();
  const sec = new THREE.Color(0x8a6a45);
  let saisonCourante = o.saison || "ete";
  function appliquer(id) {
    saisonCourante = id;
    const S = SAISONS.find((x) => x.id === id);
    scene.background = new THREE.Color(S.ciel);
    matHerbe.color.setHex(S.herbe);
    const hauteur = (90 - lat + S.decl) * Math.PI / 180;
    soleil.position.set(0, Math.sin(hauteur) * taille * 3, Math.cos(hauteur) * taille * 3); // plein sud à midi
    soleil.intensity = id === "hiver" ? 1.1 : 1.6;
    plantes.forEach((pl) => {
      const r = pl.x.relais;
      let enRecolte = pl.x.recolte.some((mm) => S.mois.includes(mm)), coul = pl.base, hautR = pl.haut;
      if (r) {
        const a = r.recA.some((mm) => S.mois.includes(mm)), b = r.recB.some((mm) => S.mois.includes(mm));
        if (b && !a) { coul = pl.baseB; hautR = HAUTEURS[r.idB] || 0.4; }
        enRecolte = a || b;
      }
      let h = enRecolte ? hautR : hautR * 0.25;
      if (pl.x.couvert && S.id === "hiver") { coul = VERT_HIVER; enRecolte = true; h = 0.28; }
      else if (pl.x.couvert && S.id === "printemps" && !enRecolte) { coul = PAILLE; enRecolte = true; h = 0.06; }
      pl.mat.color.copy(enRecolte ? coul : sec);
      pl.pos.forEach((p, k) => {
        const r = 0.17 + ((k * 37) % 10) / 100;
        v.set(p[0], 0.18 + h / 2, p[1]); s3.set(r, h / 2, r);
        mat4.compose(v, q, s3); pl.mesh.setMatrixAt(k, mat4);
      });
      pl.mesh.instanceMatrix.needsUpdate = true;
    });
    btns.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.s === id)));
  }
  SAISONS.forEach((S) => {
    const b = document.createElement("button");
    b.type = "button"; b.dataset.s = S.id; b.textContent = S.nom;
    b.addEventListener("click", () => { arreterCinematique(); appliquer(S.id); });
    btns.appendChild(b);
  });

  /* Cinématique : saisons qui défilent toutes les 3,5 s, caméra qui tourne. */
  let cine = setInterval(() => {
    const i = SAISONS.findIndex((x) => x.id === saisonCourante);
    appliquer(SAISONS[(i + 1) % 4].id);
  }, 3500);
  function arreterCinematique() { if (cine) { clearInterval(cine); cine = null; } controls.autoRotate = false; lecture.textContent = "▶"; lecture.setAttribute("aria-label", "Relancer la cinématique"); }
  function relancer() { if (!cine) cine = setInterval(() => { const i = SAISONS.findIndex((x) => x.id === saisonCourante); appliquer(SAISONS[(i + 1) % 4].id); }, 3500); controls.autoRotate = true; lecture.textContent = "❚❚"; lecture.setAttribute("aria-label", "Pause"); }
  lecture.textContent = "❚❚";
  lecture.addEventListener("click", () => (cine ? arreterCinematique() : relancer()));
  renderer.domElement.addEventListener("pointerdown", arreterCinematique);

  function taillage() {
    const w = cadre.clientWidth || 600, h = Math.round(w * 0.8);
    renderer.setSize(w, h); camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  const ro = new ResizeObserver(taillage); ro.observe(cadre); taillage();
  appliquer(saisonCourante);
  let raf = 0, vivant = true;
  (function boucle() { if (!vivant) return; controls.update(); renderer.render(scene, camera); raf = requestAnimationFrame(boucle); })();
  actives.push({ boite, stop() { vivant = false; cancelAnimationFrame(raf); if (cine) clearInterval(cine); ro.disconnect(); renderer.dispose(); } });
}

P.monter3d = monter3d;
(window.__potager3dEnAttente || []).forEach((a) => monter3d(...a));
window.__potager3dEnAttente = [];
