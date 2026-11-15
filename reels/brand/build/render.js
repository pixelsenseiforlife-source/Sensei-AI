// Rend la bible en PDF et la maquette en PNG 1080x1920
// Utilisation : python3 -I reels/brand/build/build_bible.py && node reels/brand/build/render.js
const path = require('path'); const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'bible.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, '..', 'Bible-graphique-La-Voie-du-Pixel.pdf'), printBackground: true, preferCSSPageSize: true });
  const m = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await m.goto('file://' + path.join(__dirname, '..', 'maquettes', 'maquette-reel.svg'));
  await m.screenshot({ path: path.join(__dirname, '..', 'maquettes', 'maquette-reel.png') });
  await b.close(); console.log('rendu ok');
})();
