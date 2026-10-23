# BRIEF · "Abaixo de 1.073 km por mês, caro é o seu carro"

Carrossel de 10 slides, estático + vivo (um MP4 por slide, 120 BPM). Conta: **@victornaito.financas**.
Segundo post da série do carro: mesmo carro (o Kicks cinza de R$ 80 mil), mesmas premissas do "extrato do carro quitado".
Storyboard: `STORYBOARD.md` · Fotos: `IMAGENS.md` · Contas: `python3 contas.py`.

---

## 1. Estratégia

| Item | Decisão | Origem |
|---|---|---|
| Resultado desejado | **Share** + comentário (debate e palavra-chave) | do pedido |
| Arquétipo | Teardown: derruba a crença "Uber é caro, carro é economia" com uma conta que tem resposta exata | assumido |
| Sentimento | **Contrariado** → aliviado. A pessoa descobre o próprio número. | assumido |
| Frase única | O carro cobra antes de andar; o app só cobra quando anda. Por isso existe um km exato em que um vira o outro. | escrita |
| Público | 25 a 45 anos, cidade com app, carro quitado ou pensando em comprar | assumido |
| Fidelidade ao padrão-base | média, mesma identidade do post do extrato (papel, marinho, laranja, cupom, hodômetro) | continuidade |

**Teste de tema.** Alguém procura isso daqui a um ano? Sim: "vale a pena ter carro ou andar de Uber" é busca eterna e volta toda vez que a gasolina sobe. Alguém manda pra um amigo? Sim, e por dois motivos opostos: quem anda de app manda pra provar que está certo, e quem tem carro manda pra contestar. O post dá munição pros dois lados, e é isso que gera share e comentário.

**O hook: dor + contradição.**
- **Contradição:** todo mundo acha o Uber caro. A conta mostra que, pra quem roda pouco, caro é o carro. A capa começa com a crença riscada.
- **Dor:** o carro cobra R$ 1.887 por mês antes de sair da garagem. É dinheiro que vai embora sem nenhum km rodado.
- **Número exato:** 1.073 km. Número quebrado parece conta de verdade, não chute.

**Por que vai ser compartilhado:**
1. **Veredito com número:** "abaixo de 1.073 km, o app ganha" é uma regra que cabe numa frase e dá pra repassar.
2. **A tabela de cenários (slide 7)** deixa cada um se achar: 300, 600, 1.000, 1.500, 2.000 km. É o slide de print.
3. **A tradução em trajeto (slide 8):** "1.073 km = trabalho a 24 km de casa, todo dia útil, e mais nada". Faz a pessoa pensar no próprio trajeto e marcar alguém.
4. **A surpresa do slide 9:** só o rendimento dos R$ 80 mil paga 256 km de app por mês.
5. **Debate honesto (slide 9):** o que a conta não pega, como filhos, viagem, dinâmica e estacionamento. Isso desarma o hater e alimenta os comentários.

### Variações do padrão-base (com motivo)
| Variação | Motivo |
|---|---|
| Capa com **frase riscada** em cima do número | A contradição precisa ser vista antes de ser lida: o risco laranja na crença ("Você acha o Uber caro.") é o gancho visual. |
| **Gráfico de duas retas** como virada (slide 6) | O tema tem um ponto de cruzamento de verdade. Desenhar as retas se cruzando é a prova mais forte e mais compartilhável. |
| **Duelo de taxímetros** (slides 4 e 5) | O custo por km é abstrato. Dois contadores correndo lado a lado (R$ 0,74 contra R$ 2,50 por km) tornam a diferença física. |
| Hodômetro em **km** no rodapé (não em R$) | Continua o dispositivo da série, mas agora conta km: 0 → 1.073 km até a virada. |
| App sem logo | Uber e 99 aparecem só no texto. O app é desenhado em código, genérico, sem marca. |

