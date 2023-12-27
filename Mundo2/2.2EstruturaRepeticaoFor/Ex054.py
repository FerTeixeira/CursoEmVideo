"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores."""
from datetime import date
maiores = 0
menores = 0
for i in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = date.today().year - nasc
    if idade >= 18:
        maiores +=1
    else:
        menores += 1
print(f"{maiores} pessoas já são maiores e {menores} não atingiram a maioridade.")
