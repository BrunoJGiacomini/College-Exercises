#Faça uma função que recebe uma lista e retorna outra com os elementos em ordem reversa (sem usar .reverse() ou [::-1]).

lista = [17, 6, 33, 21, 9, 48, 12, 3, 27, 39]
array = []




for i in range(len(lista)-1,-1,-1):
   
    array.append(lista[i])


print(array)

