"""Gera src/slide-01.html a slide-10.html do carrossel "Consórcio x financiamento x juntar".

Mesma moldura dos posts da série. Os números vêm do contas.py (mesmas premissas).
Rode: python3 src/gerar.py
"""
from pathlib import Path

AQUI = Path(__file__).parent
CARRO = "../../carro-quitado/assets/kicks-papel.png"

# números do contas.py
ENTRADA, PMT, MES_JUNTA = 16000, 2044, 28
VALOR, RENDE, REAJ = 80000, 0.008, (1.04) ** (1 / 12) - 1

MOLDURA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Slide {n} · consórcio x financiamento x à vista</title>
<link rel="stylesheet" href="base.css">
<style>
.marca {{ box-shadow: inset 0 -0.34em 0 rgba(242,81,31,.85); }}
.ac {{ color: var(--laranja); }}
{css}
</style>
</head>
<body>
<div id="quadro" class="{fundo}">
  <canvas id="grao" width="1080" height="1350" data-semente="{n}"></canvas>
  <div class="abs cabecalho">{cab}</div>
  <div class="abs fio" style="top:110px"></div>
{corpo}
  <div class="abs fio" style="top:1180px"></div>
  {pe}
  <div class="abs rodape" style="top:1222px">@victornaito.financas</div>
</div>
<script src="base.js"></script>
</body>
</html>
"""


def linha(rot, valor, sub=None, cls=""):
    h = f'<div class="ln {cls}"><span>{rot}</span><span class="pt"></span><span class="v">{valor}</span></div>'
    return h + (f'<div class="sub">{sub}</div>' if sub else "")


def cartao(largura, altura, img_w, img_x, img_y, extra=""):
    return (f'<div class="janela" style="width:{largura}px;height:{altura}px">'
            f'<img src="{CARRO}" style="width:{img_w}px;left:{img_x}px;top:{img_y}px;{extra}" alt=""></div>')


def grafico_juntar():
    """Saldo investido mês a mês (barras) contra o preço do carro à vista (linha)."""
    W, H, x0, x1, y0, y1 = 936, 340, 70, 920, 20, 300
    s, barras, precos = ENTRADA, [], []
    for m in range(MES_JUNTA + 1):
        if m:
            s = s * (1 + RENDE) + PMT
        barras.append(s)
        precos.append(VALOR * (1 + REAJ) ** m * 0.95)
    top = 90000
    X = lambda m: x0 + (x1 - x0) * m / MES_JUNTA
    Y = lambda v: y1 - (y1 - y0) * v / top
    bw = (x1 - x0) / (MES_JUNTA + 1) * 0.7
    out = f'<svg class="abs graf" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
    for v in (0, 30000, 60000, 90000):
        out += f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="#FBF4E8" stroke-opacity=".12" stroke-width="2"/>'
        out += (f'<text x="{x0 - 12}" y="{Y(v) + 7}" text-anchor="end" font-family="Geist Mono" font-size="18" '
                f'fill="#FBF4E8" fill-opacity=".55">{v // 1000}k</text>')
    for m, v in enumerate(barras):
        cor = "#F2511F" if m == MES_JUNTA else "#FBF4E8"
        op = "1" if m == MES_JUNTA else ".75"
        out += f'<rect x="{X(m) - bw / 2:.1f}" y="{Y(v):.1f}" width="{bw:.1f}" height="{y1 - Y(v):.1f}" fill="{cor}" fill-opacity="{op}"/>'
    pts = " ".join(f"{X(m):.1f},{Y(p):.1f}" for m, p in enumerate(precos))
    out += f'<polyline points="{pts}" fill="none" stroke="#F2511F" stroke-width="5" stroke-dasharray="10 8"/>'
    out += (f'<text x="{X(2)}" y="{Y(precos[2]) - 14}" font-family="Geist Mono" font-size="20" letter-spacing="2" '
            f'fill="#F2511F">PREÇO DO CARRO À VISTA</text>')
    for m in (0, 12, 24, 28):
        anc = "end" if m == MES_JUNTA else "middle"
        out += (f'<text x="{X(m) + (bw / 2 if m == MES_JUNTA else 0):.1f}" y="{y1 + 34}" text-anchor="{anc}" font-family="Geist Mono" font-size="20" '
                f'fill="#FBF4E8" fill-opacity=".6">{"hoje" if m == 0 else f"mês {m}"}</text>')
    return out + "</svg>"


def placar():
    linhas = [("Financiar", "R$ 114 mil", 0, 48, "#15130F", "carro hoje · paga até o mês 48"),
              ("Consórcio", "R$ 104 mil", None, 60, "#7A7468", "carro no sorteio · paga até o mês 60"),
              ("Juntar", "R$ 73 mil", 28, 28, "#F2511F", "carro no mês 28 · paga até o mês 28")]
    W, x0, x1 = 936, 0, 936
    X = lambda m: x0 + (x1 - x0) * m / 60
    out = '<div class="abs placar">'
    for nome, total, carro, ate, cor, leg in linhas:
        out += f'<div class="pl"><div class="pl-cab"><span class="pl-n">{nome}</span><span class="pl-t">{total}</span></div>'
        out += f'<svg width="{W}" height="58" viewBox="0 0 {W} 58">'
        out += f'<rect x="0" y="22" width="{W}" height="14" fill="#15130F" fill-opacity=".08"/>'
        out += f'<rect x="0" y="22" width="{X(ate):.1f}" height="14" fill="{cor}"/>'
        if carro is None:
            out += (f'<text x="{X(30)}" y="18" text-anchor="middle" font-family="Geist" font-weight="900" '
                    f'font-size="22" fill="#15130F">? ? ?</text>')
        else:
            cx = max(14, X(carro))
            out += f'<circle cx="{cx:.1f}" cy="29" r="14" fill="#FBF4E8" stroke="{cor}" stroke-width="5"/>'
        out += "</svg>"
        out += f'<div class="pl-leg">{leg}</div></div>'
    out += '<div class="pl-eixo"><span>hoje</span><span>12</span><span>24</span><span>36</span><span>48</span><span>60 meses</span></div>'
    return out + "</div>"


def roleta():
    cel = "".join(f'<span{" class=\"sorte\"" if m == 37 else ""}>{m}</span>' for m in range(1, 61))
    return f'<div class="abs roleta">{cel}</div>'


SLIDES = {
    "01": dict(fundo="papel", cab="Consórcio × financiamento × à vista",
               pe='<div class="abs seta">3 caminhos, o mesmo bolso ▸</div>', css="""
