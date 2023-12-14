""""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

metros = float(input("Digite uma distância em metros: "))
quilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10
decimetro = metros * 10
centimetro = metros * 100
milimetro = metros * 1000
print(f"A medida de {metros}m corresponde a {centimetro:.0f}cm e {milimetro:.0f}mm")

