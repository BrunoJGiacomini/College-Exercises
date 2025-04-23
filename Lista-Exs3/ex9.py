# Solicita um número ao usuário
numero = input("Digite um número: ")

# Inicializa a soma dos dígitos
soma = 0

# Itera sobre cada dígito do número e soma
for digito in numero:
    soma += int(digito)

# Exibe o resultado
print(f"A soma dos dígitos de {numero} é {soma}.")


