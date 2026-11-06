/* Plan de potager : silhouettes 3D des plantes, en formes simples (low poly) et couleurs par sommet.
   Chaque modèle est une seule géométrie (pour l'instanciation), base au sol (y = 0), en mètres. */
import * as THREE from "three";
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";

const C = (h) => new THREE.Color(h);
const VERT = C(0x3f7a35), VERT_CLAIR = C(0x7fb04f), VERT_BLEU = C(0x6f9f86), VERT_FONCE = C(0x2f5a2a);

/* Une pièce : géométrie + couleur + position, rotation, échelle. */
function piece(geo, couleur, p = [0, 0, 0], r = [0, 0, 0], s = [1, 1, 1]) {
  let g = geo.clone();
  if (g.index) g = g.toNonIndexed();
  g.deleteAttribute("uv");
  const m = new THREE.Matrix4().compose(new THREE.Vector3(...p), new THREE.Quaternion().setFromEuler(new THREE.Euler(...r)), new THREE.Vector3(...s));
  g.applyMatrix4(m);
  const n = g.attributes.position.count, col = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) { col[i * 3] = couleur.r; col[i * 3 + 1] = couleur.g; col[i * 3 + 2] = couleur.b; }
  g.setAttribute("color", new THREE.BufferAttribute(col, 3));
  return g;
}
const SPH = new THREE.SphereGeometry(1, 7, 5);
const CONE = new THREE.ConeGeometry(1, 1, 5);
const CYL = new THREE.CylinderGeometry(1, 1, 1, 6);
const BOITE = new THREE.BoxGeometry(1, 1, 1);
const rond = (k, n) => (k / n) * Math.PI * 2;

/* Feuille aplatie, inclinée vers l'extérieur. */
function feuille(couleur, angle, longueur, hauteur, inclinaison = 0.6, largeur = 0.4) {
  const L = longueur;
  return piece(SPH, couleur, [Math.cos(angle) * L * 0.6, hauteur, Math.sin(angle) * L * 0.6], [0, -angle, inclinaison], [L * 0.6, 0.012, L * largeur * 0.6]);
}

