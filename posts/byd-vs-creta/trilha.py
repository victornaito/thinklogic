"""Sintetiza efeitos sonoros + música de fundo sincronizados com events.json.

Uso: python3 trilha.py  ->  gera trilha.wav (48 kHz, estéreo)
"""
import json
import wave
from pathlib import Path

import numpy as np

SR = 48000
DIR = Path(__file__).parent
rng = np.random.default_rng(7)

data = json.loads((DIR / "events.json").read_text())
DUR = data["duration"]
N = int(DUR * SR) + SR
sfx = np.zeros(N)
mus = np.zeros(N)


def tt(sec):
    return np.arange(int(sec * SR)) / SR


def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def highpass(x, fc):
    return x - lowpass(x, fc)


def add(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i < 0:
        sig, i = sig[-i:], 0
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


# ---------- efeitos ----------

def whoosh(dur=0.5):
    t = tt(dur)
    n = rng.standard_normal(len(t))
    env = np.sin(np.pi * t / dur) ** 2
    # varredura: mistura de passa-baixa crescente
    lo, hi = lowpass(n, 500), lowpass(n, 3500)
    mix = t / dur
    return highpass(lo * (1 - mix) + hi * mix, 150) * env * 1.6


def printer(dur):
    t = tt(dur + 0.05)
    out = np.zeros(len(t))
    step = int(0.016 * SR)
    click = highpass(rng.standard_normal(int(0.004 * SR)), 2000) * np.linspace(1, 0, int(0.004 * SR))
    for k in range(0, len(t) - len(click), step):
        out[k:k + len(click)] += click * rng.uniform(0.6, 1)
    motor = np.sign(np.sin(2 * np.pi * 820 * t)) * 0.08
    env = np.minimum(1, np.minimum(t / 0.02, (dur + 0.05 - t) / 0.04))
    return lowpass(out + motor, 6000) * env * 0.5


def tick(f=2600):
    t = tt(0.012)
    return np.sin(2 * np.pi * f * t) * np.exp(-t * 400)


def counter(dur, n=14):
    out = np.zeros(int((dur + 0.05) * SR))
    for k in range(n):
        x = k / (n - 1)
        when = dur * (1 - (1 - x) ** (1 / 3)) if x < 1 else dur  # inverso do easeOut cúbico
        add(out, tick(2400 + 600 * x), when, 0.5)
    return out


def thud(big=False):
    t = tt(0.6)
    f = 90 * np.exp(-t * 9) + 45
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (7 if big else 10))
    slap = lowpass(rng.standard_normal(len(t)), 2500) * np.exp(-t * 45)
    return (body * 1.0 + slap * 0.8) * (1.0 if big else 0.75)


def chime():
    t = tt(1.6)
    notes = [1318.5, 1975.5, 2637.0]
    out = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * (3 + i)) for i, f in enumerate(notes))
    return out * 0.22


def pop():
    t = tt(0.08)
    f = 500 + 900 * t / 0.08
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 40) * 0.6


def blip(f):
    t = tt(0.18)
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 18) * 0.35


def scratch(dur=0.4):
    t = tt(dur)
    n = rng.standard_normal(len(t))
    band = lowpass(highpass(n, 1800), 4500)
    return band * np.sin(np.pi * t / dur) * 0.9


def boom():
    t = tt(0.7)
    return np.sin(2 * np.pi * (55 + 40 * np.exp(-t * 12)) * t) * np.exp(-t * 6) * 0.7


def riser(dur):
    t = tt(dur)
    n = rng.standard_normal(len(t))
    return highpass(lowpass(n, 6000), 800) * (t / dur) ** 2 * 0.5


# agenda os efeitos a partir dos eventos
last_count = -1.0
blip_notes = [523.3, 587.3, 659.3, 784.0, 880.0, 1046.5]
grow_i = 0
stamps = 0
for e in data["events"]:
    t, kind = e["t"], e["type"]
    if kind == "scene" and e["idx"] > 0:
        add(sfx, whoosh(), t - 0.2, 0.55)
    elif kind == "print":
        add(sfx, printer(min(e["d"], 0.9)), t, 0.55)
    elif kind == "count":
        if t - last_count > 0.05:  # contadores da mesma linha disparam juntos
            add(sfx, counter(e["d"]), t, 0.45)
            last_count = t
    elif kind == "stamp":
        stamps += 1
        big = stamps > 1
        add(sfx, thud(big), t + 0.26, 0.9)
        if big:
            add(sfx, chime(), t + 1.4, 0.9)  # fim do contador dos R$ 47.200
    elif kind == "pop":
        add(sfx, pop(), t, 0.7)
    elif kind == "grow":
        add(sfx, blip(blip_notes[grow_i % 6]), t, 0.8)
        grow_i += 1
    elif kind == "strike":
        add(sfx, scratch(), t, 0.35)
    elif kind == "pulse":
        add(sfx, boom(), t, 0.8)
    elif kind in ("left", "right"):
        add(sfx, whoosh(0.4), t, 0.3)

