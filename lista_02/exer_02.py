
def produto_lista(lista):

    produto = 1
    
    for numero in lista:
        produto *= numero
    
    return produto

lista = [1, 2, 3, 4]
resultado = produto_lista(lista)

print("Lista:", lista)
print("Produto de todos os elementos:", resultado)
