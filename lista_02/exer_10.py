
def diferenca_max_min(lista):
    if not lista:
        return None  
    
    max_val = max(lista)
    min_val = min(lista)
   
    return max_val - min_val

lista = [64, 25, 12, 22, 11]
resultado = diferenca_max_min(lista)
print("A diferença entre o maior e o menor valor da lista é: {resultado}")
