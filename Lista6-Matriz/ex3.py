#Mostre os elementos da diagonal principal de uma matriz quadrada.

matriz= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

elem = []

for i in range(len(matriz)):  # Índice da linha
    for j in range(len(matriz[i])):  # Índice da coluna
        if i == j:
            print(f"{matriz[i][j]}",end=" ")


