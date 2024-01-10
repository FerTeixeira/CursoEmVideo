"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

tabela = ("Palmeniras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "Bragantino",
          "Fluminense", "Atlético-PR", "Internacional", "Fortaleza", "São Paulo",
          "Cuiabá", "Corinthians", "Cruzeiro", "Vasgo da Gama", "Bahia", "Santos",
          "Goiás", "Coritiba", "América-MG")
print(f"Os 5 primeiros colocados são {tabela[0:5]}")
print(f"O 4 últimos colocados são {tabela[-4:]}")
print(f"Times em ordem alfabética: {sorted(tabela)}")
if "Chapecoense" in tabela:
    print(f"O Chapecoense está na {tabela.index('Chapecoense')+1} posição")
else:
    print("O Chapecoense não está entre os 20 primeiros do Campeonato")