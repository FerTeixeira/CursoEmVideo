"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
c = 0
termo = primeiroTermo
while c < 10:
    print(f"{termo}", end=" ")
    termo += razao
    c += 1