const MODELES = {
  carotte: () => {
    const p = [piece(CONE, C(0xe07a2e), [0, 0.02, 0], [Math.PI, 0, 0], [0.025, 0.07, 0.025])];
    for (let k = 0; k < 7; k++) { const a = rond(k, 7); p.push(piece(CONE, VERT_CLAIR, [Math.cos(a) * 0.05, 0.15, Math.sin(a) * 0.05], [Math.sin(a) * 0.35, 0, -Math.cos(a) * 0.35], [0.018, 0.28, 0.018])); }
    return p;
  },
  chou: () => {
    const p = [piece(SPH, C(0xa9d39a), [0, 0.13, 0], [0, 0, 0], [0.12, 0.11, 0.12])];
    for (let k = 0; k < 6; k++) p.push(feuille(C(0x5e9a6e), rond(k, 6), 0.32, 0.09, 0.35, 0.55));
    return p;
  },
  pomme_de_terre: () => {
    const p = [];
    [[0, 0.22, 0, 0.13], [0.09, 0.16, 0.05, 0.1], [-0.08, 0.17, 0.06, 0.1], [0.02, 0.15, -0.1, 0.1], [0, 0.32, 0, 0.08]].forEach(([x, y, z, r]) => p.push(piece(SPH, VERT, [x, y, z], [0, 0, 0], [r, r * 0.8, r])));
    [[0.05, 0.36, 0.02], [-0.04, 0.34, -0.03]].forEach((q) => p.push(piece(SPH, C(0xf2efe6), q, [0, 0, 0], [0.018, 0.018, 0.018])));
    return p;
  },
  tomate: () => {
    const p = [piece(CYL, C(0x8c6a45), [0, 0.6, 0], [0, 0, 0], [0.012, 1.2, 0.012])];
    [[0.06, 0.35, 0, 0.13], [-0.05, 0.6, 0.03, 0.12], [0.03, 0.85, -0.03, 0.1]].forEach(([x, y, z, r]) => p.push(piece(SPH, VERT_FONCE, [x, y, z], [0, 0, 0], [r, r * 1.2, r])));
    [[0.13, 0.4, 0.04], [-0.1, 0.55, 0.1], [0.08, 0.7, -0.1], [-0.07, 0.3, -0.08]].forEach((q) => p.push(piece(SPH, C(0xd23a2a), q, [0, 0, 0], [0.04, 0.04, 0.04])));
    return p;
  },
  courge: () => {
    const p = [];
    for (let k = 0; k < 5; k++) p.push(feuille(VERT, rond(k, 5) + 0.3, 0.45, 0.08, 0.15, 0.8));
    p.push(piece(SPH, C(0xd9a35b), [0.2, 0.07, 0.05], [0, 0.4, Math.PI / 2], [0.07, 0.15, 0.07]));
    p.push(piece(SPH, C(0xd9a35b), [0.2, 0.06, 0.15], [0, 0.4, 0], [0.085, 0.08, 0.085]));
    return p;
  },
  courgette: () => {
    const p = [];
    for (let k = 0; k < 6; k++) p.push(feuille(VERT_FONCE, rond(k, 6), 0.42, 0.18, 0.45, 0.75));
    p.push(piece(CYL, C(0x2f5a2a), [0.12, 0.05, 0.1], [0, 0.6, Math.PI / 2], [0.035, 0.22, 0.035]));
    return p;
  },
  poireau: () => {
    const p = [piece(CYL, C(0xe9efd8), [0, 0.12, 0], [0, 0, 0], [0.025, 0.24, 0.025])];
    for (let k = 0; k < 4; k++) { const a = k % 2 ? 0.35 : -0.35; p.push(piece(BOITE, VERT_BLEU, [0, 0.32 + k * 0.03, 0], [0, k * 0.2, a], [0.04, 0.3, 0.008])); }
    return p;
  },
  oignon: () => {
    const p = [piece(SPH, C(0xc99a4a), [0, 0.04, 0], [0, 0, 0], [0.045, 0.04, 0.045])];
    for (let k = 0; k < 5; k++) { const a = rond(k, 5); p.push(piece(CYL, VERT_BLEU, [Math.cos(a) * 0.01, 0.2, Math.sin(a) * 0.01], [Math.sin(a) * 0.12, 0, -Math.cos(a) * 0.12], [0.007, 0.32, 0.007])); }
    return p;
  },
  ail: () => {
    const p = [piece(SPH, C(0xf0ece0), [0, 0.035, 0], [0, 0, 0], [0.035, 0.035, 0.035])];
    for (let k = 0; k < 4; k++) { const a = rond(k, 4); p.push(piece(BOITE, VERT_BLEU, [0, 0.18, 0], [Math.sin(a) * 0.2, a, -Math.cos(a) * 0.2], [0.02, 0.3, 0.004])); }
    return p;
  },
  haricot_vert: () => {
    const p = [];
    [[0, 0.18, 0, 0.1], [0.08, 0.13, 0.04, 0.08], [-0.07, 0.13, -0.05, 0.08]].forEach(([x, y, z, r]) => p.push(piece(SPH, VERT_CLAIR, [x, y, z], [0, 0, 0], [r, r * 0.8, r])));
    [[0.1, 0.07, 0.07], [-0.09, 0.08, 0.02], [0.02, 0.07, -0.1]].forEach((q) => p.push(piece(CYL, C(0x6aa84f), q, [0.3, 0, 0.2], [0.008, 0.1, 0.008])));
    return p;
  },
  feve: () => {
    const p = [];
    for (let k = 0; k < 3; k++) {
      const x = (k - 1) * 0.05;
      p.push(piece(CYL, VERT, [x, 0.35, 0], [0, 0, 0], [0.012, 0.7, 0.012]));
      for (let j = 0; j < 4; j++) p.push(piece(SPH, C(0x5e8c4a), [x + 0.03, 0.2 + j * 0.13, 0.02], [0, 0, 0], [0.04, 0.025, 0.03]));
    }
    p.push(piece(CYL, C(0x7a9a50), [0.07, 0.3, 0.04], [0, 0, 0.3], [0.015, 0.14, 0.015]));
    return p;
  },
  betterave: () => {
    const p = [piece(SPH, C(0x7b1f3b), [0, 0.04, 0], [0, 0, 0], [0.055, 0.05, 0.055])];
    for (let k = 0; k < 5; k++) p.push(feuille(C(0x4f7a3a), rond(k, 5), 0.22, 0.14, 0.9, 0.45));
    return p;
  },
  blette: () => {
    const p = [];
    for (let k = 0; k < 5; k++) {
      const a = rond(k, 5);
      p.push(piece(CYL, C(0xf3f1e6), [Math.cos(a) * 0.03, 0.1, Math.sin(a) * 0.03], [Math.sin(a) * 0.2, 0, -Math.cos(a) * 0.2], [0.012, 0.2, 0.012]));
      p.push(piece(SPH, C(0x3f8a3a), [Math.cos(a) * 0.08, 0.3, Math.sin(a) * 0.08], [Math.sin(a) * 0.3, -a, -Math.cos(a) * 0.3], [0.07, 0.15, 0.015]));
    }
    return p;
  },
  fraisier: () => {
    const p = [];
    for (let k = 0; k < 6; k++) p.push(feuille(VERT, rond(k, 6), 0.16, 0.07, 0.4, 0.8));
    [[0.07, 0.03, 0.02], [-0.04, 0.03, 0.07], [0.0, 0.03, -0.08]].forEach((q) => p.push(piece(CONE, C(0xd22a3a), q, [Math.PI, 0, 0], [0.02, 0.04, 0.02])));
    return p;
  },
  /* Engrais vert d'hiver : touffes de seigle et de vesce. */
  couvert: () => {
    const p = [];
    for (let k = 0; k < 9; k++) { const a = rond(k, 9), d = 0.03 + (k % 3) * 0.04; p.push(piece(CONE, k % 3 ? C(0x5f9a3e) : C(0x4a7a30), [Math.cos(a) * d, 0.13, Math.sin(a) * d], [Math.sin(a) * 0.15, 0, -Math.cos(a) * 0.15], [0.012, 0.26, 0.012])); }
    return p;
  },
};
/* Cultures plus hautes que larges : on les espace un peu moins. */
export const ESPACEMENT = { tomate: 0.5, courge: 0.7, courgette: 0.7, chou: 0.5, pomme_de_terre: 0.4, poireau: 0.18, oignon: 0.15, ail: 0.15, carotte: 0.12, betterave: 0.2, blette: 0.35, feve: 0.25, haricot_vert: 0.3, fraisier: 0.35, couvert: 0.2 };

