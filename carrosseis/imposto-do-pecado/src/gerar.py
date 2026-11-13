#!/usr/bin/env python3
"""Gera src/slide-01.html a slide-09.html. A copy mora aqui (e em ../BRIEF.md); o visual em base.css.
Uso: python3 src/gerar.py && NODE_PATH=$(npm root -g) node src/render.mjs"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

def pagina(n, corpo, css='', classe='', semente=7, extra=''):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>slide {n:02d}</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div id="quadro" class="{classe}" data-n="{n:02d}" data-total="09" data-semente="{semente}" {extra}>
<div class="conteudo">{corpo}</div></div>
<script src="ilustras.js"></script><script src="base.js"></script></body></html>
"""

S = {}

# 1 · CAPA ---------------------------------------------------------------------------------
S[1] = dict(semente=11, css="""
.luz { left: 90px; top: 40px; width: 900px; height: 760px; background: radial-gradient(closest-side, rgba(255,186,120,.26), rgba(255,186,120,0)); }
.palco { left: 72px; right: 72px; top: 130px; height: 600px; display: flex; align-items: flex-end; justify-content: center; }
.palco > div { flex: none; }
.piso { left: 0; right: 0; top: 722px; height: 150px; background: linear-gradient(180deg, rgba(255,255,255,.07), rgba(255,255,255,0)); }
.carimbo { left: 92px; top: 116px; width: 264px; height: 264px; border-radius: 50%; transform: rotate(-11deg);
  border: 7px solid var(--coral-forma); color: var(--coral); display: flex; flex-direction: column; align-items: center; justify-content: center;
  background: rgba(22,19,18,.72); }
.carimbo::after { content: ''; position: absolute; inset: 9px; border-radius: 50%; border: 2.5px solid var(--coral-forma); }
.carimbo .k { font: 800 19px/1 'Montserrat'; letter-spacing: .16em; }
.carimbo .d { font: 400 96px/1 'Anton'; margin: 8px 0 2px; letter-spacing: .01em; }
.carimbo .y { font: 400 50px/1 'Anton'; letter-spacing: .06em; }
.manchete { top: 800px; }
.manchete .anton { line-height: 1.13; }
.manchete .anton:nth-child(3) { margin-top: 12px; }
""", corpo="""
<div class="abs luz"></div>
<div class="abs piso"></div>
<div class="abs palco">
  <div data-il="cigarro" style="width:256px;margin-right:-26px;z-index:3"></div>
  <div data-il="destilado" style="width:216px;z-index:2"></div>
  <div data-il="cerveja" style="width:194px;margin-left:-10px;z-index:1"></div>
  <div data-il="lata" style="width:176px;margin-left:-16px;z-index:3"></div>
</div>
<div class="abs carimbo"><span class="k">A PARTIR DE</span><span class="d">2 FEV</span><span class="y">2027</span></div>
<div class="col manchete">
  <div class="anton" data-fit="936" style="color:var(--coral)">Imposto do pecado</div>
  <div class="anton" data-fit="936" style="color:var(--coral)">começa em fevereiro.</div>
  <div class="anton" data-fit="936">O aumento de verdade, não.</div>
</div>
""")

# 2 · HOLD: o que é e o que entra ------------------------------------------------------------
itens = [('cigarro', 'Cigarro', 104), ('cerveja', 'Cerveja', 50), ('destilado', 'Destilado', 68), ('lata', 'Refrigerante', 74),
         ('carro', 'Carro', 178), ('aviao', 'Avião', 180), ('barco', 'Barco', 180), ('loteria', 'Loteria', 150)]
S[2] = dict(semente=23, css="""
.grade { left: 72px; right: 72px; top: 474px; display: grid; grid-template-columns: repeat(4, 216px); gap: 24px; }
.grade .vidro { height: 272px; display: flex; flex-direction: column; align-items: center; padding: 16px 10px 20px; }
.grade .ic { flex: 1; display: flex; align-items: center; justify-content: center; }
.grade .nm { font: 700 28px/1 'Montserrat'; letter-spacing: -0.01em; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo" style="font-size:68px">O nome oficial é<br><span class="c">Imposto Seletivo.</span></div>
  <div class="corpo" style="margin-top:28px">Ele cobra a mais de tudo que o governo considera <span class="c">ruim pra saúde ou pro meio ambiente.</span></div>
</div>
<div class="abs grade">
  {''.join(f'<div class="vidro"><div class="ic"><div data-il="{k}" style="width:{w}px"></div></div><div class="nm">{nm}</div></div>' for k, nm, w in itens)}
</div>
<div class="col" style="top:1096px">
  <div class="corpo forte" style="font-size:46px;line-height:1.2">Do maço de cigarro<br>ao <span class="traco">bilhete de loteria.</span></div>
</div>
""")

