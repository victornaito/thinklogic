"""Gera src/timeline.json: tempo de cada palavra a partir dos trechos da narração editada.

Os trechos (audio/trechos.json) têm início e fim reais. Dentro de cada trecho, o tempo é
dividido entre as palavras pelo tamanho falado de cada uma (números contam pelo que se fala).

Marcação do texto exibido:
  *palavra*  vira destaque em serifa itálica grande
  |          força quebra de bloco
  ~palavra~  destaque em vermelho
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
trechos = json.loads((RAIZ / "audio/trechos.json").read_text())

# texto exibido de cada trecho (mesmas palavras faladas; números escritos como número)
EXIBIR = [
    "Minha carteira | começou no | ~*vermelho.*~",
    "Hoje",
    "ela rende | quase o | *dobro* | da inflação",
    "Mas isso é | *bom* | ou *ruim?*",
    "Pra responder, | você precisa saber | quanto uma carteira | *diversificada* | rende de | *verdade.*",
    "E quase | *ninguém* | sabe.",
    "Em *um* *ano,* | uma carteira | bem montada, | com renda fixa, | ações, | fundos imobiliários | e um pouco | de exterior,",
    "rende em média | uns | *10%.*",
    "10 mil | viram | 11 mil.",
    "Parece | *pouco,* | né?",
    "E tem ano | que fica no | ~*negativo.*~",
    "A minha | ficou | também.",
    "Em *dois* *anos,* | uns | *20%.*",
    "Agora | olha a | *minha.*",
    "23",
    "vírgula 3%.",
    "Um pouco | acima do | *esperado.*",
    "Nada de | *milagre.*",
    "Carteira montada | e *paciência.*",
    "Só que | o número | *sozinho* | engana.",
    "A régua | certa | é a *inflação.*",
    "O *IPCA.*",
    "É ele que mede | quanto seu dinheiro | perde de valor | no *mercado,* | na *gasolina,* | no *aluguel.*",
    "No mesmo período, | o IPCA | subiu | *12,6%.*",
    "Eu fiz | *23,3.*",
    "Quase o | *dobro.*",
    "E aqui | é onde fica | *interessante.*",
    "Em *5* *anos,* | a mesma carteira | faz uns | *60%.*",
    "10 mil | viram | quase 16.",
    "Em *10* *anos,*",
    "mais de | *150%.*",
    "10 mil | viram | 25 mil.",
    "A inflação, | nesse tempo,",
    "levou só uns | *55%.* | Os primeiros anos | parecem | *lentos.*",
    "Mas é | no *final* | que os",
    "*juros* | sobre *juros* | aparecem.",
    "A diferença | entre quem | chega lá | e quem desiste | no caminho | não é | *sorte.*",
    "É saber | o que | *esperar.*",
    "Quem acha | que vai | *dobrar* | em um ano | larga tudo | no primeiro mês | no ~*vermelho.*~",
    "Eu quase | ~*larguei.*~",
    "Então | eu te | *pergunto.*",
    "Você se sente | *preparado* | para planejar | a sua | *liberdade* | *financeira?*",
    "Ou ainda | nem sabe | se a sua carteira | está *batendo* | a *inflação?*",
    "Comenta | *LIBERDADE* | que eu te mando | a tabela completa.",
]
assert len(EXIBIR) == len(trechos), (len(EXIBIR), len(trechos))

UNIDADES = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]


def peso(p):
    """Tamanho falado aproximado (em letras)."""
    limpo = re.sub(r"[^\wÀ-ú%,]", "", p)
    if re.search(r"\d", limpo):
        n = 0
        for ch in limpo:
            if ch.isdigit():
                n += 6
            elif ch == ",":
                n += 7  # "vírgula"
            elif ch == "%":
                n += 9  # "por cento"
        return n + 2
    return len(limpo) + 2


frases = []
for t, txt in zip(trechos, EXIBIR):
    blocos = [b.strip() for b in txt.split("|")]
    palavras = []
    for bi, bloco in enumerate(blocos):
        for tok in bloco.split():
            vermelho = "~" in tok
            destaque = "*" in tok
            limpo = tok.replace("*", "").replace("~", "")
            palavras.append({"w": limpo, "bloco": bi, "destaque": destaque, "vermelho": vermelho})
    pesos = [peso(p["w"]) for p in palavras]
    total = sum(pesos)
    ini, fim = t["ini"], t["fim"] - 0.08
    acc = ini
    for p, w in zip(palavras, pesos):
        dur = (fim - ini) * w / total
        p["ini"] = round(acc, 3)
        p["fim"] = round(acc + dur, 3)
        acc += dur
    frases.append({"ini": t["ini"], "fim": t["fim"], "texto": txt, "palavras": palavras})

(RAIZ / "src/timeline.json").write_text(json.dumps(frases, ensure_ascii=False, indent=1))
print(f"{len(frases)} frases, {sum(len(f['palavras']) for f in frases)} palavras, fim {frases[-1]['fim']:.2f}s")