.l1 { left: 72px; top: 150px; font: 800 74px/1 'Geist'; letter-spacing: -0.04em; }
.numero { left: 62px; top: 236px; font-weight: 900; font-size: 236px; letter-spacing: -0.06em; line-height: 1; white-space: nowrap; }
.numero small { font-size: 110px; letter-spacing: -0.04em; }
.numero .rs { font-size: 110px; vertical-align: .95em; margin-right: 12px; }
.p1 { left: 72px; top: 500px; font-size: 76px; }
.car { left: 110px; top: 480px; width: 860px; }
.cordao { left: 432px; top: 790px; width: 4px; height: 66px; background: var(--tinta); transform: rotate(12deg); transform-origin: top center; }
.etiqueta { left: 330px; top: 846px; transform: rotate(5deg); background: var(--laranja); color: var(--tinta);
  padding: 16px 30px 16px 58px; font: 900 44px/1 'Geist'; letter-spacing: -0.02em; white-space: nowrap;
  clip-path: polygon(30px 0, 100% 0, 100% 100%, 30px 100%, 0 50%); }
.etiqueta::before { content: ''; position: absolute; left: 26px; top: 50%; width: 14px; height: 14px; margin-top: -7px; border-radius: 50%; background: var(--papel); }
.seta { left: 560px; top: 1222px; font: 600 22px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--tinta); }
""", corpo=f"""
  <div class="abs l1">Financiar é pagar</div>
  <div class="abs numero"><span class="rs">R$</span>41<small> mil</small></div>
  <div class="abs serifa p1">pra não esperar 28 meses.</div>
  <img class="abs carro-papel car" src="{CARRO}" alt="">
  <div class="abs cordao"></div>
  <div class="abs etiqueta">PRA JÁ</div>
