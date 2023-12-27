"""Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo."""
c = 0
n = int(input("Digite um número: "))
for i in range(1, n +1):
    if n % i == 0:
        print(i, end=" ")
        c += 1
print()
print(f"{n} foi divisível {c} vezes.")
if c == 2:
    print("É um número primo.")
else:
    print("Não é um número primo.")