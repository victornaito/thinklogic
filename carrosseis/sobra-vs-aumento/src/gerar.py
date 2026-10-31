"""Gera src/slide-01.html a slide-09.html do carrossel "Ganhar mais ou gastar melhor?" (SWOT).

Mesma identidade dos stories em stories/sobra-vs-aumento: papel, tinta e laranja.
Rode: python3 src/gerar.py && node src/render.mjs
"""
from pathlib import Path

AQUI = Path(__file__).parent
TOTAL = 9

BASE = """
@font-face { font-family: 'Geist'; src: url('fontes/Geist-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'Geist Mono'; src: url('fontes/GeistMono-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'DM Serif'; src: url('fontes/DMSerifDisplay-Italic.ttf') format('truetype'); font-style: italic; }
:root { --papel: #EDE9E1; --creme: #FBF4E8; --marinho: #181D26; --tinta: #15130F; --laranja: #F2511F;
  --mudo: rgba(21,19,15,.6); --fio: rgba(21,19,15,.16); --m: 80px; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1440px; overflow: hidden; background: var(--papel); }
body { -webkit-font-smoothing: antialiased; font-family: 'Geist'; color: var(--tinta); }
#q { position: absolute; inset: 0; background: var(--papel); }
#q.escuro { background: var(--marinho); color: #fff; --mudo: rgba(255,255,255,.62); --fio: rgba(255,255,255,.16); }
#q.laranja { background: var(--laranja); color: #fff; --mudo: rgba(255,255,255,.8); --fio: rgba(255,255,255,.3); }
.abs { position: absolute; }
.cab { left: var(--m); right: var(--m); top: 64px; display: flex; justify-content: space-between;
  font: 500 22px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); }
.rodape { left: var(--m); right: var(--m); bottom: 64px; display: flex; justify-content: space-between; align-items: center;
  font: 600 24px/1 'Geist Mono'; color: var(--mudo); }
.barra { display: flex; gap: 8px; }
.barra i { width: 30px; height: 6px; border-radius: 3px; background: var(--fio); }
.barra i.on { background: currentColor; }
.miolo { left: var(--m); right: var(--m); top: 150px; bottom: 150px; display: flex; flex-direction: column; justify-content: center; gap: 44px; }
.t { font-weight: 900; font-size: 108px; line-height: .98; letter-spacing: -0.045em; }
.c { font-weight: 500; font-size: 44px; line-height: 1.25; letter-spacing: -0.02em; }
.c b { font-weight: 800; }
.la { color: var(--laranja); }
.serifa { font-family: 'DM Serif'; font-style: italic; font-weight: 400; letter-spacing: -0.01em; }
.grifo { box-shadow: inset 0 -.3em 0 rgba(242,81,31,.85); }
.nota { font: 500 23px/1.45 'Geist Mono'; color: var(--mudo); }
.selo { display: inline-flex; align-items: center; gap: 18px; font: 700 28px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; }
.selo i { font-style: normal; width: 76px; height: 76px; border-radius: 20px; display: grid; place-items: center;
  background: var(--tinta); color: var(--papel); font: 900 46px/1 'Geist'; letter-spacing: 0; }
.selo.bom i { background: var(--laranja); color: #fff; }
.lista { list-style: none; display: flex; flex-direction: column; gap: 0; }
.lista li { display: grid; grid-template-columns: 70px 1fr; padding: 30px 0; border-top: 3px solid var(--fio); }
.lista li:last-child { border-bottom: 3px solid var(--fio); }
.lista .n { font: 600 28px/1.5 'Geist Mono'; color: var(--laranja); }
.lista .h { font-weight: 800; font-size: 46px; line-height: 1.1; letter-spacing: -0.03em; }
.lista .d { grid-column: 2; margin-top: 10px; font-weight: 500; font-size: 32px; line-height: 1.3; color: var(--mudo); }
"""

PAGINA = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Slide {n:02d} · sobra vs. aumento</title>
<style>{base}{css}</style></head>
<body><div id="q" class="{fundo}">
  <div class="abs cab"><span>{rotulo}</span><span>{n:02d}/{total:02d}</span></div>
  <div class="abs miolo">{miolo}
  </div>
  <div class="abs rodape"><span>@victornaito.financas</span><span class="barra">{barra}</span></div>
