# Crie um programa que leia uma frase e diga se ela é um palindromo

# Lê a frase do usuário sem espaços
frase = str(input('Digite uma frase qualquer!')).strip()
cumprimento_frase = len(frase)

# Cria a variavel palindromo como global
palindromo = bool

# Teste se a frase é um palindromo
for c in range (0, cumprimento_frase-1):
    if cumprimento_frase - c == frase[c]:
        palindromo = True
    else:
        palindromo = False


