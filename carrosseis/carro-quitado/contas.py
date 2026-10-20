"""Contas do carrossel "Seu carro quitado ainda custa R$ X por mês".

Rode antes de publicar: troque as premissas pelos números do mês (FIPE,
preço da gasolina na ANP, CDI) e o roteiro inteiro se atualiza a partir daqui.
"""

# Premissas (out/2026, todas conferíveis)
VALOR_FIPE = 80_000        # compacto seminovo (conferir FIPE do modelo escolhido)
IPVA_ALIQUOTA = 0.04       # SP, carro a gasolina/flex
LICENCIAMENTO_ANO = 160    # taxa anual do Detran-SP (aprox.)
SEGURO_ANO = 3_600         # ~4,5% do valor, perfil médio
MANUTENCAO_ANO = 2_400     # revisões, pneus, freios, imprevistos
KM_MES = 1_000
KM_POR_LITRO = 12
GASOLINA = 6.50            # média ANP (ago/2026: R$ 6,53)
DEPRECIACAO_ANO = 0.10     # média de seminovo na FIPE
JURO_MES = 0.008           # 0,8% a.m. líquido: abaixo do CDI líquido de hoje (Selic 14%)
MESES = 120                # 10 anos
CORRIDA_APP = 30


def brl(v):
    return f"R$ {v:,.0f}".replace(",", ".")


def main():
    linhas = {
        "IPVA + licenciamento": VALOR_FIPE * IPVA_ALIQUOTA / 12 + LICENCIAMENTO_ANO / 12,
        "Seguro": SEGURO_ANO / 12,
        "Manutenção": MANUTENCAO_ANO / 12,
        "Combustível": KM_MES / KM_POR_LITRO * GASOLINA,
        "Depreciação": VALOR_FIPE * DEPRECIACAO_ANO / 12,
        "Custo de oportunidade": VALOR_FIPE * JURO_MES,
    }
    r = {k: round(v) for k, v in linhas.items()}
    visivel = sum(list(r.values())[:4])
    invisivel = sum(list(r.values())[4:])
    total = visivel + invisivel

    for k, v in r.items():
        print(f"{k:<24} {brl(v):>9}")
    print(f"{'Você vê (sai da conta)':<24} {brl(visivel):>9}")
    print(f"{'Você não vê':<24} {brl(invisivel):>9}")
    print(f"{'TOTAL':<24} {brl(total):>9}")
    print(f"Litros/mês: {KM_MES / KM_POR_LITRO:.0f}")
    print(f"Corridas de app: {total / CORRIDA_APP:.0f} por mês, {total / CORRIDA_APP / 30:.1f} por dia")

    # 10 anos. Depreciação e custo de oportunidade já estão dentro do
    # "R$ 80 mil investidos rendendo"; somá-los como aporte mensal contaria duas vezes.
    f = (1 + JURO_MES) ** MESES
    sem_carro = VALOR_FIPE * f + visivel * (f - 1) / JURO_MES
    carro_depois = VALOR_FIPE * (1 - DEPRECIACAO_ANO) ** (MESES // 12)
    print(f"Sem o carro, investindo: {brl(sem_carro)}")
    print(f"  dos R$ 80 mil: {brl(VALOR_FIPE * f)} | dos aportes: {brl(visivel * (f - 1) / JURO_MES)}")
    print(f"Com o carro, depois de 10 anos: {brl(carro_depois)}")
    print(f"Diferença: {brl(sem_carro - carro_depois)}")
    print(f"(Conta ingênua, {brl(total)}/mês como aporte: {brl(total * (f - 1) / JURO_MES)}; conta duas vezes)")


if __name__ == "__main__":
    main()
