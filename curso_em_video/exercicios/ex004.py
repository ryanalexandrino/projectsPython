# Faça um programa que leia um número e mostre todos os seus detalhes

# Le o valor do usuário
valor = input('Digite algo..')
print('Vamos ver qual tipo de informação você digitou:')
print(type(valor))
print('Sendo assim..')

# Mostra as demais informações do valor digitado
print(f'Só tem espaços? {valor.isspace()}')
print(f'É numérico? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em letras maiúsculas? {valor.isupper()}')
print(f'Está em letras minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')