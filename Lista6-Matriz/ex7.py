#Crie uma matriz identidade 4x4.

linha = 4
coluna = 4
matriz = []

for i in range(linha):
    linha = []
    for j in range(coluna):
        if i == j:
            linha.append(1)
        else:
             linha.append(0)
    matriz.append(linha)



for linha in matriz:
    print(linha)


    
           
        
           
           
        