# BRIEF · "Seu carro quitado ainda custa R$ 2.629 por mês"

Carrossel de 10 slides, estático + vivo (um MP4 por slide, 120 BPM, com música e efeitos).
Storyboard do vivo: `STORYBOARD.md` · Fotos reais: `IMAGENS.md` · Contas: `python3 contas.py`.

---

## 1. Estratégia

| Item | Decisão | Origem |
|---|---|---|
| Conta | **@victornaito.financas** (o @ vai só no rodapé do motor, nunca dentro da arte) | do pedido |
| Resultado desejado | **Share** (o principal) + comentário com palavra-chave | do pedido |
| Arquétipo | Teardown: desmonta uma crença ("carro quitado não custa nada") linha por linha, com o recibo como prova | assumido |
| Sentimento | **Desconforto** que vira clareza. Não é culpa, é conta. | assumido |
| Frase única | Parcela zero não é custo zero: metade do que o carro custa nunca aparece na sua conta. | escrita |
| Público | 25 a 45 anos, CLT ou autônomo, tem carro quitado e acha que "agora sobra" | assumido |
| Fidelidade ao padrão-base | média | default |

**Teste de tema.** Alguém procura isso daqui a um ano? Sim, a dúvida "vale a pena ter carro?" volta todo janeiro com o IPVA. Alguém manda um slide pra um amigo? Sim. Todo mundo conhece alguém que diz "meu carro já tá pago". O carrossel é feito pra ser mandado pra essa pessoa.

**Por que vai ser compartilhado (os quatro gatilhos, cada um num slide):**
1. **Identidade.** "Manda pra quem diz que carro quitado não tem custo." O share vira uma cutucada entre amigos (legenda + slide 9).
2. **O recibo que dá print.** O slide 8 é o extrato inteiro num cartão só. Funciona sozinho no story de quem repostar.
3. **A tradução que dói.** "88 corridas de app. Quase 3 por dia." (slide 9). É a linha que gera "caramba" e marcação.
4. **Debate honesto.** "Não é pra vender o carro. É pra saber quanto ele custa." Desarma o hater e mantém a discussão nos comentários, o que empurra o alcance.

**Por que vai parar o scroll:** a capa contradiz uma palavra que a pessoa conhece ("QUITADO") com um número específico e feio (R$ 2.629, não "R$ 2.500"). No vivo, os dígitos rodam como um hodômetro no primeiro segundo, então há movimento mesmo sem som.

### Variações do padrão-base (com motivo)
| Variação | Motivo |
|---|---|
| A espinha é um **recibo/extrato** em papel creme, com Geist Mono e linhas pontilhadas | O tema É um extrato. O recibo é o dispositivo, não decoração. Creme e Geist Mono já estão na receita do padrão-base, então a família visual se mantém. |
| **Hodômetro de dinheiro** no rodapé de todos os slides ("ACUMULADO R$ 0.000") | Amarra carro e conta numa imagem só e cria a antecipação: a pessoa passa o slide pra ver o número subir. |
| Virada com **fundo marinho e tinta "invisível"** | As duas linhas que ninguém vê precisam *parecer* diferentes de tudo que veio antes. |
| **Capa em papel, não em foto escura** | A foto do carro é de estúdio claro (fundo branco). Aplicada em *multiply* sobre o papel do extrato, o carro parece impresso no recibo, o que reforça a metáfora. A garagem à noite fica para os slides internos, se surgirem fotos assim. |
| Payoff e CTA no mesmo slide | O limite é 10 slides e a espinha precisa de 8. O CTA vira uma faixa no pé do slide 10. |

