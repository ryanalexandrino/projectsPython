# Melhore o jogo do desafio 028, onde a máquina vai determinar um número aleatório entre 0 e 10
# O jogador precisa acertar qual o número
# Mostrando ao final quantos palpites foram necessários para ele acertar

# Importa o módulo Random
import random
import time

# Define "numero" e "escolha" como variáveis globais
numero = 0
escolha = 1
contador = 1

# Cria a estrutura de repetição que contêm o jogo
while numero != escolha:
    # Define o número aleatório da máquina
    numero = int(random.randint(0, 10))

    # Pede o número ao usuário
    escolha = int(input(f'O computador acaba de definir un número de 0 a 10.. \n'
                        f'Qual número o computador pensou? '))

    # Cria um timer para simular um processamento da máquina
    print('PROCESSANDO...')
    time.sleep(2)

    # Cria a condicional que retorna o resultado da partida
    if escolha != numero:
        print('Você errou!')
        print(f'O número pensado pelo computador foi: {numero} \n'
              f'O número escolhido pelo usuário foi: {escolha} \n'
              f'\nVamos tentar novamente!')
        contador += 1
    else:
        print('\nVocê acertou o número! \n')

# Exibe ao usuário quantas tentativas foram necessárias para adivinhar o número
print(f'Foram necessárias {contador} tentativas para adivinhar o número!')
