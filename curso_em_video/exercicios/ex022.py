# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiscúlas
# O nome com todas as letras minusculas
# Quantas letras possui, sem considerar espaços
# Quantas letras possui o primeiro nome

# Pede o nome completo do usuário
nome = str(input('Digite seu nome completo: '))

# Realiza as transformações no nome
maiusculas = nome.upper()
minusculas = nome.lower()
total = len(nome.replace(" ",""))
divide_nome = nome.split()
primeiro_nome = len(divide_nome[0])

# Exibe as transformações ao usuário
print(f'Somente em maiusculas: {maiusculas} \n'
      f'Somente em minusculas: {minusculas} \n'
      f'Total de caracteres do primeiro nome ({divide_nome[0]}): {primeiro_nome} \n'
      f'Total de caracteres sem espaços: {total}')
