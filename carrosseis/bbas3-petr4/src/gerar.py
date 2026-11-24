#!/usr/bin/env python3
"""Gera src/slide-01.html a slide-10.html do carrossel "Banco do Brasil e Petrobras: comprar ou não?".
Números em DADOS (fontes no ../BRIEF.md). Visual em base.css (o mesmo dos outros carrosséis da conta).
Uso: python3 src/gerar.py && NODE_PATH=$(npm root -g) node src/render.mjs && python3 src/folha.py"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
TRI = ['4T25', '1T26', '2T26', '3T26']
PETR = [15.56, 32.7, 52.4, 39.8]   # lucro líquido, R$ bi
BBAS = [5.74, 3.4, 3.9, 1.27]      # lucro líquido ajustado, R$ bi
CORP, CORB = '#FF5A47', '#F4EEE2'

def pagina(n, corpo, css='', classe='', semente=7, extra=''):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>slide {n:02d}</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div id="quadro" class="{classe}" data-n="{n:02d}" data-total="10" data-semente="{semente}" {extra}>
<div class="conteudo">{corpo}</div></div>
<script src="ilustras.js"></script><script src="ilustras-acoes.js"></script><script src="base.js"></script></body></html>
"""

def br(v, d=1):
    return f'{v:.{d}f}'.replace('.', ',')

def barras(vals, cor, topo, w=936, h=430, rotulo=lambda v: 'R$ ' + br(v)):
    """Barras verticais, uma por trimestre, escala própria (0 a topo)."""
    n = len(vals); larg = 150; passo = w / n; svg = []
    for i, v in enumerate(vals):
        x = passo * i + (passo - larg) / 2; bh = v / topo * h; y = h - bh
        ult = i == n - 1
        svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{larg}" height="{bh:.0f}" rx="14" fill="{cor}" opacity="{1 if ult else .55}"/>')
        svg.append(f'<text x="{x + larg / 2:.0f}" y="{y - 22:.0f}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="{44 if ult else 36}" fill="#fff">{rotulo(v)}</text>')
        svg.append(f'<text x="{x + larg / 2:.0f}" y="{h + 48}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="28" fill="rgba(255,255,255,.62)">{TRI[i]}</text>')
    return f'<svg viewBox="0 0 {w} {h + 60}" width="{w}" height="{h + 60}" style="display:block;overflow:visible"><line x1="0" y1="{h}" x2="{w}" y2="{h}" stroke="rgba(255,255,255,.25)" stroke-width="2"/>{"".join(svg)}</svg>'

S = {}

# 1 · CAPA ------------------------------------------------------------------------------------------
S[1] = dict(semente=17, css="""
.luz { left: 60px; top: 20px; width: 960px; height: 760px; background: radial-gradient(closest-side, rgba(255,186,120,.22), rgba(255,186,120,0)); }
.piso { left: 0; right: 0; top: 650px; height: 150px; background: linear-gradient(180deg, rgba(255,255,255,.07), rgba(255,255,255,0)); }
.palco { left: 72px; right: 72px; top: 150px; height: 520px; display: flex; align-items: flex-end; justify-content: center; gap: 70px; }
.palco .tk { text-align: center; }
.palco .tk .pilula { width: 210px; height: 66px; font-size: 34px; margin-top: 18px; }
.vs { left: 0; right: 0; top: 390px; text-align: center; font: 400 70px/1 'Anton'; color: rgba(255,255,255,.4); }
.manchete { top: 770px; }
.manchete .anton { line-height: 1.12; }
""", corpo="""
<div class="abs luz"></div><div class="abs piso"></div>
<div class="abs palco">
  <div class="tk"><div data-il="banco" style="width:300px"></div><div class="pilula" style="background:linear-gradient(180deg,#F4EEE2,#D9D1C1);color:#15130F">BBAS3</div></div>
  <div class="tk"><div data-il="barril" style="width:230px"></div><div class="pilula">PETR4</div></div>
</div>
<div class="col manchete">
  <div class="anton" data-fit="936" style="color:var(--coral)">Banco do Brasil e Petrobras:</div>
  <div class="anton" data-fit="936">comprar, manter ou vender?</div>
  <div class="anton" data-fit="936" style="color:rgba(255,255,255,.72)">O que os 4 últimos balanços mostram.</div>
</div>
""")

