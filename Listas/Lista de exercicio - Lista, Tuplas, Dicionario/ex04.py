#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
#com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idades = []
alturas = []

for i in range(30):
    idade = int(input(f'Digite a idade do aluno {i+1}: '))
    altura = float(input(f'Digite a altura do aluno {i+1}: '))

    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
alunos_inferior_media = sum(1 for altura in alturas if altura < media_altura and idades[alturas.index(altura)] > 13)

print(f"Número de alunos com mais de 13 anos e altura inferior à média {alunos_inferior_media}")