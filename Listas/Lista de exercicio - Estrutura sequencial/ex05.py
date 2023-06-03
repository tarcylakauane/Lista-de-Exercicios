#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
#a temperatura em graus Celsius.

fah = float(input("Informe a temperatura em graus fahrenheit: "))

cel = 5 * ((fah-32) / 9)
print(f"A temperatura em graus Celsius é {cel}")