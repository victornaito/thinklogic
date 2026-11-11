---
name: efeitos-video-dinamico
description: Edita vídeo vertical (talking head, Reels, TikTok, Shorts) inserindo efeitos visuais, transições e efeitos sonoros em Remotion nos momentos certos para segurar a retenção até o fim. Transcreve com tempo por palavra, mapeia gancho, re-ganchos, payoff e CTA, escolhe entre 17 efeitos (Órbita, Parede de posts, Dentro do app, Saindo da tela, Zoom digital, Mockup de celular, Checklist, Mural de manchete, Corte no zoom, Gráfico subindo, Revelação, Chroma key, Recorte de papel, Rabisco vivo, Vertigem, Capa de revista, Letra de vidro), valida o plano, recorta o fundo e renderiza sem alterar o áudio. Use quando pedirem "deixa o vídeo dinâmico", "coloca efeitos", "edita esse Reels", "segura a retenção" ou citarem um dos 17 efeitos. Não use para cortar vídeo longo (corte-viral) nem motion estilo Vox (motion-vox).
---

# Efeitos de vídeo dinâmico (Remotion)

Pega um vídeo vertical já cortado e devolve o mesmo vídeo com efeitos encaixados
onde a fala pede, para que a pessoa não saia antes do fim. O áudio original nunca é alterado.

Os 17 efeitos vêm do material "17 efeitos de vídeo que o Claude cria". A ficha completa
de cada um (o que é, quando usar, duração, prompt-base, notas de Remotion) está em
`referencias/catalogo-efeitos.md`. As regras de onde encaixar estão em
`referencias/retencao.md`. O esqueleto de código está em `referencias/remotion.md`.

Leia os três antes de planejar. Não improvise a lista de efeitos de memória.

## Entradas

| Item | Obrigatório | Observação |
|---|---|---|
| Vídeo vertical (`.mp4`/`.mov`) | sim | talking head, selfie, qualquer fala. Se for horizontal ou longo, passe antes pela skill `corte-viral`. |
| Prints dos posts (pasta `prints/`) | só para 01 Órbita, 02 Parede de posts, 03 Dentro do app | sem prints, troque por outro efeito, não invente imagens. |
| Objetivo do vídeo | não | seguir, salvar, comentar palavra, clicar no link. Se faltar, assuma "seguir" e diga que assumiu. |
| Identidade visual (cores, fontes, @) | não | se não houver, use as paletas de cada efeito no catálogo. |

## Processo

### 1. Preparar o projeto

```bash
bash scripts/preparar.sh caminho/do/video.mp4 projeto-video
```

Cria um projeto Remotion vertical 1080x1920 a 30 fps em `projeto-video/`, normaliza o vídeo
para CFR 30 fps (`public/video.mp4`) e imprime duração e total de quadros. Quadro N do vídeo
= quadro N da composição, e é isso que faz o recorte encaixar sem deslizar.

Equivale ao "primeiro prompt" do material: *"Cria um projeto Remotion vertical, 1080x1920,
30 fps, e coloca meu vídeo video.mp4 na pasta public."*

### 2. Transcrever com tempo por palavra

```bash
python3 scripts/transcrever.py projeto-video/public/video.mp4 projeto-video/analise
```

Gera `transcricao.json` (palavras com início/fim) e `transcricao.txt` (frases com tempo).
Tudo que vier depois se ancora nessas marcas. Efeito que entra fora da palavra parece erro.

### 3. Ler o vídeo antes de decidir

Leia o `transcricao.txt` inteiro e extraia alguns quadros (`ffmpeg -ss T -frames:v 1`) para
ver enquadramento, luz, roupa, fundo e onde fica o rosto. Anote:

- **A frase única** do vídeo (o que a pessoa leva se só lembrar de uma coisa).
- **Os blocos:** gancho, contexto, desenvolvimento (cada ideia), virada/payoff, CTA.
- **Os gatilhos:** números, listas, nomes de ferramenta/app, perguntas, afirmações fortes,
  mudanças de assunto, palavras de impacto. Cada gatilho é candidato a efeito.
- **Os vales:** trechos de explicação mais lenta onde a atenção cai (são onde mais precisa de efeito).

### 4. Montar o plano de efeitos

Escreva `projeto-video/analise/plano-efeitos.json` seguindo `modelos/plano-efeitos.exemplo.json`.
Cada entrada tem: efeito, início/fim em segundos, a frase-gatilho, o motivo de retenção,
os textos na tela e parâmetros.

Regras que não se negociam (detalhes e tabela de densidade em `referencias/retencao.md`):

