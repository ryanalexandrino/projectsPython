# Desenvolva um programa que leia seis números inteiros
# E mostre a soma apenas daqueles que são pares

# Declara a varivel soma como global
soma = 0

# Lê os números dos usuários e verifica e soma  se eles são pares
for c in range (0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
# Mostra a soma dos números ao usuário
print(f'A soma dos números pares digitados é {soma}')