# Melhore o desafio 061 perguntando se o usuário quer que seja mostrado mais termos
# O programa encerra quando o usuário digitar 0 (termos)

# Inicia as variáveis globais
novos_termos = 10
opcao = 0
contador = 1
total = 0

# Lê o primeiro termo e a razão da PA
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
t = a1
print('Com base nos valores inseridos, os 10 primeros termos são:')

# Cria o laço do programa
while novos_termos != 0:
    # Calcula a progressão com base nos termos inseridos usando o while
    total += novos_termos
    while contador <= total:
        print(f'{t} → ', end='')
        t += r
        contador += 1
    print('FIM!\n')

    opcao = int(input('O que você deseja fazer agora? \n'
                          '[1] Digitar mais termos \n'
                          '[0] Sair do programa \n'
                          'Digite a opção desejada: '))

    if opcao == 1:
        novos_termos = int(input('\nDigite a quantidade de termos: '))
        print('O resultado dos termos adicionados é:')
    else:
        print('\nPrograma encerrado!')
        novos_termos = 0

# Exibe quantos termos foram calculados e exibidos:
print(f'Ao todo, foram exibidos {total} termos nessa progressão!')
