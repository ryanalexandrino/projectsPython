# Estrutura de repetição com teste lógico
# Cria um laço com condição de parada do tipo int
n = 1
while n != 0:
    n = int(input('Digite um número inteiro: '))
print('Fim! \n'
      'O laço terminou porque você digitou o número 0!\n')

# Cria um laço com condição de parada do tipo str
r = 'S'
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Deseja continuar? \n'
                  '[S] Sim \n'
                  '[N] Não \n'
                  'Digite a opção: ')).upper()
print('Fim! O laço terminou porque você digitou uma resposta diferente de "Sim"!\n')
