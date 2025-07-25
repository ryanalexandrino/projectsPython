# Faça um programa que leia un número inteiro e diga se ele é un número primo

# Declara as variáveis globais
contador = 0

# Lê o número do usuário
numero = int(input('Digite um número inteiro: '))

# Cria um laço for que conta quantas vezes o número é divísivel
for c in range(1, numero+1):
    if numero % c == 0:
        contador += 1

# Testa e exibe se o número é primo com base no contador
if contador == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo')