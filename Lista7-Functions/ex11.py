"""Simule um sistema de cadastro de produtos com as seguintes opções:

1 - Cadastrar produto  
2 - Listar produtos  
3 - Buscar produto pelo nome
4 - Sair
Use uma lista para armazenar os produtos.
Crie funções para cada opção.
Utilize laços de repetição e estruturas de decisão junto com funções."""

produtos = []

def cadastrar():
    produto = input("Digite o produto para cadastrar: ")
    produtos.append(produto.lower())
    print("produto cadastrado com sucesso!")

def listar():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos:")
        for produto in produtos:
            print(f"- {produto}")

def buscar():
    produto = input("Digite o nome do produto que deseja buscar:")
    if produto.lower() in produtos:
        print(f"Produto {produto} encontrado!")
    else:
        print(f"Produto {produto} não encontrado! ")


def menu():
    while True:
        opcao = int(input(
            "Bem-Vindo\n"
            "Escolha uma das opções abaixo:\n"
            "1 - Cadastrar produtos\n"
            "2 - Listar produtos\n"
            "3 - Buscar produto pelo nome\n" 
            "4 - Sair\n"
            "Opção: "
        ))

        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                buscar()
            case 4: 
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

menu()