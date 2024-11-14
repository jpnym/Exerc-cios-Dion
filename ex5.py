# Solicitar o número de clientes em A e B
num_clientes_A = int(input("Quantos clientes estão em A? "))
clientes_A = set()
for i in range(num_clientes_A):
    cliente = input(f"Digite o cliente {i+1} de A: ")
    clientes_A.add(cliente)

num_clientes_B = int(input("Quantos clientes estão em B? "))
clientes_B = set()
for i in range(num_clientes_B):
    cliente = input(f"Digite o cliente {i+1} de B: ")
    clientes_B.add(cliente)

# Identificar os clientes que estão em ambos os conjuntos
clientes_comum = clientes_A.intersection(clientes_B)
print("Clientes em ambos os conjuntos:", clientes_comum)

# Identificar os clientes que estão apenas em clientes_A
clientes_apenas_A = clientes_A - clientes_B
print("Clientes apenas em A:", clientes_apenas_A)

# Identificar os clientes que estão em apenas um dos conjuntos (exclusivos)
clientes_exclusivos = clientes_A.symmetric_difference(clientes_B)
print("Clientes exclusivos (em apenas um dos conjuntos):", clientes_exclusivos)

# Calcular a porcentagem de clientes únicos
clientes_unicos = len(clientes_exclusivos)
total_clientes = len(clientes_A.union(clientes_B))
porcentagem_unicos = (clientes_unicos / total_clientes) * 100
print(f"Porcentagem de clientes únicos: {porcentagem_unicos:.2f}%")
