// Base visual @victornaito.financas: fundo escuro, destaques dourados, canvas 1080x1920.
const W = 1080, H = 1920;
const cv = document.getElementById('c'), ctx = cv.getContext('2d');
const GOLD = '#E2B84B', GOLD_HI = '#FFE29A', GOLD_DK = '#9A7424', INK = '#F4EFE4', MUTED = '#8C877C';
const UP = '#4CC38A', DOWN = '#F0585E';
const F = (w, s) => `${w} ${s}px Inter, "Inter Display", system-ui, sans-serif`;

const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const prog = (t, a, b) => clamp((t - a) / (b - a));
const easeOut = x => 1 - Math.pow(1 - x, 3);
const easeInOut = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const backOut = x => { const c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const ptBR = (v, d = 2) => v.toFixed(d).replace('.', ',');

let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const DUST = Array.from({length: 70}, () => ({x: rnd() * W, y: rnd() * H, r: .6 + rnd() * 2.2, s: 8 + rnd() * 30, p: rnd() * 6.28}));

function roundRect(x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
function goldGrad(x0, y0, x1, y1) {
  const g = ctx.createLinearGradient(x0, y0, x1, y1);
  g.addColorStop(0, GOLD_HI); g.addColorStop(.45, GOLD); g.addColorStop(1, GOLD_DK); return g;
}
function card(x, y, w, h, r = 36) {
  roundRect(x, y, w, h, r);
  const cg = ctx.createLinearGradient(0, y, 0, y + h);
  cg.addColorStop(0, '#15130F'); cg.addColorStop(1, '#0B0A08');
  ctx.fillStyle = cg; ctx.fill();
  ctx.strokeStyle = 'rgba(226,184,75,0.28)'; ctx.lineWidth = 2; ctx.stroke();
}

function background(t, mark = 'R$') {
  const g = ctx.createLinearGradient(0, 0, 0, H);
  g.addColorStop(0, '#0C0B0A'); g.addColorStop(.5, '#060607'); g.addColorStop(1, '#100D07');
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  const rg = ctx.createRadialGradient(W * .5, 980, 40, W * .5, 980, 900);
  rg.addColorStop(0, 'rgba(226,184,75,0.10)'); rg.addColorStop(1, 'rgba(226,184,75,0)');
  ctx.fillStyle = rg; ctx.fillRect(0, 0, W, H);
  ctx.save(); ctx.globalAlpha = .035; ctx.fillStyle = GOLD; ctx.font = F(900, 760);
  ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
  ctx.fillText(mark, W / 2 + Math.sin(t * .3) * 10, 1500); ctx.restore();
  for (const d of DUST) {
    const y = (d.y - t * d.s + H) % H, a = .15 + .25 * (.5 + .5 * Math.sin(t * 1.3 + d.p));
    ctx.fillStyle = `rgba(226,184,75,${a})`; ctx.beginPath(); ctx.arc(d.x, y, d.r, 0, 6.29); ctx.fill();
  }
}

// Faixa dourada + título grande + @ (mesmo cabeçalho do vídeo de poder de compra)
function header(t, band, title, sub) {
  const p = easeOut(prog(t, .1, .9));
  ctx.save(); ctx.globalAlpha = p; ctx.translate(0, (1 - p) * -40);
  ctx.font = F(900, 74);
  const bw = ctx.measureText(band).width + 140;
  ctx.fillStyle = goldGrad(0, 180, bw, 330);
  ctx.beginPath(); ctx.moveTo(0, 200); ctx.lineTo(bw * p + 20, 200); ctx.lineTo(bw * p - 40, 300); ctx.lineTo(0, 300); ctx.fill();
  ctx.fillStyle = '#0A0907'; ctx.textBaseline = 'middle'; ctx.textAlign = 'left';
  ctx.fillText(band, 60, 252);
  ctx.fillStyle = INK; ctx.font = F(900, 92); ctx.fillText(title, 60, 370);
  ctx.fillStyle = GOLD; ctx.font = F(700, 32); ctx.fillText(sub, 64, 445);
  ctx.restore();
}

// Bloco de manchete com barra dourada; lines = [[{s, c}]], c pode ser 'gold'
function headline(t, lines, top, start, size = 58, lh = 74) {
  const pbar = easeOut(prog(t, start - .2, start + .4));
  ctx.fillStyle = goldGrad(0, top - 50, 0, top + lh * lines.length);
  ctx.fillRect(60, top - size, 6, (lh * lines.length) * pbar);
  lines.forEach((ln, i) => {
    const p = easeOut(prog(t, start + i * .22, start + .6 + i * .22));
    if (p <= 0) return;
    ctx.save(); ctx.globalAlpha = p; ctx.translate((1 - p) * 60, 0);
    ctx.font = F(900, size); ctx.textBaseline = 'alphabetic'; ctx.textAlign = 'left';
    let x = 96;
    for (const seg of ln) {
      ctx.fillStyle = seg.c === 'gold' ? goldGrad(0, top + i * lh - size, 0, top + i * lh) : seg.c;
      ctx.fillText(seg.s, x, top + i * lh); x += ctx.measureText(seg.s).width;
    }
    ctx.restore();
  });
}

function footnote(t, text, at, y = 1840) {
  const p = prog(t, at, at + .6);
  if (p <= 0) return;
  ctx.save(); ctx.globalAlpha = p; ctx.fillStyle = MUTED; ctx.font = F(500, 24);
  ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic'; ctx.fillText(text, 96, y); ctx.restore();
}

// Triângulo ▲ / ▼ ou "=" centrado em (x, y)
function trend(x, y, dir, s = 1) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  if (dir === 0) {
    ctx.fillStyle = GOLD; ctx.fillRect(-16, -10, 32, 7); ctx.fillRect(-16, 4, 32, 7);
  } else {
    ctx.fillStyle = dir > 0 ? UP : DOWN; ctx.beginPath();
    if (dir > 0) { ctx.moveTo(0, -16); ctx.lineTo(18, 14); ctx.lineTo(-18, 14); }
    else { ctx.moveTo(0, 16); ctx.lineTo(18, -14); ctx.lineTo(-18, -14); }
    ctx.closePath(); ctx.fill();
  }
  ctx.restore();
}

function startLoop(render, duration) {
  window.render = render; window.DURATION = duration;
  if (new URLSearchParams(location.search).has('capture')) return;
  const start = performance.now();
  const loop = now => { render(((now - start) / 1000) % (duration + 1.5)); requestAnimationFrame(loop); };
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => requestAnimationFrame(loop));
}