# 2 · HOLD ------------------------------------------------------------------------------------------
p9, b9 = sum(PETR[1:]), sum(BBAS[1:])
S[2] = dict(semente=23, css="""
.par { left: 72px; right: 72px; top: 348px; display: grid; grid-template-columns: repeat(2, 456px); gap: 24px; }
.par .vidro { height: 520px; display: flex; flex-direction: column; align-items: center; padding: 32px 26px; text-align: center; }
.par .ic { height: 180px; display: flex; align-items: flex-end; }
.par .caps { font-size: 24px; color: rgba(255,255,255,.78); margin-top: 22px; }
.par .num { font: 800 68px/1 'Montserrat'; letter-spacing: -0.045em; margin-top: 18px; }
.par .sub { font: 500 28px/1.3 'Montserrat'; color: rgba(255,255,255,.75); margin-top: 16px; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">Duas estatais.<br><span class="c">Dois anos opostos.</span></div>
</div>
<div class="abs par">
  <div class="vidro"><div class="ic"><div data-il="barril" style="width:140px"></div></div>
    <div class="caps">Petrobras · lucro em 2026</div><div class="num c">R$ {br(p9)} bi</div><div class="sub">de janeiro a setembro</div></div>
  <div class="vidro"><div class="ic"><div data-il="banco" style="width:190px"></div></div>
    <div class="caps">Banco do Brasil · lucro em 2026</div><div class="num">R$ {br(b9)} bi</div><div class="sub">de janeiro a setembro</div></div>
</div>
<div class="col" style="top:930px">
  <div class="corpo">Uma bateu recorde de produção. O outro levou o calote do agro pro balanço.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:28px">Os números, <span class="traco">trimestre a trimestre.</span></div>
</div>
""")

# 3 · PETROBRAS: 4 trimestres ---------------------------------------------------------------------------
S[3] = dict(semente=31, css=".graf { left: 72px; top: 400px; }", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">Petrobras:<br><span class="c">o lucro voltou forte.</span></div>
  <div class="caps" style="color:var(--mudo);margin-top:26px">Lucro líquido por trimestre · R$ bilhões</div>
</div>
<div class="abs graf">{barras(PETR, CORP, 60)}</div>
<div class="col" style="top:960px">
  <div class="corpo" style="font-size:38px">O 2T26 teve petróleo caro. No 3T26, o barril caiu e a produção recorde (2,83 milhões/dia) segurou o lucro.</div>
  <div class="corpo forte" style="font-size:44px;margin-top:26px">+ R$ 15,3 bi em dividendos <span class="c">do 3T26.</span></div>
</div>
""")

# 4 · BB: 4 trimestres ---------------------------------------------------------------------------------
S[4] = dict(semente=37, css=".graf { left: 72px; top: 400px; }", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">Banco do Brasil:<br><span class="c">lucro caiu 78%.</span></div>
  <div class="caps" style="color:var(--mudo);margin-top:26px">Lucro líquido ajustado por trimestre · R$ bilhões</div>
</div>
<div class="abs graf">{barras(BBAS, CORB, 7, rotulo=lambda v: 'R$ ' + br(v, 2 if v < 2 else 1))}</div>
<div class="col" style="top:960px">
  <div class="corpo" style="font-size:38px">Inadimplência do agro foi a 6,92%. O retorno sobre o patrimônio (ROE) caiu pra 2,8%.</div>
  <div class="corpo forte" style="font-size:44px;margin-top:26px">O problema tem nome: <span class="marca">calote no agro.</span></div>
</div>
""")

# 5 · LADO A LADO, mesma escala ----------------------------------------------------------------------------
def lado_a_lado(w=936, h=440, topo=60):
    passo = w / 4; lb = 92; svg = []
    for i in range(4):
        x0 = passo * i + (passo - 2 * lb - 12) / 2
        for j, (v, cor) in enumerate([(PETR[i], CORP), (BBAS[i], CORB)]):
            x = x0 + j * (lb + 12); bh = max(v / topo * h, 4); y = h - bh
            svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{lb}" height="{bh:.0f}" rx="10" fill="{cor}"/>')
            svg.append(f'<text x="{x + lb / 2:.0f}" y="{y - 14:.0f}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="27" fill="#fff">{br(v)}</text>')
        svg.append(f'<text x="{x0 + lb + 6:.0f}" y="{h + 46}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="28" fill="rgba(255,255,255,.62)">{TRI[i]}</text>')
    return f'<svg viewBox="0 0 {w} {h + 60}" width="{w}" height="{h + 60}" style="display:block;overflow:visible"><line x1="0" y1="{h}" x2="{w}" y2="{h}" stroke="rgba(255,255,255,.25)" stroke-width="2"/>{"".join(svg)}</svg>'

