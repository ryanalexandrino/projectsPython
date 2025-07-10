# Crie um programa que leia um número Real qualquer e mostre sua proporção inteira

# Importa o mpodulo de matemática
import math

# Pede o número ao usuário
numero = float(input('Digite um número real: '))

# Arredonda o número para baixo com o metodo ceil e para cima com metodo floor e o exibe
print(f'O número digitado ({numero}) pode ser arredondado: \n'
      f'Para cima: {math.ceil(numero)} \n'
      f'Pata baixo: {math.floor(numero)}')