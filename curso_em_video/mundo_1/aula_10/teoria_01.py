# Condições
# Estruturas Condicionais simples e compostas

# Lê a idade do carro do usuário
ano = int(input('Qual o ano do seu carro? '))

# Cria uma estrutura condiconal composta para para analisar o carro
if ano >= 2022:
    print('Ah entendi! Seu carro é um pouco mais novo!')
else:
    print('Ah entendi! Seu carro é um pouco mais antigo..')

# Cria uma estrutura condicional simplificada para analisar o carro
tempo = int(input('A quantos anos você possui esse carro'))
print('É um carro novo!' if tempo <= 3 else 'É um carro um  antigo!')