# Crie um programa que faça o computador jogar Jokempô com o usuário

# Importa o múdulos random e time
from random import randint
from time import sleep

# Apresenta o jogo
print('VAMOS JOGAR JOKENPÔ!')

# Lê a opção do usuário
print('Escolhe entre.. \n'
      '1 - Pedra! \n'
      '2 - Papel! \n'
      '3 - Tesoura!')
escolha_jogador = int(input('Digite sua escolha: '))

# Timer para anuncio da rodada
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

# Determina a escolha da máquina com randomização
escolha_maquina = randint(1,3)

# Determina o vencedor através de uma condicional aninhada:
# Se o usuário seleciona Pedra
if escolha_jogador == 1 and escolha_maquina == 2:
    print('Você selecionou Pedra! \n'
          'A máquina selecinou Papel! \n'
          'Papel enrola Pedra, a máquina venceu!')
elif escolha_jogador == 1 and escolha_maquina == 3:
    print('Você selecionou Pedra! \n'
          'A máquina selecinou Tesoura! \n'
          'Pedra quebra a Tesoura, você venceu!')
elif escolha_jogador == 1 and escolha_maquina == 1:
    print('Você selecionou Pedra! \n'
          'A máquina selecinou Pedra! \n'
          'Empatou!')

# Se o usuário seleciona Papel
elif escolha_jogador == 2 and escolha_maquina == 1:
    print('Você selecionou Papel! \n'
          'A máquina selecinou Pedra! \n'
          'Papel enrola Pedra, você venceu!')
elif escolha_jogador == 2 and escolha_maquina == 3:
    print('Você selecionou Papel! \n'
          'A máquina selecinou Tesoura! \n'
          'Tesoura corta Papel, a máquina venceu!')
elif escolha_jogador == 2 and escolha_maquina == 2:
    print('Você selecionou Papel! \n'
          'A máquina selecinou Papel! \n'
          'Empatou!')

# Se o usuário seleciona Tesoura
elif escolha_jogador == 3 and escolha_maquina == 1:
    print('Você selecionou Tesoura! \n'
          'A máquina selecinou Pedra! \n'
          'Pedra quebra a Tesoura, a máquina venceu!')
elif escolha_jogador == 3 and escolha_maquina == 2:
    print('Você selecionou Tesoura! \n'
          'A máquina selecinou Papel! \n'
          'Tesoura corta Papel, você venceu!')
elif escolha_jogador == 3 and escolha_maquina == 3:
    print('Você selecionou Tesoura! \n'
          'A máquina selecinou Tesura! \n'
          'Empatou!')
else:
    print('Opcão inválida. Tente novamente!')
