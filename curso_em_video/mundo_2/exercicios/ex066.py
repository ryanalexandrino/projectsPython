# Crie um programa que leia vários números, só parando depois da inserção do valor 999
# Ao final mostre a quantidade de números digitados e a soma desses números

# Inicializa as variáveis globais
soma = 0
contador = 0

# Laço while infinito com condição de parada 999
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    else:
        soma += numero
        contador += 1

# Exibe o resultado ao usuário
if contador == 0:
    print('Nenhum número com exceção da flag foi digitado..')
else:
    print(f'Foram digitados {contador} números no total! \n'
          f'A soma desses números é igual a {soma}.')