# Esqueleto Remotion

O `scripts/preparar.sh` cria o projeto com esta estrutura. Se o projeto já existir, só confira.

```
projeto-video/
├── public/
│   ├── video.mp4            # normalizado 1080x1920, 30 fps CFR
│   ├── recorte/00000.png    # RGBA, mesmo número do quadro (só nas janelas ✂)
│   ├── prints/              # opcional, para 01 e 02
│   └── fundo-limpo.png      # opcional, para 15 Vertigem
├── analise/
│   ├── transcricao.json / .txt
│   ├── plano-efeitos.json
│   └── RELATORIO.md
└── src/
    ├── index.ts
    ├── Root.tsx
    ├── Principal.tsx
    ├── plano.ts             # importa analise/plano-efeitos.json
    ├── comum/Recorte.tsx
    └── efeitos/             # um arquivo por efeito, ex.: SaindoDaTela.tsx
```

## Root.tsx

```tsx
import {Composition, staticFile} from 'remotion';
import {getVideoMetadata} from '@remotion/media-utils';
import {Principal} from './Principal';

export const RemotionRoot = () => (
  <Composition
    id="Principal"
    component={Principal}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={30}
    calculateMetadata={async () => {
      const {durationInSeconds} = await getVideoMetadata(staticFile('video.mp4'));
      return {durationInFrames: Math.round(durationInSeconds * 30)};
    }}
  />
);
```

## Principal.tsx

O vídeo base toca o tempo todo e carrega o áudio. Cada efeito é uma `<Sequence>` por cima.
Efeitos de FUNDO desenham o próprio fundo opaco e o recorte por cima, cobrindo o base naquele trecho.
Efeitos de CÂMERA recebem o vídeo como filho em vez de desenhar por cima (ver `envolveVideo`).

```tsx
import {AbsoluteFill, OffthreadVideo, Sequence, staticFile, useCurrentFrame} from 'remotion';
import {plano} from './plano';
import {EFEITOS} from './efeitos';

const FPS = 30;
const q = (s: number) => Math.round(s * FPS);

export const Principal = () => {
  const frame = useCurrentFrame();
  const camera = plano.efeitos.find(
    (e) => EFEITOS[e.efeito].envolveVideo && frame >= q(e.inicio) && frame < q(e.fim),
  );
  const base = <OffthreadVideo src={staticFile('video.mp4')} />;
  const Camera = camera ? EFEITOS[camera.efeito].Componente : null;

  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      {Camera && camera ? (
        <Camera item={camera} inicioAbs={q(camera.inicio)}>{base}</Camera>
      ) : (
        base
      )}
      {plano.efeitos
        .filter((e) => !EFEITOS[e.efeito].envolveVideo)
        .map((e) => {
          const {Componente} = EFEITOS[e.efeito];
          return (
            <Sequence key={e.id} from={q(e.inicio)} durationInFrames={q(e.fim) - q(e.inicio)}>
              <Componente item={e} inicioAbs={q(e.inicio)} />
            </Sequence>
          );
        })}
    </AbsoluteFill>
  );
};
```

O vídeo base só aparece uma vez na árvore, então o áudio nunca duplica. Os componentes
que precisam do vídeo como imagem (Checklist, Letra de vidro, Revelação) usam
`<OffthreadVideo muted startFrom={inicioAbs} />`. **Sempre `muted`** em toda cópia do vídeo.

## comum/Recorte.tsx

Dentro de uma `<Sequence>`, `useCurrentFrame()` começa em 0. O recorte precisa do quadro
**absoluto** do vídeo, por isso todo efeito recebe `inicioAbs`.

```tsx
import {Img, staticFile, useCurrentFrame} from 'remotion';

export const Recorte: React.FC<{inicioAbs: number; passo?: number; style?: React.CSSProperties}> = ({
  inicioAbs, passo = 1, style,
}) => {
  const f = useCurrentFrame();
  const abs = inicioAbs + Math.floor(f / passo) * passo; // passo=2 → stop motion a 15 fps
  const nome = String(abs).padStart(5, '0');
  return (
    <Img
      src={staticFile(`recorte/${nome}.png`)}
      style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', ...style}}
    />
  );
};
```

## efeitos/index.ts

```tsx
import {SaindoDaTela} from './SaindoDaTela';
import {ZoomDigital} from './ZoomDigital';
// ...

export const EFEITOS: Record<string, {Componente: React.FC<any>; envolveVideo?: boolean}> = {
  'saindo-da-tela': {Componente: SaindoDaTela},
  'zoom-digital': {Componente: ZoomDigital, envolveVideo: true},
  'corte-no-zoom': {Componente: CorteNoZoom, envolveVideo: true},
  'revelacao': {Componente: Revelacao},
  // ids: orbita, parede-de-posts, dentro-do-app, saindo-da-tela, zoom-digital,
  // mockup-celular, checklist, mural-manchete, corte-no-zoom, grafico-subindo,
  // revelacao, chroma-key, recorte-papel, rabisco-vivo, vertigem, capa-revista,
  // letra-vidro, palavra-chave, punch-in
};
```

Só crie os componentes dos efeitos que o plano usa.

## Boas práticas

- **Determinismo:** nada de `Math.random()`. Use `random('semente-' + i)` do `remotion`.
- **Fontes:** `@remotion/google-fonts` (Anton, Bebas Neue, Oswald, Playfair Display, Caveat).
  Carregue no topo do componente com `loadFont()`.
- **Animação:** `spring({frame, fps, config: {damping: 12}})` para entradas com mola,
  `interpolate(frame, [a, b], [x, y], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})` para o resto.
- **Saída suave:** todo efeito pesado faz fade/escala de saída nos últimos 4–6 quadros, salvo os "secos".
- **Rosto:** guarde o centro do rosto em `plano.rosto = {x, y}` (px no 1080x1920) e use em zoom e posições.
- **Prévia:** `npx remotion studio` abre o editor no navegador; em sessão sem tela, use
  `npx remotion still Principal out/q.png --frame=N` para conferir quadros.
- **Performance:** recortes em PNG pesam; se o render ficar lento, use `--concurrency=50%`
  e `--scale=0.5` nos rascunhos.
