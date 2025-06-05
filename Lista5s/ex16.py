#Junte duas listas e remova os elementos repetidos.

lista = [1,83, 2, 47, 91, 35, 68, 14, 76, 59, 23]
lista2 = [2,1,3,37, 5, 91, 14, 64, 41, 73, 29, 86, 10,23,23,91]


for i in lista2:
    if i in lista:
        lista2.remove(i)
    else:
        lista.append(i)


print(lista)
print(lista2)
