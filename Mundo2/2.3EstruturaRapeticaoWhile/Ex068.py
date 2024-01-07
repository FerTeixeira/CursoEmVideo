"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o
total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
pc = randint(0, 10)
c = 0
while True:
    usuario = int(input("Digite um número de 0 a 10: "))
    s = pc + usuario
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou Impar: ")).upper().strip()[0]
        print(f"Você jogou {usuario} e o computador jogou {pc}. Total de {s}.")
        print("PAR" if s % 2 == 0 else "IMPAR")
    if escolha == "P" and s % 2 == 0:
        print("Você ganhou!!")
        c += 1
    elif escolha == "I" and s % 2 != 0:
        print("Você ganhou!!")
        c += 1
    else:
        print("Você perdeu!!")
        break
print(f"Você venceu {c} vezes")
