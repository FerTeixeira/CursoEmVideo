"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário se
ele quer ou não continuar a digitar valores."""
r = ''
s = c =0
while r != 'N':
    n = int(input("Digite um número: "))
    s += n
    c += 1
    r = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"Você digitou {c} números e a média foi {s/c:.2f}")
print(f"O maior valor foi {maior} e o menor {menor}")
