# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa deve perguntar o valor da casa, o sálario do comprador e em quantos anos irá pagar
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do sálario
# Caso excede o empréstimo é negado

# Lê o valor da casa, o sálario e tempo de financiamento
valor_casa = float(input('Insira o valor da casa que deseja comprar: '))
salario = float(input('Insira o seu sálario bruto: '))
financiamento = int(input('Insira em quanto anos pretende pagar o imóvel: '))

# Calcula o valor da parcela
prestacao = valor_casa / (financiamento * 12)

# Cria uma condicional para validar a aprovação do empréstimo
if salario * 0.30 < prestacao:
    print('Infelizmente seu empréstimo foi negado..')
else:
    print(f'O seu empréstimo foi aprovado, com prestações no valor de R${prestacao:.2f}')
