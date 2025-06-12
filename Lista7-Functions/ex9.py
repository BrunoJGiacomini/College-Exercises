#Crie uma função que conte o número de vogais em uma palavra.

def vogais(palavra):
    for i in palavra:
        if i.lower() in "aeiou":
            print(i)
    
vogais("nome")