# BRIEF · "Financiar é pagar R$ 41 mil pra não esperar 28 meses"

Carrossel de 10 slides, estático + vivo (um MP4 por slide, 120 BPM), para **@victornaito.financas**.
Terceiro post da série do carro: o mesmo Kicks de R$ 80 mil. Contas: `python3 contas.py`.

---

## 1. Estratégia

| Item | Decisão |
|---|---|
| Resultado desejado | **Share + save** (quem vai comprar carro guarda; quem tem amigo comprando manda) |
| Arquétipo | Teardown com placar: três caminhos, o mesmo bolso, um vencedor por critério |
| Sentimento | **Pressa → paciência.** A pessoa descobre quanto custa a pressa. |
| Frase única | A diferença entre os três não é o carro. É quem recebe os juros: o banco, a administradora ou você. |
| Público | Quem está pra comprar carro nos próximos 12 meses e acha que "financiar é o normal" |

**A regra que deixa a comparação justa (e à prova de comentário):** o mesmo bolso nos três caminhos.
A pessoa tem **R$ 16 mil guardados** e **R$ 2.044 livres por mês** (o valor exato da parcela do financiamento). Cada caminho usa esse mesmo dinheiro.

**O hook: dor + contradição.**
- **Contradição:** financiamento parece o caminho "normal", e juntar parece coisa de quem não pode. A conta mostra que esperar 28 meses vale R$ 41 mil.
- **Dor:** R$ 34 mil de juros é quase meio carro. A pessoa paga um carro e meio pra ter um.
- **O consórcio no meio:** é a surpresa do post. Não tem juros, mas tem taxa, reajuste e sorteio. Você paga como quem financia e espera como quem junta, sem saber quanto tempo.

**Por que vai ser compartilhado:**
1. **O placar do slide 7** (os três caminhos numa linha do tempo de 60 meses) é o slide de print.
2. **A frase do consórcio** ("paga como quem financia, espera como quem junta") gera debate, porque muita gente tem consórcio.
3. **A honestidade do slide 9** (quando financiar ou fazer consórcio faz sentido) desarma quem já financiou e evita o tom de julgamento.

---

## 2. Premissas (todas no `contas.py`)

| Item | Valor | Fonte / nota |
|---|---|---|
| Carro | R$ 80 mil, sobe ~4% ao ano | o Kicks da série |
| Bolso | R$ 16 mil guardados + R$ 2.044/mês | igual nos três caminhos |
| Financiamento | 20% de entrada + 48x a 1,9% a.m. | média do BC pra veículos PF: 26,4% a.a. (ago/2026) |
| Consórcio | 60 meses, 18% de administração + 2% de fundo de reserva, parcela reajustada 4% ao ano | taxas variam de 12% a 25% por administradora; prazo médio Abac ~80 meses |
| Juntar | investir a 0,8% a.m. líquido, comprar à vista com 5% de desconto | mesma taxa dos outros posts |

**Resultado**

| | Carro chega | Paga até | Total pago | Observação |
|---|---|---|---|---|
| **Financiamento** | hoje | mês 48 | **R$ 114.126** | R$ 34.126 de juros |
| **Consórcio** | sorteio: mês 1 a 60 | mês 60 | **R$ 103.993** | sem juros, mas 20% de taxas + reajuste; os R$ 16 mil podem virar lance |
| **Juntar** | mês 28 | mês 28 | **R$ 73.240** do bolso | os juros (R$ 10.632) trabalharam a seu favor |

- **Preço da pressa:** R$ 114.126 − R$ 73.240 = **R$ 40.886** pra ter o carro 28 meses antes.
- **Meses livres:** do mês 29 ao 48, quem juntou investe os R$ 2.044 que o financiado ainda paga → **R$ 44.147** no mês 48.

**Conferir antes de publicar:** a taxa média do BC na semana (painel de taxas do Bacen, aquisição de veículos PF) e a taxa de administração de uma administradora real.

---

## 3. Estrutura e animação

