// ilustras-bf.js · objetos deste carrossel (celular, TV, console, etiqueta), mesma família do ilustras.js.
(function () {
  const sombra = (cx, cy, rx, ry = 9) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#000" opacity=".42"/>`;
  Object.assign(window.IL, {
    celular: `
<svg class="il" viewBox="0 0 150 290" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="bf-cl" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#3A3F48"/><stop offset="1" stop-color="#14171C"/></linearGradient>
  <linearGradient id="bf-tl" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#F0604A"/><stop offset=".55" stop-color="#8E2A5A"/><stop offset="1" stop-color="#1F2A55"/></linearGradient></defs>
  ${sombra(75, 280, 58)}
  <rect x="10" y="6" width="130" height="266" rx="22" fill="url(#bf-cl)"/>
  <rect x="18" y="14" width="114" height="250" rx="16" fill="url(#bf-tl)"/>
  <rect x="58" y="22" width="34" height="9" rx="4.5" fill="#0d0f12"/>
  <path d="M30 40 L60 40 L30 160 Z" fill="#fff" opacity=".1"/>
</svg>`,
    tv: `
<svg class="il" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="bf-tv" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#2F3D5C"/><stop offset=".6" stop-color="#16203A"/><stop offset="1" stop-color="#0B0F1C"/></linearGradient></defs>
  ${sombra(170, 222, 110, 7)}
  <rect x="6" y="6" width="328" height="190" rx="8" fill="#0d0e10"/>
  <rect x="14" y="14" width="312" height="174" rx="4" fill="url(#bf-tv)"/>
  <path d="M30 26 L120 26 L40 176 L30 176 Z" fill="#fff" opacity=".07"/>
  <path d="M120 196 L106 218 L234 218 L220 196 Z" fill="#2A2C30"/>
</svg>`,
    console: `
<svg class="il" viewBox="0 0 170 290" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="bf-cs" x1="0" x2="1"><stop offset="0" stop-color="#2A2D31"/><stop offset=".5" stop-color="#1A1C1F"/><stop offset="1" stop-color="#0C0D0F"/></linearGradient></defs>
  ${sombra(85, 282, 72)}
  <rect x="18" y="8" width="134" height="270" rx="10" fill="url(#bf-cs)"/>
  <ellipse cx="85" cy="30" rx="44" ry="11" fill="#0a0b0c"/>
  ${[0,1,2,3,4].map(i => `<circle cx="${57 + i * 14}" cy="30" r="3.4" fill="#2f8f4e" opacity=".75"/>`).join('')}
  <rect x="30" y="236" width="40" height="5" rx="2.5" fill="#3a3d42"/>
  <circle cx="132" cy="246" r="6" fill="#d9dbdf" opacity=".85"/>
  <path d="M26 16 L36 16 L36 270 L26 270 Z" fill="#fff" opacity=".06"/>
</svg>`,
    etiqueta: `
<svg class="il" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="bf-et" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#F0604A"/><stop offset="1" stop-color="#C13120"/></linearGradient></defs>
  <path d="M30 8 C8 -2 -4 20 6 40" fill="none" stroke="#E9DFC9" stroke-width="3"/>
  <g transform="rotate(-9 150 100)">
    <path d="M50 30 L280 30 Q292 30 292 42 L292 168 Q292 180 280 180 L50 180 L8 105 Z" fill="#000" opacity=".35" transform="translate(6 10)"/>
    <path d="M50 30 L280 30 Q292 30 292 42 L292 168 Q292 180 280 180 L50 180 L8 105 Z" fill="url(#bf-et)"/>
    <circle cx="46" cy="105" r="11" fill="#1A1817"/>
    <text x="166" y="132" text-anchor="middle" font-family="Anton" font-size="84" fill="#fff">-30%</text>
  </g>
</svg>`,
  });
})();
