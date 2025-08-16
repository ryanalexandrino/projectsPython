# Crie um programa que leia o nome e o preço de vários produtos
# O programa deve perguntar se o usuário quer continuar
# Ao final o programa deve mostrar:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000,00
# Qual o nome do produto mais barato

# Inicializa as variáveis globais
total = 0
produtos_caros = 0
mais_barato = 0
nome_barato = ''

# Laço while infinito com condição de parada de escolha do usuário
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    valor = float(input('Digite o valor desse produto: R$'))

    # Calcula o total da compra
    total += valor

    # Conta quantos produtos são mais caros que R$1000
    if valor > 1000:
        produtos_caros += 1

    # Verifica qual o produto mais barato e armazena o seu nome
    if mais_barato == 0:
        mais_barato = valor
        nome_barato = produto
    elif valor < mais_barato:
        mais_barato = valor
        nome_barato = produto

    # Lê a escolha do usuário e a valida
    escolha = str(input('Deseja adicionar mais produtos a compra? \n'
                        '[S] Sim! \n'
                        '[N] Não! \n'
                        'Digite a opção: ')).upper().strip()
    while escolha not in ['S', 'N']:
        print('Opção inválida! Tente novamente..')
        escolha = str(input('\nDeseja adicionar mais produtos a compra? \n'
                            '[S] Sim! \n'
                            '[N] Não! \n'
                            'Digite a opção: ')).upper().strip()

    # Quebra ou mantém o laço conforme a opção do usuário
    if escolha == 'N':
        break
    else:
        print('\nVamos adicionar mais produtos!')

# Exibe os resultados da compra ao usuário
# Total da compra
print('\nResumo da compra: \n'
      f'Total da compra: R${total:.2f}.')

# Realiza os testes lógicos para exibir o resultado conforme a quantidade de produtos
if produtos_caros == 0:
    print('Nenhum produto acima de R$1000,00 inserido na compra..')
elif produtos_caros == 1:
    print('Apenas 1 produto acima de R$1000,00 inserido na compra!')
else:
    print(f'Total de produtos acima de R$1000,00: {produtos_caros}')

# Produto mais barato
print(f'O produto mais barato inserido foi a(o) {nome_barato}, custando apenas R${mais_barato:.2f}!')
