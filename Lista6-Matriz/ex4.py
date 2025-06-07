#Mostre os elementos da diagonal secundária de uma matriz quadrada.


matriz= [
    [1, 22, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 111, 12],
    [13, 144, 15, 16]
]

n =len(matriz)

for i in range(n):
    print(matriz[i][n-i-1])