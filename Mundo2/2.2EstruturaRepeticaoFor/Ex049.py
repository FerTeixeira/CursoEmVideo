"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for."""
n = int(input("Digite um número pra saber a tabuada: "))
for i in range(1, 11):
    print(f"{i:2} x {n:2} = {n * i:2}")
