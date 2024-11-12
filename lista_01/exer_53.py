
def conta_ocorrencias_caracteres(s):
    return {char: s.count(char) for char in set(s)}


print(conta_ocorrencias_caracteres("banana"))  