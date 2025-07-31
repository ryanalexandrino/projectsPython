# Crie um programa que leia vários números inteiros
# A cada número o programa pergunta se o usuário deseja continuar
# Ao final mostre a média dos números digitados, o maior e o menor

# Inicializa as variáveis globais
opcao = 1
maior = 0
menor = 0
soma = 0
contador = 0

while opcao != 0:

    # Lê o número do usuário
    numero = int(input('\nDigite um número: '))

    # Realiza o teste se o número para determinar maior e menor
    if contador == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    # Realiza os incrementos para o cálculo da média
    soma += numero
    contador += 1

    # Valida a resposta do usuário
    opcao = int(input('Deseja digitar mais números?\n'
                          '[1] Sim!\n'
                          '[0] Não..\n'
                          'Opção: '))

    # Realiza a validação através desse laço
    while opcao not in [0, 1]:
        print('Opção inválida! Tente novamente.')
        opcao = int(input('Deseja digitar mais números?\n'
                              '[1] Sim!\n'
                              '[0] Não..\n'
                              'Opção: '))

# Exibe o encerramento do laço ao usuário e os cálculos
if contador == 1:
    print('Você digitou apenas um número, impossibilitando comparações e cálculos..')
else:
    print(f'Programa encerrado! \n'
          f'Dos números digitados, podemos analisar: \n'
          f'1. O maior número: {maior} \n'
          f'2. O menor número: {menor} \n'
          f'3. A média dos números digitados: {soma/contador:.2f}')
