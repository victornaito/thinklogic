"""Contas do carrossel "Uber/99 x carro próprio: a partir de quantos km por mês compensa ter carro".

Mesmo carro e mesmas premissas do post do extrato (carrosseis/carro-quitado/contas.py),
separadas em parte fixa (chega mesmo com o carro parado) e parte por km.
Troque as premissas pelos números do mês e rode: python3 contas.py
"""

# Carro (igual ao post do extrato)
VALOR_FIPE = 80_000
IPVA_ALIQUOTA = 0.04
LICENCIAMENTO_ANO = 160
SEGURO_ANO = 3_600
DEPRECIACAO_ANO = 0.10
JURO_MES = 0.008               # 0,8% a.m. líquido
KM_POR_LITRO = 12
GASOLINA = 6.50
MANUTENCAO_ANO = 2_400         # tratada como custo por km: 2.400 / 12.000 km por ano
KM_ANO_REFERENCIA = 12_000

# App (Uber/99): preço médio por km de corrida urbana, já com tarifa base e tempo.
# Recibos de 2026 achados: R$ 15,80 por 8,8 km (R$ 1,80/km) e R$ 17,80 por 5,8 km (R$ 3,07/km).
APP_POR_KM = 2.50
DINAMICA = 1.5                 # cenário com preço dinâmico


def brl(v):
    return f"R$ {v:,.0f}".replace(",", ".")


def main():
    fixos = {
        "IPVA + licenciamento": VALOR_FIPE * IPVA_ALIQUOTA / 12 + LICENCIAMENTO_ANO / 12,
        "Seguro": SEGURO_ANO / 12,
        "Depreciação": VALOR_FIPE * DEPRECIACAO_ANO / 12,
        "Dinheiro parado (custo de oportunidade)": VALOR_FIPE * JURO_MES,
    }
    fixos = {k: round(v) for k, v in fixos.items()}
    fixo = sum(fixos.values())
    comb_km = GASOLINA / KM_POR_LITRO
    manut_km = MANUTENCAO_ANO / KM_ANO_REFERENCIA
    por_km = comb_km + manut_km

    print("PARTE FIXA (por mês, rodando ou não)")
    for k, v in fixos.items():
        print(f"  {k:<40} {brl(v):>9}")
    print(f"  {'TOTAL FIXO':<40} {brl(fixo):>9}")
    print(f"PARTE POR KM: combustível R$ {comb_km:.3f} + manutenção R$ {manut_km:.3f} = R$ {por_km:.2f}/km")
    print(f"APP: R$ {APP_POR_KM:.2f}/km\n")

    virada = fixo / (APP_POR_KM - por_km)
    print(f"PONTO DE VIRADA: {virada:,.0f} km/mês".replace(",", "."))
    print(f"  = {virada / 30:.0f} km por dia, todo dia")
    print(f"  = trabalho a {virada / 44:.0f} km de casa, ida e volta em 22 dias úteis, e mais nada")
    v_din = fixo / (APP_POR_KM * DINAMICA - por_km)
    print(f"  com dinâmica {DINAMICA}x (R$ {APP_POR_KM * DINAMICA:.2f}/km): {v_din:,.0f} km/mês".replace(",", "."))
    for p in (2.00, 3.00):
        print(f"  com app a R$ {p:.2f}/km: {fixo / (p - por_km):,.0f} km/mês".replace(",", "."))

    print("\nCENÁRIOS")
    print(f"  {'km/mês':>7}  {'carro':>9}  {'app':>9}  quem ganha")
    for km in (300, 600, 1000, round(virada), 1500, 2000):
        carro = fixo + por_km * km
        app = APP_POR_KM * km
        dif = carro - app
        quem = "empate" if abs(dif) < 15 else (f"app, por {brl(dif)}" if dif > 0 else f"carro, por {brl(-dif)}")
        kms = f"{km:,}".replace(",", ".")
        print(f"  {kms:>7}  {brl(carro):>9}  {brl(app):>9}  {quem}")

    rend = VALOR_FIPE * JURO_MES
    print(f"\nSó o rendimento dos {brl(VALOR_FIPE)} ({brl(rend)}/mês) paga {rend / APP_POR_KM:.0f} km de app por mês.")


if __name__ == "__main__":
    main()
