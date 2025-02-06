cardapio = {
    100: {"item": "Cachorro Quente", "preco": 1.20},
    101: {"item": "Bauru Simples", "preco": 1.30},
    102: {"item": "Bauru com ovo", "preco": 1.50},
    103: {"item": "Hambúrguer", "preco": 1.20},
    104: {"item": "Cheeseburguer", "preco": 1.30},
    105: {"item": "Refrigerante", "preco": 1.00}
}

total_geral = 0

while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
    
    if codigo == 0:
        break
    
    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor_item = cardapio[codigo]["preco"] * quantidade
        total_geral += valor_item
        print(f"{cardapio[codigo]['item']}: {quantidade} x R$ {cardapio[codigo]['preco']:.2f} = R$ {valor_item:.2f}")
    else:
        print("Código inválido! Tente novamente.")

print(f"Total geral do pedido: R$ {total_geral:.2f}")