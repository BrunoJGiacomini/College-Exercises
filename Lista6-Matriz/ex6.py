#Calcule a média de todos os elementos de uma matriz.

matriz = [
    [14, 67, 82],
    [29, 50, 73],
    [91, 36, 249]
]

quant = 0
soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
        quant += 1

media = soma/ quant

print(f"{media:.2f}")


            