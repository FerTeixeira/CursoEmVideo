""""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""
salario = float(input("Digite o salário do funcionário: R$"))
reajuste = salario + (salario * (15/100))
print(f"O salário de R${salario:.2f} com reajuste de 15% é R${reajuste:.2f}")