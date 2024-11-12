
a = int(input("Digite um nº: "))
b = int(input("Digite outro nº: "))
c = int(input("Digite mais um nº: "))

lista = remove_duplicados = [a, b, c]

def remove_duplicados(lista):
    return list(set(lista))

print(remove_duplicados([a,b,b,c,c,c]))  