"""Elabore um programa que calcule o valor a ser pago por um
 produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
produto = float(input("Digite o valor do produto: R$"))
print('''FORMAS DE PAGAMENTO: 
      [ 1 ] À vista dinheito/cheque.
      [ 2 ] À vista no cartão.
      [ 3 ] Em até 2x no cartão.
      [ 4 ] 3x ou mais no cartão.''')
escolha = int(input("Escolha a forma de pagamento: "))
if escolha == 1:
    valor = produto - (produto * (10/100))
    print(f"O produto vai custar RS{valor:.2f}")
elif escolha == 2:
    valor = produto - (produto * (5/100))
    print(f"O produto vai custar RS{valor:.2f}")
elif escolha == 3:
    valor = produto
    parcelas = 2
    print(f'Parcelas: {parcelas}x de {valor / parcelas :.2f}')
    print(f'O produto vai custar RS{valor:.2f}')
elif escolha == 4:
    valor = produto + (produto * (20/100))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    if parcelas == 1:
        print(f"O produto vai custar RS{valor:.2f}")
    elif parcelas == 2:
        print(f'Parcelas: {parcelas}x de {valor / parcelas :.2f}'
              f'O produto vai custar RS{valor:.2f}')
    elif parcelas == 3:
        print(f'Parcelas: {parcelas}x de {valor / parcelas :.2f}'
              f'O produto vai custar RS{valor:.2f}')
    elif parcelas >= 4:
        print(f'Parcelas: {parcelas}x de {valor / parcelas :.2f}')
        print(f'O produto vai custar RS{valor:.2f}.')
else:
    print("Escolha indisponível.")



