#!/usr/bin/env python3
"""Folha de contato (resultados/folha.png) e teste de miniatura (resultados/miniatura.png)."""
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parent.parent / 'resultados'
fs = sorted((R / 'estatico').glob('slide-*.png'))
ims = [Image.open(f).convert('RGB') for f in fs]
w, h, g = 432, 540, 12
cols = 5; rows = -(-len(ims) // cols)
F = Image.new('RGB', (cols * w + (cols + 1) * g, rows * h + (rows + 1) * g), '#0b0b0b')
for i, im in enumerate(ims):
    F.paste(im.resize((w, h), Image.LANCZOS), (g + (i % cols) * (w + g), g + (i // cols) * (h + g)))
F.save(R / 'folha.png')
# miniatura: capa 1:1 a 128 px numa grade de perfil + cada slide a 390 px (feed)
M = Image.new('RGB', (3 * 128 + 4 * 6 + 20 + len(ims) * 0 + 0, 3 * 128 + 4 * 6), '#111')
capa = ims[0].crop((0, 135, 1080, 1215)).resize((128, 128), Image.LANCZOS)
for k in range(9):
    x, y = 6 + (k % 3) * 134, 6 + (k // 3) * 134
    M.paste(capa if k == 4 else Image.new('RGB', (128, 128), '#2a2a2a'), (x, y))
M.save(R / 'miniatura.png')
print('folha.png', F.size, 'miniatura.png', M.size)
