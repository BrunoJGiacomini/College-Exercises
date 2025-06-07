#Transponha uma matriz 3x3 (trocar linhas por colunas).

array =[
[ 23, 87, 45 ],
[ 76, 12, 59 ],
[ 34, 98, 61 ]
]


transposta = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3): 
    for j in range(3):      
        transposta[j][i] = array[i][j]

for linha in transposta:
    print(linha)


    