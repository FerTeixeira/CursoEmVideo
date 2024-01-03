n = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
for i in range (n, 0, -1):
    fatorial *= i
    print(f"{i}", end=" ")
    print(' x ' if i > 1 else ' = ', end=" ")
print(fatorial)