"""),

    "02": dict(fundo="marinho", cab="A regra do jogo", pe="", css="""
.t1 { top: 150px; font-size: 120px; }
.c1 { top: 430px; width: 936px; font-size: 40px; }
.portas { left: 72px; top: 560px; width: 936px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.portas div { background: var(--creme); color: var(--tinta); height: 300px; padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between; }
.portas span { font: 500 18px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: rgba(21,19,15,.6); }
.portas b { font: 900 46px/1 'Geist'; letter-spacing: -0.04em; }
.portas .j { background: var(--laranja); }
.c2 { top: 960px; width: 936px; font-size: 48px; font-weight: 800; }
""", corpo="""
  <div class="abs titulo t1">Mesmo carro.<br>Mesmo bolso.</div>
  <div class="abs corpo c1">R$ 16 mil guardados e R$ 2.044 livres por mês.</div>
  <div class="abs portas"><div><span>caminho 1</span><b>Financiar</b></div><div><span>caminho 2</span><b>Consórcio</b></div><div class="j"><span>caminho 3</span><b>Juntar</b></div></div>
  <div class="abs corpo c2"><span class="marca">Só muda quem recebe os juros.</span></div>
"""),

    "03": dict(fundo="papel", cab="Caminho 1 · financiar", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.rec { left: 72px; top: 480px; width: 936px; }
.stamp { left: 560px; top: 820px; transform: rotate(-7deg); font-size: 70px; }
.n1 { top: 1080px; }
""", corpo=f"""
  <div class="abs titulo t1">Financiar:<br>o carro sai hoje.</div>
  <div class="abs recibo rec">
    {linha("Entrada", "R$ 16.000")}
    {linha("48 parcelas de R$ 2.044", "R$ 98.126")}
    {linha("Taxa", "1,9% ao mês", "média do Banco Central pra veículos (26,4% ao ano)")}
    <div class="dupla"></div>
    <div class="ln tot"><span>TOTAL PAGO</span><span class="pt"></span><span class="v">R$ 114.126</span></div>
  </div>
  <div class="abs carimbo stamp">+ R$ 34 MIL</div>
  <div class="abs nota n1">É a taxa média. Muita gente paga mais.</div>
"""),

    "04": dict(fundo="marinho", cab="Caminho 1 · os juros", pe="", css="""
.t1 { top: 150px; font-size: 130px; }
.k1 { left: 72px; top: 480px; transform: rotate(-2deg); padding: 14px 14px 18px; }
.k2 { left: 640px; top: 492px; transform: rotate(3deg); padding: 14px 14px 18px; }
.stamp { left: 640px; top: 560px; transform: rotate(-10deg); font-size: 64px; }
.mais { left: 576px; top: 610px; font: 900 80px/1 'Geist'; color: var(--creme); }
.p1 { left: 72px; top: 900px; font-size: 68px; }
""", corpo=f"""
  <div class="abs titulo t1"><span class="ac">R$ 34 mil</span><br>de juros.</div>
  <div class="abs cartao-foto k1">{cartao(470, 290, 520, -24, -112)}</div>
  <div class="abs mais">+</div>
  <div class="abs cartao-foto k2">{cartao(235, 290, 520, -24, -112)}</div>
  <div class="abs carimbo stamp">JUROS</div>
  <div class="abs serifa p1">Você paga um carro e meio<br>pra ter um.</div>
"""),

    "05": dict(fundo="papel", cab="Caminho 2 · consórcio", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.c1 { top: 410px; width: 936px; font-size: 36px; }
.roleta { left: 72px; top: 580px; width: 936px; display: grid; grid-template-columns: repeat(12, 1fr); gap: 6px; }
.roleta span { height: 50px; display: grid; place-items: center; background: var(--creme); font: 600 20px/1 'Geist Mono'; color: var(--mudo); }
.roleta .sorte { background: var(--laranja); color: var(--tinta); font-weight: 900; }
.leg { left: 72px; top: 880px; font: 500 21px/1 'Geist Mono'; letter-spacing: .1em; text-transform: uppercase; color: var(--mudo); }
.c2 { top: 930px; width: 936px; font-size: 40px; font-weight: 800; }
.n1 { top: 1100px; width: 936px; }
""", corpo=f"""
  <div class="abs titulo t1">Consórcio:<br>sem juros.</div>
  <div class="abs corpo c1">Mas com 20% de taxas, parcela que sobe todo ano e um sorteio que decide quando o carro chega.</div>
  {roleta()}
  <div class="abs leg">O seu carro pode sair em qualquer um desses meses.</div>
  <div class="abs corpo c2"><span class="marca">Paga como quem financia. Espera como quem junta. Sem saber quanto.</span></div>
  <div class="abs nota n1">60x a partir de R$ 1.600 · total R$ 103.993 · 18% de administração + 2% de fundo de reserva</div>
"""),

    "06": dict(fundo="marinho", cab="Caminho 3 · juntar", pe="", css="""
.t1 { top: 150px; font-size: 120px; }
.t1 .ac { color: var(--laranja); }
.c1 { top: 430px; width: 936px; font-size: 36px; }
.graf { left: 72px; top: 520px; }
.stamp { left: 690px; top: 560px; transform: rotate(-8deg); font-size: 54px; }
.rec { left: 72px; top: 900px; width: 936px; }
""", corpo=f"""
  <div class="abs titulo t1">Juntar:<br><span class="ac">28 meses.</span></div>
  <div class="abs corpo c1">R$ 16 mil + R$ 2.044 por mês, investidos a 0,8% ao mês.</div>
  {grafico_juntar()}
  <div class="abs carimbo stamp">À VISTA</div>
  <div class="abs recibo rec">
    {linha("Do seu bolso", "R$ 73.240")}
    {linha("Juros a seu favor", "+ R$ 10.632")}
    {linha("Desconto à vista", "5%")}
  </div>
"""),

    "07": dict(fundo="papel", cab="O placar", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.placar { left: 72px; top: 450px; width: 936px; display: flex; flex-direction: column; gap: 26px; }
.pl-cab { display: flex; justify-content: space-between; align-items: baseline; }
.pl-n { font: 600 24px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; }
.pl-t { font: 900 60px/1 'Geist'; letter-spacing: -0.04em; }
.pl:last-of-type .pl-t { color: var(--laranja); }
.pl svg { display: block; margin-top: 4px; }
.pl-leg { font: 500 19px/1 'Geist Mono'; color: var(--mudo); margin-top: 2px; }
.pl-eixo { display: flex; justify-content: space-between; font: 500 18px/1 'Geist Mono'; color: var(--mudo); border-top: 3px dotted var(--fio); padding-top: 12px; }
.p1 { left: 72px; top: 1060px; font-size: 60px; }
""", corpo=f"""
  <div class="abs titulo t1">O mesmo carro,<br>três preços.</div>
  {placar()}
  <div class="abs serifa p1">A diferença é quem recebe os juros.</div>
"""),

    "08": dict(fundo="marinho", cab="Os meses livres", pe="", css="""
.t1 { top: 150px; font-size: 120px; }
.c1 { top: 430px; width: 936px; font-size: 42px; }
.grande { left: 62px; top: 600px; font: 900 190px/1 'Geist'; letter-spacing: -0.06em; color: var(--laranja); white-space: nowrap; }
.grande small { font-size: 90px; letter-spacing: -0.04em; }
.n1 { top: 820px; width: 936px; font-size: 22px; }
.p1 { left: 72px; top: 920px; font-size: 64px; }
""", corpo="""
  <div class="abs titulo t1">Do mês 29<br>ao 48:</div>
  <div class="abs corpo c1">quem financiou ainda paga R$ 2.044. <b>Quem juntou, investe.</b></div>
  <div class="abs grande"><small>R$ </small>44.147</div>
  <div class="abs nota n1">20 meses × R$ 2.044 a 0,8% ao mês, no mês 48</div>
  <div class="abs serifa p1">Quem esperou já começou<br>o próximo carro.</div>
"""),

    "09": dict(fundo="papel", cab="Quando faz sentido", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.col { top: 430px; width: 444px; display: flex; flex-direction: column; gap: 20px; }
.col1 { left: 72px; } .col2 { left: 564px; }
.col h3 { margin: 0 0 6px; font: 600 20px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); padding-bottom: 14px; border-bottom: 3px dotted var(--fio); }
.col p { margin: 0; font: 500 31px/1.22 'Geist'; letter-spacing: -0.01em; display: flex; gap: 14px; }
.col p::before { content: '✓'; font-weight: 800; color: var(--laranja); }
.faixa { left: 72px; top: 900px; width: 936px; height: 230px; background: var(--marinho); color: var(--creme); padding: 34px 40px; }
.faixa .a { font: 600 24px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: rgba(251,244,232,.6); }
.faixa .b { font: 900 56px/1.1 'Geist'; letter-spacing: -0.035em; margin-top: 18px; }
""", corpo="""
  <div class="abs titulo t1">Nem sempre<br>juntar ganha.</div>
  <div class="abs col col1"><h3>Financiar, quando</h3>
    <p>o carro paga a parcela (trabalho, app)</p><p>a montadora dá taxa zero de verdade</p><p>é emergência e não há outro transporte</p></div>
  <div class="abs col col2"><h3>Consórcio, quando</h3>
    <p>você não consegue guardar sozinho</p><p>tem dinheiro pra dar lance</p><p>não tem pressa nenhuma</p></div>
  <div class="abs faixa"><div class="a">A regra</div><div class="b">Só pague juros por um carro que te dá dinheiro.</div></div>
