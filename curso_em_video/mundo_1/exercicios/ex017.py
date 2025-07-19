# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# Calcule e mostre o comprimento da hipotenusa

# Importa o módulo de matemática
import math

# Pede os catetos ao usuario:
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

# Calcula e exibe a hipotenusa através do método hypot
print(f'A hipotenusa dos valores digitados é: {math.hypot(oposto,adjacente):.2f}')
