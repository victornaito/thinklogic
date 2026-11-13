# Guia de estilo · medido na referência (@gemeos.investem, 9 slides)

Números de `docs/pericia-gemeos.md` (o OCR da ferramenta não roda no Linux, então escala de texto e grade foram lidas no olho, nos quadros a 1080 px). Pega-se a gramática, nunca o conteúdo, as fotos, o rosto ou o cabeçalho.

| # | Dimensão | O que a referência faz | Como ficou no nosso |
|---|---|---|---|
| 1 | Ideia | Notícia em 9 passos: data → o que entra → tabela → casos → alívio → virada (2028) → incerteza → CTA. O dispositivo que repete é "título de duas linhas, a segunda em coral" | Mesmo dispositivo; ordem refeita (ver BRIEF §1b) |
| 2 | Formato | 4:5 (1080×1339), 9 slides, estático | 1080×1350, 9 slides |
| 3 | Paleta | Fundo carvão quente `#15110F` a `#3A2F2B`; tinta branca; destaque coral (`#CB503E`/`#D93C2D` em forma, mais claro em texto); amarelo `#E8D679`→ puro só no CTA | `--fundo #1A1817`, `--coral #FF5A47` (texto), `--coral-forma #DC3F2E`, `--amarelo #FFD60A` |
| 4 | Tipografia | Grotesca geométrica pesada, tracking fechado, nos títulos (≈ 76 a 84 px); a mesma em peso médio no corpo (≈ 38 a 42 px); condensada em caixa alta na capa e nos números gigantes | Montserrat 800 / 500 e Anton (ambas OFL, em `src/fontes/`) |
| 5 | Grade | Margem ≈ 72 a 80 px; título no topo à esquerda; dispositivo no meio; duas ou três frases embaixo; CTA centralizado | `--margem 72px`; mesma ordem vertical |
| 6 | Preenchimento | Vazio médio 44% (28% a 53%) | Parecido: dispositivo ocupa o terço do meio |
| 7 | Hierarquia | 3 níveis (título, corpo, nota) + um número gigante em alguns slides | Igual |
| 8 | Imagens | Fotos e 3D gerados por IA (produtos de marca, presidente, "2028" em 3D, ampulheta), luminância 0,33, quente | **Código (SVG)**, objetos genéricos sem marca e sem pessoa; "2028" em extrusão de CSS |
| 9 | Formas | Cartão de vidro com borda clara e raio ≈ 28 px; pílula coral com raio ≈ 20 px; aba coral inclinada no cabeçalho da tabela; seta coral; botão-pílula amarelo | `.vidro`, `.pilula`, `.tabela .cab b`, `.botao` |
| 10 | Textura | Fundo de foto desfocada (bokeh quente) + mesa escura | Luzes desfocadas geradas com semente fixa + degradê de mesa + grão leve |
| 11 | Ritmo | Todos escuros; o CTA muda a cor de destaque pra amarelo | Igual; o slide 7 (virada) fica mais escuro e sem luzes |
| 12 | Interface | Cabeçalho com avatar e nome no topo | Trocado por rodapé discreto com o @ e "03/09 · arrasta →"; cantos do contador e do som livres |

## Mecanismos verificáveis
1. Todo título tem duas linhas e a segunda (ou a palavra-chave) está em coral.
2. Uma cor de destaque por slide: coral nos slides 1 a 8, amarelo só no 9.
3. Todo número de alíquota mora numa pílula coral ou num cartão de vidro.
4. Uma marca à mão por slide, no máximo (traço, elipse ou marca-texto).
5. Margem de 72 px e texto alinhado à esquerda em todos os slides, menos o CTA (centralizado).
6. O slide do CTA termina num botão-pílula amarelo com a palavra-chave em caixa alta e uma seta apontando pra ele.
