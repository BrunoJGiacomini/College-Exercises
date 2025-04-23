opcao = input("Escolha uma das opções: \n a)Saque \n b)Depósito \n Opção:")

conta = 1000

if(opcao == "a"):
    saque = int(input("Digite o valor do saque:"))
    if(saque > conta):
        print("Saldo insuficiente para saque")
    elif(saque <= conta):
        saldo = conta - saque

        print(f"Você sacou R$ {saque}")
        print(f"Você ficou com um saldo bancário de R$ {saldo}")
if(opcao == "b"):
    deposito = int(input("Digite o valor que deseja depositar em sua conta:"))

    contatotal = deposito + conta 

    print(f"Você depositou R$ {deposito} em sua conta bancária")
    print(f"Seu saldo da conta é de R${contatotal}")

elif(opcao != "a" and opcao != "b"):
    print("Opção Inválida")
