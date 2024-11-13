
def selection_sort(lista):

    for i in range(len(lista)):
    
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        
        lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista

lista = [64, 25, 12, 22, 11]
resultado = selection_sort(lista)
print(f"Lista ordenada: {resultado}")
