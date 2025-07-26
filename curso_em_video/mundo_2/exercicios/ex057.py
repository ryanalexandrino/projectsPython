# Faça um programa que leia o sexo de uma pessoa
# Só aceite valores M ou F
# Caso esteja errado peça a digitação de novo até ter um valor correto

# Cria "sexo'como variável global
sexo = ''

# Cria a estrutura de repetição while par perguntar qual o sexo do usuário
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nQual o seu sexo? \n'
                     '[M] Masculino \n'
                     '[F] Feminino \n'
                     'Digite a opção: '))

    if sexo != 'M' and sexo != 'F':
        print('Entrada inválida! Tente novamente.')

# Exibe uma mensagem ao usuário, indicando a saída do laço
if sexo == 'M':
    print('\nEntendi, você é um homem!')
else:
    print('\nEntendi, você é uma mulher!')
