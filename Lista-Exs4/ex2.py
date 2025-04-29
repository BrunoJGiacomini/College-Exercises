#Encontrar o Máximo: Crie um programa que peça ao usuário para inserir números e encontre o maior número inserido. O programa deve continuar pedindo números até que o usuário digite "sair".


opcao = input("Digite os números (Digite 'sair' para encerrar): ").lower()
num = int(opcao)
maior = num

while opcao != "sair":
    opcao = input("Digite os números (Digite 'sair' para encerrar): ").lower()

    if opcao == "sair":
        print("Saindo...")
    else:
        num = int(opcao)
        if num > maior:
            maior = num

print(f"O maior número entre eles é o {maior}")
