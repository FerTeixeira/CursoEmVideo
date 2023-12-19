"""Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo."""
from datetime import date
nasc = int(input("Digite o ano de nascimento: "))
idade = date.today().year - nasc
print(f"Você tem {idade} anos.", end=" ")
if idade == 18:
    print("Este é o ano do seu alistamento.")
elif idade < 18:
    print(f"Faltam {18 - idade} anos para o seu alistamento.")
else:
    print(f"O seu alistamento foi {idade - 18} anos atrás")
