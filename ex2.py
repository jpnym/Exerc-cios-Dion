# Solicitar os dois números e o operador ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Verificar e realizar a operação correspondente
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    # Verificar se o segundo número não é zero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operador inválido!"

# Exibir o resultado
print(f"O resultado da operação é: {resultado}")
