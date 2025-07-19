# Faça um programa que leia o nome completo de uma pessoa
# E mostre separadamente, o primeiro e o ultimo nome

# Lê o nome completo da pessoa
nome = str(input('Digite seu nome completo: ')).strip()

# Divide o nome com split
nome_separado = nome.split()

# Encontra o último nome
ultimo_nome = len(nome_separado) - 1

# Exibe o primeiro e o último nome
print(f'Seu primeiro nome é {nome_separado[0]} \n'
      f'Seu último nome é {nome_separado[ultimo_nome]}')
