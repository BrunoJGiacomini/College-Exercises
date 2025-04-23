materia = input("Digite o nome da matéria:")
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))

media = (nota1 + nota2) / 2

print(f"A media na {materia} foi de {media}")

if media >= 6: 
    print("Parabéns, Aluno!! Vc está aprovado!!")
elif media < 6:
    print("Vc está de recuperação!!")
elif media <= 2:
    print("Reprovado!!!")
