# Faça um programa que leia um número e mostre se ele é impar ou par

# Lê o número do usuário
numero = int(input('Digite um número: '))

# Analisa se ele é par ou impar através do resto, e exibe ao usuário
if numero %2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é impar!')