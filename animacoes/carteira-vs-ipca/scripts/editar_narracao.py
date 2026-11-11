"""Corta erros/repetições da gravação e encurta pausas longas. Saída: wav editado + trechos com tempos novos."""
import json, subprocess, sys
import numpy as np

src, trechos_json, out_wav, out_json = sys.argv[1:5]
SR = 48000
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, dtype=np.float32)

trechos = json.load(open(trechos_json))
# textos corrigidos (o reconhecimento errou palavras que o Victor falou certo) e cortes
CORTAR = {87.95, 99.31, 116.72}            # "é isso, eu..." / 1a tentativa "é quem sabe" / 1a tentativa "ou ainda nem sabe a sua carteira"
CORRIGIR = {
    0.96: "Minha carteira começou no vermelho.",
    3.28: "Hoje",
    6.35: "Mas isso é bom ou é ruim?",
    8.42: "Pra responder, você precisa saber quanto uma carteira diversificada rende de verdade.",
    13.90: "E quase ninguém sabe.",
    15.36: "Em um ano, uma carteira bem montada, com renda fixa, ações, fundos imobiliários e um pouco de exterior,",
    21.85: "rende em média uns 10%.",
    24.33: "10 mil viram 11 mil.",
    27.72: "E tem ano que fica no negativo.",
    31.26: "Em dois anos, uns 20%.",
    35.92: "23",
    37.24: "vírgula 3%.",
    39.06: "Um pouco acima do esperado.",
    40.95: "Nada de milagre.",
    42.42: "Carteira montada e paciência.",
    47.31: "A régua certa é a inflação.",
    51.07: "É ele que mede quanto seu dinheiro perde de valor no mercado, na gasolina, no aluguel.",
    60.60: "Eu fiz 23,3.",
    63.12: "Quase o dobro.",
    67.14: "Em 5 anos, a mesma carteira faz uns 60%.",
    71.45: "10 mil viram quase 16.",
    74.79: "Em 10 anos,",
    81.21: "A inflação, nesse tempo,",
    83.41: "levou só uns 55%. Os primeiros anos parecem lentos.",
    101.66: "É saber o que esperar.",
    103.80: "Quem acha que vai dobrar em um ano larga tudo no primeiro mês no vermelho.",
    110.61: "Então eu te pergunto.",
    119.66: "Ou ainda nem sabe se a sua carteira está batendo a inflação?",
    122.88: "Comenta LIBERDADE que eu te mando a tabela completa.",
}
# "Mas é no final que os juros sob... / e os juros sobre juros aparecem" vira uma frase só
EMENDA = {89.78: (89.79, 90.78, "Mas é no final que os"), 92.47: (92.60, 94.30, "juros sobre juros aparecem.")}

pecas = []
for t in trechos:
    k = round(t["ini"], 2)
    if k in CORTAR:
        continue
    if k in EMENDA:
        a, b, txt = EMENDA[k]
    else:
        a, b, txt = t["ini"], t["fim"], CORRIGIR.get(k, t["texto"])
    pecas.append((a - 0.06, b + 0.10, txt))

PAUSA_MAX, PAUSA_EMENDA, FADE = 0.32, 0.02, int(0.012 * SR)
saida, novos, t_novo, fim_ant = [], [], 0.25, None
saida.append(np.zeros(int(0.25 * SR), np.float32))
for i, (a, b, txt) in enumerate(pecas):
    if fim_ant is not None:
        gap = a - fim_ant
        alvo = PAUSA_EMENDA if txt.startswith("juros sobre") else min(max(gap, 0.08), PAUSA_MAX)
        if txt == "vírgula 3%.":
            alvo = 0.05
        saida.append(np.zeros(int(alvo * SR), np.float32)); t_novo += alvo
    seg = x[int(a * SR):int(b * SR)].copy()
    seg[:FADE] *= np.linspace(0, 1, FADE); seg[-FADE:] *= np.linspace(1, 0, FADE)
    novos.append({"ini": round(t_novo, 3), "fim": round(t_novo + len(seg) / SR, 3), "texto": txt, "orig": [round(a, 2), round(b, 2)]})
    saida.append(seg); t_novo += len(seg) / SR; fim_ant = b
saida.append(np.zeros(int(0.6 * SR), np.float32))
y = np.concatenate(saida)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                "-af", "highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=9", "-ar", str(SR), out_wav],
               input=y.tobytes(), check=True)
json.dump(novos, open(out_json, "w"), ensure_ascii=False, indent=1)
print(f"{len(x)/SR:.1f}s -> {len(y)/SR:.1f}s, {len(novos)} trechos")
