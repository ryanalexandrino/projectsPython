# Faça um programa que calcule a soma de todos os números impares que são múltiplos  de 3
# Que se encontram no intervalo de 1 a 500

# Declara a soma como varíavel global
soma = 0
contador = 0

# Cria o laço que realiza a soma sob uma condicional e a exibe
for c in range(1, 501, 2):
    if c %3 == 0:
        contador += 1
        soma += c
print(f'A soma de todos os {contador} números é: {soma}!')