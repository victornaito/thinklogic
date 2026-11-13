// base.js · monta o fundo (luzes desfocadas + mesa + grão, com semente fixa), o rodapé,
// encaixa as ilustrações ([data-il]) e ajusta as linhas da capa à largura ([data-fit]).
(function () {
  const q = document.getElementById('quadro');
  let s = Number(q.dataset.semente || 7);
  const r = () => (s = (s * 16807) % 2147483647) / 2147483647;

  // luzes quentes fora de foco, só na metade de cima
  const tom = q.dataset.tom || 'ambar';
  const cor = tom === 'frio' ? [255, 226, 150] : [255, 168, 92];
  const b = document.createElement('div'); b.className = 'bokeh';
  const n = Number(q.dataset.luzes || 13);
  for (let k = 0; k < n; k++) {
    const d = 70 + r() * 190, a = 0.06 + r() * 0.13, i = document.createElement('i');
    i.style.cssText = `left:${-80 + r() * 1160}px;top:${-90 + r() * 560}px;width:${d}px;height:${d}px;` +
      `background:rgba(${cor[0]},${cor[1]},${cor[2]},${a.toFixed(3)});`;
    b.appendChild(i);
  }
  const m = document.createElement('div'); m.className = 'mesa';
  const g = document.createElement('canvas'); g.id = 'grao'; g.width = 540; g.height = 675;
  q.prepend(b, m, g);
  const x = g.getContext('2d'), dt = x.createImageData(g.width, g.height);
  for (let p = 0; p < dt.data.length; p += 4) {
    const v = 90 + r() * 110; dt.data[p] = dt.data[p + 1] = dt.data[p + 2] = v; dt.data[p + 3] = 255;
  }
  x.putImageData(dt, 0, 0);

  // rodapé
  const n0 = q.dataset.n, tot = q.dataset.total || '09';
  if (n0) {
    const f = document.createElement('div'); f.className = 'rodape';
    f.innerHTML = `<span>@victornaito.financas</span><span class="pt"></span><span>${n0}/${tot}</span>` +
      (n0 !== tot ? `<span class="pt"></span><span class="seta">arrasta →</span>` : '');
    q.appendChild(f);
  }

  // ilustrações
  document.querySelectorAll('[data-il]').forEach(el => { el.innerHTML = window.IL[el.dataset.il] || ''; });

  // linhas que ocupam a largura inteira (capa)
  const ajusta = () => document.querySelectorAll('[data-fit]').forEach(el => {
    const alvo = Number(el.dataset.fit), max = Number(el.dataset.max || 400);
    if (!el.firstElementChild) el.innerHTML = `<span style="display:inline-block;white-space:nowrap">${el.innerHTML}</span>`;
    el.style.fontSize = '100px';
    const w = el.firstElementChild.getBoundingClientRect().width;
    el.style.fontSize = Math.min(max, 100 * alvo / w) + 'px';
  });
  document.fonts.ready.then(ajusta);
})();
