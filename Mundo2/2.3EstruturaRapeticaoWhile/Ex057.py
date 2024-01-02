"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até
ter um valor correto."""
r = ""
while True:
    r = str(input("Informe o seu sexo [M/F]: ")).upper()[0].strip()
    if r in "MF":
        if r == 'M':
            sexo = "MASCULINO"
        else:
            sexo = "FEMININO"
        print(f"Sexo {sexo} registrado com sucesso")
        break
    else:
        print("Dados inválidos")
