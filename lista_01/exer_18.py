
texto = input("Digite uma frase: ")
def alterna_maiusculas(texto):
    resultado = []
    maiuscula = True
    for char in texto:
        if char.isalpha():
            if maiuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            maiuscula = not maiuscula
        else:
            resultado.append(char)
    return ''.join(resultado)

print(alterna_maiusculas(texto))