"""),

    "10": dict(fundo="marinho", cab="A pergunta", pe="", css="""
.metade { left: 0; top: 0; width: 1080px; height: 680px; background: var(--laranja); }
.cabecalho, .fio { z-index: 2; }
.cabecalho { color: rgba(21,19,15,.7) !important; }
#grao { z-index: 3; }
.q { left: 72px; top: 170px; width: 936px; font: 800 92px/1.04 'Geist'; letter-spacing: -0.045em; color: var(--tinta); }
.p1 { left: 72px; top: 750px; font-size: 62px; width: 936px; }
.faixa { left: 72px; top: 1060px; width: 936px; height: 86px; background: var(--creme); color: var(--tinta); display: flex; align-items: center; gap: 16px; padding: 0 28px; font: 800 34px/1 'Geist'; letter-spacing: -0.02em; white-space: nowrap; }
.faixa b { background: var(--laranja); padding: 8px 14px; font-weight: 900; letter-spacing: .02em; }
""", corpo="""
  <div class="abs metade"></div>
  <div class="abs q">Quanto vale, pra você, ter o carro 28 meses antes?</div>
  <div class="abs serifa p1">Se a resposta for menos de R$ 41 mil, você já sabe o caminho.</div>
  <div class="abs faixa"><b>GRATUITO</b> Diagnóstico financeiro · link na bio</div>
"""),
}

for n, s in SLIDES.items():
    html = MOLDURA.format(n=n, **s)
    if n == "10":
        html = html.replace('class="abs fio" style="top:110px"', 'class="abs fio" style="top:110px; border-top-color: rgba(21,19,15,.3)"')
    (AQUI / f"slide-{n}.html").write_text(html, encoding="utf-8")
    print(f"src/slide-{n}.html")
