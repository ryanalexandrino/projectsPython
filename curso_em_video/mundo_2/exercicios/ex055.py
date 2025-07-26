# Faça um programa que leia o peso de cinco pessoas
# No final mostre o maior e menor peso lidos

# Define as variáveis globais
menor_peso = 0
maior_peso = 0

# Cria um laço que lê o peso das pessoas e determina as máximas
for c in range (1,6):
    peso = float(input(f'{c}. Digite o seu peso: '))
    if c == 1:
        menor_peso = maior_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

# Exibe as máximas ao usuário
print(f'\nDos pesos digitados, as máximas foram: \n'
      f'Maior peso: {maior_peso} Kg \n'
      f'Menor peso: {menor_peso} Kg')
