# Solicitar o número N ao usuário
N = int(input("Digite um número inteiro N: "))

# Verificar e imprimir os números primos entre 1 e N
print(f"Os números primos entre 1 e {N} são:")
for num in range(2, N + 1):  # Começa de 2 porque 1 não é primo
    primo = True  # Assumir que o número é primo
    for i in range(2, num):  # Verifica se num é divisível por algum número de 2 até num-1
        if num % i == 0:
            primo = False  # Se for divisível, não é primo
            break  # Não precisa verificar mais divisores
    if primo:
        print(num, end=" ")  # Imprimir o número se for primo
