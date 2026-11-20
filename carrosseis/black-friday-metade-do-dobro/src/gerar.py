#!/usr/bin/env python3
"""Gera src/slide-01.html a slide-09.html do carrossel "Black Friday: metade do dobro".
A copy mora aqui (e em ../BRIEF.md); o visual em base.css (o mesmo do carrossel do imposto do pecado).
Uso: python3 src/gerar.py && NODE_PATH=$(npm root -g) node src/render.mjs && python3 src/folha.py"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

def pagina(n, corpo, css='', classe='', semente=7, extra=''):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>slide {n:02d}</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div id="quadro" class="{classe}" data-n="{n:02d}" data-total="09" data-semente="{semente}" {extra}>
<div class="conteudo">{corpo}</div></div>
<script src="ilustras.js"></script><script src="ilustras-bf.js"></script><script src="base.js"></script></body></html>
"""

def brl(v):
    return 'R$ ' + f'{v:,.0f}'.replace(',', '.')

S = {}

# 1 · CAPA --------------------------------------------------------------------------------------
S[1] = dict(semente=13, css="""
.luz { left: 60px; top: 30px; width: 960px; height: 780px; background: radial-gradient(closest-side, rgba(255,186,120,.24), rgba(255,186,120,0)); }
.piso { left: 0; right: 0; top: 700px; height: 150px; background: linear-gradient(180deg, rgba(255,255,255,.07), rgba(255,255,255,0)); }
.cel { left: 150px; top: 196px; width: 262px; }
.tag { left: 446px; top: 250px; width: 520px; }
.riscado { left: 540px; top: 152px; font: 700 54px/1 'Montserrat'; color: rgba(255,255,255,.55); letter-spacing: -0.02em; }
.riscado::after { content: ''; position: absolute; left: -6px; right: -6px; top: 50%; height: 6px; background: var(--coral-forma); transform: rotate(-4deg); }
.manchete { top: 792px; }
.manchete .anton { line-height: 1.12; }
""", corpo="""
<div class="abs luz"></div>
<div class="abs piso"></div>
<div class="abs cel" data-il="celular"></div>
<div class="abs riscado">R$ 3.560</div>
<div class="abs tag" data-il="etiqueta"></div>
<div class="col manchete">
  <div class="anton" data-fit="936" style="color:var(--coral)">O desconto da Black Friday</div>
  <div class="anton" data-fit="936" style="color:var(--coral)">pode ser só o preço</div>
  <div class="anton" data-fit="936">que estava em agosto.</div>
</div>
""")

# 2 · HOLD: 74 produtos ---------------------------------------------------------------------------
pontos = ['c'] * 24 + ['b'] * 6 + ['g'] * 44
S[2] = dict(semente=29, css="""
.grade74 { left: 72px; right: 72px; top: 388px; display: grid; grid-template-columns: repeat(10, 1fr); gap: 16px 0; justify-items: center; }
.grade74 i { width: 62px; height: 62px; border-radius: 50%; display: block; }
.grade74 i.c { background: linear-gradient(180deg, #F0604A, #C93524); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.35); }
.grade74 i.b { background: #F4EEE2; }
.grade74 i.g { background: rgba(255,255,255,.12); border: 1.5px solid rgba(255,255,255,.2); }
.leg { left: 72px; right: 72px; top: 1006px; display: flex; gap: 36px; font: 600 28px/1.2 'Montserrat'; }
.leg span { display: flex; align-items: center; gap: 12px; }
.leg i { width: 26px; height: 26px; border-radius: 50%; display: block; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo" style="font-size:72px">74 produtos vigiados<br><span class="c">desde agosto.</span></div>
  <div class="corpo" style="margin-top:24px;font-size:38px">O g1 anota o preço de cada um, todo dia.</div>
</div>
<div class="abs grade74">{''.join(f'<i class="{p}"></i>' for p in pontos)}</div>
<div class="abs leg">
  <span><i style="background:#DC3F2E"></i><b>24</b>&nbsp;mais caros</span>
  <span><i style="background:#F4EEE2"></i><b>6</b>&nbsp;na média</span>
  <span style="color:var(--mudo)"><i style="background:rgba(255,255,255,.18)"></i>os outros 44</span>
</div>
<div class="col" style="top:1094px">
  <div class="corpo forte" style="font-size:46px">30 de 74 <span class="traco">sem desconto de verdade.</span></div>
</div>
""")

