#!/usr/bin/env python3
"""Recorta a pessoa do fundo, quadro a quadro, só nas janelas que precisam.

Salva <saida>/NNNNN.png (RGBA) com o mesmo número do quadro do vídeo (30 fps).

  pip install "rembg[cpu]" pillow

Uso:
  python3 recortar.py video.mp4 public/recorte --plano analise/plano-efeitos.json
  python3 recortar.py video.mp4 public/recorte --janelas 0-2.5 15-19
  python3 recortar.py video.mp4 public/recorte --tudo

--motor vision: no macOS, o Vision da Apple (VNGeneratePersonSegmentationRequest) é grátis e
costuma recortar cabelo melhor. Este script não o chama direto; peça ao Claude para gerar um
script Swift curto que leia os PNGs de --so-extrair e grave a máscara, mantendo os nomes.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

FPS = 30
# efeitos que precisam do recorte (ids do plano)
PRECISA_RECORTE = {
    "orbita", "parede-de-posts", "saindo-da-tela", "mural-manchete", "grafico-subindo",
    "chroma-key", "recorte-papel", "rabisco-vivo", "vertigem", "capa-revista", "letra-vidro",
}
MARGEM = 0.2  # segundos extras em cada ponta, para fades


def janelas_do_plano(caminho):
    plano = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return [
        (max(0.0, e["inicio"] - MARGEM), e["fim"] + MARGEM)
        for e in plano["efeitos"]
        if e["efeito"] in PRECISA_RECORTE
    ]


def juntar(janelas):
    janelas = sorted(janelas)
    out = []
    for ini, fim in janelas:
        if out and ini <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], fim))
        else:
            out.append((ini, fim))
    return out


def duracao(video):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
        capture_output=True, text=True, check=True,
    )
    return float(r.stdout.strip())


def extrair(video, ini, fim, pasta):
    """Extrai os quadros [ini, fim) numerados pelo índice absoluto do vídeo."""
    q0 = round(ini * FPS)
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", f"{q0 / FPS:.4f}", "-i", video,
         "-frames:v", str(round(fim * FPS) - q0), "-start_number", str(q0),
         str(Path(pasta) / "%05d.png")],
        check=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("saida")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--plano")
    g.add_argument("--janelas", nargs="+", help="ex.: 0-2.5 15-19 (segundos)")
    g.add_argument("--tudo", action="store_true")
    ap.add_argument("--modelo", default="isnet-general-use",
                    help="rembg: isnet-general-use (padrão), u2net_human_seg, birefnet-portrait")
    ap.add_argument("--so-extrair", action="store_true", help="só extrai os quadros (para usar outro motor)")
    a = ap.parse_args()

    if a.plano:
        janelas = janelas_do_plano(a.plano)
    elif a.janelas:
        janelas = [tuple(map(float, j.split("-"))) for j in a.janelas]
    else:
        janelas = [(0.0, duracao(a.video))]
    janelas = juntar(janelas)
    if not janelas:
        print("Nenhum efeito do plano precisa de recorte.")
        return

    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)

    if a.so_extrair:
        for ini, fim in janelas:
            extrair(a.video, ini, fim, saida)
        print(f"quadros extraídos em {saida}")
        return

    try:
        from rembg import new_session, remove
        from PIL import Image
    except ImportError:
        sys.exit('ERRO: pip install "rembg[cpu]" pillow')

    sessao = new_session(a.modelo)
    total = 0
    with tempfile.TemporaryDirectory() as tmp:
        for ini, fim in janelas:
            extrair(a.video, ini, fim, tmp)
        quadros = sorted(Path(tmp).glob("*.png"))
        for i, q in enumerate(quadros):
            destino = saida / q.name
            if destino.exists():
                continue
            img = Image.open(q).convert("RGB")
            remove(img, session=sessao, post_process_mask=True).save(destino)
            total += 1
            if i % 30 == 0:
                print(f"{i + 1}/{len(quadros)}", flush=True)
    seg = sum(f - i for i, f in janelas)
    print(f"{total} quadros recortados ({seg:.1f}s em {len(janelas)} janelas) → {saida}")


if __name__ == "__main__":
    main()
