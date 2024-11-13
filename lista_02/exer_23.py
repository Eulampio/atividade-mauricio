
def multiplica_pares(lista):
    
    produto = 1
    
    encontrou_par = False
    
    for numero in lista:
        if numero % 2 == 0:  
            produto *= numero
            encontrou_par = True  
    
    if not encontrou_par:
        return 0
    
    return produto

lista = [2, 3, 4, 5, 6]
resultado = multiplica_pares(lista)
print("O produto dos números pares da lista é: {resultado}")
