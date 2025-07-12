# Manipulação de Texto
# Conceito de Fatiamento

# Cria uma frase para manipulação
frase = str('Você não possui inimigos Thorfin.. ninguém possui.')

# Fatia apenas uma string, conforme o índice
letra_t = frase[25]
print(letra_t)

# Fatia uma sequencia referenciada de índices
fatia_sequencial1 = frase[0:34]
fatia_sequencial2 = frase[35:52]
print(fatia_sequencial1)
print(fatia_sequencial2)

# Fatia ignorando um número de índices referenciado
fatia_csalto = frase[25:32:3]
print(fatia_csalto)