### As seis perguntas
| Posição | Slide | Resposta |
|---|---|---|
| Open | 1 | Ela quer saber de onde sai R$ 2.629 se o carro já tá pago. |
| Hold | 2 | A capa prometeu um custo; o slide 2 mostra que é um extrato de 6 linhas e que 2 são invisíveis. Abre o mapa sem ensinar. |
| Spine | 3 a 4, 6 a 7 | Cada linha soma no hodômetro. Fixos (parado) → variáveis (andando) → subtotal visível → invisíveis. A ordem é a do acumulado: não troca. |
| Rhythm | todos | Foto escura → papel creme → foto → papel → marinho → foto em par → foto quente → papel → linho → marinho. |
| Turn | 5 | "Até aqui é o que você vê." O que parecia o custo do carro era só metade. |
| Payoff | 10 | Crença nova: o carro de R$ 80 mil custa R$ 445 mil em 10 anos. Próximo passo: fazer a conta do próprio carro (comenta EXTRATO). |

**Teste de ordem.** Trocar 3 e 4 quebra a lógica "cobra parado → cobra mais andando" e o subtotal do 4. Trocar 6 e 7 até daria, mas a depreciação vem antes porque é a mais intuitiva (todo mundo sabe que carro desvaloriza) e prepara a menos intuitiva (dinheiro parado). Passa.

---

## 2. Premissas (todas no `contas.py`)

Carro de **R$ 80 mil** (o das fotos é um Nissan Kicks cinza seminovo; conferir na FIPE se o ano/versão bate com ~R$ 80 mil), **1.000 km/mês**, **São Paulo**.

| Linha | Conta | R$/mês |
|---|---|---|
| IPVA + licenciamento | 4% de 80 mil = 3.200/ano + ~160 de taxa | **280** |
| Seguro | ~3.600/ano | **300** |
| Manutenção | revisões, pneus, freios, imprevistos ~2.400/ano | **200** |
| Combustível | 1.000 km ÷ 12 km/L = 83 L × R$ 6,50 | **542** |
| **Você vê** | | **1.322** |
| Depreciação | 10%/ano de 80 mil | **667** |
| Custo de oportunidade | 80 mil × 0,8% a.m. líquido | **640** |
| **Você não vê** | | **1.307** |
| **TOTAL** | | **2.629** |

**10 anos (a conta que aguenta comentário de especialista):**
- Sem o carro: os R$ 80 mil investidos hoje + R$ 1.322/mês investidos por 120 meses a 0,8% a.m. = R$ 208 mil + R$ 265 mil = **R$ 473 mil**.
- Com o carro: ele vale **R$ 28 mil** (−10% ao ano).
- Diferença: **R$ 445 mil**.

> Por que não "R$ 2.629 × 10 anos investidos" (daria R$ 526 mil)? Porque depreciação e custo de oportunidade já estão dentro dos R$ 80 mil rendendo. Somar de novo conta duas vezes, e alguém nos comentários vai apontar. A conta acima é a honesta e ainda é um número enorme.

**Conferir antes de publicar:** gasolina (ANP, a última síntese que achei foi ago/2026: R$ 6,53), Selic/CDI (14% a.a. em ago/2026; 0,8% a.m. líquido fica abaixo do CDI líquido, então é conservador), FIPE do modelo. Troque no `contas.py` e rode.

---

## 3. Estrutura (mapa de slides)

| # | Posição | Fundo | Dispositivo | Hodômetro |
|---|---|---|---|---|
| 1 | Open | papel + foto real do carro em multiply | número gigante + carimbo QUITADO* + "*só a parcela" | 2.629 |
| 2 | Hold | papel creme | cabeçalho do extrato | 0.000 |
| 3 | Spine | foto real, carro parado (mesma garagem) | 2 linhas do recibo sobre a foto | 0.580 |
| 4 | Spine | papel creme + recortes reais (bomba, painel) | 2 linhas + subtotal | 1.322 |
| 5 | **Turn** | marinho, só texto | recibo com tinta "invisível" | ?.??? |
| 6 | Spine | foto real em par (cor × desbotada) | prova em par: mesma cena, uma variável | 1.989 |
| 7 | Spine | foto real quente (chave na mão) | etiqueta de preço pendurada na chave | 2.629 |
| 8 | Spine (clímax) | papel creme | extrato completo + carimbo + chave "você vê / não vê" | 2.629 |
| 9 | Rhythm (alívio) | linho | grade de 88 carrinhos | — |
| 10 | Payoff + CTA | marinho | par de barras R$ 473 mil × R$ 28 mil + faixa CTA | — |

