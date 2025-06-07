#Some todos os elementos de uma matriz 3x3.



matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
        soma += matriz[i][j]


print(soma)
