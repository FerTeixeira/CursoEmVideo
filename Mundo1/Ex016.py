""""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira."""
from math import trunc
n = float(input("Digite um número: "))
print(f"O número digitado foi {n} e a sua porção inteira é {trunc(n)}.")
