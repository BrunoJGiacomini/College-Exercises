#Crie uma lista com 5 strings e conte quantas começam com a letra 'A'.


palavras = ["Amor", "alegria", "Corinthians", "Azul", "Clara","Catalão","alura"]


contador = 0


for palavra in palavras:
    if palavra[0].lower() == 'a':
        contador += 1

# Exibe o resultado
print("Quantidade de palavras que começam com 'A' ou 'a':", contador)
