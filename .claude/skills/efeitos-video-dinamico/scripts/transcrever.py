#!/usr/bin/env python3
"""Transcreve o vídeo com tempo por palavra.

Saídas em <pasta-saida>:
  transcricao.json  {"palavras": [{"p", "ini", "fim"}], "frases": [{"texto", "ini", "fim"}]}
  transcricao.txt   uma frase por linha: [00:03.42 – 00:05.10] texto

Usa faster-whisper se estiver instalado, senão openai-whisper.
  pip install faster-whisper        (recomendado)
  pip install openai-whisper        (alternativa)

Uso: python3 transcrever.py <video> <pasta-saida> [--modelo small] [--idioma pt]
"""
import argparse
import json
import sys
from pathlib import Path


def mmss(t):
    m, s = divmod(t, 60)
    return f"{int(m):02d}:{s:05.2f}"


def com_faster_whisper(video, modelo, idioma):
    from faster_whisper import WhisperModel

    m = WhisperModel(modelo, device="auto", compute_type="auto")
    segs, _ = m.transcribe(str(video), language=idioma, word_timestamps=True, vad_filter=True)
    frases = []
    for s in segs:
        palavras = [{"p": w.word.strip(), "ini": round(w.start, 3), "fim": round(w.end, 3)} for w in s.words or []]
        frases.append({"texto": s.text.strip(), "ini": round(s.start, 3), "fim": round(s.end, 3), "palavras": palavras})
    return frases


def com_whisper(video, modelo, idioma):
    import whisper

    m = whisper.load_model(modelo)
    r = m.transcribe(str(video), language=idioma, word_timestamps=True)
    frases = []
    for s in r["segments"]:
        palavras = [{"p": w["word"].strip(), "ini": round(w["start"], 3), "fim": round(w["end"], 3)} for w in s.get("words", [])]
        frases.append({"texto": s["text"].strip(), "ini": round(s["start"], 3), "fim": round(s["end"], 3), "palavras": palavras})
    return frases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("saida")
    ap.add_argument("--modelo", default="small")
    ap.add_argument("--idioma", default="pt")
    a = ap.parse_args()

    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)

    frases = None
    for motor in (com_faster_whisper, com_whisper):
        try:
            frases = motor(a.video, a.modelo, a.idioma)
            print(f"motor: {motor.__name__}")
            break
        except ImportError:
            continue
    if frases is None:
        sys.exit("ERRO: instale faster-whisper (pip install faster-whisper) ou openai-whisper.")

    palavras = [w for f in frases for w in f["palavras"]]
    (saida / "transcricao.json").write_text(
        json.dumps({"palavras": palavras, "frases": frases}, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    linhas = [f"[{mmss(f['ini'])} – {mmss(f['fim'])}] {f['texto']}" for f in frases]
    (saida / "transcricao.txt").write_text("\n".join(linhas) + "\n", encoding="utf-8")

    # pausas longas: candidatas a jump cut ou a corte no zoom
    pausas = [
        (palavras[i]["fim"], palavras[i + 1]["ini"])
        for i in range(len(palavras) - 1)
        if palavras[i + 1]["ini"] - palavras[i]["fim"] >= 0.5
    ]
    print(f"{len(frases)} frases, {len(palavras)} palavras")
    for ini, fim in pausas:
        print(f"pausa {fim - ini:.2f}s em {mmss(ini)}")


if __name__ == "__main__":
    main()
