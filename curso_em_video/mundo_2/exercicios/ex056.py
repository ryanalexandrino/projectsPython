# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

# Define as váriaveis globais
soma_idade = 0
mais_velho = str
maior_idade = 0
mulheres_maiores = 0

# Cria o laço que lê o nome das pessoas e realiza os cálculos solicitados
for c in range(1,5):
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Quantos anos você têm? '))
    sexo = int(input('Você é homem ou mulher? \n'
                     '[1] Homem \n'
                     '[2] Mulher \n'
                     'Digite a opção: '))
    
