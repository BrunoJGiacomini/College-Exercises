#Controle de Votação: Faça um programa que permita cadastrar votos para 3 candidatos. Exibe contagem ao final quando for digitado "fim".

opcao = ""
cont1 = 0
cont2 = 0
cont3 = 0


while opcao != "fim":
    opcao = input("Vote nos candidatos: \n1-Yuri Alberto\n2-Depay\n3-Dorivaldiola\nOpção:").lower()

    if opcao == "fim":
        print("Finalizando votação!")
        break
    elif int(opcao) == 1:
        cont1 += 1
    elif int(opcao) == 2:
        cont2 += 1
    elif int(opcao) == 3:
        cont3 += 1
    else:
        print("Opção errada!")

print(f"Votos para Yuri alberto: {cont1}")
print(f"Votos para Depay: {cont2}")
print(f"Votos para Dorivadiola: {cont3}")
    