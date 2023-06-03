#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ")

if sexo == "M".upper:
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F".upper:
    peso_ideal = (62.1 * altura) - 44.7

if peso_ideal:
    print(f"Seu peso ideal é {peso_ideal}")
