#Crie uma função calcular_desconto(valor, percentual=10) que aplique um desconto percentual ao valor.

def calcular_desconto(valor, percentual=10):
    return valor * (1-percentual/100)


print(calcular_desconto(220))