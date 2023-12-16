"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = str(input("Digite seu nome completo: ")).strip()
print(f"O nome {nome} com as letras MAIÚSCULAS é: {nome.upper()}.")
print(f"O nome {nome} com letras MINÚSCULAS é: {nome.lower()}.")
print(f"O nome {nome} tem {len(nome) - nome.count(' ')} letras.")
print(f"Seu primeiro nome tem {nome.find(' ')} lestras.")
