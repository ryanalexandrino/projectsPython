# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# Lê o número do usuário como string
numero = str(input('Digite um número inteiro de 4 dígitos: '))

# Exibe separadamente cada dígito do número
print(f'O número digitado (como string) pode ser interpretado da seguinte maneira: \n'
      f'Milhares: {numero[0]} \n'
      f'Centenas: {numero[1]} \n'
      f'Dezenas : {numero[2]} \n'
      f'Unidades: {numero[3]}')

# Lê o número do usuário como int
numero = int(input('Digite um número inteiro de 4 dígitos: '))
