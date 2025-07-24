# Crie um programa que leia o ano de nascimento de sete pessoas
# Mostre quantas pessoas já atinjiram a maioridade e quantas não

# Importa o módulo de tempo
from datetime import datetime

# Define as variavéis globais
maiores = 0
menores = 0

# Cria um laço de repetição que lê as idades e testa a maioridade
for c in range(1,8):
    ano_nascimento = int(input(f'{c}. Digite o seu ano de nascimento: '))
    if datetime.now().year - ano_nascimento  > 18:
        maiores+=1
    else:
        menores+=1
print(f'Com base nas idades digitadas anteriormente, podemos concluir que: \n'
      f'Menores: {menores} \n'
      f'Maiores: {maiores}')