# STORYBOARD · versão viva (animação, música e efeitos)

Um MP4 por slide, 1080×1350, 30 fps, 120 BPM (1 batida = 0,5 s, 1 compasso = 2 s).
Capa e slide 10: 8 s (4 compassos). Cartões: 6 s (3 compassos). Total: 64 s.
O quadro 0 de cada MP4 é o PNG estático aprovado; todo movimento volta ao repouso antes de 0,8 s do fim, pra o loop fechar sem emenda.

Regras de movimento: nada linear, nada entrando com fade, sem brilho, neon ou partícula. Entradas por carimbo (escala com peso), deslize com easing, máscara e desenho de linha.

---

## Música

**Faixa recomendada:** "Bulletin World", de Out To The World (Epidemic Sound), 120 BPM, eletrônica tensa e contida.
`id a82223bd-9e60-3af6-bca9-2d25036077e8`, com stems de baixo, bateria, melodia e instrumentos.

O truque é usar os **stems** pra música contar a história junto com o recibo:

| Slides | Stems ligados | Por quê |
|---|---|---|
| 1 a 4 | baixo + instrumentos (sem bateria) | Tensão contida, parece "tá tudo sob controle". |
| 5 (virada) | tudo corta na batida 0; na batida 2 (1,0 s) entra a **bateria completa** | O drop da música coincide com a virada da história. |
| 6 a 8 | mix completo | O número sobe, a música pesa. |
| 9 | só melodia + baixo | Alívio: "não é pra vender o carro". |
| 10 | mix completo, resolvendo no último compasso | Fecho. |

**Alternativas:**
- "Axon Terminal", Out To The World (`bc333bec-1d67-4019-b369-9ddb194aa1c1`), 120 BPM, ambiente escuro. Mais sombria.
- "Running Time", Out To The World (`0308b5d1-2b35-3a0b-b06e-6ac0976526f5`), 120 BPM, suspense com cara de relógio correndo.
- Sem licença Epidemic: `musica.py` do motor do carrossel sintetiza uma faixa em ré menor a 120 BPM. Nesse caso a bateria entra no slide 5 do mesmo jeito.

**Mixagem:** música a −14 LUFS no total; abaixa 6 dB por 300 ms em cada impacto (carimbo, ka-ching); efeitos por cima, sem limitar o transiente. Não pôr música do Instagram por cima dos MP4.

## Banco de efeitos (Epidemic Sound, ids pra baixar)

| Código | Som | Uso | id |
|---|---|---|---|
| IMP-carimbo | carimbo de borracha no papel (0,2 s) | carimbos, pouso de número | `d530c5b9-3047-42fe-a06a-7c479d637b60` |
| IMP-carimbo-forte | carimbo pressionado (variações) | QUITADO, TODO MÊS | `87fddb71-8128-45ce-bd48-2809b5486f1d` |
| KACHING | caixa registradora "ka-ching" (2,2 s) | só 2 vezes: total do slide 8 e R$ 473 mil | `6caad476-d3e4-44ad-afa1-1e9187c46bd0` |
| RECIBO | impressora de cupom imprimindo (cortar 0,5 a 1 s por linha) | cada linha do recibo | `ff0f74c4-982e-4b24-a567-4a49e755b92f` |
| RECIBO-curto | caixa registradora antiga imprimindo (3,4 s) | cabeçalho do extrato | `54644c85-f1a0-4cbc-adb0-4376fe506ade` |
| HODOMETRO | catraca de calculadora mecânica (cortar em cliques) | dígitos rolando | `259d181b-7eb5-49df-8d66-41b7a01ff61e` |
| GARAGEM | portão de garagem metálico fechando (3,4 s) | abertura do slide 3 | `4b8daa6b-9ecd-4c6c-a7a3-81f5f8f4bc43` |
| BOMBA | bomba de combustível ligando (cortar o "clunk" de destravar) | combustível no slide 4 | `dd9aa9c0-8458-4354-bd44-4671204ae5d1` |
| CHAVE | chave de carro tilintando (1 s) | slide 7 | `24abb572-5a50-4a8a-a5a7-1a5357fbff93` |
| CHAVE-pouso | chaves caindo de leve (0,6 s) | pouso da etiqueta no slide 7 | `fc6a99ce-5221-47f9-a19f-cef2e4c9ddcc` |
| IGNICAO | partida de carro (cortar só o giro do motor de arranque, ~1 s) | capa, batida 0,5 | `48eb6df7-4631-45d9-a338-c5a2df00b5e0` |
| WHOOSH | whoosh seco curto | transições, recibo atravessando | `1aa76afb-e551-48b9-b0a7-0759f7605475` |
| WHOOSH-impacto | whoosh com impacto | entrada da virada | `35e5d4a6-38e2-4aeb-8540-e415b3e85b83` |
| MOEDAS | moedas caindo numa caixa (2 s) | barra de R$ 473 mil crescendo | `fbb4cc9c-74a9-4aef-9ad5-e68e98b534d4` |

