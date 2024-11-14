# Solicitar o peso e altura ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o IMC
print(f"O seu IMC é: {imc:.2f}")