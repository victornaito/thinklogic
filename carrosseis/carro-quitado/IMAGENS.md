# IMAGENS · fotos do carro

## Em uso: o Nissan Kicks cinza (enviado pelo autor)
- Original: `assets/originais/kicks-cinza.jpg` (552×414, foto de anúncio em estúdio claro).
- Tratada: `assets/kicks-papel.png`. A placa da loja ("DASHEM AUTO") foi coberta por uma placa Mercosul em branco, o fundo foi estourado pra branco (fica invisível em *multiply* sobre o papel) e a imagem foi ampliada 2× com nitidez.
- Recorte bruto sem fundo: `assets/recortes/kicks-sem-fundo.png`. Perde parte do capô; serve só pro parallax do vivo.
- **Resolução baixa.** Aguenta o carro a ~960 px de largura, mas aparece um pouco mole no tamanho real. Se houver a mesma foto maior (o anúncio original costuma ter 1200 px ou mais), troque o arquivo e rode de novo.
- **Direitos.** Parece foto de anúncio de uma loja. Se não for sua, peça autorização à loja ou troque por foto própria ou de banco livre antes de publicar.

---

## Alternativas (não usadas por enquanto)

### Higgsfield

**Status:** não geradas. A conta do Higgsfield está com **0 créditos** (plano free, sem gerações ilimitadas). Os prompts abaixo estão prontos pra rodar assim que houver saldo.

**Orçamento:** 5 cenas × 2 variações × 2 créditos (Nano Banana Pro, 2k, 4:5) = **20 créditos**, mais ~3 créditos de recorte sem fundo = **~23 a 25 créditos**.

**Regra:** o mesmo carro em todas as fotos. A F1 é gerada primeiro e entra como referência na F1b e na F3; é isso que mantém o carro igual. A prova em par do slide 6 é a própria F1, desbotada em código.

**O carro:** hatch compacto prata, 5 portas, cara de seminovo 2022 do mercado brasileiro, **sem logo e com placa em branco**. Prata porque é a cor mais comum na rua: o público se reconhece. Nada de esportivo ou de luxo, que quebraria a identificação com um carro de R$ 80 mil.

Fórmula de cada prompt: o que fica igual (quando há referência) · cena com coisas reais · layout em números · nunca texto.

---

## F1 · Capa / slides 1, 3, 6, 10 (gerar primeiro)
Modelo `nano_banana_pro` · 2k · 4:5 · 2 variações

```
Photorealistic night photo shot on an iPhone 15 Pro in night mode, 26mm lens, vertical 4:5.
A silver compact 5-door hatchback, generic Brazilian-market car around 2022, no brand badges,
license plate blank, parked inside a narrow residential garage in Brazil. Three-quarter front
view, camera at headlight height. Headlights off. A single warm tungsten bulb on the ceiling at
the top left is the only light; the rest falls into soft shadow. Bare painted wall, concrete
floor with a faint oil stain, a folded blue tarp and a plastic bucket against the side wall.
Layout: the car fills the lower 55% of the frame, slightly right of center; the top 40% is dark,
empty wall and ceiling with no objects. Foreground: the coil of a green garden hose at the
bottom left, out of focus and cut by the frame edge. Realistic reflections on the paint, light
sensor grain. No text, no logos, no people.
```
Depois: **remover fundo** do carro (1 crédito) → `assets/recortes/f1-carro-sem-fundo.png`; `fundo-limpo.py` pra garagem sem o carro (parallax da capa).

## F1b · Capa no vivo (faróis acesos)
Modelo `nano_banana_pro` · 2k · 4:5 · referência: a F1 escolhida · 1 variação

```
Keep exactly the same: the silver hatchback, its position and angle, the camera position and
framing, the garage walls, the ceiling bulb, the floor, the oil stain, the tarp, the bucket and
the blurred hose in the foreground. Change only one thing: the car's headlights and daytime
running lights are switched on, throwing a soft pool of light on the concrete floor in front of
the car. No text, no logos, no people.
```

## F2 · Slide 4 (painel / hodômetro)
Modelo `nano_banana_pro` · 2k · 4:5 · 2 variações

```
Photorealistic night photo from the driver's seat of a compact car, close-up of the instrument
cluster with the ignition on and the engine off: analog speedometer and tachometer with white
backlight, small digital display between them glowing but with blurred, unreadable digits.
Dark cabin. The top of the steering wheel rim crosses the lower 20% of the frame, out of focus,
with no logo on the hub. Layout: the cluster fills the middle 50% of the frame. Shot on iPhone,
shallow depth of field, slight grain. No readable text, no numbers, no logos.
```
Depois: remover fundo do cluster → recorte pro canto do slide 4.

## F3 · Slide 4 (bomba de combustível)
Modelo `nano_banana_pro` · 2k · 4:5 · referência: a F1 escolhida · 2 variações

```
Keep the same car as the reference: the same silver compact hatchback, same paint color and
finish. New scene: close-up of a black gas station fuel nozzle inserted into the open fuel door
of this car, at night, under the cold white LED canopy light of a Brazilian gas station. No hand
on the nozzle. The black rubber hose curves up and out of the frame. Fuel pumps in the
background are blurred with no readable signage. Layout: the nozzle and fuel door sit in the
upper-right 50% of the frame; the lower-left 40% is a clean, smooth car body panel. No text, no
logos, no prices.
```
Depois: remover fundo do bico → recorte que desliza e trava no slide 4.

