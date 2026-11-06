// Exporta os slides de um carrossel como PNG 1080x1350.
// Uso: node export-slides.mjs <pasta-do-carrossel>  → <pasta>/slides/01.png, 02.png, ...
// A página precisa expor window.renderSlide(i) e window.SLIDE_COUNT.
import { chromium } from 'playwright';
import { mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const dir = path.resolve(process.argv[2]);
const outDir = path.join(dir, 'slides');
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto('file://' + path.join(dir, 'index.html') + '?capture');
await page.evaluate(() => document.fonts.ready);
const n = await page.evaluate(() => window.SLIDE_COUNT);
for (let i = 0; i < n; i++) {
  const png = await page.evaluate(i => { window.renderSlide(i); return document.querySelector('canvas').toDataURL('image/png'); }, i);
  writeFileSync(path.join(outDir, String(i + 1).padStart(2, '0') + '.png'), Buffer.from(png.split(',')[1], 'base64'));
}
await browser.close();
console.log(`ok: ${n} slides em ${outDir}`);
