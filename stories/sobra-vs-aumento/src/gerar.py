"""Stories "Sobra vs. aumento": SWOT resumida em 5 telas 1080x1920.

Topo (0-240px) e base (1640-1920px) ficam livres pra barra, @ e resposta do Instagram.
Rode: python3 src/gerar.py && node src/render.mjs
"""
from pathlib import Path

AQUI = Path(__file__).parent
TOTAL = 5

BASE = """
@font-face { font-family: 'Geist'; src: url('fontes/Geist-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'Geist Mono'; src: url('fontes/GeistMono-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'DM Serif'; src: url('fontes/DMSerifDisplay-Italic.ttf') format('truetype'); font-style: italic; }
:root { --papel: #EDE9E1; --creme: #FBF4E8; --marinho: #181D26; --tinta: #15130F; --laranja: #F2511F;
  --mudo: rgba(21,19,15,.6); --fio: rgba(21,19,15,.16); --m: 84px; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; background: var(--papel); }
body { -webkit-font-smoothing: antialiased; font-family: 'Geist'; color: var(--tinta); }
#q { position: absolute; inset: 0; background: var(--papel); }
#q.escuro { background: var(--marinho); color: #fff; --mudo: rgba(255,255,255,.62); --fio: rgba(255,255,255,.16); }
.abs { position: absolute; }
.cab { left: var(--m); right: var(--m); top: 250px; display: flex; justify-content: space-between;
  font: 500 24px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); }
.miolo { left: var(--m); right: var(--m); top: 320px; bottom: 300px; display: flex; flex-direction: column; justify-content: center; gap: 48px; }
.t { font-weight: 900; font-size: 112px; line-height: .98; letter-spacing: -0.045em; }
.c { font-weight: 500; font-size: 46px; line-height: 1.25; letter-spacing: -0.02em; }
.c b { font-weight: 800; }
.la { color: var(--laranja); }
.serifa { font-family: 'DM Serif'; font-style: italic; font-weight: 400; letter-spacing: -0.01em; }
.grifo { box-shadow: inset 0 -.32em 0 rgba(242,81,31,.85); }
.vaga { border: 4px dashed var(--fio); border-radius: 36px; height: 300px; display: grid; place-items: center;
  font: 500 26px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; color: var(--mudo); }
.nota { font: 500 24px/1.45 'Geist Mono'; color: var(--mudo); }
.arroba { left: var(--m); bottom: 300px; font: 600 26px/1 'Geist Mono'; color: var(--mudo); }
"""

PAGINA = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Story {n}</title>
<style>{base}{css}</style></head>
<body><div id="q" class="{fundo}">
  <div class="abs cab"><span>{rotulo}</span><span>{n:02d}/{total:02d}</span></div>
  <div class="abs miolo">{miolo}
  </div>
