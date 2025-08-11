# Crie um programa que leia sexo e idade de várias pessoas
# A cada pessoa cadastrada, o programa deve perguntar se o usuário quer continuar
# Ao final o programa deve exibir:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

# Inicializa as variáveis globais
contador_maiores = 0
contador_homens = 0
contador_mulheres = 0

# Laço while infinito com condição de parada de escolha do usuário
while True:
    # Lê e valida sexo e idade da pessoa cadastrada
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Qual o sexo dessa pessoa? \n'
                     '[M] Masculino \n'
                     '[F] Feminino \n'
                     'Digite a opção: ')).upper().strip()
    while sexo not in ['M', 'F']:
        print('Opção inválida! Tente novamente..')
        sexo = str(input('Qual o sexo dessa pessoa? \n'
                         '[M] Masculino \n'
                         '[F] Feminino \n'
                         'Digite a opção: ')).upper().strip()

    # Realiza os teste lógicos para contabilizar as pessoas conforme os parâmetros
    if idade > 18:
        contador_maiores += 1
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_mulheres += 1

    # Pergunta ao usuário se o mesmo deseja continuar e valida a resposta
    escolha = str(input('Deseja cadastrar mais pessoas? \n'
                      '[S] Sim! \n'
                      '[N] Não. \n')).upper().strip()
    while escolha not in ['S', 'N']:
        print('Opção inválida! Tente novamente..')
        escolha = str(input('Deseja cadastrar mais pessoas? \n'
                          '[S] Sim! \n'
                          '[N] Não. \n')).upper().strip()

    # Quebra ou mantém o laço conforme a opção do usuário
    if escolha == 'N':
        break
    else:
        print('Vamos cadastrar mais pessoas!')

# Exibe os resultados dos contadores ao usuário
print('Vamos exibir os resultados das pessoas cadastradas:')

# Realiza os testes lógicos para exibir o resultado conforme a quantidade
# Maiores de Idade
if contador_maiores == 0:
    print('Nenhuma pessoa maior de idade foi cadastrada..')
elif contador_maiores == 1:
    print('Apenas 1 pessoa maior de idade foi cadastrada.')
else:
    print(f'No total {contador_maiores} maiores de idade foram cadastrados')

# Homens cadastrados
if contador_homens == 0:
    print('Nenhum homem foi cadastrado..')
elif contador_homens == 1:
    print('Apenas 1 homem foi cadastrado.')
else:
    print(f'No total {contador_homens} homens foram cadastrados')

# Mulheres menores
if contador_mulheres == 0:
    print('Nenhuma mulher menor de idade foi cadastrada..')
elif contador_mulheres == 1:
    print('Apenas 1 mulher menor de idade foi cadastrada.')
else:
    print(f'No total {contador_mulheres} mulheres menores de idade foram cadastrados')
