"""Gera src/slide-02.html a slide-10.html (a capa, slide-01.html, é escrita à mão e já foi aprovada).

Cada slide: fundo, cabeçalho, valor do hodômetro, CSS próprio e corpo. A moldura
(grão, fios, hodômetro, @) vem de MOLDURA. Rode: python3 src/gerar.py
"""
from pathlib import Path

AQUI = Path(__file__).parent

MOLDURA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Slide {n} · carro quitado</title>
<link rel="stylesheet" href="base.css">
<style>{css}</style>
</head>
<body>
<div id="quadro" class="{fundo}">
  <canvas id="grao" width="1080" height="1350" data-semente="{n}"></canvas>
  <div class="abs cabecalho">{cab}</div>
  <div class="abs fio" style="top:110px"></div>
{corpo}
  <div class="abs fio" style="top:1180px"></div>
  <div class="abs odometro">
    <div class="rot">Acumulado<br>R$ / mês</div>
    <div class="digitos" data-valor="{odo}"></div>
  </div>
  <div class="abs rodape">@victornaito.financas</div>
</div>
<script src="base.js"></script>
</body>
</html>
"""

CARRO = "../assets/kicks-papel.png"

# silhueta de hatch/SUV de perfil, pros 88 carrinhos do slide 9
CARRINHO = """<svg width="0" height="0" style="position:absolute"><defs><symbol id="c" viewBox="0 0 76 36">
<path d="M3 26 V19 Q4 14 11 13 L21 5 Q24 3 29 3 H49 Q54 3 57 7 L63 13 Q72 14 73 19 V26 Z" fill="currentColor"/>
<path d="M24 7 H36 V13 H17 Z M40 7 H50 Q53 7 55 10 L58 13 H40 Z" fill="#EDE9E1"/>
<circle cx="19" cy="27" r="6.5" fill="#EDE9E1" stroke="currentColor" stroke-width="3.5"/>
<circle cx="58" cy="27" r="6.5" fill="#EDE9E1" stroke="currentColor" stroke-width="3.5"/>
</symbol></defs></svg>"""


def linha(rot, valor, sub=None):
    h = f'<div class="ln"><span>{rot}</span><span class="pt"></span><span class="v">{valor}</span></div>'
    return h + (f'<div class="sub">{sub}</div>' if sub else "")


SLIDES = {
    "02": dict(fundo="marinho", cab="Extrato mensal · carro quitado", odo="0.000", css="""
.t1 { top: 150px; font-size: 128px; }
.t1 .nao { color: var(--laranja); }
.rec { left: 72px; top: 470px; width: 760px; transform: rotate(-2deg); }
.c1 { top: 860px; width: 900px; }
.c2 { top: 1000px; width: 900px; font-weight: 800; }
.c2 span { box-shadow: inset 0 -14px 0 rgba(242,81,31,.85); }
""", corpo=f"""
  <div class="abs titulo t1">Parcela zero.<br>Custo, <span class="nao">não.</span></div>
  <div class="abs recibo rec">
    <div class="cab">Extrato mensal · carro quitado<br>FIPE R$ 80.000 · 1.000 km/mês · SP</div>
    <div class="div"></div>
    {linha("PARCELA", "R$ 0,00")}
    {linha("OUTRAS COBRANÇAS", "6 LINHAS")}
  </div>
  <div class="abs corpo c1">Fiz o extrato de um carro de R$ 80 mil, sem 1&nbsp;real de dívida. Deu 6 linhas.</div>
  <div class="abs corpo c2"><span>Duas delas não aparecem em app de banco nenhum.</span></div>
"""),

    "03": dict(fundo="papel", cab="Linhas 01 e 02 · custos fixos", odo="0.580", css="""
.t1 { top: 150px; font-size: 120px; }
.car { left: 420px; top: 318px; width: 620px; }
.rec { left: 72px; top: 830px; width: 936px; }
.p1 { left: 72px; top: 1092px; font-size: 46px; }
""", corpo=f"""
  <div class="abs titulo t1">Ele cobra<br>até parado.</div>
  <img class="abs carro-papel car" src="{CARRO}" alt="">
  <div class="abs recibo rec">
    {linha("01 IPVA + licenciamento", "R$ 280", "4% do valor todo ano em SP + taxa do Detran")}
    {linha("02 Seguro", "R$ 300", "média de R$ 3.600 por ano")}
  </div>
  <div class="abs serifa p1">O carro dorme na garagem. O boleto, não.</div>
