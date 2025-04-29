#Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo.

saldo = 5000

while True:
    saque = float(input("Digite o valor para o saque:"))

    if(saldo <=0):
        print("Saque indisponível! Saldo insuficiente")
        break
    elif saldo < saque:
        print("Saque indisponível! Saldo insuficiente")
    else:
        saldo -= saque
        print(f"Seu saque de {saque} foi autorizado com sucesso!")
        print(f"Saldo final da conta = {saldo}")
