# Catálogo dos 17 efeitos

Cada ficha tem: o que é, quando usar (gatilho na fala), onde rende mais na curva do vídeo,
duração, registro visual, se precisa de recorte (✂), o prompt-base original (é a especificação
visual) e notas de implementação em Remotion.

**Registros** (para alternar entre efeitos vizinhos):
- **FUNDO**: troca o que está atrás da pessoa, pessoa recortada na frente.
- **OVERLAY**: algo aparece por cima do vídeo, fundo original fica.
- **CÂMERA**: mexe no enquadramento/escala do vídeo.
- **CENÁRIO**: o vídeo vira parte de uma interface ou layout maior.
- **TIPO**: o efeito é a tipografia.

**Peso:** *pesado* = muda a tela inteira, conta no limite de densidade. *tempero* = rápido,
pode repetir, serve para preencher os vãos de 4 s.

## Tabela rápida

| # | Efeito | ✂ | Registro | Peso | Duração | Gatilho típico na fala | Melhor posição |
|---|---|---|---|---|---|---|---|
| 01 | Órbita | ✂ | FUNDO | pesado | 3–4 s | "tudo que eu crio", portfólio, resultados, "meus vídeos" | gancho ou payoff |
| 02 | Parede de posts | ✂ | FUNDO | pesado | 2,5–4 s | volume, constância, "todo dia", "postei X vezes" | prova / meio |
| 03 | Dentro do app | – | CENÁRIO | pesado | 3–5 s | passo a passo numa ferramenta, "é só soltar", "manda pro…" | desenvolvimento |
| 04 | Saindo da tela | ✂ | FUNDO | pesado | 2–3 s | quebra de expectativa, "pula pra fora", "sai do padrão", gancho | gancho (0 s) |
| 05 | Zoom digital | – | CÂMERA | tempero | 0,6–1,5 s por zoom | palavra de impacto, verbo-chave, número | qualquer ponto, vãos |
| 06 | Mockup de celular | – | OVERLAY | pesado | 3–5 s | "eu pedi", conversa, mensagem, notificação, resultado no celular | desenvolvimento |
| 07 | Checklist | – | OVERLAY | pesado | 2,5–4 s | lista, passos, "1, 2, 3", "é só…, …, …" | desenvolvimento / resumo |
| 08 | Mural de manchete | ✂ | FUNDO | pesado | 3–4 s | afirmação forte, polêmica, "todo mundo tá falando", notícia | gancho ou re-gancho |
| 09 | Corte no zoom | – | CÂMERA | tempero | 0,4–0,7 s | mudança de assunto, "agora…", "e o melhor…", emenda de dois trechos | transição entre blocos |
| 10 | Gráfico subindo | ✂ | FUNDO | pesado | 3–4 s | crescimento, números, "escala", "dobrou", antes/depois | prova / payoff |
| 11 | Revelação | – | CENÁRIO | pesado | 3–5 s | bastidor, "como eu fiz", processo de edição, ferramenta | re-gancho ou payoff |
| 12 | Chroma key | ✂ | FUNDO | pesado | 3–4 s | produto, site, oferta, link, nome de marca | CTA ou apresentação |
| 13 | Recorte de papel | ✂ | FUNDO | pesado | 2,5–4 s | tom leve, criatividade, "corta e cola", humor | meio (quebra de ritmo) |
| 14 | Rabisco vivo | ✂ | FUNDO | pesado | 2,5–4 s | "olha isso", ênfase pessoal, conquista, autoestima | re-gancho / payoff |
| 15 | Vertigem | ✂ | FUNDO+CÂMERA | pesado | 2–3 s | pergunta provocativa, choque, "nunca…?", tensão | gancho ou virada |
| 16 | Capa de revista | ✂ | FUNDO | pesado | 3–4 s | autoridade, "o fim de…", título do assunto, apresentação | gancho, payoff ou final |
| 17 | Letra de vidro | ✂ | FUNDO+TIPO | pesado | 2,5–3,5 s | palavra-tema única ("CRIA", "ESCALA"), conceito | gancho ou virada |

---

