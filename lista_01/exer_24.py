a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))
c = float(input("Digite mais um nº: "))

lista = conta_ocorrencias= [a, b, c]

def conta_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

print(conta_ocorrencias([a, b, b, c,b], b))