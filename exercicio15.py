cidades = []

for i in range(5):
    codigo = int(input(f"Código da cidade {i+1}: "))
    veiculos = int(input(f"Número de veículos de passeio (1999) da cidade {i+1}: "))
    acidentes = int(input(f"Número de acidentes com vítimas (1999) da cidade {i+1}: "))
    cidades.append({"codigo": codigo, "veiculos": veiculos, "acidentes": acidentes})

maior_acidentes = cidades[0]["acidentes"]
menor_acidentes = cidades[0]["acidentes"]
codigo_maior = cidades[0]["codigo"]
codigo_menor = cidades[0]["codigo"]

total_veiculos = 0
total_acidentes_menos_2000 = 0
contador_menos_2000 = 0

for cidade in cidades:
    total_veiculos += cidade["veiculos"]

    if cidade["acidentes"] > maior_acidentes:
        maior_acidentes = cidade["acidentes"]
        codigo_maior = cidade["codigo"]

    if cidade["acidentes"] < menor_acidentes:
        menor_acidentes = cidade["acidentes"]
        codigo_menor = cidade["codigo"]

    if cidade["veiculos"] < 2000:
        total_acidentes_menos_2000 += cidade["acidentes"]
        contador_menos_2000 += 1

media_veiculos = total_veiculos / 5
media_acidentes_menos_2000 = total_acidentes_menos_2000 / contador_menos_2000 if contador_menos_2000 > 0 else 0

print(f"\nMaior índice de acidentes: {maior_acidentes} (Cidade {codigo_maior})")
print(f"Menor índice de acidentes: {menor_acidentes} (Cidade {codigo_menor})")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes_menos_2000:.2f}")