## 01 · Órbita ✂
**O que é:** seus prints girando em volta de você em órbita 3D, passando atrás e na frente.
**Quando usar:** quando a fala apresenta o conjunto do trabalho ("tudo que eu crio", "meus resultados").
Mostra volume e prova social num relance. Precisa de `prints/`.
**Prompt-base:**
> Faz os meus prints (pasta prints) girarem em volta de mim numa órbita 3D: quando estão no fundo
> passam atrás de mim, quando vêm pra frente passam na minha frente. Usa meu recorte por cima do
> vídeo pra isso funcionar. Os cartões saem de trás de mim girando rápido e vão desacelerando. Cor
> quente de fim de tarde, partículas de luz subindo e um título em serifa itálica em cima.
**Remotion:** camadas na ordem vídeo base → cartões com `z<0` → recorte (`recorte/NNNNN.png`) →
cartões com `z>=0`. Ângulo `θ = θ0 + vel·t` com `vel` caindo por `interpolate` + `Easing.out(Easing.cubic)`.
Posição: `x = R·cos θ`, `z = R·sin θ`, escala `= 1 + z/R·0.25`. Grade quente com `mix-blend-mode: soft-light`.

## 02 · Parede de posts ✂
**O que é:** a parede atrás de você vai enchendo de polaroids com seus posts.
**Quando usar:** constância, volume, "todo dia", "já fiz X vídeos". Precisa de `prints/`.
**Prompt-base:**
> Troca o fundo atrás de mim por uma parede de concreto clara e vai pregando polaroids com meus posts
> nela, uma a cada 0,1 segundo, caindo com efeito de mola e um alfinete colorido. Eu fico na frente com
> sombra na parede. Embaixo, uma legenda pequena e outra gigante em Anton.
**Remotion:** fundo de concreto (gradiente + ruído SVG `feTurbulence`). Cada polaroid entra em
`i·3` quadros com `spring({damping: 12})` em escala e rotação aleatória fixa por `random(seed)`.
Sombra do recorte: o próprio PNG com `filter: brightness(0) blur(18px)`, deslocado e com opacidade 0.35.

## 03 · Dentro do app
**O que é:** metade de cima vira uma janela de app clara mostrando o que acontece.
**Quando usar:** quando a pessoa descreve um processo numa ferramenta ("solta os clipes", "manda pro Claude").
**Prompt-base:**
> A metade de cima vira uma janela de app clara, estilo chat do Claude: uma área escrito 'solta seus
> vídeos aqui', 4 miniaturas dos meus clipes caindo nela, uma etiqueta '4 CLIPES' e a caixa de texto
> digitando um comando, com o botão de enviar sendo apertado no fim. Eu fico embaixo com uma legenda grande.
**Remotion:** vídeo base reposicionado na metade de baixo (`objectPosition` no rosto). A janela é
HTML/CSS. Miniaturas = quadros do próprio vídeo (`<OffthreadVideo startFrom>` reduzido) ou prints.
Texto digitando: `texto.slice(0, Math.floor(frame/2))`. Botão: escala 1 → 0.9 → 1 no fim. Não use
marca de terceiros sem o usuário pedir; o padrão é um app genérico com o nome que ele usar na fala.

## 04 · Saindo da tela ✂
**O que é:** o vídeo dentro de um quadro de post com borda neon; aos 0,4 s cabeça e mão saem do quadro.
**Quando usar:** gancho de abertura por excelência. Quebra a moldura = quebra o scroll.
**Prompt-base:**
> Coloca meu vídeo dentro de um quadro de post com borda neon limão, num fundo preto com grade. Aos 0,4
> segundo, minha cabeça e minha mão saem pra fora do quadro (usa meu recorte por cima, preso só na parte
> de baixo), com caquinhos voando, tremida na câmera e o brilho da borda piscando. Título em cima na mesma cor.
**Remotion:** vídeo base com `clip-path` no retângulo do post. Recorte por cima, mas com máscara
`linear-gradient` que esconde a parte de baixo **dentro** do quadro (fica "preso" embaixo).
A partir do quadro 12: recorte visível fora do quadro, 10–14 cacos (polígonos) com velocidade e gravidade,
`translate` de tremida com `random(frame)` por 6 quadros, borda `box-shadow` neon piscando.

