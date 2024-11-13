
def multiplica_matrizes(matriz1, matriz2):

    if len(matriz1) != 2 or len(matriz1[0]) != 2 or len(matriz2) != 2 or len(matriz2[0]) != 2:
        raise ValueError("Ambas as matrizes devem ser 2x2")
    
    c11 = matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0]
    c12 = matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]
    c21 = matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0]
    c22 = matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]
    
    return [[c11, c12], [c21, c22]]

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

resultado = multiplica_matrizes(matriz1, matriz2)
print("Resultado da multiplicação das matrizes:")
for linha in resultado:
    print(linha)
