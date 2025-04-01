import random

random.seed(823036)
vetnum_aleatorios = []
excluir = {2, 3, 4, 9, 21, 23, 34, 36, 42, 43, 48, 51, 55, 65, 66, 67, 68, 69, 70, 71}

while len(vetnum_aleatorios) < 20:
    numero = random.randint(2, 75)
    if numero not in excluir and numero not in vetnum_aleatorios:
        vetnum_aleatorios.append(numero)

vetnum_aleatorios.sort()

print(vetnum_aleatorios)
