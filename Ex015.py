""""Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado."""
km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite a quantidade de dias o carro foi alugado: "))
custo = (60 * dias) + (km * 0.15)
print(f"O valor do aluguel é R${custo:.2f}!")