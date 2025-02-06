preco_por_kg = float(input("Preço do pão: R$ "))
peso_por_pao = 0.087
preco_por_pao = preco_por_kg * peso_por_pao

print("Panificadora Pão de Ontem - Tabela de preços")
for quantidade in range(1, 51):
    valor_total = quantidade * preco_por_pao
    print(f"{quantidade} - R$ {valor_total:.2f}")
