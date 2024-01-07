"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
feminino = 0
masculino = 0
maior = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [F/M]: ")).upper().strip()[0]

    if sexo == "F":
        if idade > 18:
            maior += 1
            if idade < 20:
                feminino +=1

        elif idade < 18:
            feminino += 1

    elif sexo == "M":
        masculino += 1
        if idade > 18:
            maior += 1

    r = " "
    while r not in "SN":
        r = str(input("Quer continuar[S/N]? ")).upper().strip()[0]
    if r == "N":
        break

print(f"{maior} pessoas tem mais de 18 anos.")
print(f"{masculino} homens foram cadastrados.")
print(f"{feminino} mulheres tem menos de 20 anos.")
