# Manipulação de Texto
# Conceito de Transformação

# Cria uma frase para manipulação
frase = str('Você não possui inimigos Thorfin.. Ninguém possui.')

# Troca cadeia de string especificada com "replace"
troca = frase.replace('Thorfin','Einar')
print(troca)

# Transforma todas as strings em maisculas com "upper"
maisculas = frase.upper()
print(maisculas)

# Transforma todas as string em minusculas com "lower"
minusculas = frase.lower()
print(minusculas)

# Transforma apenas a primeira da frase de cada palavra em maisculas com "capitalize"
capitalizado = frase.capitalize()
print(capitalizado)

# Transforma a primeira letra de cada palavra em maiscula com "title"
titularizado = frase.title()
print(titularizado)

# Elimina espaço antes e depois de uma cadeia de string com "strip"
eliminar_espaços = frase.strip()
print(eliminar_espaços)