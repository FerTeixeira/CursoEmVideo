"""Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA."""
frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for i in range(len(junto) -1, -1, -1):
    inverso += junto[i]
print(f"O inverso de {junto} é {inverso}.")
if junto == inverso:
    print("Temos um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")
