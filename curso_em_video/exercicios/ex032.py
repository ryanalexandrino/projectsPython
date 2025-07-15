# Faça um programa que leia um ano e diga se ele é bissexto

# Importa o módulo datetime
from datetime import date

# Lê o ano do usuário
ano = int(input('Digite um ano, coloque 0 para inserir o ano atual: '))

# Condiciona a entrada "0" como ano atual
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto matematicamente
if ano %4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print('O ano digitado é bissexto!')
else:
    print('O ano digitado não é bissexto!')


