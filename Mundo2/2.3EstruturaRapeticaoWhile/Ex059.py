"""Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""
sair = False
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
while not sair:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print()
    escolha = int(input("O que você deseja fazer com os dois números digitados: "))
    if escolha == 1:
        r = n1 + n2
        print(f"A soma entre {n1} e {n2} é {r}")
    elif escolha == 2:
        r = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é {r}")
    elif escolha == 3:
        if n1 > n2:
            r = n1
            print(f"O maior número é {r}.")
        elif n2 > n1:
            r = n2
            print(f"O maior número é {r}.")
        else:
            print("Os dois números são iguais.")
    elif escolha == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        continue
    elif escolha == 5:
        sair = True
    else:
        print("Opção inválida! Tente novamente.")

