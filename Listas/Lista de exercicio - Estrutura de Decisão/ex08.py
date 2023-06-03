#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quant_atual = int(input("Informe a quantidade de produtos atual em estoque: "))
quant_max = int(input("Informe a quantidade máxima de produtos em estoque: "))
quant_min = int(input("Informe a quantidade mínima de produtos em estoque: "))

quant_media = (quant_max + quant_min)/2
print(f"{quant_media}")

if quant_atual>=quant_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")    