
def conta_ocorrencias_recursiva(lista, elem):
    if not lista:
        return 0
    return (1 if lista[0] == elem else 0) + conta_ocorrencias_recursiva(lista[1:], elem)

print(conta_ocorrencias_recursiva([1, 2, 3, 1, 4], 1))