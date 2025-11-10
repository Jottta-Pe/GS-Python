import csv

dados = []

with open("Book1.csv", newliw ='', encoding='utf-8') as f:
    leitor = csv.reder(f)
    for linha in leitor:
        dados.append(linha)
print(dados)