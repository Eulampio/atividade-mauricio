
i = int(input("Digite um nº: "))

def aproxima_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi

print(aproxima_pi(i))