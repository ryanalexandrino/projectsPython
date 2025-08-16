# Faça um programa que mostre a tabuada de vários números um de cada vez
# O programa deve ser interrompido quando um valor negativo for digitado

# Laço while infinito com condição de parada de número negativo
while True:
    numero = int(input('\nDigite um número inteiro: '))
    if numero >= 0:
        print(f'A tabuada do número digitado é..')
        for c in range (1, 11):
            print(f'{numero} x {c} : {numero * c}')
    else:
        break

# Exibe a saída do laço ao usuário
print('Você digitou um número negativo, interrompendo o programa!')