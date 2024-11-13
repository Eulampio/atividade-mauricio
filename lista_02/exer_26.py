
def merge_sort(lista):
    
    if len(lista) <= 1:
        return lista

    
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(lista1, lista2):
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
resultado = merge_sort(lista)
print("Lista ordenada: {resultado}")
