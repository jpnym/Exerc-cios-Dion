# Solicitar o número N ao usuário
N = int(input("Digite um número inteiro N: "))
crescente = input("Deseja uma pirâmide crescente (sim ou não)? ")

# Gerar lista de números primos entre 1 e N
primos = []
for num in range(2, N + 1):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

# Imprimir a pirâmide de números primos
if crescente == "sim":
    for i in range(1, len(primos) + 1):
        # Imprimir a pirâmide com espaçamento para o formato
        print(" " * (len(primos) - i) + " ".join(str(primos[j]) for j in range(i)))
else:
    for i in range(len(primos), 0, -1):
        # Imprimir a pirâmide com espaçamento para o formato
        print(" " * (len(primos) - i) + " ".join(str(primos[j]) for j in range(i)))
