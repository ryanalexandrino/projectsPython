 # Escreva um programa que leia um número inteiro e peça para o usuário escolher a base de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

# Lê o número do usuário
numero = int(input('Digite um número inteiro: '))

# Pergunta ao usuário qual a base de conversão será realizada
print(f'Escolha qual a base de conversão deve ser utilizada para converter esse número! \n'
      f'1 - Base Binária \n'
      f'2 - Base Octal \n'
      f'3 - Base Hexadecimal ')
escolha = int(input('Digite a opção desejada: '))

# Cria uma condicional aninhada que converte o número conforme a base escolhida anteriorment
if escolha == 1:
    print(f'\nNúmero convertido em Binário: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'\nNúmero convertido em Octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'\nNúmero convertido em Hexadecimal: {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente!')


