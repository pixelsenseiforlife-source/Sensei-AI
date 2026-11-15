// Génère le PDF du guide à partir de guide.html
// Utilisation : node reels/guide/build_pdf.js
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(dir, 'guide.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.join(dir, 'Guide-La-Voie-du-Pixel.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('PDF généré');
})();
