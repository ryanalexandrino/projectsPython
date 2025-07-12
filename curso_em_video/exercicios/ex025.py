# Crie um programa o nome de uma pessoa e diga se ela tem "SILVA" no nome

# Lê o nome completo da usuária
nome = str(input('Digite seu nome completo: '))

# Verifica se o nome possui "SILVA"
nome_silva = "SILVA" in nome.upper()

# Exibe se o nome é silva ou não
if nome_silva:
    print(f'O nome possui sim "SILVA"!')
else:
    print(f'O nome não possui "SILVA"!')
