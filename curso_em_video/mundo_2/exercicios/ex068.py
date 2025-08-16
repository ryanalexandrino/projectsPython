# Faça um programa que seja um jogo de par ou impar com a máquina
# O programa deve se encerrar quando o jogador perder
# Ao final, o programa deve exibir quantas vitórias consecutivas teve o jogador

# Importa o modulo random, função randint
from random import randint

# Inicializa variáveis globais
contador = 0

# Apresentação do jogo
print('Vamos jogar par ou impar!? \n')

# Laço while infinito com condição de parada em caso de derrota do jogador
while True:
    # Lê o número do jogador e válida esse número
    numero_jogador = int(input('Digite um número inteiro: '))

    # Define o número escolhido pela máquina
    numero_maquina = randint(1,10)

    # Soma o número do jogador com o da máquina
    soma = numero_jogador + numero_maquina

    # Lê a escolha do jogador e valida essa escolha
    escolha_jogador = str(input('Par ou Impar? \n'
                          '[I] Impar \n'
                          '[P] Par \n'
                          'Digite a opção: ')).upper().strip()
    while escolha_jogador not in ['P', 'I']:
        print('Escolha inválida, tente novamente!')
        escolha_jogador = str(input('Par ou Impar? \n'
                              '[I] Impar \n'
                              '[P] Par \n'
                              'Digite a opção: ')).upper().strip()

    # Realiza os testes lógicos para definir um vencedor
    if escolha_jogador == 'P' and soma % 2 == 0:
        print(f'O jogador escolheu {numero_jogador} e a máquina escolheu {numero_maquina} \n'
              f'A soma dos números escolhidos totaliza {soma}, que é par! \n'
              f'O jogador venceu!')
        contador += 1
    elif escolha_jogador == 'I' and soma % 2 != 0:
        print(f'O jogador escolheu {numero_jogador} e a máquina escolheu {numero_maquina} \n'
              f'A soma dos números escolhidos totaliza {soma}, que é impar! \n'
              f'O jogador venceu!')
        contador += 1
    elif escolha_jogador == 'P' and soma % 2 != 0:
        print(f'O jogador escolheu {numero_jogador} e a máquina escolheu {numero_maquina} \n'
              f'A soma dos números escolhidos totaliza {soma}, que é impar! \n'
              f'A máquina venceu!')
        break
    elif escolha_jogador == 'I' and soma % 2 == 0:
        print(f'O jogador escolheu {numero_jogador} e a máquina escolheu {numero_maquina} \n'
              f'A soma dos números escolhidos totaliza {soma}, que é par! \n'
              f'A máquina venceu!')
        break

# Exibe a quantidade de vitórias seguidas do jogador
if contador == 0:
    print('O jogador não venceu nenhuma vez..')
elif contador == 1:
    print('O jogador venceu apenas uma vez..')
else:
    print(f'O jogador venceu {contador} vezes seguidas!')
