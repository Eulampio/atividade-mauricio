texto = input("Digite uma palavra: ")

def conta_letras(letra):
    contador = 0
    for item in texto:
        if item == letra:
            contador += 1
    return contador

letra = "s"
print("A letra", letra, "aparece",conta_letras(letra), "vezes em", texto)