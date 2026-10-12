// Maquette 3D Longueur d'avance : maison contemporaine fictive, du plan à la 3D.
// Code écrit pour Longueur d'avance (aucune reprise d'un travail tiers). Librairie : three.js r160 (MIT), hébergée sur le site.
import * as THREE from 'three';
import { OrbitControls } from '/assets/three/addons/controls/OrbitControls.js';

const host = document.getElementById('m3d');
if (host) init(host);

function init(host) {
  const canvas = host.querySelector('canvas');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setPixelRatio(Math.min(1.6, devicePixelRatio || 1));
  renderer.shadowMap.enabled = true;
  renderer.localClippingEnabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color('#f3ede2');
  scene.fog = new THREE.Fog('#f3ede2', 48, 95);

  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 300);
  camera.position.set(26, 19, 30);
  const controls = new OrbitControls(camera, canvas);
  controls.target.set(6, 2.4, 4);
  controls.enableDamping = true;
  controls.maxPolarAngle = Math.PI * 0.47;
  controls.minDistance = 14; controls.maxDistance = 70;
  controls.enablePan = false;
  controls.autoRotate = !reduce; controls.autoRotateSpeed = 0.55;
  canvas.addEventListener('pointerdown', () => { controls.autoRotate = false; });

  // lumière
  const hemi = new THREE.HemisphereLight('#fff6ea', '#9fae8f', 0.9);
  scene.add(hemi);
  const sun = new THREE.DirectionalLight('#fff1dc', 2.4);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048); sun.shadow.radius = 4;
  Object.assign(sun.shadow.camera, { left: -26, right: 26, top: 26, bottom: -26, near: 1, far: 90 });
  sun.shadow.bias = -0.0004;
  scene.add(sun, sun.target);
  sun.target.position.set(6, 0, 4);

  // ── environnement : ciel procédural → reflets et lumière d'ambiance réalistes
  const pmrem = new THREE.PMREMGenerator(renderer);
  const envScene = new THREE.Scene();
  const skyGeo = new THREE.SphereGeometry(50, 32, 16), cols = [];
  const pos = skyGeo.attributes.position, cTop = new THREE.Color('#8fb3d9'), cHor = new THREE.Color('#f6ead8'), cGnd = new THREE.Color('#9a9a82');
  for (let i = 0; i < pos.count; i++) { const y = pos.getY(i) / 50; const c = y > 0 ? cHor.clone().lerp(cTop, Math.pow(y, .6)) : cHor.clone().lerp(cGnd, Math.min(1, -y * 3)); cols.push(c.r, c.g, c.b); }
  skyGeo.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
  envScene.add(new THREE.Mesh(skyGeo, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide })));
  const sunDisk = new THREE.Mesh(new THREE.SphereGeometry(3, 16, 8), new THREE.MeshBasicMaterial({ color: '#fff4e0' }));
  sunDisk.position.set(30, 25, 20); envScene.add(sunDisk);
  scene.environment = pmrem.fromScene(envScene, 0.04).texture;
  renderer.toneMappingExposure = 0.95;

  // ── textures procédurales (aucune image téléchargée)
  const TEX = {};
  function canvasTex(key, w, h, draw) {
    if (TEX[key]) return TEX[key];
    const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h);
    const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
    return (TEX[key] = t);
  }
  const rnd = (a, b) => a + Math.random() * (b - a);
  const woodBoards = canvasTex('wood', 512, 512, (g, w, h) => {           // bardage bois vertical
    const n = 8;
    for (let i = 0; i < n; i++) {
      const x = i * w / n, l = rnd(38, 50);
      g.fillStyle = `hsl(26,${rnd(38, 48)}%,${l}%)`; g.fillRect(x, 0, w / n, h);
      for (let k = 0; k < 26; k++) { g.strokeStyle = `rgba(60,35,18,${rnd(.05, .18)})`; g.lineWidth = rnd(.5, 1.6); g.beginPath(); const xx = x + rnd(2, w / n - 2); g.moveTo(xx, 0); g.bezierCurveTo(xx + rnd(-4, 4), h * .3, xx + rnd(-4, 4), h * .7, xx + rnd(-3, 3), h); g.stroke(); }
      g.fillStyle = 'rgba(30,18,10,.55)'; g.fillRect(x, 0, 2, h);
    }
  });
  const deckBoards = canvasTex('deck', 512, 512, (g, w, h) => {
    const n = 10;
    for (let i = 0; i < n; i++) { const y = i * h / n; g.fillStyle = `hsl(30,${rnd(30, 40)}%,${rnd(52, 62)}%)`; g.fillRect(0, y, w, h / n);
      for (let k = 0; k < 14; k++) { g.strokeStyle = `rgba(80,50,25,${rnd(.06, .16)})`; g.beginPath(); const yy = y + rnd(2, h / n - 2); g.moveTo(0, yy); g.lineTo(w, yy + rnd(-2, 2)); g.stroke(); }
      g.fillStyle = 'rgba(40,25,12,.5)'; g.fillRect(0, y, w, 2); }
  });
  const noiseTex = (key, base, amp, dots) => canvasTex(key, 256, 256, (g, w, h) => {
    g.fillStyle = base; g.fillRect(0, 0, w, h);
    for (let i = 0; i < dots; i++) { const v = Math.random() > .5 ? 255 : 0; g.fillStyle = `rgba(${v},${v},${v},${rnd(.01, amp)})`; g.fillRect(rnd(0, w), rnd(0, h), rnd(1, 3), rnd(1, 3)); }
  });
  const enduit = noiseTex('enduit', '#f1ebe1', .06, 9000);
  const beton = noiseTex('beton', '#c9c4bb', .1, 12000);
  const ardoise = noiseTex('ardoise', '#3a3d45', .08, 9000);
  const herbe = canvasTex('herbe', 512, 512, (g, w, h) => {
    g.fillStyle = '#a7b98c'; g.fillRect(0, 0, w, h);
    for (let i = 0; i < 26000; i++) { g.fillStyle = `hsla(${rnd(78, 100)},${rnd(22, 38)}%,${rnd(42, 66)}%,${rnd(.25, .7)})`; const x = rnd(0, w), y = rnd(0, h); g.fillRect(x, y, 1, rnd(2, 5)); }
  });
  const eau = canvasTex('eau', 256, 256, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, w, h); gr.addColorStop(0, '#6fb6c9'); gr.addColorStop(1, '#4f9bb3'); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    for (let i = 0; i < 260; i++) { g.strokeStyle = `rgba(255,255,255,${rnd(.08, .28)})`; g.lineWidth = rnd(.8, 2); g.beginPath(); const x = rnd(0, w), y = rnd(0, h); g.moveTo(x, y); g.quadraticCurveTo(x + 8, y - 4, x + 16, y); g.stroke(); }
  });
  const TX = (tex, rx, ry) => { const t = tex.clone(); t.needsUpdate = true; t.repeat.set(rx, ry); return t; };
  const M = (c, o = {}) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.85, metalness: 0, ...o });
  const mWall = M('#ffffff', { map: TX(enduit, 4, 2), roughness: .92 }), mDark = M('#3a3f4a', { roughness: 0.45, metalness: .55 }),
    mWood = M('#ffffff', { map: TX(woodBoards, 3, 1), roughness: .75 }), mWoodS = M('#ffffff', { map: TX(woodBoards, 1.2, 1), roughness: .75 }),
    mSlab = M('#ffffff', { map: TX(beton, 4, 4), roughness: .9 }), mFloor = M('#ffffff', { map: TX(deckBoards, 3, 2), roughness: .6 }),
    mGlass = new THREE.MeshPhysicalMaterial({ color: '#cfe0e8', roughness: 0.02, metalness: 0.0, transparent: true, opacity: 0.32, envMapIntensity: 1.6, clearcoat: 1 }),
    mGrass = M('#ffffff', { map: TX(herbe, 14, 14), roughness: 1 }), mDeck = M('#ffffff', { map: TX(deckBoards, 4, 1.6), roughness: .7 }),
    mPool = new THREE.MeshPhysicalMaterial({ color: '#ffffff', map: TX(eau, 3, 1.2), roughness: .05, clearcoat: 1, envMapIntensity: 1.2 }),
    mTrunk = M('#6b4a35'), mLeaf = M('#7f9a6d', { roughness: .9 }), mLeaf2 = M('#93ad7f', { roughness: .9 }),
    mTerra = M('#ffffff', { map: TX(woodBoards, 1.2, 1), color: '#d27a4c', roughness: .75 }), mSofa = M('#d9c7b0', { roughness: 1 }),
    mRoof = M('#ffffff', { map: TX(ardoise, 6, 4), roughness: .8 }), mAlu = M('#2b2f3a', { roughness: .35, metalness: .8 }),
    mLight = new THREE.MeshStandardMaterial({ color: '#2b2f3a', emissive: '#ffcf8a', emissiveIntensity: 0 }),
    mLine = new THREE.LineBasicMaterial({ color: '#12192b' });
  const mPoolT = mPool.map;

  const box = (w, h, d, mat, x, y, z, parent) => {
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
    m.position.set(x, y, z); m.castShadow = true; m.receiveShadow = true; (parent || scene).add(m); return m;
  };

  // terrain
  const ground = new THREE.Mesh(new THREE.CircleGeometry(60, 64), mGrass);
  ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  box(16, 0.12, 6, mDeck, 7, 0.06, -6.2);              // terrasse sud
  const pool = box(8, 0.06, 3.2, mPool, 15.5, 0.08, -6.6); pool.castShadow = false;
  box(8.6, 0.1, 3.8, mSlab, 15.5, 0.04, -6.6); box(1.2, 0.05, 1.2, mSlab, -4, 0.03, -6); box(1.2, 0.05, 1.2, mSlab, -4, 0.03, -8);
  box(1.4, 0.05, 12, mSlab, -4, 0.03, 1);               // allée
  const arbres = new THREE.Group(); scene.add(arbres);
  [[-9, -6], [-8, 10], [24, 6], [22, 12], [-6, 15], [26, -10]].forEach(([x, z], i) => {
    const s = 0.8 + (i % 3) * 0.25;
    box(0.35, 2.2 * s, 0.35, mTrunk, x, 1.1 * s, z, arbres);
    [[0, 0, 0, 1.7], [0.9, 0.5, 0.4, 1.2], [-0.8, 0.3, -0.5, 1.25], [0.2, 1.2, -0.3, 1.1]].forEach(([dx, dy, dz, r], j) => {
      const c = new THREE.Mesh(new THREE.IcosahedronGeometry(r * s, 2), j % 2 ? mLeaf2 : mLeaf);
      c.position.set(x + dx * s, 3 * s + 0.6 + dy * s, z + dz * s); c.castShadow = true; c.receiveShadow = true; arbres.add(c); });
  });

  // plan au sol (le dessin d'architecte)
  const planPts = [[0, 0], [14, 0], [14, 8], [12, 8], [12, 13], [6, 13], [6, 8], [0, 8], [0, 0]];
  const planGeo = new THREE.BufferGeometry().setFromPoints(planPts.map(([x, z]) => new THREE.Vector3(x, 0.2, z)));
  const plan = new THREE.Line(planGeo, mLine); scene.add(plan);
  const inner = [[[6, 0], [6, 8]], [[0, 4.5], [6, 4.5]], [[9, 8], [9, 13]]].map(([a, b]) => {
    const g = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(a[0], 0.2, a[1]), new THREE.Vector3(b[0], 0.2, b[1])]);
    const l = new THREE.Line(g, new THREE.LineDashedMaterial({ color: '#12192b', dashSize: 0.4, gapSize: 0.25 })); l.computeLineDistances(); scene.add(l); return l;
  });

  // rez-de-chaussée : murs (qui « montent » depuis le plan)
  const H = 3, T = 0.25;
  const rdc = new THREE.Group(); scene.add(rdc);
  box(14, 0.2, 8, mFloor, 7, 0.1, 4, rdc); box(6, 0.2, 5, mFloor, 9, 0.1, 10.5, rdc);
  const walls = new THREE.Group(); rdc.add(walls);
  // façade sud : grande baie vitrée entre deux trumeaux
  box(1.2, H, T, mWall, 0.6, H / 2, 0, walls); box(1.2, H, T, mWall, 13.4, H / 2, 0, walls);
  box(11.6, 0.4, T, mWall, 7, H - 0.2, 0, walls);
  const baie = box(11.6, H - 0.4, 0.06, mGlass, 7, (H - 0.4) / 2, 0, walls); baie.castShadow = false;
  for (let x = 1.2; x <= 12.8; x += 2.9) box(0.06, H - 0.4, 0.12, mAlu, x, (H - 0.4) / 2, 0, walls);
  box(11.6, 0.06, 0.12, mAlu, 7, 0.03, 0, walls);
  // autres murs
  box(T, H, 8, mWall, 0, H / 2, 4, walls);
  box(T, H, 8, mWall, 14, H / 2, 4, walls);
  box(6, H, T, mWall, 3, H / 2, 8, walls);
  box(2, H, T, mWall, 13, H / 2, 8, walls);
  box(T, H, 5, mTerra, 6, H / 2, 10.5, walls);         // aile cuisine, bardage teinté terracotta
  box(T, H, 5, mTerra, 12, H / 2, 10.5, walls);
  box(6, H, T, mWall, 9, H / 2, 13, walls);
  const porte = box(1.1, 2.3, 0.08, mWood, 0, 1.15, 6.2, walls); porte.position.x = -0.06;
  // mobilier
  const meubles = new THREE.Group(); rdc.add(meubles);
  box(3.4, 0.7, 1.1, mSofa, 3, 0.55, 2.2, meubles); box(3.4, 0.6, 0.3, mSofa, 3, 1, 1.75, meubles);
  box(2.2, 0.08, 1.1, mWood, 9.6, 0.95, 3.6, meubles);
  [8.8, 10.4].forEach(x => [3, 4.2].forEach(z => box(0.45, 0.5, 0.45, mDark, x, 0.45, z, meubles)));
  box(3, 0.95, 1, mWall, 9, 0.68, 10.5, meubles); box(3, 0.06, 1.1, mDark, 9, 1.18, 10.5, meubles);

  // étage en porte-à-faux, bardé bois
  const etage = new THREE.Group(); scene.add(etage);
  const E = 3.2;
  box(11, 0.3, 7.5, mSlab, 5, H + 0.15, 4.2, etage);
  box(11, E, T, mWood, 5, H + 0.3 + E / 2, 0.45, etage);
  const ruban = box(8, 1.1, 0.07, mGlass, 5.2, H + 0.3 + 1.7, 0.4, etage); ruban.castShadow = false;
  box(11, E, T, mWood, 5, H + 0.3 + E / 2, 7.95, etage);
  box(T, E, 7.5, mWoodS, -0.5, H + 0.3 + E / 2, 4.2, etage);
  box(T, E, 7.5, mWoodS, 10.5, H + 0.3 + E / 2, 4.2, etage);
  const lum1 = box(7.6, 0.9, 0.02, mLight, 5.2, H + 0.3 + 1.7, 0.36, etage); lum1.castShadow = false;
  const lum2 = box(11, 0.05, 2.2, mLight, 7, H - 0.06, 3, rdc); lum2.castShadow = false;
  box(2.2, 0.5, 2, mSofa, 7.5, H + 0.55, 5.6, etage);   // lit
  box(2.2, 0.3, 0.2, mWood, 7.5, H + 0.9, 6.6, etage);

  // toits
  const toits = new THREE.Group(); scene.add(toits);
  box(14.6, 0.3, 8.6, mDark, 7, H + 0.15, 4, toits).visible = false; // dalle RDC sous l'étage (cachée par l'étage)
  box(6.6, 0.3, 5.6, mRoof, 9, H + 0.15, 10.5, toits);
  box(11.6, 0.35, 8.1, mRoof, 5, H + 0.3 + E + 0.18, 4.2, toits);
  box(11.8, 0.12, 8.3, mAlu, 5, H + 0.3 + E + 0.4, 4.2, toits);

  // ── du plan à la 3D ──
  let t0 = -1, playing = false;
  const ease = x => 1 - Math.pow(1 - Math.min(1, Math.max(0, x)), 3);
  function setBuild(p) {                      // p de 0 (plan) à 1 (maison)
    const w = ease(p / 0.45);
    walls.scale.y = Math.max(0.001, w); walls.position.y = 0;
    meubles.visible = p > 0.2; meubles.scale.setScalar(Math.max(0.001, ease((p - 0.2) / 0.3)));
    const e = ease((p - 0.45) / 0.3);
    etage.visible = p > 0.45; etage.position.y = (1 - e) * 9;
    const r = ease((p - 0.72) / 0.28);
    toits.visible = p > 0.72; toits.position.y = (1 - r) * 6 + (roofOff ? 6 : 0);
    if (etageOff) etage.position.y += 4.2 * ease(splitP);
    if (typeof mode !== 'undefined' && mode === 'plan') { etage.visible = false; toits.visible = false; }
    plan.material.opacity = 1; inner.forEach(l => (l.visible = p < 0.95));
  }
  let roofOff = false, etageOff = false, splitP = 0, buildP = 0;
  function rejouer() { t0 = performance.now(); playing = true; controls.autoRotate = !reduce; }

  // ── lumière du matin au soir ──
  const slider = host.querySelector('#m3d-heure');
  function setHeure(h) {                       // 7 h -> 21 h
    const k = (h - 7) / 14, az = -Math.PI * 0.85 + k * Math.PI * 1.1, el = Math.sin(k * Math.PI) * 1.05 + 0.08;
    sun.position.set(6 + Math.cos(az) * 40, Math.max(3, Math.sin(el) * 38), 4 + Math.sin(az) * 40);
    const warm = 1 - Math.sin(k * Math.PI);
    sun.color.setHSL(0.08, 0.55 * warm + 0.15, 0.62 + 0.25 * (1 - warm));
    sun.intensity = 1.2 + 1.4 * Math.sin(k * Math.PI);
    hemi.intensity = 0.55 + 0.45 * Math.sin(k * Math.PI);
    const soir = Math.max(0, (h - 18.5) / 2.5); mLight.emissiveIntensity = 2.2 * soir; renderer.toneMappingExposure = 0.95 - 0.25 * soir;
    const lbl = host.querySelector('#m3d-heure-v'); if (lbl) lbl.textContent = `${Math.floor(h)} h`;
  }
  slider?.addEventListener('input', () => setHeure(+slider.value));
  setHeure(+(slider?.value || 16));

  host.querySelector('#m3d-rejouer')?.addEventListener('click', rejouer);
  const bt = host.querySelector('#m3d-toit');
  bt?.addEventListener('click', () => { roofOff = !roofOff; bt.setAttribute('aria-pressed', roofOff); setBuild(playing ? buildP : 1); });
  const be = host.querySelector('#m3d-etages');
  be?.addEventListener('click', () => { etageOff = !etageOff; be.setAttribute('aria-pressed', etageOff); splitStart = performance.now(); });
  let splitStart = 0;


  // ── voir le plan / voir la coupe ──
  const houseMats = [mWall, mDark, mWood, mWoodS, mSlab, mFloor, mGlass, mTerra, mSofa, mRoof, mAlu, mLight];
  houseMats.forEach(m => { m.side = THREE.DoubleSide; });
  const clipPlan = new THREE.Plane(new THREE.Vector3(0, -1, 0), 1.25);      // coupe horizontale à 1,25 m : le plan
  const clipCoupe = new THREE.Plane(new THREE.Vector3(-1, 0, 0), 7.2);      // coupe verticale à x = 7,2 m
  function setClip(pl) { houseMats.forEach(m => { m.clippingPlanes = pl ? [pl] : []; m.needsUpdate = true; }); }
  function label(txt, x, z, y = 0.3) {
    const c = document.createElement('canvas'); c.width = 512; c.height = 128; const g = c.getContext('2d');
    g.font = '600 54px Inter, sans-serif'; const w = g.measureText(txt).width + 60;
    g.fillStyle = 'rgba(253,252,249,.95)'; g.beginPath(); g.roundRect((512 - w) / 2, 22, w, 84, 42); g.fill();
    g.fillStyle = '#12192b'; g.textAlign = 'center'; g.fillText(txt, 256, 82);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
    const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, depthTest: false, transparent: true }));
    sp.scale.set(5.6, 1.4, 1); sp.position.set(x, y, z); sp.renderOrder = 10; sp.visible = false; scene.add(sp); return sp;
  }
  const etiquettes = [label('Séjour', 3, 3), label('Salle à manger', 9.8, 5.4), label('Cuisine', 9, 11.5), label('Entrée', 1.6, 6.6),
    label('Terrasse', 6, -6.2), label('Piscine', 15.5, -6.6)];
  const cotes = [label('14,00 m', 7, -1.2), label('13,00 m', 15.6, 6.5)];
  const cadre = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.PlaneGeometry(16, 8.5)), new THREE.LineBasicMaterial({ color: '#b4551e' }));
  cadre.rotation.y = Math.PI / 2; cadre.position.set(7.2, 4.2, 6); cadre.visible = false; scene.add(cadre);
  const coteH = [label('RDC  ±0,00', 7.4, -2.6, 1.4), label('Étage  +3,30', 7.4, -2.6, 4.7), label('Acrotère  +6,90', 7.4, -2.6, 7.4)];
  let mode = '3d', tween = null;
  const vues = {
    '3d': { pos: new THREE.Vector3(26, 19, 30), tgt: new THREE.Vector3(6, 2.4, 4) },
    plan: { pos: new THREE.Vector3(7.5, 46, 4.6), tgt: new THREE.Vector3(7.5, 0, 4.5) },
    coupe: { pos: new THREE.Vector3(40, 5.5, 5.5), tgt: new THREE.Vector3(7, 3.4, 5.5) }
  };
  function aller(v) { tween = { t: performance.now(), p0: camera.position.clone(), t0: controls.target.clone(), v: vues[v] }; }
  function setMode(m) {
    mode = m;
    host.querySelectorAll('[data-vue]').forEach(b => b.setAttribute('aria-pressed', b.dataset.vue === m));
    controls.autoRotate = false;
    setClip(m === 'plan' ? clipPlan : m === 'coupe' ? clipCoupe : null);
    etiquettes.forEach(e => (e.visible = m === 'plan')); cotes.forEach(e => (e.visible = m === 'plan'));
    cadre.visible = m === 'coupe'; coteH.forEach(e => (e.visible = m === 'coupe')); arbres.visible = m !== 'coupe';
    controls.enableRotate = m === '3d';
    aller(m);
  }
  host.querySelectorAll('[data-vue]').forEach(b => b.addEventListener('click', () => setMode(b.dataset.vue)));
  const sc = host.querySelector('#m3d-coupe');
  sc?.addEventListener('input', () => {
    const x = +sc.value; clipCoupe.constant = x; cadre.position.x = x; coteH.forEach(e => (e.position.x = x + 0.2));
    const v = host.querySelector('#m3d-coupe-v'); if (v) v.textContent = x.toFixed(1).replace('.', ',') + ' m';
    vues.coupe.tgt.x = x; vues.coupe.pos.x = x + 33;
    if (mode !== 'coupe') setMode('coupe');
  });


  function resize() {
    const w = host.clientWidth, h = canvas.clientHeight || 420;
    renderer.setSize(w, h, false); camera.aspect = w / h;
    camera.position.multiplyScalar(1); camera.fov = w < 560 ? 50 : 38; camera.updateProjectionMatrix();
  }
  addEventListener('resize', resize); resize();

  let visible = false, started = false;
  new IntersectionObserver(es => {
    visible = es[0].isIntersecting;
    if (visible && !started) { started = true; reduce ? setBuild(1) : rejouer(); }
  }, { threshold: 0.35 }).observe(host);
  setBuild(0);

  renderer.setAnimationLoop(now => {
    if (!visible) return;
    if (playing) { buildP = Math.min(1, (now - t0) / 4200); if (buildP >= 1) playing = false; }
    else if (started) buildP = 1;
    const target = etageOff ? 1 : 0; splitP += (target - splitP) * 0.08;
    setBuild(started ? buildP : 0);
    if (tween) { const k = Math.min(1, (now - tween.t) / 1100), e2 = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      camera.position.lerpVectors(tween.p0, tween.v.pos, e2); controls.target.lerpVectors(tween.t0, tween.v.tgt, e2); if (k >= 1) tween = null; }
    mPoolT.offset.x = (now / 9000) % 1; mPoolT.offset.y = Math.sin(now / 2400) * .03;
    controls.update(); renderer.render(scene, camera);
  });
}
