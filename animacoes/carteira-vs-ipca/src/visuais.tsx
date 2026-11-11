import React from 'react';
import {Easing, Img, interpolate, spring, staticFile} from 'remotion';
import curvas from './curvas-print.json';
import {SANS, SERIFA} from './fontes';
import {COR} from './Texto';
import {Cena, clamp, FPS, frases, tp} from './tempo';

type P = {t: number; cena: Cena};

const mola = (t: number, ini: number, damping = 14) =>
  spring({frame: Math.max(0, (t - ini) * FPS), fps: FPS, config: {damping}});
const lin = (t: number, ini: number, dur: number, ease = Easing.out(Easing.cubic)) =>
  interpolate(t, [ini, ini + dur], [0, 1], {...clamp, easing: ease});

const Rotulo: React.FC<{children: React.ReactNode; cor?: string; size?: number; style?: React.CSSProperties}> = ({children, cor, size = 30, style}) => (
  <div style={{fontFamily: SANS, fontWeight: 600, fontSize: size, letterSpacing: '0.06em', textTransform: 'uppercase', color: cor, ...style}}>{children}</div>
);

const Serifa: React.FC<{children: React.ReactNode; size: number; cor?: string; style?: React.CSSProperties}> = ({children, size, cor, style}) => (
  <div style={{fontFamily: SERIFA, fontStyle: 'italic', fontSize: size, lineHeight: 1, color: cor, ...style}}>{children}</div>
);

/** ▶▶ verde-limão, como o "fast forward" da referência */
const Avanco: React.FC<{size?: number}> = ({size = 120}) => (
  <svg width={size * 1.6} height={size} viewBox="0 0 160 100">
    <polygon points="0,0 80,50 0,100" fill={COR.limao} />
    <polygon points="72,0 152,50 72,100" fill={COR.limao} />
  </svg>
);

// ---------------------------------------------------------------- 1 · print da carteira
const Print: React.FC<P> = ({t}) => {
  const k = mola(t, 0.05, 16);
  const tv = tp(0, 'vermelho');
  const circ = lin(t, tv - 0.05, 0.45);
  const W = 920; const s = W / 440;
  return (
    <div style={{position: 'absolute', left: 80, top: 760, width: W, transform: `scale(${0.92 + 0.08 * k + t * 0.012}) rotate(${-2 + 2 * k}deg)`, opacity: k}}>
      <Img src={staticFile('print-carteira.png')} style={{width: W, borderRadius: 30, boxShadow: '0 40px 90px rgba(0,0,0,.7), 0 0 0 2px rgba(255,255,255,.08)'}} />
      <svg width={W} height={362 * s} style={{position: 'absolute', left: 0, top: 0}}>
        <ellipse cx={118 * s} cy={290 * s} rx={42 * s} ry={22 * s} fill="none" stroke={COR.vermelho} strokeWidth={9}
          strokeDasharray={1000} strokeDashoffset={1000 * (1 - circ)} transform={`rotate(-8 ${118 * s} ${290 * s})`} strokeLinecap="round" />
      </svg>
    </div>
  );
};

// ---------------------------------------------------------------- 3 · interrogação gigante
const Interrogacao: React.FC<P> = ({t, cena}) => {
  const k = lin(t, cena.ini, 0.6);
  return (
    <Serifa size={1100} style={{position: 'absolute', left: 0, right: 0, top: 380, textAlign: 'center', WebkitTextStroke: '3px rgba(255,255,255,.14)', color: 'transparent', opacity: k, transform: `rotate(${-6 + (t - cena.ini) * 1.5}deg) scale(${0.9 + 0.1 * k})`}}>?</Serifa>
  );
};

