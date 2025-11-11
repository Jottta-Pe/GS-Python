import csv
from pprint import pprint

dados = []
arquivo = "Book1.csv"
arquivo = "teste1.csv"

with open(arquivo, newline ='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        dados.append(linha)
pprint(dados)
