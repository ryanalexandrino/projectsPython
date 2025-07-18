# Crie um programa que leia duas notas de um aluno e calcule sua média
# Ele deve mostra as seguintes mensagens:
# Média abaixo de 5.0 - REPROVADO
# Média entre 5.0 e 6.9 - RECUPERAÇÃO
# Média de 7.0 ou superior - APROVADO

# Lê as duas notas do aluno:
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

# Calcula sua média
media = (nota_1 + nota_2) / 2

# Cria uma estrutura condicional que indica a situação do aluno
if media < 5:
    print(f'Sua média final foi de {media}! \n'
          f'Você está REPROVADO!')
elif media >= 5 and media < 7:
    print(f'Sua média final foi de {media}! \n'
          f'Você está em RECUPERAÇÃO!')
else:
    print(f'Sua média foi de de {media}! \n'
          f'Você está APROVADO!')

