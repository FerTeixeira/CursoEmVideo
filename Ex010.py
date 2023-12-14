""""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""
dinheiro = float(input("Quanto dinheiro você tem na carteira: R$ "))
dolar = dinheiro / 4.91
print(f"Com {dinheiro} reais você pode comprar {dolar:.2f} dolares")