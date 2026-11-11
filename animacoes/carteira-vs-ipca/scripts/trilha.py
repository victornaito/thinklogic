"""Trilha e efeitos sonoros sintetizados (numpy), sincronizados com a timeline.

Rode da pasta do projeto, depois de `node scripts/exportar_eventos.mjs`:
  python3 scripts/trilha.py
Saída: public/trilha.wav (música baixa, abaixa sozinha quando a voz fala, + SFX).
"""
import json
import subprocess
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
SR = 48000
frases = json.loads((RAIZ / "src/timeline.json").read_text())
ct = json.loads((RAIZ / "audio/cenas-tempo.json").read_text())
DUR = ct["duracao"]
cenas = {c["id"]: c for c in ct["cenas"]}
N = int(DUR * SR)
rng = np.random.default_rng(7)


def tp(f, trecho=None):
    ps = frases[f]["palavras"]
    if trecho is None:
        return ps[0]["ini"]
    return next(p["ini"] for p in ps if trecho.lower() in p["w"].lower())


def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)


def lowpass(x, fc):
    # um polo, suficiente para amaciar
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def nota(f, dur, vol, timbre="pluck"):
    n = int(dur * SR)
    t = np.arange(n) / SR
    if timbre == "pluck":
        s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
        return vol * s * env(n, 0.004, dur / 3)
    # pad: serras desafinadas suavizadas
    s = sum(np.sin(2 * np.pi * f * d * t) + 0.3 * np.sin(4 * np.pi * f * d * t) for d in (0.997, 1.0, 1.004))
    att = np.minimum(1, t / 0.8) * np.minimum(1, (dur - t) / 0.8)
    return vol * s * att / 3


def soma(buf, sinal, t0):
    i = int(t0 * SR)
    if i >= len(buf) or i + len(sinal) <= 0:
        return
    j = min(len(buf), i + len(sinal))
    buf[max(i, 0):j] += sinal[max(0, -i):j - i]


# ---------------------------------------------------------------- música
musica = np.zeros(N)
BPM = 92
beat = 60 / BPM
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
acordes = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G
compasso = 4 * beat
k = 0
t0 = 0.0
while t0 < DUR:
    ac = acordes[k % 4]
    pad = sum(nota(hz(m - 12), compasso + 0.6, 0.05, "pad") for m in ac)
    soma(musica, pad, t0)
    soma(musica, nota(hz(ac[0] - 24), compasso, 0.10, "pluck") * 1.0, t0)
    arp = [ac[0], ac[1], ac[2], ac[1] + 12, ac[2], ac[1], ac[0] + 12, ac[2]]
    for j, m in enumerate(arp):
        soma(musica, nota(hz(m + 12), 0.5, 0.035, "pluck"), t0 + j * beat / 2)
    k += 1
    t0 += compasso
musica = lowpass(musica, 2600)

# música mais presente na virada (cena "anos") e no CTA
ganho = np.full(N, 0.85)
for cid, g in (("anos", 1.15), ("juros", 1.1), ("cta", 1.2)):
    c = cenas[cid]
    ganho[int(c["ini"] * SR):int(c["fim"] * SR)] = g
# silêncio de respiro no "Eu quase larguei"
tl = tp(39, "larguei")
ganho[int((tl - 0.2) * SR):int((tl + 1.0) * SR)] *= 0.25

