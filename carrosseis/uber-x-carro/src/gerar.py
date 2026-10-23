"""Gera src/slide-01.html a slide-10.html do carrossel Uber/99 x carro próprio.

Mesma moldura e peças do post do extrato (base.css, base.js); o hodômetro agora conta km por mês.
Números vêm do contas.py (mesmas premissas). Rode: python3 src/gerar.py
"""
from pathlib import Path

AQUI = Path(__file__).parent
CARRO = "../../carro-quitado/assets/kicks-papel.png"

FIXO, POR_KM, APP = 1887, 6.50 / 12 + 2400 / 12000, 2.50
VIRADA = round(FIXO / (APP - POR_KM))            # 1.073


def brl(v):
    return f"R$ {v:,.0f}".replace(",", ".")


MOLDURA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Slide {n} · Uber x carro</title>
<link rel="stylesheet" href="base.css">
<style>
.taxi {{ background: #0d0d0d; border-radius: 18px; padding: 22px 26px 26px; box-shadow: 0 24px 50px rgba(0,0,0,.3); color: #f4f1ea; }}
.taxi .rot {{ font: 500 20px/1.3 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: rgba(244,241,234,.6); }}
.taxi .dig {{ display: flex; gap: 6px; margin-top: 14px; align-items: flex-end; }}
.taxi .dig span {{ width: var(--w, 80px); height: var(--h, 112px); background: linear-gradient(#000 0%, #2a2a2a 50%, #000 100%); border-radius: 6px;
  font: 600 var(--f, 92px)/var(--h, 112px) 'Geist Mono'; text-align: center; }}
.taxi .dig span.sep {{ width: 26px; background: none; }}
.taxi .dig .un {{ width: auto; background: none; font: 500 30px/1 'Geist Mono'; color: rgba(244,241,234,.7); margin-left: 10px; padding-bottom: 12px; height: auto; }}
.marca {{ box-shadow: inset 0 -0.34em 0 rgba(242,81,31,.85); }}
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
  <div class="abs odometro">
    <div class="rot">Km<br>por mês</div>
    <div class="digitos" data-valor="{odo}"></div>
  </div>
  {pe}
  <div class="abs rodape">@victornaito.financas</div>
</div>
<script src="base.js"></script>
</body>
</html>
"""


def linha(rot, valor, sub=None):
    h = f'<div class="ln"><span>{rot}</span><span class="pt"></span><span class="v">{valor}</span></div>'
    return h + (f'<div class="sub">{sub}</div>' if sub else "")


def taxi(rotulo, valor, un="/km", w=80, h=112, f=92, extra=""):
    dig = "".join('<span class="sep">,</span>' if c == "," else f"<span>{c}</span>" for c in valor)
    return (f'<div class="rot">{rotulo}</div>{extra}'
            f'<div class="dig" style="--w:{w}px;--h:{h}px;--f:{f}px">{dig}<span class="un">{un}</span></div>')


def balanca():
    # trave inclinada pro lado do carro (o prato pesado desce)
    l, r = (150, 120), (786, 52)
    def prato(x, y, blocos, nome):
        s = f'<line x1="{x}" y1="{y}" x2="{x - 110}" y2="{y + 70}" stroke="#FBF4E8" stroke-width="3"/>'
        s += f'<line x1="{x}" y1="{y}" x2="{x + 110}" y2="{y + 70}" stroke="#FBF4E8" stroke-width="3"/>'
        s += f'<rect x="{x - 130}" y="{y + 70}" width="260" height="10" rx="5" fill="#FBF4E8"/>'
        topo = y + 70
        for alt, cor, txt, tc in blocos:
            topo -= alt + 4
            s += f'<rect x="{x - 115}" y="{topo}" width="230" height="{alt}" rx="6" fill="{cor}"/>'
            s += (f'<text x="{x}" y="{topo + alt / 2 + 9}" text-anchor="middle" font-family="Geist Mono" font-weight="600" '
                  f'font-size="24" letter-spacing="2" fill="{tc}">{txt}</text>')
        s += (f'<text x="{x}" y="{y + 124}" text-anchor="middle" font-family="Geist" font-weight="800" font-size="40" '
              f'fill="#FBF4E8">{nome}</text>')
        return s
    s = '<svg class="abs bal" width="936" height="420" viewBox="0 0 936 420">'
    s += '<polygon points="468,380 418,410 518,410" fill="#FBF4E8"/>'
    s += '<rect x="463" y="90" width="10" height="295" fill="#FBF4E8"/>'
    s += f'<line x1="{l[0]}" y1="{l[1]}" x2="{r[0]}" y2="{r[1]}" stroke="#FBF4E8" stroke-width="10" stroke-linecap="round"/>'
    s += '<circle cx="468" cy="86" r="12" fill="#F2511F"/>'
    s += prato(l[0], l[1], [(96, "#F2511F", "PARTE FIXA", "#15130F"), (44, "#FBF4E8", "POR KM", "#15130F")], "CARRO")
    s += prato(r[0], r[1], [(44, "#FBF4E8", "POR KM", "#15130F")], "APP")
    return s + "</svg>"


def grafico():
    W, H = 936, 690
    x0, x1, y0, y1 = 150, 900, 30, 610          # área de plotagem
    KM, RS = 2000, 5000
    X = lambda km: x0 + (x1 - x0) * km / KM
    Y = lambda v: y1 - (y1 - y0) * v / RS
    car = lambda km: FIXO + POR_KM * km
    s = f'<svg class="abs graf" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
    # áreas: até a virada o app ganha (entre as retas), depois o carro
    s += (f'<polygon points="{X(0)},{Y(car(0))} {X(VIRADA)},{Y(car(VIRADA))} {X(0)},{Y(0)}" fill="#F2511F" fill-opacity=".16"/>')
    s += (f'<polygon points="{X(VIRADA)},{Y(car(VIRADA))} {X(KM)},{Y(APP * KM)} {X(KM)},{Y(car(KM))}" fill="#FBF4E8" fill-opacity=".10"/>')
    for v in range(0, RS + 1, 1000):
        s += f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="#FBF4E8" stroke-opacity=".12" stroke-width="2"/>'
        rot = "R$ 0" if v == 0 else f"R$ {v // 1000} mil"
        s += (f'<text x="{x0 - 14}" y="{Y(v) + 8}" text-anchor="end" font-family="Geist Mono" font-size="22" '
              f'fill="#FBF4E8" fill-opacity=".6">{rot}</text>')
    for km in range(0, KM + 1, 500):
        rot = f"{km:,}".replace(",", ".")
        s += (f'<text x="{X(km)}" y="{y1 + 40}" text-anchor="middle" font-family="Geist Mono" font-size="22" '
              f'fill="#FBF4E8" fill-opacity=".6">{rot}</text>')
    s += (f'<text x="{x1}" y="{y1 + 76}" text-anchor="end" font-family="Geist Mono" font-size="20" letter-spacing="3" '
          f'fill="#FBF4E8" fill-opacity=".6">KM POR MÊS</text>')
    s += f'<line x1="{X(0)}" y1="{Y(car(0))}" x2="{X(KM)}" y2="{Y(car(KM))}" stroke="#FBF4E8" stroke-width="8" stroke-linecap="round"/>'
    s += f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(KM)}" y2="{Y(APP * KM)}" stroke="#F2511F" stroke-width="8" stroke-linecap="round"/>'
    s += (f'<text x="{X(KM) - 6}" y="{Y(car(KM)) + 46}" text-anchor="end" font-family="Geist" font-weight="800" font-size="30" '
          f'fill="#FBF4E8">CARRO</text>')
    s += (f'<text x="{X(1820)}" y="{Y(APP * 1820) - 10}" text-anchor="end" font-family="Geist" font-weight="800" font-size="30" '
          f'fill="#F2511F">APP</text>')
    s += (f'<text x="{X(190)}" y="{Y(900)}" font-family="Geist Mono" font-size="22" letter-spacing="2" '
          f'fill="#FBF4E8" fill-opacity=".85">AQUI O APP GANHA</text>')
    s += (f'<text x="{X(1240)}" y="{Y(3700)}" font-family="Geist Mono" font-size="22" letter-spacing="2" '
          f'fill="#FBF4E8" fill-opacity=".85">AQUI O CARRO GANHA</text>')
    cx, cy = X(VIRADA), Y(car(VIRADA))
    s += f'<line x1="{cx}" x2="{cx}" y1="{cy}" y2="{y1}" stroke="#F2511F" stroke-width="3" stroke-dasharray="8 8"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="20" fill="#181D26" stroke="#F2511F" stroke-width="7"/>'
    s += f'<rect x="{cx - 330}" y="{cy - 112}" width="300" height="66" rx="8" fill="#FBF4E8"/>'
    s += (f'<text x="{cx - 180}" y="{cy - 68}" text-anchor="middle" font-family="Geist" font-weight="800" font-size="30" '
          f'fill="#15130F">1.073 km · {brl(car(VIRADA))}</text>')
    return s + "</svg>"


def mapa():
    s = '<svg class="abs mapa" width="936" height="400" viewBox="0 0 936 400">'
    ruas = [(0, 60, 936, 90), (0, 190, 936, 160), (0, 330, 936, 300), (130, 0, 170, 400), (400, 0, 360, 400),
            (620, 0, 660, 400), (820, 0, 790, 400)]
    for a, b, c, d in ruas:
        s += f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#FBF4E8" stroke-opacity=".12" stroke-width="14" stroke-linecap="round"/>'
    rota = "M120 320 C 250 320, 260 200, 400 190 S 600 120, 650 110 S 780 70, 820 80"
    s += f'<path d="{rota}" fill="none" stroke="#F2511F" stroke-width="9" stroke-linecap="round"/>'
    for x, y, nome, anc, dy in ((120, 320, "CASA", "start", 52), (820, 80, "TRABALHO", "end", -30)):
        s += f'<circle cx="{x}" cy="{y}" r="18" fill="#FBF4E8" stroke="#F2511F" stroke-width="7"/>'
        s += (f'<text x="{x}" y="{y + dy}" text-anchor="{anc}" font-family="Geist Mono" font-weight="600" font-size="24" '
              f'letter-spacing="3" fill="#FBF4E8">{nome}</text>')
    s += '<rect x="372" y="210" width="150" height="56" rx="28" fill="#FBF4E8"/>'
    s += '<text x="447" y="248" text-anchor="middle" font-family="Geist" font-weight="900" font-size="30" fill="#15130F">24 km</text>'
    s += '<rect x="560" y="250" width="330" height="56" rx="28" fill="none" stroke="#FBF4E8" stroke-width="3"/>'
    s += ('<text x="725" y="287" text-anchor="middle" font-family="Geist Mono" font-weight="600" font-size="22" '
          'letter-spacing="1" fill="#FBF4E8">× 2 × 22 DIAS ÚTEIS</text>')
    return s + "</svg>"


def tabela():
    linhas = [(300, "home office"), (600, ""), (1000, "o do extrato"), (1500, ""), (2000, "")]
    s = '<div class="abs tab">'
    s += '<div class="th"><span>km/mês</span><span>carro</span><span>app</span><span>quem ganha</span></div>'
    for km, obs in linhas:
        carro, app = FIXO + POR_KM * km, APP * km
        dif = carro - app
        selo = (f'<span class="selo app">APP · {brl(dif)}</span>' if dif > 0
                else f'<span class="selo car">CARRO · {brl(-dif)}</span>')
        kms = f"{km:,}".replace(",", ".")
        cls = "tr destaque" if km == 1000 else "tr"
        s += (f'<div class="{cls}"><span class="km">{kms}<small>{obs}</small></span><span class="rs">{brl(carro)}</span>'
              f'<span class="rs">{brl(app)}</span>{selo}</div>')
    return s + "</div>"


SLIDES = {
    "01": dict(fundo="papel", cab="Uber/99 × carro próprio", odo="1.073",
               pe='<div class="abs seta" id="seta">Fazer a conta ▸</div><script src="vivo-01.js" defer></script>', css="""
.riscada { left: 72px; top: 150px; font: 800 66px/1 'Geist'; letter-spacing: -0.04em; color: var(--mudo); }
.riscada span { position: relative; }
.riscada span::after { content: ''; position: absolute; left: -10px; right: -12px; top: 54%; height: 7px; margin-top: -3px;
  background: var(--laranja); border-radius: 6px; transform: rotate(-2.2deg); clip-path: inset(-4px var(--corte, 0%) -4px 0); }
.abaixo { left: 72px; top: 262px; font: 800 66px/1 'Geist'; letter-spacing: -0.04em; }
.numero .rolo { display: inline-block; height: 1em; vertical-align: top; clip-path: inset(.11em -.3em .1em -.3em); }
.numero .rolo:nth-of-type(1) { margin-right: -.08em; } .numero .rolo:nth-of-type(2) { margin-right: -.03em; } .numero .rolo:nth-of-type(3) { margin-right: -.06em; }
.numero .fita { display: block; } .numero .fita span { display: block; height: 1em; }
#km { display: inline-block; transform-origin: 50% 100%; }
#pormes { overflow: hidden; padding: .1em .15em .3em .2em; margin: -.1em 0 0 -.2em; }
#pormes .dentro { display: inline-block; transform-origin: 50% 100%; }
.numero { left: 62px; top: 330px; font-weight: 900; font-size: 250px; letter-spacing: -0.06em; line-height: 1; white-space: nowrap; }
.numero small { font-size: 130px; letter-spacing: -0.04em; margin-left: 18px; }
.p1 { left: 72px; top: 590px; font-size: 76px; }
.car { left: 110px; top: 498px; width: 880px; }
.cordao { left: 432px; top: 812px; width: 4px; height: 70px; background: var(--tinta); transform: rotate(12deg); transform-origin: top center; }
.etiqueta { left: 250px; top: 872px; transform: rotate(5deg); transform-origin: 182px -60px; background: var(--laranja); color: var(--tinta);
  padding: 16px 30px 16px 58px; font: 900 40px/1 'Geist'; letter-spacing: -0.02em; white-space: nowrap;
  clip-path: polygon(30px 0, 100% 0, 100% 100%, 30px 100%, 0 50%); }
.etiqueta::before { content: ''; position: absolute; left: 26px; top: 50%; width: 14px; height: 14px; margin-top: -7px; border-radius: 50%; background: var(--papel); }
.seta { left: 560px; top: 1226px; font: 600 22px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--tinta); }
""", corpo=f"""
  <div class="abs riscada"><span id="risco">Você acha o Uber caro.</span></div>
  <div class="abs abaixo">Abaixo de</div>
  <div class="abs numero" id="numero"><span class="rolo">1</span>.<span class="rolo">0</span><span class="rolo">7</span><span class="rolo">3</span><small id="km">km</small></div>
  <div class="abs serifa p1" id="pormes"><span class="dentro">por mês, caro é o seu carro.</span></div>
  <img class="abs carro-papel car" id="carro" src="{CARRO}" alt="">
  <div class="abs cordao" id="cordao"></div>
  <div class="abs etiqueta" id="etiqueta">PARADO · R$ 1.887/mês</div>
"""),

    "02": dict(fundo="marinho", cab="A conta", odo="0.000", pe="", css="""
.t1 { top: 150px; font-size: 120px; }
.bal { left: 72px; top: 420px; }
.c1 { top: 870px; width: 936px; }
.c2 { top: 1036px; width: 936px; font-weight: 800; }
""", corpo=f"""
  <div class="abs titulo t1">A conta tem<br>duas partes.</div>
  {balanca()}
  <div class="abs corpo c1">O carro te cobra antes de andar.<br>O app só cobra quando você anda.</div>
  <div class="abs corpo c2"><span class="marca">Em algum km, os dois custam igual.</span></div>
"""),

    "03": dict(fundo="papel", cab="Parte fixa · o carro parado", odo="0.000", pe="", css="""
.t1 { top: 150px; font-size: 100px; }
.car { left: 500px; top: 318px; width: 540px; }
.stamp { left: 590px; top: 520px; transform: rotate(-8deg); font-size: 76px; }
.rec { left: 72px; top: 760px; width: 936px; }
.n1 { top: 1110px; }
""", corpo=f"""
  <div class="abs titulo t1">R$ 1.887 antes de<br>girar a chave.</div>
  <img class="abs carro-papel car" src="{CARRO}" alt="">
  <div class="abs carimbo stamp">PARADO</div>
  <div class="abs recibo rec">
    {linha("IPVA + licenciamento", "R$ 280")}
    {linha("Seguro", "R$ 300")}
    {linha("Depreciação", "R$ 667")}
    {linha("Dinheiro parado no carro", "R$ 640")}
    <div class="div"></div>
    <div class="ln tot"><span>PARTE FIXA / MÊS</span><span class="pt"></span><span class="v">R$ 1.887</span></div>
  </div>
  <div class="abs nota n1">Os quatro números do post do extrato. Chegam rodando ou não.</div>
"""),

    "04": dict(fundo="marinho", cab="Parte por km · carro", odo="0.000", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.t1 .ac { color: var(--laranja); }
.tx { left: 72px; top: 440px; }
.rec { left: 72px; top: 720px; width: 936px; }
.c1 { top: 1000px; width: 936px; font-size: 40px; }
.circ { position: relative; white-space: nowrap; }
.circ::after { content: ''; position: absolute; left: -16px; right: -16px; top: -10px; bottom: -8px; border: 4px solid var(--laranja); border-radius: 50%; transform: rotate(-3deg); }
""", corpo=f"""
  <div class="abs titulo t1">Cada km de carro:<br><span class="ac">R$ 0,74.</span></div>
  <div class="abs taxi tx">{taxi("Carro · R$ por km", "0,74")}</div>
  <div class="abs recibo rec">
    {linha("Combustível", "R$ 0,54", "12 km/l a R$ 6,50")}
    {linha("Manutenção", "R$ 0,20", "pneu, revisão, freio")}
  </div>
  <div class="abs corpo c1">Parece barato. A pegadinha:<br>os <b class="circ">R$ 1.887</b> já foram antes.</div>
"""),

    "05": dict(fundo="papel", cab="Parte por km · app", odo="0.000", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.t1 .ac { color: var(--laranja); }
.tx1 { left: 72px; top: 440px; width: 444px; }
.tx2 { left: 564px; top: 440px; width: 444px; box-shadow: 0 0 0 6px var(--laranja), 0 24px 50px rgba(0,0,0,.3); }
.taxi .ini { font: 500 22px/1.3 'Geist Mono'; color: #f4f1ea; margin-top: 10px; }
.taxi .ini b { font-weight: 700; }
.c1 { top: 790px; width: 936px; font-size: 44px; font-weight: 800; }
.p1 { left: 72px; top: 870px; font-size: 76px; }
.n1 { top: 1090px; width: 936px; }
""", corpo=f"""
  <div class="abs titulo t1">Cada km de app:<br><span class="ac">R$ 2,50.</span></div>
  <div class="abs taxi tx1">{taxi("Carro", "0,74", w=64, h=96, f=78, extra='<div class="ini">começa em <b>R$ 1.887</b></div>')}</div>
  <div class="abs taxi tx2">{taxi("App", "2,50", w=64, h=96, f=78, extra='<div class="ini">começa em <b>R$ 0</b></div>')}</div>
  <div class="abs corpo c1">O app é 3 vezes mais caro por km.</div>
  <div class="abs serifa p1">Mas começa do zero.</div>
  <div class="abs nota n1">Média de corrida urbana com tarifa base e tempo. Confira no app da sua cidade.</div>
"""),

    "06": dict(fundo="marinho", cab="A virada", odo="1.073", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.p1 { left: 72px; top: 284px; font-size: 54px; }
.graf { left: 72px; top: 420px; }
""", corpo=f"""
  <div class="abs titulo t1">1.073 km por mês.</div>
  <div class="abs serifa p1">É aqui que o carro começa a compensar.</div>
  {grafico()}
"""),

    "07": dict(fundo="papel", cab="Cenários", odo="1.073", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.tab { left: 72px; top: 330px; width: 936px; }
.tab .th, .tab .tr { display: grid; grid-template-columns: 210px 190px 190px 1fr; align-items: center; column-gap: 12px; }
.tab .th { font: 500 19px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); padding: 0 20px 18px; border-bottom: 3px dotted var(--fio); }
.tab .tr { height: 132px; padding: 0 20px; border-bottom: 3px dotted var(--fio); }
.tab .tr.destaque { border: 5px solid var(--laranja); border-radius: 14px; transform: rotate(-.6deg); }
.tab .km { font: 800 58px/1 'Geist'; letter-spacing: -0.04em; display: flex; flex-direction: column; gap: 8px; }
.tab .km small { font: 500 17px/1 'Geist Mono'; letter-spacing: .08em; color: var(--mudo); text-transform: uppercase; }
.tab .rs { font: 600 30px/1 'Geist Mono'; }
.selo { justify-self: start; padding: 14px 18px; border-radius: 999px; font: 800 26px/1 'Geist'; letter-spacing: -0.01em; white-space: nowrap; }
.selo.app { background: var(--laranja); color: var(--tinta); }
.selo.car { background: var(--marinho); color: var(--creme); }
.c1 { top: 1066px; width: 936px; font-size: 32px; }
""", corpo=f"""
  <div class="abs titulo t1">Ache a sua linha.</div>
  {tabela()}
  <div class="abs corpo c1">Rodando 1.000 km, o número do post do extrato, <b>o app ainda ganha.</b></div>
"""),

    "08": dict(fundo="marinho", cab="Traduzindo", odo="1.073", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.mapa { left: 72px; top: 430px; }
.c1 { top: 870px; width: 936px; }
.c2 { top: 1050px; width: 936px; font-weight: 800; font-size: 40px; }
""", corpo=f"""
  <div class="abs titulo t1">1.073 km =<br>36 km por dia.</div>
  {mapa()}
  <div class="abs corpo c1">É ir e voltar de um trabalho a 24 km de casa, todo dia útil. E não usar o carro pra mais nada.</div>
  <div class="abs corpo c2"><span class="marca">Se o seu trajeto é menor, a conta já deu.</span></div>
"""),

    "09": dict(fundo="papel", cab="O que a conta não pega", odo="1.073", pe="", css="""
.t1 { top: 150px; font-size: 112px; }
.col { top: 420px; width: 444px; display: flex; flex-direction: column; gap: 20px; }
.col1 { left: 72px; } .col2 { left: 564px; }
.col h3 { margin: 0 0 6px; font: 600 20px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); padding-bottom: 14px; border-bottom: 3px dotted var(--fio); }
.col p { margin: 0; font: 500 31px/1.22 'Geist'; letter-spacing: -0.01em; display: flex; gap: 14px; }
.col p::before { content: '✓'; font-weight: 800; color: var(--laranja); }
.faixa { left: 72px; top: 930px; width: 936px; height: 200px; background: var(--marinho); color: var(--creme); padding: 34px 40px; }
.faixa .a { font: 500 34px/1.2 'Geist'; }
.faixa .b { font: 900 72px/1.1 'Geist'; letter-spacing: -0.04em; margin-top: 10px; }
""", corpo="""
  <div class="abs titulo t1">Antes de vender<br>o carro.</div>
  <div class="abs col col1"><h3>Pesa pro carro</h3>
    <p>filho e cadeirinha</p><p>viagem de estrada</p><p>cidade com pouco app</p><p>dinâmica de 1,5x: o ponto cai pra 627 km</p></div>
  <div class="abs col col2"><h3>Pesa pro app</h3>
    <p>estacionamento e Zona Azul</p><p>multa</p><p>dirigir cansado ou depois de beber</p><p>tempo livre no trajeto</p></div>
  <div class="abs faixa"><div class="a">Só o rendimento dos R$ 80 mil paga</div><div class="b"><span class="marca">256 km de app</span> por mês.</div></div>
"""),

    "10": dict(fundo="marinho", cab="O seu número", odo="1.073", pe="", css="""
.metade { left: 0; top: 0; width: 1080px; height: 660px; background: var(--laranja); }
.cabecalho, .fio { z-index: 2; }
.cabecalho { color: rgba(21,19,15,.7) !important; }
.fio.topo { border-top-color: rgba(21,19,15,.3) !important; }
#grao { z-index: 3; }
.v { left: 72px; width: 936px; color: var(--tinta); }
.v .h { font: 800 62px/1 'Geist'; letter-spacing: -0.04em; }
.v .d { font: 500 42px/1.2 'Geist'; letter-spacing: -0.015em; margin-top: 14px; }
.v1 { top: 168px; } .v2 { top: 430px; }
.p1 { left: 72px; top: 730px; font-size: 76px; }
.cta { left: 72px; top: 1060px; width: 936px; height: 80px; background: var(--creme); color: var(--tinta); display: flex; align-items: center; padding: 0 28px; gap: 12px; font: 700 30px/1 'Geist'; letter-spacing: -0.015em; white-space: nowrap; }
.cta b { font-weight: 900; background: var(--laranja); padding: 8px 14px; letter-spacing: .04em; }
""", corpo="""
  <div class="abs metade"></div>
  <div class="abs v v1"><div class="h">Abaixo do seu ponto de virada:</div><div class="d">o carro é conforto. Pode valer, mas tem preço.</div></div>
  <div class="abs v v2"><div class="h">Acima:</div><div class="d">o carro é economia.</div></div>
  <div class="abs serifa p1">Não existe resposta certa.<br>Existe o seu número.</div>
  <div class="abs cta">Você roda o suficiente pro seu carro valer o que ele te cobra?</div>
"""),
}

for n, s in SLIDES.items():
    html = MOLDURA.format(n=n, **s)
    if n == "10":
        html = html.replace('class="abs fio" style="top:110px"', 'class="abs fio topo" style="top:110px"')
    (AQUI / f"slide-{n}.html").write_text(html, encoding="utf-8")
    print(f"src/slide-{n}.html")
