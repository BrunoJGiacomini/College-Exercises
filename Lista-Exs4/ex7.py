#Conversor de Moeda: Crie um programa que converta uma quantia em dólares para euros. Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0".

while True:
    valor = float(input("Digite o valor a ser convertido:"))

    if valor == 0:
        print("Finalizando...")
        break
    else:
        print(f"O valor de ${valor} dólares em Euros = €{valor*0.88} ")