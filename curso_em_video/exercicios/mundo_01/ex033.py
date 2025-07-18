# Faça um programa que leia 3 números e diga qual o maior e qual o menor

# Lê os número do usuário
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Cria uma condicional para verificar qual o maior número e o exibir
if n1 > n2 and n1 > n3:
    print(f'\nO maior número digitado foi: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'\nO maior número digitado foi: {n2}')
else:
    print(f'\nO maior número digitado foi: {n3}')

# Cria uma condicional para verificar qual o menor número e o exibir
if n1 < n2 and n1 < n3:
    print(f'O menor número digitado foi: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número digitado foi: {n2}')
else:
    print(f'O menor número digitado foi: {n3}')