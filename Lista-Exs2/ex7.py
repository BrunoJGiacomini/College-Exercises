#Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

nota = float(input("Digite sua nota:"))

if(nota >= 90 and nota <= 100):
    print(f"Sua nota {nota} é tipo A")

elif(nota >= 80 and nota <= 89):
    print(f"Sua nota {nota} é tipo B")

elif(nota >= 70 and nota <= 79):
    print(f"Sua nota {nota} é tipo C")

elif(nota >= 60 and nota <= 69):
    print(f"Sua nota {nota} é tipo D")

elif(nota < 60):
    print(f"Sua nota {nota} é tipo F")