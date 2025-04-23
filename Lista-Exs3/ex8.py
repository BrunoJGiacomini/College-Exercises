nota = " "
soma = 0 
media = 0

for i in range(5):
    nota = float(input(f"Digite a sua {i + 1}ª:"))
    soma += nota

media = soma / 5

print(f"A sua média final = {media:.2f}")
