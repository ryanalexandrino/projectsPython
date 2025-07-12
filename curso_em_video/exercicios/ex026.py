# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes a letra "A" aparece
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

# Lê a frase do usuário
frase = str(input('Digite uma frase abaixo: \n'))

# Analisa a frase
conta_a = frase.count('A')
primeiro_a = frase.find('A')
ultima_frase = frase.rfind('A')

# Exibe as análise da frase
print(f'A letra "A" aparece {conta_a} vezes! \n'
      f'A primeira vez que a letra "A" aparece é na posição: {primeiro_a} \n'
      f'A última vez que a letra "A" aparece é na posição: {ultima_frase}')



