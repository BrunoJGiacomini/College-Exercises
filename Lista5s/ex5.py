
array = []
cont = 0
while True:
    valor = input("Digite o valor que deseja somar (ou 'sair' para encerrar):")
    if valor.lower() == 'sair':
        print("Saindo...")
        break
    else:
        numero = int(valor)
        array.append(numero)
        if numero == 3:
            cont+=1

print(cont)
array.sort()
print(array)

