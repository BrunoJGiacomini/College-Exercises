#Multiplique todos os elementos de uma matriz por um número dado pelo usuário.

matriz = [
    [7, 12, 5],
    [3, 9, 14],
    [8, 6, 11]
]

matriz2 = []


num = int(input("Digite um número para multiplicar os elementos da matriz:"))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        dobro = num * matriz[i][j]
        matriz2.append(dobro)
       

for linha in matriz2:
    print(linha, end= " ")
    