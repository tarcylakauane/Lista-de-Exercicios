#Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
#pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número
#favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.

numeros = {
    'Gabriel': 7,
    'Gisele': 6,
    'Guilherme': 1,
    'Lucas': 3,
    'Pricilla': 7
}

print('numeros:')
for pessoa, numero in numeros.items():
    print(pessoa + ":", numero)