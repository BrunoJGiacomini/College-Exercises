nomes = ["Bruno", "Clara", "Guilherme", "Mary", "Yasmin", "Zyon"]

while True:
    nome = input("Digite um nome (ou 'sair'): ")

    if nome.lower() == 'sair':
        print("Saindo...")
        break
    elif nome in nomes:
        print("Nome já está na lista!")
    else:
        nomes.append(nome)
        print(f"{nome} foi adicionado à lista.")

print(nomes)