S[5] = dict(semente=43, css="""
.graf { left: 72px; top: 450px; }
.leg { left: 72px; top: 372px; display: flex; gap: 40px; font: 700 28px/1 'Montserrat'; }
.leg span { display: flex; align-items: center; gap: 12px; } .leg i { width: 28px; height: 28px; border-radius: 7px; display: block; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">Lado a lado,<br><span class="c">na mesma régua.</span></div>
</div>
<div class="abs leg"><span><i style="background:{CORP}"></i>Petrobras</span><span><i style="background:{CORB}"></i>Banco do Brasil</span><span style="color:var(--mudo);font-weight:600">R$ bi por trimestre</span></div>
<div class="abs graf">{lado_a_lado()}</div>
<div class="col" style="top:1010px">
  <div class="corpo forte" style="font-size:46px;line-height:1.3">A Petrobras lucrou num trimestre<br><span class="marca">4,6× o que o BB lucrou em 9 meses.</span></div>
</div>
""")

# 6 · PLANO PETROBRAS -----------------------------------------------------------------------------------------
itens_p = [('US$ 122 bi', 'de investimento de 2027 a 2031, mais de 70% em exploração e produção'),
           ('3,2 milhões', 'de barris de óleo e gás por dia a partir de 2028 (hoje: 2,83)'),
           ('US$ 55 a 60 bi', 'em dividendos ordinários no período. Regra: 45% do fluxo de caixa livre'),
           ('R$ 15,6 bi', 'em dividendos extraordinários aprovados agora, pagos em dezembro')]
S[6] = dict(semente=53, css="""
.lista { left: 72px; right: 72px; top: 330px; display: flex; flex-direction: column; gap: 20px; }
.lista .vidro { height: 168px; display: grid; grid-template-columns: 330px 1fr; align-items: center; padding: 0 30px; gap: 20px; }
.lista .k { font: 800 44px/1 'Montserrat'; white-space: nowrap; letter-spacing: -0.04em; color: var(--coral); }
.lista .d { font: 500 30px/1.28 'Montserrat'; color: rgba(255,255,255,.88); }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">O plano da Petrobras<br><span class="c">até 2031.</span></div>
</div>
<div class="abs lista">{''.join(f'<div class="vidro"><div class="k">{k}</div><div class="d">{d}</div></div>' for k, d in itens_p)}</div>
<div class="col" style="top:1100px">
  <div class="corpo forte" style="font-size:42px">Mais petróleo, dívida no teto e <span class="traco">dividendo com regra.</span></div>
</div>
""")

# 7 · PLANO BB -------------------------------------------------------------------------------------------------
S[7] = dict(semente=59, css="""
.antesdep { left: 72px; right: 72px; top: 330px; display: grid; grid-template-columns: repeat(2, 456px); gap: 24px; }
.antesdep .vidro { height: 320px; padding: 34px 32px; display: flex; flex-direction: column; justify-content: space-between; }
.antesdep .caps { font-size: 23px; color: rgba(255,255,255,.75); }
.antesdep .de { font: 700 40px/1 'Montserrat'; color: rgba(255,255,255,.45); text-decoration: line-through; text-decoration-color: var(--coral-forma); text-decoration-thickness: 4px; }
.antesdep .por { font: 800 56px/1 'Montserrat'; letter-spacing: -0.045em; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">O plano do BB:<br><span class="c">atravessar 2026.</span></div>
</div>
<div class="abs antesdep">
  <div class="vidro"><div class="caps">Lucro previsto pra 2026</div><div class="de">R$ 18 a 22 bi</div><div class="por">R$ 9 a 11 bi</div></div>
  <div class="vidro"><div class="caps">Dividendos · % do lucro</div><div class="de">30%</div><div class="por c">25% (mínimo)</div></div>
</div>
<div class="col" style="top:710px">
  <div class="corpo" style="font-size:38px">Dividendo intermediário suspenso. Mais provisão pra calote até dezembro. Renegociação das dívidas rurais andando devagar.</div>
  <div class="corpo" style="font-size:38px;margin-top:24px">Não tem plano de crescimento na mesa. Tem plano de <b>limpar o balanço.</b></div>
  <div class="corpo forte" style="font-size:44px;margin-top:30px;line-height:1.3">A virada depende de uma coisa:<br><span class="elipse c">o agro voltar a pagar.</span></div>
</div>
""")

# 8 · 3 MOTIVOS PETROBRAS ------------------------------------------------------------------------------------
def motivos(lista):
    return ''.join(f'<div class="vidro"><div class="n">{i + 1}</div><div><div class="t">{t}</div><div class="d">{d}</div></div></div>' for i, (t, d) in enumerate(lista))
