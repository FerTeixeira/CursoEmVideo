"""Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint

lista = []
jogos = []
q = int(input("Digite quantos jogos você quer que eu sorteie: "))
t = 1
while t <= q:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            c +=1
        if c == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    t += 1

for i, l in enumerate(jogos):
    print(f"Jogo {i + 1}: {l}")


