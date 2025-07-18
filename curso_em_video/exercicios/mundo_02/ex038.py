# Escreva um programa que leia dois números inteiros
# Compare esses números e mostre a seguinte mensagem na tela
# O primeiro é maior
# O segundo é maior
# Não existe valor maior, os números são iguais

# Lê os números do usuário
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

# Cria uma condicional aninhada que compara e exibe a comparação ao usuário
if n1 > n2:
    print(f'O primeiro número ({n1}) é maior que o segundo número ({n2})')
elif n2 > n1:
    print(f'O segundo número ({n2}) é maior que o primeiro número ({n1})')
else:
    print('Não existe número maior, os dois são iguais!')
