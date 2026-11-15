// Reel 03 — L'effet Vertigo
const REEL = {
  titles: [[0, 'REGARDE LE DÉCOR.'], ["C'est", "L'EFFET VERTIGO"], ['secret', 'AVANCE + DÉZOOME'], ['Ton', 'LE SUJET NE BOUGE PAS'], ['Effet', 'CHOC · RÉVÉLATION · DÉCLIC'], ['Astuce', 'VERSION SMARTPHONE'], ['Enregistre', '']],
  sensei: [[0, 'neutre-malin'], ['Effet', 'enseigne-malin'], ['Enregistre', 'camera-rire']],
  eleve: [[0, 'neutre-emerveille'], ['Effet', 'neutre-emerveille'], ['Enregistre', 'filme-confiant']],
  panel: [[0, 'Effet'], ['Astuce', 'Enregistre']],
  labels: [[0, ''], ['secret', 'TRAVELLING AVANT + ZOOM ARRIÈRE'], ['Ton', 'LE SUJET GARDE SA TAILLE'], ['Astuce', 'RECADRE PROGRESSIVEMENT AU MONTAGE']],
  stamp: { at: 'Tu#3', until: 999, l1: 'À TESTER', l2: 'CE WEEK-END' },
  cta: { type: 'save', at: 'Enregistre', until: 'Tu#3' },
  demo(t, u) {
    const f = lerp(1.35, .78, easeInOut(tri(t / 2.4)));
    set($('vBg'), 'transform', `translate(115 120) scale(${f}) translate(-115 -120)`);
  },
};
