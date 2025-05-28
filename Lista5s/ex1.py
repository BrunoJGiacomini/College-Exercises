numeros = []
copia = numeros[:]

for i in range(5):
    numeros.append(i+1)

for n in numeros:
    copia.append(n*2)

print(numeros)
print(copia)
