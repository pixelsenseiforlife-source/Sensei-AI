// Rend l'outro image par image (30 i/s) puis l'assemble en MP4 avec le gong.
// Utilisation : node reels/brand/outro/render_outro.js
const path = require('path'), fs = require('fs'), os = require('os'), { execFileSync } = require('child_process');
const { chromium } = require('playwright');
const DUR = 3.5, FPS = 30, IMPACT = 0.78;
(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'outro-'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'outro.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const n = Math.round(DUR * FPS);
  for (let i = 0; i < n; i++) {
    const ms = (i / FPS) * 1000;
    await p.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), ms);
    await p.screenshot({ path: path.join(tmp, String(i).padStart(4, '0') + '.png') });
  }
  await b.close();
  const wav = path.join(tmp, 'gong.wav');
  execFileSync('python3', ['-I', path.join(__dirname, 'gong.py'), wav, String(DUR), String(IMPACT)]);
  const out = path.join(__dirname, 'outro-pixel-sensei.mp4');
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(FPS), '-i', path.join(tmp, '%04d.png'), '-i', wav,
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', String(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '44100', '-shortest', out]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('outro ok ->', out);
})();
