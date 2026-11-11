# Animação · carteira diversificada × minha carteira × IPCA

Reel 1080x1920, 30 fps, 1min50. Tipografia cinética no estilo da referência (palavra por palavra,
fundo claro/escuro alternando, serifa itálica nos destaques, verde-limão de acento), narração do Victor.

- `out/carteira-vs-ipca.mp4`: vídeo final.
- `public/narracao.wav`: gravação editada (erros e repetições cortados, pausas encurtadas).
- `audio/trechos.json`: trechos da narração editada com tempo; `trechos-gravacao-original.json` é a gravação bruta.

## Refazer

```bash
npm install                                   # remotion 4.0.539
python3 scripts/editar_narracao.py <gravacao.m4a> audio/trechos-gravacao-original.json public/narracao.wav audio/trechos.json
python3 scripts/timeline.py                   # tempo de cada palavra -> src/timeline.json
node scripts/exportar_eventos.mjs             # tempo das cenas -> audio/cenas-tempo.json
python3 scripts/trilha.py                     # música + efeitos -> public/trilha.wav
npx remotion render Principal out/carteira-vs-ipca.mp4 --codec=h264 --crf=18 --audio-codec=aac
```

Textos na tela: `scripts/timeline.py` (lista EXIBIR). Cenas e visuais: `src/cenas.json` e `src/visuais.tsx`.
