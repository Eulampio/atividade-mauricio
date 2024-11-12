texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")
def encontra_palavra(texto, palavra):
    palavras = texto.split()
    for i, p in enumerate(palavras):
        if p == palavra:
            return i
    return -1  

print(encontra_palavra(texto, palavra))