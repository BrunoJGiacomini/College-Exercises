num1 = float(input("Digite um número 1:"))
num2 = float(input("Digite o número 2:"))

if num1 > num2:
    print(f"{num1} é maior que o {num2}")
elif num2 > num1:
    print(f"{num2} é maior que o {num1}")
else:
    print("Os números são iguais")