def busca_neg(vetor):
    
    for index in range(len(vetor)):
        if vetor[index] < 0:
            print(vetor[index])

vetor= [1,20,5,-6,40,-97]

busca_neg(vetor)