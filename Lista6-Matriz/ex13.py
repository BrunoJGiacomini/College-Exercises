#Faça um programa que leia uma matriz 4x4 e diga quantos elementos estão acima da média.


array =[
[ 23, 81, 45, 27 ],
[ 76, 12, 59, 25 ],
[ 34, 98, 68, 13 ],
[ 29, 13, 22, 71 ]
]

acima = []

soma = 0
quant = 0

for linha in range(len(array)):
    for coluna in range(len(array[0])):
        soma += array[linha][coluna]
        quant +=1
        print(f"{array[linha][coluna]}", end= " ")
    print()

media = soma / quant

print(f"Média = {media:.2f}")

for i in range(len(array)):
    for j in range(len(array[0])):
        valor = array[i][j]
        if valor > media:
            acima.append(valor)

print(f"Números acima da média = {acima}")
            
