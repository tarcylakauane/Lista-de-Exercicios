#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    numero = int(input(f'Digite o número {i+1}: '))
    numeros.append(numero)

print(f"Números digitados: {numeros}")