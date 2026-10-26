"""Trilha do Reel: medo e receio do futuro, que vira direção e termina em esperança.

Segue as cenas do src/reel.html (48 s):
  0 a 4    hook       estrondo grave + drone que sobe
  4 a 14   a dor      coração batendo (60 bpm) + cluster dissonante (lá contra si bemol)
  14 a 20  a dúvida   o relógio entra (tique a cada 0,5 s), o coração acelera, sobe um riser
  20 a 38  as 5 dicas ostinato em lá menor a 120 BPM: ainda tenso, mas andando pra frente
  38       a virada   impacto + meio segundo de silêncio
  38 a 48  o CTA      acordes maiores (fá → dó) e sinos: o futuro que dá pra construir
Os acertos de texto (clique, carimbo, whoosh) vêm de audio/beats.json, gerado pelo reel.mjs.
Saída: audio/trilha-medo.wav a -14 LUFS. Rode de dentro da pasta do projeto: python3 src/trilha-medo.py
"""
import json, pathlib, subprocess
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

RAIZ = pathlib.Path.cwd()
SR, DUR = 48000, 48.0
N = int(SR * DUR)
rng = np.random.default_rng(20261026)
mix = np.zeros(N)

lp = lambda x, f: sosfilt(butter(2, f / (SR / 2), 'low', output='sos'), x)
hp = lambda x, f: sosfilt(butter(2, f / (SR / 2), 'high', output='sos'), x)
bp = lambda x, a, b: sosfilt(butter(2, [a / (SR / 2), b / (SR / 2)], 'band', output='sos'), x)
tt = lambda d: np.arange(int(d * SR)) / SR


def poe(x, t, g=1.0):
    i = int(t * SR)
    if i >= N:
        return
    n = min(len(x), N - i)
    mix[i:i + n] += g * x[:n]


def janela(t0, t1, ataque=1.0, saida=1.0):
    """Envelope que sobe em `ataque` s a partir de t0 e desce em `saida` s até t1."""
    t = np.arange(N) / SR
    return np.clip((t - t0) / ataque, 0, 1) * np.clip((t1 - t) / saida, 0, 1)


# ---------- instrumentos ----------
def drone(f, d):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * f * k * (1 + 0.002 * j) * t) / k for k in range(1, 7) for j in (-1, 1))
    return lp(x, 380) * 0.5


def cluster(fs, d):
    t = tt(d); x = np.zeros(len(t))
    for f in fs:
        vib = 1 + 0.004 * np.sin(2 * np.pi * 5.2 * t + f)
        for k in range(1, 5):
            x += np.sin(2 * np.pi * f * k * np.cumsum(vib) / SR) / (k * k)
    return lp(x, 1800)


def coracao(g=1.0):
    def bate(v):
        t = tt(0.35); fr = 45 + 35 * np.exp(-t / 0.03)
        return v * np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.11)
    x = np.zeros(int(0.7 * SR)); a = bate(1.0); b = bate(0.65)
    x[:len(a)] += a; i = int(0.26 * SR); x[i:i + len(b)] += b[:len(x) - i]
    return g * np.tanh(2.2 * x)


def tique(g=1.0):
    t = tt(0.06)
    return g * (hp(rng.standard_normal(len(t)), 3500) * np.exp(-t / 0.006) + 0.6 * np.sin(2 * np.pi * 2600 * t) * np.exp(-t / 0.01))


def estrondo(g=1.0):
    t = tt(3.0); fr = 32 + 50 * np.exp(-t / 0.25)
    x = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 1.1)
    x += 0.4 * lp(rng.standard_normal(len(t)), 300) * np.exp(-t / 0.4)
    return g * np.tanh(1.6 * x)


def riser(d, g=1.0):
    t = tt(d); u = t / d; ruido = rng.standard_normal(len(t)); out = np.zeros(len(t)); b = 512
    for i in range(0, len(t), b):
        fc = 300 + 5000 * (i / len(t)) ** 2
        out[i:i + b] = bp(ruido[max(0, i - 1024):i + b], fc * 0.6, min(fc * 1.6, 20000))[-len(ruido[i:i + b]):]
    return g * out * u ** 2


def piano(f, d, v=1.0):
    t = tt(d + 0.8)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.2)
    return v * x * np.exp(-t / 0.45)


def bumbo(v=1.0):
    t = tt(0.4); fr = 50 + 80 * np.exp(-t / 0.04)
    return v * np.tanh(3 * np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.18))


def sino(f, v=1.0):
    t = tt(2.5)
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 3.01 * f * t) * np.exp(-t / 0.4)
    return v * x * np.exp(-t / 0.9) * np.clip(t / 0.003, 0, 1)