## 05 · Zoom digital (tempero)
**O que é:** zooms secos no rosto, cada um com uma palavra gigante.
**Quando usar:** em qualquer palavra de impacto. É o efeito de preencher vão: barato e eficaz.
**Prompt-base:**
> Deixa o vídeo preto e branco com bastante contraste e faz 2 zooms secos no meu rosto (de 1,0 pra 1,3
> e depois pra 1,65), cada um com tremida, um flash branco rápido e borrão de 3 quadros. A cada zoom troca
> uma palavra gigante amarela em Bebas Neue no meio da tela.
**Remotion:** `transform: scale()` com `transformOrigin` no centro do rosto (pegue do quadro de referência).
Zoom em 2 quadros, não em interpolação longa: é seco. Flash: div branca com opacidade 0.8 → 0 em 3 quadros.
Borrão: `filter: blur()` 6 → 0 em 3 quadros. P&B (`grayscale(1) contrast(1.4)`) é opcional: use só no
trecho, não no vídeo todo, a menos que o tom peça.

## 06 · Mockup de celular
**O que é:** zoom no rosto, que vai pra esquerda; à direita entra um iPhone 3D com uma conversa.
**Quando usar:** "eu pedi", "mandei mensagem", "chegou o resultado", qualquer interação por chat.
**Prompt-base:**
> Dá um zoom no meu rosto e joga ele pra esquerda, com uma cor lilás. Do lado direito entra um iPhone 3D
> girado, flutuando, com uma conversa: eu peço pra editar o vídeo, aparecem os três pontinhos, chega a
> resposta e uma miniatura do vídeo com o botão de play. Embaixo, uma legenda curta com uma palavra destacada.
**Remotion:** celular em CSS (bordas arredondadas, notch) com `perspective: 1200px; rotateY(-18deg)`
e flutuação `sin(frame/20)·8px`. Bolhas entram com `spring`. Três pontinhos: 3 círculos com opacidade
em fase. Os textos da conversa vêm do plano e devem repetir o que a pessoa diz.

## 07 · Checklist
**O que é:** cartão de vidro fosco com 3 itens que vão se marcando sozinhos.
**Quando usar:** sempre que a fala enumerar passos. Também serve de resumo antes do CTA.
**Prompt-base:**
> Põe um cartão de vidro fosco (desfocando o que tem atrás) em cima do vídeo, com cor verde-água, e uma
> lista de 3 itens que vão sendo marcados um por um: o círculo enche, o check se desenha, o texto ganha
> um risco e uma barra de progresso vai enchendo. Fecha com uns confetes saindo do cartão.
**Remotion:** `backdrop-filter: blur(24px)` não funciona em todo renderer; simule com uma cópia do
vídeo borrada recortada no retângulo do cartão. Check desenhado: `strokeDashoffset` de `len` → 0.
**Cada item marca na palavra em que é dito** (pegue os tempos na transcrição). Cartão no terço de cima,
sem cobrir a boca.

## 08 · Mural de manchete ✂
**O que é:** parede escura com recortes de jornal batendo atrás de você.
**Quando usar:** afirmação forte, novidade, polêmica, "ninguém te conta isso". Ótimo re-gancho.
**Prompt-base:**
> Troca o fundo atrás de mim por uma parede escura com uma luz vindo de cima e vai batendo recortes de
> jornal nela, com manchetes em fonte de jornal serifada, cada um com uma tremida na câmera. No fim,
> desenha um círculo vermelho de caneta em volta da primeira manchete. Eu fico na frente.
**Remotion:** 4–5 recortes, cada um entra de escala 1.3 → 1 em 4 quadros com tremida de 4 quadros.
Manchetes = frases do próprio vídeo reescritas como manchete (curtas, caixa alta). Círculo: path SVG
irregular com `strokeDashoffset`.

## 09 · Corte no zoom (tempero)
**O que é:** a câmera dá zoom acelerado até um ponto e o próximo trecho sai do zoom no mesmo ponto.
**Quando usar:** entre dois blocos de assunto ou para emendar um corte seco. Esconde jump cut.
**Prompt-base:**
> Faz uma transição de zoom atravessando: o primeiro trecho dá um zoom acelerado até a minha camiseta e o
> segundo trecho sai do zoom no mesmo ponto, desacelerando. Usa umas 5 cópias do vídeo com escala diferente
> pra dar borrão de zoom, raios de luz azul saindo do centro e um flash no corte. Cor azul de cinema.
**Remotion:** janela de ±7 quadros em volta do corte. Escala 1 → 3 com `Easing.in(Easing.cubic)`, depois
3 → 1 com `Easing.out`. Borrão radial = 5 cópias do vídeo com escalas `s·(1+0.03k)` e opacidade 0.2.
Use só onde há mudança real de assunto, senão parece tique.