// ---------------------------------------------------------------- 5 · donut da carteira
const FATIAS = [
  {nome: 'Renda fixa', pct: 0.45, cor: '#F2F2F0', palavra: 'renda'},
  {nome: 'Ações', pct: 0.25, cor: COR.limao, palavra: 'ações'},
  {nome: 'Fundos imobiliários', pct: 0.17, cor: '#8C8C88', palavra: 'fundos'},
  {nome: 'Exterior', pct: 0.13, cor: '#4A4A47', palavra: 'exterior'},
];
const Donut: React.FC<P> = ({t}) => {
  const R = 250; const C = 2 * Math.PI * R; const cx = 540; const cy = 1130;
  let acc = 0;
  const t10 = tp(7, '10%');
  const kc = mola(t, t10, 12);
  return (
    <>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="rgba(255,255,255,.06)" strokeWidth={90} />
        {FATIAS.map((f) => {
          const ini = tp(6, f.palavra);
          const k = lin(t, ini - 0.05, 0.5);
          const off = acc; acc += f.pct;
          return (
            <circle key={f.nome} cx={cx} cy={cy} r={R} fill="none" stroke={f.cor} strokeWidth={90}
              strokeDasharray={`${C * f.pct * k} ${C}`} strokeDashoffset={-C * off} transform={`rotate(-90 ${cx} ${cy})`} />
          );
        })}
      </svg>
      {FATIAS.map((f, i) => {
        const k = lin(t, tp(6, f.palavra), 0.3);
        return (
          <div key={f.nome} style={{position: 'absolute', left: 120 + (i % 2) * 450, top: 1460 + Math.floor(i / 2) * 70, display: 'flex', alignItems: 'center', gap: 16, opacity: k}}>
            <div style={{width: 26, height: 26, borderRadius: 13, background: f.cor}} />
            <Rotulo cor="#D8D8D4" size={28}>{f.nome}</Rotulo>
          </div>
        );
      })}
      <div style={{position: 'absolute', left: cx - 200, width: 400, top: cy - 75, textAlign: 'center', opacity: kc, transform: `scale(${0.6 + 0.4 * kc})`}}>
        <Serifa size={130} cor="#F2F2F0">~10%</Serifa>
        <Rotulo cor={COR.escuro.suave} size={26} style={{marginTop: 8}}>ao ano</Rotulo>
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 6 · R$ 10.000 → R$ 10.970
const brl = (v: number) => 'R$ ' + Math.round(v).toLocaleString('pt-BR');
const Contador1: React.FC<P> = ({t}) => {
  const ini = tp(8, 'viram');
  const k = lin(t, ini, 1.0, Easing.inOut(Easing.cubic));
  const ent = mola(t, tp(8), 14);
  const pouco = lin(t, tp(9, 'pouco'), 0.4);
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 860, textAlign: 'center', opacity: ent, transform: `scale(${(0.85 + 0.15 * ent) * (1 - 0.12 * pouco)})`}}>
      <Serifa size={190} cor="#111">{brl(10000 + 970 * k)}</Serifa>
      <div style={{marginTop: 30, opacity: k, display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 14}}>
        <div style={{background: '#111', color: COR.limao, fontFamily: SANS, fontWeight: 700, fontSize: 40, padding: '10px 22px', borderRadius: 40}}>+ R$ 970</div>
        <Rotulo cor={COR.claro.suave} size={30}>em 1 ano</Rotulo>
      </div>
    </div>
  );
};

// ---------------------------------------------------------------- 7 · a queda (curva do print, vetorial)
const curvaPath = (pts: number[][], x0: number, x1: number, sx: number, sy: number, ox: number, oy: number, y0 = 273) =>
  pts.filter(([x]) => x >= x0 && x <= x1).map(([x, y], i) => `${i ? 'L' : 'M'}${(ox + (x - x0) * sx).toFixed(1)},${(oy + (y - y0) * sy).toFixed(1)}`).join(' ');

