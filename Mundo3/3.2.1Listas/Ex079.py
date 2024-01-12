"""Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""
lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Este valor já existe e não será adicionado novamente na lista")
    r = str(input("Quer continuar[S/N]? ")).strip().upper()[0]
    if r == "N":
        break
lista.sort()
print(lista)