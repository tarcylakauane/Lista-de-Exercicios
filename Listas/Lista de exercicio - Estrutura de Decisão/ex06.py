#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = int(input("Informe um valor: "))
valor2 = int(input("Informe outro valor: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

print("Os valores em ordem crescente são:", valor1, valor2)