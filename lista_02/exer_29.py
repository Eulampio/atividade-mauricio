
def intervalo_entre_elementos(lista):

    if not lista:
        return 0 
    maior = max(lista)
    menor = min(lista)
    
    return maior - menor
lista = [5, 12, 9, 3, 15, 8]
resultado = intervalo_entre_elementos(lista)
print("O intervalo entre os elementos é: {resultado}")