# ducking: abaixa a música quando a voz fala
voz = subprocess.run(["ffmpeg", "-v", "error", "-i", str(RAIZ / "public/narracao.wav"), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
voz = np.frombuffer(voz, dtype=np.float32)[:N]
voz = np.pad(voz, (0, N - len(voz)))
jan = int(0.05 * SR)
rms = np.sqrt(np.convolve(voz ** 2, np.ones(jan) / jan, mode="same"))
duck = 1 - 0.55 * np.clip(rms / 0.05, 0, 1)
duck = np.convolve(duck, np.ones(int(0.15 * SR)) / int(0.15 * SR), mode="same")
musica *= ganho * duck

# ---------------------------------------------------------------- efeitos
sfx = np.zeros(N)


def whoosh(t0, dur=0.38, vol=0.22):
    n = int(dur * SR)
    ruido = rng.standard_normal(n)
    fc = np.linspace(400, 5000, n)
    y = np.zeros(n)
    acc = 0.0
    for i in range(n):  # passa-baixa com corte subindo
        a = np.exp(-2 * np.pi * fc[i] / SR)
        acc = (1 - a) * ruido[i] + a * acc
        y[i] = acc
    tt = np.arange(n) / n
    soma(sfx, vol * y * np.sin(np.pi * tt) ** 2 * 3, t0 - dur * 0.6)


def pop(t0, f=520, vol=0.25):
    n = int(0.12 * SR)
    t = np.arange(n) / SR
    fr = f * (1 + 1.2 * np.exp(-t / 0.01))
    soma(sfx, vol * np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(n, 0.001, 0.03), t0)


def tick(t0, vol=0.10):
    n = int(0.02 * SR)
    soma(sfx, vol * rng.standard_normal(n) * env(n, 0.0005, 0.004), t0)


def impacto(t0, vol=0.55):
    n = int(1.2 * SR)
    t = np.arange(n) / SR
    corpo = np.sin(2 * np.pi * np.cumsum(55 + 90 * np.exp(-t / 0.05)) / SR) * env(n, 0.002, 0.35)
    ar = lowpass(rng.standard_normal(n), 900) * env(n, 0.001, 0.08) * 2
    soma(sfx, vol * (corpo + 0.4 * ar), t0)


def queda(t0, vol=0.18):
    n = int(0.6 * SR)
    t = np.arange(n) / SR
    fr = 440 * np.exp(-t / 0.35)
    soma(sfx, vol * np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(n, 0.005, 0.3), t0)


def riser(t0, t1, vol=0.16):
    n = int((t1 - t0) * SR)
    t = np.arange(n) / SR
    fr = 200 * 2 ** (3 * t / t[-1])
    s = np.sin(2 * np.pi * np.cumsum(fr) / SR) * 0.5 + lowpass(rng.standard_normal(n), 3000)
    soma(sfx, vol * s * (t / t[-1]) ** 2, t0)


def clique(t0, vol=0.35):
    for d, f in ((0, 2400), (0.035, 1600)):
        n = int(0.03 * SR)
        t = np.arange(n) / SR
        soma(sfx, vol * np.sin(2 * np.pi * f * t) * env(n, 0.0005, 0.006), t0 + d)


def lampada(t0, vol=0.3):
    n = int(0.25 * SR)
    soma(sfx, vol * lowpass(rng.standard_normal(n), 1800) * env(n, 0.001, 0.05) * 2, t0)
    n2 = int(0.8 * SR)
    t = np.arange(n2) / SR
    soma(sfx, 0.04 * np.sin(2 * np.pi * 120 * t) * np.exp(-t / 0.5), t0)


# trocas de cena com mudança de fundo
lista = ct["cenas"]
for a, b in zip(lista, lista[1:]):
    if a["fundo"] != b["fundo"]:
        whoosh(b["ini"])

queda(tp(0, "vermelho"))
impacto(tp(2, "dobro"), 0.3)
for p in ("renda", "ações", "fundos", "exterior"):
    pop(tp(6, p), 600)
pop(tp(7, "10%"), 420, 0.3)
t = tp(8, "viram")
for i in range(14):
    tick(t + i * 1.0 / 14)
pop(t + 1.0, 700)
queda(tp(10, "negativo"))
pop(tp(11, "minha"), 300)
whoosh(tp(12) + 0.15, 0.3, 0.18)
pop(tp(12, "20%"), 500)
t = frases[14]["ini"]
t1 = frases[15]["fim"]
for i in range(int((t1 - t) * 16)):
    tick(t + i / 16, 0.08)
pop(t1, 760, 0.3)
pop(tp(16), 380)
pop(tp(16, "esperado") + 0.2, 640, 0.3)
for p in ("mercado", "gasolina", "aluguel"):
    pop(tp(22, p), 480, 0.2)
pop(tp(21, "IPCA"), 350, 0.3)
pop(tp(23, "12,6%"), 420)
pop(tp(24, "23,3"), 640)
impacto(tp(25, "dobro"))
riser(cenas["interessante"]["ini"], tp(26, "interessante") + 0.5)
pop(tp(27, "5"), 560, 0.3)
pop(tp(28, "16"), 700, 0.2)
whoosh(tp(29), 0.3, 0.25)
impacto(tp(30, "150%"))
pop(tp(31, "25"), 760, 0.2)
riser(tp(34, "final") - 0.2, tp(35, "aparecem"), 0.12)
impacto(tp(35, "aparecem"), 0.35)
lampada(cenas["holofote"]["ini"])
tl = tp(39, "larguei")
for i in range(4):
    lampada(tl + i * 0.11, 0.12)
tb = tp(43, "LIBERDADE")
pop(tb, 520, 0.3)
clique(tb + 0.75)

mix = musica * 0.55 + sfx
pico = np.max(np.abs(mix))
mix = mix / pico * 0.5
saida = RAIZ / "public/trilha.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-",
                "-af", "loudnorm=I=-24:TP=-3:LRA=11", "-ar", str(SR), "-ac", "2", str(saida)],
               input=mix.astype(np.float64).tobytes(), check=True)
print("trilha:", saida, f"{DUR:.1f}s")
