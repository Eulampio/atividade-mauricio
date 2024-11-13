
def busca_binaria(lista, elemento):

    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2  
        
        if lista[meio] == elemento:
            return meio  
        
        elif lista[meio] > elemento:
            fim = meio - 1
        

        else:
            inicio = meio + 1
    
    return -1

lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento = 7

indice = busca_binaria(lista, elemento)
if indice != -1:
    print("Elemento {elemento} encontrado no índice {indice}.")
else:
    print("Elemento {elemento} não encontrado.")
