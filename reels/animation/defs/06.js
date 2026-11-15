// Reel 06 — Rends quelqu'un puissant (panoramique & tilt)
const REEL = {
  titles: [[0, '1 MOUVEMENT. + DE PRÉSENCE.'], ['Le', 'LE PANORAMIQUE'], ["l'horizontale", 'HORIZONTAL : SUIVRE'], ['verticale', 'VERTICAL : LE TILT'], ["l'inverse", 'CIEL → SOL : UN LIEU'], ['Teste', ''], ['abonne', 'LA SUITE DEMAIN']],
  sensei: [[0, 'neutre-serein'], ['Le', 'enseigne-malin'], ['Teste', 'neutre-serein'], ['abonne', 'camera-rire']],
  eleve: [[0, 'neutre-confiant'], ['Teste', 'neutre-emerveille'], ['abonne', 'filme-emerveille']],
  panel: [[0, 'Le'], ["l'horizontale", 'Teste']],
  labels: [[0, 'TILT : DES PIEDS AU VISAGE'], ["l'horizontale", 'PANORAMIQUE HORIZONTAL'], ['verticale', 'TILT : DES PIEDS AU VISAGE'], ["l'inverse", 'DU CIEL VERS LE SOL']],
  stamp: { at: 'Teste', until: 'abonne', l1: 'RÈGLE N°6', l2: 'MONTE POUR GRANDIR' },
  cta: { type: 'subscribe', at: 'abonne' },
  demo(t, u) {
    const L = C('Le'), H = C("l'horizontale"), V = C('verticale'), I = C("l'inverse"), E = C('Teste');
    const mode = t < L ? 'tilt' : t < V ? 'pano' : t < I ? 'tilt' : 'sky';
    $('tiltG').style.display = mode === 'tilt' ? '' : 'none'; $('panoG').style.display = mode === 'pano' ? '' : 'none'; $('skyG').style.display = mode === 'sky' ? '' : 'none';
    if (mode === 'tilt') { const s = t < L ? 0 : V; const e = t < L ? L : I; const y = lerp(-190, 0, easeInOut(seg(t, s + .4, e - .4)));
      set($('tiltS'), 'transform', `translate(10 ${y}) scale(1.05)`); }
    if (mode === 'pano') { set($('panoS'), 'transform', `translate(${lerp(0, -148, easeInOut(seg(t, H + .3, V - .3)))} 0)`);
      set($('panoM'), 'transform', `translate(85 ${95 - Math.abs(Math.sin(t * 8)) * 3}) scale(.28)`); }
    if (mode === 'sky') set($('skyS'), 'transform', `translate(-20 ${lerp(0, -218, easeInOut(seg(t, I + .3, E - .3)))})`);
  },
};
