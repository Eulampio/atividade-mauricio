
frase = input("Digite uma frase: ")
def apaga_vogais(s):
    vogais = "aeiouAEIOUáé"
    resultado = ''.join([char for char in s if char not in vogais])
    return resultado