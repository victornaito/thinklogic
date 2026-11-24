// Renderiza src/slide-NN.html em resultados/estatico/slide-NN.png (1080x1350).
// Uso: node src/render.mjs [01 02 ...]   (sem argumento: todos)
import { createRequire } from 'node:module';
import { readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

// playwright global (NODE_PATH) ou local: o import ESM não lê NODE_PATH, o require lê
const { chromium } = createRequire(import.meta.url)('playwright');
const raiz = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const pedidos = process.argv.slice(2);
const slides = readdirSync(path.join(raiz, 'src'))
  .filter(f => /^slide-\d\d\.html$/.test(f))
  .filter(f => !pedidos.length || pedidos.includes(f.slice(6, 8)));

const browser = await chromium.launch({ args: ['--disable-gpu', '--force-color-profile=srgb', '--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const f of slides) {
  await page.goto('file://' + path.join(raiz, 'src', f));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  const out = path.join(raiz, 'resultados', 'estatico', f.replace('.html', '.png'));
  await page.screenshot({ path: out });
  console.log(out);
}
await browser.close();
