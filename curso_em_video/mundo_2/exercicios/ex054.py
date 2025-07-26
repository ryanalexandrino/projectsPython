# Crie um programa que leia o ano de nascimento de sete pessoas
# Mostre quantas pessoas já atingiram a maioridade e quantas não atingiram

# Importa o módulo de datetime, função datetime
from datetime import date

# Define as variáveis globais
maiores = 0
menores = 0

# Cria um laço de repetição que lê as idades e testa a maioridade
for c in range(1,8):
    ano_nascimento = int(input(f'{c}. Digite o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano_nascimento
    if  idade >= 21:
        maiores+=1
    else:
        menores+=1

# Exibe quantas pessoas são maiores, quantas são menores
print(f'\nCom base nas idades digitadas anteriormente, podemos concluir que: \n'
      f'Menores: {menores} \n'
      f'Maiores: {maiores}')