import React from 'react';
import {AbsoluteFill, Audio, interpolate, staticFile, useCurrentFrame} from 'remotion';
import './fontes';
import {COR, TextoCinetico} from './Texto';
import {Cena, cenas, clamp, FPS} from './tempo';
import {VISUAIS} from './visuais';

const fundoCss = (f: Cena['fundo']) =>
  f === 'claro'
    ? 'radial-gradient(120% 80% at 50% 45%, #FBFBF8 0%, #F1F0EB 70%, #E6E5DF 100%)'
    : 'linear-gradient(180deg, #000 0%, #060606 40%, #1E1E1E 85%, #2A2A2A 100%)';

const CenaView: React.FC<{cena: Cena; t: number}> = ({cena, t}) => {
  const Visual = cena.visual ? VISUAIS[cena.visual] : null;
  return (
    <AbsoluteFill style={{background: fundoCss(cena.fundo)}}>
      {Visual && <Visual t={t} cena={cena} />}
      <TextoCinetico cena={cena} t={t} />
    </AbsoluteFill>
  );
};

export const Principal: React.FC = () => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const i = Math.max(0, cenas.findIndex((c) => t >= c.ini && t < c.fim));
  const cena = cenas[i];
  const anterior = cenas[i - 1];
  // troca de fundo: a cena nova entra numa cortina diagonal (6 quadros); mesmo fundo: corte seco
  const k = anterior && anterior.fundo !== cena.fundo ? interpolate(t, [cena.ini, cena.ini + 6 / FPS], [0, 1], clamp) : 1;
  return (
    <AbsoluteFill style={{background: COR[anterior?.fundo ?? cena.fundo].fundo}}>
      {k < 1 && anterior && <CenaView cena={anterior} t={t} />}
      <AbsoluteFill style={{clipPath: k < 1 ? `polygon(${110 - 140 * k}% 0, 200% 0, 200% 100%, ${140 - 140 * k}% 100%)` : undefined}}>
        <CenaView cena={cena} t={t} />
      </AbsoluteFill>
      <Audio src={staticFile('narracao.wav')} />
      <Audio src={staticFile('trilha.wav')} />
    </AbsoluteFill>
  );
};
