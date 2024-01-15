"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
das três listas geradas."""
lista = []
par = []
impar = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)

    r =str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if r in "nN":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print()
print(f"Todos os números digitados {lista}")
print(f"Todos os números par {par}")
print(f"Todos os números ímpar {impar}")

