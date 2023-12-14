""""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""
largura = float(input("Digite a largura em metros da parede: "))
altura = float(input("Digite a altura em metros da parede: "))
area = largura * altura
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua area é de {area}m²")
tinta = area / 2
print(f"Para pintar esta parede de {area}m² você vai precisar de {tinta} litros de tinta")

