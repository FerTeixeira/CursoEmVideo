"""Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder
30% do salário ou então o empréstimo será negado."""

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = float(input("Digite em quantos anos você quer pagar a casa: "))
meses = anos * 12
prestacao = casa / meses
print(f"Para pagar uma casa de R${casa} em {anos} anos a prestação será de"
      f"R${prestacao:.2f}")
if prestacao >= salario * (30/100):
    print("Empréstimo NEGADO!!")
else:
    print("Emoréstimo pode ser CONCEDIDO!")
