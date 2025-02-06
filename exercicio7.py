from urllib.request import Request, urlopen
url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

vetor = webpage.split()
vetor_2 = []


for palavra in vetor:
    if len(palavra) == 5:
        vetor_2.append(palavra)

import random
palavra_s = random.choice(vetor_2)
vetor_l = ['_']*5
for i in range(5):
    letra = input('escreva uma letra: ')
    for index in range(5):
        if letra == palavra_s[index]:
            vetor_l[index] = letra
    print(vetor_l)
    chute = input('quer dar um chute?(s/n): ')
    if chute == 's':
        chute1 = input()
        if chute1 == palavra_s:
            print('voce acertou a palavra era: ', palavra_s)
            break
    print('voce gastou:', i + 1, 'de 5 chances')