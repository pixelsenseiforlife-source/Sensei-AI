// Reel 04 — Même scène, deux émotions
const REEL = {
  titles: [[0, 'MÊME SCÈNE. 2 ÉMOTIONS.'], ['Travelling', 'AVANT : ON ENTRE'], ['Travelling#2', 'ARRIÈRE : ON QUITTE'], ['Avancer', ''], ['toi', 'TON CAMP ?']],
  sensei: [[0, 'enseigne-malin'], ['Avancer', 'neutre-serein'], ['toi', 'neutre-rire']],
  eleve: [[0, 'filme-confiant'], ['Avancer', 'neutre-emerveille'], ['toi', 'neutre-confiant']],
  panel: [['Travelling', 'Avancer']],
  labels: [['Travelling', 'TRAVELLING AVANT'], ['Travelling#2', 'TRAVELLING ARRIÈRE']],
  stamp: { at: 'Avancer', until: 'toi', l1: 'RÈGLE N°4', l2: 'AVANCER = ENTRER · RECULER = QUITTER' },
  cta: { type: 'chips', at: 'toi', chips: ['AVANT', 'ARRIÈRE'], label: 'LEQUEL TU UTILISES LE PLUS ?' },
  demo(t, u) {
    const A = C('Travelling'), R = C('Travelling#2');
    let k, cx = 180, cy = 304;
    if (t < R) k = lerp(1.0, 2.6, easeInOut(seg(t, A + .3, R - .4)));
    else { const p = easeInOut(seg(t, R + .1, R + 3)); k = lerp(2.6, .5, p); cx = lerp(180, 135, p); cy = lerp(304, 250, p); }
    set($('tAll'), 'transform', `translate(115 131) scale(${k}) translate(${-cx} ${-cy})`);
  },
};
