# Crie um programa que leia o nome de uma cidade e diga se ela começa com nome "Santo"

# Lê o nome da cidade do usuário
cidade = str(input('Digite o nome de uma cidade: '))

# Divide a string cidade digitada
primeiro_cidade = cidade.split()

# Analisa se a cidade possui a palavra "SANTO"
cidada_santa = "SANTO" in primeiro_cidade[0].upper()

# Exibe a mensagem ao usuário através de uma condicional, conforme retorno da análise
if cidada_santa:
    print(f'\nA cidade {cidade} possui a primeria palavra "SANTO"!')
else:
    print(f'\nA cidade {cidade} não possui a primeria palavra "SANTO"!')