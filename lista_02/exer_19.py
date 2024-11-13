
def diagonais_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz deve ser quadrada.")
    
    diagonais = []
    n = len(matriz)  
    
    diagonal_principal = [matriz[i][i] for i in range(n)]

    diagonal_secundaria = [matriz[i][n-i-1] for i in range(n)]

    diagonais.append(diagonal_principal)
    diagonais.append(diagonal_secundaria)
    
    return diagonais

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = diagonais_matriz(matriz)
print("Diagonal principal: {resultado[0]}")
print("Diagonal secundária: {resultado[1]}")
