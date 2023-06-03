#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',senão escrever a mensagem 'Saldo Negativo'.

num_conta = float(input("Informe o número da sua conta: "))
saldo = float(input("Informe o saldo da sua conta: "))
debito = float(input("Informe o valor do debito: "))
credito = float(input("Informe o valor do credito: "))

saldo_atual = saldo-debito+credito 

if saldo_atual>=0:
    print("Saldo positivo")
else: 
    print("Saldo negativo")    