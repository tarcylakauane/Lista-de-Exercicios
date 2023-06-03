#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
#cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
alunos_aprovados = 0

for i in range(10):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)

    media = sum(notas) / len(notas)

    if nota >= 7.0:
        alunos_aprovados += 1

print(f"Número de alunos com média maior ou igual a 7.0:', {alunos_aprovados}")