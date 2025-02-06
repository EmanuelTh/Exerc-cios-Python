valor_divida = float(input("Digite o valor da dívida: R$ "))

print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
print("-" * 70)

parcelas_juros = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

for qtd_parcelas, juros in parcelas_juros:
    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas if qtd_parcelas > 0 else valor_total
    
    print(f"R$ {valor_total:.2f} | R$ {valor_juros:.2f} | {qtd_parcelas:19} | R$ {valor_parcela:.2f}")