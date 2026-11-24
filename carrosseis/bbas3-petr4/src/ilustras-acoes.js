// ilustras-acoes.js · banco (prédio de colunas) e barril de petróleo, mesma família do ilustras.js.
(function () {
  const sombra = (cx, cy, rx, ry = 9) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#000" opacity=".42"/>`;
  Object.assign(window.IL, {
    banco: `
<svg class="il" viewBox="0 0 260 240" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="ac-bc" x1="0" x2="1"><stop offset="0" stop-color="#FFE47A"/><stop offset=".6" stop-color="#E9C12E"/><stop offset="1" stop-color="#A98510"/></linearGradient></defs>
  ${sombra(130, 228, 118)}
  <path d="M14 76 L130 12 L246 76 Z" fill="url(#ac-bc)"/>
  <rect x="22" y="76" width="216" height="16" fill="#C9A21C"/>
  ${[44, 88, 132, 176].map(x => `<rect x="${x}" y="98" width="24" height="96" rx="3" fill="#F4EEE2"/><rect x="${x + 16}" y="98" width="8" height="96" fill="#000" opacity=".14"/>`).join('')}
  <rect x="16" y="196" width="228" height="14" fill="#E9C12E"/><rect x="6" y="210" width="248" height="14" fill="#C9A21C"/>
  <circle cx="130" cy="52" r="12" fill="#1F3A8A"/>
</svg>`,
    barril: `
<svg class="il" viewBox="0 0 200 250" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="ac-br" x1="0" x2="1"><stop offset="0" stop-color="#3FA36A"/><stop offset=".55" stop-color="#1E7A48"/><stop offset="1" stop-color="#0C3F24"/></linearGradient></defs>
  ${sombra(100, 238, 86)}
  <path d="M26 30 Q100 18 174 30 Q186 125 174 220 Q100 232 26 220 Q14 125 26 30 Z" fill="url(#ac-br)"/>
  <path d="M20 84 Q100 74 180 84" fill="none" stroke="#0B2E1A" stroke-width="7"/>
  <path d="M20 166 Q100 176 180 166" fill="none" stroke="#0B2E1A" stroke-width="7"/>
  <ellipse cx="100" cy="30" rx="74" ry="12" fill="#2C8A55"/><ellipse cx="100" cy="30" rx="60" ry="7" fill="#145A33"/>
  <path d="M100 96 C114 118 126 132 126 146 C126 162 114 172 100 172 C86 172 74 162 74 146 C74 132 86 118 100 96 Z" fill="#FFD60A"/>
  <path d="M40 46 Q34 125 40 206" fill="none" stroke="#fff" stroke-opacity=".22" stroke-width="7" stroke-linecap="round"/>
</svg>`,
  });
})();