---

## 4. Copy, slide a slide

Regras: uma ideia por frase, ponto final cedo, zero hype, linha de print marcada com ✂.

### Slide 1 · CAPA
- pequeno: **Seu carro quitado**
- médio: **ainda custa**
- GIGANTE: **R$ 2.629**
- assinatura em serifa: ***por mês.***
- carimbo laranja inclinado sobre a lateral do carro: **QUITADO*** · e no papel, em serifa: ***só a parcela**
- pé: hodômetro "ACUMULADO R$ 2.629" e "ABRIR O EXTRATO ▸"
- render: `resultados/estatico/slide-01.png` (v1)

✂ "Seu carro quitado ainda custa R$ 2.629 por mês."

**Capas alternativas pra teste A/B:**
- B (1ª pessoa): "Quitei o carro. Ele continua me cobrando **R$ 2.629** por mês."
- C (contraste seco): "Parcela: R$ 0. Custo real: **R$ 2.629**/mês."

### Slide 2 · HOLD
Cabeçalho do recibo (mono, pequeno):
```
EXTRATO MENSAL · CARRO QUITADO
FIPE R$ 80.000 · 1.000 km/mês · SP
PARCELA ............... R$ 0,00
```
- grande: **Parcela zero.**
- grande, segunda linha: **Custo, não.**
- corpo: Fiz o extrato de um carro de R$ 80 mil, sem 1 real de dívida. Deu 6 linhas.
- corpo, em destaque: **Duas delas não aparecem em app de banco nenhum.**

✂ "Parcela zero. Custo, não."

### Slide 3 · ELE COBRA ATÉ PARADO
- título: **Ele cobra até parado.**
- recibo:
```
01 IPVA + licenciamento ...... R$ 280
02 Seguro .................... R$ 300
```
- nota mono pequena: 4% do valor todo ano em SP + taxa do Detran. Seguro médio de R$ 3.600/ano.
- ✂ **O carro dorme na garagem. O boleto, não.**

### Slide 4 · E COBRA MAIS QUANDO ANDA
- título: **E cobra mais quando anda.**
- recibo:
```
03 Manutenção ................ R$ 200
   revisão, pneu, freio, imprevisto
04 Combustível ............... R$ 542
   83 litros a R$ 6,50
---------------------------------------
   O QUE SAI DA SUA CONTA   R$ 1.322
```
- ✂ **Até aqui, é o custo que você vê.**

### Slide 5 · VIRADA
Fundo marinho. O recibo continua, mas as linhas 05 e 06 aparecem em tinta quase invisível (pontilhado creme a 25%).
- grande: **Agora as duas linhas que o banco não mostra.**
- corpo: Elas não saem da sua conta.
- corpo, na serifa: ***Saem do seu patrimônio.***
- hodômetro piscando: **?.???**

✂ "Não saem da sua conta. Saem do seu patrimônio."

### Slide 6 · DEPRECIAÇÃO
Foto em par, a mesma foto do carro dividida ao meio: à esquerda em cor ("HOJE · R$ 80.000"), à direita desbotada ("DAQUI 1 ANO · R$ 72.000").
- recibo: `05 Depreciação .............. R$ 667`
- título: **Ninguém te manda boleto.**
- corpo: Mas todo mês o seu carro vale R$ 667 a menos.
- nota mono: ~10% ao ano, média de seminovo na FIPE.

✂ "Ninguém te manda boleto. Mas todo mês ele vale R$ 667 a menos."

