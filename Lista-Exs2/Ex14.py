quantidade = float(input("Digite a quantidade de kWh consumidos:"))
valor = float(input("Digite o valor por kWh:"))

conta = quantidade * valor 

print(f"O valor da conta de energia = R$ {conta:,.2f}")