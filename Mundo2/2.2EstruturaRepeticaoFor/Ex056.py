"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos."""
maior = 0
cont = 0
somaIdade = 0
maisVelhor = ""
for i in range(1, 5):
    nome = str(input(f"Digite o nome da pessoa {i}: "))
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    sexo = str(input(f"Digite o sexo(F/M) da pessoa {i}: ")).upper()
    somaIdade = somaIdade + idade
    if sexo == "M":
        if idade > maior:
            maior = idade
            maisVelho = nome
    elif sexo == "F":
        if idade < 20:
            cont += 1

print()
print(f"A média de todas as idade é {somaIdade/4:.2f}.")
print(f"O homem mais velho é o {maisVelho} e tem {maior} anos.")
print(f"E tem {cont} mulheres com menos de 20 anos.")