| # | Posição | Fundo | Dispositivo | Animação (vivo) |
|---|---|---|---|---|
| 1 | Capa | papel + Kicks real | número gigante "R$ 41 mil" + ampulheta "28 meses" | os rolos do R$ 41 mil giram; a ampulheta vira e a areia escorre |
| 2 | Hold | marinho | três portas: FINANCIAR · CONSÓRCIO · JUNTAR | as três portas abrem uma por batida |
| 3 | Financiamento | papel | cupom de 48 parcelas | as parcelas imprimem em rajada; o total carimba R$ 114 mil |
| 4 | Juros do financiamento | marinho | carro e meio: Kicks inteiro + meio Kicks | a metade do carro desliza pra dentro com carimbo "JUROS" |
| 5 | Consórcio | papel | roleta de sorteio com os meses 1 a 60 | a roleta gira e para num mês diferente a cada loop |
| 6 | Juntar | marinho | cofre enchendo até o preço do carro | barra sobe mês a mês; em 28 ela cruza a linha do preço e carimba "À VISTA" |
| 7 | **Virada / placar** | papel | três linhas do tempo de 0 a 60 meses | as três barras crescem juntas, mês a mês; o ícone do carro aparece em cada uma no mês em que chega |
| 8 | Meses livres | marinho | do mês 29 ao 48: R$ 44 mil | contador sobe de 0 a 44.147 |
| 9 | Quando faz sentido | linho | duas colunas: financiar / consórcio | itens estalam um a um |
| 10 | Fecho | laranja + marinho | pergunta reflexiva + diagnóstico | a ampulheta da capa volta e para |

---

## 4. Copy, slide a slide

### Slide 1 · CAPA
- pequeno: Financiar é pagar
- GIGANTE: **R$ 41 mil**
- serifa: *pra não esperar 28 meses.*
- foto: o Kicks no papel, com uma etiqueta "PRA JÁ" pendurada no retrovisor
✂ "Financiar é pagar R$ 41 mil pra não esperar 28 meses."

**Capas alternativas pra teste A/B:**
- B (dor): "Você paga **um carro e meio** pra ter um."
- C (contradição do consórcio): "Consórcio não tem juros. **E mesmo assim sai R$ 30 mil mais caro.**" (R$ 103.993 contra R$ 73.240)

### Slide 2 · HOLD
- título: **Mesmo carro. Mesmo bolso.**
- corpo: R$ 16 mil guardados e R$ 2.044 livres por mês.
- três portas: **FINANCIAR · CONSÓRCIO · JUNTAR**
- destaque: Só muda quem recebe os juros.
✂ "Mesmo carro, mesmo bolso. Só muda quem recebe os juros."

### Slide 3 · FINANCIAMENTO
- título: **Financiar: o carro sai hoje.**
- cupom: Entrada R$ 16.000 · 48x R$ 2.044 · taxa 1,9% ao mês (média do BC) · **TOTAL R$ 114.126**
- nota: É a taxa média. Muita gente paga mais.
✂ "O carro de R$ 80 mil sai por R$ 114 mil."

### Slide 4 · O MEIO CARRO
- título: **R$ 34 mil de juros.**
- visual: um Kicks inteiro + meio Kicks, com carimbo JUROS
- serifa: *Você paga um carro e meio pra ter um.*
✂ "Você paga um carro e meio pra ter um."

### Slide 5 · CONSÓRCIO
- título: **Consórcio: sem juros.**
- corpo: Mas com 20% de taxas, parcela que sobe todo ano e um sorteio que decide quando o carro chega.
- roleta: mês 1 … mês 60
- cupom: 60x a partir de R$ 1.600 · **TOTAL R$ 103.993**
- destaque: **Você paga como quem financia e espera como quem junta. Sem saber quanto.**
✂ "Consórcio: paga como quem financia, espera como quem junta."

### Slide 6 · JUNTAR
- título: **Juntar: 28 meses.**
- corpo: R$ 16 mil + R$ 2.044 por mês, investidos a 0,8% ao mês.
- barra subindo até cruzar a linha do preço do carro (que também subiu)
- cupom: Do seu bolso R$ 73.240 · Juros a seu favor R$ 10.632 · Desconto à vista 5%
✂ "Juntando, os juros trabalham pra você: R$ 10.632."

