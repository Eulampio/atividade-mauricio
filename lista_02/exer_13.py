
def diferenca_elementos_lista(lista):
    diferencas = []
    
    if len(lista) < 2:
        return diferencas  
    
    for i in range(len(lista) - 1):
        diferenca = abs(lista[i] - lista[i + 1])
        diferencas.append(diferenca)
    
    return diferencas

lista = [10, 20, 15, 30, 25]
resultado = diferenca_elementos_lista(lista)
print("As diferenças absolutas entre os elementos consecutivos são: {resultado}")