## 10 · Gráfico subindo ✂
**O que é:** fundo verde-esmeralda com grade e um gráfico de barras crescendo atrás de você.
**Quando usar:** números, crescimento, resultado, "escala". Prova visual de uma afirmação.
**Prompt-base:**
> Troca o fundo por verde-esmeralda escuro com linhas de grade e põe atrás de mim um gráfico de barras dos
> dias da semana (S T Q Q S S D) crescendo uma barra depois da outra, com mola, em degradê limão. Uma linha
> se desenha ligando o topo das barras e no fim pula uma etiqueta 'ESCALA ↗'. Eu fico na frente com um
> brilho verde no contorno.
**Remotion:** barras com `spring` em `scaleY` (origem embaixo), atraso 3 quadros cada. Linha: polyline
SVG com `strokeDashoffset`. Brilho no contorno: recorte com `filter: drop-shadow(0 0 18px #7CFF6B)`.
Rótulos e etiqueta vêm do plano (troque "ESCALA" pela palavra da fala; os dias pelos números reais se houver).

## 11 · Revelação
**O que é:** o vídeo encolhe e revela que é a pré-visualização de um editor inteiro.
**Quando usar:** bastidor, "como eu fiz isso", processo. Excelente re-gancho no meio: muda tudo na tela.
**Prompt-base:**
> Começa com meu vídeo em tela cheia e puxa a câmera pra trás até ele virar a janela de pré-visualização
> de um editor escuro: lista de tarefas do lado (Transcrever, Cortar silêncio, Legenda, Efeitos, Música)
> sendo marcadas, linha do tempo embaixo com faixas coloridas, onda de áudio e o cursor andando. Destaque em laranja.
**Remotion:** a interface é um layout fixo; o vídeo base vai para o retângulo de preview com `interpolate`
de escala/posição (Easing.inOut, 18 quadros). Onda de áudio: `useAudioData` + `visualizeAudio` do
`@remotion/media-utils`. As tarefas da lista podem ser trocadas pelos passos que a pessoa cita.

## 12 · Chroma key ✂
**O que é:** você em cima de uma página de site em degradê roxo e rosa, sem fundo verde.
**Quando usar:** apresentar produto, oferta, link, perfil, "entra no site". Ótimo para o CTA.
**Prompt-base:**
> Tira meu fundo e me coloca no canto de baixo de uma página de site em degradê roxo e rosa, com manchas
> de luz se mexendo, menu em cima, um título grande, uma frase embaixo e um botão. Eu entro deslizando da direita.
**Remotion:** página em HTML (menu, H1, frase, botão) com textos do plano. Manchas = 3 círculos borrados
movendo com `sin/cos`. Recorte escalado ~0.75 no canto inferior, entrada `translateX(100%) → 0` com `spring`.

## 13 · Recorte de papel ✂
**O que é:** colagem em papel kraft, você vira adesivo com borda branca em stop motion.
**Quando usar:** tom leve, criativo, humor, "corta e cola". Quebra o ritmo no meio sem pesar.
**Prompt-base:**
> Faz uma colagem em papel kraft: pedaços de papel rasgado, fita adesiva, rabisco de caneta azul e X
> vermelho. Eu viro um adesivo recortado com borda branca grossa, meio torto, em stop motion (anima a 15
> quadros por segundo). Em cima, uma frase em letras de recorte, cada letra com fonte e papel diferente.
**Remotion:** stop motion = use `Math.floor(frame/2)*2` como quadro do recorte e das animações.
Borda branca: 8 cópias do recorte com `drop-shadow` branco sem blur, ou `filter: drop-shadow(0 0 0 #fff)`
empilhado. Rotação `-3deg`. Letras: cada uma num `span` com fonte, fundo e rotação sorteados por `random`.

## 14 · Rabisco vivo ✂
**O que é:** lousa escura, contorno de giz tremendo em volta de você e rabiscos se desenhando.
**Quando usar:** "olha isso", conquista, ênfase pessoal, momento de orgulho. Funciona como payoff.
**Prompt-base:**
> Troca meu fundo por uma lousa escura e desenha um contorno branco à mão em volta de mim que fica tremendo
> (muda o ruído a cada 3 quadros). Vão aparecendo rabiscos de giz se desenhando sozinhos: coroa amarela na
> minha cabeça, estrela, coração rosa, espiral, claquete, uma seta e uma frase escrita à mão, tudo tremendo junto.
**Remotion:** contorno = recorte com `drop-shadow` branco + `feDisplacementMap` cuja `seed` do
`feTurbulence` muda a cada 3 quadros. Rabiscos = paths SVG com `strokeDashoffset`, coroa posicionada no topo
da cabeça (pegue do quadro de referência). Frase à mão em fonte manuscrita (Caveat / Gochi Hand).

