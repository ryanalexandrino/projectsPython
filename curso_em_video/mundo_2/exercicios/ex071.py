# Crie um programa que simule um funcionamento de um caixa eletrônico
# No início pergunte ao usuário o valor a ser sacado (número inteiro)
# O programa vai informar quantas cédulas de cada valor serão entregues em notas de R$50, R$20, R$10 e R$1

# Laço while infinito com condição de parada de escolha do usuário
while True:
    valor_sacado = int(input('\nDigite o valor a ser sacado: '))
    valor_original = valor_sacado

    # Algoritmo de distribuição
    notas_50 = valor_sacado // 50
    valor_sacado %= 50

    notas_20 = valor_sacado // 20
    valor_sacado %= 20

    notas_10 = valor_sacado // 10
    valor_sacado %= 10

    notas_01 = valor_sacado

    # Resultados
    print(f'Para sacar R${valor_original}, você receberá:')
    print(f'Notas de R$50: {notas_50}')
    print(f'Notas de R$20: {notas_20}')
    print(f'Notas de R$10: {notas_10}')
    print(f'Notas de R$1: {notas_01}')

    # Pergunta se quer continuar
    print('Deseja fazer outro saque?')
    print('[S]')
    print('[N]')
    opcao = ''
    while opcao not in ['S', 'N']:
        opcao = str(input('Digite a opção: ')).upper()
        if opcao not in ['S', 'N']:
            print('Opção inválida! Tente novamente..')
    if opcao != 'S':
        break

# Mostra a saida do laço ao usuário
print('Muito obrigado por usar nosso caixa eletronico!')
