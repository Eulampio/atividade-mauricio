
def remove_multiplos(lista, n):
    
    return [x for x in lista if x % n != 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 2
resultado = remove_multiplos(lista, n)
print("Lista após remover múltiplos de {n}: {resultado}")
