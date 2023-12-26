"""Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o."""
s = 0
for i in range(0, 6):
    n = int(input(f"Digite o número {i + 1}: "))
    if n % 2 == 0:
        s = s + n
print(f"A soma dos números pares é: {s}")

