candidatos = {
    1: "Candidato A",
    2: "Candidato B",
    3: "Candidato C"
}

votos = {1: 0, 2: 0, 3: 0}

total_eleitores = int(input("Digite o número total de eleitores: "))

for i in range(total_eleitores):
    print(f"Eleitor {i + 1}, vote em um dos candidatos:")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    
    voto = int(input("Digite o número do candidato: "))
    
    if voto in candidatos:
        votos[voto] += 1
        print("Voto registrado com sucesso!")
    else:
        print("Voto inválido! Tente novamente.")

print("Resultado da eleição:")
for numero, nome in candidatos.items():
    print(f"{nome}: {votos[numero]} votos")