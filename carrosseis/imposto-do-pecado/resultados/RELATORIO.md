# Relatório · estático v1

Arquivos: `estatico/slide-01.png` a `slide-09.png` (1080×1350), `folha.png` (folha de contato), `miniatura.png` (capa a 128 px na grade), `legenda.txt`.
Fonte: `src/gerar.py` escreve os nove `src/slide-NN.html`. Render: `python3 src/gerar.py && NODE_PATH=$(npm root -g) node src/render.mjs && python3 src/folha.py`.

## Notas (rodada 3)
| Critério | Nota | Observação |
|---|---|---|
| Gancho na capa | 8 | Data no carimbo + a contradição "o aumento de verdade, não". Lê a 128 px. |
| Slide 2 paga a capa | 8 | Dá o nome oficial e abre o mapa dos 8 itens. |
| Espinha | 8 | Quanto → carro → importado → calma → 2028 → 120 dias. |
| Ritmo | 8 | Grade, tabela, trio, par, troca, número gigante, ampulheta, amarelo. Todos escuros, como a referência. |
| Virada | 9 | "2028" gigante num slide mais escuro que os outros. |
| Payoff e CTA | 8 | A crença vira antes do pedido; palavra CHEGA amarrada na frase de cima. |
| Copy | 8 | Frases curtas, uma linha de print por slide, sem hype. |
| Leitura em miniatura | 8 | Títulos e números leem a 390 px; notas de fonte são detalhe. |
| Paleta e fontes | 8 | Duas fontes, coral + amarelo só no CTA. Coral em texto abaixo de 90 px vem da referência. |
| Margens e cantos | 9 | 72 px livres; nada nos cantos do contador e do som. |
| Anti-aislop | 7 | As ilustrações em SVG são limpas, mas mais simples que as fotos da referência. É o ponto mais fraco. |
| Fidelidade à referência | 8 | Os 6 mecanismos do guia presentes; a diferença é imagem vetorial no lugar de foto. |

## Corrigido entre as rodadas
1. Capa: a terceira linha estourava a largura (o ajuste media o bloco, não o texto).
2. Slide 3: a tabela saía 72 px pra direita e cortava as pílulas (o cartão de vidro sobrescrevia a posição).
3. Slide 5: "6,09%" com a elipse passava da borda do cartão.

## Créditos do Higgsfield
Zero. A conta está com 0 créditos, então nenhuma imagem foi gerada; tudo é código.

## O que melhoraria em seguida
1. Com créditos no Higgsfield, trocar os objetos da capa e a ampulheta por fotos de produto genérico (sem marca) na mesma luz quente.
2. Versão viva (MP4 por slide): o carimbo batendo na capa, a tabela entrando linha a linha, o "2028" subindo.
3. Capa B pra teste: "CIGARRO, CERVEJA E CARRO GANHAM IMPOSTO NOVO EM FEVEREIRO."
