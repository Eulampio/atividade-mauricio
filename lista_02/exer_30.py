
def histograma(lista):
    ocorrencias = {}
    
    for elemento in lista:
        if elemento in ocorrencias:
            ocorrencias[elemento] += 1  
        else:
            ocorrencias[elemento] = 1  
    
    return ocorrencias

lista = [1, 2, 2, 3, 4, 4, 4, 5, 5]
resultado = histograma(lista)
print("Histograma de ocorrências: {resultado}")