# ---------- música (lo-fi, 92 BPM, Am7 – Fmaj7 – Cmaj7 – G6) ----------
BPM = 92
BEAT = 60 / BPM
BAR = 4 * BEAT
scene_t = [e["t"] for e in data["events"] if e["type"] == "scene"]
INTRO_END = scene_t[1]           # entra a bateria
DROP = scene_t[5]                # "Mas a conta termina no que sobrou"
OUTRO = scene_t[7]               # moral: só teclado

midi = lambda m: 440 * 2 ** ((m - 69) / 12)
CHORDS = [(57, [57, 60, 64, 67]), (53, [53, 57, 60, 64]), (48, [55, 59, 60, 64]), (55, [55, 59, 62, 64])]


def epiano(f, dur):
    t = tt(dur)
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    trem = 1 + 0.08 * np.sin(2 * np.pi * 4.5 * t)
    return s * np.exp(-t * 1.1) * np.minimum(1, t / 0.008) * trem


def bass(f, dur):
    t = tt(dur)
    return np.sin(2 * np.pi * f * t) * np.exp(-t * 2.2) * np.minimum(1, t / 0.01)


def kick():
    t = tt(0.35)
    return np.sin(2 * np.pi * np.cumsum(50 + 110 * np.exp(-t * 30)) / SR) * np.exp(-t * 9)


def hat():
    t = tt(0.05)
    return highpass(rng.standard_normal(len(t)), 7000) * np.exp(-t * 90)


def snare():
    t = tt(0.2)
    return lowpass(rng.standard_normal(len(t)), 3500) * np.exp(-t * 22) * 0.5 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * 0.3


def silent(t):
    return DROP - 0.75 <= t < DROP  # respiro antes da virada


bar = 0
while bar * BAR < DUR:
    t0 = bar * BAR
    root, notes = CHORDS[bar % 4]
    if not silent(t0):
        for k, m in enumerate(notes):
            add(mus, epiano(midi(m + 12), BAR * 1.05), t0 + k * 0.012, 0.11)
        # acorde repetido no tempo 3 (bem leve) para dar movimento
        for m in notes[1:]:
            add(mus, epiano(midi(m + 12), BAR / 2), t0 + 2 * BEAT, 0.05)
    for b in range(4):
        tb = t0 + b * BEAT
        if tb >= DUR or silent(tb):
            continue
        drums = INTRO_END <= tb < OUTRO
        if b in (0, 2) and tb >= INTRO_END - 0.01 and tb < OUTRO:
            add(mus, bass(midi(root - 12), BEAT * 1.8), tb, 0.38)
        if drums:
            if b in (0, 2):
                add(mus, kick(), tb, 0.32)
            if b in (1, 3):
                add(mus, snare(), tb, 0.2)
        for h in (0, 0.5):
            if tb + h * BEAT < DUR and not silent(tb + h * BEAT) and tb < OUTRO:
                add(mus, hat(), tb + h * BEAT, 0.12 if drums else 0.07)
    bar += 1

# silêncio total antes da virada (corta também as notas que ainda soam)
gate = np.ones(N)
a, b = int((DROP - 0.75) * SR), int(DROP * SR)
gate[a - int(0.08 * SR):a] = np.linspace(1, 0, int(0.08 * SR))
gate[a:b] = 0
mus *= gate

# transição da virada: riser + impacto
add(mus, riser(0.75), DROP - 0.75, 0.6)
add(mus, kick(), DROP, 0.8)
add(mus, lowpass(rng.standard_normal(int(1.2 * SR)), 9000) * np.exp(-tt(1.2) * 3.5), DROP, 0.12)

mus = lowpass(mus, 5200)  # calor lo-fi
# fade-in curto, fade-out no fim
fade = np.ones(N)
fade[: int(0.3 * SR)] = np.linspace(0, 1, int(0.3 * SR))
fo_start = int((DUR - 2.5) * SR)
fade[fo_start:] = np.clip(np.linspace(1, 0, N - fo_start) * 1.5, 0, 1)
mus *= fade

# ducking leve da música sob os efeitos
env = np.abs(sfx)
env = lowpass(env, 8)
duck = 1 - 0.35 * np.clip(env / (env.max() * 0.25 + 1e-9), 0, 1)
mix = mus * duck * 0.7 + sfx

# estéreo: música levemente aberta, efeitos no centro
delay = int(0.011 * SR)
L = mix
R = mus * duck * 0.7
R = np.concatenate([np.zeros(delay), R[:-delay]]) + sfx
st = np.stack([L, R], axis=1)[: int(DUR * SR)]
st = np.tanh(st * 1.2) / np.tanh(1.2)
st *= 0.89 / np.abs(st).max()

with wave.open(str(DIR / "trilha.wav"), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print("ok trilha.wav", round(len(st) / SR, 2), "s")
