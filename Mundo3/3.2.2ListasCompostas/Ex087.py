"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaTerC = 0
maiorSegL = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end="")
    print()

for l in range(0, 3):
    somaTerC += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maiorSegL = matriz[1][c]
    else:
        if matriz[1][c] > maiorSegL:
            maiorSegL = matriz[1][c]
print(f" O soma dos valores pares é {somaPares}.")
print(f"A soma dos valores da terceira coluna é {somaTerC}")
print(f"O maior valor da segunda linha é {maiorSegL}")
