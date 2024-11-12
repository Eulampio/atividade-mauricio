a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))
c = float(input("Digite mais um nº: "))

lista = maior_elemento = [a, b, c]

def maior_elemento(lista):
    if len(lista) == 0:
        return None 
    return max(lista)

print(maior_elemento([a, b, c]))