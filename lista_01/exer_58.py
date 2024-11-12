
def conta_maiusculas(texto):
    return sum(1 for char in texto if char.isupper())
print(conta_maiusculas("Python É Lindo")) 