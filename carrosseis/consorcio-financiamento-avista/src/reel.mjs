// Renderiza src/reel.html (1080x1920) quadro a quadro via window.seek(t).
// Uso: node src/reel.mjs previa 0 5 12 ...   → resultados/reel-previa/t-NN.png (quadros soltos pra conferir)
//      node src/reel.mjs video [trabalhadores] → audio/reel-mudo.mp4 + audio/beats.json (em blocos de 8 s pro musica.py)
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const { chromium } = createRequire(import.meta.url)('playwright');
const raiz = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const [modo = 'video', ...resto] = process.argv.slice(2);
const FPS = 30;
const url = 'file://' + path.join(raiz, 'src', 'reel.html');
const args = ['--disable-gpu', '--force-color-profile=srgb', '--allow-file-access-from-files'];

async function abre(browser) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(200);
  return page;
}

const browser = await chromium.launch({ args });

if (modo === 'previa') {
  const dir = path.join(raiz, 'resultados', 'reel-previa');
  mkdirSync(dir, { recursive: true });
  const page = await abre(browser);
  for (const t of resto.map(Number)) {
    await page.evaluate(t => window.seek(t), t);
    await page.screenshot({ path: path.join(dir, `t-${String(t).padStart(5, '0')}.png`) });
  }
} else {
  const n = Number(resto[0] || 4);
  const page0 = await abre(browser);
  const { dur, cues } = await page0.evaluate(() => ({ dur: window.DURACAO, cues: window.CUES }));
  await page0.close();

  // som: o musica.py trabalha por "slide"; o reel vira blocos de 8 s (4 compassos) seguidos
  const BLOCO = 8, blocos = Math.ceil(dur / BLOCO);
  const slides = Array.from({ length: blocos }, (_, k) => ({
    slide: k + 1, duracao_s: BLOCO,
    eventos: cues.filter(c => c.t >= k * BLOCO && c.t < (k + 1) * BLOCO).map(c => ({ ...c, t: +(c.t - k * BLOCO).toFixed(3) }))
  }));
  mkdirSync(path.join(raiz, 'audio'), { recursive: true });
  writeFileSync(path.join(raiz, 'audio', 'beats.json'), JSON.stringify({ bpm: 120, slides }, null, 1));

  const total = Math.round(dur * FPS);
  const dir = path.join(raiz, 'audio', 'reel-quadros');
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });
  const fatia = Math.ceil(total / n);
  await Promise.all(Array.from({ length: n }, async (_, w) => {
    const page = await abre(browser);
    for (let f = w * fatia; f < Math.min(total, (w + 1) * fatia); f++) {
      await page.evaluate(t => window.seek(t), f / FPS);
      await page.screenshot({ path: path.join(dir, `f${String(f).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 95 });
    }
  }));
  const r = spawnSync('ffmpeg', ['-y', '-hide_banner', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(dir, 'f%05d.jpg'),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p',
    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', path.join(raiz, 'audio', 'reel-mudo.mp4')], { stdio: 'inherit' });
  if (r.status !== 0) throw new Error('ffmpeg falhou');
  rmSync(dir, { recursive: true, force: true });
  console.log(`${total} quadros → audio/reel-mudo.mp4`);
}
await browser.close();
