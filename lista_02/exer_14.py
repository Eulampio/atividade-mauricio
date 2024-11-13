
import math

def desvio_padrao(lista):

    if len(lista) < 2:
        raise ValueError("A lista deve conter pelo menos dois elementos para calcular o desvio padrão.")
    

    media = sum(lista) / len(lista)
    

    soma_quadrados = sum((x - media) ** 2 for x in lista)
    
    # Calcula o desvio padrão
    desvio = math.sqrt(soma_quadrados / len(lista))
    
    return desvio

# Exemplo de uso:
lista = [10, 20, 30, 40, 50]
resultado = desvio_padrao(lista)
print("O desvio padrão da lista é: {resultado}")
