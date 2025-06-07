#Encontre o maior e o menor elemento de uma matriz.


matriz = [
    [13, 62, 81],
    [29, 50, 71],
    [19, 36, 9]
]

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        num = matriz[i][j]
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print(maior)
print(menor)

        
    