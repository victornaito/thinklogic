// Renderiza post.html em PNG 1080x1920. Uso: node render.mjs
import { createRequire } from 'module';
import path from 'path';
import { fileURLToPath } from 'url';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const aqui = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto('file://' + path.join(aqui, 'post.html'));
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: path.join(aqui, '..', 'resultados', 'post-nvda-jensen.png') });
await browser.close();
