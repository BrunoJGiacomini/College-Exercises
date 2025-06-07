#Crie uma matriz 3x3 com valores digitados pelo usuário.Crie uma matriz 3x3 com valores digitados pelo usuário.

linhas = 2
coluna = 2

matriz = []

for i in range(linhas):
    linha = []
    for j in range(coluna):
        num = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print(linha)
