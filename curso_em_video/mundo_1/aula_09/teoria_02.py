# Manipulação de Texto
# Conceito de Análise

#Importa módulo para uso do count
import itertools

# Cria uma frase para análise
frase = str('Você não possui inimigos Thorfin.. ninguém possui.')

# Analisa o cumprimento da frase com "len"
cumprimento = len(frase)
print(cumprimento)

# Conta quantos elementos especificados a frase possui com "count"
letras_t = frase.count('T')
print(letras_t)

# Conta quantos elementos especificados dentro de um intervalo da frase com "count"
letras_a = frase.count('s', 0,14)
print(letras_a)

# Encontra o começo da posição de um ou mais elementos especificos com "find"
encontar_thor = frase.find('Thor')
print(encontar_thor)

# Retorna booleano por comparação com o operador "in"
inimigos = 'inimigos' in frase
print(inimigos)



