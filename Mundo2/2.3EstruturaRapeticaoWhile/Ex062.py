primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
primeiro = primeiroTermo
r = 1
t = 0
r = 10
while r != 0:
    c = 0
    while c < r:
        print(f"{primeiro}", end=" ")
        primeiro += razao
        c += 1
        t += 1
    print()
    r = int(input("Quantos termos você quer mostrar a mais: "))
print(f"Progressão finalizada com {t} termos mostrados.")