const PrintQueda: React.FC<P> = ({t, cena}) => {
  const k = lin(t, cena.ini + 0.1, 1.6, Easing.inOut(Easing.cubic));
  const d = curvaPath(curvas.port, 60, 215, 6.2, 7.5, 80, 1050);
  const tm = tp(11, 'minha');
  const kd = mola(t, tm, 12);
  return (
    <>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <line x1={60} x2={1020} y1={1050} y2={1050} stroke="rgba(255,255,255,.25)" strokeWidth={3} strokeDasharray="10 12" />
        <text x={70} y={1030} fill={COR.escuro.suave} fontFamily={SANS} fontSize={26} fontWeight={600} letterSpacing="2">ZERO</text>
        <rect x={60} y={1050} width={960} height={260} fill="rgba(255,75,75,.08)" opacity={k} />
        <path d={d} fill="none" stroke={COR.vermelho} strokeWidth={8} strokeLinejoin="round" strokeLinecap="round"
          strokeDasharray={4000} strokeDashoffset={4000 * (1 - k)} style={{filter: 'drop-shadow(0 0 14px rgba(255,75,75,.6))'}} />
        <circle cx={80 + (104 - 60) * 6.2} cy={1050 + (298 - 273) * 7.5} r={18 * kd} fill={COR.vermelho} />
      </svg>
      <div style={{position: 'absolute', left: 80 + (104 - 60) * 6.2 - 120, top: 1050 + (298 - 273) * 7.5 + 70, width: 240, textAlign: 'center', opacity: kd}}>
        <Rotulo cor={COR.vermelho} size={30}>Set/24</Rotulo>
        <Serifa size={64} cor="#F2F2F0" style={{marginTop: 6}}>a minha</Serifa>
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 8 · ▶▶ dois anos + contador 23,3%
const Avanco233: React.FC<P> = ({t}) => {
  const ka = mola(t, tp(12), 12);
  const sai = lin(t, tp(13), 0.3);
  const t20 = tp(12, '20%');
  const k20 = lin(t, t20, 0.3);
  const ini = frases[14].ini - 0.05; const fim = frases[15].fim;
  const kc = lin(t, ini, fim - ini, Easing.out(Easing.quad));
  const ent = mola(t, ini, 12);
  const v = (23.3 * kc).toFixed(1).replace('.', ',');
  return (
    <>
      <div style={{position: 'absolute', left: 0, right: 0, top: 820, display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: ka * (1 - sai), transform: `translateX(${(1 - ka) * -200}px)`}}>
        <Avanco size={150} />
        <div style={{marginTop: 40, opacity: k20, textAlign: 'center'}}>
          <Rotulo cor={COR.claro.suave} size={30}>esperado em 2 anos</Rotulo>
          <Serifa size={170} cor="#111" style={{marginTop: 10}}>~20%</Serifa>
        </div>
      </div>
      {t >= ini && (
        <div style={{position: 'absolute', left: 0, right: 0, top: 700, textAlign: 'center', transform: `scale(${0.7 + 0.3 * ent})`, opacity: ent}}>
          <Rotulo cor={COR.claro.suave} size={32}>a minha carteira</Rotulo>
          <Serifa size={330} cor="#111" style={{marginTop: 20}}>{v}%</Serifa>
          <div style={{margin: '10px auto 0', height: 16, width: 620 * kc, background: COR.limao, borderRadius: 8}} />
        </div>
      )}
    </>
  );
};

// ---------------------------------------------------------------- 9 · esperado × minha
const Barra: React.FC<{x: number; v: number; max: number; k: number; cor: string; rotulo: string; valor: string; corTexto?: string}> = ({x, v, max, k, cor, rotulo, valor, corTexto = '#F2F2F0'}) => {
  const H = 620 * (v / max) * k;
  return (
    <>
      <div style={{position: 'absolute', left: x, width: 260, top: 1560 - H, height: H, background: cor, borderRadius: '18px 18px 0 0'}} />
      <div style={{position: 'absolute', left: x - 40, width: 340, top: 1560 - H - 130, textAlign: 'center', opacity: k}}>
        <Serifa size={110} cor={corTexto}>{valor}</Serifa>
      </div>
      <Rotulo cor={COR.escuro.suave} size={28} style={{position: 'absolute', left: x - 40, width: 340, top: 1590, textAlign: 'center'}}>{rotulo}</Rotulo>
    </>
  );
};
const Barras2: React.FC<P> = ({t}) => {
  const k1 = mola(t, tp(16), 18);
  const k2 = mola(t, tp(16, 'esperado') + 0.2, 13);
  const kp = lin(t, tp(18, 'paciência'), 0.5);
  return (
    <>
      <Barra x={200} v={20} max={23.3} k={k1} cor="#5A5A56" rotulo="esperado" valor="20%" />
      <Barra x={620} v={23.3} max={23.3} k={k2} cor={COR.limao} rotulo="minha carteira" valor="23,3%" />
      <div style={{position: 'absolute', left: 0, right: 0, top: 1680, textAlign: 'center', opacity: kp}}>
        <Rotulo cor="#D8D8D4" size={30}>carteira montada + tempo</Rotulo>
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 10 · a régua (IPCA) + mercado, gasolina, aluguel
const ICONES: Record<string, string> = {
  mercado: 'M10 20 h18 l14 62 h60 l14 -46 h-82 M48 96 a7 7 0 1 0 0.1 0 M92 96 a7 7 0 1 0 0.1 0',
  gasolina: 'M22 100 V22 a8 8 0 0 1 8 -8 h40 a8 8 0 0 1 8 8 V100 M14 100 h72 M32 30 h36 v24 h-36 z M78 40 l14 12 v34 a6 6 0 0 1 -12 0 v-16 h-2',
  aluguel: 'M12 56 L60 16 L108 56 M24 46 V104 h72 V46 M48 104 V74 h24 V104',
};
const Icone: React.FC<{nome: string; k: number; x: number}> = ({nome, k, x}) => (
  <div style={{position: 'absolute', left: x, top: 1330, width: 240, textAlign: 'center', opacity: Math.min(1, k * 2), transform: `translateY(${(1 - k) * 30}px)`}}>
    <svg width={150} height={130} viewBox="0 0 120 112">
      <path d={ICONES[nome]} fill="none" stroke="#111" strokeWidth={5} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={600} strokeDashoffset={600 * (1 - k)} />
    </svg>
    <Rotulo cor={COR.claro.suave} size={26} style={{marginTop: 10}}>{nome}</Rotulo>
  </div>
);
const Regua: React.FC<P> = ({t}) => {
  const kr = lin(t, tp(20, 'régua') - 0.1, 0.9);
  const ki = mola(t, tp(21, 'IPCA'), 12);
  const kicones = (p: string) => lin(t, tp(22, p) - 0.05, 0.6);
  const subir = lin(t, tp(22), 0.5);
  const y = 980 - 200 * subir;
  return (
    <>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, opacity: t < tp(20, 'régua') - 0.1 ? 0 : 1}}>
        <g transform={`translate(0 ${y - 980})`}>
          <rect x={110} y={930} width={860 * kr} height={110} rx={10} fill={COR.limao} />
          {Array.from({length: 41}).map((_, i) => {
            const x = 130 + i * 20.5;
            if (x > 110 + 860 * kr - 10) return null;
            const h = i % 10 === 0 ? 56 : i % 5 === 0 ? 40 : 24;
            return <line key={i} x1={x} x2={x} y1={930} y2={930 + h} stroke="#111" strokeWidth={4} />;
          })}
        </g>
      </svg>
      <div style={{position: 'absolute', left: 0, right: 0, top: y + 90, textAlign: 'center', opacity: ki, transform: `scale(${0.7 + 0.3 * ki})`}}>
        <Serifa size={160} cor="#111">IPCA</Serifa>
        <Rotulo cor={COR.claro.suave} size={26} style={{marginTop: 4, opacity: subir}}>a inflação oficial</Rotulo>
      </div>
      <Icone nome="mercado" k={kicones('mercado')} x={60} />
      <Icone nome="gasolina" k={kicones('gasolina')} x={420} />
      <Icone nome="aluguel" k={kicones('aluguel')} x={780} />
    </>
  );
};

// ---------------------------------------------------------------- 11 · IPCA × minha carteira (curvas do print)
const Linhas: React.FC<P> = ({t}) => {
  const ini = tp(23);
  const k = lin(t, ini, 2.6, Easing.inOut(Easing.cubic));
  const sx = 2.55; const sy = 4.6; const ox = 40; const oy = 1500;
  const port = curvaPath(curvas.port, 95, 429, sx, sy, ox, oy);
  const ip = curvas.ipca.filter(([x]) => x >= 102);
  const ipca = curvaPath(ip, 95, 429, sx, sy, ox, oy);
  const xFim = ox + (429 - 95) * sx;
  const yPort = oy + (143 - 273) * sy; const yIpca = oy + (215 - 273) * sy;
  const kI = lin(t, tp(23, '12,6%'), 0.4);
  const kM = lin(t, tp(24, '23,3'), 0.4);
  const kD = mola(t, tp(25, 'dobro'), 11);
  return (
    <>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <defs>
          <clipPath id="revela"><rect x={0} y={0} width={ox + (xFim - ox) * k + 4} height={1920} /></clipPath>
        </defs>
        <line x1={ox} x2={xFim} y1={oy} y2={oy} stroke="rgba(255,255,255,.18)" strokeWidth={3} />
        <g clipPath="url(#revela)">
          <path d={ipca} fill="none" stroke={COR.ipca} strokeWidth={6} strokeDasharray="14 12" />
          <path d={port} fill="none" stroke="#F2F2F0" strokeWidth={6} strokeLinejoin="round" />
        </g>
        <circle cx={xFim} cy={yPort} r={14 * kM} fill={COR.limao} />
        <circle cx={xFim} cy={yIpca} r={14 * kI} fill={COR.ipca} />
        <path d={`M${xFim + 40},${yPort} h20 V${yIpca} h-20`} fill="none" stroke={COR.limao} strokeWidth={5} opacity={kD}
          strokeDasharray={800} strokeDashoffset={800 * (1 - kD)} />
      </svg>
      <div style={{position: 'absolute', left: 560, top: yIpca + 30, opacity: kI}}>
        <Rotulo cor={COR.ipca} size={28}>IPCA</Rotulo>
        <Serifa size={88} cor={COR.ipca}>+12,6%</Serifa>
      </div>
      <div style={{position: 'absolute', left: 520, top: yPort - 200, opacity: kM}}>
        <Rotulo cor={COR.limao} size={28}>minha carteira</Rotulo>
        <Serifa size={88} cor="#F2F2F0">+23,3%</Serifa>
      </div>
      <div style={{position: 'absolute', left: 60, top: 1640, opacity: kD, transform: `scale(${0.7 + 0.3 * kD})`, transformOrigin: 'left center'}}>
        <span style={{background: COR.limao, color: '#111', fontFamily: SANS, fontWeight: 800, fontSize: 46, padding: '12px 26px', borderRadius: 40}}>1,85× a inflação</span>
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 13 · 1, 2, 5, 10 anos
const ANOS = [
  {a: '1 ano', v: 9.7, rs: 'R$ 11 mil', ipca: 4.5},
  {a: '2 anos', v: 20.4, rs: 'R$ 12 mil', ipca: 9.2},
  {a: '5 anos', v: 59.0, rs: 'R$ 16 mil', ipca: 24.6},
  {a: '10 anos', v: 153.0, rs: 'R$ 25 mil', ipca: 55.3},
];
const BarrasAnos: React.FC<P> = ({t, cena}) => {
  const base = 1560; const H = 760; const max = 153;
  const quando = [cena.ini + 0.1, cena.ini + 0.3, tp(27, '5'), tp(29, '10')];
  const quandoRs = [cena.ini + 0.2, cena.ini + 0.4, tp(28, '16'), tp(31, '25')];
  const kIpca = lin(t, tp(32), 1.2, Easing.inOut(Easing.cubic));
  const kFF = lin(t, tp(29), 0.15) * (1 - lin(t, tp(29) + 0.9, 0.3));
  const pts = ANOS.map((d, i) => [130 + i * 230 + 90, base - H * (d.ipca / max)]);
  return (
    <>
      {ANOS.map((d, i) => {
        const k = mola(t, quando[i], 15);
        const h = H * (d.v / max) * k;
        const kr = lin(t, quandoRs[i], 0.3);
        const x = 130 + i * 230;
        return (
          <React.Fragment key={d.a}>
            <div style={{position: 'absolute', left: x, width: 180, top: base - h, height: h, background: i === 3 ? COR.limao : '#E8E8E4', borderRadius: '14px 14px 0 0'}} />
            <div style={{position: 'absolute', left: x - 30, width: 240, top: base - h - 80, textAlign: 'center', opacity: k}}>
              <Serifa size={64} cor="#F2F2F0">+{Math.round(d.v)}%</Serifa>
            </div>
            <Rotulo cor="#D8D8D4" size={26} style={{position: 'absolute', left: x - 30, width: 240, top: base + 22, textAlign: 'center', opacity: k}}>{d.a}</Rotulo>
            <Rotulo cor={COR.limao} size={24} style={{position: 'absolute', left: x - 30, width: 240, top: base + 64, textAlign: 'center', opacity: kr, letterSpacing: '0.02em'}}>{d.rs}</Rotulo>
          </React.Fragment>
        );
      })}
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <defs><clipPath id="ipca-anos"><rect x={0} y={0} width={100 + 900 * kIpca} height={1920} /></clipPath></defs>
        <polyline points={pts.map((p) => p.join(',')).join(' ')} fill="none" stroke={COR.ipca} strokeWidth={6} strokeDasharray="14 12" clipPath="url(#ipca-anos)" />
        {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={10 * kIpca} fill={COR.ipca} />)}
      </svg>
      <div style={{position: 'absolute', left: 120, top: 1720, opacity: kIpca, display: 'flex', alignItems: 'center', gap: 14}}>
        <div style={{width: 50, borderTop: `5px dashed ${COR.ipca}`}} />
        <Rotulo cor={COR.ipca} size={26}>inflação no mesmo tempo: +55%</Rotulo>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 860, display: 'flex', justifyContent: 'center', opacity: kFF, transform: `scale(${1 + kFF * 0.15})`}}>
        <Avanco size={110} />
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 14 · juros sobre juros (curva exponencial)
const CurvaExp: React.FC<P> = ({t, cena}) => {
  const x0 = 110; const x1 = 980; const y0 = 1560; const H = 760;
  const ponto = (a: number) => [x0 + (x1 - x0) * (a / 10), y0 - H * ((Math.pow(1.097, a) - 1) / 1.53)];
  const ipcaP = (a: number) => [x0 + (x1 - x0) * (a / 10), y0 - H * ((Math.pow(1.045, a) - 1) / 1.53)];
  const kIpca = lin(t, cena.ini + 0.1, 1.0);
  // devagar nos primeiros anos, acelera no "final"
  const tLento = tp(33, 'primeiros'); const tFinal = tp(34, 'final');
  const prog = t < tFinal ? 0.45 * lin(t, tLento, tFinal - tLento, Easing.linear) : 0.45 + 0.55 * lin(t, tFinal, 1.4, Easing.in(Easing.quad));
  const aMax = 10 * prog;
  const pts: string[] = [];
  for (let a = 0; a <= aMax + 1e-6; a += 0.1) pts.push(ponto(a).join(','));
  const ip: string[] = [];
  for (let a = 0; a <= 10 * kIpca + 1e-6; a += 0.1) ip.push(ipcaP(a).join(','));
  const [px, py] = ponto(aMax);
  const kJ = lin(t, tp(35, 'juros'), 0.3);
  const brilho = 0.5 + 0.5 * Math.sin((t - tFinal) * 8);
  return (
    <>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <line x1={x0} x2={x1} y1={y0} y2={y0} stroke="rgba(0,0,0,.2)" strokeWidth={3} />
        {[0, 2, 4, 6, 8, 10].map((a) => (
          <text key={a} x={x0 + (x1 - x0) * (a / 10)} y={y0 + 50} textAnchor="middle" fontFamily={SANS} fontSize={26} fontWeight={600} fill={COR.claro.suave}>{a === 0 ? 'hoje' : `${a}a`}</text>
        ))}
        {ip.length > 1 && <polyline points={ip.join(' ')} fill="none" stroke={COR.ipca} strokeWidth={6} strokeDasharray="14 12" />}
        {pts.length > 1 && (
          <>
            <polygon points={`${x0},${y0} ${pts.join(' ')} ${px},${y0}`} fill="rgba(200,255,61,.25)" />
            <polyline points={pts.join(' ')} fill="none" stroke="#111" strokeWidth={9} strokeLinejoin="round" strokeLinecap="round" />
            <circle cx={px} cy={py} r={18 + (t > tFinal ? 10 * brilho * kJ : 0)} fill={COR.limao} stroke="#111" strokeWidth={5} />
          </>
        )}
      </svg>
      <div style={{position: 'absolute', left: 120, top: 1690, display: 'flex', gap: 40, alignItems: 'center', opacity: kIpca}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 12}}><div style={{width: 46, borderTop: `5px dashed ${COR.ipca}`}} /><Rotulo cor={COR.claro.suave} size={24}>inflação</Rotulo></div>
        <div style={{display: 'flex', alignItems: 'center', gap: 12}}><div style={{width: 46, height: 8, background: '#111', borderRadius: 4}} /><Rotulo cor={COR.claro.suave} size={24}>carteira</Rotulo></div>
      </div>
    </>
  );
};

// ---------------------------------------------------------------- 15 · holofote
const Holofote: React.FC<P> = ({t, cena}) => {
  const liga = lin(t, cena.ini, 0.25);
  const tl = tp(39, 'larguei');
  const pisca = t > tl && t < tl + 0.5 ? (Math.floor((t - tl) * 18) % 2 === 0 ? 0.25 : 1) : 1;
  const vermelho = lin(t, tl, 0.3);
  const cor = `rgba(255,${Math.round(255 - 140 * vermelho)},${Math.round(255 - 140 * vermelho)},`;
  const a = liga * pisca;
  return (
    <div style={{position: 'absolute', inset: 0, opacity: a}}>
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 1920, background: `linear-gradient(180deg, ${cor}.42) 0%, ${cor}.10) 70%, ${cor}0) 100%)`, clipPath: 'polygon(46% 0, 54% 0, 92% 100%, 8% 100%)', filter: 'blur(14px)'}} />
      <div style={{position: 'absolute', left: 390, top: 30, width: 300, height: 70, borderRadius: '50%', background: `radial-gradient(${cor}1), ${cor}0) 70%)`}} />
      <div style={{position: 'absolute', left: 90, top: 1560, width: 900, height: 220, borderRadius: '50%', background: `radial-gradient(${cor}.35), ${cor}0) 70%)`}} />
    </div>
  );
};

