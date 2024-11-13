def multiplica_escalar(lista, escalar):
    nova_lista = [x * escalar for x in lista]
    return nova_lista

lista_original = [1, 2, 3, 4]
escalar = 3
resultado = multiplica_escalar(lista_original, escalar)

print("Lista original:", lista_original)
print("Resultado da multiplicação escalar:", resultado)
