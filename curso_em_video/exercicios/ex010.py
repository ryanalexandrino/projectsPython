# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

# Pede o valor em carteira ao usuário
reais = float(input('Digite o valor que você possue em sua carteira: '))

# Converte e exibe a quantidade de dolares que o usuário pode comprar
print(f'Com o valor de R$ {reais:.2f}, você pode comprar um total de $ {reais/5.46:.2f} dolares americanos \n'
      f'Valor c alculado em 01/07/2025)')