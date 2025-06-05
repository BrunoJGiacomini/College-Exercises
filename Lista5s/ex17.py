#Faça uma função que recebe uma lista de números e retorna uma nova lista com o fatorial de cada número.

array = [2, 4, 5]
nova = []

fatorial = 1

for i in array:
    for j in range(1, i + 1):
        fatorial*=j
    nova.append(fatorial)


print(nova)