CSS_M = """
.lista { left: 72px; right: 72px; top: 330px; display: flex; flex-direction: column; gap: 22px; }
.lista .vidro { height: 184px; display: grid; grid-template-columns: 122px 1fr; align-items: center; padding: 0 30px 0 26px; }
.lista .n { width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 400 56px/1 'Anton';
  background: linear-gradient(180deg, #E8503C, #C93524); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.38); }
.lista .t { font: 800 40px/1.1 'Montserrat'; letter-spacing: -0.025em; }
.lista .d { font: 500 29px/1.3 'Montserrat'; color: rgba(255,255,255,.82); margin-top: 8px; }
.risco { left: 72px; right: 72px; top: 958px; padding: 26px 30px; border-radius: var(--raio); border: 2px dashed rgba(255,255,255,.3); }
.risco .caps { font-size: 22px; color: var(--coral); }
.risco .corpo { font-size: 32px; margin-top: 10px; }
"""
S[8] = dict(semente=61, css=CSS_M, corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">3 motivos pra<br><span class="c">comprar Petrobras.</span></div>
</div>
<div class="abs lista">{motivos([
  ('Produção em alta', 'Recorde de 2,83 milhões de barris/dia. O plano leva a 3,2 milhões.'),
  ('Dividendo com fórmula', '45% do caixa livre. US$ 55 a 60 bi previstos até 2031.'),
  ('Dívida controlada', 'Dívida líquida de 1× o EBITDA. Teto de US$ 75 bi no plano.')])}</div>
<div class="abs risco"><div class="caps">O que pode dar errado</div>
  <div class="corpo">Petróleo barato derruba o caixa e o dividendo. E é estatal: o governo pode mudar a regra.</div></div>
""")

# 9 · 3 MOTIVOS BB -------------------------------------------------------------------------------------------
S[9] = dict(semente=67, css=CSS_M, corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">3 motivos pra<br><span class="c">comprar o BB.</span></div>
</div>
<div class="abs lista">{motivos([
  ('O problema é um só', 'O calote está concentrado no agro. O resto do banco segue de pé.'),
  ('O motor ainda gira', 'A margem financeira cresceu 14,8% em um ano (1T26).'),
  ('Capital pra atravessar', 'Índice de capital principal (CET1) de 10,8% no 3T26.')])}</div>
<div class="abs risco"><div class="caps">O que pode dar errado</div>
  <div class="corpo">O calote do agro ainda não parou de subir. E com payout de 25%, o dividendo encolhe.</div></div>
""")

# 10 · OPINIÃO + CTA -----------------------------------------------------------------------------------------
S[10] = dict(semente=97, classe='cta', extra='data-tom="frio"', css="""
.op { left: 72px; right: 72px; top: 300px; display: flex; flex-direction: column; gap: 20px; }
.op .vidro { padding: 26px 30px; }
.op .caps { font-size: 22px; color: var(--amarelo); }
.op .corpo { font-size: 32px; margin-top: 10px; line-height: 1.3; }
.botoes { left: 72px; right: 72px; top: 1016px; display: flex; gap: 18px; justify-content: center; }
.botoes div { height: 104px; padding: 0 34px; border-radius: 52px; display: flex; align-items: center; font: 900 50px/1 'Montserrat'; letter-spacing: -0.03em;
  background: linear-gradient(180deg, #FFE23D 0%, #FFCB05 100%); color: #15130F; box-shadow: inset 0 3px 0 rgba(255,255,255,.6), inset 0 -6px 0 rgba(170,120,0,.45), 0 20px 40px rgba(0,0,0,.4); }
.aviso { left: 72px; right: 72px; top: 1150px; text-align: center; font: 500 21px/1.35 'Montserrat'; color: rgba(255,255,255,.5); }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo" style="font-size:60px">Minha leitura, pra quem pensa<br><span class="a">em 5 anos, não em 5 dias.</span></div>
</div>
<div class="abs op">
  <div class="vidro"><div class="caps">Petrobras</div><div class="corpo">Faz sentido como ação de <b>renda</b>, com aporte mês a mês, sem concentrar a carteira nela.</div></div>
  <div class="vidro"><div class="caps">Banco do Brasil</div><div class="corpo">É uma aposta na <b>virada do agro</b>. Só com pouco dinheiro e paciência pra mais 1 ou 2 anos ruins.</div></div>
  <div class="vidro"><div class="caps">Se o plano é dobrar em 3 meses</div><div class="corpo">Aí não é investimento. <b>É bet.</b> Nenhuma das duas serve pra isso.</div></div>
</div>
<div class="col centro" style="top:944px"><div class="corpo forte" style="font-size:40px">E você? Comenta o ticker e:</div></div>
<div class="abs botoes"><div>COMPRA</div><div>MANTÉM</div><div>VENDE</div></div>
<div class="abs aviso">Conteúdo educativo, não é recomendação de investimento. Lucros dos releases de 4T25 a 3T26 (BB: lucro ajustado).</div>
""")

for n, d in S.items():
    (RAIZ / f'slide-{n:02d}.html').write_text(pagina(n, d['corpo'], d.get('css', ''), d.get('classe', ''), d.get('semente', 7), d.get('extra', '')), encoding='utf-8')
    print(f'slide-{n:02d}.html')
