// Capa viva (8 s, 120 BPM): tudo é função pura de t; seek(0) é exatamente o PNG estático.
(function () {
  const $ = id => document.getElementById(id);
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const fase = (t, a, b) => clamp((t - a) / (b - a));
  const inOut = u => u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
  const outC = u => 1 - Math.pow(1 - u, 3);
  const sino = u => 0.5 - 0.5 * Math.cos(2 * Math.PI * clamp(u));
  const mola = (t, a, dur, ciclos = 1.5) => {
    const u = (t - a) / dur; if (u <= 0 || u >= 1) return 0;
    return Math.exp(-3 * u) * Math.sin(2 * Math.PI * ciclos * u) * (1 - u);
  };
  const tf = (el, s) => { el.style.transform = s; };

  // rolos do 1.073: fita d, d+1, …, d+10 (= d)
  const rolos = [...document.querySelectorAll('#numero .rolo')];
  rolos.forEach(r => {
    const d = Number(r.textContent);
    r.innerHTML = '<span class="fita">' + Array.from({ length: 11 }, (_, k) => `<span>${(d + k) % 10}</span>`).join('') + '</span>';
  });
  const fitas = rolos.map(r => r.firstChild);
  const textos = [...document.querySelectorAll('.riscada, .abaixo, .numero, #pormes')];
  const dentro = document.querySelector('#pormes .dentro');
  const carro = $('carro'), grao = $('grao'), risco = $('risco');
  carro.style.transformOrigin = '50% 80%';

  window.DURACAO = 8;
  window.CUES = [
    { t: 1.0, tipo: 'whoosh', o_que: 'risco de caneta', gain: 0.8 },
    { t: 1.5, tipo: 'clique', o_que: 'rolo 1' }, { t: 1.65, tipo: 'clique', o_que: 'rolo 2' },
    { t: 1.8, tipo: 'clique', o_que: 'rolo 3' }, { t: 1.95, tipo: 'clique', o_que: 'rolo 4' },
    { t: 2.5, tipo: 'land', o_que: 'km pousa', gain: 0.7 },
    { t: 3.0, tipo: 'clique', o_que: 'frase sobe' },
    { t: 3.5, tipo: 'pop', o_que: 'etiqueta balança' }, { t: 4.0, tipo: 'pop', o_que: 'etiqueta balança', gain: 0.6 },
    { t: 5.0, tipo: 'land', o_que: 'tranco do carro', gain: 0.8 },
    { t: 6.5, tipo: 'clique', o_que: 'seta' }, { t: 7.0, tipo: 'clique', o_que: 'seta' }
  ];

  window.seek = function (t) {
    // câmera: empurra devagar e volta
    const p = sino(fase(t, 0.5, 7.5));
    tf(grao, p ? `scale(${1 + 0.01 * p})` : '');
    textos.forEach(el => tf(el, p ? `scale(${1 + 0.02 * p})` : ''));

    // o risco recolhe (0,5 a 0,8): a frase aparece limpa; e se redesenha à mão (1,0 a 1,5)
    let corte = 0;
    if (t >= 0.5 && t < 0.8) corte = inOut(fase(t, 0.5, 0.8));
    else if (t >= 0.8 && t < 1.0) corte = 1;
    else if (t >= 1.0 && t < 1.5) corte = 1 - outC(fase(t, 1.0, 1.5));
    risco.style.setProperty('--corte', corte ? (corte * 100).toFixed(2) + '%' : '');

    // rolos do 1.073 (1,5 a 2,4)
    fitas.forEach((f, j) => {
      const u = inOut(fase(t, 1.5 + j * 0.15, 2.0 + j * 0.15));
      tf(f, u > 0 && u < 1 ? `translateY(${-10 * u}em)` : '');
    });

    // "km" pousa esmagando (2,5)
    const km = $('km'), mk = mola(t, 2.5, 0.4, 1);
    tf(km, mk ? `scale(${1 + 0.08 * mk}, ${1 - 0.1 * mk})` : '');

    // "por mês, caro é o seu carro." desce pela máscara e sobe esticando (2,7 a 3,0)
    let y = 0, sy = 1;
    if (t >= 2.7 && t < 2.9) y = 115 * inOut(fase(t, 2.7, 2.9));
    else if (t >= 2.9 && t < 3.0) { const u = fase(t, 2.9, 3.0); y = 115 * (1 - outC(u)); sy = 1 + 0.12 * (1 - u); }
    else if (t >= 3.0 && t < 3.4) sy = 1 - 0.06 * mola(t, 3.0, 0.4, 1);
    tf(dentro, (y || sy !== 1) ? `translateY(${y}%) scaleY(${sy})` : '');

    // etiqueta PARADO balança no retrovisor (3,5 a 4,7)
    const a = 9 * mola(t, 3.5, 1.2, 2);
    tf($('etiqueta'), a ? `rotate(${5 + a}deg)` : '');
    tf($('cordao'), a ? `rotate(${12 + a}deg)` : '');

    // tranco do carro (5,0): alguém tentou dar partida
    const tr = mola(t, 5.0, 0.7, 2);
    tf(carro, (p || tr) ? `translateY(${-6 * tr}px) scale(${1 + 0.035 * p})` : '');

    // seta empurra duas vezes
    const e = mola(t, 6.5, 0.45, 0.5) + mola(t, 7.0, 0.45, 0.5);
    tf($('seta'), e ? `translateX(${16 * e}px)` : '');
  };
})();