"""),

    "04": dict(fundo="marinho", cab="Linhas 03 e 04 · custos de rodar", odo="1.322", css="""
.t1 { top: 150px; font-size: 120px; }
.rec { left: 72px; top: 470px; width: 936px; }
.p1 { left: 72px; top: 940px; font-size: 64px; }
""", corpo=f"""
  <div class="abs titulo t1">E cobra mais<br>quando anda.</div>
  <div class="abs recibo rec">
    {linha("03 Manutenção", "R$ 200", "revisão, pneu, freio, imprevisto")}
    {linha("04 Combustível", "R$ 542", "83 litros a R$ 6,50 (1.000 km a 12 km/l)")}
    <div class="div"></div>
    <div class="ln tot"><span>O QUE SAI DA CONTA</span><span class="pt"></span><span class="v">R$ 1.322</span></div>
  </div>
  <div class="abs serifa p1">Até aqui, é o custo<br>que você vê.</div>
"""),

    "05": dict(fundo="laranja", cab="A virada", odo="?.???", css="""
.metade { left: 0; top: 0; width: 1080px; height: 720px; background: var(--laranja); }
.cabecalho, .fio { z-index: 2; }
#grao { z-index: 3; }
#quadro.laranja .cabecalho { color: rgba(21,19,15,.7); }
.fio.topo { border-top-color: rgba(21,19,15,.3) !important; }
.t1 { top: 170px; font-size: 112px; color: var(--tinta); }
.rec { left: 72px; top: 780px; width: 936px; }
.rec .fantasma { color: rgba(21,19,15,.14); }
.rec .fantasma .pt { border-bottom-color: rgba(21,19,15,.12); }
.c1 { top: 975px; }
.p1 { left: 72px; top: 1036px; font-size: 76px; }
""", corpo=f"""
  <div class="abs metade"></div>
  <div class="abs titulo t1">Agora as duas<br>linhas que o banco<br>não mostra.</div>
  <div class="abs recibo rec">
    <div class="fantasma">{linha("05 ██████████", "R$ ???")}{linha("06 ████████████████", "R$ ???")}</div>
  </div>
  <div class="abs corpo c1">Elas não saem da sua conta.</div>
  <div class="abs serifa p1">Saem do seu patrimônio.</div>
"""),

    "06": dict(fundo="marinho", cab="Linha 05 · depreciação", odo="1.989", css="""
.t1 { top: 150px; font-size: 112px; }
.k1 { left: 72px; top: 412px; transform: rotate(-2deg); }
.k2 { left: 564px; top: 420px; transform: rotate(2deg); }
.janela { width: 408px; height: 250px; }
.janela img { width: 430px; left: -12px; top: -88px; }
.k2 .janela img { filter: grayscale(1) contrast(.75) brightness(1.08); opacity: .8; }
.k2 .leg { color: rgba(21,19,15,.55); }
.rec { left: 72px; top: 800px; width: 936px; }
.c1 { top: 1000px; width: 936px; }
""", corpo=f"""
  <div class="abs titulo t1">Ninguém te manda<br>boleto.</div>
  <div class="abs cartao-foto k1"><div class="janela"><img src="{CARRO}" alt=""></div><div class="leg"><span>Hoje</span><span>R$ 80.000</span></div></div>
  <div class="abs cartao-foto k2"><div class="janela"><img src="{CARRO}" alt=""></div><div class="leg"><span>Em 1 ano</span><span>R$ 72.000</span></div></div>
  <div class="abs recibo rec">
    {linha("05 Depreciação", "R$ 667", "~10% ao ano, média de seminovo na FIPE")}
  </div>
  <div class="abs corpo c1">Mas todo mês o seu carro vale <b class="forte">R$ 667 a menos.</b></div>
"""),

    "07": dict(fundo="papel", cab="Linha 06 · custo de oportunidade", odo="2.629", css="""
