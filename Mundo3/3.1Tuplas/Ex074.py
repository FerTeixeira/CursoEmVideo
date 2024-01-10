""" Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla."""
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
for n in range(len(numeros)):
    print(f"{numeros[n]} ", end="")
    if n == 0:
        maior = menor = numeros[n]

    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print()
print(f"O maior número foi: {maior}")
print(f"O menor número foi: {menor}")
