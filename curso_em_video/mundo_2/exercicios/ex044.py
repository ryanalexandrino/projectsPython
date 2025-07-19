# Elabore um programa que calcule o valor a ser pago por um produto
# Considere seu preço normal e a condição de pagamento:
# A vista em dinheiro - 10% de desconto
# A vista no cartão - 5% de desconto
# Em até 2x no cartão - Preço normal
# 3x ou mais no cartão - 20% de juros

# Lê o valor a ser pago no produto:
valor_produto = float(input('Digite o valor do produto: '))

# Lê a condição de pagamento
print('Selecione qual a forma de pagamento: \n'
      '1 - A vista em dinheiro (10% de desconto) \n'
      '2 - A vista no cartão (5% de desconto) \n'
      '3 - Em 2x no cartão (preço normal, sem descontos) \n'
      '4 - Em 3x ou mais no cartão (20% de juros)')
condicao = int(input('Digite a condição de pagamento: '))

# Condicional aninahada que calcula o valor a ser pago com base na condição de pagamento
if condicao == 1:
    valor_final = valor_produto - (valor_produto * 10 / 100)
    print(f'Você selecionou pagamento a vista em dinheiro! \n'
          f'O valor total do produto (com 10% de desconto) é de R${valor_final:.2f}')
elif condicao == 2:
    valor_final = valor_produto - (valor_produto * 5 / 100)
    print(f'Você selecionou pagamento a vista no cartão! \n'
          f'O valor total do produto (com 5% de desconto) é de R${valor_final:.2f}')
elif condicao == 3:
    print(f'Você selecionou pagamento em 2x no cartão! \n'
          f'O valor total do produto (sem qualquer alteração) é de R${valor_produto:.2f} \n'
          f'Será pago em parcelas de R${valor_produto / 2:.2f}')
elif condicao == 4:
    vezes = int(input('Em quantas vezes você deseja parcelar? '))
    valor_final = valor_produto + (valor_produto * 20 / 100)
    print(f'Você selecionou pagamento em {vezes}x no cartão! \n'
          f'O valor total do produto (com 20% de juros) é de R${valor_final:.2f} \n'
          f'Será pago em parcelas de R${valor_final / vezes:.2f}')
else:
    print('Condição inválida. Tente novamente!')