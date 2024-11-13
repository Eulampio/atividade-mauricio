
def conta_consoantes(texto):

    consoantes = "bcdfghjklmnpqrtstvwxzBCDFGHJKLMNPQRTSTVWXZ"
    
    contador = 0
    
    for char in texto:
        if char in consoantes:
            contador += 1
    
    return contador

texto = "Olá Mundo!"
print(f"Número de consoantes: {conta_consoantes(texto)}")
