# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

# Define as variáveis globais
soma_idades = 0
maior_idade = 0
mais_velho = str
mulheres_menores = 0

# Cria o laço que lê o nome das pessoas e realiza os testes solicitados
for c in range(0,4):
    nome = str(input('\nQual o seu nome? ')).strip()
    idade = int(input('Quantos anos você têm? '))
    sexo = str(input('Você é homem ou mulher? \n'
                     '[H] Homem \n'
                     '[M] Mulher \n'
                     'Digite a opção: ')).upper().strip()

    # Soma todas as idades
    soma_idades += idade

    # Verifica qual o homem mais velho
    if c == 0 and sexo == 'M':
        maior_idade = idade
        mais_velho = nome

    if sexo == 'H' and idade > maior_idade:
        maior_idade = idade
        mais_velho = nome

    # Verifica quais mulheres são menores de 20
    if sexo == 'M' and idade < 20:
        mulheres_menores += 1

# Exibe os resultados ao usuário
print(f'\nÉ possível extrair as seguintes informações das pessoas inseridas: \n'
      f'1. A média das idades inseridas é {soma_idades/4}! \n'
      f'2. O homem mais velho é o {mais_velho}, com {maior_idade} anos! \n'
      f'3. Da relação, apenas {mulheres_menores} mulheres são menores de 20 anos!')