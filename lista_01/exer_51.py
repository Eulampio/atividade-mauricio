
def verifica_ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

print(verifica_ano_bissexto(2020))