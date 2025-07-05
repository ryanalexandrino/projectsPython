#Desenvolva um programa que leia as duas notas de uma aluno, calcule sua média
#Pede as notas ao usuário
aluno = str(input('Qual o nome do aluno? '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
#Calcula e exibe o resultado ao usuário
print(f'A médias das notas do(a) {aluno} é igual a: {(nota1+nota2)/2:.1f}')