# 3 · SPINE: a tabela de 2027 ------------------------------------------------------------------
linhas = [('cigarro', 62, 'Cigarro', '<span class="g">66,7%* +</span><span class="p">R$ 3,50 por maço</span>'),
          ('destilado', 40, 'Destilados', 'até 24%'), ('vinho', 46, 'Vinho', '8%'), ('cerveja', 30, 'Cerveja', '4,2%'),
          ('lata', 44, 'Refrigerante', '2,6%'), ('loteria', 104, 'Loteria', '0,5%')]
S[3] = dict(semente=37, css="""
.tabela { left: 72px; right: 72px; top: 292px; overflow: hidden; }
.tabela .cab { height: 72px; display: grid; grid-template-columns: 1fr 340px; align-items: center; }
.tabela .cab span { font: 700 25px/1 'Montserrat'; letter-spacing: .1em; color: var(--mudo); padding-left: 150px; }
.tabela .cab b { height: 100%; display: flex; align-items: center; justify-content: center; background: var(--coral-forma); color: #fff;
  font: 800 25px/1 'Montserrat'; letter-spacing: .1em; clip-path: polygon(34px 0, 100% 0, 100% 100%, 0 100%); }
.tabela .ln { height: 111px; display: grid; grid-template-columns: 150px 1fr 340px; align-items: center; border-top: 1.5px solid rgba(255,255,255,.14); }
.tabela .ic { display: flex; align-items: center; justify-content: center; height: 100%; }
.tabela .nm { font: 700 43px/1 'Montserrat'; letter-spacing: -0.02em; }
.tabela .vl { display: flex; justify-content: center; border-left: 1.5px solid rgba(255,255,255,.16); }
.tabela .pilula { width: 276px; height: 78px; font-size: 46px; }
.tabela .pilula .g { font-size: 38px; line-height: 1; }
.tabela .pilula .p { font-size: 22px; line-height: 1; margin-top: 6px; letter-spacing: -0.01em; }
.tabela .pilula.dupla { height: 92px; }
""", corpo=f"""
<div class="col" style="top:92px">
  <div class="titulo" style="font-size:76px">Quanto cada um<br>paga <span class="c traco">em 2027</span></div>
</div>
<div class="abs tabela vidro">
  <div class="cab"><span>PRODUTO</span><b>ALÍQUOTA</b></div>
  {''.join(f'<div class="ln"><div class="ic"><div data-il="{k}" style="width:{w}px"></div></div><div class="nm">{nm}</div><div class="vl"><div class="pilula{" dupla" if "class" in v else ""}">{v}</div></div></div>' for k, w, nm, v in linhas)}
</div>
<div class="col" style="top:1070px">
  <div class="corpo forte" style="font-size:42px">O cigarro leva a maior mordida.</div>
  <div class="nota" style="margin-top:16px">*Os 66,7% incidem sobre 15% do preço de venda do maço.<br>Fonte: MP 1.399/2026.</div>
</div>
""")

# 4 · SPINE: carros -----------------------------------------------------------------------------
cartoes = [('carro', 236, 'Carro de passeio', '6,3%', 'alíquota-base', ''),
           ('picape', 246, 'Picape e furgão', '3,9%', 'alíquota-base', ''),
           ('gota', 96, 'Motor a diesel', '+12', 'pontos na conta', ' c')]
