""""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math
angulo = float(input("Digite a ângulo que você precisa: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem seno {seno:.2f}, "
      f"cosseno {cosseno:.2f} e "
      f"tangente {tangente:.2f}.")
