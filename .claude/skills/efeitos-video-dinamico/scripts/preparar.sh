#!/usr/bin/env bash
# Cria um projeto Remotion vertical (1080x1920, 30 fps) e normaliza o vídeo para public/video.mp4.
# Uso: bash preparar.sh <video-de-entrada> <pasta-do-projeto> [--sem-instalar]
set -euo pipefail

ENTRADA="${1:?uso: preparar.sh <video> <pasta-do-projeto> [--sem-instalar]}"
PROJ="${2:?uso: preparar.sh <video> <pasta-do-projeto> [--sem-instalar]}"
INSTALAR=1
[[ "${3:-}" == "--sem-instalar" ]] && INSTALAR=0

command -v ffmpeg >/dev/null || { echo "ERRO: ffmpeg não encontrado"; exit 1; }

mkdir -p "$PROJ"/{public/recorte,public/prints,analise,out,src/comum,src/efeitos}

# --- vídeo: 1080x1920, 30 fps constante, áudio AAC 48 kHz ---------------------------------
# scale+crop preenche o 9:16 sem barras; se o original já é 9:16 só redimensiona.
ffmpeg -y -loglevel error -i "$ENTRADA" \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -preset medium -crf 16 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
  "$PROJ/public/video.mp4"

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$PROJ/public/video.mp4")
QUADROS=$(ffprobe -v error -count_packets -select_streams v:0 \
  -show_entries stream=nb_read_packets -of csv=p=0 "$PROJ/public/video.mp4")

# quadros de referência (rosto, enquadramento) a cada ~20% do vídeo
mkdir -p "$PROJ/analise/quadros"
for p in 0.02 0.25 0.5 0.75 0.95; do
  T=$(python3 -c "print(round($DUR*$p,2))")
  ffmpeg -y -loglevel error -ss "$T" -i "$PROJ/public/video.mp4" -frames:v 1 \
    "$PROJ/analise/quadros/ref-${T}s.jpg"
done

# --- projeto Remotion ----------------------------------------------------------------------
if [[ ! -f "$PROJ/package.json" ]]; then
cat > "$PROJ/package.json" <<'JSON'
{
  "name": "projeto-video",
  "private": true,
  "scripts": {
    "studio": "remotion studio",
    "rascunho": "remotion render Principal out/rascunho.mp4 --scale=0.5 --crf=28",
    "final": "remotion render Principal out/final.mp4 --codec=h264 --crf=18 --audio-codec=aac"
  }
}
JSON

cat > "$PROJ/tsconfig.json" <<'JSON'
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src", "analise/*.json"]
}
JSON

cat > "$PROJ/remotion.config.ts" <<'TS'
import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
TS

cat > "$PROJ/src/index.ts" <<'TS'
import {registerRoot} from 'remotion';
import {RemotionRoot} from './Root';

registerRoot(RemotionRoot);
TS

cat > "$PROJ/src/Root.tsx" <<'TSX'
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
TSX

cat > "$PROJ/src/plano.ts" <<'TS'
import bruto from '../analise/plano-efeitos.json';

export type ItemPlano = {
  id: string;
  efeito: string;
  inicio: number;
  fim: number;
  gatilho: string;
  motivo: string;
  textos?: Record<string, string | string[]>;
  params?: Record<string, unknown>;
};

export type Plano = {
  duracao: number;
  rosto?: {x: number; y: number};
  efeitos: ItemPlano[];
};

export const plano = bruto as unknown as Plano;
TS

cat > "$PROJ/src/Principal.tsx" <<'TSX'
import {AbsoluteFill, OffthreadVideo, Sequence, staticFile, useCurrentFrame} from 'remotion';
import {plano} from './plano';
import {EFEITOS} from './efeitos';

const FPS = 30;
const q = (s: number) => Math.round(s * FPS);

export const Principal = () => {
  const frame = useCurrentFrame();
  const ativos = plano.efeitos.filter((e) => EFEITOS[e.efeito]);
  const camera = ativos.find(
    (e) => EFEITOS[e.efeito].envolveVideo && frame >= q(e.inicio) && frame < q(e.fim),
  );
  const base = <OffthreadVideo src={staticFile('video.mp4')} />;
  const Camera = camera ? EFEITOS[camera.efeito].Componente : null;

  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      {Camera && camera ? (
        <Camera item={camera} inicioAbs={q(camera.inicio)}>
          {base}
        </Camera>
      ) : (
        base
      )}
      {ativos
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
TSX

cat > "$PROJ/src/comum/Recorte.tsx" <<'TSX'
import React from 'react';
import {Img, staticFile, useCurrentFrame} from 'remotion';

// Quadro N do recorte = quadro N do vídeo. Dentro de <Sequence> o frame começa em 0,
// por isso o efeito passa o início absoluto. passo=2 dá stop motion a 15 fps.
export const Recorte: React.FC<{inicioAbs: number; passo?: number; style?: React.CSSProperties}> = ({
  inicioAbs,
  passo = 1,
  style,
}) => {
  const f = useCurrentFrame();
  const abs = inicioAbs + Math.floor(f / passo) * passo;
  return (
    <Img
      src={staticFile(`recorte/${String(abs).padStart(5, '0')}.png`)}
      style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', ...style}}
    />
  );
};
TSX

cat > "$PROJ/src/efeitos/index.ts" <<'TS'
import React from 'react';
import type {ItemPlano} from '../plano';

export type PropsEfeito = {item: ItemPlano; inicioAbs: number; children?: React.ReactNode};

// Registre aqui só os efeitos que o plano usa. envolveVideo=true para efeitos de câmera
// (zoom-digital, corte-no-zoom, punch-in), que recebem o vídeo base como children.
export const EFEITOS: Record<string, {Componente: React.FC<PropsEfeito>; envolveVideo?: boolean}> = {};
TS
fi

[[ -f "$PROJ/analise/plano-efeitos.json" ]] || \
  printf '{\n  "duracao": %s,\n  "efeitos": []\n}\n' "$DUR" > "$PROJ/analise/plano-efeitos.json"

if [[ $INSTALAR -eq 1 && ! -d "$PROJ/node_modules/remotion" ]]; then
  V=$(npm view remotion version)
  (cd "$PROJ" && npm install --silent \
    "remotion@$V" "@remotion/cli@$V" "@remotion/media-utils@$V" "@remotion/google-fonts@$V" \
    react@18 react-dom@18 typescript @types/react@18)
fi

echo "Projeto: $PROJ"
echo "Duração: ${DUR}s · Quadros: ${QUADROS} · 1080x1920 · 30 fps"
echo "Quadros de referência: $PROJ/analise/quadros/"
