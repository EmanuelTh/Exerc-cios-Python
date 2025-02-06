print('quantos numeros tem o conjunto?')
n= int(input())
soma = 0
print('digite os valores: ')
vetorj = []
for i in range(n):
    x = int(input())
    vetorj.append(x)
     
vetorj.sort()
print(vetorj[0])
print(vetorj[-1])
p = sum(vetorj)
print(p)