</div></body></html>
"""

TELAS = [
    ("", "Enquete", "", """
    <div class="c" style="font-family:'Geist Mono';font-size:30px;letter-spacing:.12em;text-transform:uppercase" >No fim do mês, o que deixa mais dinheiro sobrando?</div>
    <div class="t" style="font-size:150px">Ganhar mais<br><span class="serifa la" style="font-size:130px">ou</span><br>gastar melhor?</div>
    <div class="vaga">cole a enquete aqui</div>
    <div class="c">Vota antes de passar. A resposta tá na conta. →</div>"""),

    ("", "A conta", """
    .barra { display: flex; flex-direction: column; gap: 18px; }
    .rot { font: 600 28px/1 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; color: var(--mudo); }
    .trilho { height: 120px; border-radius: 20px; background: rgba(21,19,15,.07); position: relative; overflow: hidden; }
    .cheio { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 20px; display: flex; align-items: center;
      padding-left: 34px; font-weight: 900; font-size: 64px; letter-spacing: -0.04em; color: #fff; }
    .imposto { position: absolute; top: 0; bottom: 0; right: 0; display: flex; align-items: center; justify-content: center;
      font: 600 24px/1.1 'Geist Mono'; color: var(--mudo); text-align: center;
      background: repeating-linear-gradient(135deg, rgba(21,19,15,.1) 0 10px, transparent 10px 20px); }""", """
    <div class="t">De cada R$&nbsp;100…</div>
    <div class="barra"><div class="rot">Cortado do gasto</div>
      <div class="trilho"><div class="cheio" style="width:100%;background:var(--laranja)">R$&nbsp;100 na conta</div></div></div>
    <div class="barra"><div class="rot">De aumento no salário</div>
      <div class="trilho"><div class="cheio" style="width:86%;background:var(--tinta)">R$&nbsp;86</div><div class="imposto" style="width:14%">INSS</div></div></div>
    <div class="c">E acima de R$&nbsp;5 mil o <b>IR também morde.</b> Corte de gasto <span class="grifo"><b>não paga imposto.</b></span></div>
    <div class="nota">Faixa de 14% do INSS. Entre R$ 5 mil e R$ 7,35 mil a isenção do IR vai sendo retirada e o líquido cai mais.</div>"""),

    ("", "SWOT · cortar gastos", """
    .miolo { gap: 36px; }
    .grade { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
    .q { background: var(--creme); border-radius: 30px; padding: 34px 32px 36px; box-shadow: 0 14px 34px rgba(21,19,15,.08); min-height: 420px; }
    .q.ruim { background: transparent; border: 3px solid var(--fio); box-shadow: none; }
    .q .k { display: flex; align-items: center; gap: 14px; font: 700 26px/1 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; }
    .q .k i { font-style: normal; width: 52px; height: 52px; border-radius: 14px; display: grid; place-items: center;
      background: var(--tinta); color: var(--papel); font: 900 30px/1 'Geist'; }
    .q.bom .k i { background: var(--laranja); color: #fff; }
    .q ul { list-style: none; margin-top: 28px; display: flex; flex-direction: column; gap: 18px; }
    .q li { font-weight: 600; font-size: 36px; line-height: 1.15; letter-spacing: -0.02em; }""", """
    <div class="t" style="font-size:96px">Cortar gastos,<br><span class="la">em 4 quadros.</span></div>
    <div class="grade">
      <div class="q bom"><div class="k"><i>F</i>Forças</div><ul><li>Rende 100%</li><li>Começa hoje</li><li>Só depende de você</li></ul></div>
      <div class="q ruim"><div class="k"><i>F</i>Fraquezas</div><ul><li>Tem um piso</li><li>Pede disciplina</li></ul></div>
      <div class="q bom"><div class="k"><i>O</i>Oportunidades</div><ul><li>Assinatura esquecida</li><li>Tarifa e plano caro</li><li>Dívida cara renegociada</li></ul></div>
      <div class="q ruim"><div class="k"><i>A</i>Ameaças do aumento</div><ul><li>Dissídio = inflação</li><li>Padrão de vida sobe junto</li><li>Pode nem vir</li></ul></div>
    </div>"""),

    ("escuro", "Na prática", """
    .num { font-weight: 900; font-size: 230px; line-height: .9; letter-spacing: -0.06em; color: var(--laranja); }
    .igual { font-family: 'DM Serif'; font-style: italic; font-size: 90px; line-height: 1; }""", """
    <div class="c">Cortar <b>R$&nbsp;300 por mês</b> pra quem ganha R$&nbsp;4 mil</div>
    <div class="igual">equivale a</div>
    <div><div class="num" style="font-size:300px">~9%</div><div class="num" style="font-size:120px;margin-top:10px">de aumento.</div></div>
    <div class="c">Maior que a maioria dos reajustes. E você consegue <b>hoje à noite</b>, sem pedir pra ninguém.</div>
    <div class="nota">R$ 350 bruto ≈ R$ 305 líquido nessa faixa. Simulação simplificada.</div>"""),

    ("", "Conclusão", "", """
    <div class="t">No emprego atual, <span class="grifo">gastar melhor</span> rende mais por real.</div>
    <div class="c">E quando o aumento vier, ele vira <b>sobra</b>. Não vira padrão de vida novo.</div>
    <div class="vaga" style="height:340px">cole a caixinha aqui</div>
    <div class="c">Qual gasto você corta primeiro? <b>Me conta na caixinha.</b></div>"""),
]


def main():
    for n, (fundo, rotulo, css, miolo) in enumerate(TELAS, start=1):
        f = AQUI / f"story-{n:02d}.html"
        f.write_text(PAGINA.format(n=n, total=TOTAL, base=BASE, css=css, fundo=fundo, rotulo=rotulo, miolo=miolo),
                     encoding="utf-8")


if __name__ == "__main__":
    main()
