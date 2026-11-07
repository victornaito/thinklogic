"""Contas do carrossel "Consórcio x financiamento x juntar e comprar à vista".

Mesmo carro da série (R$ 80 mil) e o MESMO BOLSO nos três caminhos:
R$ 16 mil guardados + a parcela do financiamento livre todo mês.
Troque as premissas e rode: python3 contas.py
"""
VALOR = 80_000
ENTRADA = 16_000                 # 20%: usada como entrada, lance ou ponto de partida
JURO_FIN = 0.019                 # 1,9% a.m. ≈ 26,4% a.a., média do BC pra veículos PF (ago/2026)
PRAZO_FIN = 48
ADM, FUNDO = 0.18, 0.02          # consórcio: taxa de administração e fundo de reserva sobre a carta
PRAZO_CONS = 60
REAJUSTE = 0.04                  # carro (e carta do consórcio) sobem ~4% ao ano
RENDE = 0.008                    # 0,8% a.m. líquido, igual aos outros posts da série
DESCONTO_AVISTA = 0.05


def brl(v):
    return f"R$ {v:,.0f}".replace(",", ".")


def main():
    # 1. financiamento: carro hoje
    pv = VALOR - ENTRADA
    pmt = pv * JURO_FIN / (1 - (1 + JURO_FIN) ** -PRAZO_FIN)
    fin_total = ENTRADA + pmt * PRAZO_FIN
    print(f"FINANCIAMENTO  entrada {brl(ENTRADA)} + {PRAZO_FIN}x {brl(pmt)}")
    print(f"  total {brl(fin_total)}  juros {brl(fin_total - VALOR)}  carro: mês 0  paga até o mês {PRAZO_FIN}")

    # 2. consórcio: sem juros, com taxas; parcela reajustada todo ano; carro quando for contemplado
    base = VALOR * (1 + ADM + FUNDO) / PRAZO_CONS
    cons_total = sum(base * (1 + REAJUSTE) ** (m // 12) for m in range(PRAZO_CONS))
    print(f"CONSÓRCIO      {PRAZO_CONS} meses, taxas {ADM + FUNDO:.0%}, parcela inicial {brl(base)} (sobe {REAJUSTE:.0%} ao ano)")
    print(f"  total {brl(cons_total)}  carro: sorteio entre o mês 1 e o mês {PRAZO_CONS}  sobra pra lance: {brl(ENTRADA)}")

    # 3. juntar: entrada + a mesma parcela investidas até comprar à vista com desconto
    s, m, g = ENTRADA, 0, (1 + REAJUSTE) ** (1 / 12) - 1
    while True:
        m += 1
        s = s * (1 + RENDE) + pmt
        preco = VALOR * (1 + g) ** m * (1 - DESCONTO_AVISTA)
        if s >= preco:
            break
    bolso = ENTRADA + pmt * m
    print(f"JUNTAR         {brl(ENTRADA)} + {brl(pmt)}/mês a {RENDE:.1%} a.m.")
    print(f"  compra no mês {m}: carro custa {brl(preco)} com {DESCONTO_AVISTA:.0%} de desconto; saiu do bolso {brl(bolso)}; juros a favor {brl(s - bolso)}")

    livres = PRAZO_FIN - m
    fv_livres = pmt * ((1 + RENDE) ** livres - 1) / RENDE
    print(f"\nMESES LIVRES: do mês {m + 1} ao {PRAZO_FIN}, quem juntou investe {brl(pmt)}/mês → {brl(fv_livres)} no mês {PRAZO_FIN}")
    print(f"PREÇO DA PRESSA: financiar custa {brl(fin_total - bolso)} a mais pra ter o carro {m} meses antes")


if __name__ == "__main__":
    main()