## 15 · Vertigem ✂
**O que é:** dolly zoom: o fundo cresce e você fica do mesmo tamanho.
**Quando usar:** pergunta provocativa, momento de choque, virada. Gera desconforto que prende.
**Prompt-base:**
> Faz o efeito vertigem (dolly zoom): o fundo do meu vídeo vai crescendo devagar enquanto eu fico do mesmo
> tamanho. Pra isso, monta o fundo sem mim juntando vários quadros e preenche o buraco que sobrar. Fundo em
> vermelho escuro, eu em preto e branco, raios saindo do centro e uma pergunta em Oswald com tremida de cor.
**Remotion:** fundo limpo = gere uma vez com ffmpeg/python (mediana de vários quadros com a pessoa
mascarada; o buraco que sobrar, preencha com `cv2.inpaint`) e salve em `public/fundo-limpo.png`.
Fundo escala 1 → 1.35 no trecho, com tinta vermelha (`multiply`). Recorte em `grayscale(1)` sem escala.
Pergunta com tremida RGB: 3 cópias do texto (vermelho, ciano, branco) deslocadas ±3 px.

## 16 · Capa de revista ✂
**O que é:** o quadro vira capa de revista com o nome gigante atrás da cabeça.
**Quando usar:** autoridade, apresentação ("eu sou…"), título do tema, "o fim de…". Ótimo final.
**Prompt-base:**
> Transforma o quadro numa capa de revista: fundo creme de estúdio, o nome da revista gigante em serifa
> atrás da minha cabeça (eu na frente cobrindo um pedaço), chamadas dos lados (uma em vermelho), uma faixa
> de 'ESPECIAL', código de barras e um brilho passando como papel brilhante.
**Remotion:** camadas: fundo creme → nome (serifa Didone, ~360 px, no topo) → recorte → chamadas, faixa,
código de barras. Brilho: faixa branca com gradiente, `rotate(25deg)`, atravessa em 20 quadros com
`mix-blend-mode: overlay`. O nome da revista é o nome/apelido do usuário ou o tema; as chamadas são frases do vídeo.

## 17 · Letra de vidro ✂
**O que é:** uma palavra gigante de vidro atrás de você, refratando o fundo.
**Quando usar:** quando o vídeo gira em torno de uma palavra-conceito. Gancho elegante.
**Prompt-base:**
> Põe uma palavra gigante de vidro atrás de mim: por dentro ela mostra o fundo desfocado e um pouco
> deslocado (como refração), contorno branco fino, reflexo na diagonal e um brilho passando. Ela sobe
> girando, de deitada pra em pé, saindo do desfoque. Fundo em tom gelo e umas bolhas de vidro subindo.
**Remotion:** a palavra é uma máscara (`mask-image` com SVG de texto, ou `background-clip: text`) sobre uma
cópia do vídeo base com `blur(10px)` e `translate(12px, 8px)`. Entrada: `rotateX(80deg) → 0` e `blur(20) → 0`
em 18 quadros. Bolhas: círculos com borda branca translúcida subindo com `random` por bolha.

---

## Efeitos de apoio (sem número, use à vontade)

Não estão no material, mas costuram os efeitos e ajudam a fechar os vãos de 4 s:

- **Palavra-chave na tela:** uma palavra da fala, grande, 0,8–1,2 s, sem mexer no vídeo.
- **Punch-in leve:** escala 1 → 1.08 em 6 quadros no começo de uma frase importante.
- **Jump cut de silêncio:** se houver pausa > 0,5 s, corte (ajuste o plano inteiro depois).
- **SFX:** whoosh na entrada de efeito pesado, pop em item de checklist, impacto no zoom seco.
  Se o MCP da Epidemic Sound estiver disponível, busque lá; senão, deixe a lista de SFX sugeridos no
  relatório. Volume de SFX entre -18 e -12 dB, nunca acima da voz.
