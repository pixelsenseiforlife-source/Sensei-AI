// Reel 07 — Caméra qui tremble : erreur ?
const REEL = {
  titles: [[0, 'ERREUR… OU CHOIX ?'], ['Ça', "TOUT DÉPEND DE L'INTENTION"], ['Caméra#2', 'ÉPAULE : NERVEUX'], ['Caméra#3', 'STABILISÉ : ÉLÉGANT'], ['problème', ''], ['toi', 'TON STYLE ?']],
  sensei: [[0, 'neutre-malin'], ['Caméra#2', 'enseigne-malin'], ['problème', 'stop-severe'], ['toi', 'neutre-rire']],
  eleve: [[0, 'filme-confus'], ['problème', 'neutre-confus'], ['toi', 'neutre-confiant']],
  panel: [[0, 'Ça'], ['Caméra#2', 'problème']],
  stamp: { at: 'problème', until: 'toi', l1: 'RÈGLE N°7', l2: 'TREMBLER SANS RAISON = ERREUR' },
  cta: { type: 'chips', at: 'toi', chips: ['ÉPAULE', 'STABILISÉ'], label: 'ET TOI, TU ES PLUTÔT…' },
  demo(t, u) {
    const S = C('Caméra#3'); const topOn = t < S, botOn = t >= S;
    const dx = topOn ? noise(t, 4.7, 1) * 4 : 0, dy = topOn ? noise(t, 5.9, 2) * 3 : 0, r = topOn ? noise(t, 3.3, 3) * 2 : 0;
    set($('shA'), 'transform', `translate(${dx} ${dy}) rotate(${r} 115 64)`);
    set($('shMA'), 'transform', `translate(86 ${12 - Math.abs(Math.sin(t * 9)) * 4}) scale(.25)`);
    set($('shBgB'), 'transform', `translate(${botOn ? -((t - S) * 5) % 40 : 0} 0)`);
    set($('shMB'), 'transform', `translate(86 ${12 - (botOn ? Math.abs(Math.sin(t * 9)) * 1.5 : 0)}) scale(.25)`);
    $('dimA').setAttribute('opacity', botOn ? .55 : 0); $('dimB').setAttribute('opacity', topOn ? .55 : 0);
  },
};
