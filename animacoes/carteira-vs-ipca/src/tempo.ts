import timeline from './timeline.json';
import cenasJson from './cenas.json';

export const FPS = 30;

export type Palavra = {w: string; bloco: number; destaque: boolean; vermelho: boolean; ini: number; fim: number};
export type Frase = {ini: number; fim: number; texto: string; palavras: Palavra[]};
export type Cena = {
  id: string; de: number; ate: number; fundo: 'claro' | 'escuro';
  visual: string | null; texto: 'topo' | 'centro'; semTexto?: number[];
  ini: number; fim: number;
};

export const frases = timeline as Frase[];
export const DURACAO = frases[frases.length - 1].fim + 0.6;

// a cena entra um pouco antes da primeira palavra e vai até a próxima cena
export const cenas: Cena[] = (cenasJson as Omit<Cena, 'ini' | 'fim'>[]).map((c, i, todas) => {
  const ini = i === 0 ? 0 : frases[c.de].ini - 0.12;
  const fim = i === todas.length - 1 ? DURACAO : frases[todas[i + 1].de].ini - 0.12;
  return {...c, ini, fim};
});

/** Início da primeira palavra da frase `f` que contém `trecho`. */
export const tp = (f: number, trecho?: string) => {
  const ps = frases[f].palavras;
  if (!trecho) return ps[0].ini;
  const p = ps.find((x) => x.w.toLowerCase().includes(trecho.toLowerCase()));
  if (!p) throw new Error(`palavra "${trecho}" não está na frase ${f}`);
  return p.ini;
};

export const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