### As seis perguntas
| Posição | Slide | Resposta |
|---|---|---|
| Open | 1 | Ela quer saber se está abaixo ou acima de 1.073 km, e por que o "caro" mudou de lado. |
| Hold | 2 | A capa prometeu um número; o slide 2 mostra que a conta tem duas partes (fixa e por km) e que existe um cruzamento. Não ensina ainda. |
| Spine | 3 a 5 | Parte fixa do carro (R$ 1.887 parado) → custo por km do carro (R$ 0,74) → custo por km do app (R$ 2,50). Cada um abre o próximo. |
| Rhythm | todos | Papel, marinho e laranja alternando; foto real do carro na capa e nos slides 3 e 9; gráfico, tabela e mapa no meio. |
| Turn | 6 | As retas se cruzam em 1.073 km. Até ali o app parecia caro; depois do cruzamento, a parte fixa do carro explica tudo. |
| Payoff | 10 | Crença nova: carro só compensa acima do seu ponto de virada. Próximo passo: calcular o próprio ponto (comenta KM). |

**Teste de ordem.** 3 → 4 → 5 não troca: a parte fixa tem que vir antes pra explicar por que R$ 0,74/km não é "barato". 6 depende dos três. 7 e 8 dependem do 6. Passa.

---

## 2. Premissas (todas no `contas.py`)

| Item | Valor | Observação |
|---|---|---|
| Carro | R$ 80 mil, 12 km/l, gasolina R$ 6,50, SP | igual ao post do extrato |
| **Parte fixa** | IPVA + lic. R$ 280 · seguro R$ 300 · depreciação R$ 667 · dinheiro parado R$ 640 = **R$ 1.887/mês** | chega rodando ou não |
| **Parte por km** | combustível R$ 0,54 + manutenção R$ 0,20 = **R$ 0,74/km** | manutenção = R$ 2.400/ano ÷ 12.000 km |
| **App** | **R$ 2,50/km** (corrida urbana, tarifa base e tempo incluídos) | recibos de 2026: R$ 1,80/km e R$ 3,07/km; conferir no app da sua cidade |
| **Ponto de virada** | 1.887 ÷ (2,50 − 0,74) = **1.073 km/mês** | 36 km/dia |
| Com dinâmica 1,5x | R$ 3,75/km → **627 km/mês** | |
| App a R$ 2,00 / R$ 3,00 por km | 1.500 / 836 km/mês | sensibilidade |

**Coerência com o post anterior:** a 1.000 km o carro custa R$ 2.629 (exatamente o extrato) e o app, R$ 2.500.

**Conferir antes de publicar:** preço médio por km do app na sua cidade (abrir o app e simular 3 trajetos comuns), gasolina, CDI e FIPE. Troque no `contas.py`.

---

## 3. Estrutura (mapa de slides)

| # | Posição | Fundo | Dispositivo | Hodômetro (km) |
|---|---|---|---|---|
| 1 | Open | papel + Kicks real em multiply | crença riscada + número gigante | 1.073 |
| 2 | Hold | marinho | balança: carro (fixo + km) × app (só km) | 0 |
| 3 | Spine | papel + Kicks real | cupom da parte fixa + carimbo PARADO | 0 |
| 4 | Spine | marinho | taxímetro do carro: R$ 0,74/km | 0 |
| 5 | Spine | papel | duelo de taxímetros: carro × app | 0 |
| 6 | **Turn** | marinho | gráfico de duas retas cruzando em 1.073 km | 1.073 |
| 7 | Spine (print) | papel | tabela de cenários com selo de vencedor | 1.073 |
| 8 | Rhythm | marinho | mapa: casa → trabalho, 24 km × 22 dias | 1.073 |
| 9 | Alívio | linho | duas colunas: o que a conta não pega + o rendimento que paga 256 km | — |
| 10 | Payoff + CTA | laranja (metade) + marinho | veredito em duas linhas + faixa CTA | 1.073 |

---

## 4. Copy, slide a slide

Linha de print marcada com ✂.

### Slide 1 · CAPA (contradição)
- linha média, **riscada à mão em laranja**: Você acha o Uber caro.
- pequeno: Abaixo de
- GIGANTE: **1.073 km**
- serifa: *por mês, caro é o seu carro.*
- foto: o Kicks impresso no papel, com uma etiqueta pendurada no retrovisor: **PARADO · R$ 1.887/mês**
- pé: hodômetro "KM/MÊS 1.073" · "FAZER A CONTA ▸"

