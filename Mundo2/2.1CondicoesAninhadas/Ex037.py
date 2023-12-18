"""Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal."""
n = int(input("Digite um número: "))
print('''Escolha uma das bases para a conversão:
      [ 1 ] converter poara BINÁRIO"
      [ 2 ] converter para OCTAL"
      [ 3 ] converter para HEXADECIMAL''')
r = int(input("Sua opção: "))
if r == 1:
    print(f"{n} convertido para BINÁRIO é igual a {bin(n)[2:]}.")
elif r == 2:
    print(f"{n} convertido para OCTAL é igual a {oct(n)[2:]}.")
elif r == 3:
    print(f"{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}.")
else:
    print("Resposta inválida!")
