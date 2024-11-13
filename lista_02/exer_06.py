
def diferenca_conjuntos(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    
    diferenca = set_lista1 - set_lista2
    
    return list(diferenca)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = diferenca_conjuntos(lista1, lista2)
print("Elementos de lista1 que não estão em lista2: {resultado}")
