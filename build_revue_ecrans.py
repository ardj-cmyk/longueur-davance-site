#!/usr/bin/env python3
"""Planche de revue : tous les écrans de démonstration, métier par métier (_revue-ecrans.html, noindex).
Construite à partir de _proto-v4.html : même code d'écrans, rendu figé dans l'état final."""
from pathlib import Path
ICI = Path(__file__).parent
t = (ICI / "_proto-v4.html").read_text(encoding="utf-8")
css = """<style>
body>header,body>.mobile-menu,body>main,body>footer{display:none!important}
body{background:#ebe5da}
#revue{max-width:1500px;margin:0 auto;padding:40px 24px 80px;font-family:var(--sans)}
#revue h1{font-family:var(--serif);font-size:40px;margin-bottom:6px}
#revue .intro{color:var(--muted);margin-bottom:30px;max-width:900px}
.rv-row{background:var(--ink);border-radius:22px;padding:22px 22px 26px;margin-bottom:26px;break-inside:avoid;page-break-inside:avoid}
.rv-row h2{color:var(--paper);font-family:var(--serif);font-size:26px;margin-bottom:4px}
.rv-row .meta{color:var(--muted-d);font-size:13px;margin-bottom:16px}
.rv-grid{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap}
.rv-cell{display:flex;flex-direction:column;align-items:center}
.rv-cell .slide{position:relative!important;left:auto!important;top:auto!important;transform:none!important;opacity:1!important;filter:none!important}
.rv-cell .phone{transform:scale(.8);transform-origin:top center;margin-bottom:-106px}
.rv-cell .laptop{width:500px}
.rv-cell .cap{opacity:1!important}
.rv-cell .ba-after{animation:none!important;clip-path:none!important}
.rv-cell .ba-line,.rv-cell .ba-tag.l{display:none}
.rv-cell .ba-tag.r{opacity:1!important;animation:none!important}
.rv-cell .mtoast{opacity:1!important;transform:none!important;animation:none!important}
.rv-cell .toast{transform:none!important}
.rv-cell .odo .col,.rv-cell .bar i{transition:none!important}
@media print{body{background:#fff}.rv-row{margin-bottom:14px}}
</style>"""
js = """<script>
(function(){
  const box=document.createElement('div'); box.id='revue';
  box.innerHTML='<h1>Revue des écrans, métier par métier</h1><p class="intro">Chaque ligne = les écrans de démonstration affichés quand le visiteur choisit ce métier dans le questionnaire (ou arrive sur sa page métier). Rendu figé dans l’état final des animations. Données fictives.</p>';
  document.body.prepend(box);
  const only=new URLSearchParams(location.search).get('m');
  let order=['gen'].concat(QKEY.filter(k=>k!=='gen')); if(only){order=[only]; box.querySelector('h1').remove(); box.querySelector('.intro').remove(); box.style.padding='16px';}
  order.forEach(k=>{
    renderDemos(k); refreshSlides();
    const idx=QKEY.indexOf(k), name=k==='gen'?'Sans réponse (exemples généraux)':QNAME[idx];
    const row=document.createElement('section'); row.className='rv-row';
    const n=$$('#stage .slide').filter(s=>!s.hidden).length;
    row.innerHTML=`<h2>${name}</h2><div class="meta">Profil « ${k} » · ${n} écrans${PROF[k]&&PROF[k].label?' · titre : Ce que ça change pour '+PROF[k].label:''}</div><div class="rv-grid"></div>`;
    const grid=row.querySelector('.rv-grid');
    $$('#stage .slide').filter(s=>!s.hidden).forEach(s=>{
      const c=s.cloneNode(true); c.classList.add('on'); c.removeAttribute('id'); c.querySelectorAll('[id]').forEach(e=>e.removeAttribute('id'));
      c.querySelectorAll('.odo').forEach(o=>runOdo(o,true));
      c.querySelectorAll('.relance').forEach(r=>r.classList.add('done'));
      c.querySelectorAll('.toast').forEach(t=>t.classList.add('show'));
      const sl=c.querySelector('.slots'); if(sl&&sl.children[2]) sl.children[2].classList.add('pick');
      c.querySelectorAll('.post').forEach(p=>p.classList.add('done'));
      const cell=document.createElement('div'); cell.className='rv-cell'; cell.appendChild(c); grid.appendChild(cell);
    });
    box.appendChild(row);
  });
  renderDemos('gen'); refreshSlides();
})();
</script>"""
t = t.replace("</head>", css + "\n</head>", 1)
i = t.rindex("</body>")
t = t[:i] + js + "\n" + t[i:]
(ICI / "_revue-ecrans.html").write_text(t, encoding="utf-8")
print("ok _revue-ecrans.html")
