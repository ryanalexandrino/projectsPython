# Faça um programa que leia um ano e diga se ele é bissexto

# Lê o ano do usuário
ano = int(input('Digite um ano: '))

# Verifica se ele é bissexto
if ano %4 == 0 and ano %100 != 0:
    print('O ano digitado é bissexto!')
else:
    print('O ano digitado não é bissexto!')
