
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  
    return True  

lista = [1, 2, 3, 4, 5]
resultado = esta_ordenada(lista)
print("A lista está ordenada em ordem crescente? {resultado}")
