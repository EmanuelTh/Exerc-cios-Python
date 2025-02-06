while True:
    nome = input("Digite o nome do atleta (ou deixe em branco para sair): ")
    if nome == "":
        break

    saltos = []
    for i in range(5):
        salto = float(input(f"Digite a distância do {i+1}º salto (em metros): "))
        saltos.append(salto)

    print(f"Atleta: {nome}")
    for i in range(5):
        print(f"{i+1}º Salto: {saltos[i]} m")

    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)
    media_saltos = sum(saltos) / len(saltos)

    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_saltos:.1f} m")
    print("Resultado final:")
    print(f"{nome}: {media_saltos:.1f} m")