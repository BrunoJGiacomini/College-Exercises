#Some os elementos de cada linha de uma matriz e mostre os resultados.

matriz = [
    [14, 67, 82],
    [29, 50, 73],
    [910, 36, 249]
]



for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
    print(soma)







