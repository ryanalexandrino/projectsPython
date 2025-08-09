# Faça um programa que mostre a tabuada de vários números um de cada vez
# O programa deve ser interrompido quando um valor negativo for digitado

# Laço while infinito com condição de parada de número negativo
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero < 0:
        break
    else:
        print(f'A tabuada do número digitado é.. \n'
              f'{numero} x 1 : {numero * 1} \n'
              f'{numero} x 2 : {numero * 2} \n'
              f'{numero} x 3 : {numero * 3} \n'
              f'{numero} x 4 : {numero * 4} \n'
              f'{numero} x 5 : {numero * 5} \n'
              f'{numero} x 6 : {numero * 6} \n'
              f'{numero} x 7 : {numero * 7} \n'
              f'{numero} x 8 : {numero * 8} \n'
              f'{numero} x 9 : {numero * 9} \n'
              f'{numero} x 10: {numero * 10} \n'
              f'\nVamos lá, tente novamente!')

# Exibe a saída do laço ao usuário
print('Você digitou um número negativo, interrompendo o programa!')