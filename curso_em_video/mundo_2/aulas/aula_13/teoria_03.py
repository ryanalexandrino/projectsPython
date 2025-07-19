# Estrutura de Repetição
# Trabalhando variavis e operações dentro do laço for

#Declara a variavel "soma" como global
soma = 0

# Soma de todos os valores de um laço for
for c in range(0, 3):
    numero = int(input('Digite um número inteiro: '))
    soma += numero
print(f'A soma de todos os número digitados é: {soma}')