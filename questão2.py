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
