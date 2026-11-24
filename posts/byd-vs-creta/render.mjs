// Renderiza post.html quadro a quadro e monta o MP4 com ffmpeg.
// Uso: node render.mjs [saida.mp4] [--stills t1,t2,...]
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const out = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(dir, 'byd-vs-creta.mp4');
const stillsArg = process.argv.indexOf('--stills');
const FPS = 30;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto('file://' + path.join(dir, 'post.html'));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(500);

if (stillsArg > -1) {
  for (const t of process.argv[stillsArg + 1].split(',')) {
    await page.evaluate(x => window.render(x), +t);
    await page.screenshot({ path: path.join(dir, `still-${t}.png`) });
  }
  await browser.close();
  process.exit(0);
}

const duration = await page.evaluate(() => window.DURATION);
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

const frames = Math.round(duration * FPS);
for (let i = 0; i < frames; i++) {
  await page.evaluate(x => window.render(x), i / FPS);
  const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 150 === 0) console.log(`frame ${i}/${frames}`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log('ok', out);
