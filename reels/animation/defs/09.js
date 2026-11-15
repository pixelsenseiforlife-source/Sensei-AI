// Reel 09 — Ton monteur te déteste (règle des 2 secondes)
const REEL = {
  titles: [[0, 'TON MONTEUR TE DÉTESTE.'], ['lances', 'AUCUNE MARGE…'], ['Résultat', '= IMPOSSIBLE À COUPER'], ['règle', 'LA RÈGLE DES 2 SECONDES'], ['montage', '4 SECONDES QUI SAUVENT'], ['si', '']],
  sensei: [[0, 'neutre-malin'], ['règle', 'enseigne-malin'], ['si', 'neutre-rire']],
  eleve: [[0, 'neutre-confus'], ['si', 'neutre-emerveille'], ['Enregistre', 'filme-confiant']],
  panel: [['lances', 'si']],
  labels: [['lances', 'LE MOUVEMENT COMMENCE TOUT DE SUITE'], ['règle', '2 S FIXE · MOUVEMENT · 2 S FIXE']],
  stamp: { at: 'si', until: 'Enregistre', l1: 'RÈGLE N°9', l2: '2 S AVANT · 2 S APRÈS' },
  cta: { type: 'save', at: 'Enregistre' },
  demo(t, u) {
    const A = C('lances'), R = C('règle'), Res = C('Résultat'), M = C('montage');
    const good = t >= R;
    $('clipBad').style.display = good ? 'none' : ''; $('clipGood').style.display = good ? '' : 'none';
    const s0 = good ? R : A, per = 3.2; const x = 15 + 200 * (((t - s0) / per) % 1);
    set($('playhead'), 'x', x);
    set($('cut1'), 'transform', `translate(${good ? 37 : 15} 212)`); set($('cut2'), 'transform', `translate(${good ? 193 : 215} 212)`);
    $('verdictBad').style.display = !good && t >= Res ? '' : 'none'; $('verdictGood').style.display = good && t >= M ? '' : 'none';
    const shake = !good ? noise(t, 3, 1) * 8 : 0;
    set($('monM'), 'transform', `translate(${shake} ${!good ? noise(t, 4, 2) * 4 : 0})`);
  },
};
