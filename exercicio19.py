gabarito = []
print("Professor, digite o gabarito da prova (10 questões):")
for i in range(10):
    resposta = input(f"Resposta da questão {i+1}: ").upper()
    while resposta not in ["A", "B", "C", "D", "E"]:
        print("Resposta inválida! Digite A, B, C, D ou E.")
        resposta = input(f"Resposta da questão {i+1}: ").upper()
    gabarito.append(resposta)

alunos = []
continuar = "S"

while continuar.upper() == "S":
    respostas_aluno = []
    acertos = 0

    print("Digite as respostas do aluno (A, B, C, D ou E) para cada questão:")
    for i in range(10):
        resposta = input(f"Resposta da questão {i+1}: ").upper()
        while resposta not in ["A", "B", "C", "D", "E"]:
            print("Resposta inválida! Digite A, B, C, D ou E.")
            resposta = input(f"Resposta da questão {i+1}: ").upper()
        respostas_aluno.append(resposta)

        if resposta == gabarito[i]:
            acertos += 1

    alunos.append(acertos)
    print(f"Total de acertos: {acertos}")

    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ")
    while continuar.upper() not in ["S", "N"]:
        print("Opção inválida! Digite S ou N.")
        continuar = input("Outro aluno vai utilizar o sistema? (S/N): ")

if alunos:
    maior_acerto = max(alunos)
    menor_acerto = min(alunos)
    total_alunos = len(alunos)
    media_notas = sum(alunos) / total_alunos

    print("Maior acerto:", maior_acerto)
    print("Menor acerto:", menor_acerto)
    print("Total de alunos que utilizaram o sistema:", total_alunos)
    print("Média das notas da turma:", media_notas)
else:
    print("Nenhum aluno utilizou o sistema.")