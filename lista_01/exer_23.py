a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))
c = float(input("Digite mais um nº: "))

lista = menor_elemento = [a, b, c]

def menor_elemento(lista):
    if len(lista) == 0:
        return None  
    return min(lista)

print(menor_elemento([a, b, c]))