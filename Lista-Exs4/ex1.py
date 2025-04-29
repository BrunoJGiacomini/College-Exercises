#Soma de Números: Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero. Quando zero for inserido, o programa deve imprimir a soma total.

num = ""
soma = 0

while num != 0:
    num = int(input("Digite os números para somar:"))
    if num != 0:
        soma+=num
    else:
        print("Encerrando....")
       

print(f"A soma entre os números = {soma}")
        
    


    