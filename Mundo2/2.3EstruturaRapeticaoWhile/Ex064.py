"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag)."""
n = 0
c = 1
s = 0
print("Digite números para somar e quando quiser parar digite 999.")
while n != 999:
    n = int(input(f"Digite o número {c}: "))
    if n != 999:
        c += 1
        s += n
print(f"Você digitou {c - 1} números e a soma de todos é {s}")
