def e_primo(n, contador_divisoes):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        contador_divisoes[0] += 1
        if n % i == 0:
            return False
    return True

def encontrar_primos(N):
    primos = []
    contador_divisoes = [0]
    for num in range(1, N + 1):
        if e_primo(num, contador_divisoes):
            primos.append(num)
    return primos, contador_divisoes[0]

def main():
    N = int(input("Digite um número inteiro N: "))
    primos, num_divisoes = encontrar_primos(N)
    
    print(f"Números primos entre 1 e {N}: {primos}")
    print(f"Número de divisões executadas: {num_divisoes}")

if __name__ == "__main__":
    main()