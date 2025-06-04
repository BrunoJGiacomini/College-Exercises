lista = [34, 7, 18, 55, 90, 23, 2, 67, 44, 81, 10, 39, 72, 5, 88]


for i in lista[:]:
     if i % 2 != 0:

        lista.remove(i)
    
print(lista)