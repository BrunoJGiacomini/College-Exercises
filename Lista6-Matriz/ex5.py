#Conte quantos números pares existem em uma matriz.


matriz = [
    [45, 78, 12],
    [33, 59, 84],
    [17, 91, 62]
]


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            print(matriz[i][j])