S[4] = dict(semente=41, css="""
.trio { left: 72px; right: 72px; top: 326px; display: grid; grid-template-columns: repeat(3, 296px); gap: 24px; }
.trio .vidro { height: 440px; display: flex; flex-direction: column; align-items: center; padding: 22px 12px 28px; text-align: center; }
.trio .ic { height: 170px; display: flex; align-items: center; justify-content: center; }
.trio .caps { font-size: 21px; color: rgba(255,255,255,.78); margin-top: 14px; }
.trio .num { font: 800 90px/1 'Montserrat'; letter-spacing: -0.045em; margin-top: 16px; }
.trio .nota { margin-top: 12px; }
""", corpo=f"""
<div class="col" style="top:96px">
  <div class="titulo">No carro,<br><span class="c">o motor decide.</span></div>
</div>
<div class="abs trio">
  {''.join(f'<div class="vidro"><div class="ic"><div data-il="{k}" style="width:{w}px"></div></div><div class="caps">{rot}</div><div class="num{cl}">{num}</div><div class="nota">{sub}</div></div>' for k, w, rot, num, sub, cl in cartoes)}
</div>
<div class="col" style="top:826px">
  <div class="corpo" style="font-size:42px">Potência, combustível e eficiência <b>somam ou tiram pontos</b> dessa base.</div>
  <div class="corpo forte" style="font-size:44px;margin-top:34px">PcD e táxi ficam com <span class="c traco">alíquota zero.</span></div>
  <div class="nota" style="margin-top:34px">Fonte: MP 1.399/2026 e Agência Senado.</div>
</div>
""")

# 5 · SPINE: importado ---------------------------------------------------------------------------
S[5] = dict(semente=53, css="""
.par { left: 72px; right: 72px; top: 326px; display: grid; grid-template-columns: repeat(2, 456px); gap: 24px; }
.par .vidro { height: 548px; display: grid; grid-template-columns: 164px 1fr; align-items: center; padding: 0 14px 0 6px; }
.par .gf { display: flex; justify-content: center; }
.par .caps { font-size: 27px; color: var(--coral); line-height: 1.12; }
.par .num { font: 400 94px/1 'Anton'; margin-top: 26px; letter-spacing: 0; }
.par .elipse::after { left: -4%; right: -4%; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">E o importado<br><span class="c">paga mais.</span></div>
</div>
<div class="abs par">
  <div class="vidro"><div class="gf"><div data-il="cerveja" style="width:142px"></div></div>
    <div><div class="caps">Cerveja<br>nacional</div><div class="num">4,2%</div></div></div>
  <div class="vidro"><div class="gf"><div data-il="importada" style="width:142px"></div></div>
    <div><div class="caps">Cerveja<br>importada</div><div class="num"><span class="elipse c" style="font-weight:400">6,09%</span></div></div></div>
</div>
<div class="col" style="top:930px">
  <div class="corpo" style="font-size:42px">Bebida que vem de fora leva um <b>fator de 1,45</b> na conta.</div>
  <div class="corpo forte" style="font-size:54px;margin-top:30px;letter-spacing:-0.03em">4,2% × 1,45 = <span class="c">6,09%</span></div>
  <div class="nota" style="margin-top:30px">Vale pra bebida alcoólica e bebida açucarada. Fonte: MP 1.399/2026.</div>
</div>
""")

# 6 · RHYTHM (alívio): IPI sai, Seletivo entra ------------------------------------------------------
S[6] = dict(semente=67, css="""
.troca { left: 72px; right: 72px; top: 318px; display: grid; grid-template-columns: 372px 112px 452px; align-items: center; }
.troca .bl { height: 270px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.troca .sai { opacity: .62; }
.troca .sai .anton { font-size: 150px; }
.troca .entra { border-radius: var(--raio); background: linear-gradient(180deg, #E8503C 0%, #C13120 100%);
  box-shadow: inset 0 1.5px 0 rgba(255,255,255,.4), 0 26px 54px rgba(150,32,20,.42); }
.troca .entra .anton { font-size: 82px; text-align: center; line-height: 1.02; }
.troca .rt { font: 600 30px/1 'Montserrat'; margin-top: 12px; color: rgba(255,255,255,.86); }
.troca svg { width: 112px; height: 90px; display: block; }
""", corpo="""
<div class="col" style="top:104px">
  <div class="titulo" style="font-size:112px">Mas <span class="c">calma.</span></div>
</div>
<div class="abs troca">
  <div class="bl vidro sai"><div class="anton">IPI</div><div class="rt">sai</div></div>
  <svg viewBox="0 0 112 90"><path d="M18 30 H62 V10 L100 45 L62 80 V60 H18 Z" fill="#DC3F2E"/></svg>
  <div class="bl entra"><div class="anton">Imposto<br>Seletivo</div><div class="rt">entra</div></div>
</div>
<div class="col" style="top:662px">
  <div class="corpo" style="font-size:42px">Nesses produtos, o Seletivo entra <span class="c">no lugar do IPI.</span></div>
  <div class="corpo" style="font-size:42px;margin-top:30px">Segundo o governo, as alíquotas de 2027 repetem o peso do IPI de hoje.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:40px;line-height:1.3">Na prática, a carga fica<br><span class="marca">parecida com a de hoje.</span></div>
</div>
""")

