// Rend un reel image par image, mixe voix + gong, ajoute l'outro du logo.
// Utilisation : node reels/animation/render_reel.js 01 [--preview]
const path = require('path'), fs = require('fs'), os = require('os'), { execFileSync } = require('child_process');
const { chromium } = require('playwright');
const id = process.argv[2] || '01'; const preview = process.argv.includes('--preview');
const REELS = path.join(__dirname, '..');
const scripts = fs.readdirSync(path.join(REELS, 'scripts')).filter(f => f.startsWith(id + '-'));
const slug = scripts[0].replace('.md', '');
(async () => {
  const dir = path.join(__dirname, id); const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'reel-'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(dir, 'scene.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const { duration, fps, impact } = await p.evaluate(() => ({ duration: DATA.duration, fps: DATA.fps, impact: 23.4 + .3 }));
  if (preview) {
    for (const t of [0.5, 3.0, 5.0, 7.5, 10.5, 14.0, 16.0, 17.0, 21.0, 24.5, 29.5, 31.5]) {
      await p.evaluate(t => render(t), t); await p.screenshot({ path: path.join(dir, `preview-${String(t).padStart(4, '0')}.jpg`), type: 'jpeg', quality: 80 });
    }
    await b.close(); console.log('aperçus ok'); return;
  }
  const n = Math.ceil(duration * fps) + Math.round(.4 * fps); // petite respiration avant l'outro
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => render(t), i / fps);
    await p.screenshot({ path: path.join(tmp, String(i).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 92 });
  }
  await b.close();
  const gong = path.join(tmp, 'gong.wav');
  execFileSync('python3', ['-I', path.join(REELS, 'brand', 'outro', 'gong.py'), gong, String(n / fps), String(impact)]);
  const body = path.join(tmp, 'body.mp4');
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(fps), '-i', path.join(tmp, '%05d.jpg'),
    '-i', path.join(REELS, 'voiceover', 'audio', slug + '.mp3'), '-i', gong,
    '-filter_complex', '[1:a]apad,aresample=44100,aformat=channel_layouts=stereo[v];[2:a]volume=0.45,aresample=44100,aformat=channel_layouts=stereo[g];[v][g]amix=inputs=2:duration=first:normalize=0[a]',
    '-map', '0:v', '-map', '[a]', '-t', String(n / fps), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', String(fps), '-c:a', 'aac', '-b:a', '192k', body]);
  const out = path.join(REELS, 'export', `${slug}.mp4`); fs.mkdirSync(path.dirname(out), { recursive: true });
  // transition en iris vers l'outro + volume normalisé pour les réseaux (-14 LUFS)
  const X = 0.35, off = (n / fps - X).toFixed(3);
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', body, '-i', path.join(REELS, 'brand', 'outro', 'outro-pixel-sensei.mp4'),
    '-filter_complex', `[0:v]settb=AVTB,fps=${fps}[a0];[1:v]settb=AVTB,fps=${fps}[b0];[a0][b0]xfade=transition=circleclose:duration=${X}:offset=${off}[v];` +
      `[0:a][1:a]acrossfade=d=${X}[am];[am]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]`,
    '-map', '[v]', '-map', '[a]',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', String(fps), '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('reel ok ->', out);
})();
