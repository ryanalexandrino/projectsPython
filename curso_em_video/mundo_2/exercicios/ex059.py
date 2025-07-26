# Crie um programa que leia dois valores e mostre o menu:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# O programa deve funcionar em loop até o usuário optar por sair do programa

# Cria opção como uma variável global
opcao = 0

# Solicita os números ao usuário
numero_1 = int(input('Digite o primeiro número inteiro: '))
numero_2 = int(input('Digite o segundo número inteiro: '))

# Cria a estrutura de repetição que contêm o menu e realiza as operações
while opcao != 5:

    # Lê qual opção do menu o usuário deseja
    opcao = int(input('\nO que deseja fazer com esses números? \n'
                      '[1] Somar \n'
                      '[2] Multiplicar \n'
                      '[3] Maior \n'
                      '[4] Novos números \n'
                      '[5] Sair do programa \n'
                      'Digite a opção: '))

    # Cria uma condicional que realiza cada uma das ações do menu
    if opcao == 0 or opcao > 5:
        pass
    elif opcao == 1:
        print('\nOpção inválida! Tente novamente.')
        soma = numero_1 + numero_2
        print(f'\nA soma dos números é: {soma} \n')
    elif opcao == 2:
        produto = numero_1 * numero_2
        print(f'\nO produto dos números é: {produto} \n')
    elif opcao == 3:
        if numero_1 > numero_2:
            print(f'\nO maior entre os número digitados é o : {numero_1} \n')
        elif numero_2 > numero_1:
            print(f'\nO maior entre os número digitados é o : {numero_2} \n')
        else:
            print('\nO números digitados são iguais \n')
    elif opcao == 4:
        print('\nDigite os novos números:')
        numero_1 = int(input('Digite o primeiro número inteiro: '))
        numero_2 = int(input('Digite o segundo número inteiro: '))

# Exibe a mensagem de que indica a saída do programa
print('Programa encerrado!')