"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato."""
t = maior = menor = c = 0
produto = " "
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    t += preco
    if c == 0:
        menor = preco
        produto = nome
    if preco < menor:
        menor = preco
        produto = nome

    if preco > 1000:
        maior +=1
    r = " "
    c +=1
    while r not in "SN":
        r = str(input("Deseja cadastrar mais produtos? ")).upper().strip()[0]
    if r == "N":
        break

print(f"O total gasto na compra foi {t}")
print(f"{maior} produtos custam mais que R$1000")
print(f"O produto mais barato é o {produto} que custa R${menor}")