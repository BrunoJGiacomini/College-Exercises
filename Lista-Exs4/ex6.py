#Média de Notas: Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa.

cont =0
soma = 0


while True:

    nota = float(input("Digite sua nota (0 a 10):"))

    if nota < 0:
        print("Nota Inválida!")
        break
    else:
        cont += 1
        soma += nota
        media = soma / cont

print(f"A sua média final = {media}")
    



