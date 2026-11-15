// Reel 02 — Arrête de zoomer
const REEL = {
  titles: [[0, "L'UN DES DEUX EST UNE ERREUR"], ['haut', 'ZOOM : IMAGE PLATE'], ['bas', 'TRAVELLING : PROFONDEUR'], ['zoom#2', ''], ['savais', 'TU SAVAIS ?']],
  sensei: [[0, 'enseigne-malin'], ['zoom#2', 'neutre-serein'], ['savais', 'neutre-rire']],
  eleve: [[0, 'neutre-confus'], ['zoom#2', 'neutre-emerveille'], ['savais', 'neutre-confiant']],
  panel: [['Ces', 'zoom#2']],
  stamp: { at: 'zoom#2', until: 'savais', l1: 'RÈGLE N°2', l2: 'AVANCE, NE ZOOME PAS' },
  cta: { type: 'chips', at: 'savais', chips: ['OUI', 'NON'], label: 'RÉPONDS EN COMMENTAIRE' },
  demo(t, u) {
    const H = C('haut'), B = C('bas');
    const topOn = t >= H && t < B, botOn = t >= B;
    const kz = topOn || t >= B + 4 ? 1 + .9 * easeInOut(tri((t - H) / 2.2)) : 1;
    set($('zA'), 'transform', `translate(111 62) scale(${kz}) translate(-111 -62)`);
    const e = botOn ? easeInOut(tri((t - B) / 2.2)) : 0;
    set($('bBg'), 'transform', `translate(111 100) scale(${1 + .2 * e}) translate(-111 -100)`);
    set($('bSub'), 'transform', `translate(111 118) scale(${1 + 1.1 * e}) translate(-111 -118)`);
    $('dimA').setAttribute('opacity', botOn && t < B + 4 ? .55 : 0); $('dimB').setAttribute('opacity', topOn ? .55 : 0);
  },
};
