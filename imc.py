# Programa para cálculo de IMC (Índice de Massa Corporal)
# Desenvolvido para a aula prática utilizando Python no Google Cloud Shell Editor

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Entrada de dados pelo usuário
print("Bem-vindo ao Calculador de IMC!")
peso = float(input("Digite seu peso em kg (exemplo: 70.5): "))
altura = float(input("Digite sua altura em metros (exemplo: 1.75): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Classificação do IMC
classificacao = classificar_imc(imc)

# Exibição dos resultados
print("\nResultados:")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")