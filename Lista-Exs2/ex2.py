idade = int(input("Digite qual a sua idade:"))

if idade < 18:
    print("Você é menor de idade")
elif idade >= 18 and idade <65:
    print("Você é maior de idade")
else:
    print("Você é idoso")