</div></body></html>
"""


def lista(itens):
    return '<ul class="lista">' + "".join(
        f'<li><span class="n">{i:02d}</span><div><div class="h">{h}</div></div><div class="d">{d}</div></li>'
        for i, (h, d) in enumerate(itens, start=1)) + "</ul>"


SLIDES = [
    ("", "Análise SWOT · fim do mês", """
    .t { font-size: 132px; line-height: .95; }
    .vs { display: flex; gap: 20px; }
    .vs div { flex: 1; border-radius: 26px; padding: 26px 30px; font-weight: 800; font-size: 38px; line-height: 1.1; letter-spacing: -0.02em; }
    .vs .a { border: 3px solid var(--fio); color: var(--mudo); }
    .vs .b { background: var(--tinta); color: var(--papel); }""", """
    <div class="t">Seu próximo aumento vale <span class="la">menos</span> que o gasto que você <span class="serifa">não cortou.</span></div>
    <div class="vs"><div class="a">Ganhar mais no emprego atual</div><div class="b">Gastar melhor hoje</div></div>
    <div class="c">Coloquei os dois numa análise SWOT. <b>A conta tem um vencedor.</b></div>"""),

    ("", "A pergunta", "", """
    <div class="t">Ganhar mais<br><span class="serifa la">ou</span> gastar melhor?</div>
    <div class="c">Os dois aumentam a sobra no fim do mês. Mas não do mesmo jeito.</div>
    <div class="c">Um depende do seu chefe, do orçamento da empresa e do dissídio.</div>
    <div class="c"><b>O outro depende de você, e começa hoje.</b></div>"""),

    ("", "A conta", """
    .miolo { gap: 34px; }
    .bar { display: flex; flex-direction: column; gap: 14px; }
    .rot { font: 600 25px/1 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; color: var(--mudo); }
    .trilho { height: 110px; border-radius: 18px; position: relative; overflow: hidden;
      background: repeating-linear-gradient(135deg, rgba(21,19,15,.1) 0 10px, transparent 10px 20px); }
    .cheio { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 18px; display: flex; align-items: center;
      padding-left: 30px; font-weight: 900; font-size: 58px; letter-spacing: -0.04em; color: #fff; white-space: nowrap; }""", """
    <div class="t" style="font-size:100px">De cada R$&nbsp;100…</div>
    <div class="bar"><div class="rot">Cortado do gasto</div>
      <div class="trilho"><div class="cheio" style="width:100%;background:var(--laranja)">R$&nbsp;100 na conta</div></div></div>
    <div class="bar"><div class="rot">De aumento · até R$&nbsp;5 mil</div>
      <div class="trilho"><div class="cheio" style="width:86%;background:var(--tinta)">R$&nbsp;86</div></div></div>
    <div class="bar"><div class="rot">De aumento · R$&nbsp;5 mil a R$&nbsp;7,35 mil</div>
      <div class="trilho"><div class="cheio" style="width:51%;background:var(--tinta)">~R$&nbsp;51</div></div></div>
    <div class="c">Corte de gasto <span class="grifo"><b>não paga INSS nem IR.</b></span></div>
    <div class="nota">INSS na faixa de 14%. Entre R$ 5 mil e R$ 7,35 mil a isenção nova do IR vai sendo retirada, e cada real a mais paga IR mais a perda do desconto. Simulação simplificada.</div>"""),

    ("", "S · Forças de cortar", "", """
    <div class="selo bom"><i>S</i>Forças</div>
    """ + lista([
        ("Rende 100%", "Cada real cortado sobra inteiro. Sem desconto na fonte."),
        ("Começa hoje", "Cancelou a assinatura à noite, sobra no mês que vem."),
        ("Só depende de você", "Não precisa de aprovação, avaliação nem dissídio."),
        ("Se repete todo mês", "R$ 300 cortados viram R$ 3.600 por ano. Todo ano."),
    ])),

    ("", "W · Fraquezas de cortar", "", """
    <div class="selo"><i>W</i>Fraquezas</div>
    """ + lista([
        ("Tem um piso", "Aluguel, comida e transporte não chegam a zero. O primeiro corte rende mais que o décimo."),
        ("Pede disciplina", "Corte radical demais acaba no “chutei o balde” do fim de semana."),
        ("Quem já vive no aperto tem pouco pra cortar", "Aí a renda é o gargalo de verdade. Sendo honesto."),
    ]) + """
    <div class="c" style="font-size:38px">Por isso é <b>otimizar</b>, não passar vontade.</div>"""),

    ("", "O · Oportunidades", """
    .juros { display: flex; gap: 20px; }
    .juros > div { flex: 1; background: var(--creme); border-radius: 26px; padding: 28px 30px; box-shadow: 0 14px 34px rgba(21,19,15,.08); }
    .juros .k { font: 600 23px/1.2 'Geist Mono'; letter-spacing: .08em; text-transform: uppercase; color: var(--mudo); }
    .juros .v { margin-top: 12px; font-weight: 900; font-size: 70px; letter-spacing: -0.05em; line-height: 1; color: var(--laranja); white-space: nowrap; }
    .miolo { gap: 36px; }""", """
    <div class="selo bom"><i>O</i>Oportunidades</div>
    """ + lista([
        ("Gasto invisível", "Assinatura esquecida, tarifa de banco, plano de celular maior que o uso."),
        ("Renegociar", "Internet, seguro, plano de saúde. E trocar dívida cara por crédito mais barato."),
    ]) + """
    <div class="c" style="font-size:40px">E o que sobra <b>rende juros.</b> R$&nbsp;300 por mês a 0,8%:</div>
    <div class="juros"><div><div class="k">Em 1 ano</div><div class="v">R$&nbsp;3,8 mil</div></div>
      <div><div class="k">Em 10 anos</div><div class="v">R$&nbsp;60 mil</div></div></div>"""),

    ("escuro", "T · Ameaças do aumento", """
    .selo i { background: #fff; color: var(--marinho); }
    .lista .n { color: var(--laranja); }""", """
    <div class="selo"><i>T</i>Ameaças · só esperar o aumento</div>
    """ + lista([
        ("O reajuste costuma só repor a inflação", "Dissídio de 5% com inflação de 4,5%: ganho real perto de zero."),
        ("O padrão de vida sobe junto", "Quem não sobra com R$ 4 mil normalmente não sobra com R$ 5 mil."),
        ("O imposto morde no caminho", "Na faixa de R$ 5 mil a R$ 7,35 mil, metade do aumento pode sumir."),
        ("Pode nem vir", "Crise, corte de orçamento, chefe novo. Fora do seu controle."),
    ])),

    ("laranja", "Na prática", """
    .num { font-weight: 900; font-size: 300px; line-height: .85; letter-spacing: -0.06em; }
    .grifo { box-shadow: inset 0 -.3em 0 rgba(21,19,15,.3); }
    .nota { color: rgba(255,255,255,.85); }""", """
    <div class="c">Cortar <b>R$&nbsp;300 por mês</b> pra quem ganha R$&nbsp;4&nbsp;mil</div>
    <div class="serifa" style="font-size:96px;line-height:1">equivale a</div>
    <div><div class="num">~9%</div><div class="t" style="margin-top:14px">de aumento.</div></div>
    <div class="c">Maior que a maioria dos reajustes. E dá pra fazer <span class="grifo"><b>hoje à noite.</b></span></div>
    <div class="nota">Aumento bruto de R$ 350 ≈ R$ 305 líquidos nessa faixa. Simulação simplificada.</div>"""),

    ("", "Conclusão", """
    .miolo { gap: 40px; }
    .dm { align-self: flex-start; max-width: 860px; background: var(--tinta); color: var(--papel); border-radius: 44px 44px 44px 12px;
      padding: 34px 44px; font-weight: 600; font-size: 44px; line-height: 1.2; letter-spacing: -0.02em; box-shadow: 0 20px 50px rgba(21,19,15,.18); }
    .dm small { display: block; margin-bottom: 12px; font: 600 22px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; color: rgba(237,233,225,.55); }
    .enviar { display: inline-flex; align-items: center; gap: 22px; background: var(--laranja); color: #fff; border-radius: 22px;
      padding: 22px 38px 24px; font-weight: 900; font-size: 64px; letter-spacing: -0.03em; line-height: 1; box-shadow: 0 20px 50px rgba(242,81,31,.35); }
    .enviar svg { width: 60px; height: 60px; }""", """
    <div class="t" style="font-size:92px">No emprego atual, <span class="grifo">gastar melhor</span> rende mais por real.</div>
    <div class="c">Manda pro amigo que <b>só pensa em ganhar mais</b> e ainda não entendeu que o jogo pode ser <span class="grifo"><b>gastar melhor.</b></span></div>
    <div class="dm"><small>Você, no direct dele</small>Lê isso antes de pedir aumento 👀</div>
    <div><span class="enviar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7Z"/></svg>Envia pra ele</span></div>"""),
]


def main():
    for n, (fundo, rotulo, css, miolo) in enumerate(SLIDES, start=1):
        barra = "".join(f'<i class="{"on" if i <= n else ""}"></i>' for i in range(1, TOTAL + 1))
        (AQUI / f"slide-{n:02d}.html").write_text(
            PAGINA.format(n=n, total=TOTAL, base=BASE, css=css, fundo=fundo, rotulo=rotulo, miolo=miolo, barra=barra),
            encoding="utf-8")


if __name__ == "__main__":
    main()