// ---------------------------------------------------------------- 18 · CTA: botão LIBERDADE com cursor
const Cta: React.FC<P> = ({t, cena}) => {
  const tb = tp(43, 'LIBERDADE');
  const kComenta = lin(t, tp(43) - 0.05, 0.25);
  const kb = mola(t, tb - 0.05, 11);
  const tClique = tb + 0.75;
  const cursor = lin(t, tb + 0.15, 0.55, Easing.out(Easing.cubic));
  const aperta = t > tClique && t < tClique + 0.18 ? 0.93 : 1;
  const onda = lin(t, tClique, 0.6);
  const kResto = lin(t, tp(43, 'mando') - 0.05, 0.3);
  const kTabela = mola(t, tp(43, 'tabela'), 14);
  const kAviso = lin(t, cena.fim - 3.2, 0.4);
  return (
    <>
      <div style={{position: 'absolute', left: 0, right: 0, top: 560, textAlign: 'center', opacity: kComenta}}>
        <Serifa size={110} cor="#111">Comenta</Serifa>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 740, display: 'flex', justifyContent: 'center'}}>
        <div style={{position: 'relative', transform: `scale(${kb * aperta})`}}>
          <div style={{position: 'absolute', inset: -30 * onda, borderRadius: 999, border: `4px solid ${COR.limao}`, opacity: 1 - onda}} />
          <div style={{background: COR.limao, color: '#111', fontFamily: SANS, fontWeight: 800, fontSize: 92, letterSpacing: '0.02em', padding: '26px 70px', borderRadius: 999, boxShadow: '0 20px 50px rgba(0,0,0,.18)'}}>LIBERDADE</div>
        </div>
      </div>
      <svg width={70} height={90} viewBox="0 0 24 30" style={{position: 'absolute', left: 900 - 260 * cursor, top: 1150 - 240 * cursor, opacity: cursor, transform: `scale(${aperta})`}}>
        <path d="M2 2 L2 24 L8 18 L12 28 L16 26 L12 16 L20 16 Z" fill="#111" stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
      </svg>
      <div style={{position: 'absolute', left: 0, right: 0, top: 1000, textAlign: 'center', opacity: kResto}}>
        <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 44, color: '#111'}}>que eu te mando a tabela completa</div>
      </div>
      <div style={{position: 'absolute', left: 190, width: 700, top: 1110, background: '#111', borderRadius: 28, padding: '28px 40px', opacity: kTabela, transform: `translateY(${(1 - kTabela) * 60}px)`}}>
        {ANOS.map((d) => (
          <div key={d.a} style={{display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', padding: '10px 0', borderBottom: '1px solid rgba(255,255,255,.12)'}}>
            <Rotulo cor="#D8D8D4" size={28}>{d.a}</Rotulo>
            <Serifa size={56} cor={COR.limao}>+{Math.round(d.v)}%</Serifa>
          </div>
        ))}
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 1545, textAlign: 'center', opacity: kTabela}}>
        <Rotulo cor="#111" size={30} style={{letterSpacing: '0.02em', textTransform: 'none'}}>@victornaito.financas</Rotulo>
      </div>
      <div style={{position: 'absolute', left: 120, right: 120, top: 1610, textAlign: 'center', opacity: kAviso, fontFamily: SANS, fontSize: 24, color: COR.claro.suave, lineHeight: 1.35}}>
        Cenários ilustrativos (IPCA + 5% a.a., inflação de 4,5% a.a.). Rentabilidade passada não garante rentabilidade futura. Não é recomendação de investimento.
      </div>
    </>
  );
};

export const VISUAIS: Record<string, React.FC<P>> = {
  print: Print, interrogacao: Interrogacao, donut: Donut, contador1: Contador1, printQueda: PrintQueda,
  avanco233: Avanco233, barras2: Barras2, regua: Regua, linhas: Linhas, barrasAnos: BarrasAnos,
  curvaExp: CurvaExp, holofote: Holofote, cta: Cta,
};
