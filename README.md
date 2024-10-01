# Repositório criado com o intuito de avaliação de habilidades.
# O arquivo nomeado como "dados.json" foi baixado do link do e-mail que foi enviado para que pudesse ser feito o teste, nele contém as informações para responder a questão 3.
# Colocarei aqui os códigos e exemplos utilizados, assim como suas respostas.

1) Código: 
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1  
    soma += k

print(soma)

Resposta: 91


2) Código: 
def sequencia_fibonacci(n):
    sequencia_fib = [0, 1]  
    while True:
        proximo_fib = sequencia_fib[-1] + sequencia_fib[-2] 
        if proximo_fib > n:
            break
        sequencia_fib.append(proximo_fib)
    return sequencia_fib

def verificar_numero_fibonacci(n):
    sequencia_fib = sequencia_fibonacci(n)
    if n in sequencia_fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Solicita um número do usuário
num = int(input("Digite um número inteiro: "))
resultado = verificar_numero_fibonacci(num)
print(resultado)

Resposta: Digite um número inteiro: 55
O número 55 pertence à sequência de Fibonacci.

3)Código:
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


Resposta: 
Menor valor de faturamento: R$ 373.78
Maior valor de faturamento: R$ 48924.24
Número de dias com faturamento superior à média: 10

4)Código: 
#Valores informados pela questão:
faturamento = {
"SP":67836.43,
"RJ": 36678.66,
"MG": 29229.88,
"ES":27165.48,
"Outros": 19849.53,}

#Encontrando o total de faturamento
total = sum(faturamento.values())

print("Percentual de representação por estado")

#Cálculo para representação percentual de cada estado
for estado, valor in faturamento.items():
    percentual = (valor/total)*100
    print(f"{estado}: {percentual:.2f}%")

Resposta: 
Percentual de representação por estado
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 10.98%

5) Código: 
def inverter_string(string):
    # Declara string vazia para armazenar
    string_invertida = ""
    
    # Loop para ler a striung de trás para frente
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]  # Adiciona cada caractere à string invertida
    
    return string_invertida

# Solicita uma string do usuário
entrada = input("Digite uma string para inverter: ")

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")

Resposta:
Digite uma string para inverter: exemplo
String invertida: olpmexe
