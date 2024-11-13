
def media_ponderada(lista_valores, lista_pesos):
    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")
    
    soma_produtos = sum(valor * peso for valor, peso in zip(lista_valores, lista_pesos))
    soma_pesos = sum(lista_pesos)
    
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")
    
    return soma_produtos / soma_pesos

valores = [10, 20, 30]
pesos = [1, 2, 3]

resultado = media_ponderada(valores, pesos)
print("A média ponderada é: {resultado}")
