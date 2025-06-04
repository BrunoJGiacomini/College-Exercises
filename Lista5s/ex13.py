#Leia uma lista de números e crie uma nova lista apenas com os valores únicos (sem repetições).

lista = [1,2,4,5,8,10,20,13,200,2,10,200]
uni = []

for i in lista[:]:
    if i in uni:
        lista.remove(i)
    else:
        uni.append(i)
    


print(lista)
print(uni)