✂ "Abaixo de 1.073 km por mês, caro é o seu carro."

**Capas alternativas pra teste A/B:**
- B (dor pura): "Seu carro te cobra **R$ 1.887** antes de você sair da garagem."
- C (contradição com o post anterior): "Rodando 1.000 km por mês, o Uber **ainda** sai mais barato que o seu carro."

### Slide 2 · HOLD
- título: **A conta tem duas partes.**
- balança desenhada (dois pratos):
  - CARRO: parte fixa + parte por km
  - APP: só parte por km
- corpo: O carro te cobra antes de andar. O app só cobra quando você anda.
- corpo em destaque: **Em algum km, os dois custam igual. Esse é o seu número.**

✂ "O carro cobra antes de andar. O app só cobra quando você anda."

### Slide 3 · PARTE FIXA
- título: **R$ 1.887 antes de girar a chave.**
- cupom:
```
IPVA + licenciamento ......... R$ 280
Seguro ....................... R$ 300
Depreciação .................. R$ 667
Dinheiro parado no carro ..... R$ 640
-------------------------------------
PARTE FIXA / MÊS            R$ 1.887
```
- Kicks no papel, carimbo laranja: **PARADO**
- nota mono: Os quatro números do post do extrato. Chegam rodando ou não.

✂ "R$ 1.887 por mês pro carro ficar parado."

### Slide 4 · O KM DO CARRO
- título: **Cada km de carro: R$ 0,74.**
- taxímetro grande (contador mecânico): R$ 0,74
- cupom curto: Combustível R$ 0,54 (12 km/l a R$ 6,50) · Manutenção R$ 0,20 (pneu, revisão, freio)
- corpo: Parece barato. É aí que mora a pegadinha: os R$ 1.887 já foram antes.

✂ "Parece barato. Os R$ 1.887 já foram antes."

### Slide 5 · O KM DO APP
- título: **Cada km de app: R$ 2,50.**
- duelo de taxímetros lado a lado, mesmo hodômetro no meio:
  - CARRO: começa em R$ 1.887 · sobe R$ 0,74 por km
  - APP: começa em R$ 0 · sobe R$ 2,50 por km
- corpo: O app é 3 vezes mais caro por km. Mas começa do zero.
- nota mono: média de corrida urbana com tarifa base e tempo. Confira no app da sua cidade.

✂ "O app é 3x mais caro por km. Mas começa do zero."

### Slide 6 · VIRADA (o cruzamento)
- gráfico em marinho: eixo X km/mês (0 a 2.000), eixo Y R$/mês
  - reta do CARRO: começa em R$ 1.887, sobe devagar (creme)
  - reta do APP: começa em R$ 0, sobe rápido (laranja)
  - o cruzamento marcado com um círculo: **1.073 km · R$ 2.683**
  - à esquerda do cruzamento, sombreado: "aqui o app ganha"; à direita: "aqui o carro ganha"
- título: **1.073 km por mês.**
- serifa: *É aqui que o carro começa a compensar.*

✂ "1.073 km por mês. Abaixo disso, o app ganha."

### Slide 7 · CENÁRIOS (o slide de print)
| km/mês | carro | app | quem ganha |
|---|---|---|---|
| 300 (home office) | R$ 2.110 | R$ 750 | **app, por R$ 1.360** |
| 600 | R$ 2.332 | R$ 1.500 | **app, por R$ 832** |
| 1.000 | R$ 2.629 | R$ 2.500 | **app, por R$ 129** |
| 1.500 | R$ 3.000 | R$ 3.750 | **carro, por R$ 750** |
| 2.000 | R$ 3.370 | R$ 5.000 | **carro, por R$ 1.630** |
- título: **Ache a sua linha.**
- selos: APP em laranja, CARRO em creme
- nota: Rodando 1.000 km, o número do post do extrato, o app ainda ganha.

