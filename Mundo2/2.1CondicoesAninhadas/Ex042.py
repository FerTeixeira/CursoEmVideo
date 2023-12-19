"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

segmento1 = float(input("Digite o primeiro segmento: "))
segmento2 = float(input("Digite o segundo segmento: "))
segmento3 = float(input("Digite o terceiro segmento: "))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento2 + segmento1:
    print("É um triângulo ", end=' ')
    if segmento1 == segmento2 == segmento3:
        print("EQUILÁTERO.")

    elif segmento1 != segmento2 != segmento3 != segmento1:
        print("ESCALENO.")

    else:
        print("ISÓSCELES.")

else:
    print("Estes segmentos não formam um triângulo")
