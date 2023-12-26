"""Desenvolva um programa que leia o primeiro termo e a razão de uma
PA. No final, mostre os 10 primeiros termos dessa progressão."""
primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiroTermo + (10 - 1) * razao
for i in range(primeiroTermo, decimo + razao, razao):
    print(i, end=" ")