# 3 · SPINE: o gráfico do Realme ---------------------------------------------------------------------
# eixo: R$ 2.200 (base) a R$ 3.800 (topo) em 380 px; datas em x
def y(v): return 400 - (v - 2200) / 1600 * 380
pts = [(60, 2499, '26/08'), (420, 2470, '14/10'), (800, 3560, '20/11')]
linha = ' '.join(f'{x},{y(v):.0f}' for x, v, _ in pts)
desc = 3560 * 0.7
grafico = f"""
<svg viewBox="0 0 936 470" width="936" height="470" style="display:block;overflow:visible">
  <line x1="0" y1="{y(desc):.0f}" x2="936" y2="{y(desc):.0f}" stroke="#F4EEE2" stroke-opacity=".7" stroke-width="3" stroke-dasharray="12 10"/>
  <path d="M{linha.replace(' ', ' L')} L800,420 L60,420 Z" fill="#DC3F2E" opacity=".14"/>
  <polyline points="{linha}" fill="none" stroke="#FF5A47" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  {''.join(f'<circle cx="{x}" cy="{y(v):.0f}" r="13" fill="#1A1817" stroke="#FF5A47" stroke-width="7"/>' for x, v, _ in pts)}
  {''.join(f'<text x="{x}" y="462" text-anchor="middle" font-family="Montserrat" font-weight="600" font-size="26" fill="rgba(255,255,255,.6)">{d}</text>' for x, _, d in pts)}
  <text x="60" y="{y(2499) - 34:.0f}" text-anchor="start" font-family="Montserrat" font-weight="800" font-size="40" fill="#fff">{brl(2499)}</text>
  <text x="420" y="{y(2470) + 62:.0f}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="40" fill="#fff">{brl(2470)}</text>
  <text x="770" y="{y(3560) - 34:.0f}" text-anchor="end" font-family="Montserrat" font-weight="800" font-size="52" fill="#FF5A47">{brl(3560)}</text>
  <text x="936" y="{y(desc) + 46:.0f}" text-anchor="end" font-family="Montserrat" font-weight="700" font-size="28" fill="#F4EEE2">com "30% off": {brl(desc)}</text>
</svg>"""
S[3] = dict(semente=37, css="""
.graf { left: 72px; top: 424px; padding: 36px 0 0; }
.rot { left: 72px; top: 360px; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">O truque tem nome:<br><span class="c">metade do dobro.</span></div>
</div>
<div class="abs rot caps" style="color:var(--mudo)">Realme P4 Power · 256 GB</div>
<div class="abs graf">{grafico}</div>
<div class="col" style="top:1000px">
  <div class="corpo">Subiu 42% em cinco semanas.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:22px;line-height:1.28">Com 30% de desconto,<br>volta pro <span class="marca">preço de agosto.</span></div>
</div>
""")

# 4 · SPINE: subiu antes ---------------------------------------------------------------------------
S[4] = dict(semente=43, css="""
.par { left: 72px; right: 72px; top: 330px; display: grid; grid-template-columns: repeat(2, 456px); gap: 24px; }
.par .vidro { height: 560px; display: flex; flex-direction: column; align-items: center; padding: 30px 28px 34px; text-align: center; }
.par .ic { height: 230px; display: flex; align-items: flex-end; justify-content: center; }
.par .caps { font-size: 23px; color: rgba(255,255,255,.8); margin-top: 24px; }
.par .de { font: 600 30px/1 'Montserrat'; color: var(--mudo); margin-top: 22px; }
.par .por { font: 800 60px/1 'Montserrat'; letter-spacing: -0.04em; margin-top: 10px; }
.par .pct { margin-top: 20px; }
.par .pilula { width: 220px; height: 70px; font-size: 40px; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">Tem produto que<br><span class="c">subiu na véspera.</span></div>
</div>
<div class="abs par">
  <div class="vidro"><div class="ic"><div data-il="celular" style="width:118px"></div></div>
    <div class="caps">Galaxy A17 5G · 128 GB</div>
    <div class="de">set/out: R$ 999</div><div class="por">R$ 1.199</div>
    <div class="pct"><div class="pilula">+20%</div></div></div>
  <div class="vidro"><div class="ic"><div data-il="console" style="width:124px"></div></div>
    <div class="caps">Xbox Series X</div>
    <div class="de">em 19/11</div><div class="por">R$ 8.500</div>
    <div class="pct"><div class="pilula">+26%</div></div></div>
</div>
<div class="col" style="top:944px">
  <div class="corpo" style="font-size:38px">O Galaxy, na semana antes da Black Friday. O Xbox, acima da própria média desde agosto.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:28px">Sobe 20% pra <span class="traco">"cair" 20%.</span></div>
</div>
""")

