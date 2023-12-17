"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date
ano = int(input("Digite o ano que você quer analisar: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSESTO!")
else:
    print(f"O ano {ano} não é BISSESTO!")