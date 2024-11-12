

frase = input("Digite uma frase: ")
def troca_vogais(s, nova_letra):
    vogais = "aeiouAEIOUáé"
    resultado = ''.join([nova_letra if char in vogais else char for char in s])
    return resultado

print(troca_vogais(frase, "*"))