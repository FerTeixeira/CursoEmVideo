""""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""

algo = input("Digite algo: ")

print(f"Qual o tipo primitivo de {algo}? {type(algo)}.")
print(f"{algo} é um número? {algo.isnumeric()}.")
print(f"{algo} é uma string? {algo.isalpha()}.")
print(f"{algo} é alfanumérico? {algo.isalnum()}.")
print(f"{algo} está escrito em maiúsculo? {algo.isupper()}.")
print(f"{algo} está escrito em minúsculo? {algo.islower()}.")
print(f"{algo} só tem espaços? {algo.isspace()}.")