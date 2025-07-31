# Melhore o jogo do desafio 028, onde a máquina vai determinar um número aleatório entre 0 e 10
# O jogador precisa acertar qual o número
# Mostrando ao final quantos palpites foram necessários para ele acertar

# Importa o módulo Random
import random
import time

# Inicializa as variávris globais
escolha = -1
contador = 1

# Define o número aleatório da máquina
numero = int(random.randint(0, 10))
print('O computador acaba de definir un número de 0 a 10..')

# Cria a estrutura de repetição que contêm o jogo
while numero != escolha:

    # Pede o número ao usuário
    escolha = int(input('Qual número o computador pensou? '))
    contador += 1

    # Cria um timer para simular um processamento da máquina
    print('\nPROCESSANDO...')
    time.sleep(2)

    # Cria a condicional que retorna o resultado da partida
    if escolha < numero:
        print('Quase! \n'
              'O número que a máquina escolheu é maior!\n'
              'Tente novamente!')
    elif escolha > numero:
        print('Quase! \n'
              'O número que a máquina escolheu é menor! \n'
              'Tente novamente!')
    else:
        print('Você acertou o número! \n'
              f'A máquina havia definido o número {numero}')

# Exibe ao usuário quantas tentativas foram necessárias para adivinhar o número
print(f'Foram necessárias {contador} tentativas para adivinhar o número!')