const cache = {};
export function modele(id) {
  if (cache[id]) return cache[id];
  const f = MODELES[id] || (() => [piece(SPH, VERT, [0, 0.15, 0], [0, 0, 0], [0.15, 0.15, 0.15])]);
  cache[id] = mergeGeometries(f());
  cache[id].computeVertexNormals();
  return cache[id];
}

/* Modèles du pack Quaternius « LowPoly Crops Pack » (licence CC0, OpenGameArt, 2021), convertis en JSON.
   Deux stades par culture : pousse et récolte. Taille finale = plus grande dimension, en mètres. */
const TAILLE_PACK = { carotte: 0.35, betterave: 0.4, tomate: 1.2, courge: 1.1, chou: 0.55, fraisier: 0.3, couvert: 0.45 };
const pack = {};
let promesse = null;
export function chargerModeles() {
  if (!promesse) promesse = fetch("/assets/potager/modeles3d.json").then((r) => (r.ok ? r.json() : {})).then((d) => {
    Object.keys(d).forEach((id) => {
      pack[id] = {};
      ["pousse", "recolte"].forEach((st) => {
        const m = d[id][st], n = m.p.length / 3, col = new Float32Array(n * 3);
        m.c.forEach((k, t) => { const c = m.pal[k]; for (let s = 0; s < 3; s++) { col[(t * 3 + s) * 3] = c[0]; col[(t * 3 + s) * 3 + 1] = c[1]; col[(t * 3 + s) * 3 + 2] = c[2]; } });
        const g = new THREE.BufferGeometry();
        g.setAttribute("position", new THREE.BufferAttribute(new Float32Array(m.p), 3));
        g.setAttribute("color", new THREE.BufferAttribute(col, 3));
        g.scale(TAILLE_PACK[id] || 0.4, TAILLE_PACK[id] || 0.4, TAILLE_PACK[id] || 0.4);
        g.computeVertexNormals();
        pack[id][st] = g;
      });
    });
  }).catch(() => {});
  return promesse;
}
/* Géométrie d'une culture à un stade : modèle du pack s'il existe, sinon silhouette dessinée. */
export function modeleStade(id, stade) { return pack[id] ? pack[id][stade] : modele(id); }
export function aUnModele(id) { return !!pack[id]; }
