lista = []

while True:
    valor = input("Digite o valor que deseja somar (ou 'sair' para encerrar):")
    if valor.lower() == 'sair':
        print("Saindo...")
        break
    else:
        numero = int(valor)
        lista.append(numero)

total = sum(lista)

print(f"Soma: {total}")
