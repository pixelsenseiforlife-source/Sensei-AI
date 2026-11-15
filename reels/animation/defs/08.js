// Reel 08 — Ton drone, au début ou à la fin ?
const REEL = {
  titles: [[0, 'DÉBUT OU FIN ?'], ['Quand', 'MONTER : CONCLURE'], ['Quand#2', 'DESCENDRE : COMMENCER'], ['Pas', 'PAS DE DRONE ?'], ['Monter', '']],
  sensei: [[0, 'neutre-malin'], ['Quand', 'enseigne-malin'], ['Pas', 'camera-serein'], ['Monter', 'neutre-serein'], ['Enregistre', 'neutre-rire']],
  eleve: [[0, 'filme-confus'], ['Quand', 'neutre-emerveille'], ['Pas', 'filme-confiant']],
  panel: [['Quand', 'Pas']],
  labels: [['Quand', 'LA CAMÉRA MONTE'], ['Quand#2', 'LA CAMÉRA DESCEND']],
  stamp: { at: 'Monter', until: 'Enregistre', l1: 'RÈGLE N°8', l2: 'DESCENDRE = DÉBUT · MONTER = FIN' },
  cta: { type: 'save', at: 'Enregistre' },
  demo(t, u) {
    const M = C('Quand'), D = C('Quand#2'), P = C('Pas');
    let k, cx, cy, dy;
    if (t < D) { const p = easeInOut(seg(t, M + .3, D - .3)); k = lerp(2.4, .55, p); cx = lerp(180, 135, p); cy = lerp(330, 240, p); dy = lerp(70, 18, p); }
    else { const p = easeInOut(seg(t, D + .3, P - .4)); k = lerp(.9, 2.4, p); cx = lerp(135, 180, p); cy = lerp(70, 330, p); dy = lerp(18, 70, p); }
    set($('dAll'), 'transform', `translate(115 131) scale(${k}) translate(${-cx} ${-cy})`);
    set($('dDrone'), 'transform', `translate(150 ${dy + Math.sin(t * 5) * 2})`);
  },
};
