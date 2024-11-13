
def quick_sort(lista):
    pilha = [(0, len(lista) - 1)]
    
    while pilha:
        inicio, fim = pilha.pop()
        
        if inicio < fim:
            pivo_index = particiona(lista, inicio, fim)
            
            pilha.append((inicio, pivo_index - 1)) 
            pilha.append((pivo_index + 1, fim))     
    
    return lista

def particiona(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    
    return i + 1

lista = [64, 25, 12, 22, 11]
resultado = quick_sort(lista)
print(f"Lista ordenada: {resultado}")
