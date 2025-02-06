import random


random.seed(823036)
vetnum_aleatorios = []

while len(vetnum_aleatorios) < 20:
    numero = random.randint(2, 75)
    if numero not in vetnum_aleatorios:
        vetnum_aleatorios.append(numero)


vetnum_aleatorios.sort()


print(vetnum_aleatorios)