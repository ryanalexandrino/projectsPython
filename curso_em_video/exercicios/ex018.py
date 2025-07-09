#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

#Importa a biblioteca de matemática
import math

#Pede o angulo ao usuário e converte em radios
angulo = int(input('Digite um valor equivalente a um angulo: '))
radio = math.radians(angulo)

#Calcula os angulos solicitados
seno = math.sin(radio)
cosseno = math.cos(radio)
tangente = math.tan(radio)

#Exibe os angulos calculados ao usuário
print(f'Angulos calculados a partir do valor inserido: \n'
      f'Seno: {seno:.2f} \n'
      f'Cosseno: {cosseno:.2f} \n'
      f'Tangente: {tangente:.2f}')
