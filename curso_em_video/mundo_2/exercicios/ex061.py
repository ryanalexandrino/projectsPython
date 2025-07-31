# Refaça o desafio 51 lendo o primeiro termo e a razão
# Ao final, mostre os 10 primeiros termos dessa progressão
# Use a estrutura while

# Lê o primeiro termo e a razão da PA
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
t = a1
contador = 1
print('Com base nos valores inseridos, os 10 primeros termos são:')

# Calcula a progressão com base nos termos inseridos usando o while
while contador <= 10:
    print(f'{t} → ', end='')
    t += r
    contador += 1
print('FIM!')