.t1 { top: 150px; font-size: 104px; }
.car { left: 300px; top: 300px; width: 700px; }
.cordao { left: 548px; top: 548px; width: 4px; height: 92px; background: var(--tinta); transform: rotate(14deg); transform-origin: top center; }
.etiqueta { left: 380px; top: 628px; transform: rotate(8deg); background: var(--laranja); color: var(--tinta);
  padding: 18px 34px 18px 64px; border-radius: 8px 18px 18px 8px; font: 900 64px/1 'Geist'; letter-spacing: -0.03em;
  clip-path: polygon(34px 0, 100% 0, 100% 100%, 34px 100%, 0 50%); }
.etiqueta::before { content: ''; position: absolute; left: 30px; top: 50%; width: 16px; height: 16px; margin-top: -8px; border-radius: 50%; background: var(--papel); }
.rec { left: 72px; top: 850px; width: 936px; }
.c1 { top: 1010px; width: 936px; }
.n1 { top: 1124px; }
""", corpo=f"""
  <div class="abs titulo t1">R$ 80 mil parados<br>na garagem.</div>
  <img class="abs carro-papel car" src="{CARRO}" alt="">
  <div class="abs cordao"></div>
  <div class="abs etiqueta">R$ 80.000</div>
  <div class="abs recibo rec">
    {linha("06 Custo de oportunidade", "R$ 640")}
  </div>
  <div class="abs corpo c1">Investidos, pagariam R$ 640. Todo mês. Sem você sair de casa.</div>
  <div class="abs nota n1">0,8% a.m. líquido: abaixo do CDI de hoje. A conta é conservadora.</div>
"""),

    "08": dict(fundo="marinho", cab="O extrato completo", odo="2.629", css="""
.rec { left: 120px; top: 150px; width: 840px; transform: rotate(-1.5deg); }
.stamp { left: 610px; top: 684px; transform: rotate(-6deg); font-size: 72px; }
.par { left: 72px; width: 936px; display: flex; align-items: baseline; gap: 16px; font: 600 28px/1 'Geist Mono'; letter-spacing: .04em; white-space: nowrap; }
.par .pt { flex: 1; border-bottom: 3px dotted var(--fio); transform: translateY(-6px); }
.par .m { width: 22px; height: 22px; background: var(--creme); align-self: center; }
.par.b .m { background: var(--laranja); }
.par1 { top: 830px; } .par2 { top: 886px; }
.p1 { left: 72px; top: 974px; font-size: 68px; }
""", corpo=f"""
  <div class="abs recibo rec">
    <div class="cab">Extrato mensal · carro quitado<br>FIPE R$ 80.000 · 1.000 km/mês · SP</div>
    <div class="div"></div>
    {linha("01 IPVA + licenciamento", "R$ 280")}
    {linha("02 Seguro", "R$ 300")}
    {linha("03 Manutenção", "R$ 200")}
    {linha("04 Combustível", "R$ 542")}
    {linha("05 Depreciação", "R$ 667")}
    {linha("06 Custo de oportunidade", "R$ 640")}
    <div class="dupla"></div>
    <div class="ln tot"><span>TOTAL MENSAL</span><span class="pt"></span><span class="v">R$ 2.629</span></div>
  </div>
  <div class="abs carimbo stamp">TODO MÊS</div>
  <div class="abs par a par1"><span class="m"></span><span>01–04 · você paga</span><span class="pt"></span><span>R$ 1.322</span></div>
  <div class="abs par b par2"><span class="m"></span><span>05–06 · você perde sem ver</span><span class="pt"></span><span>R$ 1.307</span></div>
  <div class="abs serifa p1">Metade você paga.<br>A outra metade, perde sem ver.</div>
"""),

    "09": dict(fundo="papel", cab="Traduzindo", odo="2.629", css="""
