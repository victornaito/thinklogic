"""Gera src/slide-01.html a slide-09.html do carrossel "5 passos pra não depender de eleição".

A capa usa duas fotos reais (Agência Brasil, CC BY): assets/foto-lula.jpg e assets/foto-flavio.jpg.
Enquanto os arquivos não existem, a capa mostra um espaço marcado no lugar de cada foto.
Os créditos vêm de CREDITO. Rode: python3 src/gerar.py
"""
from pathlib import Path

AQUI = Path(__file__).parent
ASSETS = AQUI.parent / "assets"
CREDITO = "Fotos: [fotógrafo]/Agência Brasil"   # troque pelo nome que vem na legenda da foto

MOLDURA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Slide {n} · 5 passos</title>
<link rel="stylesheet" href="base.css">
<style>
#quadro.cheio {{ background: var(--laranja); color: var(--tinta); --mudo: rgba(21,19,15,.68); --fio: rgba(21,19,15,.28); }}
.num {{ left: 72px; top: 140px; font: 900 190px/1 'Geist'; letter-spacing: -0.06em; color: var(--laranja); }}
.marca {{ box-shadow: inset 0 -0.34em 0 rgba(242,81,31,.85); }}
#quadro.cheio .marca {{ box-shadow: inset 0 -0.34em 0 rgba(21,19,15,.18); }}
{css}
</style>
</head>
<body>
<div id="quadro" class="{fundo}">
  <canvas id="grao" width="1080" height="1350" data-semente="{n}"></canvas>
  {cab}
{corpo}
  <div class="abs fio" style="top:1180px"></div>
  <div class="abs rodape" style="top:1222px">@victornaito.financas</div>
</div>
<script src="base.js"></script>
</body>
</html>
"""


def cab(texto):
    return f'<div class="abs cabecalho">{texto}</div>\n  <div class="abs fio" style="top:110px"></div>'


def linha(rot, valor, cls=""):
    return f'<div class="ln {cls}"><span>{rot}</span><span class="pt"></span><span class="v">{valor}</span></div>'


def foto(arquivo, rotulo):
    if (ASSETS / arquivo).exists():
        return f'<img src="../assets/{arquivo}" alt="">'
    return f'<div class="vaga"><span>{rotulo}</span></div>'


SLIDES = {
    "01": dict(fundo="marinho", cab="", css="""
.fotos { left: 0; top: 0; width: 1080px; height: 720px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; background: var(--marinho); }
.fotos img { width: 100%; height: 720px; object-fit: cover; display: block; filter: grayscale(.2) contrast(1.06); }
.vaga { height: 720px; background: #262c38; display: grid; place-items: center; text-align: center; padding: 40px;
  font: 500 22px/1.5 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; color: rgba(251,244,232,.55);
  border: 3px dashed rgba(251,244,232,.25); }
.credito { left: 72px; top: 686px; font: 500 15px/1 'Geist Mono'; letter-spacing: .04em; color: rgba(251,244,232,.8); text-shadow: 0 1px 6px rgba(0,0,0,.7); }
.t1 { top: 770px; font-size: 104px; }
.p1 { left: 72px; top: 890px; font-size: 104px; color: var(--laranja); }
.pe { left: 72px; top: 1080px; font: 600 22px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; color: var(--mudo); }
""", corpo=f"""
  <div class="abs fotos">{foto("foto-lula.jpg", "Foto 1<br>Lula comemorando<br>Agência Brasil · CC BY")}{foto("foto-flavio.jpg", "Foto 2<br>Flávio após o resultado<br>Agência Brasil · CC BY")}</div>
  <div class="abs credito">{CREDITO}</div>
  <div class="abs titulo t1">O Bolsonaro perdeu.</div>
  <div class="abs serifa p1">O seu boleto, não.</div>
  <div class="abs pe">5 passos pra não depender de eleição ▸</div>
"""),

    "02": dict(fundo="papel", cab=cab("O erro"), css="""
