"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
pc = randint(1, 3)
if pc == 1:
    escolhaPc = "Pedra"
elif pc == 2:
    escolhaPc = "Papel"
else:
    escolhaPc = "Tesoura"

print('''Suas opções
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input("Digite a sua opção: "))

if opcao == 1:
    escolhaUsuario = "Pedra"
elif opcao == 2:
    escolhaUsuario = "Papel"
elif opcao == 3:
    escolhaUsuario = "Tesoura"
else:
    print("Opção inválida!")

print(f"O computador escolheu {escolhaPc} e vc escolheu {escolhaUsuario}.")

if escolhaUsuario == "Pedra" and escolhaPc == "Pedra":
    print("EMPATE")
elif escolhaUsuario == "Pedra" and escolhaPc == "Papel":
    print(f"{escolhaUsuario} perde de {escolhaPc}! Você PERDEU!")
elif escolhaUsuario == "Pedra" and escolhaPc == "Tesoura!":
    print(f"{escolhaUsuario} ganha de  {escolhaPc}! Você ganhou!")
elif escolhaUsuario == "Papel" and escolhaPc == "Pedra":
    print(f"{escolhaUsuario} ganha de  {escolhaPc}! Você ganhou!")
elif escolhaUsuario == "Papel" and escolhaPc == "Papel":
    print("EMPATE")
elif escolhaUsuario == "Papel" and escolhaPc == "Tesoura":
    print(f"{escolhaUsuario} perde de {escolhaPc}! Você PERDEU!")
elif escolhaUsuario == "Tesoura" and escolhaPc == "Pedra":
    print(f"{escolhaUsuario} perde de {escolhaPc}! Você PERDEU!")
elif escolhaUsuario == "Tesoura" and escolhaPc == "Papel":
    print(f"{escolhaUsuario} ganha de  {escolhaPc}! Você ganhou!")
elif escolhaUsuario == "Tesoura" and escolhaPc == "Tesoura":
    print("EMPATE")

