// Animation du reel 01 « Le plan fixe » : tout est fonction du temps t (secondes), donc rendu image par image déterministe.
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const easeOut = x => 1 - Math.pow(1 - x, 3);
const easeInOut = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const back = x => { const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const lerp = (a, b, x) => a + (b - a) * x;
const pick = (t, list) => { let v = list[0][1]; for (const [s, val] of list) if (t >= s) v = val; return v; };
function show(cls, root, key) { root.querySelectorAll('.' + cls).forEach(g => g.style.display = g.dataset.k === key ? '' : 'none'); }
function noise(t, f, seed) { return Math.sin(t * f * 6.28 + seed) * .6 + Math.sin(t * f * 2.3 * 6.28 + seed * 3) * .4; }

// Repères calés sur la voix
const T = { arrete: 2.6, puissant: 4.1, nepas: 6.9, plan: 8.9, sujet: 13.35, entre: 15.6, agit: 16.55, sort: 17.6, specta: 19.0, regle: 23.4, abonne: 28.1 };
const TITLES = [[0, 'TU BOUGES TROP.'], [T.arrete, 'STOP.'], [T.puissant, 'LE PLUS PUISSANT ?'], [T.nepas, 'NE PAS BOUGER.'],
  [T.plan, 'LE PLAN FIXE'], [T.sujet, 'LE SUJET AGIT'], [T.specta, "IL REGARDE L'HISTOIRE"], [T.regle, ''], [T.abonne, 'DEMAIN : ON BOUGE.']];

let lastTitle = null;
function title(t) {
  const txt = pick(t, TITLES); const start = TITLES.filter(x => x[0] <= t).pop()[0];
  const g = $('title'); g.style.display = txt ? '' : 'none'; if (!txt) return;
  const tx = $('ttx');
  if (txt !== lastTitle) { tx.textContent = txt; tx.removeAttribute('transform'); const w = tx.getComputedTextLength();
    tx.dataset.k = w > 206 ? 206 / w : 1; lastTitle = txt; }
  const k = +tx.dataset.k, p = back(seg(t, start, start + .25));
  tx.setAttribute('transform', `translate(135 72) scale(${k}) translate(-135 -72)`);
  g.setAttribute('transform', `translate(135 62) scale(${lerp(.75, 1, p)}) translate(-135 -62)`); g.style.opacity = seg(t, start, start + .12);
}

function sensei(t, f) {
  const g = $('sensei');
  const inVf = t >= T.sujet + .25 && t < T.regle - .1;
  const x = lerp(-200, 14, back(seg(t, T.arrete - .25, T.arrete + .15)));
  const breathe = 1 + .008 * Math.sin(t * 2.2);
  g.style.display = inVf ? 'none' : '';
  g.setAttribute('transform', `translate(${x} ${186 + (1 - breathe) * 215}) scale(.5 ${.5 * breathe})`);
  const key = pick(t, [[0, 'stop-severe'], [T.puissant, 'neutre-serein'], [T.plan, 'enseigne-malin'], [T.regle, 'neutre-serein'], [T.abonne, 'camera-rire']]);
  show('sv', g, key);
  const a = DATA.amp[Math.min(f, DATA.amp.length - 1)] || 0;
  const ry = clamp((a - .12) * 14, 0, 7.5);
  g.querySelectorAll('.talk').forEach(e => e.setAttribute('ry', t >= T.arrete - .2 ? ry.toFixed(2) : 0));
}

function eleve(t) {
  const g = $('eleve');
  const inVf = t >= T.sujet + .25 && t < T.regle - .1;
  g.style.display = inVf ? 'none' : '';
  let dx = 0, dy = 0;
  if (t < T.arrete) { dx = noise(t, 5.3, 1) * 5; dy = noise(t, 6.1, 2) * 4; }       // il secoue son téléphone
  const jump = t >= T.arrete && t < T.arrete + .3 ? -Math.sin(seg(t, T.arrete, T.arrete + .3) * Math.PI) * 8 : 0; // sursaut au STOP
  const breathe = 1 + .01 * Math.sin(t * 2.6 + 1);
  g.setAttribute('transform', `translate(${128 + dx} ${222 + dy + jump + (1 - breathe) * 190}) scale(.44 ${.44 * breathe})`);
  show('ev', g, pick(t, [[0, 'filme-confiant'], [T.arrete, 'filme-confus'], [T.puissant, 'neutre-confus'], [T.plan, 'neutre-confiant'],
    [T.regle, 'neutre-emerveille'], [T.abonne, 'filme-emerveille']]));
  // clignement des yeux
  const blink = [1.9, 5.3, 9.8, 12.1, 25.2, 30.4].some(b => t >= b && t < b + .12);
  g.querySelectorAll('[id=eyes]').forEach(e => e.setAttribute('transform', blink ? 'translate(0 107) scale(1 .1) translate(0 -107)' : ''));
}

function tripod(t) {
  const g = $('tripod'); const on = t >= T.plan && t < T.sujet + .3;
  g.style.display = on ? '' : 'none'; if (!on) return;
  const p = back(seg(t, T.plan, T.plan + .35));
  g.setAttribute('transform', `translate(118 ${lerp(250, 318, p)}) scale(.95)`); g.style.opacity = seg(t, T.plan, T.plan + .1);
}

function viewfinder(t) {
  const g = $('vf'); const on = t >= T.sujet && t < T.regle;
  g.style.display = on ? '' : 'none'; if (!on) return;
  const pin = easeInOut(seg(t, T.sujet, T.sujet + .45)), pout = easeInOut(seg(t, T.regle - .35, T.regle));
  const p = pin * (1 - pout);
  const x = lerp(118, 20, p), y = lerp(300, 96, p), k = lerp(.08, 1, p);
  g.setAttribute('transform', `translate(${x} ${y}) scale(${k})`);
  // personnage dans le cadre : entre, agit, sort, puis revient pour « l'histoire »
  const m = $('mini'); let mx = -80, key = 'neutre-confiant', hop = 0;
  if (t < T.entre) mx = -80;
  else if (t < T.agit) mx = lerp(-80, 78, easeOut(seg(t, T.entre, T.agit - .1)));
  else if (t < T.sort) { mx = 78; key = 'filme-emerveille'; hop = -Math.abs(Math.sin(seg(t, T.agit, T.sort) * Math.PI * 2)) * 6; }
  else if (t < T.specta) mx = lerp(78, 250, easeInOut(seg(t, T.sort, T.specta - .2)));
  else { mx = lerp(250, 78, easeOut(seg(t, T.specta, T.specta + .9))); key = 'neutre-emerveille'; }
  const walking = (t >= T.entre && t < T.agit - .1) || (t >= T.sort && t < T.specta - .2) || (t >= T.specta && t < T.specta + .9);
  const bob = walking ? -Math.abs(Math.sin(t * 9)) * 4 : 0;
  m.setAttribute('transform', `translate(${mx} ${100 + bob + hop}) scale(.32)`); show('mv', m, key);
  $('rec').style.opacity = Math.floor(t * 2) % 2 ? .25 : 1;
  const el = Math.max(0, t - T.sujet), fr = Math.floor((el % 1) * 25);
  $('tc').textContent = `00:00:${String(Math.floor(el)).padStart(2, '0')}:${String(fr).padStart(2, '0')}`;
}

function stamp(t) {
  const g = $('stamp'); const a = T.regle + .05, b = T.abonne - .15;
  const on = t >= a && t < b + .2; g.style.display = on ? '' : 'none'; if (!on) return;
  const p = seg(t, a, a + .25), k = lerp(2.6, 1, easeOut(p)) * (p >= 1 ? 1 + .04 * Math.sin(seg(t, a + .25, a + .45) * Math.PI) : 1);
  g.setAttribute('transform', `translate(135 165) scale(${k})`); g.style.opacity = Math.min(seg(t, a, a + .08), 1 - seg(t, b, b + .2));
}

function subscribe(t) {
  const g = $('subbtn'); const a = T.abonne + .05; const on = t >= a; g.style.display = on ? '' : 'none'; if (!on) return;
  const k = back(seg(t, a, a + .3)); g.setAttribute('transform', `translate(135 140) scale(${k})`);
  const click = T.abonne + .85; const done = t >= click;
  $('btnbg').setAttribute('fill', done ? '#5b5650' : '#E63B2E'); $('btntx').textContent = done ? 'ABONNÉ ✓' : "S'ABONNER";
  const cp = easeInOut(seg(t, a + .3, click - .05));
  const press = t >= click - .05 && t < click + .12 ? .85 : 1;
  $('cursor').setAttribute('transform', `translate(${lerp(70, 8, cp)} ${lerp(60, 2, cp)}) scale(${press})`);
  $('cursor').style.opacity = 1 - seg(t, click + .6, click + .9);
}

function shake(t) {
  const a = T.regle + .3; let dx = 0, dy = 0;
  if (t >= a && t < a + .25) { const d = 1 - seg(t, a, a + .25); dx = Math.sin(t * 90) * 3 * d; dy = Math.cos(t * 70) * 2.2 * d; }
  const push = 1 + .025 * seg(t, 0, DATA.duration);
  $('world').setAttribute('transform', `translate(${dx} ${dy}) translate(135 240) scale(${push}) translate(-135 -240)`);
}

let lastChunk = -1;
function subtitles(t) {
  const C = DATA.chunks; let i = -1;
  for (let j = 0; j < C.length; j++) if (t >= C[j].s - .05) i = j;
  const g = $('sub');
  if (i < 0 || t > C[i].e + .7 && !(C[i + 1] && t >= C[i + 1].s - .05)) { g.style.display = 'none'; return; }
  g.style.display = '';
  const tx = $('stx');
  if (i !== lastChunk) {
    tx.innerHTML = ''; C[i].w.forEach(([w], k) => { const s = document.createElementNS('http://www.w3.org/2000/svg', 'tspan'); s.textContent = (k ? ' ' : '') + w; tx.appendChild(s); });
    const bb = tx.getBBox(); $('sbg').setAttribute('x', bb.x - 9); $('sbg').setAttribute('width', bb.width + 18); lastChunk = i;
  }
  tx.querySelectorAll('tspan').forEach((s, k) => s.setAttribute('fill', t >= C[i].w[k][1] ? '#F2B33D' : '#FFFFFF'));
  g.setAttribute('transform', `translate(135 388) scale(${lerp(.92, 1, easeOut(seg(t, C[i].s - .05, C[i].s + .08)))})`);
}

window.render = t => { const f = Math.round(t * DATA.fps); shake(t); title(t); sensei(t, f); eleve(t); tripod(t); viewfinder(t); stamp(t); subscribe(t); subtitles(t); };
render(0);
