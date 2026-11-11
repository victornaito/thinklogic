// Lê os tempos das animações do post.html e grava events.json para a trilha sonora.
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { writeFileSync } from 'node:fs';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.join(dir, 'post.html'));

const data = await page.evaluate(() => {
  const ev = [];
  const scenes = [...document.querySelectorAll('.scene')];
  scenes.forEach((s, i) => {
    const st = +s.dataset.start;
    ev.push({ type: 'scene', t: st, idx: i });
    const rel = (el, k, d = 0) => el.dataset[k] !== undefined ? parseFloat(el.dataset[k]) : d;
    s.querySelectorAll('[data-a]').forEach(el => {
      const a = el.dataset.a;
      if (a === 'up' || a === 'fade') return;
      ev.push({ type: a, t: st + rel(el, 't'), d: rel(el, 'd', .45) });
    });
    s.querySelectorAll('[data-count]').forEach(el => ev.push({ type: 'count', t: st + rel(el, 't'), d: rel(el, 'cd', 1) }));
    s.querySelectorAll('[data-pulse]').forEach(el => ev.push({ type: 'pulse', t: st + +el.dataset.pulse }));
    s.querySelectorAll('[data-strike]').forEach(el => ev.push({ type: 'strike', t: st + +el.dataset.strike }));
    if (s.querySelector('#beam')) ev.push({ type: 'balance', t: st + 1.2 });
  });
  return { duration: window.DURATION, events: ev.sort((a, b) => a.t - b.t) };
});

writeFileSync(path.join(dir, 'events.json'), JSON.stringify(data, null, 1));
await browser.close();
console.log(data.events.length, 'eventos');
