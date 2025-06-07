#Verifique se duas matrizes 2x2 digitadas pelo usuário são iguais.

linhas = 2
coluna = 2

matriz = []
matriz2= []

for i in range(linhas):
    linha = []
    for j in range(coluna):
        num = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

for a in range(linhas):
    lin = []
    for b in range(coluna):
        nume = int(input(f"Digite o valor para [{a}][{b}]: "))
        lin.append(nume)
    matriz2.append(lin)


if matriz == matriz2:
    print("As matrizes são iguais!")
else:
    print("Matrizes não são iguais!")
    

