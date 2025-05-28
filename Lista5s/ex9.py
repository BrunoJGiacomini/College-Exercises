alunos = []
todas_as_notas = []

quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

for _ in range(quantidade_alunos):
    nome = input("Nome do aluno: ")
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1} do aluno {nome}: "))
        notas.append(nota)
        todas_as_notas.append(nota)  # Armazena todas as notas em uma lista separada
    media = sum(notas) / len(notas)
    alunos.append({'nome': nome, 'notas': notas, 'media': media})

# Calculando a média geral de todas as notas
media_geral = sum(todas_as_notas) / len(todas_as_notas)

print(f"\nMédia geral de todas as notas: {media_geral:.2f}")
print("Alunos com média acima da média geral:")

for aluno in alunos:
    if aluno['media'] > media_geral:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")