# 5 · SPINE: na média ---------------------------------------------------------------------------------
S[5] = dict(semente=59, css="""
.tv { left: 72px; top: 330px; width: 936px; height: 470px; display: grid; grid-template-columns: 380px 1fr; align-items: center; padding: 0 40px 0 30px; }
.tv .caps { font-size: 23px; color: rgba(255,255,255,.8); }
.tv .de { font: 700 50px/1 'Montserrat'; color: rgba(255,255,255,.5); margin-top: 22px; letter-spacing: -0.03em; }
.tv .de s { text-decoration-color: var(--coral-forma); text-decoration-thickness: 5px; }
.tv .por { font: 800 72px/1 'Montserrat'; letter-spacing: -0.045em; margin-top: 12px; }
.tv .pilula { width: 200px; height: 64px; font-size: 36px; margin-top: 22px; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">E tem desconto que<br><span class="c">é só a média.</span></div>
</div>
<div class="abs tv vidro">
  <div data-il="tv" style="width:350px"></div>
  <div><div class="caps">TV de 100" · pico em outubro</div>
    <div class="de"><s>R$ 32.999</s></div><div class="por">R$ 21.062</div>
    <div class="pilula">-36%?</div></div>
</div>
<div class="col" style="top:856px">
  <div class="corpo" style="font-size:40px">R$ 21.062 é a média dela desde agosto. O "de" usa o pico.</div>
  <div class="corpo" style="font-size:40px;margin-top:24px">O iPhone 17e (256 GB) está por R$ 4.417. Também na média. Em setembro, R$ 4.499 sem selo nenhum.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:30px">O selo mudou. <span class="c">O preço, não.</span></div>
</div>
""")

# 6 · TURN ----------------------------------------------------------------------------------------------
S[6] = dict(semente=71, extra='data-luzes="5"', css="""
#quadro { background: radial-gradient(120% 70% at 50% 0%, #2A2423 0%, #1B1918 46%, #0E0D0C 100%); }
.de-gig { top: 300px; }
.de-gig .anton { font-size: 300px; line-height: .9; color: rgba(255,255,255,.18); position: relative; display: inline-block; }
.de-gig .anton::after { content: ''; position: absolute; left: -20px; right: -20px; top: 48%; height: 22px; background: var(--coral-forma); transform: rotate(-6deg); border-radius: 11px; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">O preço que importa<br><span class="c">não é o "de".</span></div>
</div>
<div class="col de-gig"><div><span class="anton">DE R$</span></div></div>
<div class="col" style="top:700px">
  <div class="corpo">O "de" quem escolhe é a loja. Pode ser o pico de outubro ou o preço da semana passada.</div>
  <div class="corpo forte" style="font-size:54px;margin-top:40px;line-height:1.24">A sua régua é<br><span class="elipse c">o histórico.</span></div>
</div>
""")

# 7 · SPINE: como conferir ---------------------------------------------------------------------------------
passos = [('1', 'Buscapé ou Zoom', 'Abre o gráfico de 3 a 6 meses do produto.'),
          ('2', 'Keepa', 'Extensão que mostra o histórico dentro da Amazon.'),
          ('3', 'A régua', 'Só é desconto se ficar abaixo da média de 3 meses.')]
S[7] = dict(semente=83, css="""
.lista { left: 72px; right: 72px; top: 330px; display: flex; flex-direction: column; gap: 24px; }
.lista .vidro { height: 200px; display: grid; grid-template-columns: 130px 1fr; align-items: center; padding: 0 34px 0 30px; }
.lista .n { width: 96px; height: 96px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 400 60px/1 'Anton';
  background: linear-gradient(180deg, #E8503C, #C93524); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.38); }
.lista .t { font: 800 44px/1.1 'Montserrat'; letter-spacing: -0.025em; }
.lista .d { font: 500 32px/1.3 'Montserrat'; color: rgba(255,255,255,.82); margin-top: 10px; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">Antes de pagar,<br><span class="c">confere em 1 minuto.</span></div>
</div>
<div class="abs lista">
  {''.join(f'<div class="vidro"><div class="n">{n}</div><div><div class="t">{t}</div><div class="d">{d}</div></div></div>' for n, t, d in passos)}
</div>
<div class="col" style="top:1032px">
  <div class="corpo forte" style="font-size:46px">Print do gráfico <span class="traco">antes do carrinho.</span></div>
</div>
""")

