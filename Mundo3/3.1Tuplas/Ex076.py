"""Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular."""
lista = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.90, "Estojo", 25,
         "Transferirdor", 4.20, "Compasso", 9.99, "Mochila", 120.32,
         "Canetas", 22.30, "Livro", 34.90)
for item in range(len(lista)):
    if item % 2 == 0:
        print(f"{lista[item]:.<30}", end="")
    else:
        print(f"R${lista[item]:>7}")