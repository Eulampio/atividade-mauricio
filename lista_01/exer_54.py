
def media_notas(dicionario):
    return sum(dicionario.values()) / len(dicionario)

print(media_notas({'João': 8, 'Maria': 9, 'Pedro': 7})) 
