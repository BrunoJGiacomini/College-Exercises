#Conversão de Temperatura: Faça um programa que converta uma temperatura de Celsius para Fahrenheit. Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair".




while True:

    temp = input("Digite a temperatura em Celsius para converter ('sair' para encerrar):").lower()
    

    if temp == "sair":
        break
    else:
        print(f"A temperatura de {int(temp)}°C para Fahrenheit = {(int(temp) * 1.8)+32:.2f}°F ")