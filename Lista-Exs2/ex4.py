num1 = float(input("Digite um número 1:"))
num2 = float(input("Digite o número 2:"))

opcao = input("Escolha uma das opções abaixo: \n a)Adição \n b)Subtração \n c)Multiplicação \n d) Divisão \n Opção:")

if opcao == "a":
    
    adicao = num1 + num2
    print(f"Resultado: {adicao}")
elif opcao == "b":

    subtracao = num1 - num2
    print(f"Resultado: {subtracao}")
elif opcao == "c":

    multiplicacao = num1 * num2
    print(f"Resultado: {multiplicacao}")
elif opcao == "d":

    divisao = num1 / num2
    print(f"Resultado: {divisao}")
else:
    print("Opção Inválida!!!")
