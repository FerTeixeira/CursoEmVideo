"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""
nome = str(input("Disgite seu nome completo: ")).strip()
nomeCompleto = nome.split()
print(f"Primeiro nome: {nomeCompleto[0]}")
print(f"Último nome: {nomeCompleto[len(nomeCompleto) -1 ]}")

