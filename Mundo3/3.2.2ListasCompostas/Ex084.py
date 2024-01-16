"""Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
lista = []
aux = []
p = 0
maior = menor = 0
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    aux.append(nome)
    p +=1
    aux.append(peso)
    if len(lista) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]
    lista.append(aux[:])
    aux.clear()
    r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if r == "N":
        break

print(f"{p} pessoas foram cadastradas.")
print(f"O maior peso foi {maior}kg. Peso de ", end="")
for p in lista:
    if p[1] == maior:
        print(f"{p[0]} ", end="")

print(f"O menor peso foi {menor}kg. Peso de ", end="")
for p in lista:
    if p[1] == menor:
        print(f"{p[0]} ", end="")

