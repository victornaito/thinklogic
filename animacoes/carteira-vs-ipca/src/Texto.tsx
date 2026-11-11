import React from 'react';
import {interpolate} from 'remotion';
import {SANS, SERIFA} from './fontes';
import {Cena, frases, Palavra} from './tempo';

export const COR = {
  claro: {fundo: '#F6F5F1', texto: '#111111', suave: '#8A8A85'},
  escuro: {fundo: '#050505', texto: '#F2F2F0', suave: '#7C7C78'},
  limao: '#C8FF3D',
  vermelho: '#FF4B4B',
  ipca: '#9C9CF0',
};

type Bloco = {frase: number; palavras: Palavra[]; ini: number; destaque: boolean};

const blocosDaCena = (c: Cena): Bloco[] => {
  const out: Bloco[] = [];
  for (let f = c.de; f <= c.ate; f++) {
    if (c.semTexto?.includes(f)) continue;
    const porBloco = new Map<number, Palavra[]>();
    frases[f].palavras.forEach((p) => porBloco.set(p.bloco, [...(porBloco.get(p.bloco) ?? []), p]));
    porBloco.forEach((ps) => out.push({frase: f, palavras: ps, ini: ps[0].ini, destaque: ps.some((p) => p.destaque)}));
  }
  return out;
};

const tamanhoDestaque = (w: string) => (w.length > 12 ? 104 : w.length > 9 ? 124 : 152);

const PalavraAnimada: React.FC<{p: Palavra; t: number; tema: 'claro' | 'escuro'; pequeno?: boolean}> = ({p, t, tema, pequeno}) => {
  const k = interpolate(t, [p.ini - 0.06, p.ini + 0.14], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const cor = p.vermelho ? COR.vermelho : COR[tema].texto;
  const estilo: React.CSSProperties = p.destaque
    ? {fontFamily: SERIFA, fontStyle: 'italic', fontSize: tamanhoDestaque(p.w) * (pequeno ? 0.55 : 1), letterSpacing: '-0.01em', lineHeight: 1.0}
    : {fontFamily: SANS, fontWeight: 500, fontSize: pequeno ? 34 : 46, letterSpacing: '-0.01em', lineHeight: 1.1};
  return (
    <span
      style={{
        ...estilo,
        color: cor,
        display: 'inline-block',
        opacity: k,
        transform: `translateY(${(1 - k) * 18}px)`,
        filter: `blur(${(1 - k) * 8}px)`,
        whiteSpace: 'pre',
      }}
    >
      {p.w}
    </span>
  );
};

const Linha: React.FC<{b: Bloco; t: number; tema: 'claro' | 'escuro'; pequeno?: boolean}> = ({b, t, tema, pequeno}) => (
  <div
    style={{
      display: 'flex', flexWrap: 'wrap', justifyContent: 'center', alignItems: 'baseline',
      columnGap: pequeno ? 10 : 16, rowGap: 4, maxWidth: 900,
    }}
  >
    {b.palavras.map((p, i) => <PalavraAnimada key={i} p={p} t={t} tema={tema} pequeno={pequeno} />)}
  </div>
);

export const TextoCinetico: React.FC<{cena: Cena; t: number; y?: number}> = ({cena, t, y}) => {
  const blocos = blocosDaCena(cena);
  let i = -1;
  blocos.forEach((b, k) => {
    if (b.ini - 0.06 <= t) i = k;
  });
  if (i < 0) return null;
  const atual = blocos[i];
  const ant = blocos[i - 1];
  // o bloco pequeno de antes fica empilhado em cima do destaque (como "This is / Ryan Reynolds")
  const empilha = ant && ant.frase === atual.frase && !ant.destaque && atual.destaque;
  const centroY = y ?? (cena.texto === 'topo' ? 470 : 960);
  return (
    <div
      style={{
        position: 'absolute', left: 0, right: 0, top: centroY, transform: 'translateY(-50%)',
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6,
      }}
    >
      {empilha && (
        <div style={{opacity: 0.75, marginBottom: -6}}>
          <Linha b={ant} t={t} tema={cena.fundo} pequeno />
        </div>
      )}
      <Linha b={atual} t={t} tema={cena.fundo} />
    </div>
  );
};
