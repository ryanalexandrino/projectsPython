# O mesmo professor do desafio passado quer sortear a ordem de apresentação de trabalho dos alunos
# Faça um programa que leia o nome de quatro alunos e os exiba numa ordem aleatória

# Importa o módulo random
import random

# Lê o nome dos alunos
aluno_1 = str(input('Digite o nome do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro alunp: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))

# Cria uma lista com os alunos
lista = str([aluno_1,aluno_2,aluno_3,aluno_4])

# Embaralha a ordem com o método sample
embaralhamento = random.sample(lista, 4)

# Exibe a ordem de apresentação de trabalhos de maneira aleatória
print(f'A ordem de apresentação dos trabalhos, ficou: \n'
      f'Primeiro trabalho - {embaralhamento[0]} \n'
      f'Segundo trabalho - {embaralhamento[1]} \n'
      f'Terceiro trabalho - {embaralhamento[2]} \n'
      f'Quarto trabalho - {embaralhamento[3]}')
