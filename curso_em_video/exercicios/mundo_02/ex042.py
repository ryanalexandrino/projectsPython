# Desenvolva um programa que leia o comprimento de três retas
# Diga ao usuário se elas podem ou não formar um triangulo

# Lê as retas do usuário
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

# Condicional que verifica se as retas podem formar um triangulo
if a + b > c and a + c > b and b + c > a:
    print(f'Os lados digitados ({a}, {b}, {c}) podem sim formar um triangulo!')
    # Verifica qual o tipo triangulo
    if a == b == c:
        print(f'Esse triangulo é equilátero!')
    elif a != b != c:
        print(f'Esse triangulo é escaleno!')
    else:
        print(f'Esse triangulo é isósceles!')
else:
    print(f'Os lados digitados ({a}, {b}, {c}) não podem formar um triangulo!')
