// ilustras.js · objetos desenhados em código (SVG), sem marca nenhuma.
// Uma família só: formas cheias, uma luz vindo da esquerda, creme + âmbar + coral sobre o escuro.
// Uso: <div data-il="cerveja" style="width:..px"></div> (base.js injeta).
(function () {
  const brilho = (x, y1, y2, w = 6, o = .28) =>
    `<path d="M${x} ${y1} L${x} ${y2}" stroke="#fff" stroke-opacity="${o}" stroke-width="${w}" stroke-linecap="round"/>`;
  const sombra = (cx, cy, rx, ry = 9) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#000" opacity=".42"/>`;

  const garrafa = (id, vidro1, vidro2, rotulo, faixa, tampa) => `
<svg class="il" viewBox="0 0 110 330" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="${id}" x1="0" x2="1"><stop offset="0" stop-color="${vidro1}"/><stop offset=".55" stop-color="${vidro2}"/><stop offset="1" stop-color="#1c0f06"/></linearGradient></defs>
  ${sombra(55, 314, 46)}
  <rect x="41" y="8" width="28" height="18" rx="4" fill="${tampa}"/>
  <path d="M44 26 L44 88 C44 114 20 124 20 158 L20 298 Q20 312 34 312 L76 312 Q90 312 90 298 L90 158 C90 124 66 114 66 88 L66 26 Z" fill="url(#${id})"/>
  <rect x="44" y="50" width="22" height="26" fill="${faixa}"/>
  <rect x="20" y="178" width="70" height="88" fill="${rotulo}"/>
  <ellipse cx="55" cy="222" rx="25" ry="19" fill="${faixa}"/>
  <rect x="20" y="178" width="70" height="7" fill="${faixa}"/><rect x="20" y="259" width="70" height="7" fill="${faixa}"/>
  ${brilho(30, 166, 296, 6, .22)}${brilho(49, 32, 84, 3, .3)}
</svg>`;

  const rodas = (a, b, y, r) => [a, b].map(cx => `
    <circle cx="${cx}" cy="${y}" r="${r}" fill="#0f0e0d"/><circle cx="${cx}" cy="${y}" r="${r * .56}" fill="#8f8a82"/><circle cx="${cx}" cy="${y}" r="${r * .2}" fill="#2a2826"/>`).join('');

  window.IL = {
    cigarro: `
<svg class="il" viewBox="0 0 200 270" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-cg" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".26"/></linearGradient></defs>
  ${sombra(100, 256, 82)}
  <g>
    <rect x="50" y="24" width="27" height="90" rx="4" fill="#F4EEE2"/><rect x="50" y="24" width="27" height="32" rx="4" fill="#E0A04A"/>
    <rect x="83" y="8" width="27" height="100" rx="4" fill="#F4EEE2"/><rect x="83" y="8" width="27" height="32" rx="4" fill="#E0A04A"/>
    <rect x="116" y="28" width="27" height="90" rx="4" fill="#F4EEE2"/><rect x="116" y="28" width="27" height="32" rx="4" fill="#E0A04A"/>
  </g>
  <rect x="30" y="82" width="140" height="170" rx="10" fill="#F4EEE2"/>
  <path d="M30 92 a10 10 0 0 1 10 -10 h120 a10 10 0 0 1 10 10 v52 h-140 z" fill="#DC3F2E"/>
  <rect x="30" y="156" width="140" height="8" fill="#DC3F2E"/>
  <rect x="62" y="192" width="76" height="10" rx="5" fill="#1A1817" opacity=".8"/>
  <rect x="76" y="212" width="48" height="7" rx="3.5" fill="#1A1817" opacity=".45"/>
  <rect x="30" y="82" width="140" height="170" rx="10" fill="url(#il-cg)"/>
</svg>`,

    cerveja: garrafa('il-cv', '#9A5A1E', '#6B3A14', '#F4EEE2', '#DC3F2E', '#D9B24C'),
    importada: garrafa('il-im', '#4E7A3A', '#2F5226', '#F4EEE2', '#1F3A5F', '#C9CED6'),

    destilado: `
<svg class="il" viewBox="0 0 150 330" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-ds" x1="0" x2="1"><stop offset="0" stop-color="#E09A3A"/><stop offset=".55" stop-color="#B8691F"/><stop offset="1" stop-color="#6E3A0E"/></linearGradient></defs>
  ${sombra(75, 314, 60)}
  <rect x="55" y="8" width="40" height="36" rx="5" fill="#141211" stroke="#55504A" stroke-width="2"/>
  <rect x="60" y="44" width="30" height="52" fill="#C27A28"/>
  <path d="M60 94 L60 100 C60 118 22 118 22 142 L22 298 Q22 312 36 312 L114 312 Q128 312 128 298 L128 142 C128 118 90 118 90 100 L90 94 Z" fill="url(#il-ds)"/>
  <rect x="34" y="172" width="82" height="104" fill="#141211"/>
  <rect x="40" y="178" width="70" height="92" fill="none" stroke="#F4EEE2" stroke-width="2" opacity=".8"/>
  <rect x="50" y="196" width="50" height="9" rx="2" fill="#F4EEE2"/>
  <rect x="58" y="216" width="34" height="5" rx="2" fill="#F4EEE2" opacity=".7"/>
  <rect x="54" y="236" width="42" height="14" rx="2" fill="#E0A04A"/>
  ${brilho(33, 150, 296, 6, .3)}
</svg>`,

    lata: `
<svg class="il" viewBox="0 0 120 240" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-lt" x1="0" x2="1"><stop offset="0" stop-color="#F0604A"/><stop offset=".45" stop-color="#DC3F2E"/><stop offset="1" stop-color="#8E2114"/></linearGradient>
  <clipPath id="il-ltc"><rect x="12" y="24" width="96" height="192" rx="16"/></clipPath></defs>
  ${sombra(60, 222, 50)}
  <rect x="12" y="24" width="96" height="192" rx="16" fill="url(#il-lt)"/>
  <g clip-path="url(#il-ltc)">
    <path d="M12 128 C40 96 76 156 108 114 L108 146 C76 188 40 128 12 160 Z" fill="#fff" opacity=".94"/>
    <rect x="12" y="24" width="96" height="14" fill="#C9CED6"/><rect x="12" y="204" width="96" height="12" fill="#B4B9C1"/>
  </g>
  <ellipse cx="60" cy="25" rx="43" ry="9" fill="#DADDE2"/><ellipse cx="60" cy="25" rx="33" ry="6" fill="#9DA2AA"/>
  <ellipse cx="68" cy="25" rx="8" ry="3" fill="#5B6068"/>
  ${brilho(26, 46, 196, 6, .3)}
</svg>`,

    vinho: `
<svg class="il" viewBox="0 0 140 260" xmlns="http://www.w3.org/2000/svg">
  ${sombra(70, 244, 46, 7)}
  <path d="M32 62 L108 62 C106 100 96 126 70 128 C44 126 34 100 32 62 Z" fill="#9B1F2E"/>
  <path d="M30 18 L110 18 C114 80 100 130 70 132 C40 130 26 80 30 18 Z" fill="#fff" fill-opacity=".12" stroke="#fff" stroke-opacity=".7" stroke-width="3"/>
  <rect x="67" y="132" width="6" height="96" fill="#fff" opacity=".6"/>
  <ellipse cx="70" cy="232" rx="38" ry="8" fill="#fff" fill-opacity=".18" stroke="#fff" stroke-opacity=".7" stroke-width="3"/>
  ${brilho(44, 30, 96, 5, .35)}
</svg>`,

    carro: `
<svg class="il" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-cr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F1EEE8"/><stop offset="1" stop-color="#A9A49B"/></linearGradient></defs>
  ${sombra(170, 138, 150, 8)}
  <path d="M18 104 L18 88 C18 78 26 72 40 70 L80 63 L112 35 C120 28 130 24 144 24 L214 24 C232 24 246 30 258 42 L282 64 L308 70 C320 73 326 80 326 90 L326 104 C326 110 322 114 316 114 L28 114 C22 114 18 110 18 104 Z" fill="url(#il-cr)"/>
  <path d="M122 41 C126 37 132 35 140 35 L176 35 L176 62 L97 62 Z" fill="#1F252C"/>
  <path d="M186 35 L212 35 C226 35 236 39 246 49 L260 62 L186 62 Z" fill="#1F252C"/>
  <rect x="304" y="78" width="20" height="9" rx="4" fill="#DC3F2E"/><rect x="20" y="80" width="18" height="9" rx="4" fill="#F6D98A"/>
  <rect x="150" y="72" width="16" height="4" rx="2" fill="#6F6A62"/>
  ${rodas(92, 256, 114, 27)}
</svg>`,

    picape: `
<svg class="il" viewBox="0 0 360 150" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-pc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A5E66"/><stop offset="1" stop-color="#2B2E33"/></linearGradient></defs>
  ${sombra(180, 140, 160, 8)}
  <path d="M16 108 L16 84 C16 76 22 71 32 69 L92 64 L116 32 C120 27 126 24 134 24 L188 24 C194 24 198 28 198 34 L198 64 L338 64 C343 64 346 67 346 72 L346 108 C346 113 343 116 338 116 L24 116 C19 116 16 113 16 108 Z" fill="url(#il-pc)"/>
  <path d="M126 36 L186 36 L186 62 L105 62 Z" fill="#12161B"/>
  <rect x="204" y="72" width="136" height="5" fill="#16181B" opacity=".6"/>
  <rect x="18" y="80" width="18" height="9" rx="4" fill="#F6D98A"/><rect x="328" y="76" width="16" height="10" rx="3" fill="#DC3F2E"/>
  ${rodas(84, 280, 116, 29)}
</svg>`,

    aviao: `
<svg class="il" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-av" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4F1EB"/><stop offset="1" stop-color="#B3AEA5"/></linearGradient></defs>
  <path d="M268 62 L304 14 L324 14 L312 62 Z" fill="#DC3F2E"/>
  <path d="M12 82 C40 62 82 56 132 56 L292 56 C312 56 328 62 332 72 C328 84 312 90 292 90 L122 94 C70 94 34 92 12 82 Z" fill="url(#il-av)"/>
  <path d="M34 72 C44 66 54 63 66 63 L66 73 L33 75 Z" fill="#1F252C"/>
  <g fill="#1F252C">${[96, 120, 144, 168, 192, 216, 240].map(x => `<rect x="${x}" y="66" width="12" height="9" rx="3"/>`).join('')}</g>
  <path d="M150 84 L226 136 L252 136 L214 84 Z" fill="#8F8A82"/>
  <rect x="150" y="96" width="44" height="18" rx="9" fill="#5E5A54"/>
  <path d="M286 70 L330 58 L332 66 L296 78 Z" fill="#8F8A82"/>
</svg>`,

    barco: `
<svg class="il" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-bc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4F1EB"/><stop offset="1" stop-color="#B8B3AA"/></linearGradient></defs>
  <rect x="150" y="22" width="64" height="20" rx="4" fill="#CFCAC1"/>
  <path d="M92 78 L112 42 L232 42 L266 78 Z" fill="#E4E0D8"/>
  <path d="M118 50 L226 50 L244 70 L108 70 Z" fill="#1F252C"/>
  <path d="M8 84 L332 76 C324 104 302 122 272 122 L62 122 C40 122 20 108 8 84 Z" fill="url(#il-bc)"/>
  <path d="M20 100 L318 94 L314 102 L26 108 Z" fill="#DC3F2E"/>
  <path d="M6 134 C30 126 54 142 78 134 C102 126 126 142 150 134 C174 126 198 142 222 134 C246 126 270 142 294 134 C310 129 322 131 334 134" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="4" stroke-linecap="round"/>
</svg>`,

    loteria: `
<svg class="il" viewBox="0 0 220 180" xmlns="http://www.w3.org/2000/svg">
  <g transform="rotate(-8 110 90)">
    <rect x="30" y="18" width="160" height="144" rx="8" fill="#000" opacity=".35" transform="translate(6 10)"/>
    <rect x="30" y="18" width="160" height="144" rx="8" fill="#F4EEE2"/>
    <rect x="30" y="18" width="160" height="30" rx="8" fill="#DC3F2E"/><rect x="30" y="38" width="160" height="10" fill="#DC3F2E"/>
    <rect x="44" y="28" width="60" height="9" rx="4" fill="#fff" opacity=".9"/>
    ${[0, 1, 2, 3].map(l => [0, 1, 2, 3, 4, 5].map(c => {
      const m = [[0, 1], [1, 4], [2, 2], [3, 5], [1, 0], [3, 3]].some(([a, b]) => a === l && b === c);
      return `<rect x="${44 + c * 23}" y="${60 + l * 24}" width="17" height="17" rx="3" fill="${m ? '#DC3F2E' : 'none'}" stroke="${m ? '#DC3F2E' : '#B9B1A2'}" stroke-width="2"/>`;
    }).join('')).join('')}
  </g>
</svg>`,

    gota: `
<svg class="il" viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-gt" x1="0" x2="1"><stop offset="0" stop-color="#F0604A"/><stop offset="1" stop-color="#B02A1B"/></linearGradient></defs>
  ${sombra(80, 188, 52, 7)}
  <path d="M80 10 C108 58 140 92 140 126 C140 160 113 184 80 184 C47 184 20 160 20 126 C20 92 52 58 80 10 Z" fill="url(#il-gt)"/>
  <path d="M46 128 C46 148 58 162 76 166" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="7" stroke-linecap="round"/>
</svg>`,

    ampulheta: `
<svg class="il" viewBox="0 0 240 390" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="il-am" x1="0" x2="1"><stop offset="0" stop-color="#C98A3E"/><stop offset="1" stop-color="#7A4A17"/></linearGradient></defs>
  ${sombra(120, 378, 108, 10)}
  <rect x="42" y="34" width="8" height="314" fill="#8A5A22"/><rect x="190" y="34" width="8" height="314" fill="#5E3A12"/>
  <path d="M58 36 L182 36 C182 110 148 150 128 182 L128 200 C148 232 182 272 182 346 L58 346 C58 272 92 232 112 200 L112 182 C92 150 58 110 58 36 Z" fill="#fff" fill-opacity=".1" stroke="#fff" stroke-opacity=".6" stroke-width="3"/>
  <path d="M76 104 L164 104 C156 134 138 156 125 178 L115 178 C102 156 84 134 76 104 Z" fill="#EBC98F"/>
  <rect x="118" y="178" width="4" height="112" fill="#EBC98F"/>
  <path d="M66 346 C70 304 100 290 120 284 C140 290 170 304 174 346 Z" fill="#EBC98F"/>
  <rect x="26" y="10" width="188" height="28" rx="9" fill="url(#il-am)"/>
  <rect x="26" y="344" width="188" height="28" rx="9" fill="url(#il-am)"/>
  ${brilho(74, 52, 96, 5, .35)}${brilho(72, 290, 330, 5, .25)}
</svg>`,
  };
})();