# 7 · TURN: 2028 ------------------------------------------------------------------------------------
ext = ','.join(f'{i}px {i}px 0 #A62A1B' for i in range(1, 19))
S[7] = dict(semente=71, extra='data-luzes="5"', css=f"""
#quadro {{ background: radial-gradient(120% 70% at 50% 0%, #2A2423 0%, #1B1918 46%, #0E0D0C 100%); }}
.ano {{ left: 0; right: 0; top: 268px; text-align: center; font: 900 372px/1 'Montserrat'; letter-spacing: -0.05em; color: #F2543E;
  text-shadow: {ext}, 26px 44px 46px rgba(0,0,0,.6); }}
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo">O problema é<br><span class="c">o ano seguinte.</span></div>
</div>
<div class="abs ano">2028</div>
<div class="col" style="top:720px">
  <div class="corpo">Essas alíquotas só valem até <span class="c" style="white-space:nowrap">dezembro de 2027.</span></div>
  <div class="corpo" style="margin-top:30px">Até <span class="c">31 de maio</span>, o governo manda ao Congresso as alíquotas de 2028 em diante.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:40px;line-height:1.36">É aí que o <span class="elipse c">aumento de verdade</span><br>pode chegar.</div>
</div>
""")

# 8 · SPINE: 120 dias ---------------------------------------------------------------------------------
S[8] = dict(semente=83, css="""
.amp { right: 60px; top: 330px; width: 372px; }
.esq { top: 318px; right: 440px; }
.esq .anton { font-size: 168px; color: var(--coral); line-height: 1; }
.esq .caps { font-size: 30px; color: var(--coral); margin-top: 6px; letter-spacing: .06em; }
""", corpo="""
<div class="col" style="top:96px">
  <div class="titulo" style="font-size:76px">E nada disso<br><span class="c">está garantido.</span></div>
</div>
<div class="abs amp" data-il="ampulheta"></div>
<div class="col esq">
  <div class="anton">120 dias</div>
  <div class="caps">Prazo do Congresso</div>
  <div class="corpo" style="margin-top:40px">A regra veio por <span class="c">medida provisória.</span></div>
  <div class="corpo" style="margin-top:26px">Já tem força de lei, mas o Congresso precisa aprovar em 120 dias.</div>
</div>
<div class="col" style="top:1006px">
  <div class="corpo forte" style="font-size:50px;line-height:1.34">Se não aprovar,<br><span class="elipse c">perde a validade.</span></div>
</div>
""")

# 9 · PAYOFF + CTA ---------------------------------------------------------------------------------------
S[9] = dict(semente=97, classe='cta', extra='data-tom="frio"', css="""
.botao { margin-top: 26px; width: 640px; height: 176px; border-radius: 88px; display: flex; align-items: center; justify-content: center; position: relative;
  background: linear-gradient(180deg, #FFE23D 0%, #FFCB05 100%); color: #15130F; font: 900 118px/1 'Montserrat'; letter-spacing: -0.03em;
  box-shadow: inset 0 3px 0 rgba(255,255,255,.6), inset 0 -8px 0 rgba(170,120,0,.45), 0 26px 50px rgba(0,0,0,.45); }
.botao svg { position: absolute; left: -150px; top: -86px; width: 150px; height: 190px; }
.fio { width: 120px; height: 5px; border-radius: 3px; background: var(--amarelo); margin: 44px 0 40px; }
""", corpo="""
<div class="col centro" style="top:104px">
  <div class="titulo" style="font-size:70px;line-height:1.08">Imposto novo<br>você não escolhe.</div>
  <div class="titulo a" style="font-size:70px;line-height:1.08;margin-top:6px">O que faz com<br>o seu dinheiro, sim.</div>
  <div class="corpo forte" style="font-size:46px;margin-top:44px;line-height:1.3">Chega de descobrir o aumento<br><span class="marca am">só na hora de pagar.</span></div>
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
