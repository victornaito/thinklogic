// Versão viva: fotografa src/slide-NN.html quadro a quadro via window.seek(t) e monta o MP4 mudo,
// escreve audio/beats.json com os acertos (window.CUES) e guarda os quadros de teste.
// Uso: node src/vivo.mjs 01   (depois: python3 src/musica.py e o mux do vivo.sh)
import { createRequire } from 'node:module';
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const { chromium } = createRequire(import.meta.url)('playwright');
const raiz = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const n = process.argv[2] || '01';
const FPS = 30;
const quadros = path.join(raiz, 'resultados', 'quadros', `slide-${n}`);
mkdirSync(quadros, { recursive: true });
mkdirSync(path.join(raiz, 'audio'), { recursive: true });

const browser = await chromium.launch({ args: ['--disable-gpu', '--force-color-profile=srgb', '--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.goto('file://' + path.join(raiz, 'src', `slide-${n}.html`));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(200);

const { dur, cues } = await page.evaluate(() => ({ dur: window.DURACAO, cues: window.CUES }));
writeFileSync(path.join(raiz, 'audio', 'beats.json'),
  JSON.stringify({ bpm: 120, slides: [{ slide: Number(n), duracao_s: dur, eventos: cues }] }, null, 1));

const mudo = path.join(raiz, 'audio', `slide-${n}-mudo.mp4`);
const ff = spawn('ffmpeg', ['-y', '-hide_banner', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '15', '-pix_fmt', 'yuv420p',
  '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', mudo]);
const total = Math.round(dur * FPS);
for (let f = 0; f < total; f++) {
  const t = f / FPS;
  await page.evaluate(t => window.seek(t), t);
  const png = await page.screenshot({ type: 'png' });
  if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
  // quadro 0, último, e um por batida (0,5 s) pra folha
  if (f === 0 || f === total - 1 || f % (FPS / 2) === 0) writeFileSync(path.join(quadros, `t${t.toFixed(2).padStart(5, '0')}.png`), png);
}
ff.stdin.end();
await new Promise((ok, erro) => ff.on('close', c => c === 0 ? ok() : erro(new Error('ffmpeg ' + c))));
await page.evaluate(() => window.seek(0));
writeFileSync(path.join(quadros, 'seek0.png'), await page.screenshot({ type: 'png' }));
await browser.close();
console.log(`${total} quadros → ${mudo}`);
