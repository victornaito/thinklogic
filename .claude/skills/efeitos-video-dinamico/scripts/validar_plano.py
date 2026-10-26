#!/usr/bin/env python3
"""Confere o plano de efeitos contra as regras de retenção (referencias/retencao.md).

Uso: python3 validar_plano.py plano-efeitos.json [--duracao 38.2]
Sai com código 1 se houver ERRO.
"""
import argparse
import json
import sys
from pathlib import Path

# id: (nome, registro, peso, dur_min, dur_max, precisa_recorte, precisa_prints)
EFEITOS = {
    "orbita":          ("01 Órbita",            "FUNDO",    "pesado", 2.5, 4.5, True,  True),
    "parede-de-posts": ("02 Parede de posts",   "FUNDO",    "pesado", 2.0, 4.5, True,  True),
    "dentro-do-app":   ("03 Dentro do app",     "CENÁRIO",  "pesado", 2.5, 5.5, False, False),
    "saindo-da-tela":  ("04 Saindo da tela",    "FUNDO",    "pesado", 1.5, 3.5, True,  False),
    "zoom-digital":    ("05 Zoom digital",      "CÂMERA",   "tempero", 0.4, 3.0, False, False),
    "mockup-celular":  ("06 Mockup de celular", "OVERLAY",  "pesado", 2.5, 5.5, False, False),
    "checklist":       ("07 Checklist",         "OVERLAY",  "pesado", 2.0, 5.0, False, False),
    "mural-manchete":  ("08 Mural de manchete", "FUNDO",    "pesado", 2.5, 4.5, True,  False),
    "corte-no-zoom":   ("09 Corte no zoom",     "CÂMERA",   "tempero", 0.3, 0.9, False, False),
    "grafico-subindo": ("10 Gráfico subindo",   "FUNDO",    "pesado", 2.5, 4.5, True,  False),
    "revelacao":       ("11 Revelação",         "CENÁRIO",  "pesado", 2.5, 5.5, False, False),
    "chroma-key":      ("12 Chroma key",        "FUNDO",    "pesado", 2.5, 4.5, True,  False),
    "recorte-papel":   ("13 Recorte de papel",  "FUNDO",    "pesado", 2.0, 4.5, True,  False),
    "rabisco-vivo":    ("14 Rabisco vivo",      "FUNDO",    "pesado", 2.0, 4.5, True,  False),
    "vertigem":        ("15 Vertigem",          "FUNDO",    "pesado", 1.5, 3.5, True,  False),
    "capa-revista":    ("16 Capa de revista",   "FUNDO",    "pesado", 2.5, 4.5, True,  False),
    "letra-vidro":     ("17 Letra de vidro",    "TIPO",     "pesado", 2.0, 4.0, True,  False),
    "palavra-chave":   ("Palavra-chave",        "TIPO",     "tempero", 0.6, 2.0, False, False),
    "punch-in":        ("Punch-in leve",        "CÂMERA",   "tempero", 0.3, 4.0, False, False),
}

# (duração máxima do vídeo, pesados mín, pesados máx)
DENSIDADE = [(15, 1, 2), (30, 3, 4), (60, 5, 7), (90, 7, 9)]
MAIOR_VAO = 4.0


