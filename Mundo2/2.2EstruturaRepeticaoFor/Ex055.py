"""Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso(kg) da pessoa {i}: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso é {maior}kg e o menor peso é {menor}kg.")