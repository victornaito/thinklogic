"""Transcreve por trechos de fala (separados por silêncio) com Whisper small via sherpa-onnx."""
import json, re, subprocess, sys, wave
import numpy as np, sherpa_onnx

wav, modelo_dir, saida = sys.argv[1:4]
r = subprocess.run(["ffmpeg", "-i", wav, "-af", "silencedetect=noise=-35dB:d=0.3", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
with wave.open(wav) as w:
    sr = w.getframerate(); dados = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
dur = len(dados) / sr
# trechos de fala = intervalos entre silêncios
falas, t = [], 0.0
pares = list(zip(ini, fim + [dur] * (len(ini) - len(fim))))
for s, e in pares:
    if s - t > 0.15: falas.append((t, s))
    t = e
if dur - t > 0.15: falas.append((t, dur))

rec = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder=f"{modelo_dir}/small-encoder.int8.onnx", decoder=f"{modelo_dir}/small-decoder.int8.onnx",
    tokens=f"{modelo_dir}/small-tokens.txt", language="pt", task="transcribe", num_threads=4)
out = []
for a, b in falas:
    pad = 0.1
    trecho = dados[int(max(0, a - pad) * sr): int(min(dur, b + pad) * sr)]
    st = rec.create_stream(); st.accept_waveform(sr, trecho); rec.decode_stream(st)
    txt = st.result.text.strip()
    out.append({"ini": round(a, 3), "fim": round(b, 3), "texto": txt})
    print(f"[{a:6.2f}–{b:6.2f}] {txt}", flush=True)
json.dump(out, open(saida, "w"), ensure_ascii=False, indent=1)