# 8 · RHYTHM: o desconto que sai mais caro ------------------------------------------------------------------
S[8] = dict(semente=89, css="""
.par2 { left: 72px; right: 72px; top: 330px; display: grid; grid-template-columns: repeat(2, 456px); gap: 24px; }
.par2 .vidro { height: 380px; padding: 40px 36px; display: flex; flex-direction: column; justify-content: space-between; }
.par2 .caps { font-size: 24px; }
.par2 .big { font: 800 64px/1.02 'Montserrat'; letter-spacing: -0.04em; }
.par2 .sub { font: 500 30px/1.3 'Montserrat'; color: rgba(255,255,255,.8); }
.par2 .ruim { background: linear-gradient(180deg, #E8503C 0%, #B92F1F 100%); border-color: rgba(255,255,255,.3); }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">O desconto mais caro<br><span class="c">é o que não cabe.</span></div>
</div>
<div class="abs par2">
  <div class="vidro"><div class="caps" style="color:var(--mudo)">O que a loja mostra</div><div class="big">30% off</div><div class="sub">em 12x sem juros</div></div>
  <div class="vidro ruim"><div class="caps">O que chega em janeiro</div><div class="big">12 parcelas</div><div class="sub">+ IPVA, IPTU e material escolar</div></div>
</div>
<div class="col" style="top:776px">
  <div class="corpo">Compra boa é a que você já ia fazer, no preço abaixo da média, e que cabe no mês.</div>
  <div class="corpo forte" style="font-size:48px;margin-top:40px;line-height:1.28">Fora disso, é só<br><span class="marca">gasto com selo de economia.</span></div>
</div>
""")

# 9 · PAYOFF + CTA ---------------------------------------------------------------------------------------------
S[9] = dict(semente=97, classe='cta', extra='data-tom="frio"', css="""
.botao { margin-top: 26px; width: 640px; height: 176px; border-radius: 88px; display: flex; align-items: center; justify-content: center; position: relative;
  background: linear-gradient(180deg, #FFE23D 0%, #FFCB05 100%); color: #15130F; font: 900 118px/1 'Montserrat'; letter-spacing: -0.03em;
  box-shadow: inset 0 3px 0 rgba(255,255,255,.6), inset 0 -8px 0 rgba(170,120,0,.45), 0 26px 50px rgba(0,0,0,.45); }
.botao svg { position: absolute; left: -150px; top: -86px; width: 150px; height: 190px; }
.fio { width: 120px; height: 5px; border-radius: 3px; background: var(--amarelo); margin: 44px 0 40px; }
""", corpo="""
<div class="col centro" style="top:104px">
  <div class="titulo" style="font-size:70px;line-height:1.08">A loja escolhe o "de".</div>
  <div class="titulo a" style="font-size:70px;line-height:1.08;margin-top:6px">Você escolhe<br>se cabe no seu plano.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:44px;line-height:1.3">Chega de comprar no impulso<br><span class="marca am">e pagar até março.</span></div>
  <div class="fio"></div>
  <div class="corpo" style="font-size:41px;line-height:1.3">Quer fazer o seu<br><span class="a">diagnóstico financeiro gratuito</span><br>e se planejar pra <span class="a">liberdade financeira?</span><br>Comenta</div>
  <div class="botao">CHEGA
    <svg viewBox="0 0 150 190"><path d="M36 14 C2 70 14 132 104 150" fill="none" stroke="#FFD60A" stroke-width="9" stroke-linecap="round"/><path d="M78 124 L108 151 L72 172" fill="none" stroke="#FFD60A" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
  <div class="corpo" style="font-size:38px;margin-top:28px">aqui nos comentários.</div>
</div>
""")

for n, d in S.items():
    (RAIZ / f'slide-{n:02d}.html').write_text(pagina(n, d['corpo'], d.get('css', ''), d.get('classe', ''), d.get('semente', 7), d.get('extra', '')), encoding='utf-8')
    print(f'slide-{n:02d}.html')
