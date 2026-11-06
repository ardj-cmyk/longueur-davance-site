/* Plan de potager : textures dessinées dans le navigateur (aucun fichier téléchargé).
   Chaque texture couvre 1 m et se répète. */
import * as THREE from "three";

function graine(n) { let s = n; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

function toile(dessin, taille = 256) {
  const c = document.createElement("canvas"); c.width = c.height = taille;
  const g = c.getContext("2d");
  dessin(g, taille);
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 4;
  return t;
}

const cache = {};
export function texture(nom) {
  if (cache[nom]) return cache[nom];
  const r = graine(nom.length * 7919 + 13);
  const T = {
    /* Terre travaillée : brun avec mottes et petits cailloux. */
    terre: (g, s) => {
      g.fillStyle = "#5e412b"; g.fillRect(0, 0, s, s);
      for (let i = 0; i < 2600; i++) { const v = 60 + r() * 50; g.fillStyle = `rgb(${v + 25},${v * 0.72},${v * 0.45})`; g.fillRect(r() * s, r() * s, 1 + r() * 3, 1 + r() * 3); }
      for (let i = 0; i < 70; i++) { g.fillStyle = `rgba(40,26,16,${0.25 + r() * 0.3})`; g.beginPath(); g.ellipse(r() * s, r() * s, 3 + r() * 7, 2 + r() * 5, r() * 3, 0, 7); g.fill(); }
      for (let i = 0; i < 40; i++) { g.fillStyle = "rgba(190,175,150,.55)"; g.fillRect(r() * s, r() * s, 2, 2); }
    },
    /* Herbe : vert avec des brins. */
    herbe: (g, s) => {
      g.fillStyle = "#6f8f45"; g.fillRect(0, 0, s, s);
      for (let i = 0; i < 2200; i++) {
        const x = r() * s, y = r() * s, l = 4 + r() * 9, a = -Math.PI / 2 + (r() - 0.5) * 0.9;
        g.strokeStyle = `hsl(${85 + r() * 25},${35 + r() * 25}%,${28 + r() * 22}%)`; g.lineWidth = 1 + r();
        g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke();
      }
    },
    /* Allées : copeaux et gravier clair. */
    allee: (g, s) => {
      g.fillStyle = "#cdb98f"; g.fillRect(0, 0, s, s);
      for (let i = 0; i < 1800; i++) { const v = 150 + r() * 70; g.fillStyle = `rgb(${v},${v * 0.88},${v * 0.66})`; g.save(); g.translate(r() * s, r() * s); g.rotate(r() * 3); g.fillRect(-3, -1, 4 + r() * 6, 2 + r() * 2); g.restore(); }
    },
    /* Paille et paillis. */
    paille: (g, s) => {
      g.fillStyle = "#c9ad6a"; g.fillRect(0, 0, s, s);
      for (let i = 0; i < 900; i++) {
        const x = r() * s, y = r() * s, l = 10 + r() * 26, a = r() * Math.PI;
        g.strokeStyle = `hsl(${40 + r() * 10},${45 + r() * 20}%,${55 + r() * 25}%)`; g.lineWidth = 1 + r() * 1.5;
        g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke();
      }
    },
    /* Bois des bordures de planches. */
    bois: (g, s) => {
      g.fillStyle = "#8a6440"; g.fillRect(0, 0, s, s);
      for (let y = 0; y < s; y += 3) { g.fillStyle = `rgba(60,40,22,${0.1 + r() * 0.25})`; g.fillRect(0, y, s, 1 + r() * 2); }
    },
  };
  cache[nom] = toile(T[nom] || T.terre);
  return cache[nom];
}
