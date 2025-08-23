# Tuplas + Laços de repetição

# Cria uma tupla que representa um combo de um lanche
lanche = ('Hambúrguer', 'Batata frita', 'Refrigerante', 'Milk Shake')

# Laço de repetição que mostar os elementos dentro da tupla
print('Meu combo é formato por:')
for comida in lanche:
    print(f'1x {comida}')

# Laço de repetição que usa o comprimento de uma tupla como argumento do range
print('\nContando os elementos de lanche')
for cont in range(0, len(lanche)):
    print(f'Elemento de lanche: {cont}')

# Método alternativo de exibir elementos de uma tupla
print('\nMeu combo é formato por:')
for cont in range(0, len(lanche)):
    print(f'1x {lanche[cont]}')
