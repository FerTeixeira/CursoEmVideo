"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""
salario = float(input("Digite o salário do funcionário: R$"))
if salario >= 1250:
    aumento = salario + (salario * (10/100))
    print(f"O salário de R${salario:.2f} com aumento de 10% é {aumento}.")
else:
    aumento = salario + (salario * (15/100))
    print(f"O salário de R${salario:.2f} com aumento de 15% é {aumento}.")