#Crie uma função valida_idade(idade) que retorne se a pessoa é maior de idade.

def valida_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
print(valida_idade(21))