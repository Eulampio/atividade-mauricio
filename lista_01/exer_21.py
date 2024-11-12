
a = float(input("Digite um nº: "))
b = float(input("Digite outro nº: "))
c = float(input("Digite mais um nº: "))

lista = media_lista = [a, b, c]

def media_lista(lista):
    if len(lista) == 0:
        return 0  
    soma = sum(lista)
    media = soma / len(lista)
    return media

print(media_lista([a, b, c]))