.t1 { top: 150px; font-size: 120px; }
.anos { left: 72px; top: 450px; width: 936px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.anos div { background: var(--creme); box-shadow: 0 10px 24px rgba(21,19,15,.1); padding: 22px 0 26px; text-align: center; }
.anos b { display: block; font: 900 64px/1 'Geist'; letter-spacing: -0.04em; }
.anos span { font: 500 17px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; color: var(--mudo); }
.anos .agora { background: var(--laranja); }
.anos .agora span { color: rgba(21,19,15,.75); }
.c1 { top: 700px; width: 936px; font-size: 42px; }
.c2 { top: 930px; width: 936px; font-size: 44px; font-weight: 800; }
""", corpo="""
  <div class="abs titulo t1">O erro não foi<br>o voto.</div>
  <div class="abs anos"><div><b>2014</b><span>eleição</span></div><div><b>2018</b><span>eleição</span></div><div><b>2022</b><span>eleição</span></div><div class="agora"><b>2026</b><span>e agora?</span></div></div>
  <div class="abs corpo c1">Foi deixar a sua vida financeira depender de quem ganha a cada 4 anos.</div>
  <div class="abs corpo c2"><span class="marca">Governo nenhum anota os seus gastos por você.</span></div>
"""),

    "03": dict(fundo="marinho", cab=cab("Passo 1 de 5"), css="""
.t1 { top: 340px; font-size: 112px; }
.c1 { top: 480px; width: 936px; }
.rec { left: 72px; top: 590px; width: 936px; }
.rec .ln.duvida .v { color: #D9481A; }
.p1 { left: 72px; top: 960px; font-size: 50px; width: 936px; }
""", corpo=f"""
  <div class="abs num">01</div>
  <div class="abs titulo t1">Anote cada gasto.</div>
  <div class="abs corpo c1">Por 30 dias, tudo. Do aluguel ao cafezinho.</div>
  <div class="abs recibo rec">
    {linha("Aluguel", "R$ 1.200")}
    {linha("Mercado", "R$ 650")}
    {linha("Delivery", "R$ 280")}
    {linha("Assinaturas", "R$ 90")}
    {linha("Não sei onde foi", "R$ 410", "duvida")}
  </div>
  <div class="abs serifa p1">Quem não anota, não sabe pra onde o dinheiro vai. E culpa o governo.</div>
"""),

    "04": dict(fundo="papel", cab=cab("Passo 2 de 5"), css="""
.t1 { top: 340px; font-size: 100px; }
.bloco { left: 72px; width: 936px; }
.b1 { top: 590px; } .b2 { top: 840px; }
.bloco h3 { margin: 0 0 12px; font: 600 22px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase; }
.bloco h3 b { color: var(--laranja); }
.barra { display: flex; height: 78px; }
.barra div { display: flex; align-items: center; padding: 0 18px; font: 900 34px/1 'Geist'; letter-spacing: -0.03em; overflow: hidden; white-space: nowrap; }
.s1 { background: var(--tinta); color: var(--creme); } .s2 { background: var(--laranja); color: var(--tinta); } .s3 { background: #B9B2A6; color: var(--tinta); }
.leg { margin-top: 12px; font: 500 21px/1.45 'Geist Mono'; color: var(--mudo); }
.leg b { color: var(--tinta); }
.n1 { top: 1100px; font-size: 22px; }
""", corpo="""
  <div class="abs num">02</div>
  <div class="abs titulo t1">Dê um destino<br>pra cada real.</div>
  <div class="abs bloco b1"><h3>Ganha até R$ 4 mil · <b>80/10/10</b></h3>
    <div class="barra"><div class="s1" style="width:80%">80%</div><div class="s2" style="width:10%">10</div><div class="s3" style="width:10%">10</div></div>
    <div class="leg">custo de vida · reserva e investimento · objetivos<br><b>R$ 3.000 → R$ 2.400 · R$ 300 · R$ 300</b></div></div>
  <div class="abs bloco b2"><h3>Ganha mais de R$ 4 mil · <b>50/30/20</b></h3>
    <div class="barra"><div class="s1" style="width:50%">50%</div><div class="s3" style="width:30%">30%</div><div class="s2" style="width:20%">20%</div></div>
    <div class="leg">necessidades · desejos · investimento<br><b>R$ 6.000 → R$ 3.000 · R$ 1.800 · R$ 1.200</b></div></div>
  <div class="abs nota n1">Na dúvida entre os dois, o diagnóstico mostra qual é o seu.</div>
"""),

    "05": dict(fundo="marinho", cab=cab("Passo 3 de 5"), css="""
.t1 { top: 340px; font-size: 112px; }
.rec { left: 72px; top: 610px; width: 936px; font-size: 32px; }
.rec .tot .v { background: var(--laranja); padding: 2px 12px; }
.c1 { top: 900px; width: 936px; }
.c2 { top: 1040px; width: 936px; font-size: 42px; font-weight: 800; }
""", corpo=f"""
  <div class="abs num">03</div>
  <div class="abs titulo t1">A conta tem<br>que sobrar.</div>
  <div class="abs recibo rec">
    {linha("Receita", "R$ 3.000")}
    {linha("− Despesa", "R$ 2.700")}
    <div class="div"></div>
    {linha("= SOBRA", "R$ 300", "tot")}
  </div>
  <div class="abs corpo c1">Todo mês, antes de qualquer coisa.<br>Sobra negativa é dívida chegando.</div>
  <div class="abs corpo c2"><span class="marca">Não importa quanto você ganha. Importa quanto sobra.</span></div>
"""),

    "06": dict(fundo="papel", cab=cab("Passo 4 de 5"), css="""
.t1 { top: 340px; font-size: 112px; }
.c1 { top: 590px; width: 936px; }
.meses { left: 72px; top: 730px; width: 936px; display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; }
.meses div { background: var(--laranja); padding: 18px 12px 16px; }
.meses b { display: block; font: 900 30px/1 'Geist'; letter-spacing: -0.03em; }
.meses span { font: 500 16px/1 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; color: rgba(21,19,15,.7); }
.tot { left: 72px; top: 870px; font: 600 40px/1.2 'Geist'; letter-spacing: -0.02em; }
.tot b { font-weight: 900; }
.p1 { left: 72px; top: 990px; font-size: 48px; width: 936px; }
""", corpo="""
  <div class="abs num">04</div>
  <div class="abs titulo t1">Monte a sua<br>reserva.</div>
  <div class="abs corpo c1">6 meses do seu custo de vida, num lugar seguro e com liquidez diária.</div>
  <div class="abs meses"><div><span>mês 1</span><b>2.400</b></div><div><span>mês 2</span><b>2.400</b></div><div><span>mês 3</span><b>2.400</b></div><div><span>mês 4</span><b>2.400</b></div><div><span>mês 5</span><b>2.400</b></div><div><span>mês 6</span><b>2.400</b></div></div>
  <div class="abs tot">R$ 2.400 × 6 = <b class="marca">R$ 14.400</b></div>
  <div class="abs serifa p1">Crise econômica vem com qualquer presidente. A reserva segura a sua.</div>
"""),

    "07": dict(fundo="marinho", cab=cab("Passo 5 de 5"), css="""
.t1 { top: 340px; font-size: 96px; }
.c1 { top: 580px; width: 936px; font-size: 34px; }
.curva { left: 72px; top: 780px; }
.p1 { left: 72px; top: 1040px; font-size: 46px; width: 936px; }
""", corpo="""
  <div class="abs num">05</div>
  <div class="abs titulo t1">Crie a sua própria<br>aposentadoria.</div>
  <div class="abs corpo c1">Os 10% (ou 20%) investidos todo mês viram uma renda que não depende de reforma, de INSS nem de quem estiver no poder.</div>
  <svg class="abs curva" width="936" height="230" viewBox="0 0 936 230">
    <line x1="0" y1="200" x2="936" y2="200" stroke="#FBF4E8" stroke-opacity=".25" stroke-width="3"/>
    <path d="M10 196 C 300 190, 560 160, 720 100 S 880 22, 920 14" fill="none" stroke="#F2511F" stroke-width="9" stroke-linecap="round"/>
    <circle cx="920" cy="14" r="12" fill="#F2511F"/>
    <text x="10" y="228" font-family="Geist Mono" font-size="20" fill="#FBF4E8" fill-opacity=".6">HOJE</text>
    <text x="926" y="228" text-anchor="end" font-family="Geist Mono" font-size="20" fill="#FBF4E8" fill-opacity=".6">APOSENTADORIA</text>
    <text x="890" y="70" text-anchor="end" font-family="Geist" font-weight="800" font-size="28" fill="#FBF4E8">a sua renda</text>
  </svg>
  <div class="abs serifa p1">A sua aposentadoria não precisa passar por Brasília.</div>
"""),

    "08": dict(fundo="cheio", cab=cab("A virada"), css="""
.t1 { top: 300px; font-size: 120px; color: var(--tinta); }
.p1 { left: 72px; top: 590px; font-size: 92px; color: var(--tinta); }
.c1 { top: 900px; width: 936px; font-size: 44px; font-weight: 700; }
""", corpo="""
  <div class="abs titulo t1">Presidente muda<br>a cada 4 anos.</div>
  <div class="abs serifa p1">O seu boleto chega<br>todo mês.</div>
  <div class="abs corpo c1">Você não controla a eleição.<br><span class="marca">Controla o seu dinheiro.</span></div>
"""),

    "09": dict(fundo="marinho", cab=cab("Próximo passo"), css="""
.t1 { top: 150px; font-size: 104px; }
.c1 { top: 410px; width: 936px; font-size: 38px; }
.lista { left: 72px; top: 650px; display: flex; flex-direction: column; gap: 18px; }
.lista p { margin: 0; font: 600 36px/1.2 'Geist'; letter-spacing: -0.015em; display: flex; gap: 16px; }
.lista p::before { content: '✓'; color: var(--laranja); font-weight: 900; }
.p1 { left: 72px; top: 890px; font-size: 56px; }
.faixa { left: 72px; top: 1060px; width: 936px; height: 86px; background: var(--creme); color: var(--tinta); display: flex; align-items: center; gap: 16px; padding: 0 28px; font: 800 34px/1 'Geist'; letter-spacing: -0.02em; white-space: nowrap; }
.faixa b { background: var(--laranja); padding: 8px 14px; font-weight: 900; letter-spacing: .02em; }
""", corpo="""
  <div class="abs titulo t1">O próximo passo<br>é o diagnóstico.</div>
  <div class="abs corpo c1">Um diagnóstico financeiro gratuito comigo, pra começar o plano da sua liberdade financeira.</div>
  <div class="abs lista"><p>os seus números na mesa</p><p>o método certo pra sua renda</p><p>o plano da sua aposentadoria</p></div>
  <div class="abs serifa p1">Sem depender de governo.</div>
  <div class="abs faixa"><b>GRATUITO</b> Diagnóstico financeiro · link na bio</div>
"""),
}

for n, s in SLIDES.items():
    (AQUI / f"slide-{n}.html").write_text(MOLDURA.format(n=n, **s), encoding="utf-8")
    print(f"src/slide-{n}.html")
