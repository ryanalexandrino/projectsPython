# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# Indo do 10 até o 0, com uma pausa de 1 segundo entre eles

# Importa o módulo time, função sleep e emonji
from time import sleep
import emoji

# Realiza a contagem regressica com um laço de repetição for
print('Contagem regressiva para o estouro dos fogos!')
for c in range(10, -1, -1):
    print(f'{c}!')
    sleep(1)
print(emoji.emojize("FIM! A contagem terminou! :fireworks: :rocket: :sparkles:"))
