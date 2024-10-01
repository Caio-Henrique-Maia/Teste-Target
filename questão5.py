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
