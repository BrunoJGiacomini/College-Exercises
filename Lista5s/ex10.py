
numeros = []

while True:
    num = int(input("Digite um número para somar (ou 0 para sair):"))

    if num == 0:
        print("Saindo...")
        break
    else:
        numeros.append(num)
        

total = sum(numeros)

print(f"A lista é = {numeros}")
print(f"A soma é = {total}")


