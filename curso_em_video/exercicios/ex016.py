#Crie um programa que leia um número Real qualquer e mostre sua proporção inteira
#Importa a biblioteca de matemática
import math
#Pede o número ao usuário
numero = float(input('Digite um número real: '))
#Converte e exibe o número
print(f'O número digitado pode ser arredondado: \n'
      f'Para cima: {math.ceil(numero)} \n'
      f'Pata baixo: {math.floor(numero)}')