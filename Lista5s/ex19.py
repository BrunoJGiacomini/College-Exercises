#Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho.

compras = []

while True:
    compra = input("Digite o item para adicionar ao carrinho (ou 'sair'):")

    if compra.lower() == 'sair':
        print("Saindo...")
        break
    else:
        compras.append(compra)
        print(f"{compra} foi adicionado ao carrinho!")

print(compras)
