
def ocorrencias_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower() 
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(ocorrencias_palavras(texto))