.t1 { top: 150px; font-size: 100px; }
.grade { left: 72px; top: 410px; width: 936px; display: grid; grid-template-columns: repeat(11, 76px); column-gap: 10px; row-gap: 14px; color: var(--tinta); }
.grade svg { width: 76px; height: 36px; display: block; }
.c1 { top: 880px; font-size: 44px; font-weight: 600; }
.c1 .tres { box-shadow: inset 0 -16px 0 rgba(242,81,31,.85); }
.p1 { left: 72px; top: 980px; font-size: 54px; color: var(--mudo); }
""", corpo="""
  """ + CARRINHO + """
  <div class="abs titulo t1">R$ 2.629 =<br>88 corridas de app.</div>
  <div class="abs grade">""" + "".join('<svg><use href="#c"/></svg>' for _ in range(88)) + """</div>
  <div class="abs corpo c1">A R$ 30 cada. <span class="tres">Quase 3 por dia.</span> Todo dia.</div>
  <div class="abs serifa p1">Não é pra vender o carro.<br>É pra saber quanto ele custa.</div>
"""),

    "10": dict(fundo="marinho", cab="A conta de 10 anos", odo="2.629", css="""
.t1 { top: 150px; font-size: 100px; }
.base { left: 72px; width: 936px; top: 820px; border-top: 3px solid var(--fio); }
.barA { left: 72px; top: 300px; width: 420px; height: 520px; background: var(--laranja); color: var(--tinta); padding: 28px 30px; }
.barA .val { font: 900 100px/1 'Geist'; letter-spacing: -0.05em; }
.barA .val small { font-size: 52px; letter-spacing: -0.03em; }
.barB { left: 588px; top: 789px; width: 420px; height: 31px; background: var(--creme); }
.valB { left: 588px; top: 470px; font: 900 100px/1 'Geist'; letter-spacing: -0.05em; }
.valB small { font-size: 52px; letter-spacing: -0.03em; }
.kB { left: 620px; top: 590px; padding: 10px 10px 12px; transform: rotate(-3deg); }
.kB .janela { width: 300px; height: 160px; }
.kB .janela img { width: 310px; left: -6px; top: -54px; filter: grayscale(1) contrast(.75) brightness(1.08); opacity: .85; }
.rotulo { top: 840px; width: 420px; font: 500 19px/1.45 'Geist Mono'; letter-spacing: .06em; text-transform: uppercase; color: var(--mudo); }
.rA { left: 72px; } .rB { left: 588px; }
.p1 { left: 72px; top: 930px; font-size: 56px; }
.p1 b { font-style: normal; font-family: 'Geist'; font-weight: 900; letter-spacing: -0.04em; box-shadow: inset 0 -14px 0 var(--laranja); }
.cta { left: 72px; top: 1080px; width: 936px; height: 80px; background: var(--creme); color: var(--tinta); display: flex; align-items: center; padding: 0 24px; gap: 12px; font: 500 25px/1 'Geist'; letter-spacing: -0.01em; white-space: nowrap; }
.cta b { font-weight: 900; background: var(--laranja); padding: 8px 12px; letter-spacing: .02em; }
""", corpo=f"""
  <div class="abs titulo t1">Em 10 anos:</div>
  <div class="abs barA"><div class="val"><small>R$</small> 473<small> mil</small></div></div>
  <div class="abs valB"><small>R$</small> 28<small> mil</small></div>
  <div class="abs cartao-foto kB"><div class="janela"><img src="{CARRO}" alt=""></div></div>
  <div class="abs barB"></div>
  <div class="abs base"></div>
  <div class="abs rotulo rA">Sem o carro: os R$ 80 mil<br>+ R$ 1.322/mês investidos</div>
  <div class="abs rotulo rB">Com o carro: um carro<br>de 10 anos</div>
  <div class="abs serifa p1">O carro quitado de R$ 80 mil<br>custa <b>R$ 445 mil.</b></div>
  <div class="abs cta">Comenta <b>EXTRATO</b> e eu te mando o site pra você calcular o seu cenário.</div>
"""),
}

for n, s in SLIDES.items():
    html = MOLDURA.format(n=n, **s)
    if n == "05":  # na virada o fio de cima fica sobre o laranja
        html = html.replace('class="abs fio" style="top:110px"', 'class="abs fio topo" style="top:110px"')
    (AQUI / f"slide-{n}.html").write_text(html, encoding="utf-8")
    print(f"src/slide-{n}.html")
