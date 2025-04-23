Km_percorridos = float(input("Digite a quantidade de Km percorridos:"))
dias = float(input("Digite a quantidade de dias que alugou:"))

pagar = 90*dias + 0.20*Km_percorridos

print(f"O preço total a pagar = R$ {pagar:,.2f}")