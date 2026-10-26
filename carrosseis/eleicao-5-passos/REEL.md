# REEL · "O seu boleto não perdeu"

Vídeo vertical 1080×1920, 48 s, 30 fps, com trilha sintetizada a 120 BPM (−14 LUFS) e efeitos sincronizados ao texto.
Fonte: `src/reel.html` (cada cena e cada linha com o seu tempo em `data-a`, `data-b` e `data-t`). Render: `node src/reel.mjs video 4`, depois `python3 src/musica.py` e o mux.

**Objetivo:** furar a bolha. Reel é o formato que o Instagram mais mostra pra quem não segue a conta. O vídeo acolhe a frustração de quem perdeu, mas a cena 3 fala direto com quem ganhou, pra o vídeo não morrer dentro de um lado só.

## Linha do tempo

| Tempo | Cena | Texto | Por quê |
|---|---|---|---|
| 0 a 4 s | Hook (fotos de Lula e Flávio) | **O Bolsonaro perdeu.** / *O seu boleto, não.* / 5 passos pra não depender de eleição | A frase já está na tela no quadro 0: para o scroll sem depender de som. |
| 4 a 10 s | A dor | Eu sei. / Dá medo do que vem aí. / boleto com carimbo VENCE DIA 5 / **Quem paga as suas contas não é Brasília.** | Valida o sentimento antes de ensinar. Quem se sente entendido continua assistindo. |
| 10 a 14 s | Furar a bolha | Ganhou ou perdeu, / *o boleto chega igual.* / Isso vale pra quem votou no Lula também. | Abre o vídeo pros dois lados: quem ganhou também compartilha. |
| 14 a 20 s | A dúvida | Daqui a 4 anos, / **2026 → 2030** (contador) / a sua vida financeira vai estar melhor? / *Ou você vai esperar a próxima eleição?* | A dor deixa de ser o resultado e passa a ser o futuro da pessoa. |
| 20 a 38 s | As 5 dicas | 01 Anote cada gasto · 02 Escolha um método (80/10/10 ou 50/30/20) · 03 Receita − despesa · 04 Reserva de emergência · 05 Invista na sua aposentadoria | 3 a 4,5 s por dica: dá tempo de ler cada uma. |
| 38 a 42 s | Virada | Presidente muda a cada 4 anos. / *O seu boleto chega todo mês.* | A frase que as pessoas repetem. |
| 42 a 48 s | CTA | Não sabe por onde começar? / **Diagnóstico financeiro comigo.** / carimbo GRATUITO / **Link na bio** e começa o seu plano. | Fica 6 s parado no fim pra pessoa agir. |

Todo texto fica entre y 260 e y 1500, fora das áreas cobertas pela interface do Reels (topo, legenda embaixo e ícones à direita).

## Legenda sugerida pro Reel

```
O seu boleto não sabe quem ganhou a eleição.

Se você está com medo do que vem aí, eu entendo. Mas a sua vida financeira não precisa depender de quem ganha a cada 4 anos.

5 passos pra começar hoje:
1. Anote cada gasto por 30 dias
2. Escolha um método: 80/10/10 ou 50/30/20
3. Receita menos despesa: tem que sobrar
4. Reserva de emergência de 6 meses
5. Invista na sua própria aposentadoria

Não sabe por onde começar? Faça o diagnóstico financeiro gratuito comigo. Link na bio.

#financaspessoais #educacaofinanceira #eleicoes2026 #reservadeemergencia #liberdadefinanceira
```

## Pendências
- [ ] Crédito do fotógrafo na cena 1 (hoje: "[fotógrafo]/Agência Brasil").
- [ ] Ao subir: escolher o quadro 0 como capa do Reel e não colocar música do Instagram por cima (o vídeo já tem trilha).
