# Faça um programa que leia um número e mostre o seu fatorial

# Lê o número do usuário
n = int(input('Digite um número: '))
fatorial = 1

# Exibe o inicio do fatorial
print(f'O resultado de {n} fatorial é: \n'
      f'{n}! = ', end='')

# Cria um laço while que calcula o fatorial
while n > 0:
    # Calcula o fatorial
    fatorial = n * fatorial
    # Ajusta o print do calculo
    if n > 1:
        print(f'{n} x ', end='')
    else:
        print(n, end=' ')
    # Diminui o número para o próximo calculo
    n = n-1

# Exibe o resultado final do fatorial
print(f'= {fatorial}')