### Slide 7 · O PLACAR (virada)
- título: **O mesmo carro, três preços.**
- três linhas do tempo (0 a 60 meses):
  - FINANCIAR: carro no mês 0 · paga até 48 · **R$ 114 mil**
  - CONSÓRCIO: carro no mês ? · paga até 60 · **R$ 104 mil**
  - JUNTAR: carro no mês 28 · paga até 28 · **R$ 73 mil**
- serifa: *A diferença é quem recebe os juros.*
✂ "R$ 114 mil, R$ 104 mil ou R$ 73 mil. O mesmo carro."

### Slide 8 · OS MESES LIVRES
- título: **Do mês 29 ao 48:**
- corpo: quem financiou ainda paga R$ 2.044. Quem juntou, investe.
- contador: **R$ 44.147**
- serifa: *Quem esperou já começou o próximo carro.*
✂ "Quem esperou 28 meses chega no mês 48 com R$ 44 mil."

### Slide 9 · QUANDO FAZ SENTIDO
- título: **Nem sempre juntar ganha.**
- **Financiar faz sentido quando:** o carro paga a parcela (trabalho, aplicativo) · a montadora oferece taxa zero de verdade · é emergência e não há transporte
- **Consórcio faz sentido quando:** você não consegue guardar sozinho · tem dinheiro pra dar lance · não tem pressa nenhuma
- faixa: A regra: só pague juros por um carro que te dá dinheiro.
✂ "Só pague juros por um carro que te dá dinheiro."

### Slide 10 · FECHO
- metade laranja: **Quanto vale, pra você, ter o carro 28 meses antes?**
- metade marinho, serifa: *Se a resposta for menos de R$ 41 mil, você já sabe o caminho.*
- faixa: Diagnóstico financeiro gratuito comigo · link na bio
✂ "Quanto vale ter o carro 28 meses antes?"

---

## 5. Legenda

```
Financiar é pagar R$ 41 mil pra não esperar 28 meses.

Fiz a conta com o mesmo carro de R$ 80 mil e o mesmo bolso: R$ 16 mil guardados e R$ 2.044 livres por mês.

Financiando (1,9% ao mês, a média do Banco Central): o carro sai hoje e custa R$ 114 mil. São R$ 34 mil de juros, um carro e meio pra ter um.

Consórcio: não tem juros, mas tem 20% de taxas, parcela que sobe todo ano e sorteio. Sai por R$ 104 mil, e o carro chega quando a sorte quiser.

Juntando e investindo a mesma parcela: em 28 meses você compra à vista, com desconto, tirando R$ 73 mil do bolso. Os juros trabalham pra você.

E do mês 29 ao 48, enquanto quem financiou ainda paga, quem juntou investe. Chega no mês 48 com R$ 44 mil.

Nem sempre juntar ganha. Se o carro te dá dinheiro (trabalho, aplicativo) ou se a montadora oferece taxa zero de verdade, financiar pode fazer sentido. A regra: só pague juros por um carro que te dá dinheiro.

Quanto vale, pra você, ter o carro 28 meses antes?

Se quiser montar o seu plano pra comprar sem pagar juros, faça o diagnóstico financeiro gratuito comigo. Link na bio.

Salva pra quando for comprar e manda pra quem está pensando em financiar.

Premissas: carro de R$ 80 mil subindo 4% ao ano, financiamento 20% de entrada + 48x a 1,9% a.m., consórcio de 60 meses com 18% de administração e 2% de fundo de reserva, investimento a 0,8% a.m. líquido, 5% de desconto à vista. Simulação educativa.

#financaspessoais #educacaofinanceira #consorcio #financiamento #carro
```

---

## 6. Pontos pra confirmar
- [ ] Taxa média do BC na semana de publicação (o post usa 1,9% a.m. / 26,4% a.a., dado de ago/2026).
- [ ] Taxa de administração de uma administradora real (o post usa 18% + 2% de fundo de reserva, dentro da faixa de 12% a 25% que aparece nas fontes).
- [ ] O CTA: diagnóstico gratuito (como no post da eleição) ou só a pergunta reflexiva (como no post do Uber).
