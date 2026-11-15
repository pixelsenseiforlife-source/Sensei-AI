// Moteur commun des reels « La Voie du Pixel ». Chaque reel fournit un objet REEL (défini dans defs/NN.js).
// Tout est fonction du temps t → rendu image par image déterministe.
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const easeOut = x => 1 - Math.pow(1 - x, 3);
const easeInOut = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const back = x => { const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const lerp = (a, b, x) => a + (b - a) * x;
const noise = (t, f, s) => Math.sin(t * f * 6.28 + s) * .6 + Math.sin(t * f * 2.3 * 6.28 + s * 3) * .4;
const tri = x => 1 - Math.abs(((x % 2) + 2) % 2 - 1);            // 0→1→0 périodique
const set = (el, attr, v) => { if (el) el.setAttribute(attr, v); };
function show(cls, root, key) { root.querySelectorAll('.' + cls).forEach(g => g.style.display = g.dataset.k === key ? '' : 'none'); }

// ---------- repères : un mot du texte (« Caméra#2 » = 2e occurrence), un nombre, ou « mot+0.3 »
const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9']/g, '');
const cueCache = {};
function C(cue) {
  if (typeof cue === 'number') return cue;
  if (cue in cueCache) return cueCache[cue];
  let off = 0, c = cue; const m = c.match(/([+-]\d*\.?\d+)$/); if (m && isNaN(+c)) { off = +m[1]; c = c.slice(0, -m[1].length); }
  let [w, occ] = c.split('#'); occ = +(occ || 1); const n = norm(w);
  let hits = DATA.words.filter(x => norm(x[0]) === n);
  if (hits.length < occ) hits = DATA.words.filter(x => norm(x[0]).startsWith(n));
  if (hits.length < occ) throw new Error('Repère introuvable : ' + cue);
  return cueCache[cue] = hits[occ - 1][1] + off;
}
const pickT = (t, list) => { let v = list[0][1], s = C(list[0][0]); for (const [c, val] of list) if (t >= C(c)) { v = val; s = C(c); } return [v, s]; };
const inRanges = (t, ranges) => (ranges || []).some(([a, b]) => t >= C(a) && t < C(b));

// ---------- titre
let lastTitle = null;
function title(t) {
  const [txt, start] = pickT(t, REEL.titles); const g = $('title');
  g.style.display = txt ? '' : 'none'; if (!txt) return;
  const tx = $('ttx');
  if (txt !== lastTitle) { tx.textContent = txt; tx.removeAttribute('transform'); const w = tx.getComputedTextLength(); tx.dataset.k = w > 206 ? 206 / w : 1; lastTitle = txt; }
  set(tx, 'transform', `translate(135 72) scale(${+tx.dataset.k}) translate(-135 -72)`);
  set(g, 'transform', `translate(135 62) scale(${lerp(.75, 1, back(seg(t, start, start + .25)))}) translate(-135 -62)`); g.style.opacity = seg(t, start, start + .12);
}

// ---------- personnages
function panelOn(t) { return inRanges(t, REEL.panel); }
function sensei(t, f) {
  const g = $('sensei'); const hidden = panelOn(t);
  const enter = C(REEL.senseiEnter ?? 0);
  const x = lerp(-200, 14, back(seg(t, enter - .25, enter + .15)));
  const br = 1 + .008 * Math.sin(t * 2.2);
  g.style.display = hidden ? 'none' : '';
  set(g, 'transform', `translate(${x} ${186 + (1 - br) * 215}) scale(.5 ${.5 * br})`);
  show('sv', g, pickT(t, REEL.sensei)[0]);
  const a = DATA.amp[Math.min(f, DATA.amp.length - 1)] || 0;
  const ry = t >= enter - .2 ? clamp((a - .12) * 14, 0, 7.5) : 0;
  g.querySelectorAll('.talk').forEach(e => e.setAttribute('ry', ry.toFixed(2)));
}
function eleve(t) {
  const g = $('eleve'); g.style.display = panelOn(t) ? 'none' : '';
  let dx = 0, dy = 0;
  if (REEL.eleveShake && t >= C(REEL.eleveShake[0]) && t < C(REEL.eleveShake[1])) { dx = noise(t, 5.3, 1) * 5; dy = noise(t, 6.1, 2) * 4; }
  const [key, start] = pickT(t, REEL.eleve);
  const hop = t >= start && t < start + .3 && start > 0 ? -Math.sin(seg(t, start, start + .3) * Math.PI) * 5 : 0;
  const br = 1 + .01 * Math.sin(t * 2.6 + 1);
  set(g, 'transform', `translate(${128 + dx} ${222 + dy + hop + (1 - br) * 190}) scale(.44 ${.44 * br})`);
  show('ev', g, key);
  const blink = [1.9, 5.3, 9.8, 12.1, 17.7, 25.2, 30.4].some(b => t >= b && t < b + .12);
  g.querySelectorAll('[id=eyes]').forEach(e => e.setAttribute('transform', blink ? 'translate(0 107) scale(1 .1) translate(0 -107)' : ''));
}

// ---------- panneau de démonstration (cadre caméra)
function panel(t) {
  const g = $('panel'); const r = (REEL.panel || []).find(([a, b]) => t >= C(a) - .01 && t < C(b));
  g.style.display = r ? '' : 'none'; if (!r) return;
  const a = C(r[0]), b = C(r[1]);
  const p = easeInOut(seg(t, a, a + .4)) * (1 - easeInOut(seg(t, b - .3, b)));
  const k = lerp(.08, 1, p);
  set(g, 'transform', `translate(${lerp(135, 20, p)} ${lerp(260, 96, p)}) scale(${k})`); g.style.opacity = clamp(p * 3);
  $('rec').style.opacity = Math.floor(t * 2) % 2 ? .25 : 1;
  const el = Math.max(0, t - a); $('tc').textContent = `00:00:${String(Math.floor(el)).padStart(2, '0')}:${String(Math.floor((el % 1) * 25)).padStart(2, '0')}`;
  const lab = REEL.labels ? pickT(t, REEL.labels)[0] : '';
  const L = $('plabel'); L.style.display = lab ? '' : 'none';
  if (lab && L.dataset.txt !== lab) { $('pltx').textContent = lab; const w = $('pltx').getComputedTextLength(); set($('plbg'), 'x', 115 - w / 2 - 7); set($('plbg'), 'width', w + 14); L.dataset.txt = lab; }
  REEL.demo && REEL.demo(t, t - a);
}

// ---------- tampon
function stamp(t) {
  const g = $('stamp'); const S = REEL.stamp; if (!S) { g.style.display = 'none'; return; }
  const a = C(S.at) + .05, b = C(S.until) - .15; const on = t >= a && t < b + .2;
  g.style.display = on ? '' : 'none'; if (!on) return;
  if (!g.dataset.init) { $('st1').textContent = S.l1; $('st2').textContent = S.l2; const w = $('st2').getComputedTextLength(); if (w > 196) set($('st2'), 'transform', `scale(${196 / w} 1)`); g.dataset.init = 1; }
  const p = seg(t, a, a + .25), k = lerp(2.6, 1, easeOut(p)) * (p >= 1 ? 1 + .04 * Math.sin(seg(t, a + .25, a + .45) * Math.PI) : 1);
  set(g, 'transform', `translate(135 165) scale(${k})`); g.style.opacity = Math.min(seg(t, a, a + .08), 1 - seg(t, b, b + .2));
}

// ---------- appel à l'action
function cta(t) {
  const g = $('cta'); const A = REEL.cta; const a = C(A.at) + .05; const z = A.until ? C(A.until) : 1e9; const on = t >= a && t < z + .2;
  g.style.display = on ? '' : 'none'; if (!on) return;
  show('cv', g, A.type);
  set(g, 'transform', `translate(135 ${A.y || 140}) scale(${back(seg(t, a, a + .3))})`); g.style.opacity = 1 - seg(t, z, z + .2);
  const u = t - a;
  if (A.type === 'subscribe') {
    const click = .8, done = u >= click;
    set($('btnbg'), 'fill', done ? '#5b5650' : '#E63B2E'); $('btntx').textContent = done ? 'ABONNÉ ✓' : "S'ABONNER";
    const cp = easeInOut(seg(u, .3, click - .05)); const press = u >= click - .05 && u < click + .12 ? .85 : 1;
    set($('cursor'), 'transform', `translate(${lerp(70, 8, cp)} ${lerp(60, 2, cp)}) scale(${press})`); $('cursor').style.opacity = 1 - seg(u, click + .6, click + .9);
  } else if (A.type === 'chips') {
    $('chip1').style.opacity = seg(u, .2, .35); $('chip2').style.opacity = seg(u, .45, .6);
    set($('chip1'), 'transform', `translate(-52 26) scale(${back(seg(u, .2, .45))})`); set($('chip2'), 'transform', `translate(52 26) scale(${back(seg(u, .45, .7))})`);
    if (!g.dataset.init) { $('c1tx').textContent = A.chips[0]; $('c2tx').textContent = A.chips[1]; $('cqtx').textContent = A.label || 'DIS-LE EN COMMENTAIRE'; const w = $('cqtx').getComputedTextLength(); if (w > 168) set($('cqtx'), 'transform', `translate(8 0) scale(${168 / w} 1) translate(-8 0)`); g.dataset.init = 1; }
  } else if (A.type === 'save') {
    const fill = u >= .6; set($('bkm'), 'fill', fill ? '#F2B33D' : 'none');
    set($('bkicon'), 'transform', `scale(${u >= .6 && u < .8 ? 1.25 : 1})`);
  } else if (A.type === 'share') {
    const fly = easeInOut(seg(u, .5, 1.1)); set($('plane'), 'transform', `translate(${fly * 60} ${-fly * 30}) rotate(${-fly * 15})`); $('plane').style.opacity = 1 - seg(u, 1.0, 1.2);
    $('sharedone').style.opacity = seg(u, 1.1, 1.3);
  } else if (A.type === 'keyword') {
    const word = 'SENSEI', nch = Math.floor(clamp((u - .3) / .12, 0, word.length)); $('kwtx').textContent = word.slice(0, nch) + (nch < word.length && Math.floor(u * 4) % 2 ? '|' : '');
    $('kwsend').style.opacity = seg(u, 1.2, 1.4); $('kwgift').style.opacity = seg(u, 1.5, 1.7);
  }
}

function world(t) {
  let dx = 0, dy = 0;
  for (const s of (window.IMPACTS || [])) if (t >= s && t < s + .25) { const d = 1 - seg(t, s, s + .25); dx += Math.sin(t * 90) * 3 * d; dy += Math.cos(t * 70) * 2.2 * d; }
  set($('world'), 'transform', `translate(${dx} ${dy}) translate(135 240) scale(${1 + .025 * seg(t, 0, DATA.duration)}) translate(-135 -240)`);
}

let lastChunk = -1;
function subtitles(t) {
  const CH = DATA.chunks; let i = -1; for (let j = 0; j < CH.length; j++) if (t >= CH[j].s - .05) i = j;
  const g = $('sub');
  if (i < 0 || t > CH[i].e + .7 && !(CH[i + 1] && t >= CH[i + 1].s - .05)) { g.style.display = 'none'; return; }
  g.style.display = ''; const tx = $('stx');
  if (i !== lastChunk) {
    tx.innerHTML = ''; CH[i].w.forEach(([w], k) => { const s = document.createElementNS('http://www.w3.org/2000/svg', 'tspan'); s.textContent = (k ? ' ' : '') + w; tx.appendChild(s); });
    const bb = tx.getBBox(); set($('sbg'), 'x', bb.x - 9); set($('sbg'), 'width', bb.width + 18); lastChunk = i;
  }
  tx.querySelectorAll('tspan').forEach((s, k) => s.setAttribute('fill', t >= CH[i].w[k][1] ? '#F2B33D' : '#FFFFFF'));
  set(g, 'transform', `translate(135 388) scale(${lerp(.92, 1, easeOut(seg(t, CH[i].s - .05, CH[i].s + .08)))})`);
}

window.IMPACTS = [];
window.render = t => {
  const f = Math.round(t * DATA.fps);
  world(t); title(t); sensei(t, f); eleve(t); panel(t); REEL.extra && REEL.extra(t); stamp(t); cta(t); subtitles(t);
};
window.addEventListener('load', () => {
  if (REEL.stamp) IMPACTS.push(C(REEL.stamp.at) + .3);
  (REEL.impacts || []).forEach(c => IMPACTS.push(C(c)));
  render(0);
});
