number = int(input("Digite o número para a tabuada:"))

for i in range(1,11):
    if(i % 3 == 0):
        print("Múltiplo de 3")
    else:
        print(f"{number} x {i} = {number*i}")
    