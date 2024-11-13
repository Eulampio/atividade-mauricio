
def conta_intervalo(lista, inicio, fim):
    
    contador = 0
    for numero in lista:

        if inicio <= numero <= fim:
            contador += 1
    
    return contador

lista = [1, 3, 5, 7, 9, 10, 12, 15]
inicio = 5
fim = 10

resultado = conta_intervalo(lista, inicio, fim)
print("Quantidade de números no intervalo [{inicio}, {fim}]: {resultado}")
