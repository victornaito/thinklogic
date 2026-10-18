// Renderiza index.html em MP4 1080x1920 @30fps: node render.mjs [saida.mp4]
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const out = process.argv[2] || path.join(dir, 'poder-de-compra.mp4');
const FPS = 30;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto('file://' + path.join(dir, 'index.html') + '?capture');
await page.evaluate(() => document.fonts.ready);
const duration = await page.evaluate(() => window.DURATION);
const canvas = await page.$('canvas');

const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

const frames = Math.round(duration * FPS);
for (let f = 0; f < frames; f++) {
  const png = await page.evaluate(t => { window.render(t); return document.querySelector('canvas').toDataURL('image/png'); }, f / FPS);
  ff.stdin.write(Buffer.from(png.split(',')[1], 'base64'));
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log('ok:', out);