✂ "Rodando 1.000 km por mês, o app ainda sai R$ 129 mais barato."

### Slide 8 · TRADUZINDO 1.073 KM
- mapa desenhado (linhas de rua simples, sem marca de mapa): CASA ● ——— 24 km ——— ● TRABALHO
- título: **1.073 km = 36 km por dia.**
- corpo: É ir e voltar de um trabalho a 24 km de casa, todo dia útil. E não usar o carro pra mais nada.
- corpo em destaque: **Se o seu trajeto é menor, a conta já deu.**

✂ "1.073 km por mês é trabalhar a 24 km de casa e não usar o carro pra mais nada."

### Slide 9 · O QUE A CONTA NÃO PEGA
- título: **Antes de vender o carro.**
- duas colunas:
  - **Pesa pro carro:** filho e cadeirinha · viagem de estrada · cidade com pouco app · dinâmica de 1,5x (o ponto cai pra 627 km)
  - **Pesa pro app:** estacionamento e Zona Azul · multa · dirigir cansado ou depois de beber · tempo livre no trajeto
- faixa no pé: **Só o rendimento dos R$ 80 mil paga 256 km de app por mês.**

✂ "Só o rendimento dos R$ 80 mil paga 256 km de app por mês."

### Slide 10 · PAYOFF + CTA
- metade de cima em laranja, texto em tinta:
  - **Abaixo do seu ponto de virada:** o carro é conforto. Pode valer, mas tem preço.
  - **Acima:** o carro é economia.
- metade de baixo em marinho:
  - serifa: *Não existe resposta certa. Existe o seu número.*
  - faixa CTA: Comenta **KM** e eu te mando o site pra você calcular o seu ponto de virada.

✂ "Não existe resposta certa. Existe o seu número."

---

## 5. Legenda

```
Todo mundo acha o Uber caro. Pra quem roda pouco, caro é o carro.

A conta tem duas partes.

O carro te cobra antes de andar. IPVA, seguro, depreciação e o dinheiro parado nele somam R$ 1.887 por mês, rodando ou não. Depois, cada km custa mais R$ 0,74 de combustível e manutenção.

O app não tem parte fixa. Só cobra quando você anda: uns R$ 2,50 por km numa corrida urbana.

Por km, o app é 3 vezes mais caro. Mas começa do zero. As duas contas se cruzam em 1.073 km por mês.

Abaixo disso, o app sai mais barato. Acima, o carro compensa.

Pra ter ideia:
300 km/mês: o app economiza R$ 1.360
1.000 km/mês: o app ainda economiza R$ 129
1.500 km/mês: o carro economiza R$ 750

1.073 km é ir e voltar de um trabalho a 24 km de casa, todo dia útil, e não usar o carro pra mais nada.

Não é pra vender o carro amanhã. Filho, estrada e cidade sem app pesam do lado do carro. Estacionamento, multa e tempo livre pesam do lado do app. É pra decidir sabendo o seu número.

Comenta KM que eu te mando o site pra você calcular o seu ponto de virada com o seu carro e o preço do app na sua cidade.

E manda pra quem diz que Uber é caro.

Premissas: carro de R$ 80 mil (o mesmo do post do extrato), 12 km/l, gasolina R$ 6,50, SP, app a R$ 2,50/km em média. Com preço dinâmico de 1,5x, o ponto cai pra 627 km. Simulação educativa.

#financaspessoais #educacaofinanceira #uber #carro #mobilidade
```

**Primeiro comentário fixado:** "Quantos km você roda por mês? Comenta aqui que eu te digo de que lado você está 👇"

---

## 6. Dependências antes de publicar
- [ ] Simular 3 corridas comuns no app da sua cidade e conferir o R$ 2,50/km (trocar no `contas.py` se precisar).
- [ ] O site do CTA KM: estender a `carro-quitado/calculadora.html` com o campo "preço do app por km" e o gráfico do ponto de virada.
- [ ] Automação de DM pra palavra KM.
- [ ] Foto do Kicks: a mesma do post anterior (ver `IMAGENS.md`).
