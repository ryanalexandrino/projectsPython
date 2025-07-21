# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# Ao final, mostre os 10 primeiros termos dessa progressão

# Lê o primeiro termo e a razão da PA
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))

# Calcula a progressão com base nos termos inseridos
print('Com base nos valores inseridos, os 10 primeros termos são:')
for c in range(1, 11):
    an = a1 + (c - 1) * r
    print(f'{c}º Termo - {an}')