Regra: o KACHING aparece só duas vezes. Se tocar em toda linha, perde o peso.

---

## Dispositivo que atravessa tudo: o hodômetro

No rodapé esquerdo de todos os slides (longe do ícone de som, que fica no canto inferior direito): um hodômetro de carro, dígitos brancos em fundo preto, rolos mecânicos. Ele mostra o **acumulado em R$**. Em cada slide, os rolos giram do valor do slide anterior pro novo, com uma catraca de clique por dígito que muda. É a âncora de retenção: a pessoa passa pra ver o número subir.

---

## Slide 1 · CAPA (8 s, compassos 1 a 4)
Ordem de leitura: número → "por mês" → carimbo → recibo.

| t (s) | O que se mexe | Som |
|---|---|---|
| 0,0 | quadro 0 = PNG estático (número já em R$ 2.629) | música entra (baixo + instrumentos) |
| 0,5 | farol do carro acende (camada em *screen* sobre a foto, 2 batidas) | IGNICAO |
| 0,5 a 7,5 | câmera empurra devagar com parallax em 3 camadas: fundo da garagem 4%, carro recortado 5,5%, texto 7%; volta ao repouso | — |
| 1,0 a 2,0 | os dígitos do R$ 2.629 giram como hodômetro (cada rolo dá uma volta inteira, da esquerda pra direita, uma batida de atraso entre eles) e assentam no mesmo número | HODOMETRO, 4 cliques |
| 2,0 | "por mês." sobe de uma máscara, esticando, e achata no pouso | clique |
| 3,0 | o carimbo QUITADO levanta (cresce 14%, gira −6°) e **carimba** sobre o capô | IMP-carimbo-forte |
| 3,5 | "(só a parcela)" se escreve à mão, traço a traço | lápis curto (opcional) |
| 4,5 a 6,0 | a ponta do recibo sai da borda de baixo, 3 linhas pontilhadas imprimindo | RECIBO, 3 pulsos |
| 6,5 e 7,0 | a seta "EXTRATO MENSAL ▸" pulsa e empurra pra direita | 2 cliques |
| 7,2 a 8,0 | repouso | — |

## Slide 2 · HOLD (6 s, compassos 5 a 7)

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | o papel entra pela esquerda com sobrepasso (continua o recibo da capa) | WHOOSH |
| 0,5 a 1,5 | o cabeçalho imprime linha a linha, de cima pra baixo, com a borda serrilhada descendo | RECIBO-curto |
| 1,5 | "PARCELA ........ R$ 0,00": o R$ 0,00 carimba | IMP-carimbo |
| 2,0 | "Parcela zero." cai e achata | clique |
| 2,5 | "Custo, não." cai e achata (pra direita, pra não comer o espaço) | impacto grave |
| 3,0 e 3,5 | as duas frases de corpo sobem da máscara, uma por batida | 2 cliques |
| 4,0 | "Duas delas não aparecem..." ganha um marca-texto laranja que se desenha atrás | risco de marcador |
| 4,5 | hodômetro mostra 0.000 (pisca uma vez) | clique |
| 5,2 a 6,0 | repouso | — |

## Slide 3 · ELE COBRA ATÉ PARADO (6 s, compassos 8 a 10)
Foto: o mesmo carro da capa, parado na garagem, mais escuro.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | a sombra de um portão de garagem desce sobre a foto até 60% (camada *multiply*) e para | GARAGEM (só o fim, o "clank") |
| 1,0 | "Ele cobra até parado." entra palavra por palavra (4 batidas curtas) | cliques |
| 2,0 | linha 01 imprime da esquerda pra direita, pontilhado se desenhando até o valor | RECIBO |
| 2,5 | R$ 280 carimba | IMP-carimbo |
| 3,0 | linha 02 imprime | RECIBO |
| 3,5 | R$ 300 carimba | IMP-carimbo |
| 4,0 a 4,5 | hodômetro rola de 0.000 a 0.580 | HODOMETRO |
| 4,5 | linha de print sobe da máscara | clique |
| 5,0 a 6,0 | sombra do portão sobe de volta; repouso | — |