def faixa_pesados(dur):
    for limite, lo, hi in DENSIDADE:
        if dur <= limite:
            return lo, hi
    return int(dur / 12), int(dur / 10) + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plano")
    ap.add_argument("--duracao", type=float)
    a = ap.parse_args()

    plano = json.loads(Path(a.plano).read_text(encoding="utf-8"))
    dur = a.duracao or plano.get("duracao")
    if not dur:
        sys.exit("ERRO: informe --duracao ou 'duracao' no plano")
    itens = sorted(plano.get("efeitos", []), key=lambda e: e["inicio"])
    erros, avisos = [], []

    for e in itens:
        rot = f"[{e.get('id', '?')} {e['inicio']:.1f}s]"
        if e["efeito"] not in EFEITOS:
            erros.append(f"{rot} efeito desconhecido '{e['efeito']}'")
            continue
        nome, _, _, dmin, dmax, _, prints = EFEITOS[e["efeito"]]
        d = e["fim"] - e["inicio"]
        if d <= 0:
            erros.append(f"{rot} fim antes do início")
        if e["inicio"] < 0 or e["fim"] > dur + 0.05:
            erros.append(f"{rot} fora do vídeo (0–{dur:.1f}s)")
        if d > dmax + 1.5:
            erros.append(f"{rot} {nome} com {d:.1f}s: longo demais (até {dmax}s), volte pro rosto")
        elif d > dmax or d < dmin:
            avisos.append(f"{rot} {nome} com {d:.1f}s (faixa {dmin}–{dmax}s)")
        if not e.get("motivo") or not e.get("gatilho"):
            erros.append(f"{rot} sem 'gatilho' ou 'motivo': se não dá pra justificar, tire o efeito")
        if prints:
            avisos.append(f"{rot} {nome} precisa da pasta public/prints/ com os posts")

    itens = [e for e in itens if e["efeito"] in EFEITOS]
    pesados = [e for e in itens if EFEITOS[e["efeito"]][2] == "pesado"]

    # sobreposição entre efeitos que desenham a tela inteira
    for x, y in zip(pesados, pesados[1:]):
        if y["inicio"] < x["fim"] - 0.01:
            erros.append(f"{x['id']} e {y['id']} se sobrepõem ({y['inicio']:.1f}s < {x['fim']:.1f}s)")
    camera = [e for e in itens if EFEITOS[e["efeito"]][1] == "CÂMERA"]
    for x, y in zip(camera, camera[1:]):
        if y["inicio"] < x["fim"] - 0.01:
            erros.append(f"{x['id']} e {y['id']}: dois efeitos de câmera ao mesmo tempo")

    # gancho
    if not itens or itens[0]["inicio"] > 1.5:
        erros.append("sem gancho visual nos primeiros 1,5 s")
    elif EFEITOS[itens[0]["efeito"]][2] != "pesado" and not any(p["inicio"] <= 1.5 for p in pesados):
        avisos.append("o gancho é só tempero: considere um efeito pesado no início")

    # vãos sem mudança visual (início ou fim de qualquer efeito conta como mudança)
    marcas = sorted({0.0, dur} | {e["inicio"] for e in itens} | {e["fim"] for e in itens})
    for p, q in zip(marcas, marcas[1:]):
        dentro = any(e["inicio"] <= p and e["fim"] >= q and EFEITOS[e["efeito"]][2] == "pesado" for e in itens)
        if q - p > MAIOR_VAO and not dentro:
            erros.append(f"vão de {q - p:.1f}s sem mudança visual entre {p:.1f}s e {q:.1f}s")

    # repetição
    if dur <= 60:
        vistos = {}
        for e in pesados:
            if e["efeito"] in vistos:
                erros.append(f"{EFEITOS[e['efeito']][0]} repetido ({vistos[e['efeito']]} e {e['id']})")
            vistos[e["efeito"]] = e["id"]

    # registros vizinhos
    for x, y in zip(pesados, pesados[1:]):
        rx, ry = EFEITOS[x["efeito"]][1], EFEITOS[y["efeito"]][1]
        if rx == ry and y["inicio"] - x["fim"] < 4:
            avisos.append(f"{x['id']} e {y['id']}: dois {rx} seguidos com menos de 4 s de rosto entre eles")

    # densidade e tempo total
    lo, hi = faixa_pesados(dur)
    if not lo <= len(pesados) <= hi:
        (erros if len(pesados) > hi + 1 else avisos).append(
            f"{len(pesados)} efeitos pesados em {dur:.0f}s (recomendado {lo}–{hi})"
        )
    tempo_pesado = sum(e["fim"] - e["inicio"] for e in pesados)
    if tempo_pesado > 0.5 * dur:
        avisos.append(f"efeitos pesados ocupam {100 * tempo_pesado / dur:.0f}% do vídeo (máx. 50%): pouco rosto")

    # re-gancho e final
    if dur >= 20 and not any(0.35 * dur <= e["inicio"] <= 0.65 * dur for e in pesados):
        avisos.append("sem efeito pesado entre 35% e 65%: falta o re-gancho do meio")
    if not any(e["fim"] >= 0.85 * dur for e in itens):
        erros.append("nada nos últimos 15%: falta payoff/CTA visual")

    precisa = sorted({EFEITOS[e["efeito"]][0] for e in itens if EFEITOS[e["efeito"]][5]})

    print(f"Plano: {len(itens)} efeitos ({len(pesados)} pesados, {len(itens) - len(pesados)} temperos) em {dur:.1f}s")
    print(f"Tempo em efeito pesado: {tempo_pesado:.1f}s ({100 * tempo_pesado / dur:.0f}%)")
    if precisa:
        print("Precisam de recorte: " + ", ".join(precisa))
    for m in erros:
        print("ERRO  " + m)
    for m in avisos:
        print("AVISO " + m)
    if not erros:
        print("OK, sem erros.")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
