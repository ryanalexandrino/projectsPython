# Faça um programa que leia un número inteiro e diga se ele é un número primo

# Importa o módulo matemática, função sqrt
from math import sqrt

# Declara a varíavel primo como global
primo = bool

# Lê o número do usuário e calcula sua raiz quadrada
numero = int(input('Digite um número inteiro: '))
raiz = int(sqrt(numero))

# Cria um laço for que testa se o número é primo testando divisores até a sua raiz quadrada
for c in range(2, raiz+1):
    if numero % c == 0:
        primo = False

if primo:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo')