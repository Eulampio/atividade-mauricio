texto = input("Digite uma palavra: ")
def retira_espacos(texto):
    return texto.replace(" ", "")

# Testando a função
print(retira_espacos(texto))