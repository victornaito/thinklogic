"""Gera src/slide-01.html a slide-08.html do carrossel "O que o BTS fez antes do exército".

A capa usa a foto de assets/capa-bts.png; os outros slides são tipográficos, fundo
noturno com roxo ARMY. Rode: python3 src/gerar.py && node src/render.mjs
"""
from pathlib import Path

AQUI = Path(__file__).parent
TOTAL = 8

BASE_CSS = """
@font-face { font-family: 'Geist'; src: url('fontes/Geist-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'Geist Mono'; src: url('fontes/GeistMono-Variable.ttf') format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'DM Serif'; src: url('fontes/DMSerifDisplay-Italic.ttf') format('truetype'); font-style: italic; }
:root {
  --noite: #120B1F; --roxo: #8B3DFF; --lilas: #C9A7FF; --branco: #FFFFFF;
  --mudo: rgba(255,255,255,.62); --fio: rgba(255,255,255,.16); --margem: 80px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1350px; overflow: hidden; background: var(--noite); }
body { -webkit-font-smoothing: antialiased; font-family: 'Geist'; color: var(--branco); }
#quadro { position: absolute; inset: 0; overflow: hidden;
  background: radial-gradient(900px 700px at 85% 0%, rgba(139,61,255,.38), transparent 70%), var(--noite); }
#quadro.roxo { background: radial-gradient(900px 900px at 20% 100%, #5B17C9, transparent 70%), var(--roxo); }
.abs { position: absolute; }
.cab { left: var(--margem); right: var(--margem); top: 64px; display: flex; justify-content: space-between;
  font: 500 22px/1 'Geist Mono'; letter-spacing: .14em; text-transform: uppercase; color: var(--mudo); }
.rodape { left: var(--margem); right: var(--margem); bottom: 64px; display: flex; justify-content: space-between; align-items: center;
  font: 600 24px/1 'Geist Mono'; letter-spacing: .04em; color: var(--mudo); }
.barra { display: flex; gap: 8px; }
.barra i { width: 34px; height: 6px; border-radius: 3px; background: var(--fio); }
.barra i.on { background: var(--lilas); }
.miolo { left: var(--margem); right: var(--margem); top: 170px; bottom: 170px;
  display: flex; flex-direction: column; justify-content: center; gap: 44px; }
.titulo { font-weight: 900; font-size: 104px; line-height: .98; letter-spacing: -0.045em; }
.corpo { font-weight: 500; font-size: 44px; line-height: 1.25; letter-spacing: -0.02em; color: rgba(255,255,255,.88); }
.corpo b { font-weight: 800; color: var(--branco); }
.marca { background: var(--roxo); color: var(--branco); padding: 0 .16em; border-radius: .12em;
  -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.lilas { color: var(--lilas); }
.serifa { font-family: 'DM Serif'; font-style: italic; font-weight: 400; letter-spacing: -0.01em; }
.seta { font-weight: 800; font-size: 46px; color: var(--lilas); letter-spacing: -0.02em; }
.cartao { background: rgba(255,255,255,.07); border: 2px solid var(--fio); border-radius: 28px; padding: 40px 48px; }
.numero { font-weight: 900; font-size: 150px; line-height: .95; letter-spacing: -0.055em; font-variant-numeric: tabular-nums; }
.nota { font: 500 24px/1.4 'Geist Mono'; color: var(--mudo); }
"""

PAGINA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Slide {n} · BTS antes do exército</title>
<style>{base}{css}</style>
</head>
<body>
<div id="quadro" class="{fundo}">
{corpo}
</div>
</body>
</html>
"""


def moldura(n, rotulo):
    barra = "".join(f'<i class="{"on" if i <= n else ""}"></i>' for i in range(1, TOTAL + 1))
    return (f'  <div class="abs cab"><span>{rotulo}</span><span>{n:02d}/{TOTAL:02d}</span></div>\n'
            f'  <div class="abs rodape"><span>@victornaito.financas</span><span class="barra">{barra}</span></div>\n')


CAPA_CSS = """
.foto { position: absolute; left: -135px; top: 0; width: 1350px; height: 1350px; object-fit: cover; }
.sombra { position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(18,11,31,.55) 0%, rgba(18,11,31,0) 16%, rgba(18,11,31,0) 34%,
    rgba(18,11,31,.82) 52%, rgba(18,11,31,.97) 66%, var(--noite) 100%); }
