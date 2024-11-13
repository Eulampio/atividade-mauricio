
def separa_pares_impares(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = separa_pares_impares(lista)
print("Pares: {pares}")
print("Ímpares: {impares}")