## F4 · Slide 7 (chave na mão)
Modelo `nano_banana_pro` · 2k · 4:5 · 2 variações

```
Photorealistic close-up of an open adult palm, held flat, holding a plain black car key fob on
a steel key ring, no brand logo on the fob. Warm side light from a window on the left, a dark
wooden table out of focus below. Layout: the hand and key sit in the lower 50% of the frame;
the upper 45% is dark, empty space. Natural skin texture, no jewelry, no watch, no face.
Shot on iPhone, 50mm equivalent, shallow depth of field. No text, no logos.
```
A etiqueta de preço "R$ 80.000" que desce do chaveiro é desenhada em código.

---

## Como escolher
- Duas variações por cena: fica a limpa (sombra crível, reflexo coerente, nada derretido nas rodas, nos retrovisores ou nos dedos).
- Roda, retrovisor e grade são onde a IA mais erra. Confira no tamanho real.
- Se a F1b ou a F3 vierem com outro carro (cor, formato do farol), gere de novo só aquela.
- Salvar em `assets/geradas/`; as escolhidas em `assets/` com o código da cena; folha de contato em `assets/folha-fotos-escolhidas.jpg`.

## O que não usa foto
Os slides 2, 5, 8 e 9 são papel, marinho e linho, com texto e desenho em código. Isso cria o ritmo foto, papel, foto, papel, e deixa o slide 8 (o de print) limpo pra ser repostado.

## Fotos reais da internet (candidatas, licença livre)

A rede desta sessão bloqueia `images.unsplash.com`, `images.pexels.com` e `upload.wikimedia.org`, então eu achei as fotos pela busca mas ainda **não consegui baixar nem olhar nenhuma**. Elas precisam passar pelo olho antes de entrar no carrossel.

| Cena | Primeira opção | Alternativas | Licença |
|---|---|---|---|
| F1 · capa, slides 3, 6, 10 | [carro prata numa garagem escura](https://unsplash.com/photos/a-silver-car-parked-in-a-dark-garage-qvfSbpqY9sk) (Kia K8, Hyundai Motor Group) | [carro prata em garagem](https://unsplash.com/photos/silver-car-parked-in-garage-hPeahMW3Z-M) · [carro em garagem à noite](https://unsplash.com/photos/a-car-parked-in-a-parking-garage-at-night-_SYkjw8i8rA) | Unsplash |
| F2 · painel (slide 4) | [velocímetro aceso](https://www.pexels.com/photo/close-up-photo-of-illuminated-speedometer-4141872/) | [velocímetro, conta-giros e hodômetro](https://www.pexels.com/photo/photo-of-a-car-speedometer-a-rev-counter-and-a-odometer-14992303/) · [velocímetro iluminado](https://www.pexels.com/photo/illuminated-car-speedometer-18031874/) | Pexels |
| F3 · bomba (slide 4) | [abastecendo à noite](https://www.pexels.com/photo/close-up-of-a-person-refueling-the-car-at-a-gas-station-20500733/) | [abastecendo um carro](https://www.pexels.com/photo/fueling-a-vehicle-at-a-gas-station-29370543/) · [bico no tanque](https://www.pexels.com/photo/person-refilling-gasoline-on-gas-tank-3784137/) | Pexels |
| F4 · chave (slide 7) | [chave na mão, foco raso](https://www.pexels.com/photo/shallow-focus-car-key-held-by-a-man-97075/) | [chave na mão](https://www.pexels.com/photo/car-key-on-hand-6097/) · [pessoa segurando chave](https://www.pexels.com/photo/person-holding-a-car-key-12969398/) | Pexels |

Cuidados com essas fotos:
- **A F1 é um Kia K8, um sedã mais caro que R$ 80 mil.** Funciona pelo clima (prata, garagem escura), mas se alguém reconhecer o modelo, a identificação com "carro de R$ 80 mil" enfraquece. Se uma das alternativas for um hatch compacto, ela ganha.
- As fotos vão ser de carros diferentes. O slide 6 continua funcionando, porque a comparação é a F1 colorida contra ela mesma desbotada.
- Borrar placas e evitar logo em destaque. As licenças da Unsplash e da Pexels permitem uso comercial, mas não permitem sugerir que a marca apoia o post.
- Wikimedia tem fotos reais do Onix brasileiro (por exemplo, [Onix LT 2015](https://commons.wikimedia.org/wiki/File:Chevrolet_Onix_20150814-DSC05650.JPG)). Mas a licença CC BY-SA exige crédito e que a arte derivada use a mesma licença, então fica como última opção.

**Para eu baixar e montar:** libere `images.unsplash.com`, `images.pexels.com` e `unsplash.com` em Network access, nas configurações do ambiente. Ou baixe as fotos e envie aqui.

## Plano B, sem créditos
Fotos reais de banco com licença livre pra uso comercial (Unsplash, Pexels), todas de uma mesma sessão de um fotógrafo só, pra que seja o mesmo carro.
Buscas: `hatchback garage night`, `car parked garage dark`, `car key hand`, `car dashboard night`, `fuel nozzle car`.
Borrar a placa. Conferir a licença na página de cada foto.
