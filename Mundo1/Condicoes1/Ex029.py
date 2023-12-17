"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""
velocidade = float(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    velocidade = velocidade - 80
    print("Você ultrapassou o limite de velocidade que é 80km/h."
          f"Sua multa é de: R${velocidade * 7:.2f} reais.")
else:
    print("Tenha um bom dia e dirija com segurança!")