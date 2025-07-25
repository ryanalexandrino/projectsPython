# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

# Define as variáveis globais
soma_idades = 0
maior_idade = 0
mais_velho = str
mulheres_menores = 0

# Cria o laço que lê o nome das pessoas e realiza os cálculos solicitados
for c in range(0,4):
    nome = str(input('\nQual o seu nome? '))
    idade = int(input('Quantos anos você têm? '))
    sexo = int(input('Você é homem ou mulher? \n'
                     '[1] Homem \n'
                     '[2] Mulher \n'
                     'Digite a opção: '))

    # Soma todas as idades
    soma_idades += idade

    # Verifica qual o homem mais velho
    if c == 0:
        maior_idade = idade

    if sexo == 1 and idade > maior_idade:
        mais_velho = nome

    # Verifica quais mulheres são menores de 20
    if sexo == 2 and idade < 20:
        mulheres_menores += 1

# Exibe os resultados ao usuário
print(f'É possível extrair as seguintes informações das pessoas inseridas: \n'
      f'1. A média das idades inseridas é {soma_idades/4}! \n'
      f'2. O homem mais velho é o {mais_velho}! \n'
      f'3. Da relação, {mulheres_menores} mulheres são menores de 20 anos!')