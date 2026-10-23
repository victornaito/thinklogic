// base.js · grão do papel com semente fixa e o hodômetro (data-valor="1.322" ou "?.???").
(function () {
  const c = document.getElementById('grao');
  if (c) {
    const x = c.getContext('2d'), d = x.createImageData(c.width, c.height);
    let s = Number(c.dataset.semente || 7);
    const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    for (let i = 0; i < d.data.length; i += 4) {
      const v = 200 + r() * 55;
      d.data[i] = d.data[i + 1] = d.data[i + 2] = v; d.data[i + 3] = 255;
    }
    x.putImageData(d, 0, 0);
  }
  document.querySelectorAll('.digitos[data-valor]').forEach(el => {
    el.innerHTML = [...el.dataset.valor]
      .map(ch => ch === '.' ? '<span class="sep">.</span>' : `<span>${ch}</span>`).join('');
  });
})();
