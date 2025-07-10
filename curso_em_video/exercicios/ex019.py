# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido aleatoriamente

# Importa o módulo random
import random

# Lê os nomes dos alunos
aluno_1 = str(input('Digite o nome do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro alunp: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))

# Cria uma lista com os alunos
lista = [aluno_1,aluno_2,aluno_3,aluno_4]

# Randomiza a escolha do aluno com o método choice
aluno_escolhido = random.choice(lista)

# Exibe o aluno escolhido aleatoriamente
print(f'O aluno sorteado para apagar o quadro foi o {aluno_escolhido}!')
