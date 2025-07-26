# Crie um programa que leia uma frase e diga se ela é um palindromo

# Metodo com laço de repetição
# Lê a frase do usuário sem espaços
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
palavras_juntas = ''.join(palavras)
inverso = ''
cumprimento_frase = len(palavras_juntas)

# Cria um laço que inverte a frase
for c in range (cumprimento_frase - 1, -1, -1):
    inverso += palavras_juntas[c]

# Condicional que compara a frase original e a frase invertida
if inverso == palavras_juntas:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

# Metodo com fatiamento de string, exclusivo do Python
# Lê a frase do usuário sem espaços
frase = str(input('\nDigite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
palavras_juntas = ''.join(palavras)
inverso = palavras_juntas[::-1]

# Condicional que compara a frase original e a frase invertida
if inverso == palavras_juntas:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