def pad(fs, d):
    t = tt(d); x = np.zeros(len(t))
    for f in fs:
        for j in (-0.1, 0, 0.1):
            for k in range(1, 6):
                x += ((-1) ** (k + 1)) * np.sin(2 * np.pi * f * 2 ** (j / 12) * k * t) / k
    return lp(x, 1600) * np.clip(t / 0.8, 0, 1) * np.clip((d - t) / 0.8, 0, 1)


# ---------- efeitos dos acertos de texto ----------
def clique(v=1.0):
    t = tt(0.1)
    return v * (np.sin(2 * np.pi * 1700 * t) * np.exp(-t / 0.01) + 0.4 * hp(rng.standard_normal(len(t)), 3000) * np.exp(-t / 0.003))


def carimbo(v=1.0):
    t = tt(0.5); fr = 42 + 60 * np.exp(-t / 0.05)
    return v * (np.tanh(1.8 * np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.18)) + 0.5 * bp(rng.standard_normal(len(t)), 350, 1800) * np.exp(-t / 0.03))


def whoosh(v=1.0):
    t = tt(0.5); u = t / 0.5
    return v * bp(rng.standard_normal(len(t)), 500, 2500) * np.sin(np.pi * u) ** 2


hz = lambda m: 440 * 2 ** ((m - 69) / 12)
A1, A2, C3, E3, A3, Bb3, E4 = hz(33), hz(45), hz(48), hz(52), hz(57), hz(58), hz(64)

# 0 a 4: estrondo no quadro 0 + drone grave que sobe
poe(estrondo(), 0.0, 0.9)
poe(drone(A1, 21.0) * janela(0, 21.0, 2.0, 1.0)[:int(21 * SR)], 0.0, 0.55)

# 4 a 20: coração; acelera na dúvida (14 a 20)
t = 4.0
while t < 20.0:
    poe(coracao(), t, 0.7)
    t += 1.0 if t < 14.0 else max(0.62, 1.0 - (t - 14.0) * 0.07)

# 4 a 20: cluster dissonante lá / si bemol / mi, crescendo até 20 s
cl = cluster([A3, Bb3, E4], 16.5)
cl *= np.clip(np.arange(len(cl)) / SR / 14.0, 0, 1) ** 1.5 * np.clip((16.5 - np.arange(len(cl)) / SR) / 0.5, 0, 1)
poe(cl, 4.0, 0.22)

# 14 a 20: o relógio (o ano passando no contador)
t = 14.0
while t < 20.0:
    poe(tique(), t, 0.35)
    t += 0.5
poe(riser(2.0), 18.0, 0.5)

# 20 a 38: ostinato em lá menor, colcheias a 120 BPM, bumbo nos tempos
notas = [A2, E3, A3, E3, C3, E3, A3, E3]
t, i = 20.0, 0
while t < 37.9:
    poe(piano(notas[i % 8], 0.25, 0.8 if i % 2 == 0 else 0.55), t, 0.35)
    if i % 2 == 0:
        poe(bumbo(0.9), t, 0.6)
    t += 0.25; i += 1
poe(drone(A1, 18.0) * janela(0, 18.0, 1.0, 0.6)[:int(18 * SR)], 20.0, 0.35)

# 38: a virada. Impacto, meio segundo de silêncio
poe(estrondo(0.8), 38.0, 0.8)

# 38,5 a 48: esperança. Fá maior → dó maior, sinos no CTA
poe(pad([hz(53), hz(57), hz(60), hz(65)], 4.2), 38.5, 0.16)
poe(pad([hz(48), hz(52), hz(55), hz(60), hz(64)], 6.0), 42.4, 0.16)
for tb, m in ((42.5, 76), (43.2, 79), (44.2, 84), (45.2, 79), (46.0, 76)):
    poe(sino(hz(m), 0.6), tb, 0.35)
for tb in (42.5, 43.5, 44.5, 45.5, 46.5):
    poe(bumbo(0.5), tb, 0.4)

# acertos de texto do reel (audio/beats.json vem em blocos de 8 s)
grade = json.load(open(RAIZ / 'audio' / 'beats.json'))
for k, sl in enumerate(grade['slides']):
    for ev in sl['eventos']:
        tabs = ev['t'] + k * sl['duracao_s']
        tipo = ev.get('tipo')
        if tipo == 'impacto':
            poe(carimbo(), tabs, 0.55)
        elif tipo == 'whoosh':
            poe(whoosh(), tabs - 0.1, 0.25 * ev.get('gain', 1.0))
        else:
            poe(clique(), tabs, 0.12)

# master: grave limpo, limite e -14 LUFS
mix = hp(mix, 28)
mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.9
mix = np.tanh(1.3 * mix) / np.tanh(1.3)
bruto = RAIZ / 'audio' / 'trilha-medo-bruto.wav'
wavfile.write(str(bruto), SR, (np.stack([mix, mix], 1) * 32767).astype(np.int16))
saida = RAIZ / 'audio' / 'trilha-medo.wav'
subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(bruto),
                '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', str(SR), str(saida)], check=True)
bruto.unlink()
print(saida)
