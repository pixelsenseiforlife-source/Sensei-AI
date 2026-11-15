// Reel 05 — Pourquoi tes vidéos sont plates (parallaxe)
const REEL = {
  titles: [[0, 'POURQUOI LA TIENNE EST PLATE ?'], ['secret', 'LA PARALLAXE'], ['Fais', 'TRAVELLING LATÉRAL'], ['Regarde', '1ER PLAN VITE · FOND LENT'], ["L'astuce", 'TOUJOURS UN 1ER PLAN'], ['Pas', 'PAS DE RAIL ?'], ['Envoie', '']],
  sensei: [[0, 'neutre-malin'], ['secret', 'enseigne-malin'], ['Envoie', 'neutre-rire']],
  eleve: [[0, 'filme-confus'], ['secret', 'neutre-emerveille'], ['Envoie', 'filme-confiant']],
  panel: [['Fais', 'Envoie']],
  labels: [['Fais', 'LA CAMÉRA GLISSE SUR LE CÔTÉ'], ['Regarde', '1ER PLAN : VITE · FOND : LENT'], ["L'astuce", 'BRANCHE · POTEAU · TABLE'], ['Pas', 'MARCHE LENTEMENT, GENOUX FLÉCHIS']],
  stamp: { at: 'qui', until: 999, l1: 'RÈGLE N°5', l2: 'UN PREMIER PLAN, TOUJOURS' },
  cta: { type: 'share', at: 'Envoie', until: 'qui' },
  demo(t, u) {
    set($('pFar'), 'transform', `translate(${-(u * 9) % 270} 0)`);
    set($('pFore'), 'transform', `translate(${-(u * 75) % 120} 0)`);
    set($('pS'), 'transform', `translate(85 ${107 - Math.abs(Math.sin(u * 8)) * 3}) scale(.3)`);
  },
};
