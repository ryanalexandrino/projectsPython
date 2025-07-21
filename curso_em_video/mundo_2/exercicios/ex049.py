# Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher
# Utilizando o laço for

# Lê o número do usuário
numero = int(input('Digite um número inteiro: '))

# Mostra a tabuada até o 10 com um laço for
print(f'TABUADA DO NÚMERO {numero}!')

for c in range(1, 11):
    print(f'{numero} x {c}: {numero * c}')
print('FIM!')