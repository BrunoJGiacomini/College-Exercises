#Simulação de Dados de Sensor: Crie um programa que simule a leitura de dados de um sensor e continue capturando dados até que um valor fora do intervalo de operação seja detectado (por exemplo, fora de 0 a 100).


dados = []


while True:
    valores = float(input("Digite o valor:"))

    if valores < 0 or valores > 100:
        print("Valor fora do intervalo!")
        break
    else:
        dados.append(valores)

print(f"{dados}")