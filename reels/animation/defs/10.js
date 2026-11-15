// Reel 10 — Les 4 règles de la Voie
const REEL = {
  titles: [[0, "4 RÈGLES. FINI L'AMATEUR."], ['Un', ''], ['guide', 'LE GUIDE GRATUIT'], ['Écris', 'COMMENTE « SENSEI »']],
  sensei: [[0, 'neutre-serein'], ['Un', 'enseigne-malin'], ['Quatre#2', 'neutre-serein'], ['guide', 'camera-rire']],
  eleve: [[0, 'filme-confiant'], ['Un', 'neutre-emerveille'], ['Écris', 'filme-emerveille']],
  impacts: ['Un+0.25', 'Deux+0.25', 'Trois+0.25', 'Quatre#2+0.25'],
  cta: { type: 'keyword', at: 'Écris', y: 300 },
  extra(t) {
    const G = C('guide');
    ['Un', 'Deux', 'Trois', 'Quatre#2'].forEach((c, i) => {
      const a = C(c), el = $('r' + (i + 1)), on = t >= a && t < G;
      el.style.display = on ? '' : 'none'; if (!on) return;
      const p = seg(t, a, a + .25); const k = lerp(2.2, 1, easeOut(p));
      el.setAttribute('transform', `translate(135 ${96 + i * 31}) scale(${k}) rotate(${lerp(-6, 0, p)})`); el.style.opacity = seg(t, a, a + .08);
    });
    const g = $('guide'); g.style.display = t >= G ? '' : 'none';
    if (t >= G) g.setAttribute('transform', `translate(135 165) scale(${back(seg(t, G, G + .35)) * (1 + .02 * Math.sin(t * 2))})`);
  },
};
