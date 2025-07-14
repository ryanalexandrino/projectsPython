# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes a letra "A" aparece
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

# Lê a frase do usuário
frase = str(input('Digite uma frase abaixo: \n')).upper().strip()

# Analisa a frase
conta_a = frase.count('A')
primeiro_a = frase.find('A')
ultimo_a = frase.rfind('A')

# Exibe as análise da frase
print(f'A letra "A" aparece {conta_a} vezes! \n'
      f'A primeira vez que a letra "A" aparece é na posição: {primeiro_a} \n'
      f'A última vez que a letra "A" aparece é na posição: {ultimo_a}')
