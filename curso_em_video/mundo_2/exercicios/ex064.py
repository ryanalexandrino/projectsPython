# Crie um programa que leia vários números inteiros
# O programa deve parar quando o usuário digitar o valor "999"
# Ao final mostre quantos números foram digitados e a soma deles
# Desconsidere o valor 999 nos dois casos

# Inicializa as variáveis globais
contador = 0
soma = 0
numero = int(input('Digite um número: '))

# Cria o laço que executa o programa
while numero != 999:
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
print(f'\nO programa foi encerrado devido a inserção do valor "999"! \n'
      f'Você digitou um total de {contador} números \n'
      f'A soma desses número é igual a: {soma}')