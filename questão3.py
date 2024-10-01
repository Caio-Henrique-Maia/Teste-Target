import json

def ler_dados_json(caminho_arquivo):
    # Lê os dados do arquivo JSON
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def processar_dados(dados):
    # Filtra os dias com valor maior que zero para os cálculos
    valores_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

    # Calcula o total e a média dos valores
    total = sum(valores_validos)
    dias_com_valor = len(valores_validos)
    media = total / dias_com_valor if dias_com_valor > 0 else 0

    # Encontra o maior e o menor valor
    maior_valor = max(valores_validos)
    menor_valor = min(valores_validos)

    # Contabiliza os dias em que o valor foi superior à média
    dias_superiores_media = len([valor for valor in valores_validos if valor > media])

    # Exibe os resultados
    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias com faturamento superior à média: {dias_superiores_media}")

# Caminho do arquivo JSON
caminho_do_arquivo = 'dados.json'

# Lê os dados e processa
dados = ler_dados_json(caminho_do_arquivo)
processar_dados(dados)
