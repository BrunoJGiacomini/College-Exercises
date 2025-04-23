preco = float(input("Digite o preço do produto:"))

if(preco > 100):
    desconto = preco * 0.9
    print(f"Seu produto com valor R$ {preco} saiu por R$ {desconto}")
else:
    print(f"Seu produto saiu por R$ {preco}")