1. **Gancho visual nos primeiros 1,5 s.** O primeiro quadro já tem que estar em movimento.
2. **Nenhum trecho de 4 s sem mudança visual** (efeito pesado, zoom seco, corte ou texto).
3. **Efeito pesado dura de 1,5 a 4 s** e volta para o rosto cru. O rosto é o que gera confiança.
4. **Um efeito pesado a cada 6 a 12 s**, com um re-gancho forte entre 40 e 60% da duração.
5. **Sem repetir efeito pesado** no mesmo vídeo de até 60 s. Zoom digital e Corte no zoom
   são "tempero" e podem repetir.
6. **Efeitos vizinhos mudam de registro** (fundo trocado → overlay → câmera → tipografia).
7. **Os últimos 15% têm payoff visual** e o CTA na tela. O último quadro deve emendar com
   o primeiro quando possível (loop).
8. **O efeito serve à frase.** Se você não consegue escrever o motivo em uma linha, tire o efeito.

Valide antes de escrever código:

```bash
python3 scripts/validar_plano.py projeto-video/analise/plano-efeitos.json --duracao <segundos>
```

Corrija todo ERRO. AVISO pode ficar se o motivo estiver escrito no plano.

Mostre o plano ao usuário como tabela (tempo · frase · efeito · por quê) antes de implementar,
a menos que ele tenha pedido para seguir direto.

### 5. Recortar o fundo (só se o plano tiver efeito ✂)

Os efeitos 01, 02, 04, 08, 10, 12, 13, 14, 15, 16 e 17 precisam de você recortado.
Recorte só as janelas usadas, não o vídeo inteiro:

```bash
python3 scripts/recortar.py projeto-video/public/video.mp4 projeto-video/public/recorte \
  --plano projeto-video/analise/plano-efeitos.json
```

Salva `recorte/00042.png` (RGBA) com o mesmo número do quadro do vídeo. Usa `rembg`
(grátis, funciona em Mac, Windows e Linux). No Mac, o Vision da Apple é alternativa
(`--motor vision` explica como). Confira 3 quadros do recorte antes de seguir: cabelo,
mãos e objetos na mão são onde ele falha.

### 6. Implementar

Siga `referencias/remotion.md`: uma composição `Principal` que toca o vídeo base e, para cada
item do plano, uma `<Sequence>` com o componente do efeito. Um arquivo por efeito em
`src/efeitos/`. Os textos vêm do plano, nunca fixos no componente.

Para o visual de cada efeito, use o prompt-base do catálogo como especificação e adapte cores
e textos ao vídeo do usuário.

### 7. Rascunho, revisão e master

```bash
cd projeto-video
npx remotion render Principal out/rascunho.mp4 --scale=0.5 --crf=28
```

Se o Remotion não conseguir baixar o Chrome (rede bloqueada, sessão na nuvem), aponte um
Chromium local com `--browser-executable=<caminho>` em todo `render`/`still` (em sessões
Claude Code na nuvem: `/opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell`).

Extraia um quadro do meio de cada efeito (`npx remotion still Principal out/q.png --frame=N`)
e monte uma folha de contato. Revise com a rubrica:

| Pergunta | Precisa ser "sim" |
|---|---|
| O quadro 0 já tem movimento ou texto forte? | sim |
| Cada efeito começa na palavra-gatilho (±3 quadros)? | sim |
| O recorte não tem halo, buraco ou dedo cortado? | sim |
| Algum texto fica embaixo do rosto, da boca ou fora da área segura (topo 220 px, base 380 px)? | não |
| Dá para ler cada texto na tela no tempo que ele fica? (≈ 0,3 s por palavra, mínimo 1 s) | sim |
| O áudio está idêntico ao original e em sincronia? | sim |
| Há algum trecho de mais de 4 s parado? | não |

Corrija, depois renderize o master:

```bash
npx remotion render Principal out/final.mp4 --codec=h264 --crf=18 --audio-codec=aac
```

### 8. Entregar

- `out/final.mp4`
- `analise/plano-efeitos.json` e a tabela do plano em `analise/RELATORIO.md`, com o motivo de
  cada efeito e o que ficou de fora.
- Diga o que foi assumido (objetivo, cores, CTA) e ofereça trocar qualquer efeito: o usuário
  só precisa dizer "troca o efeito das 0:12 por X".

## Quando faltar algo

- **Sem prints:** troque Órbita/Parede de posts por Mural de manchete ou Letra de vidro.
- **Recorte ruim** (fundo parecido com a roupa, muito movimento): use efeitos sem ✂
  (03, 05, 06, 07, 09, 11) naquele trecho.
- **Vídeo com menos de 15 s:** no máximo 2 efeitos pesados + zooms secos.
- **Fala sem gatilhos claros:** apoie-se em Zoom digital com palavra, Checklist do que foi dito
  e Corte no zoom nas mudanças de frase.

## Dica do material

Depois de cada efeito, renderize um rascunho e mostre. Se o usuário não gostar, ele fala o que
mudar do jeito dele e você ajusta só aquele efeito.
