# Escreva um programa que faça o computador definir um número de aleatório de 1 a 5
# Peça ppara usuário tentar descobrir qual é esse número
# O programa deve retornar se o usuário acertou ou não esse número

# Importa a biibiloteca Random
import random

# Define o número aleatório
numero = int(random.randint(1,5))

# Pede o número ao usuário
escolha = int(input(f'O computador acaba de definir un número de 1 a 5 \n'
                    f'Qual número o computador pensou? '))

# Cria a condicional para retorno da escolha do usuário
if escolha == numero:
    print('\nVocê acertou o número! \n')
else:
    print('\nVocê não acertou.. tente novamente! \n')
print(f'O número definido pelo computador foi: {numero} \n'
      f'O número escolhido pelo usuário foi: {escolha}')