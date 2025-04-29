#Quantidade de valores: Conte quantos valores positivos, negativos e zeros foram digitados.

pos = 0
neg = 0
zeros = 0


while True:
    num = input("Digite os números('Sair' para encerrar):").lower()

    if num == "sair":
        break
    elif int(num) < 0:
        neg += 1
    elif int(num) == 0:
        zeros += 1
    else:
        pos += 1
        


print(f"Tem {pos} números positivos")
print(f"Tem {neg} números negativos")
print(f"Tem {zeros} números zeros")