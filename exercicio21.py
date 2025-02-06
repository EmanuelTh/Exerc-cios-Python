while True:
    nome = input("Digite o nome do atleta (ou deixe em branco para sair): ")
    if nome == "":
        break

    notas = []
    for i in range(7):
        nota = float(input(f"Nota do {i+1}º jurado: "))
        notas.append(nota)

    print(f"Atleta: {nome}")
    for i in range(7):
        print(f"Nota: {notas[i]}")

    melhor_nota = max(notas)
    pior_nota = min(notas)
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    media = sum(notas) / len(notas)

    print("Resultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media:.2f}")
    print("")