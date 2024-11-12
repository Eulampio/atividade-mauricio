
n = int(input("Digite um nº: "))

def eh_perfeito(n):
    if n < 1:
        return False
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return soma_divisores == n

print(eh_perfeito(n))