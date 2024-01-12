"""Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista. No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista."""
c = 1
lista = []


while c < 6:
    n = int(input(f"Digite o {c}º número: "))

    lista.append(n)
    c += 1
print(lista)
for i in range(len(lista)):
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]

        if lista[i] < menor:
            menor = lista[i]

print(f"O maior número é o {maior} e está na posição ", end="")
for c, i in enumerate(lista):
    if i == maior:
        print(c, end=" ")

print()

print(f"O menor número é o {menor} e está na posição ", end="")
for c, i in enumerate(lista):
    if i == menor:
        print(c, end=" ")
