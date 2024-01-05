"""Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo."""
while True:
    n = int(input("Digite um número para saber a tabuada: "))
    c = 1
    if n <= 0:
        break
    while c < 11:
        t = n * c
        print(f"{n} x {c} = {t}")
        c += 1
