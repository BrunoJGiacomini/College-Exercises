altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))

imc = peso/ altura**2

if(imc < 18.5):
    print(f"Seu IMC é {imc:.2f}, classificado como Abaixo do peso")
elif(imc > 18.5 and imc < 24.9):
    print(f"Seu IMC é {imc:.2f}, classificado como Peso Normal")
elif(imc > 25 and imc < 29.9):
    print(f"Seu IMC é {imc:.2f}, classificado como Sobrepeso")
elif(imc > 30 and imc < 34.9):
    print(f"Seu IMC é {imc:.2f}, classificado como Obseidade Grau 1")
elif(imc > 35 and imc < 39.9):
    print(f"Seu IMC é {imc:.2f}, classificado como Obseidade Grau 2")
elif(imc > 40):
    print(f"Seu IMC é {imc:.2f}, classificado como Obesidade Grau 3")