#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
 
maças = float(input("Informe o número de maças compradas: "))

if maças < 12:
    valor1 = maças*1.30 
    print(f"o valor total será {valor1}")     
elif maças >= 12:
    valor2 = maças*1
    print(f"O valor total será {valor2}")
