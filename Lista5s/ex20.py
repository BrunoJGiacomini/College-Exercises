#Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair.

tarefas =  []

while True:
    opcao = int(input("Lista de Tarefas:\n1-Adicionar\n2-Remover\n3-Exibir\n4-Sair\nOpção:"))

    match opcao:
        case 1:
            tarefa = input("Digite oq quer adicionar:")
            tarefas.append(tarefa.lower())
            print(f"{tarefa}, adicionada com sucesso em sua lista de tarefas!")
        case 2:
            tarefa = input("Remover item da lista:")
            if tarefa.lower() in tarefas[:]:
                tarefas.remove(tarefa.lower())
                print("Tarefa removida com sucesso!")
            else:
                print("Tarefa não está na lista!")
        case 3:
            print(tarefas)
        case 4:
            print("Saindo...")
            break
        case _:
            print("Número inválido, tente novamente!")



            


    