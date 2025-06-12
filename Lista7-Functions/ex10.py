"""Crie um menu com funções para:
Cadastrar nomes
Listar nomes
Sair do programa"""


 
nomes = []

def cadastrar():
    nome = input("Digite o nome para cadastrar: ")
    nomes.append(nome)
    print("Nome cadastrado com sucesso!")

def listar():
    if not nomes:
        print("Nenhum nome cadastrado.")
    else:
        print("Lista de nomes:")
        for nome in nomes:
            print(f"- {nome}")

def menu():
    while True:
        opcao = int(input(
            "Bem-Vindo\n"
            "Escolha uma das opções abaixo:\n"
            "1 - Cadastrar Nomes\n"
            "2 - Listar Nomes\n"
            "3 - Sair\n"
            "Opção: "
        ))

        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

menu()