## Slide 4 · E COBRA MAIS QUANDO ANDA (6 s, compassos 11 a 13)
Papel creme + recortes reais: o bico da bomba (canto superior direito) e o painel com o hodômetro do carro (inferior esquerdo, ao lado do hodômetro de dinheiro).

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | o papel atravessa da direita (troca de fundo) | WHOOSH |
| 0,5 | título cai e achata | impacto grave |
| 1,0 | o recorte do bico da bomba desliza pra dentro e dá um tranco (trava) | BOMBA ("clunk") |
| 1,5 | linha 03 imprime; R$ 200 carimba em 2,0 | RECIBO, IMP-carimbo |
| 2,5 | linha 04 imprime; enquanto isso o "83 litros" conta de 0 a 83 em 1 batida | RECIBO + chiado curto da bomba |
| 3,0 | R$ 542 carimba | IMP-carimbo |
| 3,5 | a linha tracejada de subtotal se desenha da esquerda pra direita | risco |
| 4,0 | "O QUE SAI DA SUA CONTA R$ 1.322" carimba | IMP-carimbo-forte |
| 4,0 a 4,5 | hodômetro rola até 1.322; o painel recortado gira os km junto | HODOMETRO |
| 5,2 a 6,0 | repouso | — |

## Slide 5 · VIRADA (6 s, compassos 14 a 16)
Fundo marinho, só texto. É o slide que precisa parecer diferente de todos.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 | **música corta seco** (só um resto de reverb) | silêncio |
| 0,0 a 0,5 | tudo escurece pro marinho numa varrida vertical (de cima pra baixo, não fade) | WHOOSH-impacto |
| 1,0 | **a bateria entra** | (música, drop) |
| 1,0 | "Agora as duas linhas" cai palavra por palavra no tempo da caixa | clique por palavra |
| 2,0 | "que o banco não mostra." cai; a última palavra carimba | impacto |
| 2,5 a 3,5 | linhas 05 e 06 imprimem em pontilhado creme a 25%: dá pra ver que tem coisa escrita, mas não dá pra ler | RECIBO abafado (passa-baixa) |
| 3,5 | "Elas não saem da sua conta." sobe da máscara | clique |
| 4,0 | "*Saem do seu patrimônio.*" sobe em serifa, esticando | impacto grave |
| 4,5 | hodômetro gira descontrolado e trava em ?.??? | HODOMETRO acelerado, trava |
| 5,2 a 6,0 | repouso | — |

## Slide 6 · DEPRECIAÇÃO (6 s, compassos 17 a 19)
Prova em par: a mesma foto do carro, metade em cor, metade desbotada.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | a foto inteira entra em cor | WHOOSH |
| 0,5 a 1,5 | uma linha vertical varre da esquerda pro meio e, por onde passa, a foto perde cor e contraste (de 100% pra 35% de saturação) | risco longo |
| 1,5 | etiquetas "HOJE · R$ 80.000" e "DAQUI 1 ANO · R$ 72.000" carimbam, uma por batida | 2 × IMP-carimbo |
| 2,5 | no lado desbotado, o R$ 72.000 conta pra baixo a partir de 80.000 em 1 batida | HODOMETRO |
| 3,0 | linha 05 imprime; R$ 667 carimba em 3,5 | RECIBO, IMP-carimbo |
| 4,0 | "Ninguém te manda boleto." cai e achata | impacto grave |
| 4,5 | corpo sobe da máscara | clique |
| 4,5 a 5,0 | hodômetro de ?.??? pra 1.989 | HODOMETRO |
| 5,5 a 6,0 | repouso (a respiração da foto termina em 5,5) | — |

