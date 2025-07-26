# Estrutura de repetição com teste lógico
# Laço de repetição com estrutura condicional

# Define as variáveis globais
n = 1
total = 0
par = impar = 0

# Cria a estrutura de repetição while
while n != 0:
    n = int(input('Digite um valor: '))
    total += 1
    # Testa se é par ou impar, sem contar o zero!
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

# Exibe os totais ao usuário
print(f'Fim! \n'
      f'O laço terminou porque você digitou o número 0! \n'
      f'Você digitou {total} ao todo, sendo {par} pares e {impar} impares!')