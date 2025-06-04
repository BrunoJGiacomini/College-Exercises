#11.Remova todos os números negativos de uma lista de inteiros.

lista = [10,7,29,13,2003,23,27,-3,-2,-7,-5,100,1914]


for i in lista[:]:
    if i < 0:
        lista.remove(i)
        print(i)
    
print(lista)