### Slide 7 · CUSTO DE OPORTUNIDADE
Foto da chave do carro na mão, com uma etiqueta de preço desenhada pelo código: "R$ 80.000".
- recibo: `06 Custo de oportunidade .... R$ 640`
- título: **R$ 80 mil parados na garagem.**
- corpo: Investidos a 0,8% ao mês, pagariam R$ 640. Todo mês. Sem você sair de casa.
- nota mono: 0,8% a.m. líquido fica abaixo do CDI de hoje. A conta é conservadora.

✂ "R$ 80 mil que poderiam te pagar R$ 640 por mês. Estão parados na garagem."

### Slide 8 · O EXTRATO (o slide de print)
O recibo completo, centralizado, com carimbo laranja no total.
```
EXTRATO MENSAL · CARRO QUITADO
01 IPVA + licenciamento ...... R$ 280
02 Seguro .................... R$ 300
03 Manutenção ................ R$ 200
04 Combustível ............... R$ 542
05 Depreciação ............... R$ 667
06 Custo de oportunidade ..... R$ 640
=======================================
   TOTAL MENSAL            R$ 2.629
```
- chave lateral (colchete): linhas 01–04 "você paga: R$ 1.322" · linhas 05–06 "você perde sem ver: R$ 1.307"
- carimbo: **TODO MÊS**
- ✂ **Metade você paga. A outra metade você perde sem ver.**

### Slide 9 · TRADUÇÃO
Fundo linho. Grade de 88 carrinhos de linha (desenho simples, um por corrida), que preenche o slide.
- grande: **R$ 2.629 = 88 corridas de app.**
- corpo: A R$ 30 cada. **Quase 3 por dia. Todo dia.**
- pé, tom calmo: Não é pra vender o carro. É pra saber quanto ele custa.

✂ "Quase 3 corridas de app por dia, todo dia."

### Slide 10 · PAYOFF + CTA
Fundo marinho. Duas barras lado a lado.
- topo: **Em 10 anos:**
- barra alta (laranja): **R$ 473 mil** · "sem o carro, investindo os R$ 80 mil + os R$ 1.322 do mês"
- barra baixa (com miniatura desbotada do carro das fotos): **R$ 28 mil** · "com o carro: um carro de 10 anos"
- crença, na serifa: ***O carro quitado de R$ 80 mil custa R$ 445 mil.***
- faixa CTA no pé: Comenta **EXTRATO** que eu te mando a planilha: põe FIPE, km por mês e estado. Sai o **seu** número.

✂ "O carro quitado de R$ 80 mil custa R$ 445 mil em 10 anos."

---

## 5. Legenda

```
Quitar o carro tira a parcela. Não tira o custo.

Fiz o extrato de um carro de R$ 80 mil, sem dívida nenhuma:
IPVA, seguro, manutenção e gasolina dão R$ 1.322 por mês.
Isso você vê sair da conta.

Depreciação e o dinheiro parado no carro somam mais R$ 1.307.
Isso você não vê. Mas paga igual.

Não é pra vender o carro. Às vezes ele vale cada centavo.
É pra decidir sabendo o preço.

Comenta EXTRATO que eu te mando a planilha.
Você põe a FIPE do seu carro, quantos km roda e o seu estado,
e ela devolve o seu número.

E manda pra quem fala "meu carro já tá pago".

Premissas: carro de R$ 80 mil, 1.000 km/mês, SP, gasolina R$ 6,50,
depreciação 10% a.a., dinheiro investido a 0,8% a.m. líquido.
```

**Primeiro comentário fixado (puxa debate qualificado):**
"Comenta o modelo do seu carro e quantos km você roda por mês que eu respondo com o seu número 👇"

---

## 6. Dependências antes de publicar
- [x] O extrato do CTA: `calculadora.html` (publicada como página; compartilhe o link pelo menu Share antes de mandar por DM).
- [ ] Automação de DM pra palavra EXTRATO (ManyChat ou similar).
- [ ] Fotos do `IMAGENS.md`: gerar no Higgsfield com os prompts prontos (~24 créditos; a conta está com 0) ou fotografar o próprio carro.
- [ ] Rodar `contas.py` com gasolina, CDI e FIPE do mês.