.selo { left: var(--margem); top: 64px; background: var(--roxo); color: #fff; border-radius: 999px;
  padding: 14px 26px; font: 700 24px/1 'Geist Mono'; letter-spacing: .12em; text-transform: uppercase;
  box-shadow: 0 10px 30px rgba(0,0,0,.35); }
.bloco { left: var(--margem); right: var(--margem); bottom: 140px; }
.h1 { font-weight: 900; font-size: 98px; line-height: .96; letter-spacing: -0.05em; text-shadow: 0 6px 30px rgba(0,0,0,.5); }
.h1 .big { color: var(--lilas); }
.h2 { margin-top: 26px; font-weight: 900; font-size: 74px; line-height: 1.12; letter-spacing: -0.04em; }
.h2 .marca { padding: 0 .18em .04em; }
.sub { margin-top: 34px; font-weight: 500; font-size: 36px; line-height: 1.28; letter-spacing: -0.015em; color: rgba(255,255,255,.86); max-width: 900px; }
.sub b { color: #fff; font-weight: 800; box-shadow: inset 0 -12px 0 rgba(139,61,255,.8); }
.handle { left: var(--margem); right: var(--margem); bottom: 64px; display: flex; justify-content: space-between;
  font: 600 24px/1 'Geist Mono'; color: var(--mudo); }
.handle .arrasta { color: var(--lilas); }
"""

CAPA = """  <img class="foto" src="../assets/capa-bts.png" alt="">
  <div class="sombra"></div>
  <div class="abs selo">Aula de dinheiro · ARMY 💜</div>
  <div class="abs bloco">
    <div class="h1">O BTS ficou <span class="big">quase 3&nbsp;anos</span> sem o grupo completo.</div>
    <div class="h2"><span class="marca">E continuou lançando música.</span></div>
    <div class="sub">O que eles fizeram antes do exército é <b>a aula de dinheiro que a escola não te deu.</b></div>
  </div>
  <div class="abs handle"><span>@victornaito.financas</span><span class="arrasta">arrasta →</span></div>"""

SLIDES = [
    # (fundo, rótulo, css, miolo)
    ("", "O fato", "", """
    <div class="titulo">Na Coreia do Sul, todo homem serve o exército por <span class="lilas">cerca de 18&nbsp;meses.</span><br><span class="serifa">Famoso também.</span></div>
    <div class="corpo">Antes de ir, eles <b>gravaram músicas, clipes e conteúdos</b> e deixaram tudo programado.</div>
    <div class="corpo">Teve lançamento saindo com o artista <b>dentro do quartel.</b></div>
    <div class="seta">→ Em finanças, isso tem nome.</div>"""),

    ("", "A lição", ".titulo { font-size: 150px; }", """
    <div class="titulo"><span class="marca">Reserva de emergência.</span></div>
    <div class="corpo">É deixar seu trabalho <b>“gravado”</b> antes de uma pausa que você não escolheu: demissão, doença, carro quebrado.</div>
    <div class="cartao">
      <div class="corpo">A meta é <b>6 meses do seu custo de vida.</b></div>
      <div class="corpo" style="margin-top:18px">Gasta R$&nbsp;3.000 por mês?<br>Sua reserva é <span class="lilas" style="font-weight:900">R$&nbsp;18.000.</span></div>
    </div>"""),

    ("", "Como começar", "", """
    <div class="titulo">R$&nbsp;18 mil assusta.<br><span class="lilas">Então começa menor.</span></div>
    <div class="cartao">
      <div class="corpo"><b>R$&nbsp;300 por mês</b> viram</div>
      <div class="numero lilas">R$&nbsp;3.600</div>
      <div class="corpo">em 1 ano.</div>
    </div>
    <div class="corpo">Isso já é <b>1 mês inteiro de vida</b> pago sem pedir ajuda pra ninguém.</div>
    <div class="seta">→ Pronto, você está protegido. Só que tem uma pausa que ninguém grava.</div>"""),

    ("roxo", "Reviravolta", """
    .titulo { font-size: 128px; }
    .grande { font-weight: 900; font-size: 210px; line-height: .9; letter-spacing: -0.06em; }
    .cab, .rodape { color: rgba(255,255,255,.8); }
    .barra i { background: rgba(255,255,255,.25); } .barra i.on { background: #fff; }
    .corpo { color: #fff; }""", """
    <div class="titulo">A pausa do BTS durou 2&nbsp;anos.</div>
    <div class="grande">A sua vai<br>durar 20.</div>
    <div class="corpo">A aposentadoria é o seu <b>serviço militar obrigatório.</b><br><span class="serifa" style="font-size:56px">Só que sem data de volta.</span></div>"""),

    ("", "A conta", """
    .linha { display: flex; justify-content: space-between; align-items: baseline; gap: 30px; padding: 22px 0; border-bottom: 2px solid var(--fio); }
    .linha .r { font-weight: 800; font-size: 50px; letter-spacing: -0.03em; white-space: nowrap; }
    .linha .l { font-weight: 500; font-size: 36px; color: rgba(255,255,255,.85); line-height: 1.2; }
    .falta .l, .falta .r { color: var(--lilas); } .falta { border-bottom: none; }
    .falta .r { font-size: 76px; font-weight: 900; }
    .miolo { gap: 36px; }""", """
    <div class="titulo" style="font-size:96px">Faltam <span class="marca">R$&nbsp;1.400</span> por mês.</div>
    <div>
      <div class="linha"><span class="l">Você vai precisar pra viver</span><span class="r">R$&nbsp;3.000</span></div>
      <div class="linha"><span class="l">A maioria dos aposentados do INSS recebe</span><span class="r">1 salário mínimo</span></div>
      <div class="linha falta"><span class="l">Diferença, em dinheiro de hoje</span><span class="r">−R$&nbsp;1.400</span></div>
    </div>
    <div class="corpo">Durante <b>20 anos</b> de aposentadoria.</div>
    <div class="titulo" style="font-size:84px">Quem cobre essa diferença <span class="lilas">é você.</span></div>"""),

    ("", "A virada boa", """
    .duo { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
    .duo .cartao { padding: 34px 36px; }
    .duo .k { font: 600 24px/1.2 'Geist Mono'; letter-spacing: .08em; text-transform: uppercase; color: var(--mudo); }
    .duo .v { font-weight: 900; font-size: 84px; letter-spacing: -0.05em; line-height: 1; margin: 14px 0 10px; }
    .duo .d { font-size: 30px; line-height: 1.25; color: rgba(255,255,255,.85); }
    .destaque { border-color: var(--roxo); background: rgba(139,61,255,.18); }
    .miolo { gap: 36px; }""", """
    <div class="corpo">Quem guarda <b>R$&nbsp;200 por mês dos 25 aos 65 anos</b> coloca R$&nbsp;96 mil do bolso.</div>
    <div class="corpo">Rendendo 0,8% ao mês, chega perto de</div>
    <div class="numero lilas" style="font-size:170px">R$&nbsp;1,1 mi</div>
    <div class="duo">
      <div class="cartao destaque"><div class="k">Começa aos 25</div><div class="v">R$&nbsp;200</div><div class="d">por mês</div></div>
      <div class="cartao"><div class="k">Começa aos 45</div><div class="v">R$&nbsp;1.550</div><div class="d">por mês, pro mesmo lugar</div></div>
    </div>
    <div class="titulo" style="font-size:80px;line-height:1.12">O tempo faz o <span class="marca">trabalho pesado.</span></div>
    <div class="nota">Simulação, sem garantia de rentabilidade, valores sem descontar a inflação.</div>"""),

    ("", "Fechamento", """
    .palavra { display: inline-block; background: var(--roxo); border-radius: 22px; padding: 18px 40px 22px;
      font-weight: 900; font-size: 120px; letter-spacing: -0.03em; line-height: 1; box-shadow: 0 20px 60px rgba(139,61,255,.45); }
    .miolo { gap: 40px; }""", """
    <div class="titulo" style="font-size:92px">O BTS gravou antes de ir.<br><span class="lilas">E você, o que já deixou gravado pro seu futuro?</span></div>
    <div class="corpo">Comenta</div>
    <div><span class="palavra">PLANEJA</span></div>
    <div class="corpo">que eu te mando o passo a passo pra montar sua reserva e começar a sua <b>“gravação”.</b></div>
    <div class="corpo">Manda pra aquela amiga ARMY que vive dizendo que um dia começa. 💜</div>"""),
]


def main():
    (AQUI / "slide-01.html").write_text(
        PAGINA.format(n="01", base=BASE_CSS, css=CAPA_CSS, fundo="", corpo=CAPA), encoding="utf-8")
    for i, (fundo, rotulo, css, miolo) in enumerate(SLIDES, start=2):
        corpo = moldura(i, rotulo) + f'  <div class="abs miolo">{miolo}\n  </div>'
        (AQUI / f"slide-{i:02d}.html").write_text(
            PAGINA.format(n=f"{i:02d}", base=BASE_CSS, css=css, fundo=fundo, corpo=corpo), encoding="utf-8")


if __name__ == "__main__":
    main()
