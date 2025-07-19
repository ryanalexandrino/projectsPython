# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# Lê o número do usuário
numero = int(input('Digite um número inteiro de 4 dígitos: '))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

# Converte esse número para string
numero_str = str(numero)

# Exibe separadamente cada dígito do número como int
print(f'O número digitado (como int) pode ser interpretado da seguinte maneira: \n'
      f'Milhares: {milhar} \n'
      f'Centenas: {centena} \n'
      f'Dezenas : {dezena} \n'
      f'Unidades: {unidade}')

# Exibe separadamente cada dígito do número como string
print(f'O número digitado (como string) pode ser interpretado da seguinte maneira: \n'
      f'Milhares: {numero_str[0]} \n'
      f'Centenas: {numero_str[1]} \n'
      f'Dezenas : {numero_str[2]} \n'
      f'Unidades: {numero_str[3]}')
