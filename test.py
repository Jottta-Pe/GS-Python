import csv
from pprint import pprint

arquivo = r"C:\Users\Usuário\OneDrive\Área de Trabalho\VSCode-Jean\Python\GS-Python\teste2.csv"

dados = []

def limpar_valor(valor):
    if not valor or valor.strip() == '':
        return None
    valor = valor.strip()
    valor = valor.replace('.', '').replace(',', '.').replace('%', '')
    try:
        return float(valor)
    except:
        return valor

with open(arquivo, newline='', encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        if not linha['Localizacao'].strip():
            continue
        for chave in linha:
            linha[chave] = limpar_valor(linha[chave])
        dados.append(linha)

dados_paises = {}
for linha in dados:
    pais = linha["Localizacao"]
    dados_paises[pais] = linha

def apresenta_dado(nome_dado):
    print("\n===", nome_dado, "por pais ===")
    for pais, info in dados_paises.items():
        if nome_dado in info and isinstance(info[nome_dado], (int, float)):
            print(pais, ":", info[nome_dado])
        else:
            print(pais, ": dado nao disponivel")

def apresenta_pais(nome_pais):
    print("\n=== Dados de", nome_pais, "===")
    print(dados_paises.get(nome_pais, "Pais nao encontrado"))

def media_dado(nome_dado):
    valores = []
    for info in dados_paises.values():
        if isinstance(info.get(nome_dado), (int, float)):
            valores.append(info[nome_dado])
    if valores:
        return sum(valores) / len(valores)
    return None

def variancia_dado(nome_dado):
    valores = []
    for info in dados_paises.values():
        if isinstance(info.get(nome_dado), (int, float)):
            valores.append(info[nome_dado])
    if len(valores) < 2:
        return None
    media = sum(valores) / len(valores)
    soma = 0
    for v in valores:
        soma += (v - media) ** 2
    return soma / (len(valores) - 1)

def maior_valor(nome_dado):
    maior_pais = None
    maior_valor = float('-inf')
    for pais, info in dados_paises.items():
        valor = info.get(nome_dado)
        if isinstance(valor, (int, float)) and valor > maior_valor:
            maior_valor = valor
            maior_pais = pais
    return maior_pais, maior_valor

while True:
    print("\n=== MENU ===")
    print("1 - Apresentar um dado por pais")
    print("2 - Apresentar um pais todos os dados")
    print("3 - Calcular media de um dado")
    print("4 - Calcular variancia de um dado")
    print("5 - Ver pais com maior valor")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "0":
        print("Saindo... ate mais!")
        break
    elif opcao == "1":
        nome_dado = input("Digite o nome do dado: ").strip()
        apresenta_dado(nome_dado)
    elif opcao == "2":
        nome_pais = input("Digite o nome do pais: ").strip()
        apresenta_pais(nome_pais)
    elif opcao == "3":
        nome_dado = input("Digite o nome do dado: ").strip()
        m = media_dado(nome_dado)
        if m is not None:
            print("Media de", nome_dado, ":", round(m,2))
        else:
            print("Nao foi possivel calcular a media")
    elif opcao == "4":
        nome_dado = input("Digite o nome do dado: ").strip()
        v = variancia_dado(nome_dado)
        if v is not None:
            print("Variancia de", nome_dado, ":", round(v,2))
        else:
            print("Nao foi possivel calcular a variancia")
    elif opcao == "5":
        nome_dado = input("Digite o nome do dado: ").strip()
        pais, valor = maior_valor(nome_dado)
        print("O pais com o maior valor de", nome_dado, "e", pais, "com", round(valor,2))
    else:
        print("Opcao invalida! Tente novamente")
