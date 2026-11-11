// lê timeline + cenas e escreve audio/eventos.json para a trilha (mesma regra de tempo do tempo.ts)
import fs from 'node:fs';
const frases = JSON.parse(fs.readFileSync(new URL('../src/timeline.json', import.meta.url)));
const cenas = JSON.parse(fs.readFileSync(new URL('../src/cenas.json', import.meta.url)));
const DUR = frases.at(-1).fim + 0.6;
const out = cenas.map((c, i) => ({...c, ini: i === 0 ? 0 : frases[c.de].ini - 0.12,
  fim: i === cenas.length - 1 ? DUR : frases[cenas[i + 1].de].ini - 0.12}));
fs.writeFileSync(new URL('../audio/cenas-tempo.json', import.meta.url), JSON.stringify({duracao: DUR, cenas: out}, null, 1));
console.log(out.map((c) => `${c.ini.toFixed(2)} ${c.id}`).join('\n'));