## Slide 7 · CUSTO DE OPORTUNIDADE (6 s, compassos 20 a 22)
Foto quente: a chave do carro na mão, ou numa mesa de madeira.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | a foto entra pela direita | WHOOSH |
| 0,5 | a chave balança (rotação de ±4° com mola, só a camada recortada) | CHAVE |
| 1,0 | a etiqueta de preço desce pendurada no chaveiro, balança duas vezes e para | CHAVE-pouso |
| 1,5 | "R$ 80.000" se escreve na etiqueta | clique |
| 2,0 | título "R$ 80 mil parados na garagem." cai e achata | impacto grave |
| 2,5 | linha 06 imprime; R$ 640 carimba em 3,0 | RECIBO, IMP-carimbo |
| 3,5 e 4,0 | as duas frases de corpo sobem da máscara | 2 cliques |
| 4,5 a 5,0 | hodômetro de 1.989 pra 2.629, os 4 rolos girando | HODOMETRO |
| 5,5 a 6,0 | repouso | — |

## Slide 8 · O EXTRATO (6 s, compassos 23 a 25)
O clímax e o slide de print. O quadro 0 tem que funcionar sozinho no story.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | o recibo inteiro sobe de baixo como se saísse da impressora, rápido | RECIBO (aceleração) |
| 0,5 a 2,0 | as 6 linhas se acendem uma por batida (passa um marca-texto rápido em cada valor) | 3 cliques em subida (escala pentatônica) |
| 2,0 | a linha dupla "=====" se desenha | risco |
| 2,5 | **TOTAL MENSAL R$ 2.629** carimba | KACHING (1ª de 2) |
| 3,0 | o colchete "você paga: R$ 1.322" se desenha ao lado das linhas 01 a 04 | risco |
| 3,5 | o colchete "você perde sem ver: R$ 1.307" se desenha ao lado de 05 e 06, em laranja | risco + impacto |
| 4,0 | o carimbo TODO MÊS levanta e bate | IMP-carimbo-forte |
| 4,5 | linha de print sobe | clique |
| 5,2 a 6,0 | repouso | — |

## Slide 9 · TRADUÇÃO (6 s, compassos 26 a 28)
Linho. Grade de 88 carrinhos de linha. A música perde a bateria (alívio).

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | o linho entra numa varrida | WHOOSH |
| 0,5 | "R$ 2.629 =" carimba | impacto |
| 1,0 a 3,0 | os 88 carrinhos aparecem em ondas, linha a linha (uma linha de 11 por meia batida, 8 linhas), cada um estalando de leve | "tic" curto por linha (8 no total) |
| 3,0 | "88 corridas de app." carimba | impacto grave |
| 3,5 | "Quase 3 por dia. Todo dia." sobe; "3" ganha círculo laranja desenhado à mão | clique + risco |
| 4,5 | "Não é pra vender o carro..." sobe devagar, tom calmo | nenhum (respiro) |
| 5,2 a 6,0 | repouso | — |

## Slide 10 · PAYOFF + CTA (8 s, compassos 29 a 32)
Marinho. Mix completo, resolvendo no último compasso.

| t | O que se mexe | Som |
|---|---|---|
| 0,0 a 0,5 | marinho entra pela direita | WHOOSH |
| 0,5 | "Em 10 anos:" cai | clique |
| 1,0 a 2,5 | a barra laranja cresce do chão, com o valor contando junto de R$ 0 a R$ 473 mil | MOEDAS |
| 2,5 | R$ 473 mil carimba no topo da barra | KACHING (2ª de 2) |
| 3,0 | a barra baixa sobe só um pouquinho; a miniatura do carro desbotado pousa nela; R$ 28 mil aparece | IMP-carimbo (seco, sem graça, de propósito) |
| 3,5 a 4,5 | a frase-crença em serifa se escreve: "O carro quitado de R$ 80 mil custa **R$ 445 mil**." O 445 carimba em 4,5 | cliques + impacto |
| 5,0 | faixa CTA sobe do pé | WHOOSH curto |
| 5,5 | "EXTRATO" é digitada letra a letra, uma por meia batida | tecla por letra |
| 6,5 e 7,0 | a palavra EXTRATO pulsa duas vezes | 2 cliques |
| 7,2 a 8,0 | repouso, a música resolve no primeiro acorde | — |

---

## Ordem de render
1. Estático aprovado → PNGs.
2. `K.slide({ cues })` em cada slide com os tempos acima.
3. `zsh scripts/vivo.sh all` (cues → música/stems → MP4 → folhas por batida → testes).
4. Testes: quadro 0 = PNG (diferença zero), último quadro = quadro 0, sem degrau de som na emenda.
5. Subir os 10 MP4 em ordem, sem música do Instagram.
