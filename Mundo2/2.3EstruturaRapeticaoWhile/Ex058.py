"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
pc = randint(1, 10)
print("Acabei de pensar em um número entre 0 e 10. Tente adivinhar\n"
                     "qual número eu escolhi.")
cont = usuario =0

acertou = False
while not acertou:
    cont += 1
    usuario = int(input("Digite o seu palpite: "))
    if pc > usuario:
        print("Mais... tente mais uma vez")
    elif pc < usuario:
        print("Menos...  tente mais uma vez")
    else:
        acertou = True
if cont == 1:
    print("Você acertou na primeira tentativa")
else:
    print(f"Você acertou com {cont} tentativas")
